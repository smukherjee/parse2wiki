---
name: rfp-pipeline
summary: End-to-end RFP knowledge pipeline. Converts raw source documents into token-optimised markdown (doc2md engine), then enforces provenance, verification gates, taxonomy, and audit across the curated knowledge layer.
version: 2
---

# RFP Pipeline Skill

Use this skill for any RFP knowledge base, bid repository, or proposal wiki task —
from converting raw source files, through extraction into reusable knowledge cards,
to auditing the wiki for staleness and broken provenance.

This is a single portable skill. It absorbs document conversion (via the doc2md
engine) as its ingest layer, so no separate conversion skill needs to be installed
or invoked. Folder paths follow the RFP extraction convention (`Raw/`, `MD/`,
`WIP/`, `Curated/`), not doc2md's own default `raw/`/`sources/` naming.

## Core invariant

Nothing becomes trusted ground truth without a traceable, verbatim link back to its source.

Every rule in this skill — conversion, hashing, extraction, verification, audit — is
an instance of this invariant. New edge cases get a new check under this invariant,
not a bypass of it.

## Repository structure

```text
RFP Knowledge Master/
├── WIP/       <- scratch drafting, excluded from retrieval and audit
├── Raw/       <- immutable source documents (docx, pptx, pdf, xlsx). doc2md input.
├── MD/        <- token-optimised markdown + Mermaid. doc2md output. Never hand-edit.
└── Curated/
    ├── cards/
    ├── tags/
    └── index/
