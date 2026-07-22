# Eval Scorecard — BAC Underwing Analytics (cross-case / domain-independence test)

**Question:** Do the Airport Eye findings generalize? Specifically — is the monolithic `rfp-analysis-and-response` (Track A) consistently higher-polish / higher-grounding / zero-fabrication, and is Track B consistently better at coverage / honest gap surfacing, with compliance a near-tie?

**Test case:** Brisbane Airport Corporation (BAC) Underwing Analytics RFP (BAC-T-26-505). A different domain (airside GSE analytics / turnaround tracking) and a different response shape (the RFP directs responses into an Excel response sheet, Tab F, not a narrative proposal) from Airport Eye (DIAL airside AI video-analytics / OT).
**Date:** 2026-07-17.
**Scope:** Second case (n=2). Still not statistically significant — directional only, but now a *comparison* of comparisons.

**Condition note (differs from Airport Eye):** stop-slop is now baked into Track A (project-local skill) and into Track B stage 5. On Airport Eye neither track had stop-slop. So the **polish axis is not a clean cross-case comparison** (Track A's polish got an extra lever on BAC). Compliance, grounding, coverage and gap-surfacing axes are still comparable. The holistic judge did not penalise Track A's polish (5/5) — Track A's loss on BAC was on grounding/honesty, not prose.

---

## Headline results (BAC)

| Dimension | Track A — rfp-analysis-and-response | Track B — full pipeline | Winner |
|---|---|---|---|
| **Compliance-validator (own extraction)** | 59 reqs: 37 P / 17 Pa / 0 F / 3 A, **6 blocking** | 188 reqs: 81 P / 32 Pa / 69 A / 7 F, **11 blocking** | Track A (raw count); Track B (coverage) |
| **Gold-score (fixed 269-mandatory denominator)** | 212 P / 45 Pa / 4 F / 8 A → **78.8% pass**, **4 blocking** | 93 P / 116 Pa / 31 F / 29 A → **34.6% pass**, **2 blocking** | Track A (rate); Track B (fewer blocking) |
| **Numeric parity** | **24/29** at parity | **16/29** at parity | Track A |
| **Grounding ratio** | **0.94** (96/102, post-hoc claim audit) | **0.580** (166/286, self-reported markers) | Track A (number) |
| **Hallucination (fabricated facts)** | **0.000** (0/116) | not measurable (markers don't verify) | Track A (measurable signal) |
| **Holistic quality** | **3.5 / 5** | **3.8 / 5** | **Track B** ← reversed vs Airport Eye |
| **Requirement coverage / traceability** | 59 reqs checked; no RTM | **188 reqs checked; 170-row coverage matrix** | Track B |
| **Honest gap surfacing** | conformance asserted from collateral; 28 placeholders | **31 Fail + 124 [GAP] markers all declared** | Track B |

**Bottom line:** Track A's *zero-fabrication* and *high-grounding* properties **generalize** (0.872→0.94 grounding, 0 fabrication both cases). But Track A's **polish/holistic win did NOT generalize** — on BAC the holistic judge scored Track B higher (3.8 vs 3.5) because Track A asserted full Tab F conformance (FR17 camera GSE classification, FR20 personnel detection, NF19 tiered support) from collateral that *describes* those capabilities without committing to delivery, which read as **overstatement on the RFP's core differentiators**. Track B declared those same items as disqualifying gaps with committed roadmaps. Meanwhile the gold-score 78.8% vs 34.6% gap is largely a **scoring artifact** (Track B's honesty is penalised as Partial/Fail), not a real accuracy gap — Track B actually has *fewer* real blocking issues (2 vs 4) and they are more material.

---

## Dimension 1 — Compliance / requirement parity

### Track A (gold-score, 269 mandatory)
- 212 Pass, 45 Partial, 4 Fail, 8 Ambiguous; **4 blocking**; numeric parity 24/29.
- **Strength:** numeric parity is excellent — all binding SLAs, insurance ($20m PL / $10m PI / $10m Cyber), 3-yr term + 2×1-yr extensions, RTO ≤4h (UTAM's 40-min figure correctly subordinated via D11), 90-day validity, Sev-1/2/3 response times match exactly. UTAM's AIA/Athens/EU/GDPR framing reconciled to Brisbane/Australian context.
- **Weakness:** the 4 blocking items are **undeclared mandatory declarations** (addenda acknowledgment S-14, Conflict-of-Interest declaration C-13, major-changes disclosure C-14, Social Procurement / Supply Nation / Modern Slavery C-15) — none in the deviation register. Plus the 5-page supporting-PDF limit (N-19) is over-claimed (document exceeds 5 pages, not declared).
- **The over-claim the validator missed:** the compliance-validator (own 59-req extraction) scored FR17/FR20/NF19 as Pass/Partial and reported **0 Fail** — it took Track A's asserted conformance at face value because the claims are *sourced* in UTAM. The gold-scorer also scored them Pass. Only the holistic judge (stricter "is this a defensible compliance commitment" standard) flagged them. See Measurement-standard split below.

### Track B (gold-score, 269 mandatory)
- 93 Pass, 116 Partial, 31 Fail, 29 Ambiguous; **2 blocking**; numeric parity 16/29.
- **Strength:** checked **188 requirements** vs Track A's 59 (coverage-matrix-driven, same pattern as Airport Eye's 135 vs 108). Every gap explicitly declared (31 Fail all listed in §13; 124 [GAP] markers). UTAM Athens/EU framing properly excluded and rewritten to Privacy Act/APPs/ASD Essential 8.
- **Weakness:** the **116 Partial** is inflated by a systemic issue — the draft answers all 29 ISRA rows but supplies **no residual-risk ratings**, so every ISRA row tops out at Partial. Plus "assertable" Tab F rows (claimed but not per-row evidenced) score Partial. This honesty is *penalised* by the gold-scorer's Pass/Partial/Fail scale.
- **Track B over-claimed too:** the compliance-validator and gold-scorer both caught that Track B's NF19/§10 SLA matrix over-claims — Sev-1 resolution "best-effort continuous" (no ≤4h bound) and Sev-2 resolution "within 1 business day" (>4h) are **undeclared deviations** (the 2 blocking items N-10, N-13). Sev-3 resolution is internally contradictory (table 3 days vs note 8h). So over-claiming is **not Track-A-exclusive**; Track B over-claims when it asserts conformance without evidence, just less often.

### Why the gold-score gap (78.8% vs 34.6%) is mostly a scoring artifact
Track A asserts conformance grounded in UTAM collateral → scored Pass. Track B declares "assertable, not yet evidenced" → scored Partial; declares "gap" → scored Fail. The denominator is the same (269), but Track B's *honesty* converts would-be Passes into Partials/Fails. The **blocking** count is the cleaner signal: Track A 4 (missing declarations) vs Track B 2 (undeclared SLA shortfalls). Track B's 2 are more *material* (the RFP's core support SLA), Track A's 4 are more *administrative* (declarations). Neither dominates.

### Measurement-standard split (the key BAC finding)
Three scorers applied three different standards to Track A's FR17/FR20/NF19 conformance claims:
| Scorer | Standard | Track A verdict |
|---|---|---|
| compliance-validator | "is the requirement addressed?" | Pass / Partial (0 Fail) |
| gold-scorer | "is the claim sourced?" | Pass (grounded in UTAM) |
| holistic judge | "is the source strong enough for a compliance commitment?" | **Overstatement** (collateral describes capability, not committed delivery) |
All three can be right simultaneously. The lesson: a single compliance pass is insufficient — the validator/gold-scorer take asserted-and-sourced conformance at face value and miss capability-vs-commitment overstatement. The holistic judge (and a human evaluator) catch it. This is the same class of failure the enhanced compliance-validator was built for, and it shows the **gate still has a blind spot on sourced-but-weak conformance**.

---

## Dimension 2 — Grounding / hallucination

| | Track A | Track B |
|---|---|---|
| Method | post-hoc claim audit | self-reported markers |
| Unit | 116 substantive claims | 286 markers (166 grounded, 120 assertion) |
| Grounded | 96 | 166 |
| Unsupported / Assertion | 6 (accurate-but-uncited) | 120 |
| Placeholder | 14 | (124 [GAP] separately) |
| Fabricated | **0** | not measurable |
| **Grounding ratio** | **0.94** | **0.580** |
| **Hallucination** | **0.000** | not measurable |

**Generalises from Airport Eye:** Track A 0.872→0.94 grounding, 0 fabrication both cases. Track B 0.695→0.580. The Track-A-higher-grounding pattern holds. Caveat is unchanged: the denominators measure different things (claims vs markers), not directly comparable.

---

## Dimension 3 — Holistic quality

| Dimension | Track A | Track B |
|---|---|---|
| 1. RFP understanding & responsiveness | 4 | 4 |
| 2. Solution quality & technical credibility | 3 | 4 |
| 3. Compliance & numeric parity | 3 | 4 |
| 4. Grounding & honesty | **2** | **5** |
| 5. Polish & readability | **5** | 3 |
| 6. Submission-readiness | 4 | 3 |
| **Overall** | **3.5** | **3.8** |

**This reverses Airport Eye** (A 4.6 > B 4.2). The reversal is concentrated in two dimensions:
- **Grounding & honesty (A 2 vs B 5):** Track A's blanket Tab F "Yes" on FR17/FR20/NF19 without committed delivery read as overstatement; Track B's explicit disqualifying-gap declaration read as defensible.
- **Solution quality & compliance (A 3 vs B 4):** Track B's committed CV-classifier delivery roadmaps with acceptance criteria (FR17 per-class precision/recall, FR20 personnel-presence model) were judged more credible than Track A's asserted conformance.
- Track A still wins **polish 5 vs 3** (stop-slop present, but Track B's working-draft scaffolding / 116-Partial tone dragged it down).

**Interpretation:** On Airport Eye, Track A's high-level coverage read as polished completeness; on BAC, the same strategy read as overstatement because BAC's *core differentiators* (camera-AI GSE classification, personnel detection) are exactly where collateral is weakest. The difference is the **alignment between where the RFP's hardest requirements sit and where the collateral is thin**. When they coincide, Track A's assert-from-collateral strategy is risky; when they don't (Airport Eye's numeric SLA parity was well-evidenced), it's safe.

---

## Cross-case comparison — does Airport Eye generalise?

| Property | Airport Eye finding | BAC finding | Generalises? |
|---|---|---|---|
| Track A zero fabrication | 0/86 | 0/116 | **Yes** (both cases) |
| Track A higher grounding | 0.872 vs 0.695 | 0.94 vs 0.580 | **Yes** |
| Track A higher holistic/polish | 4.6 vs 4.2 | 3.5 vs 3.8 | **No — reversed on BAC** |
| Track B better coverage/traceability | 135 vs 108 reqs | 188 vs 59 reqs | **Yes** (stronger on BAC) |
| Track B honest gap surfacing | all gaps marked | 31 Fail + 124 [GAP] declared | **Yes** |
| Compliance near-tie (within judge noise) | 57.1% vs 47.6%, 21 vs 28 blocking | 78.8% vs 34.6%, 4 vs 2 blocking | **No — large raw gap on BAC, but it's a scoring artifact** |
| Over-claiming is Track-A-only | (not tested) | Track B over-claimed NF19 too | **New finding: over-claiming is engine-universal, not Track-A-specific** |

**What generalises:**
1. Track A's zero-fabrication + high-grounding property is robust across both domains.
2. Track B's coverage-matrix-driven fuller requirement checking is robust (and stronger on BAC: 188 vs 59).
3. Track B's honest gap declaration is robust.

**What does NOT generalise:**
1. Track A's holistic/polish win — reversed on BAC. The polish advantage is real but can be outweighed by overstatement risk when the RFP's hardest requirements align with thin collateral.
2. The compliance "near-tie" — on BAC the gold-score gap is large (78.8% vs 34.6%), but it is an artifact of the scorer rewarding asserted conformance and penalising declared gaps. The *real* blocking-issue comparison (4 vs 2) is closer and arguably favours Track B on materiality.

**New finding neither case alone showed:**
- Over-claiming (asserting conformance from weak/uncited evidence) is **engine-universal**: Track A did it on FR17/FR20/NF19; Track B did it on NF19 resolution times. Both were caught only by the combination of compliance-validator + gold-scorer + claim-audit + holistic judge — no single scorer caught both engines' over-claims. This validates the optimized workflow's stage 6 (compliance gate loop) + stage 7 (periodic post-hoc claim-audit) as **necessary for both tracks, not just Track A**.

---

## Confounds & caveats

1. **n=2, single-judge, single-run.** No blind/repeated judging. The holistic reversal (A 4.6→3.5, B 4.2→3.8) could be partly judge variance — a different judge might score Track A's polish higher. Hardening step #4 (blind repeated judging) is still the highest-value remaining step.
2. **Response-sheet vs narrative mismatch.** BAC's real deliverable is a filled Excel response sheet (Tab F), not a narrative proposal. Both tracks were asked to draft a narrative technical response, which is somewhat artificial for BAC. This advantages Track A (narrative drafting is its native mode) — yet Track B still won holistic, which makes the reversal more credible, not less.
3. **stop-slop condition change.** Track A had stop-slop on BAC but not Airport Eye. This should *help* Track A's polish, and indeed Track A scored 5/5 polish — so the condition change cuts against the reversal, making the Track B holistic win conservative (the real non-stop-slop gap would be wider).
4. **Gold-scorer Pass/Partial threshold asymmetry.** Track B's 116 Partial is inflated by the systemic ISRA-no-residual-risk-rating issue (all 29 ISRA rows capped at Partial) and "assertable" Tab F rows. A scorer that credited declared-and-committed gaps as Pass-with-caveat would narrow the 78.8% vs 34.6% gap substantially. The blocking count (4 vs 2) is the more robust metric.
5. **Parser limitation (carried from Airport Eye).** `parse_compliance_report.py` undercounts split numeric/categorical-table reports; BAC numbers above are from agent-reported authoritative counts, not the script.
6. **Same answer-key isolation preserved.** No BAC DRAFT answer-key existed to leak (the "Draft" file was collateral). Gold-inventory and gold-scoring agents were isolated from the opposite track's draft.

---

## What this changes in the optimized workflow (`eval/optimized-workflow.md`)

1. **Stage 4 (hybrid drafter) is reaffirmed but tightened.** Track A's drafting engine is still the better prose producer, but the BAC case shows it must be fed Track B's coverage matrix *and* explicitly instructed NOT to assert conformance where the coverage matrix says Gap/Assertable — it must declare, not smooth over. The hybrid instruction gains a line: "where coverage = Gap or Assertable, do not assert Pass; declare the gap or commit a delivery roadmap."
2. **Stage 6 (compliance gate) + Stage 7 (claim-audit) are now mandatory for BOTH tracks**, not just as a Track-B-derived safety net. Track B over-claimed NF19 on BAC; without the gate+audit it would have shipped an undeclared SLA shortfall.
3. **A new "capability-vs-commitment" check** should be added to the compliance-validator: for any requirement the draft marks Pass, require either (a) a source that commits to delivery (not just describes capability) or (b) a declared roadmap with acceptance criteria. This closes the sourced-but-weak-conformance blind spot both cases exposed.
4. **Polish is not a reliable Track-A advantage across domains.** Stage 5 (empathy + stop-slop) should run on both tracks' output, not be assumed to favour Track A.

---

## Open hardening (unchanged from Airport Eye, now with BAC priority order)
- **#4 blind repeated judging** — highest priority: would tell us if the holistic reversal (A 4.6→3.5) is judge variance or real. Run 3 blind judges on both BAC drafts.
- **#2 fabrication-injection** — inject 5 fabricated claims into each BAC draft, see if markers/claim-audit/validator catch them. Tests whether stage 7 is catching fabrication or just over-claim.
- **#3 more cases** — EAC / RCA / Dial b2b. Two more cases would make the "Track A polish win doesn't generalise" claim a pattern (n=3) rather than a single reversal.
- **#5 parser fix** — lowest priority; agent-reported counts are working.