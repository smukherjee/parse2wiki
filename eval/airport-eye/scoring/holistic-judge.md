# Holistic Quality Scoring — Airport Eye APOC Phase 2

**Scoring agent:** holistic judge (blind to approach identity)
**Scale:** 0–5 (0=absent, 1=poor, 2=weak, 3=adequate, 4=strong, 5=excellent)
**Rubric source:** empathy-reviewer anti-pattern list, calibrated against the client voice profile in `trackB/brief.md`
**Sources read:** both proposals in full, the client-voice brief, and the binding CR/BRD v1.5 (to verify genuine client understanding). Reserved baseline drafts were not read.

---

## Draft A — `eval/airport-eye/trackA/proposal-trackA.md`

A single consolidated 16-section proposal with cover letter, executive summary, understanding, solution, scope, methodology, governance, integration, security, testing, SLA, assumptions, commercial narrative, deviations table, experience, and a populated existing-system inventory appendix.

| # | Dimension | Score | Justification |
|---|---|---|---|
| 1 | Client-specificity | 5 | Written unambiguously for DIAL/APOC Phase 2 — uses DIAL, APOC, WAISL, GEOKNO, IGIA, Aerocity, federated BIM, Concession Agreement, the 19 named OT systems with OEMs and named DIAL owners, the eight-agent roster, and BRD section references (§3.5.4) a DIAL reader would recognise; the populated Appendix D inventory reads as a direct engagement with this client's estate. |
| 2 | Vendor-centric-framing avoidance | 4 | Executive Summary and Understanding lead with DIAL's situation and vision; the cover letter opens with WAISL but only to establish the incumbent-Concessionaire context, which is the load-bearing fact. Loses a point because the "Differentiators" section and recurring "WAISL is uniquely positioned / we already operate" framing, while justified by the incumbent role, still centres the vendor. |
| 3 | Superlative/filler avoidance | 5 | No "world-class / best-in-class / industry-leading / cutting-edge" language; nearly every sentence carries a number, a named system, or a contractual reference; "one of the world's busiest" is factual, and "most transformative component" mirrors the BRD's own wording. |
| 4 | Tone-fit | 5 | Formal, procurement-oriented, risk-aware — mirrors the BRD's aspirational-front / conservative-back tone precisely; gaps are acknowledged in professional, accountable language without theatrics. |
| 5 | Evaluator persuasiveness | 4 | Well-structured, complete, and submission-ready with clear solution architecture, phased plan, binding-KPI tables, milestone schedule, and a deviations table that flags the procurement-mechanism conflict constructively; the honest "to be confirmed from bidder input" handling of case studies and personnel is the main soft spot, but framed gracefully rather than self-underminingly. |

**Draft A overall: 4.6** (23/5)

---

## Draft B — `eval/airport-eye/trackB/proposal-trackB.md`

A 7-volume RFP-v5-structured proposal plus a full 135-row Requirements Traceability Matrix appendix, preceded by an assembler pre-flight checklist (an internal artifact, not part of the client-facing body).

| # | Dimension | Score | Justification |
|---|---|---|---|
| 1 | Client-specificity | 4 | Content is exceptionally specific — verbatim BRD §2.1 quoting, DIAL legal vocabulary ("demised premises / carved-out assets / MCD and DCB area bifurcation"), 19 systems with 10 named owners — but the prose is threaded with internal requirement IDs (R-001, R-074, R-128) and evidence markers that a DIAL evaluator would not recognise, slightly breaking the "written for you" register. |
| 2 | Vendor-centric-framing avoidance | 5 | Disciplined client-need leadership throughout: every volume opens with an "Understanding of the Problem" section centred on DIAL's estate, Volume 1 leads with "DIAL's Problem, In DIAL's Words" before any vendor response, and capability claims are consistently tied back to the client's named systems. |
| 3 | Superlative/filler avoidance | 4 | No ungrounded superlatives, but the same gap flags (R-001, R-007/R-128, R-129, the Singapore-hosting exclusion) are restated across multiple volumes, which reads as structural repetition rather than fresh information; the RTM's marker legend is necessary scaffolding but adds bulk. |
| 4 | Tone-fit | 4 | Formal and risk-aware in the body, matching the BRD's compliance-driven register; however internal-pipeline fingerprints ("per binding-priority order", "conditional-Disqualifying", the unresolved-items checklist at the head of the file) leak a stage-gate-process voice that is more pipeline-internal than DIAL-facing. |
| 5 | Evaluator persuasiveness | 4 | The full RTM and Volume 3's rigorous, source-reconciled AI-agent treatment (roster ambiguity flagged rather than silently resolved, per-agent dependencies on CISF/SHM/MRSS upgrade named) are genuinely persuasive to a sophisticated evaluator, and honest gap handling is rewarded; but the repeated self-description of items as "conditional-Disqualifying", two placeholder case studies, and an effectively empty Team volume leave the submission reading as an honest draft awaiting another pass rather than a finished, confidence-building document. |

**Draft B overall: 4.2** (21/5)

---

## Comparative note

Both drafts are strong and clearly written for this specific client and procurement; neither reads like a generic airport-vendor template, and both handle the binding-KPI / 19-system / 8-agent specifics with real command of the source material. Draft A scores higher on client-facing polish: it is the more submission-ready document, with cleaner tone, no internal-pipeline leakage, and gap-handling that flags incompleteness without dramatising it. Draft B scores higher on client-need leadership and compliance traceability — its 7-volume structure and 135-row RTM are the more rigorous compliance artefact, and its Volume 3 AI-agent treatment is the most intellectually honest handling of the roster/scope ambiguity in either draft. The gap between them is not one of substance but of register: Draft A reads as a proposal an evaluator would receive; Draft B reads as a proposal an evaluator would receive after one more integration pass to strip pipeline scaffolding and close the self-flagged disqualifying gaps. On pure quality-of-thinking they are close; on evaluator-readiness Draft A has a small but consistent edge.