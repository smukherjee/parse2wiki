#!/usr/bin/env python3
"""
Detect diagram and workflow content in extracted text.

Classifies as:
- simple: Can be converted to Mermaid deterministically (0 tokens)
- complex: Requires LLM interpretation (token cost)
"""

import re
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class DiagramDetection:
    """Result of diagram detection."""
    has_diagram: bool
    diagram_type: Optional[str]  # flowchart, sequence, state, class, er
    complexity: str  # simple, complex
    confidence: float  # 0.0 to 1.0
    keywords_found: List[str]
    component_count: int
    connection_count: int
    reasons: List[str]


# Keywords that indicate diagram/workflow content
DIAGRAM_KEYWORDS = {
    'flowchart': ['workflow', 'flow', 'process', 'steps', 'phase', 'stage', 'then', 'next'],
    'sequence': ['sequence', 'messages', 'exchange', 'request', 'response', 'send', 'receive'],
    'state': ['state', 'status', 'transition', 'initial', 'final', 'pending', 'active'],
    'class': ['class', 'interface', 'extends', 'implements', 'attributes', 'methods'],
    'er': ['entity', 'relationship', 'table', 'primary key', 'foreign key', 'references'],
    'architecture': ['architecture', 'component', 'layer', 'tier', 'module', 'system', 'integration'],
}

# Patterns that indicate connections/arrows
CONNECTION_PATTERNS = [
    r'→', r'←', r'↔', r'⇒', r'⇐', r'⇔',  # Unicode arrows
    r'->', r'<-', r'<->', r'=>', r'<=', r'<=>',  # ASCII arrows
    r'\[.+\]\s*--+\s*\[.+\]',  # Mermaid-style connections
    r'.+\s+leads to\s+.+',
    r'.+\s+triggers\s+.+',
    r'.+\s+feeds\s+.+',
]

# Patterns indicating complex branching
COMPLEX_PATTERNS = [
    r'if.*then.*else',
    r'switch.*case',
    r'decision.*branch',
    r'parallel|concurrent|async',
    r'loop.*until|while.*do|for.*each',
    r'fork|join|merge',
]


def detect_diagrams(text: str) -> DiagramDetection:
    """Detect if text contains diagram/workflow content."""
    text_lower = text.lower()

    # Find matching keywords
    keywords_found = []
    diagram_types = []

    for dtype, keywords in DIAGRAM_KEYWORDS.items():
        matches = [kw for kw in keywords if kw in text_lower]
        if matches:
            keywords_found.extend(matches)
            diagram_types.append(dtype)

    # Count components and connections
    component_count = len(re.findall(r'\b[A-Z][A-Za-z0-9_]+\b', text))  # CamelCase identifiers
    connection_count = 0
    for pattern in CONNECTION_PATTERNS:
        connection_count += len(re.findall(pattern, text))

    # Check for complex patterns
    has_complex = any(re.search(p, text_lower) for p in COMPLEX_PATTERNS)

    # Determine if this is diagram content
    has_diagram = len(keywords_found) >= 2 or connection_count >= 3

    # Classify complexity
    if has_complex or connection_count > 10 or component_count > 20:
        complexity = "complex"
        confidence = 0.8
    elif has_diagram:
        complexity = "simple"
        confidence = 0.9
    else:
        complexity = "none"
        confidence = 0.5

    # Build reasons
    reasons = []
    if keywords_found:
        reasons.append(f"Keywords: {', '.join(set(keywords_found))}")
    if connection_count > 0:
        reasons.append(f"Connections: {connection_count} arrows/links detected")
    if has_complex:
        reasons.append("Complex branching logic detected")
    if component_count > 20:
        reasons.append(f"Many components: {component_count} potential entities")

    primary_type = diagram_types[0] if diagram_types else None

    return DiagramDetection(
        has_diagram=has_diagram,
        diagram_type=primary_type,
        complexity=complexity,
        confidence=confidence,
        keywords_found=list(set(keywords_found)),
        component_count=component_count,
        connection_count=connection_count,
        reasons=reasons
    )


def classify_complexity(text: str) -> dict:
    """
    Classify diagram complexity for LLM routing.

    Returns:
        dict with keys: complexity, llm_required, estimated_tokens
    """
    detection = detect_diagrams(text)

    result = {
        'complexity': detection.complexity,
        'llm_required': detection.complexity == 'complex',
        'estimated_tokens': 0,
        'diagram_type': detection.diagram_type,
    }

    if detection.complexity == 'complex':
        # Estimate based on component count
        result['estimated_tokens'] = 500 + (detection.component_count * 20)
        result['reason'] = "Complex diagram requires LLM interpretation"
    elif detection.complexity == 'simple':
        result['reason'] = "Simple diagram - deterministic Mermaid generation"
    else:
        result['reason'] = "No clear diagram structure detected"

    return result
