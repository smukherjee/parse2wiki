"""MultilingualPDFParser — PDF extraction with automatic language detection.

Uses pymupdf4llm for text extraction, then applies multilingual OCR on pages
that contain non-Latin scripts (Arabic, Hindi, etc.) where text extraction
fails or produces garbled output.
"""

from __future__ import annotations

import importlib
from pathlib import Path
from typing import Optional

from ..ocr import ocr_pdf_multilingual, render_pdf_pages
from ..lang import has_non_latin_text, detect_language, get_tesseract_langs_for_text
from .base import ExtractionResult


class MultilingualPDFParser:
    """PDF parser with multilingual OCR fallback for non-Latin scripts."""

    name = "pdf-multilingual"
    kinds = ("file",)
    extensions = (".pdf",)

    @property
    def available(self) -> bool:
        """Available if pdf2image and pytesseract are installed."""
        try:
            importlib.import_module("pdf2image")
            importlib.import_module("pytesseract")
            return True
        except Exception:
            return False

    def supports(self, source: str) -> bool:
        return Path(source).suffix.lower() == ".pdf"

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        """Extract text from PDF with multilingual OCR support.

        1. Try pymupdf4llm first (fastest, best text extraction)
        2. If text is garbled or empty, detect language and apply OCR
        3. For mixed-language docs, OCR with appropriate language packs
        """
        warnings: list[str] = []
        images: list[str] = []
        meta: dict = {}

        # Step 1: Try pymupdf4llm
        try:
            pymupdf4llm = importlib.import_module("pymupdf4llm")
            md_text = pymupdf4llm.to_markdown(source)

            if md_text and len(md_text.strip()) > 100:
                # Check if text looks valid (not garbled)
                if not self._is_garbled(md_text):
                    # Valid text extracted, check for non-Latin content
                    lang_result = detect_language(md_text[:500])
                    meta["detected_language"] = lang_result.language
                    meta["detected_script"] = lang_result.script

                    if lang_result.script != "latin":
                        langs = get_tesseract_langs_for_text(md_text)
                        meta["ocr_languages"] = langs
                        if langs != ["eng"]:
                            warnings.append(f"Non-Latin script detected: {lang_result.script}")

                    return ExtractionResult(
                        text=md_text,
                        parser=self.name,
                        images=images,
                        warnings=warnings,
                        meta=meta,
                    )
        except Exception as exc:
            warnings.append(f"pymupdf4llm failed: {exc}")

        # Step 2: pymupdf4llm failed or produced garbled text, use OCR
        if ocr:
            ocr_results = ocr_pdf_multilingual(source, dpi=200)
            if ocr_results:
                texts = []
                all_langs = set()
                for page_num, text, langs in ocr_results:
                    texts.append(f"<!-- Page {page_num} -->\n{text}")
                    all_langs.update(langs)

                md_text = "\n\n".join(texts)
                meta["ocr_languages"] = list(all_langs)
                meta["ocr_pages"] = len(ocr_results)
                warnings.append(f"OCR applied with languages: {'+'.join(sorted(all_langs))}")

                return ExtractionResult(
                    text=md_text,
                    parser=self.name,
                    images=images,
                    warnings=warnings,
                    meta=meta,
                )
        else:
            warnings.append("OCR not enabled; try with ocr=True for non-Latin scripts")

        # Step 3: No text extracted
        return ExtractionResult(
            text="",
            parser=self.name,
            images=images,
            warnings=warnings + ["No text could be extracted"],
            meta=meta,
        )

    def _is_garbled(self, text: str, threshold: float = 0.3) -> bool:
        """Check if text appears garbled (high ratio of non-printable chars).

        Garbled text often has many control characters, replacement chars,
        or nonsensical sequences from failed text extraction.
        """
        if not text:
            return True

        # Count problematic characters
        garbled_chars = 0
        total_chars = len(text)

        for char in text:
            code = ord(char)
            # Control characters (except newline, tab, carriage return)
            if code < 32 and code not in (9, 10, 13):
                garbled_chars += 1
            # Replacement character
            elif code == 0xFFFD:
                garbled_chars += 1
            # High ratio of very high Unicode (possible extraction errors)
            elif code > 0xFFFF:
                garbled_chars += 1

        return (garbled_chars / total_chars) > threshold
