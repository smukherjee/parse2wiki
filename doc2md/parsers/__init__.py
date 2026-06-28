"""Parser package: build the registry from built-ins + entry-point discovery.

External parser packages register themselves via the ``doc2md.parsers``
entry-point group, each exposing a zero-arg constructor returning a Parser.
"""

from __future__ import annotations

from typing import Callable

from .base import Parser
from .registry import ExtractorRegistry, _DEFAULT_CHAINS


def _importlib_parsers() -> list[Parser]:
    """Built-in adapters (lazy import keeps optional deps out of startup)."""
    from .pdftotext import PdftotextParser
    from .pdfplumber import PdfplumberParser
    from .pymupdf4llm import Pymupdf4llmParser
    from .markitdown import MarkitdownParser
    from .docx import DocxParser
    from .pptx import PptxParser
    from .xlsx import XlsxParser
    from .pandoc import PandocParser
    from .image import ImageParser
    from .pdf_inspector import PdfInspectorParser
    from .undoc import UndocParser
    from .unpdf import UnpdfParser
    from .pdf_multilingual import MultilingualPDFParser
    from .mineru import MineruParser

    return [
        PdftotextParser(),
        PdfplumberParser(),
        Pymupdf4llmParser(),
        MarkitdownParser(),
        DocxParser(),
        PptxParser(),
        XlsxParser(),
        PandocParser(),
        ImageParser(),
        PdfInspectorParser(),
        UndocParser(),
        UnpdfParser(),
        MultilingualPDFParser(),
        MineruParser(),
    ]


def _discover_entry_points() -> list[Parser]:
    found: list[Parser] = []
    try:
        from importlib.metadata import entry_points
        eps = entry_points(group="doc2md.parsers")
    except Exception:
        return found
    for ep in eps:
        try:
            factory: Callable[[], Parser] = ep.load()
            found.append(factory())
        except Exception as exc:  # a broken external parser must not kill the registry
            found.append(_BrokenParser(ep.name, str(exc)))
    return found


class _BrokenParser:
    """Placeholder so a failed entry-point load is visible, not silent."""

    def __init__(self, name: str, reason: str) -> None:
        self.name = name
        self.reason = reason
        self.kinds = ("file",)

    @property
    def available(self) -> bool:
        return False

    def supports(self, source: str) -> bool:
        return False

    def extract(self, source: str, *, ocr: bool = False):
        from .base import ExtractionResult

        return ExtractionResult(text="", parser=self.name, warnings=[f"load failed: {self.reason}"])


def build_registry(chains: dict[str, list[str]] | None = None) -> ExtractorRegistry:
    parsers = _importlib_parsers() + _discover_entry_points()
    return ExtractorRegistry(parsers, chains=chains)


__all__ = ["build_registry", "ExtractorRegistry", "Parser", "_DEFAULT_CHAINS"]