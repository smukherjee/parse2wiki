"""Engine — the deterministic library API the ``/doc2md`` skill calls.

Walks ``raw/``, extracts via the parser seam (with content-addressed caching),
optimises tokens, detects diagrams, renders deterministic simple Mermaid, and
materialises infographic/complex-diagram work for the skill. It never calls an
LLM; everything LLM-bound is emitted as a work-order the skill fulfils.
"""

from __future__ import annotations

import logging
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .detection import DiagramDetection, detect_diagrams
from .finance import VerificationReport, compare_extractors, is_financial
from .manifest import FileRecord, Manifest, hash_file
from .mermaid import generate_simple
from .ocr import render_pdf_pages
from .optimise import optimise, optimise_with_tokens
from .parsers import build_registry
from .parsers.base import ExtractionResult
from .parsers.registry import ExtractorRegistry
from .figures import graphic_dense_pages, image_dominant_pages
from .writer import WorkItem, apply_work, build_source, write_work_order

_SUPPORTED = {".pdf", ".docx", ".pptx", ".xlsx", ".doc", ".odt",
              ".html", ".htm", ".csv", ".md", ".txt",
              ".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp", ".gif"}


@dataclass
class ConvertReport:
    path: str
    source: Optional[str] = None
    work_order: Optional[str] = None
    items: list[dict] = field(default_factory=list)
    parser: str = ""
    needs_llm: bool = False
    skipped: bool = False
    warnings: list[str] = field(default_factory=list)
    verification: Optional[VerificationReport] = None


class Engine:
    def __init__(
        self,
        raw_dir: str | Path,
        sources_dir: str | Path,
        cache_dir: str | Path | None = None,
        *,
        registry: Optional[ExtractorRegistry] = None,
        ocr: bool = True,
        parser: str | None = None,
        finance: Optional[bool] = None,
        vision_dpi: int = 150,  # P7: lower default cuts vision tokens ~30%
        max_image_dim: int = 1024,  # cap longest edge — keeps 7-image batches under API limit
        mineru: bool = False,  # force MinerU for every PDF (overrides parser chain)
    ) -> None:
        self.raw_dir = Path(raw_dir)
        self.sources_dir = Path(sources_dir)
        self.cache_dir = Path(cache_dir) if cache_dir else self.sources_dir.parent / ".doc2md-cache"
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.sources_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.registry = registry or build_registry()
        self.ocr = ocr
        self.parser = parser
        self.finance = finance  # True=force, False=disable, None=auto-detect
        self.vision_dpi = vision_dpi  # P7
        self.max_image_dim = max_image_dim
        if mineru:
            self.parser = "mineru"
            # Warn eagerly so the user sees the install hint before waiting for convert_all
            p = self.registry.parsers.get("mineru")
            if p is not None and not p.available:
                from .parsers.mineru import _INSTALL_HINT
                logging.warning("MinerU requested but not available.\n%s", _INSTALL_HINT)
        self.manifest = Manifest(self.cache_dir)
        self._batch_mode = False  # P4: suppresses per-file saves during convert_all

    # -- discovery -----------------------------------------------------

    def _iter_files(self) -> list[Path]:
        files: list[Path] = []
        for p in sorted(self.raw_dir.rglob("*")):
            if not p.is_file():
                continue
            ext = p.suffix.lower()
            if ext == ".zip":
                files.extend(self._expand_zip(p))
            elif ext in _SUPPORTED:
                files.append(p)
        return files

    def _expand_zip(self, zip_path: Path) -> list[Path]:
        dest = self.cache_dir / "unzipped" / zip_path.stem
        dest.mkdir(parents=True, exist_ok=True)

        # P5: skip re-extraction when zip content is unchanged
        marker = dest / ".extracted"
        try:
            zip_hash = hash_file(zip_path)
        except OSError:
            zip_hash = None

        if zip_hash and marker.exists() and marker.read_text().strip() == zip_hash:
            return [
                p for p in dest.rglob("*")
                if p.is_file() and p != marker and p.suffix.lower() in _SUPPORTED
            ]

        try:
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(dest)
            if zip_hash:
                marker.write_text(zip_hash)
        except Exception as exc:
            logging.warning("Could not extract %s: %s: %s", zip_path, type(exc).__name__, exc)
            return []
        return [
            p for p in dest.rglob("*")
            if p.is_file() and p != marker and p.suffix.lower() in _SUPPORTED
        ]

    def pending(self) -> list[Path]:
        """Files that (re)need conversion — hash-delta aware."""
        return [p for p in self._iter_files() if not self.manifest.has_unchanged(str(p))[0]]

    # -- extraction ----------------------------------------------------

    def _extract(self, path: Path, file_hash: str) -> ExtractionResult:
        """Extract, reusing the content-addressed cache (text + images + meta)."""
        primary = self.parser
        if primary is None:
            chain = self.registry.select(str(path))
            primary = chain[0].name if chain else None

        if primary is not None:
            cached = self.manifest.get_extraction(file_hash, primary)
            if cached is not None:
                return ExtractionResult(
                    text=cached.get("text", ""),
                    parser=primary,
                    images=cached.get("images", []),
                    meta=cached.get("meta", {}),
                )

        result = self.registry.extract(str(path), ocr=self.ocr, parser=self.parser)
        if result.ok:
            self.manifest.set_extraction(file_hash, result.parser, {
                "text": result.text,
                "images": result.images,
                "meta": result.meta,
            })
        return result

    # -- vision images -------------------------------------------------

    def _render_vision_pages(self, path: Path, file_hash: str, pages: list[int]) -> list[str]:
        out: list[str] = []
        if not pages:
            return out
        img_dir = self.cache_dir / "images" / file_hash
        img_dir.mkdir(parents=True, exist_ok=True)
        for page in pages:
            img_path = img_dir / f"page-{page:03d}.jpg"
            if img_path.exists() and self._image_within_dim_cap(img_path):
                out.append(str(img_path))
                continue
            # P7: use vision_dpi (default 150) — ~30% fewer tokens vs 200
            imgs = render_pdf_pages(str(path), first=page, last=page, dpi=self.vision_dpi)
            if imgs:
                try:
                    self._save_vision_image(imgs[0], img_path)
                    out.append(str(img_path))
                except Exception:
                    pass
        return out

    def _image_within_dim_cap(self, img_path: Path) -> bool:
        """True if the cached image fits within max_image_dim — avoids re-render."""
        try:
            from PIL import Image
            img = Image.open(img_path)
            return max(img.width, img.height) <= self.max_image_dim
        except Exception:
            return True  # can't read → assume ok, let the caller handle the error

    def _save_vision_image(self, img: "Image.Image", dest: Path) -> None:  # type: ignore[name-defined]
        """Resize if needed, then save as JPEG (smaller than PNG for typical slide/photo content)."""
        from PIL import Image
        if max(img.width, img.height) > self.max_image_dim:
            scale = self.max_image_dim / max(img.width, img.height)
            img = img.resize(
                (int(img.width * scale), int(img.height * scale)),
                Image.LANCZOS,
            )
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")
        img.save(dest, "JPEG", quality=85, optimize=True)

    # -- conversion ----------------------------------------------------

    def convert_one(
        self,
        path: str | Path,
        *,
        file_hash: str | None = None,  # P2: accept precomputed hash to avoid double-read
    ) -> ConvertReport:
        path = Path(path)
        report = ConvertReport(path=str(path))

        # P3: stat the file once for mtime+size tracking and fast-path
        mtime: float = 0.0
        size: int = 0
        try:
            st = path.stat()
            mtime, size = st.st_mtime, st.st_size
        except OSError:
            pass

        # P2: compute hash once; caller may supply precomputed value
        if file_hash is None:
            try:
                file_hash = hash_file(path)
            except OSError as exc:
                report.warnings.append(f"unreadable: {exc}")
                return report

        unchanged, rec = self.manifest.is_current(str(path), file_hash)
        if unchanged and rec and not rec.needs_llm and not self.parser:
            # Re-process PDFs whose page analysis predates raster-image detection (v2).
            # Extraction cache is reused; only the vision-routing heuristic re-runs.
            needs_reanalysis = (
                path.suffix.lower() == ".pdf"
                and self.manifest.get_page_analysis(file_hash) is None
            )
            if not needs_reanalysis:
                report.skipped = True
                report.source = rec.source
                report.parser = rec.parser
                return report

        result = self._extract(path, file_hash)
        report.parser = result.parser
        report.warnings.extend(result.warnings)

        if not result.ok:
            report.warnings.append("extraction yielded no text")
            self._record(path, file_hash, result, detection=None, source=None, items=[],
                         failed=True, mtime=mtime, size=size)
            return report

        opt_result = optimise_with_tokens(result.text)
        text = opt_result.text
        tokens_raw = opt_result.tokens_raw
        tokens_optimised = opt_result.tokens_optimised
        detection = detect_diagrams(text)
        simple_mermaid = generate_simple(detection, text, title=path.stem)

        work_items: list[WorkItem] = []
        if detection.complexity == "complex":
            work_items.append(WorkItem(
                id=f"{file_hash[:8]}-cm",
                kind="complex_mermaid",
                text=text,
                diagram_type=detection.diagram_type,
                cache_key=f"{file_hash}-complex",
                file_hash=file_hash,
            ))

        # Infographic image files → vision. Unique id per image.
        if result.meta.get("needs_vision") and result.images:
            for i, img in enumerate(result.images):
                work_items.append(WorkItem(
                    id=f"{file_hash[:8]}-img{i}",
                    kind="infographic",
                    text=result.text,
                    image=img,
                    cache_key=f"{file_hash}-vision",
                    file_hash=file_hash,
                ))

        # PDF pages flagged as figure-like → render & route to vision. Unique id per page.
        vision_pages = result.meta.get("vision_pages") or []
        # P1: if no vision_pages from parser, use pdfplumber graphic-density heuristic
        # — but cache the result so re-runs of needs_llm files skip the full PDF scan.
        if not vision_pages and path.suffix.lower() == ".pdf":
            cached_pages = self.manifest.get_page_analysis(file_hash)
            if cached_pages is None:
                cached_pages = graphic_dense_pages(str(path))
                if not cached_pages:
                    # Fallback for raster-only PDFs (screenshots, WhatsApp, scanned slides):
                    # zero vector elements fool graphic_dense_pages, but pdfplumber can
                    # enumerate the embedded raster images and measure their coverage.
                    cached_pages = image_dominant_pages(str(path))
                self.manifest.set_page_analysis(file_hash, cached_pages)
            vision_pages = cached_pages

        rendered_pages = self._render_vision_pages(path, file_hash, vision_pages)
        if vision_pages and not rendered_pages:
            # Don't silently drop a figure the parser asked us to look at.
            report.warnings.append(
                f"figure pages {vision_pages} flagged for vision but none rendered "
                "(pdf2image/poppler unavailable?); figure text kept as fallback"
            )
        for i, img in enumerate(rendered_pages):
            work_items.append(WorkItem(
                id=f"{file_hash[:8]}-pg{i}",
                kind="infographic",
                image=img,
                cache_key=f"{file_hash}-vision",
                file_hash=file_hash,
            ))

        # Reuse cached LLM output so re-runs spend zero tokens; fulfilled items
        # are inlined into the source instead of emitting an await marker.
        for item in work_items:
            cached = self.manifest.get_work(file_hash, item.id)
            if cached is not None:
                item.fulfilled = cached

        source_md, order = build_source(
            title=path.stem,
            result=ExtractionResult(text=text, parser=result.parser),
            detection=detection,
            simple_mermaid=simple_mermaid,
            work_items=work_items,
        )

        # Preserve subdirectory structure and original extension so files
        # with the same stem (e.g. report.pdf vs report.docx, or nested dirs)
        # do not overwrite each other.
        try:
            rel = path.relative_to(self.raw_dir)
            base = rel.with_suffix("")
        except ValueError:
            base = Path(path.stem)
        source_path = (self.sources_dir / base).with_suffix(f"{path.suffix}.md")
        source_path.parent.mkdir(parents=True, exist_ok=True)
        source_path.write_text(source_md)
        report.source = str(source_path)
        report.items = order
        report.needs_llm = any(item.fulfilled is None for item in work_items)

        if order:
            wo_path = self.cache_dir / "workorders" / f"{path.stem}.json"
            write_work_order(wo_path, order)
            report.work_order = str(wo_path)

        # Finance verification — auto-detect or explicit flag
        do_finance = self.finance
        if do_finance is None:
            do_finance = is_financial(result.text, path=path)
        if do_finance:
            verify = self.finance_verify_one(path, file_hash)
            report.verification = verify
            verify_path = source_path.with_suffix(".verify.json")
            verify.write(verify_path)
            for line in verify.summary_lines():
                report.warnings.append(line)

        self._record(path, file_hash, result, detection=detection,
                     source=str(source_path), items=order, failed=False,
                     tokens_raw=tokens_raw, tokens_optimised=tokens_optimised,
                     mtime=mtime, size=size)
        return report

    def _record(self, path: Path, file_hash: str, result: ExtractionResult,
                *, detection: Optional[DiagramDetection], source: Optional[str],
                items: list[dict], failed: bool = False,
                tokens_raw: int = 0, tokens_optimised: int = 0,
                mtime: float = 0.0, size: int = 0) -> None:
        complexity = detection.complexity if detection is not None else "none"
        self.manifest.upsert(FileRecord(
            original=str(path.resolve()),
            hash=file_hash,
            parser=result.parser,
            source=source,
            complexity=complexity,
            images=result.images,
            work_order=None,
            needs_llm=bool(items),
            failed=failed,
            tokens_raw=tokens_raw,
            tokens_optimised=tokens_optimised,
            mtime=mtime,
            size=size,
        ))
        # P4: skip per-file save in batch mode; convert_all saves once at end
        if not self._batch_mode:
            self.manifest.save()

    def convert_all(self, *, workers: int = 4) -> list[ConvertReport]:
        """Convert all files in raw_dir.

        P4: saves manifest once after all files (not N times).
        P6: parallelises extraction across files with a bounded thread pool.
        """
        files = self._iter_files()
        if not files:
            return []

        self._batch_mode = True
        ordered: list[Optional[ConvertReport]] = [None] * len(files)
        try:
            if workers > 1 and len(files) > 1:
                # P6: parallel extraction — I/O-bound, threads work under GIL
                with ThreadPoolExecutor(max_workers=workers) as pool:
                    # P2: precompute hashes in the pool too (avoids serial hash pass)
                    future_to_idx = {
                        pool.submit(self._convert_one_with_hash, p): i
                        for i, p in enumerate(files)
                    }
                    for fut in as_completed(future_to_idx):
                        idx = future_to_idx[fut]
                        try:
                            ordered[idx] = fut.result()
                        except Exception as exc:
                            ordered[idx] = ConvertReport(
                                path=str(files[idx]), warnings=[str(exc)]
                            )
            else:
                for i, p in enumerate(files):
                    ordered[i] = self._convert_one_with_hash(p)
        finally:
            self._batch_mode = False
            self.manifest.save()  # P4: single save for the entire batch

        return [r for r in ordered if r is not None]

    def _convert_one_with_hash(self, path: Path) -> ConvertReport:
        """P2: hash the file once here, pass into convert_one to avoid re-read."""
        try:
            fh = hash_file(path)
        except OSError:
            fh = None
        return self.convert_one(path, file_hash=fh)

    # -- finance verification ------------------------------------------

    def finance_verify_one(self, path: Path, file_hash: str) -> VerificationReport:
        """Run all available parsers on path, compare numeric figures across them."""
        results: dict[str, str] = {}
        for parser in self.registry.all_for(str(path)):
            cached = self.manifest.get_extraction(file_hash, parser.name)
            if cached is not None:
                results[parser.name] = cached.get("text", "")
            else:
                try:
                    res = parser.extract(str(path), ocr=self.ocr)
                except Exception as exc:
                    logging.warning("finance verify: %s failed on %s: %s", parser.name, path, exc)
                    continue
                if res.ok:
                    self.manifest.set_extraction(file_hash, parser.name, {
                        "text": res.text,
                        "images": res.images,
                        "meta": res.meta,
                    })
                    results[parser.name] = res.text
        return compare_extractors(results, document=str(path))

    # -- compare mode --------------------------------------------------

    def compare_one(self, path: str | Path) -> list[ConvertReport]:
        """Run every available parser on ``path``; one attributed source each."""
        path = Path(path)
        reports: list[ConvertReport] = []
        try:
            file_hash = hash_file(path)
        except OSError as exc:
            return [ConvertReport(path=str(path), warnings=[f"unreadable: {exc}"])]

        for parser in self.registry.all_for(str(path)):
            res = parser.extract(str(path), ocr=self.ocr)
            text = optimise(res.text) if res.ok else ""
            detection = detect_diagrams(text) if text else detect_diagrams("")
            simple = generate_simple(detection, text, title=path.stem) if text else ""
            source_md, _ = build_source(
                title=f"{path.stem} ({parser.name})",
                result=ExtractionResult(text=text or "(no text)", parser=parser.name),
                detection=detection,
                simple_mermaid=simple,
                work_items=[],
            )
            out = self.sources_dir / f"{path.stem}.{parser.name}.md"
            out.write_text(source_md)
            reports.append(ConvertReport(
                path=str(path), source=str(out), parser=parser.name,
                warnings=res.warnings,
            ))
        return reports

    # -- skill fulfilment ----------------------------------------------

    def apply_work(self, source_path: str | Path, fulfilled: dict[str, str]) -> None:
        """Splice the skill's Claude output into a source, cache it, then persist.

        Only clears ``needs_llm`` when no ``await`` markers remain (full fulfilment);
        cached work is written regardless, so a later full run reuses it.
        """
        p = Path(source_path)
        new_md = apply_work(p.read_text(), fulfilled)
        p.write_text(new_md)
        rec = self.manifest.mark_done(source_path) if "<!-- doc2md:await:" not in new_md else None
        if rec is not None:
            # Track LLM tokens (input = work item text, output = fulfilled content)
            tokens_llm_input = 0
            tokens_llm_output = 0
            try:
                import tiktoken
                enc = tiktoken.get_encoding("cl100k_base")
                for item_id, content in fulfilled.items():
                    tokens_llm_output += len(enc.encode(content))
                # Input tokens already counted in tokens_optimised; this is additional context
                # For simplicity, estimate input as 10% of output for diagram work
                tokens_llm_input = tokens_llm_output // 10
            except ImportError:
                pass
            # Update the record with LLM token counts
            rec.tokens_llm_input = tokens_llm_input
            rec.tokens_llm_output = tokens_llm_output
            self.manifest.save()
            for item_id, content in fulfilled.items():
                self.manifest.set_work(rec.hash, item_id, content)
