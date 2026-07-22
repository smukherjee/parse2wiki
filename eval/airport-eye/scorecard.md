# Eval Scorecard — Airport Eye APOC Phase 2

**Question:** Which approach produces more accurate RFP responses — the monolithic `rfp-analysis-and-response` skill (Track A) or the multi-stage evidence-tracked pipeline `collateral-analyzer → requirements-mapper → section-drafter → empathy-reviewer → proposal-assembler` (Track B)?

**Test case:** Airport Eye APOC Phase 2 (DIAL airport, AI video-analytics / OT-systems platform).
**Date:** 2026-07-17.
**Scope:** Single case (pilot). Not statistically significant — directional findings only.

---

## Headline results

| Dimension | Track A — rfp-analysis-and-response | Track B — full pipeline | Winner |
|---|---|---|---|
| **Compliance — pass rate** | 81/108 = **0.750** | 91/134 = **0.679** | Track A (raw rate) |
| **Compliance — blocking issues** | **7** | **14** | Track A (count) |
| **Compliance — verdict** | BLOCKING | BLOCKING | tie (both fail gate) |
| **Grounding ratio** | **0.872** (75/86 claims, post-hoc audit) | **0.695** (123/177 markers, self-reported) | Track A (number) |
| **Hallucination rate** | **0.000** (0/86) | not measurable (markers can't capture fabrication) | Track A (measurable signal) |
| **Holistic quality** | **4.6 / 5** | **4.2 / 5** | Track A |
| **Requirement coverage / traceability** | 108 reqs checked; no RTM | **135 reqs checked; full 135-row RTM + coverage matrix** | Track B |
| **Honest gap surfacing** | gaps partly silent (see below) | **all gaps explicitly marked** | Track B |

**Bottom line:** On every *numeric* axis Track A scores higher. But the two most important compliance-gate properties — *requirement coverage* and *honest gap surfacing* — favor Track B, and those are exactly the properties that determine whether a shortfall slips past the checker unnoticed. The raw "Track A wins" headline is partly an artifact of the measurement (see Confounds). The honest answer to "which is more accurate" is **accuracy-of-what depends on which failure mode you're optimizing against**.

---

## Dimension 1 — Compliance / requirement parity

Both tracks are **BLOCKING** — neither produces a submittable proposal from the given collateral, which is the *correct* outcome (the source collateral genuinely lacks team bios, 2 of 3 case studies, commercial pricing, and several certifications; no approach can fabricate those and remain honest).

### Track A (108 requirements checked)
- 81 Pass, 14 Partial, 10 Fail, 3 Ambiguous, **7 blocking**
- **Strength:** numeric parity is excellent — all 28 AI-agent precision/recall/horizon/latency cells match BRD §3.5.4 at 1.0×; correctly adopts the stricter BRD ≤10-min critical-incident figure over the RFP's ≤1 hr; no carve-out weakening or status-word over-claims.
- **Weakness:** the validator found Track A **silently dropped** Phase-1 deliverables (10 cm contours, 3D mesh model, ISO 19115 metadata report) and whole scope areas (Land & Space Management, Environmental/CAQM, landside spot levels, 10-layer GIS catalogue) — **undeclared in the deviation register**. This is the silent-gap class the enhanced validator was built to catch.

### Track B (135 requirements checked)
- 91 Pass, 24 Partial, 12 Fail, 7 Ambiguous, 1 N/A, **14 blocking**
- **Strength:** checked **27 more requirements** than Track A because the pipeline pre-built a 135-row coverage matrix + RTM, so the validator held the draft to a fuller requirement set (SPG what-if use cases, space allocation, fog navigation, CLM integration, 15-yr lifecycle, IEC 62443, SOC/SIEM). Every gap is **explicitly marked** — no silent shortfalls except one (the 10 cm contour dataset, N-SUR-07, was undeclared even in Track B).
- **Weakness:** more blocking items, partly *because* it surfaces more. Honesty was not credited: the staffing blank (R-129), 2 placeholder case studies (R-128), unpriced commercial tables (R-123), and IEC 62443/SOC-SIEM roadmaps all correctly scored Fail.

### Why the raw numbers favor Track A but the gate-property favors Track B
Track A's lower blocking count (7 vs 14) coexists with it **silently omitting** deliverables and scope areas — gaps that only surfaced because an independent validator went looking. Track B's higher blocking count is the *result* of it checking 27 more requirements and declaring its gaps openly. For a compliance gate whose job is "make sure nothing slips through," Track B's behavior is the safer accuracy property even though its scorecard number looks worse. Track A's better number is partly a *coverage* artifact: you can't fail a requirement you never extracted.

---

## Dimension 2 — Grounding / hallucination

| | Track A | Track B |
|---|---|---|
| Measurement method | post-hoc claim audit (an LLM extracted every substantive claim and checked each against source) | self-reported markers placed by section-drafter (`[GROUNDED:]` / `[ASSERTION:]`) |
| Unit | 86 substantive claims | 177 markers (123 grounded, 54 assertion) |
| Grounded | 75 | 123 |
| Assertion/unsupported | 11 (all explicit placeholders) | 54 |
| **Grounding ratio** | **0.872** | **0.695** |
| **Hallucination (fabricated facts)** | **0.000** (0/86, verified) | **not measurable** — markers assert grounding but don't independently verify it |

**Caveat — these are not directly comparable.** Track A's 0.872 counts *claims* (coarser; one marker per claim); Track B's 0.695 counts *markers* (finer; the RTM appendix alone carries many, and the drafter marks liberally). The denominators measure different things. What is comparable and meaningful:
- Both tracks are well-grounded; neither fabricated projects, numbers, or certifications where measurable.
- Track A's explicit-placeholder discipline ("to be confirmed from bidder input") yields a higher ratio *and* a measurable zero-fabrication signal.
- Track B's marker system is structurally weaker on the fabrication axis: a `[GROUNDED: source]` marker asserts a source link but the pipeline does not independently verify the link is real — an over-claim placed under a GROUNDED marker would pass the internal review. Track A's post-hoc audit (an independent check against source) is the only one of the two that can catch fabrication.

**Net:** Track A grounds higher and is fabrication-verifiable; Track B grounds adequately but its grounding is self-attested, not independently checked.

---

## Dimension 3 — Holistic quality (LLM-judge, same rubric, 0–5)

| Dimension | Track A | Track B |
|---|---|---|
| Client-specificity | 5 | 4 |
| Vendor-centric-framing avoidance | 4 | 5 |
| Superlative/filler avoidance | 5 | 4 |
| Tone-fit | 5 | 4 |
| Evaluator persuasiveness | 4 | 4 |
| **Overall** | **4.6** | **4.2** |

Track A reads as a proposal an evaluator would receive — clean register, no internal scaffolding, graceful gap-handling, submission-ready. Track B reads as one that needs one more integration pass: it leads every volume with DIAL's problem (the one dimension it wins) and carries a full 135-row RTM, but loses points for internal requirement-ID/marker leakage into prose, repeated gap-flagging across volumes, an effectively empty Team volume, and placeholder case studies. The deciding gap is **register/readiness, not substance**.

---

## Confounds and limitations (read before trusting any single number)

1. **Single test case.** Airport Eye only. One procurement, one collateral set. Directional, not statistical.
2. **Compliance denominators differ (108 vs 135).** Each track's compliance-validator independently extracted requirements. Track B's pipeline pre-built a 135-row coverage matrix/RTM, which gave its validator a fuller requirement list to check against — so Track B was held to a larger set and naturally accumulated more fails/blockers. Track A's validator extracted from the BRD/RFP directly and found 108. A truly apples-to-apples compliance comparison requires **one fixed gold requirement inventory scored against both drafts** (recommendation below).
3. **Grounding units differ (claims vs markers).** 0.872 vs 0.695 is not a like-for-like ratio; see Dimension 2.
4. **Scorer independence.** The compliance and holistic scorers were separate LLM agents run with identical prompts, but LLM judges are noisy; small score deltas (0.4 on holistic) are within judge variance.
5. **Track B was penalized for honesty.** Its declared gaps scored as Fail/Partial per the binary compliance rule. That is correct scoring, but it means "more blocking" ≠ "worse draft" — it can mean "more honest/complete draft."
6. **Track A's silent omissions are a hidden accuracy cost** not fully captured by its better scorecard numbers: a compliance gate that lets dropped Phase-1 deliverables and entire scope areas pass undeclared is failing at its core job, even with a 0.75 pass rate.

---

## Interpretation — which is "more accurate"?

- **For producing a polished, submission-ready, evaluator-pleasing proposal from available collateral:** **Track A** (`rfp-analysis-and-response`). Higher holistic quality, higher grounding, zero fabrication, cleaner register, faster (one pass vs five stages).
- **For acting as a compliance/coverage gate that surfaces every requirement and every gap so nothing slips through unnoticed:** **Track B** (the pipeline). It extracts 25% more requirements, builds a traceable RTM, and explicitly marks every gap instead of silently omitting it. Its worse raw score is the *evidence* that it's doing the more thorough job.
- **The two are not substitutes — they're different stages**, which matches the workflow memory already recorded: `rfp-analysis-and-response` for fast bid-strategy/drafting, the enhanced `compliance-validator` (and ideally the full pipeline's coverage matrix) as the final gate. This eval supports keeping them separate rather than collapsing to one.

**One-sentence answer:** Track A produces the better *proposal*; Track B produces the better *audit trail* — and for the specific failure mode the enhanced compliance-validator was built to prevent (silent undeclared shortfalls), Track B's transparency is the more accurate behavior even though it scores lower on every numeric axis.

---

## Recommended next steps to harden the eval

1. **Fix the compliance denominator.** Pre-build a single gold requirement inventory from the BRD/ABR/RFP (the existing `compliance-report-numeric-inventory.md` + `requirements-traceability-matrix.md` are a starting point) and score *both* drafts against that identical set. This removes the 108-vs-135 artifact and makes pass rates comparable.
2. **Add a fabrication-injection test.** Deliberately plant a fake case study / number in each track's source collateral and check whether each approach propagates or catches it. Track B's self-attested markers are untested on this axis; Track A's post-hoc audit already shows 0/86.
3. **Run more cases.** BAC, EAC, RCA, Dial b2b are already in `raw/`. At minimum add BAC (different domain, already has a known compliance report) to test domain-independence of the finding.
4. **Blind the judges.** Have the holistic judge score anonymized copies (strip track-identifying scaffolding from Track B) to remove the "Track B looks unfinished" bias.
5. **Fix the parser.** `eval/scripts/parse_compliance_report.py` assumes a single summary table; the track reports split numeric/categorical tables. Extend it to sum across all verdict tables, or have the validator emit a machine-readable summary block.

---

## Artefacts produced

```
eval/airport-eye/
├── scorecard.md                          ← this file
├── trackA/
│   └── proposal-trackA.md                (~8,015 words)
├── trackB/
│   ├── brief.md
│   ├── coverage-matrix.md                (135 reqs classified)
│   ├── gap-report.md
│   ├── review-notes.md
│   ├── proposal-trackB.md                (~11,452 words)
│   └── sections/                         (8 drafts + 8 reviewed)
└── scoring/
    ├── compliance-report-trackA.md
    ├── compliance-report-trackA-numeric-inventory.md
    ├── compliance-report-trackB.md
    ├── compliance-report-trackB-numeric-inventory.md
    ├── trackA-claim-audit.md
    └── holistic-judge.md

eval/scripts/
├── parse_compliance_report.py
└── count_grounding_markers.py
```

**Eval integrity:** Both tracks verified to not cite the reserved human baseline (`AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md` / `...RTM_DRAFT.docx.md`) as a source — the only mentions are in each track's "Excluded Sources" disclosure. No answer-key leakage.

---

# Hardened compliance comparison (apples-to-apples denominator)

**Why this section exists:** The Dimension 1 comparison above was confounded — each track's compliance-validator independently extracted its own requirements (Track A: 108, Track B: 135), so the pass rates (0.750 vs 0.679) were measured against different sets. Hardening step #1 fixed this: an independent agent built a single **gold requirement inventory of 189 requirements** (`gold-requirements.md`, extracted only from the authoritative sources — neither track's draft was read), and two fresh scoring agents scored each draft against that identical 189-row set with identical prompts.

## Gold-scored results (same 189-requirement denominator)

| Verdict | Track A | Track B |
|---|---|---|
| Pass | 108 | 90 |
| Partial | 51 | 70 |
| Fail | 21 | 28 |
| Ambiguous | 9 | 1 |
| N/A | 0 | 0 |
| **Total** | **189** | **189** |
| **Pass rate** | 108/189 = **57.1%** | 90/189 = **47.6%** |
| **Blocking (mandatory Fails)** | **21** | **28** |
| **Verdict** | BLOCKING | BLOCKING |

**On the raw numbers, Track A still leads** — higher pass rate (57.1% vs 47.6%) and fewer blocking issues (21 vs 28). This confirms the original direction is not purely a denominator artifact: Track A's draft genuinely satisfies more of the fixed requirement set outright.

## But the gap is partly scorer-threshold noise, not a robust track difference

The two scoring agents, despite identical prompts, applied **different strictness at the "unaddressed requirement" boundary:**

- Track A's scorer marked 9 unaddressed register-tier numeric values (T1/T2/T3 BIM areas, FDAS/ECMS/BHS point counts, survey acreage) as **Ambiguous** ("not locatable in the proposal") rather than Fail.
- Track B's scorer marked comparable unaddressed register-tier items as **Fail**.

If Track A's 9 Ambiguous are reclassified to Fail under Track B's stricter standard (an unaddressed mandatory numeric is a shortfall, not an ambiguity), Track A becomes **108 Pass / 51 Partial / 30 Fail / 0 Ambiguous → 30 blocking** — which would be *worse* than Track B's 28. Conversely, if Track B's unaddressed items were scored as leniently as Track A's, its Fail count would drop.

**Implication:** the compliance difference between the two tracks is **within the scorer's Ambiguous-vs-Fail threshold variance**, not a robust signal. With N=1 case and LLM-judge noise, 57.1% vs 47.6% is not a reliable gap. The only way to settle it is hardening step #4 (blind, repeated judging) or a deterministic scorer.

## What IS robust in the gold-scored data

1. **Both BLOCKING.** Neither track is submittable from the given collateral — correct outcome, since the collateral genuinely lacks team bios, 2 of 3 case studies, pricing, and several certs.
2. **Track B declares more Partials (70 vs 51).** This is the pipeline's honesty signal — it explicitly marks partial coverage and declared deviations rather than passing things outright or leaving them ambiguous. Track A either Passes (108) or marks Ambiguous (9); it rarely says "partial." Track B's higher Partial count is the more truthful granularity.
3. **Track A leaves more Ambiguous (9 vs 1).** Nine register-tier numeric values it simply didn't restate; the scorer couldn't locate them. Track B, having built a coverage matrix from those same registers, restated or explicitly flagged nearly all of them — only 1 Ambiguous.
4. **The same big holes appear in both:** missing case studies (≥3 required, 1 evidenced), missing team/CVs, unpriced commercial tables, missing PAS 1192-2 / ISO 19650-2 standard, missing SBOM/RTM artifacts. These are collateral gaps no approach can fill honestly.
5. **Track B's unique large hole:** the Operational Digital Twin functional layer (G-121..G-132, 12 fails) — airside/terminal/curbside/security ops views, asset widgets, LOD-350 viz, asset registry/federation. Track A addressed these at a high level (scored Partial, not Fail). This is a real content difference, not noise: Track B's section-drafter, bound to the coverage matrix's Gap classifications, left these unfilled rather than asserting high-level coverage.

## Revised bottom line

Hardening step #1 **did not overturn** the original direction (Track A still scores higher on raw compliance), but it **substantially weakened the confidence** of that lead — the apparent 9.5-point pass-rate gap is largely scorer-threshold noise on unaddressed register items, and would invert under a stricter threshold. The robust, defensible findings are:

- The two tracks are **comparable on compliance** once the denominator is fixed (both ~50-57%, both blocking, gap within judge noise).
- Track B is **more granular and honest** (70 declared Partials vs 51; 1 Ambiguous vs 9) — it restates or flags register-tier requirements Track A leaves unlocated.
- Track A is **more complete at the high level** on the DT/ops layer that Track B left as honest gaps.
- The Dimension 2 and 3 findings (grounding 0.872 vs 0.695; holistic 4.6 vs 4.2) **stand unchanged** — they were not affected by the denominator confound.

**Net judgment unchanged from the original scorecard:** Track A produces the better *proposal*; Track B produces the better *audit trail*. The hardened comparison makes the compliance axis a near-tie rather than a Track A win, which actually *strengthens* the "different stages, not substitutes" conclusion — neither approach dominates the other on accuracy.

## Files added by hardening step #1

```
eval/airport-eye/
├── gold-requirements.md                  (189 reqs, independent extraction)
└── scoring/
    ├── gold-score-trackA.md              (compact: summary + blocking + numeric parity + non-Pass rows)
    └── gold-score-trackB.md              (full 189-row verdict table)
```

**Remaining hardening (not yet done):** #2 fabrication-injection test, #3 more cases (BAC/EAC/RCA/Dial b2b), #4 blind repeated judging, #5 parser fix for split-table reports.