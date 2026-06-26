"""pdf-inspector parser — wraps Firecrawl's Rust `pdf2md` CLI.

Fast, layout-aware PDF→markdown (headings, lists, tables, multi-column reading
order) with scanned/text classification. Install the binary with
``cargo install pdf-inspector`` (ships the ``pdf2md`` binary). Pure Rust, no ML,
so it's a strong first entry in the PDF chain when present; if absent it
degrades silently to the next parser.
"""

from __future__ import annotations

from .base import SubprocessParser


class PdfInspectorParser(SubprocessParser):
    name = "pdf-inspector"
    binary = "pdf2md"
    extensions = (".pdf",)
    timeout = 180

    def args(self, source: str, *, ocr: bool) -> list[str]:
        # Default conversion preserves heading structure; positional file arg.
        return [source]

    def parse(self, stdout: str, source: str) -> str:
        return stdout.strip()