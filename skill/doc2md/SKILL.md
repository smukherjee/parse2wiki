---
name: doc2md
description: Convert documents in raw/ into token-optimised markdown + Mermaid sources for llm_wiki. Zero-config, one-shot. Claude renders complex text-diagram Mermaid and interprets infographics via vision; everything else is deterministic.
---

# doc2md

You are the LLM inside a deterministic pre-processor. The `doc2md` Python package
does all the deterministic work (extraction, diagram detection, simple Mermaid,
OCR, token optimisation, caching, writing). **Your only jobs are the things
deterministic code cannot do:**

1. Render **complex text diagrams** → Mermaid (simple ones are already done).
2. Interpret **infographics / diagram images** → markdown + Mermaid, using your **vision**.

You never call an `anthropic` SDK and never need an `ANTHROPIC_KEY` — you *are* Claude.

## When to use

Run `/doc2md` for either of these — they are the **same command**:

- **Fresh wiki:** drop all source documents into `raw/`, run `/doc2md`.
- **New sources:** drop the new documents into `raw/`, run `/doc2md` (unchanged files are skipped via content-hash delta).

Output lands in `sources/` as one token-optimised markdown file per document — feed that directory to [llm_wiki](https://github.com/nashsu/llm_wiki).

## Setup (once)

Verify the engine and its parsers are available. Run, and report what's missing:

```bash
pip install -e ".[modern]"   # markitdown + pymupdf4llm are optional extras
doc2md parsers                # list parsers and availability
```

System binaries some parsers wrap: `pdftotext` (poppler), `pandoc`, `tesseract` (OCR).
Missing ones degrade gracefully to the next parser in the fallback chain — note any
gaps to the user but do not block.

## The run

You orchestrate per-document. Work in the project root (where `raw/` lives).

### 1. Convert (deterministic)

```python
from doc2md.engine import Engine
eng = Engine("raw", "sources")          # zero-config defaults; ocr=True
reports = eng.convert_all()
```

Each `ConvertReport` tells you: `source` (the written markdown), `work_order`
(path to a JSON list of items only you can do), `items`, `needs_llm`, `parser`,
`skipped`, `warnings`. Print a short summary for the user (how many converted,
how many skipped, how many need you, any warnings).

If a report `needs_llm` is False, its source is **done** — nothing more to do for it.

### 2. Fulfil the work-orders (your LLM work)

For each report with `needs_llm`, load its work-order JSON. Each item is one of:

- **`kind: "complex_mermaid"`** — `text` holds the document text; render a compact
  Mermaid diagram (`diagram_type` suggests flowchart/sequence/state/er/class).
  Supplement the text — do not replace it. Keep it tight; this is a token-optimised source.
- **`kind: "infographic"`** — `image` is a path to a PNG (a standalone infographic or
  a rendered PDF page). **Read the image with your vision** (use the Read tool on the
  `image` path). Produce markdown describing the diagram **and** a Mermaid where the
  image is genuinely a diagram (flowchart/architecture/sequence/etc.). Use the `text`
  field (OCR labels) as a hint when present.

For every Mermaid block you produce, **validate before returning it**:

```python
from doc2md.mermaid_validate import clean_llm_mermaid
src, reason = clean_llm_mermaid(raw_mermaid)
```

If `src is None`, the Mermaid is invalid — fix and retry, or omit the Mermaid and keep
only the markdown description. Never splice invalid Mermaid into a source.

You do **not** manage the cache yourself. The engine pre-fulfils each item from its
work-cache during `convert_all` (so unchanged files and previously-fulfilled items never
re-enter your work-order), and `apply_work` writes your output back to that cache. So a
re-run spends zero LLM tokens automatically. Each work-order item carries a `file_hash`
for traceability, but you only need the `id` to splice.

### 3. Splice your results into the source

Map each fulfilled item id → your markdown (which may contain a Mermaid fence), then:

```python
eng.apply_work(report.source, fulfilled)   # rewrites the source in place, clears needs_llm
```

`apply_work` replaces each `<!-- doc2md:await:<id> -->` marker with your output and
marks the manifest record as no longer awaiting the LLM.

### 4. Hand off

Tell the user the sources are ready in `sources/` and to run llm_wiki against that
directory. Do not summarise, build wiki pages, or write an index — that is llm_wiki's job.

## Finance verification (automatic)

When a document contains financial figures, a single parser can silently
mis-read a digit or miss a decimal. The engine defends against this by running
**all available parsers** and cross-checking every numeric figure.

**Trigger:** automatic when the document contains ≥3 finance keywords
(`revenue`, `ebitda`, `balance sheet`, …) or the filename matches a financial
pattern (`annual-report`, `10K`, `income-statement`, etc.).
Override at runtime:

```python
eng = Engine("raw", "sources", finance=True)   # force on
eng = Engine("raw", "sources", finance=False)  # disable
eng = Engine("raw", "sources")                 # auto-detect (default)
```

CLI equivalents: `doc2md convert --finance` / `doc2md convert --no-finance`.

**Output:** a sibling `<source>.verify.json` is written alongside every
converted markdown file that triggers verification:

```json
{
  "document": "raw/Q3-results.pdf",
  "parsers_used": ["pdf-inspector", "pymupdf4llm", "pdftotext"],
  "total_figures": 142,
  "mismatch_count": 2,
  "verified": false,
  "mismatches": [
    {"label": "total revenue", "values": {"pymupdf4llm": "$1,234M", "pdftotext": "$1,284M"}, "flag": "warn"},
    ...
  ]
}
```

**Your job when `verified` is false:**
1. Read the verify.json and list the flagged figures to the user.
2. Tell them: _"N figures could not be verified across parsers — check the
   original document for these values before using this source."_
3. Optionally: read the flagged page image with your vision and confirm the
   correct value, then note it in the source with an inline comment.

When `verified` is true, tell the user: _"All figures cross-checked across N
parsers — no discrepancies found."_

## Accuracy tuning (optional, only if the user asks)

- `doc2md convert --parser pdftotext` — force one parser on every file.
- `doc2md convert --compare` — run **every** available parser per file, writing
  `sources/<name>.<parser>.md` each, so the user can diff accuracy and pick a chain.
- Reorder fallback chains in code (`doc2md/parsers/registry.py`) to change defaults.

## Rules

- You are the only LLM. No SDK calls, no API keys.
- Deterministic code does extraction, simple Mermaid, OCR, optimisation, caching.
- All infographics go through your vision — there is no deterministic-only branch for images.
- Mermaid supplements diagram text (replace only for clearly-diagram-only sections).
- Invalid Mermaid is dropped, never baked into a source.
- Unchanged files are skipped automatically; do not re-process them.