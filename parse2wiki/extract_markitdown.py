#!/usr/bin/env python3
"""
Extract text using MarkItDown and PyMuPDF4LLM.

This backend is optimized for richer Markdown output from modern document
parsers while keeping the same directory traversal and extraction contract as
the classic extractor.
"""

import json
import os
import os
import importlib
import tempfile
import zipfile
from pathlib import Path
from typing import Optional

from .diagrams.detector import classify_complexity
from .diagrams.mermaid_gen import generate_mermaid_flowchart, generate_mermaid_sequence


def _extract_with_markitdown(file_path: str) -> str:
    """Convert a file to markdown using MarkItDown."""
    try:
        markitdown_module = importlib.import_module("markitdown")
        MarkItDown = getattr(markitdown_module, "MarkItDown")
        converter = MarkItDown()
        result = converter.convert(file_path)

        for attribute in ("text_content", "markdown", "text"):
            content = getattr(result, attribute, None)
            if isinstance(content, str) and content.strip():
                return content

        if isinstance(result, str) and result.strip():
            return result

        return "No text content found."
    except ImportError:
        return "MarkItDown not available (install parse2wiki[modern])."
    except Exception as exc:
        return f"MarkItDown extraction failed: {exc}"


def extract_pdf_ocr(pdf_path: str, page_num: Optional[int] = None) -> str:
    """Extract text from a PDF page using Tesseract OCR."""
    try:
        pdf2image = importlib.import_module("pdf2image")
        pytesseract = importlib.import_module("pytesseract")

        if page_num:
            images = pdf2image.convert_from_path(
                pdf_path,
                first_page=page_num,
                last_page=page_num,
                dpi=300,
            )
        else:
            images = pdf2image.convert_from_path(pdf_path, dpi=300)

        result = []
        for index, image in enumerate(images):
            text = pytesseract.image_to_string(image)
            if text.strip():
                result.append(f"Page {page_num or index + 1} (OCR): {text}")

        return "\n".join(result)
    except ImportError:
        return "OCR not available (install pdf2image and pytesseract)."
    except Exception as exc:
        return f"OCR failed: {exc}"


def extract_pdf_text(pdf_path: str, ocr: bool = False) -> str:
    """Extract PDF text using PyMuPDF4LLM with MarkItDown and OCR fallback."""
    try:
        pymupdf4llm = importlib.import_module("pymupdf4llm")
        markdown = pymupdf4llm.to_markdown(pdf_path)
        if isinstance(markdown, str) and markdown.strip():
            return markdown
    except ImportError:
        pass
    except Exception:
        pass

    if ocr:
        ocr_text = extract_pdf_ocr(pdf_path)
        if ocr_text and "failed" not in ocr_text.lower():
            return f"## Extracted with OCR\n\n{ocr_text}"

    return _extract_with_markitdown(pdf_path)


def _render_mermaid(text: str, diagram_type: Optional[str]) -> str:
    """Render a Mermaid block using the best available deterministic generator."""
    if diagram_type == "sequence":
        return generate_mermaid_sequence(text)

    return generate_mermaid_flowchart(text)


def _generate_llm_interpretation(text: str, diagram_type: Optional[str]) -> Optional[dict]:
    """Use an LLM to produce a concise interpretation and Mermaid when diagrams are complex."""
    try:
        anthropic_module = importlib.import_module("anthropic")
        Client = getattr(anthropic_module, "Client")
        client = Client(api_key=os.environ.get("ANTHROPIC_KEY"))

        if not os.environ.get("ANTHROPIC_KEY"):
            return None

        prompt = (
            "You convert extracted document text into a compact markdown interpretation. "
            "Return ONLY valid JSON with keys: summary, mermaid. "
            "summary must be a short markdown paragraph or bullet list. "
            "mermaid must be a valid Mermaid diagram block as a plain string without backticks. "
            f"Use a {diagram_type or 'flowchart'} representation when possible.\n\n"
            f"Document text:\n{text[:12000]}"
        )

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1200,
            messages=[{"role": "user", "content": prompt}],
        )

        content = response.content[0].text
        payload = json.loads(content)

        summary = str(payload.get("summary", "")).strip()
        mermaid = str(payload.get("mermaid", "")).strip()

        if summary and mermaid:
            return {"summary": summary, "mermaid": mermaid}

        return None
    except ImportError:
        return None
    except Exception:
        return None


def build_combined_markdown(file_path: str, extracted_text: str, ocr: bool = False) -> str:
    """Combine extracted text with Mermaid output and optional LLM interpretation."""
    title = Path(file_path).stem
    detection = classify_complexity(extracted_text)
    source_text = extracted_text.strip() or "No text content found."

    parts = [f"# {title}", "", "## Extracted Text", "", source_text]

    if detection["llm_required"]:
        llm_output = _generate_llm_interpretation(source_text, detection.get("diagram_type"))
        if llm_output:
            parts.extend(
                [
                    "",
                    "## LLM Interpretation",
                    "",
                    llm_output["summary"],
                    "",
                    "## Mermaid Diagram",
                    "",
                    llm_output["mermaid"],
                ]
            )
            return "\n".join(parts)

    if detection["complexity"] == "simple":
        parts.extend(
            [
                "",
                "## Mermaid Diagram",
                "",
                _render_mermaid(source_text, detection.get("diagram_type")),
            ]
        )

    return "\n".join(parts)


def _write_output_markdown(output_dir: str, source_name: str, content: str) -> Path:
    """Write combined markdown for one source document."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / f"{source_name}-extracted.md"
    output_file.write_text(content)
    return output_file


def extract_file(file_path: str, ocr: bool = False) -> str:
    """Extract text from a single file based on extension."""
    ext = Path(file_path).suffix.lower()

    extractors = {
        ".pdf": lambda path: extract_pdf_text(path, ocr),
        ".docx": _extract_with_markitdown,
        ".pptx": _extract_with_markitdown,
        ".xlsx": _extract_with_markitdown,
    }

    extractor = extractors.get(ext)
    if extractor:
        return extractor(file_path)

    return f"Unsupported file type: {ext}"


def extract_zip_contents(zip_path: str, output_dir: str, ocr: bool = False) -> list:
    """Extract ZIP contents and process nested files with the modern backend."""
    extracted_files = []

    with zipfile.ZipFile(zip_path, "r") as zip_file:
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_file.extractall(tmpdir)

            for root, _, files in os.walk(tmpdir):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    rel_path = os.path.relpath(file_path, tmpdir)
                    source_name = Path(rel_path).stem

                    ext = Path(file_name).suffix.lower()
                    if ext in [".pdf", ".docx", ".pptx", ".xlsx"]:
                        extracted_text = extract_file(file_path, ocr)
                        combined = build_combined_markdown(file_path, extracted_text, ocr)
                        output_file = _write_output_markdown(output_dir, source_name, combined)
                        extracted_files.append(
                            {
                                "path": f"{zip_path}/{rel_path}",
                                "output": str(output_file),
                                "extension": ext,
                                "status": "extracted",
                            }
                        )

    return extracted_files


def process_directory(
    input_dir: str,
    output_dir: str,
    dry_run: bool = False,
    ocr: bool = False,
) -> list:
    """Process supported files in a directory recursively."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    if not dry_run:
        output_path.mkdir(parents=True, exist_ok=True)

    results = []

    for file_path in input_path.rglob("*"):
        if file_path.is_file():
            ext = file_path.suffix.lower()

            if ext == ".zip":
                if dry_run:
                    results.append({"path": str(file_path), "status": "would_extract_zip"})
                else:
                    zip_results = extract_zip_contents(str(file_path), str(output_path), ocr)
                    results.extend(zip_results)
            elif ext in [".pdf", ".docx", ".pptx", ".xlsx"]:
                if dry_run:
                    results.append({"path": str(file_path), "status": "would_extract"})
                else:
                    extracted_text = extract_file(str(file_path), ocr)
                    combined = build_combined_markdown(str(file_path), extracted_text, ocr)
                    output_file = _write_output_markdown(str(output_path), file_path.stem, combined)
                    results.append(
                        {
                            "path": str(file_path),
                            "output": str(output_file),
                            "status": "extracted",
                        }
                    )

    return results