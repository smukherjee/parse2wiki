# doc2md

A deterministic pre-processor that converts documents into **token-optimised markdown + Mermaid**, to be fed as sources to an LLM-wiki builder ([nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)). doc2md does **not** build a wiki, summarise, or maintain an index — that is llm_wiki's job. doc2md's value is: accuracy-controlled pluggable extraction, Mermaid generation (llm_wiki can't), diagram/infographic OCR, and token-optimised output.

## Language

**Document**:
A source file — PDF, DOCX, PPTX, XLSX, an image (PNG/JPG infographic), or a ZIP of the same.
_Avoid_: file, input, asset.

**Extraction**:
Zero-token deterministic recovery of text and structure from a document via a pluggable Parser.
_Avoid_: conversion.

**Parser**:
A pluggable adapter that performs extraction for a set of source kinds/extensions (docling, pandoc, pymupdf4llm, pdftotext, markitdown, image-OCR, …). May wrap a Python library **or** an external binary of any language (Rust/Go/CLI); output is normalised to markdown. Each extraction records which parser produced it, so accuracy can be audited. New parsers are added as technology improves.
_Avoid_: backend, driver, extractor (use **Parser** for the adapter; "extraction" for the stage).

**Fallback chain**:
The ordered parsers tried for a given source kind/extension; the first that yields non-empty text wins. Config-driven, so a user can test accuracy by reordering or forcing one parser.
_Avoid_: pipeline (reserved for the whole flow), strategy.

**Diagram detection**:
Classifying extracted text *or an extracted image* as simple / complex / none, plus a diagram type. Routes Mermaid generation.
_Avoid_: classification, analysis.

**Complexity** (`simple` | `complex` | `none`):
Whether a diagram can be rendered deterministically (`simple`), needs the LLM (`complex`), or has no diagram structure (`none`). This routes between the deterministic and LLM paths.
_Avoid_: difficulty, level.

**Mermaid**:
The diagram block in the output — deterministic for simple diagrams, Claude for complex ones (text diagrams and infographics). llm_wiki cannot produce Mermaid; this is doc2md's differentiator.
_Avoid_: diagram (reserved for the detected content), chart, graph.

**Infographic / diagram image**:
An image — standalone file or embedded figure — whose meaning is visual (flowchart, chart, infographic). Deterministic OCR may extract its text/labels, but **all infographics are interpreted by Claude vision** → markdown + Mermaid. There is no deterministic-only branch for image diagrams (unlike text diagrams, which keep the simple/complex split).
_Avoid_: figure, picture, illustration.

**Token optimisation**:
The deterministic compaction stage — strip repeated headers/footers/page numbers, dedupe, collapse whitespace, keep semantic structure, embed compact Mermaid. Produces the token-optimised source llm_wiki ingests.
_Avoid_: compression, minification.

**Source** (output):
The per-document token-optimised markdown + Mermaid file doc2md writes, placed where llm_wiki ingests sources. Not a wiki page, not a summary.
_Avoid_: page, summary, article.

## Stage split — doc2md vs llm_wiki

- **doc2md = deterministic + Mermaid.** Extraction (pluggable parsers), diagram detection, simple Mermaid, diagram/image OCR, token optimisation, Mermaid validation, and the *one* LLM use — complex Mermaid and infographic interpretation, done by **Claude in the `/doc2md` skill**. No summarisation, no wiki, no index.
- **llm_wiki = the LLM wiki.** It ingests doc2md's sources (or raw files) and builds the wiki: summaries, entity/concept pages, `[[wikilink]]` cross-refs, `index.md`/`log.md`/`overview.md`, knowledge graph. It does **not** do Mermaid.

## The one LLM task (Claude, in the skill)

Claude is invoked only for what deterministic code can't do:

- **Complex text diagrams → Mermaid** (supplemented into the output, not replacing the text — supplement-default). Simple *text* diagrams stay deterministic.
- **All infographics / diagram images → markdown + Mermaid** via **vision**: every detected diagram image is passed to Claude (no deterministic-only branch for images).

Everything else (summaries, wiki pages, knowledge base) is llm_wiki's. No `anthropic` SDK, no `ANTHROPIC_KEY` — Claude is the LLM in the skill.

## Architecture (skill-first)

- **`/doc2md` skill** — the only user-facing surface; one-shot over `raw/`; orchestrates the engine per-document and is the LLM (complex Mermaid + infographic vision). End user is not exposed to the internal architecture.
- **Deterministic engine** (Python, exposed as a library API the skill calls — not CLI stdout) — extract (parsers), detect, simple Mermaid, diagram/image OCR, token optimisation, Mermaid validation, write sources, manifest/cache. No LLM.
- **Pluggable parser seam** — `Parser` protocol + `ExtractorRegistry` + fallback chains + `SubprocessParser` helper (wraps binaries of any language); built-in explicit registry **+** entry-point discovery; `--parser` to force one, `--compare` to run all for accuracy diffing. File parsers now (pymupdf4llm, pdfplumber, pdftotext, markitdown, python-docx/pptx/openpyxl, pandoc); `kinds=("file",)` so web/URL (firecrawl) is a non-breaking add later.
- **Diagram/image OCR** — detect diagram/infographic regions (parser figure/layout analysis + standalone image files), extract as images, tesseract text-OCR (deterministic); **all infographics routed to Claude vision**. New `ImageParser` for PNG/JPG/WebP.
- **Manifest + content-addressed caches** — `original → hash → parser → extraction → (complex-Mermaid cache) → source`. Hash-delta re-runs skip unchanged work; reproducible; no wasted tokens on re-runs.
- **Mermaid validation** — invalid LLM Mermaid is dropped with a warning, never baked into a source.
- **Supplement-default** — Mermaid supplements the diagram text in the output; replace only for clearly-diagram-only sections.
- **Zero-config defaults** — `/doc2md` works with no config (`raw/` → sources); config is override-only.

## Removed from earlier scope

Summarisation, source pages (frontmatter wiki pages), wiki `index.md`/`log.md`, knowledge base, grounding verification, claim quality-gate/quarantine, the summarisation contract, `WikiIngester`, `wiki_summary` — all removed. Owned by llm_wiki. (`wiki/ingester.py`, `summarizer/wiki_summary.py`, `cli.ingest`, and the `wiki/` config section get deleted.)

## Flagged ambiguities

- **"Extraction" vs "wiki ingest"** are different tools. Extraction is doc2md's zero-token deterministic stage; wiki ingest is llm_wiki's LLM stage. Don't use "ingestion" for doc2md.

- **"Diagram"** is the detected content (in text or image); **"Mermaid"** is the rendered block. An infographic is a diagram image; its Mermaid (if any) is rendered by Claude vision.