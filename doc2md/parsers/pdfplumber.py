"""pdfplumber parser — Python library, per-page text with OCR + vision signals."""

from __future__ import annotations

import importlib

from ..ocr import ocr_pdf_page
from .base import ExtractionResult, LibraryParser

# Pages yielding fewer than this many characters even after OCR are treated as
# figure/infographic pages and flagged for Claude vision.
_SPARSE_PAGE_CHARS = 80


class PdfplumberParser(LibraryParser):
    name = "pdfplumber"
    module_name = "pdfplumber"
    extensions = (".pdf",)

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        try:
            pdfplumber = importlib.import_module("pdfplumber")
        except Exception as exc:
            return ExtractionResult(
                text="", parser=self.name, warnings=[f"pdfplumber unavailable: {exc}"]
            )

        pages: list[str] = []
        vision_pages: list[int] = []
        try:
            with pdfplumber.open(source) as pdf:
                for i, page in enumerate(pdf.pages, start=1):
                    txt = (page.extract_text() or "").strip()
                    if txt:
                        pages.append(f"<!-- page {i} -->\n{txt}")
                        continue
                    if not ocr:
                        continue
                    ocr_txt = ocr_pdf_page(source, i)
                    if ocr_txt and len(ocr_txt) >= _SPARSE_PAGE_CHARS:
                        pages.append(f"<!-- page {i} (OCR) -->\n{ocr_txt}")
                    else:
                        vision_pages.append(i)  # sparse → likely figure/infographic
        except Exception as exc:
            return ExtractionResult(
                text="", parser=self.name, warnings=[f"pdfplumber failed: {exc}"]
            )

        meta = {"vision_pages": vision_pages} if vision_pages else {}
        return ExtractionResult(text="\n\n".join(pages), parser=self.name, meta=meta)