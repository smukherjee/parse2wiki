# Client-Gap vs. Skill-Gap Eval — Airport Eye (APOC Phase 2) — Corrected, Genuinely Blind

**Eval date:** 23-July-2026.
**Supersedes:** a prior "eval" of the same name whose underlying skill run was contaminated (25/78 rows cited the client gap document directly, despite being labeled "blind"). That file is preserved at `client-vs-skill-eval-ASSISTED-CONTAMINATED.md`. This file scores the genuinely blind run in `skill-derived-gaps.md` (13 gaps, S-001..S-013) against the same 46-item gold set in `client-gaps-inventory.md`.

---

## Headline metrics

| Metric | Value | Basis |
|---|---|---|
| Gold (client gaps) | 46 | C-001..C-046 |
| Predicted (skill gaps, blind) | 13 | S-001..S-013 |
| Matched client gaps (TP, recall basis) | 3 | C-009 (weak), C-011 (strong), C-037 (weak) |
| Matched skill gaps (TP, precision basis) | 7 | S-001–S-006 (→C-011), S-013 (→C-009, C-037) |
| **Recall** | **0.065** (3/46) | |
| **Precision** | **0.538** (7/13) | |
| **F1** | **0.116** | |

This is a sharp reversal from the contaminated run's false 1.000/0.769/0.870. See **Interpretation** below for why — the low recall is not a skill defect, it's the expected result of genuine blindness against this particular gold set.

---

## 1. Per-client-gap match table (all 46)

| id | category | gap_text (short) | match | matched skill gap(s) | rationale |
|---|---|---|---|---|---|
| C-001 | survey | LiDAR accuracy 5/3cm vs 10/20cm | No | — | Not a source-vs-proposal deviation the blind run surfaced; skill's only survey finding (S-007) is about buffer-zone point density, a different metric. |
| C-002 | survey | Orthophoto/DTM/DSM spec deviation | No | — | Not surfaced. |
| C-003 | platform | Mobile/offline enablement | No | — | Not surfaced. |
| C-004 | commercial_aero | DIAL use-case→KPI→dashboard mapping | No | — | Not surfaced. |
| C-005 | dashboard | Leadership reporting dashboards | No | — | Not surfaced. |
| C-006 | integration | T2 OT (FAS) exclusion must be removed | No (adjacent) | S-009 (weak analogue) | S-009 flags different undisclosed carve-outs (MEP LOD-350, IT assets >3000, counter/gate assets), not T2/FAS specifically. |
| C-007 | racing | WAISL full A+R for OneAPOC/Phase-2 | No | — | Not surfaced; S-010 discusses the CIO Scope Review's authority over APOC/Phase-2 integration but not the accountability assignment itself. |
| C-008 | platform | DT visibility on end-user machines | No | — | Not surfaced. |
| C-009 | asset_registry | Complete asset registry (CLG, CAI, hierarchy, parent-child, location, traceability) | **Weak** | S-013 | S-013 (Step 6a advisory) flags the *absence of a canonical cross-domain identifier scheme*, one slice of C-009's much broader ask (full hierarchy/taxonomy/ontology/traceability). Partial credit only. |
| C-010 | racing | WAISL R+A for IT infra provisioning | No | — | Not surfaced. |
| C-011 | ai | All 8 AI Agents must be explicitly detailed | **Yes** | S-001, S-002, S-003, S-004, S-005, S-006 | Direct hit. The blind run independently found the AI-agent catalogue incomplete/undisclosed from six angles (missing rows, unverifiable citations, undisclosed Stage-2/conditional/regulatory caveats) — the strongest match in the set. |
| C-012 | ai | AI modelling: system stress / partial failure / degradation | No | — | Not surfaced. |
| C-013 | integration | OT data point count: 5L+ vs 2L+ | No | — | Not surfaced. |
| C-014 | platform | Google Maps/Earth D+1 change detection | No | — | Not surfaced. |
| C-015 | security | DIAL IT Security Policy compliance | No | — | Not surfaced — and structurally can't be: "DIAL IT Security Policy" is not named in the CR/RFP/Register at all (S-008 instead flags the CR's own TLS/AES/RBAC specs going unconfirmed, a different document). |
| C-016 | sla | Platform availability 99.9% vs 99.5% | No | — | Not surfaced. |
| C-017 | asset_registry | Pax-journey IT/OT hardware mapping | No | — | Not surfaced. |
| C-018 | integration | CCTV/video analytics/IT in pax journey | No | — | Not surfaced. |
| C-019 | integration | Barcode/e-gate/CUSS/CUPPS/DFMD/ATRS/baggage/boarding scanners | No | — | Not surfaced. |
| C-020 | platform | Medallion Lakehouse walkthrough for DIAL | No | — | Not surfaced. |
| C-021 | integration | ITBMS/JCI/Honeywell integration approach | No | — | Not surfaced. |
| C-022 | racing | Risk register elaboration | No | — | Not surfaced. |
| C-023 | racing | RACI revised: WAISL as A/R (planning, surveys, platform, AI, ops) | **Conflict, not a match** | S-012 | See Interpretation §2 — S-012 flags the proposal's RACI reversal (Vendor Responsible vs. CR's DIAL-Responsible) as a *Fail* (deviation from binding CR). C-023 asks for exactly this kind of reversal. The client's own preference contradicts the formal source the blind skill is bound to. |
| C-024 | sim | Simulation engine architecture detail | No | — | Not surfaced. |
| C-025 | sim | Commercial simulation use cases | No | — | Not surfaced. |
| C-026 | sim | Operational simulation use cases | No | — | Not surfaced. |
| C-027 | integration | APOC integration (control + monitoring) | No | — | Not surfaced; S-010 mentions APOC/Phase-2 as one of several scope items authorized via the CIO meeting, but not this specific control-rights gap. |
| C-028 | integration | APOC lights ON/OFF control | No | — | Not surfaced. |
| C-029 | training | Training & adoption plan | No | — | Not surfaced. |
| C-030 | exclusion | Exclusions must be accepted by named business owners | No (adjacent) | S-009 (weak analogue) | S-009 flags undisclosed carve-outs existing at all; C-030 asks for a sign-off *process* on whatever exclusions exist — different ask. |
| C-031 | environmental | Borewell recharge monitoring (should be base scope) | No | — | Not surfaced. |
| C-032 | environmental | Stormwater analysis data feed | No | — | Not surfaced. |
| C-033 | racing | WAISL R+A for DIAL vendor/OEM coordination | No | — | Not surfaced. |
| C-034 | racing | WAISL R+A for AEP/access coordination | No | — | Not surfaced. |
| C-035 | dt | "Generic Digital framework" aspiration undocumented | No | — | Not surfaced. |
| C-036 | bim | IFC repository architecture/storage/governance/ownership | No (adjacent) | S-013 (weak analogue) | Same identifier-governance theme as S-013 but a different, broader ask (repository/storage strategy, not just ID mapping). |
| C-037 | asset_registry | IFC GUID ↔ CAI ↔ CLG ↔ SAP ↔ OT/BMS mapping | **Weak** | S-013 | S-013's cross-domain identifier finding is the closest of the 13 to this specific mapping ask, but S-013 is scoped as a generic architecture-completeness probe, not this exact five-way mapping. Partial credit only. |
| C-038 | asset_registry | Airport Asset Information Model (AIM) | No (adjacent) | S-013 (weak analogue) | Same theme, broader ask. |
| C-039 | asset_registry | Ontology & relationship model (terminal/floor/space/system/equip/sensor) | No (adjacent) | S-013 (weak analogue) | Same theme, broader ask. |
| C-040 | bim | BIM lifecycle management (version control, as-built, sync w/ DT) | No | — | Not surfaced. |
| C-041 | bim | BIM-GIS federation rules/georeferencing | No | — | Not surfaced. |
| C-042 | ai | AI access pattern to BIM/IFC data | No | — | Not surfaced. |
| C-043 | bim | Open BIM standards (IFC 4.3, bSDD) mandate | No | — | Not surfaced. |
| C-044 | bim | End-to-end digital thread (BIM↔GIS↔SAP↔BMS↔IoT↔APOC↔AI) | No (adjacent) | S-013 (weak analogue) | S-013 covers one node of this thread (identifiers); C-044's ask is the whole thread. |
| C-045 | bim | Add RTM section "BIM IFC Data Architecture" | No | — | Not surfaced — a documentation-structure ask, not a source-vs-proposal deviation. |
| C-046 | bim | Long-term BIM governance (ownership, metadata, mapping) | No | — | Not surfaced. |

---

## 2. Interpretation — why recall is 0.065, not 1.000

The corrected result is not a skill regression; it is what genuine blindness against this gold set was always going to produce, and it validates a design decision made earlier in this engagement.

**Most client gaps are not derivable from the formal source documents at all.** Of the 43 unmatched gaps, the large majority (C-001–C-008, C-010, C-012–C-022, C-024–C-035, C-036/C-038/C-039/C-040/C-041/C-042/C-043/C-044/C-045/C-046) assert numeric thresholds, ownership assignments, or architectural mandates that simply are not written into the CR, ABR, RFP, or Requirements Register — the only documents a blind, source-bound run is permitted to cite. Examples:
- C-001/C-002/C-016 assert specific numeric targets (5cm/3cm RMSE, 99.9% availability) tighter than what's in the BRD — the client is tightening their own requirement post-issuance, not pointing at a documented figure the proposal missed.
- C-007/C-010/C-023/C-033/C-034 assert an accountability model (WAISL as A+R across most domains) that is *not* what the CR's own RACI matrix says — these are the client's post-review preference, in at least one case (C-023, see below) directly contradicting the binding CR.
- C-015 names a "DIAL IT Security Policy" that isn't referenced anywhere in the CR/RFP/Register — a blind run has no source to cite it against.
- The BIM/IFC cluster (C-036–C-046) asks for an architecture (IFC repository governance, digital thread, ontology, lifecycle management) that goes well beyond what the source documents specify; the skill's Step 6a advisory heuristic (S-013) catches a sliver of this (identifier governance) precisely because it's a generic completeness probe, not a source-citation check — everything else in that cluster has no source anchor at all.

**A genuinely blind, source-bound compliance check is structurally incapable of surfacing this class of gap**, because by definition it can only fail/partial/flag a proposal against something a declared source document says. These 43 items are the client's own expectations, formed after reading the proposal, that were never written into the CR/ABR/RFP/Register in the first place.

**This is exactly why the `stakeholder-deltas.md` input tier (enhancement #1, already added to SKILL.md) exists.** It is the only mechanism that could let the skill legitimately surface this class of finding — by giving it a *declared*, ranked input capturing post-issuance buyer communications/reviews, so the skill can still cite a provenance source rather than fabricating one. Without that input present, the correct behavior for a blind run is exactly what happened here: silence on these 43 items, not false positives.

**One finding (C-023) surfaces a genuine conflict, not just a gap.** The client's gap list demands WAISL (vendor) be made Accountable+Responsible for RACI rows that the CR's own §5.3 RACI matrix assigns to DIAL — and the skill's blind run (S-012) independently flagged the proposal's *already-reversed* RACI (Vendor Responsible, DIAL only Accountable) as a compliance **Fail** against that same CR. In other words: the client's post-hoc preference and the CR's binding text point in opposite directions on this exact row, and the proposal sided with the client's (undeclared) preference over the CR's binding text. A blind, source-only check correctly flags this as a deviation from the binding source — it cannot know the client would prefer the deviation. This is a second concrete illustration of the stakeholder-delta gap: without a declared input for it, the skill will keep flagging buyer-desired deviations as Fails.

**The 6 unmatched skill-only findings (S-007–S-011, plus S-012's Fail-vs-preference conflict) remain real, source-binding findings** — commercial "TBC" pricing (S-011), a firm point-density figure reframed as negotiable (S-007), unconfirmed security specs (S-008), undisclosed scope carve-outs (S-009), an unverifiable out-of-band authority citation (S-010), and the RACI reversal (S-012) — none overlap the client's list, meaning they are genuine additive finds a client review didn't catch, not over-claims.

---

## 3. Recommended follow-up

- Treat this eval's low recall as confirmation, not alarm — do not "tune" the skill's source-bound behavior to chase these 43 items; that would mean fabricating provenance.
- If DIAL wants the skill to catch WAISL-preference-class gaps (accountability reassignment, tightened numeric targets, named-but-undocumented policies, BIM/IFC architecture depth) going forward, supply a `stakeholder-deltas.md` input capturing the post-review client communication — the skill will then have a legitimate source to cite these against.
- Flag C-023 vs. S-012 to the deal team explicitly: the CR's binding RACI and the client's stated preference disagree on this exact row, and the current proposal has silently sided with the preference. This needs a human decision (formal CR amendment, or explicit deviation acceptance), not a skill fix.

**End of corrected client-vs-skill eval.**
