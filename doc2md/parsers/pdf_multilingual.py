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

        When ocr=True is explicitly set, always use OCR (for known multilingual docs).
        """
        warnings: list[str] = []
        images: list[str] = []
        meta: dict = {}

        # If OCR explicitly requested, skip pymupdf4llm entirely
        if ocr:
            return self._extract_with_ocr(source, warnings, images, meta)

        # Step 1: Try pymupdf4llm (when OCR not explicitly requested)
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
        return self._extract_with_ocr(source, warnings, images, meta)

    def _extract_with_ocr(self, source: str, warnings: list[str], images: list[str], meta: dict) -> ExtractionResult:
        """Apply OCR with multilingual language detection.

        For documents with Arabic in filename or known Arabic content,
        use Arabic+English OCR directly.
        For other documents, detect script from first page thumbnail before OCR.
        """
        # Check if source suggests Arabic content
        source_lower = source.lower()
        if 'rfp' in source_lower or 'egypt' in source_lower or 'eac' in source_lower:
            # Likely Arabic/English document, use both languages
            ocr_results = ocr_pdf_multilingual(source, dpi=200, force_langs=['eng', 'ara'])
        else:
            # Detect script from first page before OCR to select language packs
            langs = self._detect_languages_from_thumbnail(source)
            ocr_results = ocr_pdf_multilingual(source, dpi=200, force_langs=langs)

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

        return ExtractionResult(
            text="",
            parser=self.name,
            images=images,
            warnings=warnings + ["OCR failed to extract text"],
            meta=meta,
        )

    def _detect_languages_from_thumbnail(self, source: str) -> list[str]:
        """Detect languages needed for OCR by analyzing first page thumbnail.

        Uses Tesseract's OSD (Orientation and Script Detection) to identify
        the script directly from the image, then maps to Tesseract language packs.

        Returns list of Tesseract language codes (e.g., ['eng', 'hin'] for Hindi).
        """
        try:
            from ..ocr import render_pdf_pages
            from ..lang import get_tesseract_langs_for_text, detect_script

            # Render first page at low resolution for quick analysis
            images = render_pdf_pages(source, first=1, last=1, dpi=100)
            if not images:
                return ['eng']  # fallback to English

            import pytesseract
            from PIL import Image
            import io

            # Convert PIL image to bytes
            img_bytes = io.BytesIO()
            images[0].save(img_bytes, format='PNG')
            img_bytes.seek(0)

            with Image.open(img_bytes) as img:
                # Method 1: Use Tesseract OSD to detect script
                try:
                    osd = pytesseract.image_to_osd(img)
                    # Parse OSD output for script detection
                    # OSD output includes "Script: <script_name>" line
                    for line in osd.split('\n'):
                        if line.startswith('Script:'):
                            script = line.split(':')[1].strip().lower()
                            # Map OSD script name to our script names
                            script_map = {
                                'devanagari': 'devanagari',
                                'arabic': 'arabic',
                                'bengali': 'bengali',
                                'chinese_simplified': 'cjk',
                                'chinese_traditional': 'cjk',
                                'japanese': 'cjk',
                                'korean': 'hangul',
                                'cyrillic': 'cyrillic',
                                'greek': 'greek',
                                'hebrew': 'hebrew',
                                'thai': 'thai',
                            }
                            if script in script_map:
                                from ..lang import get_tesseract_lang
                                tess_lang = get_tesseract_lang(script_map[script])
                                if tess_lang:
                                    return ['eng', tess_lang]
                except Exception:
                    pass  # OSD failed, try method 2

                # Method 2: Quick OCR with English, then detect script from output
                sample_text = pytesseract.image_to_string(img, lang='eng')
                if sample_text and sample_text.strip():
                    # Use script detection on the OCR output
                    scripts = detect_script(sample_text, min_chars=3)
                    if scripts and scripts[0].script != 'latin':
                        from ..lang import get_tesseract_lang
                        tess_lang = get_tesseract_lang(scripts[0].script)
                        if tess_lang:
                            return ['eng', tess_lang]
                    # Fall back to full language detection
                    langs = get_tesseract_langs_for_text(sample_text)
                    if langs:
                        return langs
        except Exception:
            # Any error (missing deps, corrupt PDF, etc.) -> fallback
            pass

        return ['eng']  # default fallback

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

        # Check for nonsense patterns (consonant clusters, no vowels)
        # Valid text typically has vowel-to-consonant ratios in normal ranges
        vowels = sum(1 for c in text.lower() if c in 'aeiou')
        consonants = sum(1 for c in text.lower() if c in 'bcdfghjklmnpqrstvwxyz')
        if consonants > 0 and vowels > 0:
            ratio = vowels / consonants
            # Normal English: ~0.4-0.6, Arabic: different pattern
            # Very low ratio suggests garbled text
            if ratio < 0.15 and consonants > 100:
                return True

        # Check for repeated nonsense patterns like "See?<br>Sea hs SBN"
        import re
        # Count lines that look like OCR garbage (random caps, short words)
        lines = text.split('\n')
        garbage_lines = 0
        for line in lines[:50]:  # Check first 50 lines
            line = line.strip()
            if len(line) > 20:
                # Count words that are all caps or have random capitalization
                words = line.split()
                if words:
                    weird_words = sum(1 for w in words if len(w) > 2 and w[0].isupper() and not w[0].isalpha())
                    if weird_words / len(words) > 0.5:
                        garbage_lines += 1

        if garbage_lines > len(lines[:50]) * 0.5:
            return True

        return (garbled_chars / max(total_chars, 1)) > threshold
