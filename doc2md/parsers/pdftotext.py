"""pdftotext parser — wraps the poppler CLI. SubprocessParser example.

Robust fallback for malformed PDFs that defeat Python libraries.
"""

from __future__ import annotations

from .base import SubprocessParser


class PdftotextParser(SubprocessParser):
    name = "pdftotext"
    binary = "pdftotext"
    extensions = (".pdf",)

    def args(self, source: str, *, ocr: bool) -> list[str]:
        # -layout keeps column structure; stdout via "-"
        return ["-layout", source, "-"]

    def parse(self, stdout: str, source: str) -> str:
        return stdout.strip()