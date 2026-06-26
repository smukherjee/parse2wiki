"""markitdown parser — Microsoft's multi-format → markdown converter.

A broad-coverage first-line parser for office formats; library-backed, so it
sits early in chains where richer structure isn't critical.
"""

from __future__ import annotations

import importlib

from .base import ExtractionResult, LibraryParser


class MarkitdownParser(LibraryParser):
    name = "markitdown"
    module_name = "markitdown"
    extensions = (".pdf", ".docx", ".pptx", ".xlsx", ".doc", ".odt", ".html", ".csv")

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        try:
            markitdown = importlib.import_module("markitdown")
            MarkItDown = getattr(markitdown, "MarkItDown")
            result = MarkItDown().convert(source)
        except Exception as exc:
            return ExtractionResult(
                text="", parser=self.name, warnings=[f"markitdown failed: {exc}"]
            )
        text = ""
        for attr in ("text_content", "markdown", "text"):
            content = getattr(result, attr, None)
            if isinstance(content, str) and content.strip():
                text = content
                break
        if not text and isinstance(result, str):
            text = result
        return ExtractionResult(text=(text or "").strip(), parser=self.name)