#!/usr/bin/env python3
"""
LLM-assisted summarization for wiki source pages.

Token-optimized with schema-constrained extraction.
"""

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class SummarizerConfig:
    """Configuration for LLM summarization."""
    model: str = "claude-sonnet-4-6"
    max_tokens: int = 2000
    only_complex_diagrams: bool = True
    batch_size: int = 10


# Schema-constrained system prompt (minimizes tokens)
SYSTEM_PROMPT = """
You are a technical documentation summarizer. Extract structured data from document text.

Return ONLY valid JSON matching this schema:
{
    "title": "Document title (infer from content)",
    "type": "source-summary",
    "doc_type": "product-datasheet|workflow-diagram|user-manual|spec|release-notes|other",
    "products": ["product1", "product2"],
    "key_claims": ["claim1 (<20 words)", "claim2"],
    "versions": ["v1.0", "v2.3"],
    "diagram_type": "flowchart|sequence|state|architecture|none",
    "confidence": "high|medium|low"
}

Rules:
- No prose, only JSON
- key_claims: max 5 bullets, each <20 words
- products: only RESA products (CREWS, VISTA, INFOPAX, etc.) or clearly named systems
- If uncertain, use "other" for doc_type, "none" for diagram_type, "low" for confidence
"""


def summarize_for_wiki(
    text: str,
    source_path: str,
    config: Optional[SummarizerConfig] = None
) -> Dict[str, Any]:
    """
    Generate a wiki source summary from extracted text.

    Args:
        text: Extracted document text
        source_path: Path to original source (for backlink)
        config: Summarizer configuration

    Returns:
        Dict with frontmatter fields and summary content
    """
    config = config or SummarizerConfig()

    # Try to use Claude API if available
    try:
        from anthropic import Client
        client = Client(api_key=os.environ.get("ANTHROPIC_KEY"))

        response = client.messages.create(
            model=config.model,
            max_tokens=config.max_tokens,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": f"Summarize this document:\n\n{text[:8000]}"}  # Truncate long docs
            ]
        )

        # Parse JSON response
        content = response.content[0].text
        result = json.loads(content)

    except ImportError:
        result = _fallback_summarization(text, source_path)
    except json.JSONDecodeError:
        result = _fallback_summarization(text, source_path)
    except Exception as e:
        result = {
            "title": Path(source_path).stem,
            "type": "source-summary",
            "doc_type": "other",
            "products": [],
            "key_claims": [f"Extraction error: {e}"],
            "versions": [],
            "diagram_type": "none",
            "confidence": "low"
        }

    return result


def _fallback_summarization(text: str, source_path: str) -> Dict[str, Any]:
    """
    Fallback summarization without LLM (rule-based).

    Uses keyword matching and heuristics.
    """
    text_lower = text.lower()

    # Detect product names
    RESA_PRODUCTS = [
        'crews', 'vista', 'infopax', 'fairway', 'bagera', 'bagway',
        'paxtrack', 'clever', 'invoice', 'on-board', 'layer-one',
        'on board', 'ldcs', 'cuss', 'sbd', 'aims', 'gaims'
    ]

    products = [p.upper() for p in RESA_PRODUCTS if p in text_lower]

    # Detect document type
    if 'workflow' in text_lower or 'flowchart' in text_lower:
        doc_type = 'workflow-diagram'
        diagram_type = 'flowchart'
    elif 'datasheet' in text_lower or 'data sheet' in text_lower:
        doc_type = 'product-datasheet'
        diagram_type = 'none'
    elif 'user' in text_lower and ('manual' in text_lower or 'guide' in text_lower):
        doc_type = 'user-manual'
        diagram_type = 'none'
    elif 'spec' in text_lower or 'specification' in text_lower:
        doc_type = 'spec'
        diagram_type = 'none'
    else:
        doc_type = 'other'
        diagram_type = 'none'

    # Extract version numbers
    import re
    versions = re.findall(r'[vV]\d+\.\d+', text)
    versions = list(set(versions))[:3]  # Dedupe, max 3

    # Extract key claims (first sentence of each paragraph, truncated)
    key_claims = []
    for para in text.split('\n\n'):
        para = para.strip()
        if para and len(para) > 20:
            first_sentence = para.split('.')[0] + '.'
            if len(first_sentence) < 100:
                key_claims.append(first_sentence)
            if len(key_claims) >= 5:
                break

    return {
        "title": Path(source_path).stem.replace('-extracted', '').replace('_', ' ').title(),
        "type": "source-summary",
        "doc_type": doc_type,
        "products": products,
        "key_claims": key_claims,
        "versions": versions,
        "diagram_type": diagram_type,
        "confidence": "medium"
    }


def generate_wiki_source_page(
    summary: Dict[str, Any],
    source_path: str,
    created_date: str
) -> str:
    """
    Generate a complete wiki source page with frontmatter.

    Args:
        summary: Output from summarize_for_wiki()
        source_path: Original source file path
        created_date: Date string (YYYY-MM-DD)

    Returns:
        Complete markdown page content
    """
    # Generate frontmatter
    frontmatter = f"""---
title: {summary['title']}
type: {summary['type']}
sources:
  - {source_path}
related: []
created: {created_date}
updated: {created_date}
confidence: {summary['confidence']}
---

"""

    # Generate body
    body_parts = []

    if summary.get('doc_type'):
        body_parts.append(f"**Document Type:** {summary['doc_type']}\n")

    if summary.get('products'):
        body_parts.append(f"**Products:** {', '.join(summary['products'])}\n")

    if summary.get('versions'):
        body_parts.append(f"**Versions:** {', '.join(summary['versions'])}\n")

    if summary.get('key_claims'):
        body_parts.append("## Key Takeaways\n\n")
        for claim in summary['key_claims']:
            body_parts.append(f"- {claim}\n")

    if summary.get('diagram_type') and summary['diagram_type'] != 'none':
        body_parts.append(f"\n**Diagram Type:** {summary['diagram_type']}\n")

    body = "\n".join(body_parts)

    return frontmatter + body
