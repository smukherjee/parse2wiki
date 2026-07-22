# Holistic LLM-Judge Scoring — BAC Underwing Analytics RFP (BAC-T-26-505)

**Judge model:** glm-5.2 (independent LLM-judge, single pass, same rubric)
**Date:** 2026-07-17
**Ground truth sources read:**
- `sources/BAC/BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md` (authoritative RFP)
- `sources/BAC/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md` (Tab F: FR01–FR73, NF01–NF48, PMR-01..PMR-10, ISRA 1–29)

**Drafts scored:**
- Track A: `eval/bac/trackA/proposal-trackA.md`
- Track B: `eval/bac/trackB/proposal-trackB.md`

Excluded per instructions: `eval/airport-eye/`, any `*Proposal_DRAFT*` / `*RTM_DRAFT*` answer key.

---

## Rubric

Each dimension scored 1–5 (5 = excellent, 1 = unacceptable) with a one-sentence justification.

### 1. RFP understanding & responsiveness
Addresses BAC's actual Underwing Analytics requirements: GSE detection (FR17), turnaround tracking (FR24), alerting (FR43), the NF/PMR/ISRA Tab F set, insurance, commercial, and ISRA data sovereignty.

| Draft | Score | Justification |
|---|---|---|
| Track A | 4 | Comprehensive coverage of all Tab F domains with explicit FR17/FR24/FR43 callouts, a full ISRA row-by-row table, insurance table, and commercial section; understands Terminal/Airside Operations users and the Australian regulatory frame. |
| Track B | 4 | Equally comprehensive and explicitly maps the 170 Tab F rows to a coverage classification, naming FR17/FR24/FR43 and the disqualifying gaps; correctly identifies the user communities and Australian regulatory context. |

### 2. Solution quality & technical credibility
Architecture, feasibility, and credibility of the proposed technical solution.

| Draft | Score | Justification |
|---|---|---|
| Track A | 3 | Architecture is detailed and credible (3-layer Edge/Platform/UI, Lakehouse, AWS EKS, multi-AZ), but credibility is undermined by asserting full existing conformance for FR17 camera-based GSE classification and FR20 personnel detection without evidencing them from collateral. |
| Track B | 4 | Same architecture, but it explicitly separates Grounded / Assertable / Gap and commits to a delivery roadmap with per-class acceptance criteria for the ungrounded CV models, making the solution story more realistic and trustworthy. |

### 3. Compliance & numeric parity
Measurable thresholds — RTO ≤4h (NF07), Sev-1 ≤1h (NF19), insurance $20m/$10m/$10m (§4.4), 90-day validity (§4.2), 3-yr term (§4.3), 6-mo defects (PMR-10), 20% retention (PMR-09) — addressed correctly; conflicts/missing items declared, not fabricated.

| Draft | Score | Justification |
|---|---|---|
| Track A | 3 | All numeric thresholds are stated correctly (RTO 4h binding with 40-min design objective noted, Sev-1 ≤1h, $20m/$10m/$10m, 90 days, 3-yr term, 6-mo defects, 20% withhold) and the RFP issue-date inconsistency (15 May vs 15 June) is surfaced, but Tab F conformance is marked "Yes" across the board including FR17/FR20/NF19, hiding capability gaps rather than declaring them. |
| Track B | 4 | All numeric thresholds correct and prominently tabulated; the five disqualifying compliance gaps (FR17, FR20, NF19, ISRA-19, ISRA-25) are explicitly declared with committed resolution paths rather than asserted as met. |

### 4. Grounding & honesty
No fabrication; gaps declared; source conflicts like the UTAM Athens/EU framing reconciled, not propagated.

| Draft | Score | Justification |
|---|---|---|
| Track A | 2 | Reconciles the UTAM Athens/EU/GDPR/NIS2 framing to the Australian Privacy Act / ASD Essential 8 context (Sections 4.9, 9.3, D01) and honestly placeholders bios/referees/pricing/certs, but materially overstates existing capability by claiming "TurnWise detects and classifies GSE against the FR17 taxonomy" and "detects personnel presence… (FR20)" as conformant when the source collateral does not evidence camera-based GSE-type classification or personnel-presence detection. |
| Track B | 5 | Exemplary honesty: declares 5 disqualifying gaps and 22 manageable gaps by ID, states "We will not fabricate team bios, referees, case studies, pricing values, or certifications," rewrites every Athens/Hellenic-DPA/GDPR/EU-residency reference to the Australian frame, and flags that the Turnwise IST–NAP example route and non-Australian registration must be reframed to BNE. |

### 5. Polish & readability
Prose quality, structure, register appropriate to a formal airport procurement.

| Draft | Score | Justification |
|---|---|---|
| Track A | 5 | Clean, well-structured, formal procurement register throughout — cover letter, executive summary, dedicated subsections per FR cluster, consistent tables, professional buyer-facing voice, no draft scaffolding visible in the body. |
| Track B | 3 | Content is well-organised into 14 numbered sections, but the document ships with a Pre-Flight Checklist, inline "Section assembly" meta-notes, tone-gate scoring tables, and "carved out" commentary that read as internal working-draft artefacts rather than a submission-ready proposal. |

### 6. Submission-readiness
Usable as a draft basis — completeness vs placeholder-dependence.

| Draft | Score | Justification |
|---|---|---|
| Track A | 4 | Structurally close to a submittable draft (cover letter, all RFP sections, deliverables table, ISRA table, insurance table, deviation register); needs only bidder-input placeholders filled (bios, referees, pricing, certs, contract execution) — but the FR17/FR20/NF19 overstatement must be corrected before it can be honestly submitted. |
| Track B | 3 | Honest and audit-ready on gaps, but explicitly a draft with a long unresolved-items checklist (vendor contact, Schedule A/C/E content, QA docs, hosting target, camera models, Phase-2 scope, civil-cost responsibility, signatures) and meta-scaffolding that must be stripped/completed before submission. |

---

## Overall Scores

| Dimension | Track A | Track B |
|---|---|---|
| 1. RFP understanding & responsiveness | 4 | 4 |
| 2. Solution quality & technical credibility | 3 | 4 |
| 3. Compliance & numeric parity | 3 | 4 |
| 4. Grounding & honesty | 2 | 5 |
| 5. Polish & readability | 5 | 3 |
| 6. Submission-readiness | 4 | 3 |
| **Sum / 30** | **21** | **23** |
| **Overall /5** | **3.5** | **3.8** |

---

## Comparative Verdict

Track B is the more accurate and trustworthy draft, while Track A is the more polished and structurally complete one. They differ most sharply on **grounding & honesty** (B 5 vs A 2) and **polish & readability** (A 5 vs B 3). On numeric parity both correctly state RTO ≤4h, Sev-1 ≤1h, $20m/$10m/$10m insurance, 90-day validity, 3-year term, 6-month defects, and 20% retention, but Track A then marks Tab F conformance "Yes" across the board — including FR17 camera-based GSE-type classification, FR20 personnel presence, and NF19 tiered support — which the source collateral does not evidence and which Track B explicitly declares as disqualifying gaps with committed delivery roadmaps. That single difference drives the credibility gap: Track B's explicit "Grounded / Assertable / Gap" classification and its refusal to claim capabilities it cannot evidence makes its solution story more believable and its compliance posture defensible, whereas Track A's blanket conformance would likely fail an evaluator's evidence check on the very items (FR17, FR20) that the RFP treats as core camera-AI differentiators. Track A is further ahead as a formatting/template basis and would be the stronger draft if its FR17/FR20/NF19 claims were rewritten to match Track B's honest gap-with-mitigation treatment; Track B is further ahead as an evidence-true draft but needs its meta-scaffolding stripped and its placeholders filled before it can be lodged. Neither is submission-ready today: A must fix its overstatements, B must fill its placeholders and shed its working-draft scaffolding.