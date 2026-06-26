"""unpdf parser — wraps iyulab's Rust `unpdf` CLI (PDF sibling of undoc).

Feature-rich PDF→markdown: headings, lists, tables, multi-column (recursive
XY-Cut), CJK + RTL, AcroForm fields, RC4/AES-128 decryption. No OCR for
image-based PDFs yet (planned upstream) — pair with the OCR fallback chain.
Install with ``cargo install unpdf-cli`` (ships the ``unpdf`` binary). When
absent, degrades to pdf-inspector / pymupdf4llm / pdfplumber / pdftotext.
"""

from __future__ import annotations

from .base import SubprocessParser


class UnpdfParser(SubprocessParser):
    name = "unpdf"
    binary = "unpdf"
    extensions = (".pdf",)
    timeout = 180

    def args(self, source: str, *, ocr: bool) -> list[str]:
        # `unpdf markdown <file>` writes markdown to stdout when -o is omitted.
        return ["markdown", source]

    def parse(self, stdout: str, source: str) -> str:
        return stdout.strip()