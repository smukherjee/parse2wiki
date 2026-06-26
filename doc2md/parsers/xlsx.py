"""openpyxl parser — XLSX sheets → markdown tables."""

from __future__ import annotations

import importlib

from .base import ExtractionResult, LibraryParser

_MAX_ROWS = 200
_MAX_COLS = 32


class XlsxParser(LibraryParser):
    name = "xlsx"
    module_name = "openpyxl"
    extensions = (".xlsx",)

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        try:
            openpyxl = importlib.import_module("openpyxl")
            wb = openpyxl.load_workbook(source, read_only=True, data_only=True)
        except Exception as exc:
            return ExtractionResult(
                text="", parser=self.name, warnings=[f"openpyxl failed: {exc}"]
            )

        out: list[str] = []
        for ws in wb.worksheets:
            out.append(f"## {ws.title}")
            rows = list(ws.iter_rows(values_only=True))
            if not rows:
                continue
            total = len(rows)
            rows = rows[:_MAX_ROWS]
            width = min(max(len(r) for r in rows), _MAX_COLS)
            for r in rows:
                cells = ["" if c is None else str(c) for c in r[:width]]
                out.append("| " + " | ".join(cells) + " |")
            if total > _MAX_ROWS:
                out.append(f"> (truncated to {_MAX_ROWS} rows)")
        try:
            wb.close()
        except Exception:
            pass
        return ExtractionResult(text="\n\n".join(out), parser=self.name)