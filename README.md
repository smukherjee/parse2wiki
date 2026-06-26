# doc2md

A **deterministic pre-processor** that converts documents into **token-optimised markdown + Mermaid**, to be fed as sources to an LLM-wiki builder ([nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)).

doc2md does **not** build a wiki, summarise, or maintain an index — that is llm_wiki's job. doc2md's value is: accuracy-controlled **pluggable extraction**, **Mermaid** generation (llm_wiki can't), diagram/infographic **OCR**, and **token-optimised** output.

It ships as a **Claude skill** (`/doc2md`): Claude is the LLM and does the only two things deterministic code can't — complex text-diagram Mermaid and infographic interpretation via **vision**. The Python package is a deterministic engine that never calls an LLM (no `anthropic` SDK, no `ANTHROPIC_KEY`).

## Install

```bash
pip install -e ".[modern]"          # markitdown + pymupdf4llm are optional extras
doc2md parsers                      # list parsers and availability
```

Some parsers wrap system binaries (install what you want; missing ones degrade to the next parser in the fallback chain):

```bash
brew install poppler tesseract      # pdftotext, tesseract OCR
brew install pandoc                 # pandoc (docx/html/…)
cargo install pdf-inspector         # pdf2md (PDF → markdown, Rust)
cargo install unpdf-cli             # unpdf (PDF → markdown, Rust)
cargo install undoc-cli             # undoc (DOCX/XLSX/PPTX → markdown, Rust)
```

## Use as a skill (zero-config)

Drop documents in `raw/`, run `/doc2md`. Output lands in `sources/` — feed that to llm_wiki.

- **Fresh wiki:** put all source documents in `raw/`, run `/doc2md`.
- **New sources:** drop the new documents in `raw/`, run `/doc2md` (unchanged files are skipped via a content-hash delta).

The skill orchestrates the engine per document and does the LLM work (complex Mermaid + infographic vision), validating every Mermaid block before writing it. See [`skill/doc2md/SKILL.md`](skill/doc2md/SKILL.md).

## Use from the shell

```bash
doc2md convert                       # raw/ → sources/ (zero-config)
doc2md convert --parser pdftotext    # force one parser on every file
doc2md convert --compare              # run every available parser per file for accuracy diffing
doc2md check                          # show new/changed files vs the manifest (hash-delta)
doc2md parsers                        # list parsers + availability
```

## Parsers (pluggable seam)

Each extraction records which parser produced it, so accuracy can be audited. Built-in adapters: `pdf-inspector` (pdf2md), `unpdf`, `pymupdf4llm`, `pdfplumber`, `pdftotext`, `undoc`, `markitdown`, `docx` (python-docx), `pptx` (python-pptx), `xlsx` (openpyxl), `pandoc`, `image` (OCR → vision).

External parser packages register via the `doc2md.parsers` entry-point group — no doc2md edit required:

```toml
# in an external plugin package's pyproject.toml
[project.entry-points."doc2md.parsers"]
my_parser = "my_pkg:factory"   # zero-arg factory → doc2md.parsers.base.Parser
```

Fallback chains (ext → ordered parser names) live in [`doc2md/parsers/registry.py`](doc2md/parsers/registry.py); reorder to change defaults.

## Token cost

| Stage | Cost |
|-------|------|
| Extraction (any parser) | 0 |
| OCR | 0 |
| Diagram detection | 0 |
| Simple Mermaid | 0 |
| Complex text-diagram Mermaid | Claude (in the skill) |
| Infographic interpretation (vision) | Claude (in the skill) |

Unchanged files are skipped automatically, so re-runs spend zero LLM tokens.

## Architecture

- `doc2md/` — deterministic engine: `parsers/` (seam), `detection.py`, `mermaid.py` + `mermaid_validate.py`, `ocr.py`, `optimise.py`, `manifest.py` (content-addressed cache), `writer.py` (source + work-order), `engine.py` (library API), `cli.py`.
- `skill/doc2md/SKILL.md` — the `/doc2md` Claude skill (Claude is the LLM).

See [`CONTEXT.md`](CONTEXT.md) for the domain language and [`docs/adr/0001-skill-first-preprocessor-architecture.md`](docs/adr/0001-skill-first-preprocessor-architecture.md) for the architecture decision.

## License

MIT
