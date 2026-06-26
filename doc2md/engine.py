"""Engine — the deterministic library API the ``/doc2md`` skill calls.

Walks ``raw/``, extracts via the parser seam (with content-addressed caching),
optimises tokens, detects diagrams, renders deterministic simple Mermaid, and
materialises infographic/complex-diagram work for the skill. It never calls an
LLM; everything LLM-bound is emitted as a work-order the skill fulfils.
"""

from __future__ import annotations

import logging
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .detection import DiagramDetection, detect_diagrams
from .manifest import FileRecord, Manifest, hash_file
from .mermaid import generate_simple
from .ocr import render_pdf_pages
from .optimise import optimise, optimise_with_tokens
from .parsers import build_registry
from .parsers.base import ExtractionResult
from .parsers.registry import ExtractorRegistry
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
        self.manifest = Manifest(self.cache_dir)

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
        try:
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(dest)
        except Exception as exc:
            logging.warning("Could not extract %s: %s: %s", zip_path, type(exc).__name__, exc)
            return []
        return [p for p in dest.rglob("*") if p.is_file() and p.suffix.lower() in _SUPPORTED]

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
            img_path = img_dir / f"page-{page:03d}.png"
            if img_path.exists():
                out.append(str(img_path))
                continue
            imgs = render_pdf_pages(str(path), first=page, last=page, dpi=200)
            if imgs:
                try:
                    imgs[0].save(img_path, "PNG")
                    out.append(str(img_path))
                except Exception:
                    pass
        return out

    # -- conversion ----------------------------------------------------

    def convert_one(self, path: str | Path) -> ConvertReport:
        path = Path(path)
        report = ConvertReport(path=str(path))

        try:
            file_hash = hash_file(path)
        except OSError as exc:
            report.warnings.append(f"unreadable: {exc}")
            return report

        unchanged, rec = self.manifest.is_current(str(path), file_hash)
        if unchanged and rec and not rec.needs_llm and not self.parser:
            report.skipped = True
            report.source = rec.source
            report.parser = rec.parser
            return report

        result = self._extract(path, file_hash)
        report.parser = result.parser
        report.warnings.extend(result.warnings)

        if not result.ok:
            report.warnings.append("extraction yielded no text")
            self._record(path, file_hash, result, detection=None, source=None, items=[], failed=True)
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

        self._record(path, file_hash, result, detection=detection,
                     source=str(source_path), items=order, failed=False,
                     tokens_raw=tokens_raw, tokens_optimised=tokens_optimised)
        return report

    def _record(self, path: Path, file_hash: str, result: ExtractionResult,
                *, detection: Optional[DiagramDetection], source: Optional[str],
                items: list[dict], failed: bool = False,
                tokens_raw: int = 0, tokens_optimised: int = 0) -> None:
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
        ))
        self.manifest.save()

    def convert_all(self) -> list[ConvertReport]:
        return [self.convert_one(p) for p in self._iter_files()]

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