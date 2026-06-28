"""Figure-page detection for PDFs whose text parser inlines images as text.

Some PDF parsers (pymupdf4llm) cannot render an embedded figure as markdown, so
they emit an annotation in the text stream instead — e.g.::

    **==> picture [889 x 438] intentionally omitted <==**
    **----- Start of picture text -----**
    <flattened labels / OCR of the figure>
    **----- End of picture text -----**

Such a figure is genuinely a diagram, but the flattened text has no real edge
structure, so text-diagram detection correctly returns ``none``. The right
handling is **vision**: render the page that contains the figure to a PNG and
let the skill (Claude vision) interpret it.

This module is the deterministic bridge: it finds which pages carry a
picture-omission marker and strips the annotation markers from the source text
(they are parser noise, not content). Pure functions; no LLM.
"""

from __future__ import annotations

import re

# The "picture intentionally omitted" marker (searchable anywhere in a page's
# text — used to flag that page for vision routing).
PICTURE_OMITTED_RE = re.compile(r"==>\s*picture\b[^<]*?intentionally\s+omitted", re.IGNORECASE)

# pymupdf4llm's picture annotations. Removed as *substrings*, not whole lines:
# pymupdf4llm sometimes glues the End marker onto the end of the figure-text
# line (``...labels<br>**----- End of picture text -----**<br>``), so a
# line-anchored strip would miss it. The marker strings are distinctive enough
# that substring removal cannot clip real figure text. ``[^<\n]`` keeps each
# match on a single line.
_PICTURE_ANNOTATION_RE = [
    re.compile(r"\*{0,2}==>\s*picture\b[^<\n]*?intentionally\s+omitted[^<\n]*?<==\*{0,2}", re.IGNORECASE),
    re.compile(r"\*{0,2}-{2,}\s*Start\s+of\s+picture\s+text\s*-{2,}\*{0,2}", re.IGNORECASE),
    re.compile(r"\*{0,2}-{2,}\s*End\s+of\s+picture\s+text\s*-{2,}\*{0,2}", re.IGNORECASE),
]


def has_picture_omission(text: str) -> bool:
    """True if the text carries a picture-omission marker."""
    return bool(PICTURE_OMITTED_RE.search(text or ""))


def picture_omitted_pages(page_texts: dict[int, str]) -> list[int]:
    """Return the sorted 1-based page numbers whose text contains a
    picture-omission marker. Pages are keyed 1-based to match PDF rendering.
    """
    return sorted(p for p, t in page_texts.items() if has_picture_omission(t))


_FIGURE_RECT_MIN_AREA = 400   # pts² — ignore hairlines and thin borders (< ~20×20 pt)
_FIGURE_RECTS_MIN = 5         # minimum meaningful rectangles to infer node boxes
_FIGURE_GRAPHICS_MIN = 15     # rects+lines+curves threshold for "real" graphic density


def graphic_dense_pages(
    source: str,
    *,
    min_rects: int = _FIGURE_RECTS_MIN,
    min_graphics: int = _FIGURE_GRAPHICS_MIN,
) -> list[int]:
    """Return 1-based page numbers where pdfplumber finds a visual-diagram layout.

    A page is flagged when it has many bounding-box rectangles (diagram node
    boxes) and enough total graphic elements (rects + lines + curves). This
    catches visual workflow diagrams where the primary text parser extracted
    node labels but lost the connecting arrows entirely.

    Returns [] if pdfplumber is unavailable or the PDF cannot be opened.
    """
    try:
        import pdfplumber  # type: ignore
    except ImportError:
        return []

    figure_pages: list[int] = []
    try:
        with pdfplumber.open(source) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                big_rects = [
                    r for r in (page.rects or [])
                    if r.get("width", 0) * r.get("height", 0) >= _FIGURE_RECT_MIN_AREA
                ]
                total_graphics = (
                    len(big_rects)
                    + len(page.lines or [])
                    + len(page.curves or [])
                )
                if len(big_rects) >= min_rects and total_graphics >= min_graphics:
                    figure_pages.append(i)
    except Exception:
        pass
    return figure_pages


def image_dominant_pages(
    source: str,
    *,
    min_coverage: float = 0.4,
) -> list[int]:
    """Return 1-based page numbers where raster images cover ≥40% of the page.

    Catches image-embedded PDFs (phone screenshots, scanned slides, WhatsApp
    PDFs) that have zero vector elements so graphic_dense_pages returns [].
    Those pages carry their content as pixels and need vision to interpret.
    """
    try:
        import pdfplumber  # type: ignore
    except ImportError:
        return []

    pages: list[int] = []
    try:
        with pdfplumber.open(source) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                page_area = page.width * page.height
                if not page_area:
                    continue
                covered = sum(
                    (im.get("x1", 0) - im.get("x0", 0)) *
                    (im.get("bottom", 0) - im.get("top", 0))
                    for im in (page.images or [])
                )
                if covered / page_area >= min_coverage:
                    pages.append(i)
    except Exception:
        pass
    return pages


def strip_picture_markers(text: str) -> str:
    """Remove pymupdf4llm's picture annotation markers from the source text.

    Only the marker substrings are dropped; any flattened figure text between
    the Start/End markers is preserved (it may be the only fallback if vision
    rendering is unavailable).
    """
    if not text:
        return ""
    for rx in _PICTURE_ANNOTATION_RE:
        text = rx.sub("", text)
    return text