# Compliance Report — Airport Eye (APOC Phase 2) Proposal DRAFT

**Subject under validation:** `sources/Airport Eye/AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`

**Validated against (authoritative, in priority order):**
1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` — CR/BRD v1.5 (DIAL-AE-BRD-001, 05-June-2026)
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` — ABR
3. `PE_OT System_09.06.pptx.md` — PE_OT final OT-systems list

**Cross-check artefact:** `sources/Airport Eye/AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`

**Document hierarchy:** CR/BRD + ABR **override** the RFP. The proposal acknowledges this hierarchy at line 89. All numeric comparisons below use the CR/BRD v1.5 as the binding bar unless the ABR adds a stricter or additional requirement.

**Validation method used:**
- Categorical requirement extraction from CR/BRD + ABR
- Numeric/quantitative requirements inventory (see `compliance-report-numeric-inventory.md`)
- Parity/delta check: proposal value vs binding value
- Deviation-register completeness audit
- Semantic carve-out detection on "Compliant" rows
- Multi-artefact reconciliation: proposal vs RTM
- Adversarial critic pass

**Date:** 2026-07-17

---

## Executive summary

The proposal addresses most high-level topics but contains **material numeric and scope shortfalls** against the binding CR/BRD v1.5. A presence-based check would mark many sections "addressed"; a parity check shows the proposal frequently commits to weaker values, omits mandatory deliverables, or narrows the BRD obligation through parenthetical carve-outs.

**Result:** the validation surfaces three known gap classes from earlier manual passes (AI-agent inventory, survey/accuracy, SLA carve-outs) plus **one additional concern** not prominent in the original report: a data-sovereignty / data-retention / O&M-renewal carve-out that makes long-term retention and cross-border rules "to be agreed at renewal," weakening the BRD's "all data remains in India" and 5-year retention commitments.

**Counts (numeric parity + deviation register + carve-out checks):**

| Verdict | Count | Note |
|---|---|---|
| Pass | 17 | Proposal meets or exceeds binding value |
| Partial | 11 | Addressed but weaker, declared deviation needing acceptance, or carve-out detected |
| Fail (gap) | 14 | Undeclared shortfall or missing target |
| Ambiguous | 2 | Status word without measurable figure, or interpretation-dependent (N-AIR-11, N-AI-23) |
| **Blocking** | **10** | Items requiring DIAL written acceptance or correction before the proposal can be called compliant |

*Counts cover the 42 comparable numeric/quantitative and categorical requirements evaluated in the parity tables below. Submission-format and procedural requirements are outside the current DRAFT scope.*

---

## Blocking issues

The following 10 items are **blocking**. Do not assemble the proposal until they are resolved or DIAL has accepted the relevant deviations in writing.

| # | Blocking issue | BRD target | Proposal position | Why blocking |
|---|---|---|---|---|
| B-01 | Vertical RMSE | ≤ 3 cm | ≤ 20 cm (Deviation 1) | 6.7× worse than BRD; needs DIAL acceptance |
| B-02 | Horizontal RMSE | ≤ 5 cm | ≤ 10 cm (Deviation 1) | 2× worse than BRD; needs DIAL acceptance |
| B-03 | Incident response (critical) | ≤ 10 min | ≤ 30 min (Deviation 2) | 3× slower than BRD; needs DIAL acceptance |
| B-04 | DTM/DSM grid | 10 cm | 50 cm | Undeclared 5× coarsening |
| B-05 | Orthophoto GSD | ≤ 5 cm | ≤ 10 cm | Undeclared 2× coarsening |
| B-06 | Contour interval | 10 cm | not mentioned | Undeclared missing deliverable |
| B-07 | Indoor positional RMSE | ≤ 5 cm | not restated | Undeclared missing target |
| B-08 | Mandatory AI agents | 8 | 3 itemised | Six mandatory agents missing from proposal |
| B-09 | Per-agent performance targets | 7 predictive agents | 2 agents with targets | Five agents' SLA targets not offered |
| B-10 | KPI 4 over-claim | ≥ 80% precision / ≥ 75% recall per aggregate and per-agent | "Compliant" for all | Unsubstantiated status word; only 2 of 7 agents have targets |

---

## Validation scope and method

### Categorical requirements (Step 1)

All explicit content and substantive requirements from the CR/BRD and ABR were extracted and checked against the proposal. Submission-format and procedural requirements are outside the current DRAFT validation because the document is a technical draft, not a formatted submission. Coverage of mandatory topics is reported in the per-domain tables below.

*Input note:* the standard skill inputs `sections/[section]-reviewed.md`, `brief.md`, and `coverage-matrix.md` were not present in this working directory, so the validation was run against the raw proposal draft with graceful degradation.

### Numeric inventory (Step 2)

Every comparable numeric requirement from CR/BRD §2.3 (KPIs), §3.1 (survey), §3.4 (security/platform), §3.5 (AI agents), §9.9/§9.11 (SLA/penalty/breach), and ABR §4.1 (simulation) was captured. The full inventory is in `compliance-report-numeric-inventory.md`.

### Parity / delta evaluation (Step 4)

For each numeric row, the proposal's value was compared to the binding value. Ratios/deltas are reported to make severity visible (e.g., vertical RMSE 6.7× worse than BRD).

### Carve-out and over-claim detection (Step 5)

All "Compliant" status entries in the proposal's SLA table were read for parenthetical weakening. Three rows were downgraded to **Partial**. KPI 4 "Compliant" was downgraded to **Partial / Over-claim** because only 2 of 7 predictive agents have substantiated targets.

### Multi-artefact reconciliation (Step 8)

The proposal was reconciled against its own RTM DRAFT. Key inconsistencies are in §6 below.

### Adversarial critic pass (Step 10)

A second pass over the proposal and numeric inventory confirmed the 10 blocking issues and surfaced the 15-year O&M-renewal risk described in §7.

---

## Numeric parity evaluation by domain

### AI agent estate

| Req ID | Parameter | Binding value | Proposal value | Ratio | Declared in deviation register? | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| N-AI-01 | Mandatory domain agents | 8 (Mechanical, Electrical, Fire, Water, Energy, Passenger Flow, Structural, Security) | 3 itemised (Mechanical & HVAC, Passenger Flow, NLP query agent) | 37.5% | n/a | **Fail** | Proposal lines 500–503. BRD §3.5.3 lines 441–448. |
| N-AI-02–04 | Mechanical & HVAC targets | ≥ 82% / ≥ 78% / ≤ 72 h / ≤ 30 s | Same | — | n/a | Pass | Proposal line 511. |
| N-AI-05–07 | Electrical Systems targets | ≥ 80% / ≥ 75% / ≤ 48 h / ≤ 30 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-08–10 | Passenger Flow targets | ≥ 85% / ≥ 80% / ≤ 45 min / ≤ 15 s | Same | — | n/a | Pass | Proposal line 512. |
| N-AI-11–13 | Structural Integrity targets | ≥ 90% / ≥ 85% / ≤ 7 d / ≤ 60 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-14–16 | Fire Safety targets | ≥ 95% / ≥ 95% / real-time / ≤ 5 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-17–19 | Energy Management targets | ≥ 80% / ≥ 75% / ≤ 24 h / ≤ 60 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-20–22 | Security targets | ≥ 88% / ≥ 82% / real-time · 15 min / ≤ 10 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-23 | Aggregate predictive alert accuracy | ≥ 80% precision / ≥ 75% recall | "Per-agent standards, each at or above the BRD threshold — Compliant" | — | n/a | **Over-claim / Partial** | Proposal line 988. Only 2 of 7 predictive agents have per-agent targets in the proposal. |

**Net AI-agent result:** 6 of 8 mandatory agents are missing from the proposal's technical narrative. Only 2 of 7 predictive agents have per-agent SLA targets stated. KPI 4 "Compliant" is an unsubstantiated over-claim.

### Survey and geospatial accuracy

| Req ID | Parameter | Binding value | Proposal value | Ratio | Declared in deviation register? | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| N-AIR-01 | Point density (boundary) | ≥ 20 pts/m² | ≥ 20 pts/m² | 1.0× | n/a | Pass | Proposal lines 147, 210. |
| N-AIR-02 | Point density (buffer) | ≥ 8 pts/m² | 8 pts/m² | 1.0× | n/a | Pass | Proposal lines 148, 210. |
| N-AIR-03 | Horizontal RMSE | ≤ 5 cm | ≤ 10 cm | 2× worse | **Yes** (Deviation 1) | Partial (declared deviation) | Proposal lines 151, 215, 989. |
| N-AIR-04 | Vertical RMSE | ≤ 3 cm | ≤ 20 cm | **6.7× worse** | **Yes** (Deviation 1) | Partial (declared deviation, **blocking**) | Proposal lines 151, 215, 989. |
| N-AIR-05 | Orthophoto GSD | ≤ 5 cm | ≤ 10 cm | 2× coarser | **No** | **Fail** | Proposal lines 150, 212. |
| N-AIR-06 | DTM/DSM grid | 10 cm | 50 cm | 5× coarser | **No** | **Fail** | Proposal lines 149, 211. |
| N-AIR-07 | Contour interval | 10 cm | Not mentioned | — | **No** | **Fail** | No 10 cm contour commitment in proposal §2.2; 50 cm contours only (line 182). |
| N-AIR-08 | Indoor positional RMSE | ≤ 5 cm | Not restated | — | **No** | **Fail** | Proposal line 237 says "registered to airborne coord system" but does not repeat ≤ 5 cm. |
| N-AIR-09 | Utility scanning methods | GPR + DGPS + GNSS + 12D | GPR only | 1 of 4 methods | **No** | **Partial / Fail** | Proposal line 214 says "GPR-based mapping"; DGPS/GNSS/12D absent. |
| N-AIR-10 | Airside NAVAID layers | AGL, PAPI, DVOR, Signage, RVR, MSSR, AMSR | Not enumerated | — | **No** | **Fail** | NAVAID mentioned only as sensitive data class (line 405), not as survey deliverable. |
| N-AIR-11 | Point cloud format | ASPRS LAS 1.4 | "Classified LAS/LAZ per ASPRS classes" | ambiguous | **No** | **Partial / Ambiguous** | Survey deliverable (line 218) does not explicitly commit to LAS 1.4; LAS 1.4 appears only in architecture section (line 1009). |
| N-AIR-12 | Landside GIS topographic layers | 10-layer catalogue | Not enumerated | — | **No** | **Fail** | Proposal §2.2 does not list the BRD layer catalogue (BRD line 245). |
| N-AIR-13 | 3×3 m spot levels | required | Not mentioned | — | **No** | **Fail** | BRD §3.1.2 line 243 requires spot levels at 3×3 m intervals. |
| N-AIR-14 | DEM | required | Not mentioned | — | **No** | **Fail** | BRD §3.1.2 line 243 requires DEM alongside DTM/DSM. |

**Net survey result:** only point density passes as written. Two deviations are declared (horizontal/vertical RMSE), but vertical is 6.7× worse and is the most consequential downstream. Four additional accuracy/resolution shortfalls are **undeclared** (orthophoto GSD, DTM/DSM, contours, indoor RMSE), and four survey-scope items are missing or not enumerated (DGPS/GNSS/12D, NAVAID layers, landside GIS catalogue, DEM/spot levels).

### SLA / KPIs

| Req ID | Parameter | Binding value | Proposal value | Ratio | Declared in deviation register? | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| N-SLA-01 | Platform uptime | ≥ 99.5% excl. planned maintenance | ≥ 99.5% excl. planned maintenance **and Excluded Events** | widened exclusion | **No** | **Partial / carve-out** | Proposal lines 985, 917, 995. Adds force majeure, DIAL/sub-vendor, third-party feed/API, and planned maintenance exclusions. |
| N-SLA-02 | Data latency | ≤ 5 s sensor → dashboard | ≤ 5 s "measured at the platform boundary" | narrowed scope | **No** | **Partial / carve-out** | Proposal lines 985, 291–292. Source-side polling/publication latency excluded. |
| N-SLA-03 | BIM LOD compliance | 100% at agreed LOD | 100% at agreed LOD | 1.0× | n/a | Pass | Proposal line 986. |
| N-SLA-04 | Incident response (critical) | ≤ 10 min from notification | ≤ 30 min from notification | 3× slower | **Yes** (Deviation 2) | Partial (declared deviation, **blocking**) | Proposal lines 990, 931. |
| N-SLA-05 | Integration coverage | 100% of agreed points within 3 months | 100% of agreed **baseline** within 3 months | narrowed scope | **No** | **Partial / carve-out** | Proposal lines 991, 993. Baseline excludes not-present / not-commissioned / not-exposed points at freeze time. |
| N-SLA-06 | Breach notification | ≤ 12 h for any incident | 2 h for CERT-In-reportable incidents; no blanket 12 h stated | mixed | **No** | **Partial / Fail** | Proposal line 425. Better for CERT-In, but BRD §9.11 line 699 covers *any* incident. |
| N-SLA-07 | Penalty / material default | ≥ 3 breaches/quarter | ≥ 3 breaches/quarter accepted in principle | 1.0× | n/a | Pass (mechanism) | Proposal lines 1001–1003. Contention is liability cap and Excluded Events. |

**Net SLA result:** only KPI 3 fully passes. Two declared deviations (KPI 5 geospatial accuracy, KPI 6 response time). Three KPIs carry **undeclared carve-outs** that narrow the BRD commitment (KPI 1 uptime exclusions, KPI 2 latency measurement point, KPI 7 baseline freeze). Breach-notification is partially better but does not restate the universal 12-hour obligation.

### Platform architecture, security, and NFRs

| Req ID | Parameter | Binding value | Proposal value | Ratio / status | Verdict | Evidence |
|---|---|---|---|---|---|---|
| N-SEC-01 | User roles | ≥ 5 | 5 default + additional AOCC/P&E/etc. | exceeds | Pass | Proposal line 343; RTM ROW-943. |
| N-SEC-02 | TLS in transit | TLS 1.3 | TLS 1.3 minimum | 1.0× | Pass | Proposal line 398. |
| N-SEC-03 | AES-256 at rest | required | AES-256 | 1.0× | Pass | Proposal line 399. |
| N-SEC-04 | Audit log retention | ≥ 2 years | ≥ 5 years | 2.5× longer | Pass | Proposal line 411. |
| N-SEC-05 | Historical BMS data retention | ≥ 5 years | ≥ 5 years | 1.0× | Pass | Proposal line 960; CR/BRD §3.4.2 line 414. |
| N-SEC-06 | AI audit log retention | ≥ 5 years | ≥ 5 years | 1.0× | Pass | Proposal line 534; CR/BRD §3.5.5 line 465. |
| N-PLAT-01 | 15-year operational design life | ≥ 15 years | 15-year architecture; 5-year O&M renewable | conditional risk | Partial | Proposal lines 1009–1011. Architecture is 15-year but O&M renewal terms "agreed at renewal" could break continuity. |
| N-PLAT-02 | RTO | ≤ 4 h | < 4 h | favourable | Pass | Proposal line 938. |
| N-PLAT-03 | RPO | ≤ 24 h (RTM) | < 1 h | 24× better | Pass | Proposal line 938; RTM ROW-964. |
| N-ABR-01 | Simulation-engine components | 4 | 4 | 1.0× | Pass | Proposal lines 550–557; ABR §4.1 lines 67–73. |
| N-ABR-02 | IoT machine-room pumps | 40 | 40 | 1.0× | Pass | Proposal line 263; CR/BRD line 379. |
| N-ABR-03 | T1 roof sensors | 12 | 12 | 1.0× | Pass | Proposal line 263; CR/BRD line 380. |

**Net NFR result:** most security and architecture items pass. The 15-year lifecycle is structurally sound but carries a renewal-pricing risk because the 5-year O&M term is renewable "on terms agreed at renewal."

---

## Deviation-register completeness audit

The proposal's deviation/compliance register is at lines 984–991 and related text at lines 993–997. It explicitly declares only **two** deviations:
- **Deviation 1:** KPI 5 geospatial accuracy (≤ 10 cm H / ≤ 20 cm V vs BRD ≤ 5 cm / ≤ 3 cm)
- **Deviation 2:** KPI 6 incident response (≤ 30 min vs BRD ≤ 10 min)

The following shortfalls or carve-outs are **not** in the register:

| # | Shortfall / carve-out | BRD target | Proposal commitment | Why it should be in the register |
|---|---|---|---|---|
| DRA-01 | Orthophoto GSD | ≤ 5 cm | ≤ 10 cm | 2× coarser than BRD; in scope table at lines 150, 212 |
| DRA-02 | DTM/DSM grid | 10 cm | 50 cm | 5× coarser; in scope table at lines 149, 211 |
| DRA-03 | Contour interval | 10 cm | not mentioned | Deliverable absent or weaker |
| DRA-04 | Indoor positional RMSE | ≤ 5 cm | not restated | BRD §3.1.5 line 259 not mirrored |
| DRA-05 | Underground utility methods | GPR + DGPS + GNSS + 12D | GPR only | Missing positioning methods and drainage model |
| DRA-06 | Airside NAVAID GIS layers | enumerated set | not enumerated | BRD §3.1.3 line 250 deliverable missing |
| DRA-07 | Landside GIS topographic catalogue | 10-layer set | not enumerated | BRD §3.1.2 line 245 deliverable missing |
| DRA-08 | Landside DEM / 3×3 m spot levels | required | not mentioned | BRD §3.1.2 line 243 deliverables missing |
| DRA-09 | Six missing mandatory AI agents | 8 agents | 3 itemised | Agent inventory shortfall |
| DRA-10 | Five missing per-agent performance target sets | 7 predictive agents with targets | 2 agents with targets | KPI 4 over-claim root cause |
| DRA-11 | KPI 1 uptime exclusions | planned maintenance only | + Excluded Events | Widens exclusion set |
| DRA-12 | KPI 2 latency measurement point | sensor-to-dashboard | platform boundary | Narrows measurement scope |
| DRA-13 | KPI 7 integration baseline | 100% of agreed points | 100% of baseline, subject to freeze | Narrows coverage scope |
| DRA-14 | Breach notification (non-CERT-In) | ≤ 12 h any incident | 2 h only for CERT-In-reportable | Universal obligation not restated |
| DRA-15 | Data retention / sovereignty on renewal | in-India, 5-year minima | "renewal terms agreed" | Could reopen retention and cross-border rules |

**Finding:** the proposal's deviation register captures only 2 of at least 15 material shortfalls or carve-outs against the BRD. A presence-based checker sees "deviations declared" and stops; a completeness audit finds the register is under-populated by a factor of ~7.

---

## Semantic carve-out detection

Rows in the proposal's SLA table that are marked **Compliant** but contain weakening language:

| KPI | Proposal status | Commitment text | Carve-out detected | Verdict |
|---|---|---|---|---|
| 1 Platform Uptime | Compliant | "≥ 99.5%, excluding planned maintenance **and Excluded Events**" | Adds force majeure, DIAL/third-party-caused outage, third-party feed/API unavailability | **Partial** |
| 2 Data Latency | Compliant | "≤ 5 s, sensor to dashboard, **measured at the platform boundary**" | Excludes source-side polling/publication latency | **Partial** |
| 7 Integration Coverage | Compliant, **subject to baseline confirmation** | "100% of the agreed data-point baseline within 3 months" | Baseline freeze excludes not-present/not-commissioned points | **Partial** |

Rows marked **Compliant** but unsubstantiated:

| KPI | Claim | Evidence gap | Verdict |
|---|---|---|---|
| 4 Predictive Alert Accuracy | "Per-agent standards, each at or above the BRD threshold — Compliant" | Only 2 of 7 predictive agents have targets in the proposal. | **Over-claim / Partial** |

---

## Multi-artefact reconciliation: proposal vs RTM

The RTM is complete on agents and per-agent ownership; the proposal is not. Where the proposal claims alignment with its own RTM, the following inconsistencies appear:

| Topic | RTM position | Proposal position | Verdict |
|---|---|---|---|
| AI agent count | 8 mandatory + 1 NLP (AI-08…AI-16 + AI-10) = 9 rows | 3 itemised in §3.2 technical table | **Fail — proposal does not match its own RTM** |
| Per-agent performance targets | RTM ROW-933 references Sec 6.5 / BRD §3.5.4 targets for all agents | Only Mechanical & HVAC and Passenger Flow targets stated | **Fail — proposal does not match RTM/BRD** |
| OT integration estate | RTM covers 15 PE_OT families + ITBMS/Noise | Proposal §2.5 covers the same families and counts | Pass |
| 15-year lifecycle | RTM has no explicit 15-year design-life row (original B7 gap) | Proposal architecture states 15-year lifecycle (line 1009) | Partially addresses RTM gap but O&M term is 5-year renewable |
| TLS | RTM ROW-946 says TLS 1.2+ | Proposal says TLS 1.3 minimum | Pass — proposal is stricter than RTM and matches BRD |

**Note on proposal structure:** the DRAFT proposal does not contain a separate commercial-costing table. Its technical narrative (§3.2, lines 500–503) commits only 3 agents, while the BRD §3.5.3 requires 8 and the RTM traces 9 rows (AI-08…AI-16 + AI-10). The agent gap is therefore an external shortfall against the BRD/RTM, not an internal inconsistency within the proposal.

---

## New issue: 15-year lifecycle / O&M renewal carve-out

The original manual passes focused on the RTM and then added three adversarial passes on the proposal. Running the improved logic from the start against the proposal surfaces one additional concern:

- **BRD Objective 6 (line 202):** platform designed for minimum 15-year operational lifecycle.
- **Proposal line 1009:** architecture is 15-year / open-standards.
- **Proposal lines 1010–1011:** O&M is a 5-year term "renewable for two further five-year terms at DIAL's option on **terms agreed at renewal**"; data retention commitments are stated as five-year minima within the contracted term and extended on renewal.

This is not a deviation in the technical sense, but it is a **conditional risk:** the 15-year design-life commitment is not matched by pre-agreed O&M pricing/mechanism for the second and third 5-year terms. If renewal terms are not pre-agreed, SLA continuity, data-retention, and data-sovereignty commitments could be renegotiated at each renewal boundary, effectively reopening the BRD's "all data remains in India" and 5-year retention commitments.

**Remediation:** pre-agree the 5-year renewal pricing and mechanism, or state that renewal pricing is capped/indexed in the contract so the 15-year commitment is not reopened. Add this as Deviation/Risk DRA-15 in the register.

---

## Page count / section-size note

The DRAFT proposal is `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`, extracted as **1,089 lines** of markdown. No page limits, font, margin, or file-format requirements were found in the CR/BRD or ABR for this technical draft. 

Estimated formatted length: approximately **35–45 pages** in a standard Word layout (depending on tables, diagrams, and white space). No section is flagged as at risk of a page limit because **no page limits are specified**.

---

## Remediation instructions (ordered)

### Must do before submission

1. **Resolve Deviation 1:** either commit to BRD ≤ 5 cm H / ≤ 3 cm V RMSE, or obtain DIAL's written acceptance of ≤ 10 cm / ≤ 20 cm before submission.
2. **Resolve Deviation 2:** either commit to BRD ≤ 10 min critical incident response, or obtain DIAL's written acceptance of ≤ 30 min.
3. **Add DRA-01 to DRA-04 to the deviation register or correct the proposal:** DTM/DSM 50 cm, orthophoto ≤ 10 cm, 10 cm contours, indoor ≤ 5 cm RMSE must either be corrected to BRD values or declared as deviations with rationale.
4. **Add missing survey methods and deliverables:** DGPS, GNSS, 12D drainage model, NAVAID GIS layers, landside GIS catalogue, DEM, 3×3 m spot levels.
5. **Add the missing AI agents:** expand the proposal §3.2 "Domain AI agents" table to include all 8 mandatory agents required by BRD §3.5.3, plus the NLP query agent as an additive capability.
6. **Add per-agent performance targets:** add the five missing target rows (Electrical, Structural, Fire Safety, Energy Management, Security) with BRD §3.5.4 values.
7. **Fix KPI 4 claim:** reword to "Compliant for Mechanical & HVAC and Passenger Flow; remaining agents baselined per AI-01 Data Readiness Gate and accepted on rolling 90-day window," or add all per-agent targets.
8. **Declare KPI 1/2/7 carve-outs as deviations** or align wording to BRD (planned-maintenance-only uptime exclusion, true sensor-to-dashboard latency, 100% of agreed points unconditionally).
9. **Restate breach-notification rule:** add "all non-CERT-In cybersecurity incidents notified to DIAL within 12 hours of detection" alongside the 2-hour CERT-In commitment.

### Should do

10. **Pre-agree 5-year O&M renewal pricing/mechanism** to remove the 15-year lifecycle continuity risk (DRA-15).
11. **State LAS 1.4 explicitly** in the D-02 deliverable spec, not only in the architecture section.
12. **Add the missing protocols to the proposal's protocol inventory** if MQTT/SNMP are not explicitly committed in all tables (they are mentioned at line 288).
13. **Add DGA, cityside IoT, mobile app, AR/VR, CCC, PSIM, SIEM, pen-test, 15-year lifecycle** as explicit deliverable/scope items where the RTM has gaps; the proposal partially addresses some but should cross-reference them.

---

## Pre-flight verdict

**NOT READY for assembly.** The compliance validation confirms three known gap classes (AI-agent inventory, survey/accuracy shortfalls, SLA carve-outs) and adds one new concern (15-year O&M-renewal / data-retention conditional risk). The proposal's deviation register is materially under-populated: it declares 2 deviations while at least 15 material shortfalls or carve-outs should appear. Until the **10 blocking items** are resolved or DIAL accepts the declared and undeclared deviations in writing, the proposal is non-compliant with the binding CR/BRD v1.5.

*Grounded only in: CR/BRD v1.5, ABR 2-July-2026, PE_OT 09.06, the Proposal DRAFT, and the RTM DRAFT. No external references used.*
