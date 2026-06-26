"""ImageParser — standalone PNG/JPG/WebP/TIFF infographics.

Deterministic OCR recovers text/labels; the image itself is always routed to
Claude vision for interpretation (there is no deterministic-only branch for
image diagrams). The parser therefore returns the OCR text *and* the source
path in ``images`` with ``meta["needs_vision"] = True`` so the skill sends it
to Claude.
"""

from __future__ import annotations

from pathlib import Path

from ..ocr import ocr_available, ocr_image_file, ocr_image_multilingual
from .base import ExtractionResult

_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp", ".gif")


class ImageParser:
    name = "image"
    kinds = ("file",)
    extensions = _EXTS

    @property
    def available(self) -> bool:
        # Always "available": even without tesseract we still route to vision.
        return True

    def supports(self, source: str) -> bool:
        return Path(source).suffix.lower() in self.extensions

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        text = ""
        langs_used = ["eng"]
        warnings: list[str] = []

        if ocr and ocr_available():
            # Try multilingual OCR first
            text, langs_used = ocr_image_multilingual(source)
            if langs_used != ["eng"]:
                warnings.append(f"OCR languages: {'+'.join(langs_used)}")
            if not text.strip():
                # Fallback to simple OCR if multilingual failed
                text = ocr_image_file(source)
                langs_used = ["eng"]
        elif ocr:
            warnings.append("tesseract not available; image sent to vision without OCR labels")

        return ExtractionResult(
            text=text,
            parser=self.name,
            images=[str(Path(source).resolve())],
            warnings=warnings,
            meta={
                "needs_vision": True,
                "kind": "infographic",
                "ocr_languages": langs_used,
            },
        )