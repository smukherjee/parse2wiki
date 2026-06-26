# doc2md is a skill-first, deterministic pre-processor for llm_wiki

Status: accepted

doc2md converts documents into token-optimised markdown + Mermaid to be fed as sources to an external LLM-wiki builder ([nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)). It is delivered as a Claude skill (`/doc2md`); **Claude is the LLM** and the Python package is a **deterministic engine** (extraction, detection, simple Mermaid, OCR, token optimisation, writing) that never calls an LLM. The only LLM work in doc2md is complex-diagram Mermaid and infographic interpretation via Claude vision — done in the skill, with no `anthropic` SDK and no `ANTHROPIC_KEY`. Summarisation, source pages, wiki index/log, and the knowledge base are explicitly **out of scope**; llm_wiki owns them.

## Considered Options

- **Python SDK as the LLM (skill merely calls the CLI).** Rejected: forces a non-savvy user to set `ANTHROPIC_KEY`, puts two LLMs in the room, and means Claude isn't authoring the output. Claude-in-the-skill removes the SDK seam entirely.
- **Keep summarisation/wiki-creation in doc2md.** Rejected after surveying llm_wiki, which already does LLM wiki building (analysis → generation, entity/concept pages, cross-refs, index/log) *and* deterministic multi-format extraction with SHA256 caching. Keeping it would duplicate llm_wiki. Mermaid is the one thing llm_wiki cannot do, so that became doc2md's reason to exist.
- **An `anthropic` SDK "LLM client" seam (the original Candidate 3).** Generalised away: the seam is now the Markdown output contract between Claude and the deterministic engine, not a transport client. No import-guard/key/retry boilerplate because there is no SDK call.
- **Wiki-suffixed naming (`parse2wiki`, `preparsewiki`).** Rejected: the "wiki" suffix implies the tool builds a wiki, which it does not. Renamed to `doc2md` (documents → markdown; matches the repo's existing `pdf2image`/`pdftotext` naming idiom).
- **Complex Mermaid deferred to llm_wiki.** Rejected: llm_wiki produces no Mermaid, so deferring it means losing it entirely. Complex Mermaid stays as doc2md's one text-LLM task.
- **Simple/complex routing for infographics.** Rejected: all infographics go through Claude vision — deterministic OCR cannot accurately interpret visual diagrams.

## Consequences

- **Deleted:** `wiki/ingester.py`, `summarizer/wiki_summary.py`, `cli.ingest`, the `parse2wiki-ingest` entry point, and the `wiki/` config section. The summarisation contract, grounding verification, and claim quality-gate/quarantine are gone (no claims to ground, no KB to quarantine — llm_wiki owns the KB). Only Mermaid validation survives from the quality-gate theme.
- **Extraction is fully zero-token and deterministic**, which makes the README's "Text extraction: 0 tokens" claim true. The two current extractor backends collapse into one pluggable parser seam (`Parser` protocol + `ExtractorRegistry` + fallback chains + `SubprocessParser` for any-language binaries); built-in explicit registration **plus** entry-point discovery so external parser packages register themselves.
- **`--compare`** runs every available parser on a file for accuracy diffing; each output records `extracted_by` for auditing.
- **Manifest + content-addressed caches** (`original → hash → parser → extraction → complex-Mermaid cache → source`) drive hash-delta re-runs: unchanged files are skipped, results are reproducible, and re-runs spend zero LLM tokens. (llm_wiki re-caches downstream independently.)
- **Supplement-default:** Mermaid supplements the diagram text in the output; replace only for clearly-diagram-only sections.
- **Engine is a Python library the skill calls directly** (not CLI stdout parsing); `/doc2md` is zero-config (`raw/` → sources).
- **`kinds=("file",)`** in the parser interface now, so URL/web sources (firecrawl) are a non-breaking add later.