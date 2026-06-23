#!/usr/bin/env python3
"""
CLI entry points for parse2wiki.

Commands:
- parse2wiki-check: Check for new/unprocessed files
- parse2wiki-extract: Extract text from documents
- parse2wiki-extract-markitdown: Extract text using MarkItDown and PyMuPDF4LLM
- parse2wiki-ingest: Generate wiki summaries and update index
"""

import json
import os
from datetime import date
from pathlib import Path

import click
import yaml

from .extract import process_directory, extract_file
from .extract_markitdown import process_directory as process_directory_markitdown
from .diagrams.detector import detect_diagrams, classify_complexity
from .diagrams.mermaid_gen import generate_mermaid_flowchart
from .summarizer.wiki_summary import summarize_for_wiki, generate_wiki_source_page, SummarizerConfig
from .wiki.ingester import WikiIngester, WikiConfig


def load_config(config_path: str) -> dict:
    """Load configuration from YAML file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """parse2wiki - Convert documents to wiki-ready markdown."""
    pass


@cli.command("check")
@click.option("--config", "-c", required=True, help="Path to config file")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def check(config: str, as_json: bool):
    """Check for new/unprocessed files in source directory."""
    cfg = load_config(config)
    base = Path(cfg['project']['base_path'])
    input_dir = base / cfg['sources']['input_dir']

    sources_dir = base / cfg['wiki']['path'] / cfg['wiki']['sources_dir']

    # Find all supported files
    extensions = ['.pdf', '.docx', '.pptx', '.xlsx', '.zip']
    all_files = []
    for ext in extensions:
        all_files.extend(input_dir.rglob(f'*{ext}'))

    # Check which are already processed
    new_files = []
    for f in all_files:
        # Generate expected output filename
        name = f.stem.replace('_US', '').replace('_UK', '')
        name = name.replace('_', '-').replace(' ', '-').lower()
        name = f"{name}.md"

        output_path = sources_dir / name
        if not output_path.exists():
            new_files.append(str(f))

    if as_json:
        print(json.dumps({"new_files": new_files, "count": len(new_files)}))
    else:
        print(f"Found {len(new_files)} new/unprocessed files:")
        for f in new_files[:20]:
            print(f"  - {f}")
        if len(new_files) > 20:
            print(f"  ... and {len(new_files) - 20} more")


@cli.command("extract")
@click.option("--input", "-i", "input_dir", required=True, help="Input directory")
@click.option("--output", "-o", "output_dir", help="Output directory")
@click.option("--ocr", is_flag=True, help="Enable OCR for PDFs")
@click.option("--dry-run", is_flag=True, help="Show what would be processed")
@click.option("--config", "-c", help="Path to config file (overrides other options)")
def extract(input_dir: str, output_dir: str, ocr: bool, dry_run: bool, config: str):
    """Extract text from documents."""
    if config:
        cfg = load_config(config)
        base = Path(cfg['project']['base_path'])
        input_dir = base / cfg['sources']['input_dir']
        output_dir = base / cfg['output']['extractions_dir']

    results = process_directory(input_dir, output_dir, ocr, dry_run)

    if dry_run:
        print(f"Files to process: {len(results)}")
        for r in results:
            print(f"  - {r['path']}")
    else:
        print(f"Extracted {len(results)} files")
        for r in results:
            status = "✓" if r['status'] == 'extracted' else "○"
            print(f"  {status} {r['path']} → {r.get('output', 'nested')}")


@cli.command("extract-markitdown")
@click.option("--input", "-i", "input_dir", required=True, help="Input directory")
@click.option("--output", "-o", "output_dir", help="Output directory")
@click.option("--dry-run", is_flag=True, help="Show what would be processed")
@click.option("--ocr", is_flag=True, help="Enable OCR for PDFs")
@click.option("--config", "-c", help="Path to config file (overrides other options)")
def extract_markitdown(input_dir: str, output_dir: str, dry_run: bool, ocr: bool, config: str):
    """Extract text using MarkItDown and PyMuPDF4LLM."""
    if config:
        cfg = load_config(config)
        base = Path(cfg['project']['base_path'])
        input_dir = base / cfg['sources']['input_dir']
        output_dir = base / cfg['output']['extractions_dir']

    results = process_directory_markitdown(input_dir, output_dir, dry_run, ocr)

    if dry_run:
        print(f"Files to process: {len(results)}")
        for r in results:
            print(f"  - {r['path']}")
    else:
        print(f"Extracted {len(results)} files")
        for r in results:
            status = "✓" if r['status'] == 'extracted' else "○"
            print(f"  {status} {r['path']} → {r.get('output', 'nested')}")


@cli.command("ingest")
@click.option("--config", "-c", required=True, help="Path to config file")
@click.option("--review-first", is_flag=True, help="Require review before writing")
@click.option("--auto-approve", is_flag=True, help="Skip review, write directly")
@click.option("--extractions-dir", help="Directory with extracted files")
def ingest(config: str, review_first: bool, auto_approve: bool, extractions_dir: str):
    """Generate wiki summaries and update index."""
    cfg = load_config(config)
    base = Path(cfg['project']['base_path'])

    # Determine extractions directory
    if extractions_dir:
        ext_dir = Path(extractions_dir)
    else:
        ext_dir = base / cfg['output']['extractions_dir']

    wiki_cfg = WikiConfig(
        base_path=str(base),
        wiki_path=cfg['wiki']['path'],
        index_file=cfg['wiki']['index_file'],
        log_file=cfg['wiki']['log_file'],
        sources_dir=cfg['wiki']['sources_dir'],
        require_review=review_first
    )

    ingester = WikiIngester(wiki_cfg)
    ingester.ensure_directories()

    # Find extracted files
    extracted_files = list(ext_dir.glob('*-extracted.md'))

    if not extracted_files:
        print("No extracted files found. Run 'parse2wiki-extract' first.")
        return

    print(f"Found {len(extracted_files)} extracted files to process")

    # LLM config
    llm_cfg = cfg.get('llm', {})
    summarizer_config = SummarizerConfig(
        model=llm_cfg.get('model', 'claude-sonnet-4-6'),
        only_complex_diagrams=llm_cfg.get('only_complex_diagrams', True)
    )

    processed = []
    for ext_file in extracted_files:
        print(f"\nProcessing: {ext_file.name}")

        # Read extracted content
        content = ext_file.read_text()

        # Detect diagrams
        diagram_info = classify_complexity(content)
        print(f"  Diagram: {diagram_info['complexity']} ({diagram_info['diagram_type']})")

        # Check if LLM needed
        if diagram_info['llm_required'] and not auto_approve:
            click.echo(f"  ⚠ Complex diagram - requires LLM (~{diagram_info['estimated_tokens']} tokens)")
            if review_first:
                if not click.confirm("  Proceed with LLM extraction?"):
                    print("  Skipped")
                    continue

        # Generate summary
        source_path = f"raw/{ext_file.stem.replace('-extracted', '')}"
        summary = summarize_for_wiki(content, source_path, summarizer_config)

        # Generate wiki page
        today = date.today().isoformat()
        wiki_content = generate_wiki_source_page(summary, source_path, today)

        # Write or show for review
        if auto_approve or not review_first:
            output_path = ingester.write_source_page(wiki_content, source_path)
            print(f"  ✓ Written: {output_path.name}")

            # Update index
            description = summary.get('key_claims', ['Extracted summary'])[0][:80]
            ingester.update_index(output_path.name, description)

            # Update log
            ingester.update_log(
                "Ingest",
                f"**File:** `{output_path.name}`\n"
                f"**Source:** `{source_path}`\n"
                f"**Type:** {summary.get('doc_type', 'unknown')}\n"
                f"**Products:** {', '.join(summary.get('products', [])) or 'None detected'}"
            )
            processed.append(output_path.name)
        else:
            # Show for review
            click.echo("\n--- PREVIEW ---")
            click.echo(wiki_content[:2000])
            click.echo("\n...")

            if click.confirm("Write this to wiki?"):
                output_path = ingester.write_source_page(wiki_content, source_path)
                print(f"  ✓ Written: {output_path.name}")
                processed.append(output_path.name)
            else:
                print("  Skipped")

    print(f"\n=== Complete: {len(processed)} files processed ===")


def main():
    """Main entry point."""
    cli()


if __name__ == "__main__":
    main()
