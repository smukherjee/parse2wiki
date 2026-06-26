"""Thin CLI wrapper over the engine. The skill calls the library directly;
this exists for shell use and for ``--compare`` accuracy diffing.
"""

from __future__ import annotations

from pathlib import Path

import click

from .engine import Engine


@click.group()
def cli() -> None:
    """doc2md — documents → token-optimised markdown + Mermaid."""


@cli.command()
@click.option("--raw", "raw_dir", default="raw", show_default=True, help="Directory of source documents.")
@click.option("--sources", "sources_dir", default="sources", show_default=True, help="Output directory for token-optimised markdown.")
@click.option("--cache", "cache_dir", default=None, help="Cache/manifest directory (default: <sources>/../.doc2md-cache).")
@click.option("--parser", default=None, help="Force one parser (e.g. pdftotext).")
@click.option("--ocr/--no-ocr", default=True, show_default=True, help="Run OCR fallback + figure-page detection.")
@click.option("--compare", is_flag=True, help="Run every available parser per file for accuracy diffing.")
@click.option("--finance/--no-finance", default=None,
              help="Finance verification: run all parsers and cross-check figures. "
                   "Default: auto-detect from document content.")
def convert(raw_dir, sources_dir, cache_dir, parser, ocr, compare, finance):
    """Convert documents in --raw to token-optimised markdown in --sources."""
    eng = Engine(raw_dir, sources_dir, cache_dir, ocr=ocr, parser=parser, finance=finance)
    if compare:
        for p in eng._iter_files():  # noqa: SLF001
            for r in eng.compare_one(p):
                click.echo(f"  {r.parser:14s} → {r.source}")
        return
    reports = eng.convert_all()
    for r in reports:
        if r.skipped:
            click.echo(f"  skip  {r.path} (unchanged)")
            continue
        tag = "llm " if r.needs_llm else "ok  "
        click.echo(f"  {tag} {r.parser:14s} {r.path} → {r.source}")
        for w in r.warnings:
            click.echo(f"        ! {w}")


@cli.command()
@click.option("--raw", "raw_dir", default="raw", show_default=True)
@click.option("--sources", "sources_dir", default="sources", show_default=True)
@click.option("--cache", "cache_dir", default=None)
def check(raw_dir, sources_dir, cache_dir):
    """Show hash-delta: which documents are new or changed vs the manifest."""
    eng = Engine(raw_dir, sources_dir, cache_dir, ocr=False)
    pending = eng.pending()
    if not pending:
        click.echo("nothing pending — all sources up to date")
        return
    for p in pending:
        click.echo(f"  pending  {p}")


@cli.command()
@click.option("--raw", "raw_dir", default="raw", show_default=True)
def parsers(raw_dir):
    """List registered parsers and availability."""
    eng = Engine(raw_dir, "sources", ocr=False)
    for name, p in eng.registry.parsers.items():
        click.echo(f"  {'ok' if p.available else '--':2s}  {name:14s} {', '.join(getattr(p, 'extensions', ()) or ())}")


@cli.command()
@click.option("--text", "-t", default=None, help="Text sample to analyze")
@click.option("--file", "-f", default=None, help="File to read text from")
@click.option("--show-scripts", is_flag=True, help="Show detailed script detection")
def detect_lang(text, file, show_scripts):
    """Detect language(s) in text using Unicode script analysis."""
    from .lang import detect_language, detect_script, get_tesseract_langs_for_text, extract_multilingual

    if file:
        try:
            with open(file) as f:
                text = f.read()[:2000]
        except Exception as e:
            click.echo(f"Error reading file: {e}", err=True)
            return

    if not text:
        click.echo("Provide text with --text or --file", err=True)
        return

    result = detect_language(text)
    click.echo(f"Primary language: {result.language}")
    click.echo(f"Primary script: {result.script}")
    click.echo(f"Confidence: {result.confidence:.2f}")

    if show_scripts:
        scripts = detect_script(text)
        click.echo("\nScript breakdown:")
        for s in scripts:
            click.echo(f"  {s.script}: {s.char_count} chars ({s.confidence:.1%})")

    tess_langs = get_tesseract_langs_for_text(text)
    click.echo(f"\nTesseract languages needed: {'+'.join(tess_langs)}")


@cli.command()
def tesseract_langs():
    """Show available Tesseract language packs and installation commands."""
    import subprocess

    click.echo("=== Tesseract Language Detection ===\n")

    # Try to get installed languages
    try:
        result = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True)
        if result.returncode == 0:
            langs = [l.strip() for l in result.stdout.strip().split("\n")[1:] if l.strip()]
            click.echo(f"Installed languages ({len(langs)}):")
            for lang in langs:
                click.echo(f"  - {lang}")
    except Exception:
        click.echo("tesseract not found in PATH")

    click.echo("\n=== Common Language Packs ===\n")
    click.echo("For multilingual documents, install these language packs:")
    click.echo()
    click.echo("  Arabic:        ara")
    click.echo("  Hindi:         hin")
    click.echo("  Bengali:       ben")
    click.echo("  Chinese:       chi_sim (Simplified), chi_tra (Traditional)")
    click.echo("  Japanese:      jpn")
    click.echo("  Korean:        kor")
    click.echo("  Russian:       rus")
    click.echo("  Hebrew:        heb")
    click.echo("  Thai:          tha")
    click.echo()
    click.echo("=== Installation Commands ===\n")
    click.echo("macOS (Homebrew):")
    click.echo("  brew install tesseract-lang")
    click.echo()
    click.echo("Ubuntu/Debian:")
    click.echo("  sudo apt install tesseract-ocr-ara tesseract-ocr-hin tesseract-ocr-ben")
    click.echo("  sudo apt install tesseract-ocr-chi-sim tesseract-ocr-chi-tra")
    click.echo("  sudo apt install tesseract-ocr-jpn tesseract-ocr-kor")
    click.echo()
    click.echo("After installation, rerun doc2md with --ocr to apply multilingual OCR.")


@cli.command()
@click.option("--cache", "cache_dir", default=None)
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def token_report(cache_dir, as_json):
    """Show token usage and savings report."""
    from .manifest import Manifest
    from pathlib import Path

    cache = Path(cache_dir) if cache_dir else Path("sources").parent / ".doc2md-cache"
    manifest = Manifest(cache)

    total_raw = 0
    total_optimised = 0
    total_llm_input = 0
    total_llm_output = 0
    records = []

    for rec in manifest._files.values():
        total_raw += rec.tokens_raw
        total_optimised += rec.tokens_optimised
        total_llm_input += rec.tokens_llm_input
        total_llm_output += rec.tokens_llm_output
        records.append({
            "file": Path(rec.original).name,
            "parser": rec.parser,
            "tokens_raw": rec.tokens_raw,
            "tokens_optimised": rec.tokens_optimised,
            "tokens_llm_input": rec.tokens_llm_input,
            "tokens_llm_output": rec.tokens_llm_output,
            "savings_pct": round((1 - rec.tokens_optimised / rec.tokens_raw) * 100, 1) if rec.tokens_raw > 0 else 0,
        })

    if as_json:
        import json
        print(json.dumps({
            "files": records,
            "totals": {
                "tokens_raw": total_raw,
                "tokens_optimised": total_optimised,
                "tokens_llm_input": total_llm_input,
                "tokens_llm_output": total_llm_output,
                "optimization_savings": total_raw - total_optimised,
                "optimization_savings_pct": round((1 - total_optimised / total_raw) * 100, 1) if total_raw > 0 else 0,
            }
        }, indent=2))
        return

    # Table format
    click.echo("\n=== Token Usage Report ===\n")
    click.echo(f"{'File':<40} {'Raw':>8} {'Optimised':>10} {'LLM In':>8} {'LLM Out':>9} {'Savings':>8}")
    click.echo("-" * 85)

    for r in records:
        click.echo(f"{r['file']:<40} {r['tokens_raw']:>8} {r['tokens_optimised']:>10} {r['tokens_llm_input']:>8} {r['tokens_llm_output']:>9} {r['savings_pct']:>7.1f}%")

    click.echo("-" * 85)
    click.echo(f"{'TOTAL':<40} {total_raw:>8} {total_optimised:>10} {total_llm_input:>8} {total_llm_output:>9} {(1 - total_optimised / total_raw) * 100 if total_raw > 0 else 0:>7.1f}%")
    click.echo(f"\nOptimization saved: {total_raw - total_optimised:,} tokens ({(1 - total_optimised / total_raw) * 100:.1f}%)")
    if total_llm_output > 0:
        click.echo(f"LLM tokens (output): {total_llm_output:,}")
    click.echo()


def main() -> None:
    cli()


if __name__ == "__main__":
    main()