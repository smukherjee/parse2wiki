"""Writer — assembles the token-optimised source + a skill work-order.

The engine does everything deterministic and emits a *work-order*: the list of
items only Claude can do (complex text-diagram Mermaid, infographic vision).
The ``/doc2md`` skill fulfils the work-order and calls :func:`apply_work` to
splice results into the source, replacing ``await`` markers.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .detection import DiagramDetection
from .parsers.base import ExtractionResult

_AWAIT_RE = re.compile(r"^[ \t]*<!--\s*doc2md:await:(\S+)\s*-->[ \t]*$")


@dataclass
class WorkItem:
    id: str
    kind: str  # "complex_mermaid" | "infographic"
    text: str = ""
    image: Optional[str] = None
    diagram_type: Optional[str] = None
    cache_key: str = ""
    file_hash: str = ""          # content hash of the source doc (for cache lookups)
    fulfilled: Optional[str] = None  # cached LLM output; when set, inlined, not awaited


def _await_marker(item_id: str) -> str:
    return f"<!-- doc2md:await:{item_id} -->"


def build_source(
    *,
    title: str,
    result: ExtractionResult,
    detection: DiagramDetection,
    simple_mermaid: str,
    work_items: list[WorkItem],
) -> tuple[str, list[dict]]:
    """Return (source_markdown, work_order_dicts).

    Items with ``fulfilled`` set are inlined into the source; only pending
    items (``fulfilled is None``) appear in the work-order.
    """
    parts: list[str] = [f"# {title}", "", f"<!-- doc2md: extracted_by={result.parser} -->", ""]

    body = result.text.strip()
    if body:
        parts.append(body)
        parts.append("")

    # Diagrams: deterministic simple Mermaid first, then per-item (inlined if
    # cached, awaited if pending).
    diagram_bits: list[str] = []
    if simple_mermaid:
        diagram_bits.append("## Diagram\n\n" + simple_mermaid)
    for item in work_items:
        if item.kind == "complex_mermaid":
            if item.fulfilled is not None:
                diagram_bits.append("## Diagram\n\n" + item.fulfilled.rstrip())
            else:
                diagram_bits.append(
                    f"## Diagram\n\n{_await_marker(item.id)}\n"
                    f"<!-- pending: Claude Mermaid for {item.diagram_type or 'flowchart'} -->"
                )
        elif item.kind == "infographic":
            if item.fulfilled is not None:
                diagram_bits.append("## Infographic\n\n" + item.fulfilled.rstrip())
            else:
                label = item.text.strip()
                block = f"## Infographic\n\n{_await_marker(item.id)}\n"
                if label:
                    block += f"<!-- OCR labels:\n{label}\n-->\n"
                block += f"<!-- pending: Claude vision of {item.image} -->"
                diagram_bits.append(block)

    if diagram_bits:
        parts.append("\n\n".join(diagram_bits))
        parts.append("")

    source = "\n".join(parts).rstrip() + "\n"
    order = [
        {
            "id": i.id, "kind": i.kind, "text": i.text, "image": i.image,
            "diagram_type": i.diagram_type, "cache_key": i.cache_key,
            "file_hash": i.file_hash,
        }
        for i in work_items if i.fulfilled is None
    ]
    return source, order


def write_work_order(path: str | Path, items: list[dict]) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(items, indent=2))
    return p


def apply_work(source_md: str, fulfilled: dict[str, str]) -> str:
    """Replace ``await`` markers with the skill's output for each id.

    ``fulfilled`` maps item id → markdown to splice in (may contain Mermaid).
    Unfulfilled ids are left as markers.
    """
    out: list[str] = []
    for line in source_md.split("\n"):
        m = _AWAIT_RE.match(line)
        if m and m.group(1) in fulfilled:
            out.append(fulfilled[m.group(1)].rstrip())
        else:
            out.append(line)
    return "\n".join(out)