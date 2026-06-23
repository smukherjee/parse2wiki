#!/usr/bin/env python3
"""
Shared document-to-markdown pipeline.

Builds combined markdown from extracted text, adds Mermaid for simple diagrams,
and optionally uses an LLM for complex diagram interpretation.
"""

import importlib
import os
from pathlib import Path
from typing import Optional

from .diagrams.detector import classify_complexity
from .diagrams.mermaid_gen import generate_mermaid_flowchart, generate_mermaid_sequence


def _normalize_title(source_path: str) -> str:
    """Generate a readable title from a source filename."""
    title = Path(source_path).stem.replace("-extracted", "")
    title = title.replace("_", " ").replace("-", " ").strip()
    return title.title() if title else Path(source_path).stem


def _generate_mermaid(text: str, diagram_type: Optional[str]) -> str:
    """Generate Mermaid from the extracted text."""
    if diagram_type == "sequence":
        return generate_mermaid_sequence(text)
    return generate_mermaid_flowchart(text)


def _generate_llm_mermaid(text: str, diagram_type: Optional[str], title: str) -> str:
    """Ask an LLM to turn complex extracted text into Mermaid."""
    api_key = os.environ.get("ANTHROPIC_KEY")
    if not api_key:
        return ""

    try:
        anthropic_module = importlib.import_module("anthropic")
        Client = getattr(anthropic_module, "Client")
        client = Client(api_key=api_key)

        response = client.messages.create(
            model=os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
            max_tokens=1200,
            system="Return only Mermaid code or a fenced Mermaid code block.",
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Convert this text into a {diagram_type or 'flowchart'} Mermaid diagram. "
                        f"Title: {title}\n\n{text[:12000]}"
                    ),
                }
            ],
        )

        content = response.content[0].text.strip()
        if content.startswith("```"):
            return content
        return f"```mermaid\n{content}\n```"
    except Exception:
        return ""


def build_document_markdown(source_path: str, extracted_text: str) -> str:
    """Build the final combined markdown for a document."""
    title = _normalize_title(source_path)
    text = extracted_text.strip() if extracted_text else "No text content found."

    parts = [
        f"# {title}",
        "",
        "## Extracted Text",
        "",
        text,
    ]

    detection = classify_complexity(text)
    mermaid = ""

    if detection["llm_required"]:
        mermaid = _generate_llm_mermaid(text, detection.get("diagram_type"), title)
        if not mermaid:
            mermaid = _generate_mermaid(text, detection.get("diagram_type"))
    elif detection["complexity"] == "simple":
        mermaid = _generate_mermaid(text, detection.get("diagram_type"))

    if mermaid:
        parts.extend(["", "## Mermaid Diagram", "", mermaid])

    return "\n".join(parts).rstrip() + "\n"


def write_document_markdown(output_dir: str, source_path: str, extracted_text: str) -> Path:
    """Write the combined markdown to <original>-extracted.md."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    output_name = Path(source_path).stem
    output_file = output_path / f"{output_name}-extracted.md"
    output_file.write_text(build_document_markdown(source_path, extracted_text))
    return output_file