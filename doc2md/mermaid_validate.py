"""Mermaid validation — cheap structural checks for LLM-produced Mermaid.

Invalid LLM Mermaid is dropped (with a warning) rather than baked into a
source. This is the only surviving piece of the old quality-gate theme.
"""

from __future__ import annotations

import re

# Minimal Mermaid diagram heads we recognise.
_HEADS = (
    "flowchart", "graph", "sequenceDiagram", "stateDiagram", "stateDiagram-v2",
    "classDiagram", "erDiagram", "gantt", "pie", "journey", "mindmap",
)


def extract_mermaid_blocks(markdown: str) -> list[str]:
    """Return the inner Mermaid source of each ```mermaid fenced block."""
    blocks: list[str] = []
    for m in re.finditer(r"```mermaid\s*\n(.*?)```", markdown, re.DOTALL):
        blocks.append(m.group(1).strip())
    return blocks


def validate(mermaid_src: str) -> tuple[bool, str]:
    """Return (ok, reason). Ok requires a known head and balanced braces."""
    src = mermaid_src.strip()
    if not src:
        return False, "empty"
    first = src.splitlines()[0].strip()
    head = first.split()[0] if first.split() else ""
    if head not in _HEADS:
        return False, f"unknown diagram head: {head!r}"
    # erDiagram uses braces for attribute blocks that may legitimately be
    # unbalanced in partial output; don't reject on brace count alone.
    if head != "erDiagram" and src.count("{") != src.count("}"):
        return False, "unbalanced braces"
    if src.count("[[") != src.count("]]"):
        return False, "unbalanced [[ ]]"
    # flowchart/graph subgraphs must pair with end.
    if head in ("flowchart", "graph") and len(re.findall(r"\bsubgraph\b", src)) != len(re.findall(r"\bend\b", src)):
        return False, "unbalanced subgraph/end"
    return True, "ok"


def clean_llm_mermaid(raw: str) -> tuple[str | None, str]:
    """Accept raw LLM output; return (validated_src, reason).

    Strips a leading ```mermaid fence if the model wrapped its answer.
    """
    text = raw.strip()
    # Strip wrapping code fences if present.
    fence = re.match(r"^```(?:mermaid)?\s*\n(.*)\n```\s*$", text, re.DOTALL)
    if fence:
        text = fence.group(1).strip()
    ok, reason = validate(text)
    return (text if ok else None, reason)