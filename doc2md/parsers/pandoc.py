"""pandoc parser — wraps the pandoc CLI for docx/markdown/html/etc."""

from __future__ import annotations

from .base import SubprocessParser


class PandocParser(SubprocessParser):
    name = "pandoc"
    binary = "pandoc"
    extensions = (".docx", ".doc", ".odt", ".html", ".htm", ".rst", ".epub", ".md", ".txt")
    timeout = 120

    def args(self, source: str, *, ocr: bool) -> list[str]:
        # Pandoc infers the input format from the file extension when --from is
        # omitted; there is no "auto" input format, so don't pass --from=auto
        # (it errors with "Unknown input format auto" on real pandoc builds).
        return ["--to=markdown", "--wrap=none", source]

    def parse(self, stdout: str, source: str) -> str:
        return stdout.strip()