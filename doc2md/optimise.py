"""Token-optimisation — the deterministic compaction stage.

Strips repeated running headers/footers/page numbers, collapses whitespace,
drops page markers, and keeps semantic structure. Produces the
token-optimised source llm_wiki ingests. Pure function; no LLM.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from typing import Optional

try:
    import tiktoken
    _enc = tiktoken.get_encoding("cl100k_base")
    _HAS_TIKTOKEN = True
except ImportError:
    _HAS_TIKTOKEN = False
    _enc = None

from .figures import strip_picture_markers


@dataclass
class OptimiseResult:
    text: str
    tokens_raw: int = 0
    tokens_optimised: int = 0

_PAGE_MARKER = re.compile(r"^\s*<!--\s*page\s+\d+.*?-->\s*$", re.IGNORECASE)
_PAGE_NUM_LINE = re.compile(
    r"^\s*(?:page\s+\d{1,4}\s*(?:of\s+\d{1,4})?|\d{1,4}\s+of\s+\d{1,4})\s*$",
    re.IGNORECASE,
)
# Parser garbage: pymupdf4llm renders low-quality raster regions as strikethrough
# spans like ``~~QO~~`` / ``~~a eee~~``. These are not words — strip them before
# they contaminate diagram detection (they otherwise count as ALL-CAPS "components"
# and satisfy keyword matches). Replace with a space so adjacent words don't
# merge into a false CamelCase token (``Annual~~Info~~`` → ``Annual Info`` not
# ``AnnualInfo``), then collapse the resulting space runs.
_STRIKETHROUGH = re.compile(r"~~[^~\n]*~~")
_MULTI_SPACE = re.compile(r"[ \t]{2,}")


def _strip_page_markers(lines: list[str]) -> list[str]:
    return [ln for ln in lines if not _PAGE_MARKER.match(ln)]


def _find_running_headers(lines: list[str]) -> set[str]:
    """Short lines repeated across many lines → running header/footer."""
    counts = Counter(ln.strip() for ln in lines if ln.strip())
    if not counts:
        return set()
    # A running header repeats often and is short. 6+ occurrences is a strong
    # signal for a multi-page document's header/footer.
    return {
        line
        for line, n in counts.items()
        if n >= 6 and 0 < len(line) <= 80
    }


def _count_tokens(text: str) -> int:
    """Count tokens using tiktoken (cl100k_base for Claude)."""
    if not _HAS_TIKTOKEN or not text:
        return 0
    return len(_enc.encode(text))


def optimise(text: str) -> str:
    """Backward-compatible: returns optimized text only."""
    result = optimise_with_tokens(text)
    return result.text


def optimise_with_tokens(text: str) -> OptimiseResult:
    """Optimize text and return token counts."""
    if not text:
        return OptimiseResult(text="")

    tokens_raw = _count_tokens(text)

    # Strip parser garbage (strikethrough spans) before any line work.
    text = _MULTI_SPACE.sub(" ", _STRIKETHROUGH.sub(" ", text))
    # Drop pymupdf4llm picture annotation lines (the figure is routed to vision
    # via meta["vision_pages"]; these markers are parser noise, not content).
    text = strip_picture_markers(text)

    lines = text.split("\n")
    lines = [ln.rstrip() for ln in lines]
    lines = _strip_page_markers(lines)
    lines = [ln for ln in lines if not _PAGE_NUM_LINE.match(ln)]

    headers = _find_running_headers(lines)
    if headers:
        lines = [ln for ln in lines if ln.strip() not in headers]

    # Collapse runs of blank lines to at most one blank line.
    out: list[str] = []
    blank_run = 0
    for ln in lines:
        if ln.strip():
            out.append(ln)
            blank_run = 0
        else:
            blank_run += 1
            if blank_run <= 1:
                out.append("")

    # Trim leading/trailing blanks.
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()

    optimized = "\n".join(out)
    tokens_optimised = _count_tokens(optimized)

    return OptimiseResult(
        text=optimized,
        tokens_raw=tokens_raw,
        tokens_optimised=tokens_optimised,
    )