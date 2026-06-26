"""pymupdf4llm parser — rich markdown from PDFs (headings, tables, lists).

Page-aware: when pymupdf4llm can't render an embedded figure, it inlines a
``==> picture [...] intentionally omitted`` marker plus the figure's flattened
text. Such pages are flagged in ``meta["vision_pages"]`` (1-based) so the engine
renders them to PNG and routes them to Claude vision — the figure is a real
diagram that text-diagram detection cannot recover.
"""

from __future__ import annotations

import importlib

from ..figures import picture_omitted_pages
from .base import ExtractionResult, LibraryParser


class Pymupdf4llmParser(LibraryParser):
    name = "pymupdf4llm"
    module_name = "pymupdf4llm"
    extensions = (".pdf",)

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        try:
            pymupdf4llm = importlib.import_module("pymupdf4llm")
        except Exception as exc:
            return ExtractionResult(
                text="", parser=self.name, warnings=[f"pymupdf4llm failed: {exc}"]
            )

        # Prefer page_chunks so we can map picture-omission markers to pages.
        page_texts: dict[int, str] = {}
        try:
            chunks = pymupdf4llm.to_markdown(source, page_chunks=True)
        except Exception:
            chunks = None

        if isinstance(chunks, list) and chunks:
            parts: list[str] = []
            for chunk in chunks:
                if isinstance(chunk, dict):
                    t = chunk.get("text") or ""
                    meta = chunk.get("metadata") or {}
                    pg = meta.get("page_number")
                    if isinstance(pg, int):
                        page_texts[pg] = t
                else:
                    t = str(chunk) if chunk else ""
                if t:
                    parts.append(t)
            text = "\n\n".join(parts).strip()
        else:
            # Fallback: single-string form (no page attribution available).
            try:
                text = pymupdf4llm.to_markdown(source)
            except Exception as exc:
                return ExtractionResult(
                    text="", parser=self.name, warnings=[f"pymupdf4llm failed: {exc}"]
                )
            if not isinstance(text, str):
                text = str(text) if text else ""

        meta: dict = {}
        vision_pages = picture_omitted_pages(page_texts)
        if vision_pages:
            meta["vision_pages"] = vision_pages

        return ExtractionResult(text=(text or "").strip(), parser=self.name, meta=meta)