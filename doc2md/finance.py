"""Financial document detection and cross-extractor figure verification.

When a document is detected as financial (by filename or keyword scan), the
engine runs every available parser, extracts numeric figures with their label
context, compares across parsers, and emits a ``<source>.verify.json`` report.

Verification is purely deterministic — no LLM involved.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# ── detection ─────────────────────────────────────────────────────────────────

FINANCE_KEYWORDS = [
    "revenue", "profit", "loss", "ebitda", "ebit", "net income", "gross margin",
    "balance sheet", "cash flow", "earnings per share", "eps", "dividend",
    "total assets", "total liabilities", "equity", "income statement",
    "quarterly", "annual report", "fiscal year", "interest rate", "yield",
    "basis points", "bps", "irr", "npv", "wacc", "capex", "opex",
    "working capital", "liquidity", "leverage", "operating income",
    "net revenue", "gross profit", "free cash flow", "market cap",
    "enterprise value", "book value", "price earnings",
]

_FINANCE_FILENAME_RE = re.compile(
    r"annual[_\s-]?report|financial[_\s-]?(statement|report|summary)|"
    r"income[_\s-]?statement|balance[_\s-]?sheet|cash[_\s-]?flow|"
    r"10[_\s-]?[kq]\b|earnings|prospectus|investor|p[&_]l\b|pnl\b",
    re.IGNORECASE,
)

_KEYWORD_THRESHOLD = 3


def is_financial(text: str, path: Optional[str | Path] = None) -> bool:
    """Return True if the document looks like it contains financial figures."""
    if path is not None and _FINANCE_FILENAME_RE.search(Path(path).stem):
        return True
    text_lower = text.lower()
    return sum(1 for kw in FINANCE_KEYWORDS if kw in text_lower) >= _KEYWORD_THRESHOLD


# ── figure extraction ─────────────────────────────────────────────────────────

# Matches numbers with optional currency symbol/prefix and magnitude suffix.
# Skips standalone 4-digit years (1990-2099).
_FIGURE_RE = re.compile(
    r"(?:USD|EUR|GBP|AUD|CAD|CHF|JPY|\$|€|£|¥|₹|₩)?\s*"
    r"(?<!\d)"
    r"(\d{1,3}(?:[,\s]\d{3})+(?:\.\d+)?|\d+\.\d+|\d{4,})"
    r"(?:\s*(?:USD|EUR|GBP|AUD|CAD|CHF|JPY|M|B|K|T|bn|mn|thousand|million|billion|trillion|%|bps))?"
    r"(?!\d)",
    re.IGNORECASE,
)

_YEAR_RE = re.compile(r"^(?:19|20)\d{2}$")

_LABEL_WINDOW = 50  # chars of preceding text used as the figure label/key


def extract_figures(text: str) -> dict[str, str]:
    """Return {label: raw_value} for each numeric figure found in text.

    The label is the last _LABEL_WINDOW chars before the number (normalised
    whitespace, lowercased). When two figures share the same label the last wins.
    """
    figures: dict[str, str] = {}
    for m in _FIGURE_RE.finditer(text):
        raw = m.group(0).strip()
        digits = re.sub(r"[^\d]", "", raw)
        if _YEAR_RE.match(digits):
            continue
        start = max(0, m.start() - _LABEL_WINDOW)
        prefix = re.sub(r"\s+", " ", text[start:m.start()].strip()).lower()
        label = prefix[-_LABEL_WINDOW:]
        if label and raw:
            figures[label] = raw
    return figures


def _normalise(val: str) -> str:
    """Collapse a figure string for equality comparison."""
    v = re.sub(r"\s+", "", val.strip().lower())
    v = re.sub(r"(\d),(\d{3})", r"\1\2", v)  # 1,234 → 1234
    return v


# ── comparison report ─────────────────────────────────────────────────────────

@dataclass
class FigureMismatch:
    label: str
    values: dict[str, str]  # parser_name → raw extracted value
    flag: str               # "warn" (one outlier) | "error" (majority disagree)


@dataclass
class VerificationReport:
    document: str
    parsers_used: list[str]
    total_figures: int
    mismatch_count: int
    mismatches: list[FigureMismatch] = field(default_factory=list)

    @property
    def verified(self) -> bool:
        return self.mismatch_count == 0

    def to_dict(self) -> dict:
        return {
            "document": self.document,
            "parsers_used": self.parsers_used,
            "total_figures": self.total_figures,
            "mismatch_count": self.mismatch_count,
            "verified": self.verified,
            "mismatches": [
                {"label": m.label, "values": m.values, "flag": m.flag}
                for m in self.mismatches
            ],
        }

    def write(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps(self.to_dict(), indent=2))

    def summary_lines(self) -> list[str]:
        """Short human-readable lines for CLI/skill output."""
        lines = [
            f"finance verify: {len(self.parsers_used)} parsers, "
            f"{self.total_figures} figures, "
            f"{self.mismatch_count} mismatches — "
            f"{'OK' if self.verified else 'REVIEW REQUIRED'}"
        ]
        for mm in self.mismatches:
            vals = ", ".join(f"{k}={v}" for k, v in mm.values.items())
            lines.append(f"  [{mm.flag}] «{mm.label}» → {vals}")
        return lines


def compare_extractors(
    results: dict[str, str],
    document: str = "",
) -> VerificationReport:
    """Compare figures across multiple parser outputs.

    Args:
        results: mapping of parser_name → extracted_text
        document: document path for the report header

    Returns:
        VerificationReport with one FigureMismatch per disagreeing figure.
    """
    parser_figures: dict[str, dict[str, str]] = {
        name: extract_figures(text) for name, text in results.items()
    }

    all_labels: set[str] = set()
    for figs in parser_figures.values():
        all_labels.update(figs)

    mismatches: list[FigureMismatch] = []
    for label in sorted(all_labels):
        seen = {
            name: figs[label]
            for name, figs in parser_figures.items()
            if label in figs
        }
        if len(seen) < 2:
            continue  # only one parser extracted this — nothing to compare

        normalised = {name: _normalise(val) for name, val in seen.items()}
        if len(set(normalised.values())) == 1:
            continue  # all agree

        counts = {v: list(normalised.values()).count(v) for v in set(normalised.values())}
        majority = max(counts.values())
        flag = "warn" if majority >= len(seen) - 1 else "error"
        mismatches.append(FigureMismatch(label=label, values=seen, flag=flag))

    return VerificationReport(
        document=document,
        parsers_used=list(results.keys()),
        total_figures=len(all_labels),
        mismatch_count=len(mismatches),
        mismatches=mismatches,
    )
