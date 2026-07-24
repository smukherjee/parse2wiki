<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# output a summarised final recomendation as a md file with the folder structure, best practices and all the relevant files

The final recommendation file has been created at `/tmp/RFP-Pipeline-Final-Recommendation.md` — I wasn't able to move it to your Desktop because no active workspace is currently set in this sandbox (all write operations outside `/tmp` are blocked until you select a workspace folder). You can either set a workspace, or simply copy the file from `/tmp/RFP-Pipeline-Final-Recommendation.md` yourself.

Here's the full content for your reference and copying:

## RFP Knowledge Pipeline — Final Recommendation

### Overview

This consolidates the complete recommendation: repository structure, the merged `rfp-pipeline` skill (doc2md as ingest engine), the `rfp-analysis-and-response` drafting skill, per-opportunity record-keeping, and operating rules. Core invariant: **nothing becomes trusted ground truth without a traceable, verbatim link back to its source.**

### 1. Top-level folder structure

```text
RFP Knowledge Master/
├── WIP/                          <- scratch drafting, excluded from retrieval/audit
├── Raw/                          <- immutable source documents. doc2md input.
├── MD/                           <- token-optimised markdown + Mermaid. doc2md output.
├── Curated/
│   ├── cards/                    <- extracted knowledge cards, verbatim-first
│   ├── tags/                     <- taxonomy definitions
│   └── index/                    <- retrieval index
└── Opportunities/
    └── <YYYY-MM-ClientName-ProjectName>/
        ├── RFP-Received/         <- tender as issued, immutable
        ├── Addenda-Clarifications/  <- dated, immutable, with log.md
        ├── Response/              <- drafts + final-submission.pdf
        └── meta.md                <- opportunity summary
```

| Folder | Purpose | Mutability |
| :-- | :-- | :-- |
| WIP/ | Drafting new reusable content before promotion | Fully editable |
| Raw/ | Source of truth for reusable knowledge | Immutable; version, don't overwrite |
| MD/ | doc2md-generated derivative of Raw/ | Regenerated only; never hand-edited |
| Curated/cards/ | Reusable, tagged, provenance-linked knowledge | Editable via status lifecycle |
| Opportunities/*/RFP-Received/ | Tender as issued by buyer | Immutable |
| Opportunities/*/Addenda-Clarifications/ | Buyer-issued changes/answers, dated | Immutable |
| Opportunities/*/Response/ | Drafts + final submission for this bid | Drafts mutable; final submission read-only once sent |

### 2. Skills involved

**rfp-pipeline** (ingestion, extraction, audit, harvest, migration) — merged skill absorbing doc2md as its internal ingest engine, remapped from doc2md's default `raw/`/`sources/` to `Raw/`/`MD/`. Owns conversion (`Engine("Raw","MD").convert_all()`), verbatim-first extraction into `Curated/cards/`, full trust-chain audit, post-submission harvest, and legacy migration.

**rfp-analysis-and-response** (drafting) — separate skill used per-opportunity. Analyzes `RFP-Received/` plus `Addenda-Clarifications/`, extracts scope/deliverables/compliance/evaluation criteria, drafts a narrative proposal (not a bullet-dump), distinguishing "Mandatory from RFP" vs "Recommended for response quality," sourcing evidence exclusively from user-specified `Curated/`.

### 3. Metadata model (every Curated card)

```yaml
status: draft
verification_status: unverified
derived_from: MD/02-Products/Product-X-Brochure.md
source_anchor: "Capacity and throughput"
verbatim_quote: "The system supports up to 1,200 passengers per hour in standard configuration."
engine_parser: pdftotext
engine_warnings: []
finance_verified: true
tags:
  - product:product-x
  - content-type:technical
  - sensitivity:internal
```


### 4. Best practices

- **Ingestion**: Raw/ immutable; edit Raw/, never MD/; rely on doc2md's hash delta-skip; treat warnings/fallback-parser/MinerU runs as review flags; block unverified finance figures.
- **Extraction**: verbatim-first, no untagged promotion to Curated/, unresolvable spans marked unverifiable.
- **Verification \& retrieval**: prefer approved > human-reviewed > unverified; sample-audit approved cards; deprecate rather than delete.
- **Audit**: run on demand, not continuously; full audit ≠ lint; migrate legacy wikis incrementally before expecting a meaningful trust score.
- **Per-opportunity record-keeping**: separate RFP-Received/ from Addenda-Clarifications/; log.md tracks addenda impact; final submission stays read-only in Response/; meta.md summarizes the opportunity.
- **Harvest**: extract reusable narrative post-submission as draft cards; never promote client-specific pricing/tailoring; human review required before promotion.
- **Portability**: package as an installable skill, not a bloated CLAUDE.md; keep any CLAUDE.md minimal.


### 5. Relevant files (skill package)

```text
.claude/skills/rfp-pipeline/
├── SKILL.md
└── references/
    ├── operating-model.md
    ├── ingestion-and-extraction.md
    ├── audit.md
    ├── harvest.md
    └── migration.md
```

Plus, per opportunity: `RFP-Received/`, `Addenda-Clarifications/` (with `log.md`), `Response/` (drafts + `final-submission.pdf`), `meta.md`.

### 6. End-to-end workflow summary

1. Drop new sources into Raw/; convert to MD/.
2. Extract verbatim-first cards into Curated/cards/, gated through the verification lifecycle.
3. New RFP → create Opportunities/<name>/, file tender in RFP-Received/, log addenda as they arrive.
4. Run rfp-analysis-and-response for compliance matrix and outline.
5. Draft in Response/, sourcing only from Curated/cards/.
6. Lock final-submission.pdf; update meta.md.
7. Harvest reusable material back into Curated/cards/ as draft cards.
8. Periodically run full audit.

<div align="center">⁂</div>

