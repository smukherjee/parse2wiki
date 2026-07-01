"""Tesseract OCR helpers — deterministic text recovery from images.

This module is purely deterministic. OCR recovers *labels/text* from images;
the *interpretation* of an infographic is the skill's job (Claude vision).
"""

from __future__ import annotations

import importlib
from pathlib import Path
from typing import Optional


def _have(*mods: str) -> bool:
    for m in mods:
        try:
            importlib.import_module(m)
        except Exception:
            return False
    return True


def ocr_available() -> bool:
    return _have("pytesseract")


def pdf2image_available() -> bool:
    return _have("pdf2image", "PIL")


def ocr_image_file(image_path: str) -> str:
    """OCR a standalone image file. Empty string if pytesseract missing."""
    if not ocr_available():
        return ""
    from PIL import Image
    import pytesseract

    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
    except Exception:  # corrupt image, tesseract not installed, etc.
        return ""
    return text or ""


def render_pdf_pages(
    pdf_path: str,
    *,
    first: Optional[int] = None,
    last: Optional[int] = None,
    dpi: int = 300,
):
    """Render PDF pages to PIL images. Empty list if no backend available.

    Backends tried in order: pdf2image (poppler), PyMuPDF (fitz), pypdfium2.
    """
    if pdf2image_available():
        pdf2image = importlib.import_module("pdf2image")
        try:
            return pdf2image.convert_from_path(
                pdf_path, first_page=first, last_page=last, dpi=dpi
            )
        except Exception:
            pass
    # ponytail: fitz/pypdfium2 fallback so vision rendering works without poppler/pdf2image
    if _have("fitz", "PIL"):
        import fitz  # PyMuPDF
        from PIL import Image
        import io

        try:
            zoom = dpi / 72.0
            doc = fitz.open(pdf_path)
            total = doc.page_count
            f = first or 1
            l = last or total
            f = max(f, 1)
            l = min(l, total)
            out = []
            for i in range(f, l + 1):
                pix = doc.load_page(i - 1).get_pixmap(matrix=fitz.Matrix(zoom, zoom))
                out.append(Image.open(io.BytesIO(pix.tobytes("png"))))
            doc.close()
            return out
        except Exception:
            pass
    if _have("pypdfium2", "PIL"):
        import pypdfium2 as pdfium
        from PIL import Image

        try:
            scale = dpi / 72.0
            doc = pdfium.PdfDocument(pdf_path)
            total = len(doc)
            f = first or 1
            l = last or total
            f = max(f, 1)
            l = min(l, total)
            out = []
            for i in range(f, l + 1):
                out.append(doc[i - 1].render(scale=scale).to_pil())
            doc.close()
            return out
        except Exception:
            pass
    return []


def ocr_pdf(pdf_path: str, *, dpi: int = 300) -> str:
    """Full-document OCR fallback for PDFs that have no extractable text."""
    if not ocr_available() or not pdf2image_available():
        return ""
    import pytesseract

    pages = render_pdf_pages(pdf_path, dpi=dpi)
    out: list[str] = []
    for i, img in enumerate(pages, start=1):
        text = pytesseract.image_to_string(img)
        if text and text.strip():
            out.append(f"<!-- page {i} (OCR) -->\n{text.strip()}")
    return "\n\n".join(out)


def ocr_pdf_page(pdf_path: str, page_num: int) -> str:
    """OCR a single page (1-indexed). Empty string on failure."""
    if not ocr_available() or not pdf2image_available():
        return ""
    import pytesseract

    images = render_pdf_pages(pdf_path, first=page_num, last=page_num)
    if not images:
        return ""
    return (pytesseract.image_to_string(images[0]) or "").strip()


def ocr_image_multilingual(image_path: str) -> tuple[str, list[str]]:
    """OCR an image with automatic language detection.

    Returns (text, languages_used) where languages_used is the list of
    Tesseract language codes applied (e.g., ['eng', 'ara'] for Arabic/English).

    Uses langdetect to identify non-Latin scripts and loads appropriate
    Tesseract language packs. Falls back to English-only if detection fails.
    """
    if not ocr_available():
        return "", ["eng"]

    from PIL import Image
    import pytesseract

    # First pass: OCR with English to get sample text
    try:
        with Image.open(image_path) as img:
            # Quick OCR with English to detect language
            sample_text = pytesseract.image_to_string(img, lang="eng")

            # Detect languages in the text
            try:
                from .lang import get_tesseract_langs_for_text
                langs = get_tesseract_langs_for_text(sample_text)
            except Exception:
                langs = ["eng"]

            # Re-OCR with detected languages
            lang_str = "+".join(langs)
            try:
                full_text = pytesseract.image_to_string(img, lang=lang_str)
                return full_text or "", langs
            except Exception:
                # Language pack not installed, fall back to English
                return sample_text or "", ["eng"]

    except Exception:
        return "", ["eng"]


def ocr_pdf_multilingual(pdf_path: str, *, dpi: int = 200, force_langs: list[str] = None) -> list[tuple[int, str, list[str]]]:
    """OCR a PDF with automatic language detection per page.

    Returns list of (page_num, text, languages_used) tuples.

    Args:
        pdf_path: Path to PDF file
        dpi: Resolution for rendering pages
        force_langs: If provided, use these languages instead of auto-detection
    """
    if not ocr_available() or not pdf2image_available():
        return []

    from PIL import Image
    import pytesseract

    pages = render_pdf_pages(pdf_path, dpi=dpi)
    results = []

    # If force_langs provided, use those directly
    if force_langs:
        lang_str = "+".join(force_langs)
        for i, img in enumerate(pages, start=1):
            try:
                text = pytesseract.image_to_string(img, lang=lang_str)
                results.append((i, text or "", force_langs))
            except Exception as exc:
                results.append((i, "", [str(exc)]))
        return results

    for i, img in enumerate(pages, start=1):
        try:
            # Quick OCR with English for language detection
            sample_text = pytesseract.image_to_string(img, lang="eng")

            try:
                from .lang import get_tesseract_langs_for_text
                langs = get_tesseract_langs_for_text(sample_text)
            except Exception:
                langs = ["eng"]

            # Re-OCR with detected languages
            lang_str = "+".join(langs)
            try:
                text = pytesseract.image_to_string(img, lang=lang_str)
                results.append((i, text or "", langs))
            except Exception:
                results.append((i, sample_text or "", ["eng"]))

        except Exception:
            results.append((i, "", ["eng"]))

    return results