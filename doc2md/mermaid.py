"""Deterministic Mermaid generation for *simple* text diagrams.

Complex text diagrams and all infographics are the skill's job (Claude).
"""

from __future__ import annotations

import re
from typing import Optional

from .detection import DiagramDetection


def generate_flowchart(text: str, title: Optional[str] = None) -> str:
    nodes: dict[str, str] = {}
    edges: list[tuple[str, str]] = []
    counter = 0

    arrow_patterns = [
        r"([A-Z][A-Za-z0-9_ ]+)\s*→\s*([A-Z][A-Za-z0-9_ ]+)",
        r"([A-Z][A-Za-z0-9_ ]+)\s*->\s*([A-Z][A-Za-z0-9_ ]+)",
        r"([A-Za-z]+)\s+feeds?\s+(?:into\s+)?([A-Za-z]+)",
        r"([A-Za-z]+)\s+triggers?\s+([A-Za-z]+)",
        r"([A-Za-z]+)\s+leads?\s+to\s+([A-Za-z]+)",
    ]
    for pattern in arrow_patterns:
        for source, target in re.findall(pattern, text, re.IGNORECASE):
            source = source.strip().replace(" ", "_")
            target = target.strip().replace(" ", "_")
            for name in (source, target):
                if name and name not in nodes:
                    nodes[name] = f"N{counter}"
                    counter += 1
            if source and target:
                edges.append((nodes[source], nodes[target]))

    step_markers = ["first", "then", "next", "after", "finally", "step", "phase"]
    steps: list[str] = []
    for line in text.split("\n"):
        low = line.lower().strip()
        if any(low.startswith(m) for m in step_markers):
            action = re.sub(
                r"^(first|then|next|after that|finally|step \d+|phase \d+)[,:\s]*", "", low
            ).strip()[:50]
            if action:
                nodes[action] = f"S{len(steps)}"
                steps.append(action)
    for i in range(len(steps) - 1):
        edges.append((f"S{i}", f"S{i + 1}"))

    if not nodes:
        return ""

    def _label(name: str) -> str:
        return name.replace("_", " ").replace('"', "'")

    out = ["```mermaid", "flowchart TD"]
    if title:
        out.append(f"    subgraph {title.replace(' ', '_')}")
    for name, node_id in nodes.items():
        out.append(f'    {node_id}["{_label(name)}"]')
    for source, target in edges:
        out.append(f"    {source} --> {target}")
    if title:
        out.append("    end")
    out.append("```")
    return "\n".join(out)


def generate_sequence(text: str) -> str:
    participants: list[str] = []
    messages: list[tuple[str, str]] = []
    patterns = [
        r"([A-Z][A-Za-z]+)\s+sends?\s+(?:to\s+)?([A-Z][A-Za-z]+)",
        r"([A-Z][A-Za-z]+)\s+→\s*([A-Z][A-Za-z]+)",
        r"([A-Z][A-Za-z]+)\s+requests?\s+(?:from\s+)?([A-Z][A-Za-z]+)",
        r"([A-Z][A-Za-z]+)\s+responds?\s+(?:to\s+)?([A-Z][A-Za-z]+)",
    ]
    for pattern in patterns:
        for source, target in re.findall(pattern, text):
            messages.append((source.strip(), target.strip()))
    if not messages:
        return ""
    for source, target in messages:
        for p in (source, target):
            if p not in participants:
                participants.append(p)

    out = ["```mermaid", "sequenceDiagram"]
    for p in participants:
        safe = p.replace(" ", "_")
        out.append(f"    participant {safe} as {p}")
    for i, (source, target) in enumerate(messages):
        src = source.replace(" ", "_")
        tgt = target.replace(" ", "_")
        out.append(f"    {src}->>{tgt}: message {i + 1}")
    out.append("```")
    return "\n".join(out)


def generate_simple(detection: DiagramDetection, text: str, *, title: Optional[str] = None) -> str:
    """Render deterministic Mermaid for a *simple* detection. Empty if none."""
    if detection.complexity != "simple":
        return ""
    if detection.diagram_type == "sequence":
        seq = generate_sequence(text)
        if seq:
            return seq
    return generate_flowchart(text, title=title)