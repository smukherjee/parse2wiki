"""undoc parser — wraps iyulab's Rust `undoc` CLI for Office documents.

High-performance DOCX/XLSX/PPTX→markdown with table alignment, footnotes,
headers/footers, and CJK support. Does **not** handle PDF. Install with
``cargo install undoc-cli`` (ships the ``undoc`` binary). When absent, the
chain falls back to markitdown / python-docx/pptx/openpyxl / pandoc.
"""

from __future__ import annotations

from .base import SubprocessParser


class UndocParser(SubprocessParser):
    name = "undoc"
    binary = "undoc"
    extensions = (".docx", ".xlsx", ".pptx")
    timeout = 180

    def args(self, source: str, *, ocr: bool) -> list[str]:
        # `undoc markdown <file>` writes markdown to stdout when -o is omitted.
        return ["markdown", source]

    def parse(self, stdout: str, source: str) -> str:
        return stdout.strip()