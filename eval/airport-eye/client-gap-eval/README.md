# Client vs. Skill Eval — Scoreboard (Corrected, Genuinely Blind)

**Gold set:** 46 client gaps (`C-001..C-046`) in `client-gaps-inventory.md`.
**Predicted set:** 13 skill gaps (`S-001..S-013`) in `skill-derived-gaps.md`.
**Date:** 23-July-2026.

**Supersedes:** an earlier version of this scoreboard that reported a false Recall = 1.000. That run was not actually blind — 25 of its 78 rows cited the client gap document directly. The contaminated artefacts are preserved as `skill-derived-gaps-ASSISTED-CONTAMINATED.md` and `client-vs-skill-eval-ASSISTED-CONTAMINATED.md` for the audit trail. This scoreboard reflects a genuinely blind re-run (fresh subagent, no exposure to the client gap document or this eval directory).

---

## 1. Headline metrics

| Metric | Value | Calculation |
|---|---|---|
| Client gaps matched | 3 / 46 | 6.5% |
| Skill gaps matching a client gap | 7 / 13 | 53.8% |
| Skill-only gaps (not in client set) | 6 / 13 | 46.2% |
| **Recall** | **0.065** | TP / (TP + FN) = 3 / 46 |
| **Precision** | **0.538** | TP / (TP + FP) = 7 / 13 |
| **F1 score** | **0.116** | 2·P·R / (P + R) |
| False negatives (missed client gaps) | 43 | |
| False positives (skill-only gaps) | 6 | S-007..S-012 — all real, source-binding findings, just not in the client's list |

---

## 2. Headline finding

**Recall = 0.065, not 1.000.** A genuinely blind run of the compliance-validator — bound only to the CR/ABR/RFP/Requirements Register/RTM and the proposal — surfaces only 3 of the client's 46 gaps (C-009 weak, C-011 strong, C-037 weak). This is expected, not a regression: **43 of the 46 client gaps are not derivable from the formal source documents at all.** They are the client's own post-review preferences and tightening (accountability reassignment, tighter numeric thresholds, named-but-undocumented policies, BIM/IFC architecture depth) that were never written into the CR/ABR/RFP/Register. A blind, source-bound check is structurally incapable of citing a source for them.

One match, **C-011** ("All 8 AI Agents must be explicitly detailed"), is a strong direct hit: the blind run independently found the AI-agent catalogue incomplete from six angles (S-001–S-006).

One item, **C-023** (RACI revision demanding WAISL be A+R), surfaces a genuine **conflict**, not a gap: the skill's S-012 flags the proposal's already-reversed RACI (vendor made Responsible instead of DIAL, per the CR's §5.3) as a compliance Fail against the binding CR — but the client's own gap list asks for exactly this kind of reversal. The formal source and the client's post-hoc preference disagree, and the proposal sided with the preference. See `client-vs-skill-eval.md` §2 for the full analysis.

**What this means for the eval design:**
- The compliance-validator is a strict, source-bound gate. It is a strong check against the *formal* requirement baseline (CR/ABR/RFP/Register) but is **not** a substitute for client review — the two catch structurally different failure classes.
- The right fix is not to loosen the skill's blindness/provenance discipline, but to give it a legitimate additional input: `stakeholder-deltas.md` (already added to `SKILL.md` as an optional, ranked input) so post-issuance buyer preferences can be checked against with a declared provenance source instead of being fabricated or missed entirely.

---

## 3. File map

```
eval/airport-eye/client-gap-eval/
├── README.md                                   ← this scoreboard
├── client-gaps-inventory.md                    ← 46 client gaps (gold)
├── skill-derived-gaps.md                       ← 13 skill gaps (genuinely blind)
├── client-vs-skill-eval.md                     ← per-gap match table + interpretation
├── skill-derived-gaps-ASSISTED-CONTAMINATED.md ← archived prior (non-blind) run, 78 gaps
└── client-vs-skill-eval-ASSISTED-CONTAMINATED.md ← archived prior (non-blind) match table
```

**End of scoreboard.**
