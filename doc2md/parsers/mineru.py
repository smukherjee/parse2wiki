"""MinerU parser — deep-learning PDF extraction via the magic-pdf CLI.

MinerU (https://github.com/opendatalab/MinerU) uses PaddleOCR + layout detection
to handle complex PDFs: image-heavy pages, dense tables, mixed-language content,
multi-column layouts.  It is invoked as the ``magic-pdf`` CLI and is treated as an
optional heavy-weight backend — only used when explicitly requested (``--mineru``)
or when lighter parsers fail on a page-type that MinerU handles well.

Installation:
    pip install magic-pdf[full]   # or: pip install magic-pdf[lite]
    # Requires model weights; see MinerU docs for first-run download (~2 GB).
    # Run once to trigger weight download: magic-pdf --help
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from .base import ExtractionResult, SubprocessParser

_INSTALL_HINT = (
    "magic-pdf not found. Install MinerU with:\n"
    "  pip install magic-pdf[full]\n"
    "Then download model weights (first run only, ~2 GB):\n"
    "  magic-pdf --help\n"
    "See: https://github.com/opendatalab/MinerU"
)


class MineruParser(SubprocessParser):
    """Wrap the ``magic-pdf`` CLI as a doc2md parser.

    MinerU writes output into a directory tree.  We collect the first .md file
    found under the output directory — MinerU places it at:
      <out>/<stem>/auto/<stem>.md  or  <out>/<stem>/ocr/<stem>.md
    """

    name = "mineru"
    binary = "magic-pdf"
    extensions = (".pdf",)
    kinds = ("file",)
    timeout = 300  # MinerU downloads models on first run; allow extra time

    def _resolve_binary(self) -> str | None:
        """Resolve magic-pdf, also checking venv bin (for uv/pip installs)."""
        found = super()._resolve_binary()
        if found:
            return found
        # Check venv bin directory (uv/pip installs)
        import sys
        venv_bin = Path(sys.executable).parent / "magic-pdf"
        if venv_bin.exists():
            return str(venv_bin)
        return None

    def args(self, source: str, *, ocr: bool) -> list[str]:
        raise NotImplementedError("MineruParser uses a custom extract() path")

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        bin_path = self._resolve_binary()
        if not bin_path:
            return ExtractionResult(
                text="", parser=self.name, warnings=[_INSTALL_HINT]
            )

        source_path = Path(source)
        warnings: list[str] = []

        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir) / "out"
            out_dir.mkdir()

            # magic-pdf pdf --pdf <file> --method <method>
            # --method auto: picks ocr or txt method based on page content
            method = "ocr" if ocr else "auto"
            cmd = [bin_path, "pdf", "--pdf", str(source_path), "--method", method]

            try:
                proc = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=self.timeout,
                )
            except subprocess.TimeoutExpired:
                return ExtractionResult(
                    text="", parser=self.name,
                    warnings=[f"magic-pdf timeout after {self.timeout}s"],
                )
            except FileNotFoundError:
                return ExtractionResult(
                    text="", parser=self.name, warnings=["magic-pdf not found"]
                )

            if proc.returncode != 0:
                err = (proc.stderr or "").strip().splitlines()
                msg = err[-1] if err else f"magic-pdf exit {proc.returncode}"
                return ExtractionResult(text="", parser=self.name, warnings=[msg[:300]])

            if proc.stderr:
                for line in proc.stderr.strip().splitlines():
                    if line.strip():
                        warnings.append(line.strip()[:200])

            text = self._collect_output(out_dir, source_path.stem)

        if not text:
            return ExtractionResult(
                text="", parser=self.name,
                warnings=warnings + ["magic-pdf produced no text"],
            )
        return ExtractionResult(text=text, parser=self.name, warnings=warnings)

    def _collect_output(self, out_dir: Path, stem: str) -> str:
        """Walk MinerU's output tree and return the best markdown we can find.

        MinerU writes:  <out_dir>/<stem>/auto/<stem>.md
                    or: <out_dir>/<stem>/ocr/<stem>.md
        We take the first .md file found under out_dir.
        """
        for md_file in sorted(out_dir.rglob("*.md")):
            text = md_file.read_text(encoding="utf-8", errors="replace").strip()
            if text:
                return text
        return ""
