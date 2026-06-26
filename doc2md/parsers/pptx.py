"""python-pptx parser — PPTX slides → markdown."""

from __future__ import annotations

import importlib

from .base import ExtractionResult, LibraryParser


class PptxParser(LibraryParser):
    name = "pptx"
    module_name = "pptx"
    extensions = (".pptx",)

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        try:
            pptx = importlib.import_module("pptx")
            prs = pptx.Presentation(source)
        except Exception as exc:
            return ExtractionResult(
                text="", parser=self.name, warnings=[f"python-pptx failed: {exc}"]
            )

        out: list[str] = []
        for i, slide in enumerate(prs.slides, start=1):
            out.append(f"## Slide {i}")
            for shape in slide.shapes:
                if shape.has_text_frame:
                    txt = "\n".join(
                        p.text for p in shape.text_frame.paragraphs if p.text.strip()
                    ).strip()
                    if txt:
                        out.append(txt)
                if shape.has_table:
                    rows = [[c.text.strip() for c in row.cells] for row in shape.table.rows]
                    for r in rows:
                        out.append("| " + " | ".join(r) + " |")
            if slide.has_notes_slide:
                notes = slide.notes_slide.notes_text_frame.text.strip()
                if notes:
                    out.append(f"> notes: {notes}")
        return ExtractionResult(text="\n\n".join(out), parser=self.name)