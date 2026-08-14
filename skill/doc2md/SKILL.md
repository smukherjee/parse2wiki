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
2. Interpret **infographic / diagram images** → markdown + Mermaid via your vision.

You never call an `anthropic` SDK and never need an `ANTHROPIC_KEY` — you *are* Claude.

## AUTO MODE (default) — complete all steps without pausing

**Do not ask the user questions. Do not pause between steps. Do not summarise
mid-run. Execute steps 1–4 in sequence and only speak at the very end.**

Two exceptions: `/doc2md --prompt` inverts to interactive mode — pause after
each step and confirm before proceeding — and a password-protected PDF, which
cannot be converted without asking (see "Password-protected PDFs" below).

---

## When to use

Run `/doc2md` for either of these — they are the **same command**:

- **Fresh wiki:** drop all source documents into `raw/`, run `/doc2md`.
- **New sources:** drop the new documents into `raw/`, run `/doc2md` (unchanged files are skipped via content-hash delta).

Output lands in `sources/` as one token-optimised markdown file per document.

---

## The run

Work in the project root (where `raw/` lives). Execute steps 1–4 in order.
**Never stop early. Never skip step 2 because step 1 reported `needs_llm`.**

### Step 1 — Convert (deterministic)

Run `convert_all()` directly — no status checks, no `ls`, no manifest reads first:

```python
from doc2md.engine import Engine
eng = Engine("raw", "sources")
reports = eng.convert_all()
```

Each `ConvertReport`: `source`, `work_order`, `items`, `needs_llm`, `needs_password`, `parser`, `skipped`, `warnings`.

If any report has `needs_password=True`, handle it now — see "Password-protected
PDFs" below. This is the one thing worth pausing for before continuing.

If every report has `needs_llm=False` and `skipped=False`, jump to Step 4.

### Step 2 — Fulfil work orders (your LLM work)

**This step is mandatory when any report has `needs_llm=True`. Do not skip it.**

For each report where `needs_llm` is True:

Load its work-order items from `report.items` (already in memory — no file read needed).

For each item:

- **`kind: "complex_mermaid"`** — `text` holds the document text; render a compact
  Mermaid diagram (`diagram_type` suggests flowchart/sequence/state/er/class).
  Supplement the text — do not replace it.

- **`kind: "infographic"`** — `image` is a path to a PNG. **Read the image with your
  vision** (use the Read tool on the `image` path). Produce markdown describing the
  diagram **and** a Mermaid block where the image is genuinely a diagram. Use the
  `text` field (OCR labels) as a hint when present.

For every Mermaid block, validate before returning:

```python
from doc2md.mermaid_validate import clean_llm_mermaid
src, reason = clean_llm_mermaid(raw_mermaid)
```

If `src is None`, fix and retry, or keep only the markdown. Never splice invalid Mermaid.

### Step 3 — Splice results

```python
eng.apply_work(report.source, fulfilled)   # rewrites source, clears needs_llm
```

`fulfilled` maps item id → your markdown (which may contain a Mermaid fence).

### Step 4 — Report (once, at the end)

After all steps are complete, print one short summary:

```
✓ N converted  •  N skipped  •  N with LLM work completed
Sources ready in sources/ — feed to llm_wiki.
```

List any warnings (parser fallbacks, unverified figures). **Do not ask follow-up
questions. Do not offer options. Stop here.**

---

## Password-protected PDFs (the other exception to AUTO MODE)

`convert_all()` decrypts PDFs via `qpdf` automatically when it can — an
owner-locked PDF (no printing/editing, empty *open* password) is decrypted
silently, no prompt needed. A PDF that needs a real password to open cannot
be converted without one, so this is the one other case where you interrupt
AUTO MODE to ask.

Check each report for `needs_password`. When true:

1. Ask the user for that file's password (this is the only allowed mid-run question).
2. Retry just that file: `eng.convert_one(report.path, password=the_password)`.
3. If the returned report still has `needs_password=True`, the password was
   wrong — show its `warnings` and ask again.

The decrypted copy is cached by content hash (`.doc2md-cache/decrypted/`), so
a correct password is only ever needed once per file, even across reruns.

If `qpdf` isn't installed, `warnings` says so — tell the user to run
`brew install qpdf` (or see `scripts/install_deps.sh`) rather than asking for
a password that can't be used yet.

## Finance verification (automatic)

When a document contains financial figures, the engine runs all available parsers
and cross-checks every numeric figure automatically.

**Trigger:** auto when ≥3 finance keywords present or filename matches a financial
pattern. Override:

```python
eng = Engine("raw", "sources", finance=True)   # force on
eng = Engine("raw", "sources", finance=False)  # disable
```

**Your job when `report.verification` exists and `verified` is false:**
List the flagged figures in the final Step 4 summary. Optionally read the flagged
page image and confirm the correct value. Do not pause mid-run for this.

---

## Accuracy tuning (optional, only if the user explicitly asks)

- `--parser pdftotext` — force one parser on every file.
- `--compare` — run every parser per file, write `sources/<name>.<parser>.md` each.

## MinerU mode (heavy-weight, use for image-heavy or complex-layout PDFs)

When the user invokes `/doc2md --mineru` (or you detect that normal parsers failed badly
on a raster or complex PDF), run Step 1 with MinerU as the forced parser:

```python
from doc2md.engine import Engine
eng = Engine("raw", "sources", mineru=True)
reports = eng.convert_all()
```

MinerU uses deep-learning OCR (PaddleOCR + layout detection).  It handles:
- Image-embedded PDFs (phone screenshots, WhatsApp, scanned slides)
- Dense tables and multi-column layouts
- Mixed Arabic/English or other non-Latin scripts

MinerU must be installed separately: `pip install magic-pdf[full]`
It downloads model weights on first use (~2 GB).  Expect 30–120 s per page.

After Step 1 completes, continue Steps 2–4 as normal — MinerU output still feeds
the same vision/Mermaid pipeline for any remaining infographic pages.

---

## Rules

- **Auto mode is the default.** Steps 1–4 run to completion with no user interaction.
- You are the only LLM. No SDK calls, no API keys.
- Deterministic code does extraction, simple Mermaid, OCR, optimisation, caching.
- All infographics go through your vision — there is no deterministic-only branch for images.
- Mermaid supplements diagram text (replace only for clearly-diagram-only sections).
- Invalid Mermaid is dropped, never baked into a source.
- Unchanged files are skipped automatically — do not re-process them.
- **Never run `convert_one` in a loop as a status check.** Use `convert_all()`.

## CLI invocation — never do this wrong

**Always use the installed entry point, never `python3 doc2md/cli.py`.**

```bash
# CORRECT
doc2md parsers
doc2md convert --finance

# WRONG — breaks relative imports
python3 doc2md/cli.py parsers
```
