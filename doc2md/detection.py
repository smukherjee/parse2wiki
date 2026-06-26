"""Diagram detection — classify extracted text as simple / complex / none.

One call returns a typed :class:`DiagramDetection` that routes Mermaid
generation: ``simple`` → deterministic generator; ``complex`` → the skill's
Claude Mermaid; ``none`` → no diagram. (Image diagrams bypass this — all
infographics go to Claude vision regardless.)

Design rules (generalise, don't patch one doc):

* A diagram is **named nodes connected by edges**. Diagram-ness is therefore
  established by *structural* evidence — arrow/connection patterns, explicit
  branching language (if/then/else, parallel, fork), or a linear step sequence
  (first/then/next/...). Keyword presence alone never establishes a diagram:
  a table full of "Status: Active" rows has the words but no edges.
* Escalating to the LLM (``complex``) requires a diagram to exist *and* enough
  degree (many distinct nodes, many edges, or branching text). A single proxy
  signal — e.g. a high acronym count — never spends LLM tokens on its own.
* Components are counted **distinct**, not by occurrence, so a table repeating
  ``TDS`` 200× counts as one component, not 200.
* Keywords match on **word boundaries** with light inflectional suffixes, so
  ``state`` no longer matches ``statement`` and ``flow`` no longer matches
  ``flower``.
* ``diagram_type`` is picked by keyword-match score, not by dict iteration
  order, and only assigned once diagram-ness is established.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

DIAGRAM_KEYWORDS: dict[str, list[str]] = {
    "flowchart": ["workflow", "flow", "process", "steps", "phase", "stage", "then", "next"],
    "sequence": ["sequence", "messages", "exchange", "request", "response", "send", "receive"],
    "state": ["state", "status", "transition", "initial", "final", "pending", "active"],
    "class": ["class", "interface", "extends", "implements", "attributes", "methods"],
    "er": ["entity", "relationship", "table", "primary key", "foreign key", "references"],
    "architecture": ["architecture", "component", "layer", "tier", "module", "system", "integration", "depends"],
}

CONNECTION_PATTERNS = [
    r"→", r"←", r"↔", r"⇒", r"⇐", r"⇔",
    r"->", r"<-", r"<->", r"=>", r"<=", r"<=>",
    r"\[.+\]\s*--+\s*\[.+\]",
    r".+\s+leads to\s+.+",
    r".+\s+triggers\s+.+",
    r".+\s+feeds\s+.+",
]

# Relational verbs that express a structural relationship between two named
# entities (class hierarchy, interface realization, dependency, composition,
# reference). These recover diagrams from prose that has no arrow characters.
# Operands are constrained to Capitalized names (``[A-Z][A-Za-z0-9_]+``) so
# prose false positives like "the report extends the analysis" (lowercase
# operands) don't fire — the operand must sit immediately adjacent to the verb.
RELATIONAL_PATTERNS = [
    r"([A-Z][A-Za-z0-9_]+)\s+extends?\s+([A-Z][A-Za-z0-9_]+)",
    r"([A-Z][A-Za-z0-9_]+)\s+implements?\s+([A-Z][A-Za-z0-9_]+)",
    r"([A-Z][A-Za-z0-9_]+)\s+inherits\s+from\s+([A-Z][A-Za-z0-9_]+)",
    r"([A-Z][A-Za-z0-9_]+)\s+derives\s+from\s+([A-Z][A-Za-z0-9_]+)",
    r"([A-Z][A-Za-z0-9_]+)\s+depends\s+on\s+([A-Z][A-Za-z0-9_]+)",
    r"([A-Z][A-Za-z0-9_]+)\s+references?\s+([A-Z][A-Za-z0-9_]+)",
    r"([A-Z][A-Za-z0-9_]+)\s+(?:is\s+)?part\s+of\s+([A-Z][A-Za-z0-9_]+)",
    r"([A-Z][A-Za-z0-9_]+)\s+(?:consists|composed)\s+of\s+([A-Z][A-Za-z0-9_]+)",
]

COMPLEX_PATTERNS = [
    r"\bif\b.*\bthen\b.*\belse\b",
    r"\bswitch\b.*\bcase\b",
    r"\bdecision\b.*\bbranch\b",
    r"\b(parallel|concurrent|async)\b",
    r"\bloop\b.*\buntil\b|\bwhile\b.*\bdo\b|\bfor\b.*\beach\b",
    r"\b(fork|join|merge)\b",
]

# A line that opens a linear-process step. Two or more of these is a simple
# diagram signal even without arrow characters.
_STEP_MARKER = re.compile(
    r"^\s*(?:first|then|next|after that|after|finally|step\s+\d+|phase\s+\d+)\b",
    re.IGNORECASE,
)

# CamelCase (leading-Capital or lowercase-led) / ALL-CAPS acronyms (2+ caps)
# / snake_case identifiers — real component names. Plain Capitalised Words
# like "The"/"And"/"It"/"First" have no internal capital, no underscore, and
# fewer than 2 capitals, so they do not count.
_COMPONENT_RE = re.compile(
    r"\b(?:[A-Za-z][a-z0-9]+[A-Z][A-Za-z0-9]*|[A-Z]{2,}[A-Za-z0-9]*|[A-Za-z]+_[A-Za-z0-9]+)\b"
)

# Word-boundary keyword match with light inflectional suffix, so "class"
# matches "classes"/"classed" but "state" does not match "statement".
_KW_RE_CACHE: dict[str, re.Pattern] = {}


def _keyword_re(kw: str) -> re.Pattern:
    pat = _KW_RE_CACHE.get(kw)
    if pat is None:
        pat = re.compile(r"\b" + re.escape(kw) + r"(?:s|es|ed|ing)?\b", re.IGNORECASE)
        _KW_RE_CACHE[kw] = pat
    return pat


@dataclass
class DiagramDetection:
    has_diagram: bool
    diagram_type: Optional[str]
    complexity: str  # "simple" | "complex" | "none"
    confidence: float
    keywords_found: list[str] = field(default_factory=list)
    component_count: int = 0
    connection_count: int = 0
    reasons: list[str] = field(default_factory=list)

    @property
    def llm_required(self) -> bool:
        return self.complexity == "complex"


def detect_diagrams(text: str) -> DiagramDetection:
    text_lower = text.lower()

    # Keywords — word-boundary match (R3). Collected to *type* a diagram; they
    # do not establish diagram-ness on their own (R2).
    type_matches: dict[str, int] = {}
    keywords_found: list[str] = []
    for dtype, keywords in DIAGRAM_KEYWORDS.items():
        count = 0
        for kw in keywords:
            if _keyword_re(kw).search(text):
                count += 1
                keywords_found.append(kw)
        if count:
            type_matches[dtype] = count

    # Components — distinct count (R1).
    component_count = len(set(re.findall(_COMPONENT_RE, text)))
    arrow_count = sum(len(re.findall(p, text)) for p in CONNECTION_PATTERNS)
    relational_count = sum(len(re.findall(p, text)) for p in RELATIONAL_PATTERNS)
    connection_count = arrow_count + relational_count
    has_complex = any(re.search(p, text_lower) for p in COMPLEX_PATTERNS)
    step_count = sum(1 for ln in text.split("\n") if _STEP_MARKER.match(ln))

    # Diagram-ness requires STRUCTURE: edges (arrows or relational verbs),
    # branching text, or a step sequence (R2). Keyword presence alone is not a
    # diagram. Two relational verbs is a real class/dependency/composition
    # structure even with zero arrow characters.
    has_diagram = (
        arrow_count >= 3
        or relational_count >= 2
        or has_complex
        or step_count >= 2
    )

    # Complexity — only escalate when a diagram exists. A single node-count
    # proxy never escalates on its own: distinct components > 20 only counts
    # toward `complex` when there are also edges (a real graph). Relational-verb
    # prose (class / ER / dependency / composition) routes to Claude: the
    # deterministic generator renders only flowchart (arrows/steps) and
    # sequence, so a relational diagram with few arrows has no deterministic
    # renderer.
    if not has_diagram:
        complexity, confidence = "none", 0.5
    elif has_complex or connection_count > 10 or (
        component_count > 20 and connection_count >= 3
    ):
        complexity, confidence = "complex", 0.8
    elif relational_count >= 2 and arrow_count < 3:
        complexity, confidence = "complex", 0.8
    else:
        complexity, confidence = "simple", 0.9

    # diagram_type — highest keyword-match score, dict order breaks ties
    # (flowchart first). Only assigned once diagram-ness is established; an
    # edge-only diagram with no keyword hits defaults to flowchart (R5).
    diagram_type: Optional[str] = None
    if has_diagram:
        best_type, best_count = None, 0
        for dtype in DIAGRAM_KEYWORDS:  # dict order → deterministic tie-break
            c = type_matches.get(dtype, 0)
            if c > best_count:
                best_type, best_count = dtype, c
        diagram_type = best_type or "flowchart"

    reasons: list[str] = []
    if keywords_found:
        reasons.append(f"Keywords: {', '.join(sorted(set(keywords_found)))}")
    if connection_count:
        reasons.append(f"Connections: {arrow_count} arrows + {relational_count} relational = {connection_count} edges")
    if step_count >= 2:
        reasons.append(f"Linear process: {step_count} step markers")
    if has_complex:
        reasons.append("Complex branching logic")
    if component_count > 20:
        reasons.append(f"Many components: {component_count} distinct entities")

    return DiagramDetection(
        has_diagram=has_diagram,
        diagram_type=diagram_type,
        complexity=complexity,
        confidence=confidence,
        keywords_found=sorted(set(keywords_found)),
        component_count=component_count,
        connection_count=connection_count,
        reasons=reasons,
    )