"""ExtractorRegistry — resolves a Parser (or fallback chain) for a source.

Built-in parsers register explicitly here; external parser packages register
via the ``doc2md.parsers`` entry-point group (discovered in
``parsers/__init__.py``). Chains are config-driven so a user can reorder or
force one parser to test accuracy.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .base import ExtractionResult, Parser

_DEFAULT_CHAINS: dict[str, list[str]] = {
    ".pdf": ["pdf-inspector", "unpdf", "pymupdf4llm", "pdfplumber", "pdftotext"],
    ".docx": ["undoc", "markitdown", "docx", "pandoc"],
    ".pptx": ["undoc", "markitdown", "pptx"],
    ".xlsx": ["undoc", "markitdown", "xlsx"],
    ".png": ["image"],
    ".jpg": ["image"],
    ".jpeg": ["image"],
    ".webp": ["image"],
    ".tif": ["image"],
    ".tiff": ["image"],
    ".bmp": ["image"],
    ".gif": ["image"],
    ".doc": ["pandoc"],
    ".odt": ["pandoc"],
    ".html": ["pandoc"],
    ".htm": ["pandoc"],
    ".rst": ["pandoc"],
    ".epub": ["pandoc"],
    ".md": ["pandoc"],
    ".txt": ["pandoc"],
    ".csv": ["markitdown", "pandoc"],
    "file": ["pdftotext"],  # last-resort fallback for unknown extensions
}


class ExtractorRegistry:
    """Holds parser adapters + ordered chains; runs fallback on empty text."""

    def __init__(
        self,
        parsers: Iterable[Parser],
        chains: dict[str, list[str]] | None = None,
    ) -> None:
        self._parsers: dict[str, Parser] = {}
        for p in parsers:
            if p.name in self._parsers:
                continue
            self._parsers[p.name] = p
        self.chains = dict(_DEFAULT_CHAINS)
        if chains:
            self.chains.update(chains)

    # -- introspection -------------------------------------------------

    @property
    def parsers(self) -> dict[str, Parser]:
        return dict(self._parsers)

    @property
    def names(self) -> list[str]:
        return list(self._parsers)

    # -- routing -------------------------------------------------------

    @staticmethod
    def _kind(source: str) -> str:
        return "url" if source.startswith(("http://", "https://")) else "file"

    @staticmethod
    def _ext(source: str) -> str:
        return Path(source).suffix.lower()

    def _chain_names(self, source: str) -> list[str]:
        kind = self._kind(source)
        ext = self._ext(source)
        if ext and ext in self.chains:
            return self.chains[ext]
        return self.chains.get(kind, [])

    def select(self, source: str, *, parser: str | None = None) -> list[Parser]:
        """Return the ordered, available parsers to try for ``source``.

        With ``parser`` set, force exactly that one (empty list if
        unavailable/unsupported) — used by ``--parser``.
        """
        if parser:
            p = self._parsers.get(parser)
            if p is None:
                return []
            return [p] if (p.available and p.supports(source)) else []

        out: list[Parser] = []
        for name in self._chain_names(source):
            p = self._parsers.get(name)
            if p is not None and p.available and p.supports(source):
                out.append(p)
        return out

    def all_for(self, source: str) -> list[Parser]:
        """Every available parser that supports ``source`` — for ``--compare``."""
        return [
            p
            for p in self._parsers.values()
            if p.available and p.supports(source)
        ]

    # -- extraction ----------------------------------------------------

    def extract(
        self,
        source: str,
        *,
        ocr: bool = False,
        parser: str | None = None,
    ) -> ExtractionResult:
        chain = self.select(source, parser=parser)
        warnings: list[str] = []
        last = chain[-1].name if chain else "none"
        for i, p in enumerate(chain):
            try:
                res = p.extract(source, ocr=ocr)
            except Exception as exc:
                warnings.append(f"{p.name}: {type(exc).__name__}: {exc}")
                continue
            if res.ok:
                if i > 0:
                    res.used_fallback = True
                res.warnings = warnings + res.warnings
                return res
            warnings.extend(res.warnings or [f"{p.name}: no text"])
        return ExtractionResult(
            text="",
            parser=last,
            used_fallback=bool(chain),
            warnings=warnings or ["no parser available"],
        )

    def extract_all(
        self,
        source: str,
        *,
        ocr: bool = False,
    ) -> list[ExtractionResult]:
        """Run every available parser on ``source`` independently (``--compare``)."""
        return [p.extract(source, ocr=ocr) for p in self.all_for(source)]