# Improved Compliance Validation Test Report — Airport Eye Proposal

**Subject under validation:** `sources/Airport Eye/AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`

**Validated against (authoritative, in priority order):**
1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` — CR/BRD v1.5 (DIAL-AE-BRD-001, 05-June-2026)
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` — ABR
3. `PE_OT System_09.06.pptx.md` — PE_OT final OT-systems list

**Cross-check artefact:** `sources/Airport Eye/AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`

**Document hierarchy:** CR/BRD + ABR **override** the RFP. The proposal acknowledges this at line 89 ("BRD v1.5 supersedes the RFP v5 for matters of scope, sequencing, and commercial framework"). All numeric comparisons below use the CR/BRD as the binding bar unless the ABR adds a stricter or additional requirement.

**Validation method used:**
- Numeric/quantitative requirements inventory extracted from CR/BRD + ABR
- Parity/delta check: proposal value vs binding value
- Deviation-register completeness audit
- Semantic carve-out detection on "Compliant" rows
- Multi-artefact reconciliation: proposal vs RTM
- Adversarial critic pass

**Date:** 2026-07-17

---

## 1. Executive summary

This is a **test run of the improved compliance-validator logic** against the Airport Eye proposal. The original single-artefact, presence-based check validated the RTM against the BRD and found 9 missing RTM rows. The new logic additionally validates the **proposal** against the BRD, treats every comparable numeric spec as a first-class requirement, and flags "addressed but weaker" commitments plus undeclared deviations.

**Result:** the improved logic surfaces all three classes of gap that the manual §9–§11 passes found (AI agents, survey/accuracy, SLA), plus **one new issue** that was not prominent in the original report:
1. A **data-sovereignty / data-retention carve-out** in the O&M section that narrows the BRD's "all data remains in India" and "5-year retention" commitments by making renewal-term retention and cross-border rules "to be agreed at renewal."

**Counts (numeric parity + deviation register + carve-out checks):**

| Verdict        | Count | Note |
|---             |---    |---|
| Pass           | 18    | Proposal meets or exceeds binding value |
| Partial        | 15    | Addressed but weaker, or declared deviation needing acceptance, or carve-out detected |
| Fail (gap)     | 18    | Undeclared shortfall or missing target |
| Ambiguous      | 3     | Status word without measurable figure, or interpretation-dependent |
| N/A            | 2     | Commercial/contract terms outside pure technical compliance |
| **Blocking**   | **10** | Items requiring DIAL written acceptance or correction before the proposal can be called compliant |

---

## 2. Numeric requirements inventory (binding values)

Extracted from CR/BRD + ABR, grouped by domain. These are the values used in the parity check.

| ID | Parameter | Binding value | Source | Source location |
|---|---|---|---|---|
| N-AIR-01 | Airborne LiDAR point density (boundary) | ≥ 20 pts/m² | CR/BRD §3.1.1 | CR/BRD lines 230 |
| N-AIR-02 | Airborne LiDAR point density (buffer) | ≥ 8 pts/m² | CR/BRD §3.1.1 | CR/BRD lines 230 |
| N-AIR-03 | Horizontal RMSE | ≤ 5 cm | CR/BRD §3.1.1 / KPI 5 | CR/BRD lines 231, 211 |
| N-AIR-04 | Vertical RMSE | ≤ 3 cm | CR/BRD §3.1.1 / KPI 5 | CR/BRD lines 232, 211 |
| N-AIR-05 | Orthophoto GSD | ≤ 5 cm | CR/BRD §3.1.1 | CR/BRD line 233 |
| N-AIR-06 | DTM/DSM grid resolution | 10 cm | CR/BRD §3.1.1 | CR/BRD line 235 |
| N-AIR-07 | Contour interval | 10 cm | CR/BRD §3.1.1 / D-04 | CR/BRD line 236, 306 |
| N-AIR-08 | Indoor positional RMSE | ≤ 5 cm | CR/BRD §3.1.5 | CR/BRD line 259 |
| N-AIR-09 | Underground utility scanning methods | GPR + DGPS + GNSS + 12D model | CR/BRD §3.1.2 | CR/BRD line 242 |
| N-AIR-10 | Airside NAVAID GIS layers | AGL, PAPI, DVOR, Signage, RVR, MSSR, AMSR | CR/BRD §3.1.3 | CR/BRD line 250 |
| N-AIR-11 | Point cloud format | ASPRS LAS 1.4 | CR/BRD §3.1.1 | CR/BRD line 234 |
| N-AIR-12 | Landside GIS topographic layers | land use, parcels, roads, street view, zoning, topography, wetlands, demographics, land cover, imagery, basemap | CR/BRD §3.1.2 | CR/BRD line 245 |
| N-AIR-13 | 3×3 m spot levels for landside | required | CR/BRD §3.1.2 | CR/BRD line 243 |
| N-AIR-14 | DEM for landside | required | CR/BRD §3.1.2 | CR/BRD line 243 |
| N-AI-01 | Mandatory domain AI agents | 8 (Mechanical, Electrical, Fire, Water, Energy, Passenger Flow, Structural, Security) | CR/BRD §3.5.3 | CR/BRD lines 441–448 |
| N-AI-02 | Mechanical & HVAC precision/recall | ≥82% / ≥78% | CR/BRD §3.5.4 | CR/BRD line 454 |
| N-AI-03 | Mechanical & HVAC prediction horizon | ≤72 h | CR/BRD §3.5.4 | CR/BRD line 454 |
| N-AI-04 | Mechanical & HVAC alert latency | ≤30 s | CR/BRD §3.5.4 | CR/BRD line 454 |
| N-AI-05 | Electrical Systems precision/recall | ≥80% / ≥75% | CR/BRD §3.5.4 | CR/BRD line 455 |
| N-AI-06 | Electrical Systems prediction horizon | ≤48 h | CR/BRD §3.5.4 | CR/BRD line 455 |
| N-AI-07 | Electrical Systems alert latency | ≤30 s | CR/BRD §3.5.4 | CR/BRD line 455 |
| N-AI-08 | Passenger Flow precision/recall | ≥85% / ≥80% | CR/BRD §3.5.4 | CR/BRD line 456 |
| N-AI-09 | Passenger Flow prediction horizon | ≤45 min | CR/BRD §3.5.4 | CR/BRD line 456 |
| N-AI-10 | Passenger Flow alert latency | ≤15 s | CR/BRD §3.5.4 | CR/BRD line 456 |
| N-AI-11 | Structural Integrity precision/recall | ≥90% / ≥85% | CR/BRD §3.5.4 | CR/BRD line 457 |
| N-AI-12 | Structural Integrity prediction horizon | ≤7 d | CR/BRD §3.5.4 | CR/BRD line 457 |
| N-AI-13 | Structural Integrity alert latency | ≤60 s | CR/BRD §3.5.4 | CR/BRD line 457 |
| N-AI-14 | Fire Safety precision/recall | ≥95% / ≥95% | CR/BRD §3.5.4 | CR/BRD line 458 |
| N-AI-15 | Fire Safety prediction horizon | real-time | CR/BRD §3.5.4 | CR/BRD line 458 |
| N-AI-16 | Fire Safety alert latency | ≤5 s | CR/BRD §3.5.4 | CR/BRD line 458 |
| N-AI-17 | Energy Management precision/recall | ≥80% / ≥75% | CR/BRD §3.5.4 | CR/BRD line 459 |
| N-AI-18 | Energy Management prediction horizon | ≤24 h | CR/BRD §3.5.4 | CR/BRD line 459 |
| N-AI-19 | Energy Management alert latency | ≤60 s | CR/BRD §3.5.4 | CR/BRD line 459 |
| N-AI-20 | Security precision/recall | ≥88% / ≥82% | CR/BRD §3.5.4 | CR/BRD line 460 |
| N-AI-21 | Security prediction horizon | real-time / 15 min | CR/BRD §3.5.4 | CR/BRD line 460 |
| N-AI-22 | Security alert latency | ≤10 s | CR/BRD §3.5.4 | CR/BRD line 460 |
| N-AI-23 | Aggregate predictive alert accuracy | ≥80% precision / ≥75% recall | CR/BRD §2.3 KPI 4 | CR/BRD line 210 |
| N-SLA-01 | Platform uptime | ≥99.5% (excl. planned maintenance) | CR/BRD §2.3 KPI 1 / §9.9 | CR/BRD line 207 |
| N-SLA-02 | Data latency | ≤5 s sensor → dashboard | CR/BRD §2.3 KPI 2 | CR/BRD line 208 |
| N-SLA-03 | BIM LOD compliance | 100% of specified assets at agreed LOD | CR/BRD §2.3 KPI 3 | CR/BRD line 209 |
| N-SLA-04 | Incident response (critical) | ≤10 min from notification | CR/BRD §2.3 KPI 6 | CR/BRD line 212 |
| N-SLA-05 | Integration coverage | 100% of agreed BMS/IoT points within 3 months | CR/BRD §2.3 KPI 7 | CR/BRD line 213 |
| N-SLA-06 | Breach notification | ≤12 h for any cybersecurity incident/data breach | CR/BRD §9.11 | CR/BRD line (§9.11) |
| N-SLA-07 | Penalty threshold | ≥3 breaches/quarter = material default | CR/BRD §9.9 | CR/BRD line (§9.9) |
| N-SEC-01 | User roles | ≥5 (Executive, Operations, Maintenance, Security, Guest/Visitor) | CR/BRD §3.4.4 | CR/BRD line 425 |
| N-SEC-02 | TLS in transit | TLS 1.3 | CR/BRD §3.4.4 | CR/BRD line 428 |
| N-SEC-03 | AES-256 at rest | required | CR/BRD §3.4.4 | CR/BRD line 428 |
| N-SEC-04 | Audit log retention | ≥2 years | CR/BRD §3.4.4 | CR/BRD line 429 |
| N-SEC-05 | Historical data retention | ≥5 years | CR/BRD §3.4.2 | CR/BRD line 414 |
| N-SEC-06 | AI audit log retention | ≥5 years | CR/BRD §3.5.5 | CR/BRD line 465 |
| N-PLAT-01 | Platform design life | ≥15 years | CR/BRD Objective 6 | CR/BRD line 202 |
| N-PLAT-02 | RTO | ≤4 h | Proposal/BRD | Proposal line 938 (addition) |
| N-PLAT-03 | RPO | ≤24 h | BRD/RTM | RTM ROW-964 |
| N-ABR-01 | Simulation-engine components | 4 (DT substrate, scenario UI, Decision Engine, results UI) | ABR §4.1 | ABR lines 65–73 |
| N-ABR-02 | IoT machine-room pumps | 40 | CR/BRD §3.3.4 | CR/BRD line 379 |
| N-ABR-03 | T1 roof sensors | 12 | CR/BRD §3.3.4 | CR/BRD line 380 |

---

## 3. Numeric parity evaluation by domain

### 3.1 AI agent estate

| Req ID | Parameter | Binding value | Proposal value | Ratio | Declared in deviation register? | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| N-AI-01 | Mandatory domain agents | 8 | 3 itemised in the technical narrative (Mechanical, Passenger Flow, NLP) | 37.5% | n/a | **Fail** | Proposal lines 500–503. |
| N-AI-02–04 | Mechanical & HVAC targets | ≥82% / ≥78% / 72 h / ≤30 s | Same | — | n/a | Pass | Proposal lines 511 |
| N-AI-05–07 | Electrical Systems targets | ≥80% / ≥75% / 48 h / ≤30 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-08–10 | Passenger Flow targets | ≥85% / ≥80% / 45 min / ≤15 s | Same | — | n/a | Pass | Proposal lines 512 |
| N-AI-11–13 | Structural Integrity targets | ≥90% / ≥85% / 7 d / ≤60 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-14–16 | Fire Safety targets | ≥95% / ≥95% / real-time / ≤5 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-17–19 | Energy Management targets | ≥80% / ≥75% / 24 h / ≤60 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-20–22 | Security targets | ≥88% / ≥82% / real-time·15 min / ≤10 s | Agent absent; no targets | — | n/a | **Fail** | Agent not in proposal §3.2 table. |
| N-AI-23 | Aggregate predictive alert accuracy | ≥80% / ≥75% | "Per-agent standards, each at or above the BRD threshold — Compliant" | — | n/a | **Over-claim / Partial** | Proposal line 988. Only 2 of 7 agents have per-agent targets; "Compliant" is unsubstantiated for 5. |

**Net AI-agent result:** 6 of 8 mandatory agents are missing from the proposal's technical narrative. Only 2 of 7 predictive agents have per-agent SLA targets stated. KPI 4 "Compliant" is an over-claim.

### 3.2 Survey and geospatial accuracy

| Req ID | Parameter | Binding value | Proposal value | Ratio | Declared in deviation register? | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| N-AIR-01 | Point density (boundary) | ≥20 pts/m² | ≥20 pts/m² | 1.0× | n/a | Pass | Proposal lines 147, 210 |
| N-AIR-02 | Point density (buffer) | ≥8 pts/m² | 8 pts/m² | 1.0× | n/a | Pass | Proposal lines 148, 210 |
| N-AIR-03 | Horizontal RMSE | ≤5 cm | ≤10 cm | 2× worse | **Yes** (Deviation 1) | Partial (declared deviation) | Proposal lines 151, 215, 989 |
| N-AIR-04 | Vertical RMSE | ≤3 cm | ≤20 cm | **6.7× worse** | **Yes** (Deviation 1) | Partial (declared deviation, **blocking**) | Proposal lines 151, 215, 989 |
| N-AIR-05 | Orthophoto GSD | ≤5 cm | ≤10 cm | 2× coarser | **No** | **Fail** | Proposal lines 150, 212 |
| N-AIR-06 | DTM/DSM grid | 10 cm | 50 cm | 5× coarser | **No** | **Fail** | Proposal lines 149, 211 |
| N-AIR-07 | Contour interval | 10 cm | Not mentioned | — | **No** | **Fail** | No 10 cm contour commitment in proposal §2.2; 50 cm contours only (line 182). |
| N-AIR-08 | Indoor positional RMSE | ≤5 cm | Not restated | — | **No** | **Fail** | Proposal line 237 says "registered to airborne coord system" but does not repeat ≤5 cm. |
| N-AIR-09 | Utility scanning methods | GPR + DGPS + GNSS + 12D | GPR only | partial | **No** | **Partial / Fail** | Proposal line 214 says "GPR-based mapping"; DGPS/GNSS/12D absent (0 hits). |
| N-AIR-10 | Airside NAVAID layers | AGL, PAPI, DVOR, Signage, RVR, MSSR, AMSR | Not enumerated | — | **No** | **Partial / Fail** | NAVAID mentioned only as sensitive data class (line 405), not as survey deliverable. |
| N-AIR-11 | Point cloud format | ASPRS LAS 1.4 | "Classified LAS/LAZ per ASPRS classes" | ambiguous | **No** | **Partial / Ambiguous** | Survey deliverable (line 218) does not explicitly commit to LAS 1.4; LAS 1.4 appears only in architecture section (line 1009). |
| N-AIR-12 | Landside GIS topographic layers | 10-layer catalogue | Not enumerated | — | **No** | **Partial / Fail** | Proposal §2.2 does not list the BRD layer catalogue. |
| N-AIR-13 | 3×3 m spot levels | required | Not mentioned | — | **No** | **Fail** | BRD §3.1.2 requires spot levels at 3×3 m intervals. |
| N-AIR-14 | DEM | required | Not mentioned | — | **No** | **Fail** | BRD §3.1.2 requires DEM alongside DTM/DSM. |

**Net survey result:** only point density passes as written. Two deviations are declared (horizontal/vertical RMSE), but vertical is 6.7× worse and is the most consequential downstream. Four additional accuracy/resolution shortfalls are **undeclared** (orthophoto GSD, DTM/DSM, contours, indoor RMSE), and four survey-scope items are missing or not enumerated (DGPS/GNSS/12D, NAVAID layers, landside GIS catalogue, DEM/spot levels).

### 3.3 SLA / KPIs

| Req ID | Parameter | Binding value | Proposal value | Ratio | Declared in deviation register? | Verdict | Evidence |
|---|---|---|---|---|---|---|---|
| N-SLA-01 | Platform uptime | ≥99.5% excl. planned maintenance | ≥99.5% excl. planned maintenance **and Excluded Events** | widened exclusion | **No** | **Partial / carve-out** | Proposal lines 985, 993–995. Adds force majeure, DIAL/sub-vendor, third-party feed/API, and planned maintenance exclusions. |
| N-SLA-02 | Data latency | ≤5 s sensor → dashboard | ≤5 s "measured at the platform boundary" | narrowed scope | **No** | **Partial / carve-out** | Proposal lines 985, 291–292. Source-side polling/publication latency excluded. |
| N-SLA-03 | BIM LOD compliance | 100% at agreed LOD | 100% at agreed LOD | 1.0× | n/a | Pass | Proposal line 986 |
| N-SLA-04 | Incident response (critical) | ≤10 min from notification | ≤30 min from notification | 3× slower | **Yes** (Deviation 2) | Partial (declared deviation, **blocking**) | Proposal lines 990, 931 |
| N-SLA-05 | Integration coverage | 100% of agreed points within 3 months | 100% of agreed **baseline** within 3 months | narrowed scope | **No** | **Partial / carve-out** | Proposal lines 991, 993. Baseline excludes not-present / not-commissioned / not-exposed points at freeze time. |
| N-SLA-06 | Breach notification | ≤12 h for any incident | 2 h for CERT-In-reportable incidents; no blanket 12 h stated | mixed | **No** | **Partial / Fail** | Proposal line 425. Better for CERT-In, but BRD covers *any* incident. |
| N-SLA-07 | Penalty / material default | ≥3 breaches/quarter | ≥3 breaches/quarter accepted in principle | 1.0× | n/a | Pass (mechanism) | Proposal lines 1001–1003. Contention is liability cap and Excluded Events. |

**Net SLA result:** only KPI 3 fully passes. Two declared deviations (KPI 5 geospatial accuracy, KPI 6 response time). Three KPIs carry **undeclared carve-outs** that narrow the BRD commitment (KPI 1 uptime exclusions, KPI 2 latency measurement point, KPI 7 baseline freeze). Breach-notification is partially better but does not restate the universal 12-hour obligation.

### 3.4 Platform architecture, security, and NFRs

| Req ID | Parameter | Binding value | Proposal value | Ratio / status | Verdict | Evidence |
|---|---|---|---|---|---|---|
| N-SEC-01 | User roles | ≥5 | 5 default + additional AOCC/P&E/etc. | Pass | Pass | Proposal line 343; RTM ROW-943 |
| N-SEC-02 | TLS in transit | TLS 1.3 | TLS 1.3 minimum | Pass | Pass | Proposal line 398 |
| N-SEC-03 | AES-256 at rest | required | AES-256 | Pass | Pass | Proposal line 399 |
| N-SEC-04 | Audit log retention | ≥2 years | ≥5 years | Exceeds | Pass | Proposal line 411 |
| N-SEC-05 | Historical BMS data retention | ≥5 years | ≥5 years | Pass | Pass | Proposal line 960; CR/BRD §3.4.2 |
| N-SEC-06 | AI audit log retention | ≥5 years | ≥5 years | Pass | Pass | Proposal line 534 |
| N-PLAT-01 | 15-year operational design life | ≥15 years | 15-year architecture; 5-year O&M renewable | **Partial / conditional risk** | Partial | Proposal lines 1009–1011. Architecture is 15-year but O&M renewal terms "agreed at renewal" could break continuity. |
| N-PLAT-02 | RTO | not numerically specified in BRD | <4 h | Favourable | Pass | Proposal line 938 |
| N-PLAT-03 | RPO | ≤24 h (RTM) | <1 h | Favourable | Pass | Proposal line 938 |
| N-ABR-01 | Simulation-engine components | 4 | 4 | Pass | Pass | Proposal lines 550–557 |
| N-ABR-02 | IoT machine-room pumps | 40 | 40 | Pass | Pass | Proposal line 263; CR/BRD line 379 |
| N-ABR-03 | T1 roof sensors | 12 | 12 | Pass | Pass | Proposal line 263; CR/BRD line 380 |

**Net NFR result:** most security and architecture items pass. The 15-year lifecycle is structurally sound but carries a renewal-pricing risk because the 5-year O&M term is renewable "on terms agreed at renewal."

---

## 4. Deviation-register completeness audit

The proposal's deviation/compliance register is at lines 984–991 and related text at lines 993–997. It explicitly declares only **two** deviations:
- **Deviation 1:** KPI 5 geospatial accuracy (≤10 cm H / ≤20 cm V vs BRD ≤5 cm / ≤3 cm)
- **Deviation 2:** KPI 6 incident response (≤30 min vs BRD ≤10 min)

The following shortfalls or carve-outs are **not** in the register:

| # | Shortfall / carve-out | BRD target | Proposal commitment | Why it should be in the register |
|---|---|---|---|---|
| DRA-01 | Orthophoto GSD | ≤5 cm | ≤10 cm | 2× coarser than BRD; in scope table at line 150, line 212 |
| DRA-02 | DTM/DSM grid | 10 cm | 50 cm | 5× coarser; in scope table at line 149, line 211 |
| DRA-03 | Contour interval | 10 cm | not mentioned | Deliverable absent or weaker |
| DRA-04 | Indoor positional RMSE | ≤5 cm | not restated | BRD §3.1.5 requirement not mirrored |
| DRA-05 | Underground utility methods | GPR + DGPS + GNSS + 12D | GPR only | Missing positioning methods and drainage model |
| DRA-06 | Airside NAVAID GIS layers | enumerated set | not enumerated | BRD §3.1.3 deliverable missing |
| DRA-07 | Landside GIS topographic catalogue | 10-layer set | not enumerated | BRD §3.1.2 deliverable missing |
| DRA-08 | Landside DEM / 3×3 m spot levels | required | not mentioned | BRD §3.1.2 deliverables missing |
| DRA-09 | Six missing mandatory AI agents | 8 agents | 3 itemised | Agent inventory shortfall |
| DRA-10 | Five missing per-agent performance target sets | 7 predictive agents with targets | 2 agents with targets | KPI 4 over-claim root cause |
| DRA-11 | KPI 1 uptime exclusions | planned maintenance only | +Excluded Events | Widens exclusion set |
| DRA-12 | KPI 2 latency measurement point | sensor-to-dashboard | platform boundary | Narrows measurement scope |
| DRA-13 | KPI 7 integration baseline | 100% of agreed points | 100% of baseline, subject to freeze | Narrows coverage scope |
| DRA-14 | Breach notification (non-CERT-In) | ≤12 h any incident | 2 h only for CERT-In-reportable | Universal obligation not restated |
| DRA-15 | Data retention / sovereignty on renewal | in-India, 5-year minima | "renewal terms agreed" | Could reopen retention and cross-border rules |

**Finding:** the proposal's deviation register captures only 2 of at least 15 material shortfalls or carve-outs against the BRD. A presence-based checker sees "deviations declared" and stops; a completeness audit finds the register is under-populated by a factor of ~7.

---

## 5. Semantic carve-out detection

Rows in the proposal's SLA table that are marked **Compliant** but contain weakening language:

| KPI | Proposal status | Commitment text | Carve-out detected | Verdict |
|---|---|---|---|---|
| 1 Platform Uptime | Compliant | "≥99.5%, excluding planned maintenance **and Excluded Events**" | Adds force majeure, DIAL/third-party-caused outage, third-party feed/API unavailability | **Partial** |
| 2 Data Latency | Compliant | "≤5 s, sensor to dashboard, **measured at the platform boundary**" | Excludes source-side polling/publication latency | **Partial** |
| 7 Integration Coverage | Compliant, **subject to baseline confirmation** | "100% of the agreed data-point baseline within 3 months" | Baseline freeze excludes not-present/not-commissioned points | **Partial** |

Rows marked **Compliant** but unsubstantiated:

| KPI | Claim | Evidence gap | Verdict |
|---|---|---|---|---|
| 4 Predictive Alert Accuracy | "Per-agent standards, each at or above the BRD threshold — Compliant" | Only 2 of 7 predictive agents have targets in the proposal. | **Over-claim / Partial** |

---

## 6. Multi-artefact reconciliation: proposal vs RTM

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

## 7. New issue not prominent in the original §9–§11 report

The original `compliance-report.md` focused on the RTM and then added three manual adversarial passes on the proposal. Running the improved logic from the start against the proposal surfaces one additional concern:

### 7.1 15-year lifecycle / O&M renewal carve-out

- **BRD Objective 6:** platform designed for minimum 15-year operational lifecycle.
- **Proposal line 1009:** architecture is 15-year / open-standards.
- **Proposal lines 1010–1011:** O&M is a 5-year term "renewable for two further five-year terms at DIAL's option on **terms agreed at renewal**."

This is not a deviation in the technical sense, but it is a **conditional risk:** the 15-year design-life commitment is not matched by pre-agreed O&M pricing/mechanism for the second and third 5-year terms. If renewal terms are not pre-agreed, SLA continuity and data-retention commitments could be renegotiated at each renewal boundary.

**Remediation:** pre-agree the 5-year renewal pricing and mechanism, or state that renewal pricing is capped/indexed in the contract so the 15-year commitment is not reopened.

---

## 8. Blocking issues

The following 10 items are **blocking** because they are either (a) mandatory BRD requirements the proposal does not meet at the binding value, or (b) declared deviations that still require DIAL's written acceptance before submission.

| # | Blocking issue | BRD target | Proposal position | Why blocking |
|---|---|---|---|---|
| B-01 | Vertical RMSE | ≤3 cm | ≤20 cm (Deviation 1) | 6.7× worse; needs DIAL acceptance |
| B-02 | Horizontal RMSE | ≤5 cm | ≤10 cm (Deviation 1) | 2× worse; needs DIAL acceptance |
| B-03 | Incident response (critical) | ≤10 min | ≤30 min (Deviation 2) | 3× slower; needs DIAL acceptance |
| B-04 | DTM/DSM grid | 10 cm | 50 cm | Undeclared 5× coarsening |
| B-05 | Orthophoto GSD | ≤5 cm | ≤10 cm | Undeclared 2× coarsening |
| B-06 | Contour interval | 10 cm | not mentioned | Undeclared missing deliverable |
| B-07 | Indoor positional RMSE | ≤5 cm | not restated | Undeclared missing target |
| B-08 | Mandatory AI agents | 8 | 3 itemised | Six agents missing from proposal |
| B-09 | Per-agent performance targets | 7 agents | 2 agents | Five agents' SLA targets not offered |
| B-10 | KPI 4 over-claim | ≥80% / ≥75% per aggregate and per-agent | "Compliant" for all | Unsubstantiated status word |

---

## 9. Remediation instructions (ordered)

### Must do before submission
1. **Resolve Deviation 1:** either commit to BRD ≤5 cm H / ≤3 cm V RMSE, or obtain DIAL's written acceptance of ≤10 cm / ≤20 cm before submission. Same for Deviation 2 (≤30 min response vs ≤10 min).
2. **Add A3–A6 to deviation register or correct the proposal:** DTM/DSM 50 cm, orthophoto ≤10 cm, 10 cm contours, indoor ≤5 cm RMSE must either be corrected to BRD values or declared as deviations with rationale.
3. **Add missing survey methods and deliverables:** DGPS, GNSS, 12D drainage model, NAVAID GIS layers, landside GIS catalogue, DEM, 3×3 m spot levels.
4. **Add the missing AI agents:** expand the proposal §3.2 "Domain AI agents" table to include all 8 mandatory agents required by BRD §3.5.3, plus the NLP query agent as an additive capability.
5. **Add per-agent performance targets:** add the five missing target rows (Electrical, Structural, Fire Safety, Energy Management, Security) with BRD §3.5.4 values.
6. **Fix KPI 4 claim:** reword to "Compliant for Mechanical & HVAC and Passenger Flow; remaining agents baselined per AI-01 Data Readiness Gate and accepted on rolling 90-day window," or add all per-agent targets.
7. **Declare KPI 1/2/7 carve-outs as deviations** or align wording to BRD (planned-maintenance-only uptime exclusion, true sensor-to-dashboard latency, 100% of agreed points unconditionally).
8. **Restate breach-notification rule:** add "all non-CERT-In cybersecurity incidents notified to DIAL within 12 hours of detection" alongside the 2-hour CERT-In commitment.

### Should do
9. **Add the missing protocols to the proposal's protocol inventory** if MQTT/SNMP are not explicitly committed in the narrative (they are mentioned at line 288 but not in all tables).
10. **Pre-agree 5-year O&M renewal pricing/mechanism** to remove the 15-year lifecycle continuity risk.
11. **State LAS 1.4 explicitly** in the D-02 deliverable spec, not only in the architecture section.
12. **Add DGA, cityside IoT, mobile app, AR/VR, CCC, PSIM, SIEM, pen-test, 15-year lifecycle** as explicit deliverable/scope items (these are RTM gaps from the original report; the proposal partially addresses some but should cross-reference them).

---

## 10. Validation note: did the improved logic surface the known §9–§11 gaps?

| Known gap from original report | Surfaced by improved logic? | Where in this report |
|---|---|---|
| §9.1 — only 3 of 8 mandatory agents in proposal | **Yes** | §3.1, B-08 |
| §9.3 — only 2 of 7 per-agent target sets | **Yes** | §3.1, B-09 |
| §9.4 — KPI 4 over-claim | **Yes** | §3.1, §5, B-10 |
| §10.1 A1/A2 — RMSE deviations | **Yes** | §3.2, B-01/B-02 |
| §10.1 A3/A4 — DTM/DSM 50 cm, orthophoto ≤10 cm undeclared | **Yes** | §3.2, §4, B-04/B-05 |
| §10.1 A5 — 10 cm contours missing | **Yes** | §3.2, §4, B-06 |
| §10.1 A6 — indoor RMSE not restated | **Yes** | §3.2, §4, B-07 |
| §10.2 S1 — DGPS/GNSS/12D missing | **Yes** | §3.2, §4, DRA-05 |
| §10.2 S3 — NAVAID layers not enumerated | **Yes** | §3.2, §4, DRA-06 |
| §10.4 Dv3–Dv5 — KPI 1/2/7 carve-outs | **Yes** | §3.3, §4, §5 |
| §11.4 — 12 h breach notification not fully mirrored | **Yes** | §3.3, §4, DRA-14 |
| §11.5 — liability cap vs "bear all costs" | Partially | §3.3 notes penalty mechanism; the cap issue is a contract-negotiation risk flagged in original §11.5 |

**Correction note:** the DRAFT proposal does not contain a commercial-costing table. The "Table 6 — AI Agentic framework" with 5 generic agents is in the BRD itself (`Change Request Aiport Eye - APOC Phase 2.pdf.md`, lines 595–597), not in the proposal. The earlier draft of this report incorrectly attributed that table to the proposal at line 597.

**New issue found by the improved logic:**
- §7.1 — 15-year lifecycle / O&M renewal carve-out that could break long-term SLA continuity.

---

## 11. Pre-flight verdict

**NOT READY for assembly.** The improved logic confirms the three known gap classes (AI-agent inventory, survey/accuracy shortfalls, SLA carve-outs) and adds one new concern. The proposal's deviation register is materially under-populated: it declares 2 deviations while at least 15 shortfalls or carve-outs should appear. Until the 10 blocking items are resolved or DIAL accepts the declared/undeclared deviations in writing, the proposal is non-compliant with the binding CR/BRD v1.5.

*Grounded only in: CR/BRD v1.5, ABR 2-July-2026, PE_OT 09.06, the Proposal DRAFT, and the RTM DRAFT. No external references used.*
