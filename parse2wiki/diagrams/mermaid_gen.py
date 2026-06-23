#!/usr/bin/env python3
"""
Generate Mermaid diagrams from extracted text.

Zero-token deterministic generation for simple diagrams.
"""

import re
from typing import List, Optional, Tuple


def generate_mermaid_flowchart(text: str, title: Optional[str] = None) -> str:
    """
    Generate a Mermaid flowchart from text.

    Detects:
    - Arrow connections (→, ->, leads to, etc.)
    - Step sequences (First, Then, Next, Finally)
    - Component lists
    """
    nodes = {}
    edges = []
    node_counter = 0

    # Pattern 1: Arrow connections
    arrow_patterns = [
        (r'([A-Z][A-Za-z0-9_ ]+)\s*→\s*([A-Z][A-Za-z0-9_ ]+)', 'unicode'),
        (r'([A-Z][A-Za-z0-9_ ]+)\s*->\s*([A-Z][A-Za-z0-9_ ]+)', 'ascii'),
        (r'([A-Za-z]+)\s+feeds?\s+(?:into\s+)?([A-Za-z]+)', 'feeds'),
        (r'([A-Za-z]+)\s+triggers?\s+([A-Za-z]+)', 'triggers'),
        (r'([A-Za-z]+)\s+leads?\s+to\s+([A-Za-z]+)', 'leads'),
    ]

    for pattern, _ in arrow_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for source, target in matches:
            source = source.strip().replace(' ', '_')
            target = target.strip().replace(' ', '_')

            if source not in nodes:
                nodes[source] = f"N{node_counter}"
                node_counter += 1
            if target not in nodes:
                nodes[target] = f"N{node_counter}"
                node_counter += 1

            edges.append((nodes[source], nodes[target]))

    # Pattern 2: Step sequences
    step_markers = ['first', 'then', 'next', 'after', 'finally', 'step', 'phase']
    lines = text.split('\n')
    steps = []

    for line in lines:
        line_lower = line.lower().strip()
        if any(line_lower.startswith(m) for m in step_markers):
            # Extract the action
            action = re.sub(r'^(first|then|next|after that|finally|step \d+|phase \d+)[,:\s]*', '', line_lower)
            action = action.strip()[:50]  # Truncate long descriptions
            if action:
                step_id = f"step_{len(steps)}"
                nodes[step_id] = f"S{len(steps)}"
                steps.append(action)

    # Connect steps in sequence
    for i in range(len(steps) - 1):
        edges.append((f"S{i}", f"S{i + 1}"))

    # Build Mermaid output
    result = ["```mermaid", "flowchart TD"]

    if title:
        result.append(f"    subgraph {title.replace(' ', '_')}")

    # Add nodes with labels
    for name, node_id in nodes.items():
        label = name.replace('_', ' ')
        result.append(f"    {node_id}[{label}]")

    # Add edges
    for source, target in edges:
        result.append(f"    {source} --> {target}")

    if title:
        result.append("    end")

    result.append("```")

    return "\n".join(result)


def generate_mermaid_sequence(text: str, participants: Optional[List[str]] = None) -> str:
    """
    Generate a Mermaid sequence diagram from text.

    Detects:
    - Message exchanges (A sends to B, A → B)
    - Request/response patterns
    """
    participants = participants or []
    messages = []

    # Pattern: "A sends to B" or "A → B"
    patterns = [
        r'([A-Z][A-Za-z]+)\s+sends?\s+(?:to\s+)?([A-Z][A-Za-z]+)',
        r'([A-Z][A-Za-z]+)\s+→\s+([A-Z][A-Za-z]+)',
        r'([A-Z][A-Za-z]+)\s+requests?\s+(?:from\s+)?([A-Z][A-Za-z]+)',
        r'([A-Z][A-Za-z]+)\s+responds?\s+(?:to\s+)?([A-Z][A-Za-z]+)',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text)
        for source, target in matches:
            messages.append((source.strip(), target.strip(), "message"))

    if not participants and messages:
        # Extract unique participants
        for source, target, _ in messages:
            if source not in participants:
                participants.append(source)
            if target not in participants:
                participants.append(target)

    # Build Mermaid output
    result = ["```mermaid", "sequenceDiagram"]

    for p in participants:
        result.append(f"    participant {p.replace(' ', '_')} as {p[:3].upper()}")

    for i, (source, target, msg_type) in enumerate(messages):
        src = source.replace(' ', '_')[:3].upper()
        tgt = target.replace(' ', '_')[:3].upper()
        result.append(f"    {src}->>{tgt}: Message {i + 1}")

    result.append("```")

    return "\n".join(result)


def extract_components_for_mermaid(text: str) -> dict:
    """
    Extract structured components for Mermaid generation.

    Returns dict with: nodes, edges, type
    """
    components = {
        'nodes': [],
        'edges': [],
        'type': 'flowchart',
        'subgraphs': {}
    }

    # Extract layer/subsystem indicators
    layer_keywords = ['input', 'processing', 'output', 'layer', 'tier', 'system']
    current_layer = None

    for line in text.split('\n'):
        line_lower = line.lower()

        # Detect layer changes
        for kw in layer_keywords:
            if kw in line_lower and ':' in line:
                current_layer = line.split(':')[0].strip()
                components['subgraphs'][current_layer] = []

        # Extract potential nodes (capitalized terms)
        nodes_in_line = re.findall(r'\b[A-Z][A-Za-z0-9_]{2,}\b', line)
        for node in nodes_in_line:
            if node not in [n['id'] for n in components['nodes']]:
                components['nodes'].append({'id': node, 'label': node})
                if current_layer:
                    components['subgraphs'].setdefault(current_layer, []).append(node)

        # Extract edges
        for pattern in [r'→', r'->', r'⇒']:
            if pattern in line:
                parts = line.split(pattern)
                if len(parts) == 2:
                    source_match = re.search(r'([A-Z][A-Za-z0-9_]+)', parts[0])
                    target_match = re.search(r'([A-Z][A-Za-z0-9_]+)', parts[1])
                    if source_match and target_match:
                        components['edges'].append({
                            'source': source_match.group(1),
                            'target': target_match.group(1)
                        })

    return components
