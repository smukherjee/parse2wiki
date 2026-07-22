# Numeric / Quantitative Requirements Inventory — Track B

**Target artefact:** `eval/airport-eye/trackB/proposal-trackB.md`
**Authoritative sources (binding priority order):**
1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` (CR/BRD v1.5, binding)
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` (ABR)
3. `PE_OT System_09.06.pptx.md` (PE_OT list)
4. `Airport_Eye_RFP_v5.docx.md` (base RFP)
5. `AirportEye_Requirements_Register_v5.xlsx.md`, `Final requirements.xlsx.md`

**Scorer:** compliance-validator skill, Step 2 output. Every comparable numeric/quantitative requirement extracted from the authoritative sources, with the corresponding value found in the Track B proposal and a parity verdict.

## Verdict key
- **Pass** — proposal value meets or exceeds binding value, no weakening.
- **Partial** — value stated but carries a carve-out / external dependency, OR declared as a deviation, OR structure present but content (e.g. pricing) absent.
- **Fail** — binding value not met and not declared in a deviation register (no formal deviation register exists in the proposal, so undeclared shortfalls are Fail per skill graceful-degradation rule).
- **Ambiguous** — source value is itself unfilled, or proposal uses a status word without a measurable figure.
- **N/A** — no comparable binding value exists in the source documents.

## Numeric inventory

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-KPI-01 | sla | Platform uptime | 99.5 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 1, line 207 | Platform | Match | V1 Headline Commitments, line 149 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-KPI-02 | sla | Real-time data latency | 5 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 2, line 208 | Data pipeline | Match | V1 line 150 | n/a | n/a | 1.0× | Pass | Matches BRD. No "measured at boundary" carve-out. |
| N-KPI-03 | platform | BIM LOD compliance | 100 | = | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 3, line 209 | BIM models | Match | V1 line 151 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-KPI-04 | ai | Predictive alert accuracy (precision) | 80 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 4, line 210 | AI agent estate | Match | V1 line 152, V3 line 456 | n/a | n/a | 1.0× | Pass | Platform-wide floor committed. |
| N-KPI-04b | ai | Predictive alert accuracy (recall) | 75 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 4, line 210 | AI agent estate | Match | V1 line 152, V3 line 456 | n/a | n/a | 1.0× | Pass | Platform-wide floor committed. |
| N-KPI-05 | survey | Horizontal RMSE | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 5 / §3.1.1, lines 211,231 | Geospatial accuracy | Match | V1 line 153, V2 line 209 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-KPI-05b | survey | Vertical RMSE | 3 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 5 / §3.1.1, lines 211,232 | Geospatial accuracy | Match | V1 line 153, V2 line 210 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-KPI-06 | sla | Critical incident response time | 10 | ≤ | min | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 6, line 212 | Incident response | Match (BRD ≤10min adopted over RFP v5 ≤1hr) | V1 lines 154,157; V4 line 516 | n/a | n/a | 1.0× | Pass | BRD adopted per binding priority. Note: V4 O&M ladder states Sev1 ≤30min response — potential internal inconsistency vs ≤10min critical-incident KPI; flagged Ambiguous in report. |
| N-KPI-07 | integration | System integration coverage | 100 | = | % within 3mo | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 7, line 213 | BMS/IoT points | Match | V1 line 155 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-01 | survey | Core airborne LiDAR point density | 20 | ≥ | pts/m² | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 230 | Airborne LiDAR | Match (≥20 pts/m²) | V2 line 207 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-02 | survey | Buffer-zone LiDAR point density | 8 | ≥ | pts/m² | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 230 | Airborne LiDAR buffer | "Match, pending DIAL confirmation" | V2 line 208 | No (no formal deviation register) | — | carve-out | Partial | Carve-out "pending DIAL confirmation" weakens a binding BRD figure. Not in a deviation register. |
| N-SUR-03 | survey | Horizontal accuracy (RMSE vs GCPs) | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 231 | Geospatial accuracy | Match | V2 line 209 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-04 | survey | Vertical accuracy (RMSE vs benchmarks) | 3 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 232 | Geospatial accuracy | Match | V2 line 210 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-05 | survey | Orthophotography GSD | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 233 | Orthophoto | Match | V2 line 211 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-06 | survey | DTM/DSM grid resolution | 10 | = | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 235 | DTM/DSM | Match | V2 line 212 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-07 | survey | Contour interval | 10 | = | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 236 | Contours | not addressed | — | No | — | — | Fail | BRD §3.1.1 requires "10 cm contour datasets"; proposal's V2 Component 1 commitment table omits contours entirely. Undeclared shortfall. Blocking. |
| N-SUR-08 | survey | Indoor positional accuracy | 5 | ≤ | cm RMSE | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.5, line 259 | Indoor LiDAR | Match | V2 line 213 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-09 | survey | Survey extent / buffer | 200 / 5 | ≈ / ≥ | sq.km / km | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 228 | Survey coverage | ~200+ sq.km, 5km buffer | V2 line 201, V3 line 326 | n/a | n/a | 1.0× | Pass | Addressed. |
| N-SUR-10 | survey | LOD range / BIM categories | 200–350 / 10 | = | range / count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.8, lines 289–299 | BIM modelling | Match | V2 line 214 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-01 | ai | Mandatory domain AI agents (count) | 8 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.3, lines 436–448 | AI agent estate | 8 itemised | V3 lines 352–386 | n/a | n/a | 1.0× | Pass | All 8 BRD agents present in narrative. |
| N-AI-02 | ai | Mech&HVAC precision / recall / horizon / latency | 82 / 78 / 72 / 30 | ≥ / ≥ / ≤(hr) / ≤(s) | % / % / hr / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 454 | Mech&HVAC Agent | Match | V3 line 357 | n/a | n/a | 1.0× | Pass | All four targets stated. |
| N-AI-03 | ai | Electrical precision / recall / horizon / latency | 80 / 75 / 48 / 30 | ≥ / ≥ / ≤(hr) / ≤(s) | % / % / hr / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 455 | Electrical Agent | Match | V3 line 361 | n/a | n/a | 1.0× | Pass | All four targets stated. |
| N-AI-04 | ai | Fire Safety precision / recall / horizon / latency | 95 / 95 / real-time / 5 | ≥ / ≥ / = / ≤(s) | % / % / — / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 458 | Fire Safety Agent | Match | V3 line 365 | n/a | n/a | 1.0× | Pass | Tightest targets matched. |
| N-AI-05 | ai | Water & Drainage performance target | — | — | — | (absent from BRD §3.5.4 and RFP §6.5) | §3.5.4 / §6.5 | Water & Drainage Agent | no source target | V3 line 369 | n/a | n/a | — | N/A | Genuine source-document gap; agent scope delivered, no numeric parity possible. |
| N-AI-06 | ai | Energy Mgmt precision / recall / horizon / latency | 80 / 75 / 24 / 60 | ≥ / ≥ / ≤(hr) / ≤(s) | % / % / hr / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 459 | Energy Agent | Match | V3 line 373 | n/a | n/a | 1.0× | Pass | All four targets stated. (Agent unpriced in BRD Table 6 — commercial gap, not parity.) |
| N-AI-07 | ai | Passenger Flow precision / recall / horizon / latency | 85 / 80 / 45 / 15 | ≥ / ≥ / ≤(min) / ≤(s) | % / % / min / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 456 | Passenger Flow Agent | Match | V3 line 377 | n/a | n/a | 1.0× | Pass | All four targets stated. (Unpriced — commercial gap.) |
| N-AI-08 | ai | Structural Integrity precision / recall / horizon / latency | 90 / 85 / 7(days) / 60 | ≥ / ≥ / ≤(d) / ≤(s) | % / % / d / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 457 | Structural Agent | Targets matched, but "roster inclusion is; actual deliverability is" — truncated/conditional | V3 lines 381–382 | No (informal flag only, no deviation ID) | — | conditional | Partial | Performance targets stated, but delivery contingent on DIAL procuring SHM sensor network + 6–12mo baseline. Carve-out weakens commitment; not in a deviation register. |
| N-AI-09 | ai | Security precision / recall / horizon / latency | 88 / 82 / 15(min) / 10 | ≥ / ≥ / ≤(min) / ≤(s) | % / % / min / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 460 | Security Agent | Targets matched, but "all scope subject to CISF approval before build starts" | V3 line 386 | No (informal flag only) | — | conditional | Partial | Carve-out "subject to CISF approval" weakens a binding performance commitment; not in a deviation register. |
| N-GOV-01 | ai | AI alert audit log retention | 5 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.5, line 465 | AI governance | Match | V3 line 412 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-GOV-02 | ai | Model rollback time | 4 | ≤ | hours | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.5, line 468 | AI governance | Match | V3 line 414 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-01 | security | Breach notification to DIAL | 12 | ≤ | hours | Change Request Aiport Eye - APOC Phase 2.pdf.md | §9.11, line 699 | Cybersecurity | Match | V2 line 278 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-02 | security | Activity audit log retention | 2 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 429 | Platform security | Match | V2 line 266 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-03 | platform | BMS historical data retention | 5 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.2, line 414 | BMS archive | Match | V2 line 258 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-04 | security | RBAC user roles (count) | 5 | ≥ | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 425 | Access control | Match (5 named roles) | V2 line 262 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-05 | security | In-transit / at-rest encryption | TLS 1.3 / AES-256 | = | standard | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 428 | Encryption | Match (BRD TLS 1.3 adopted over register's TLS 1.2+) | V2 line 264 | n/a | n/a | 1.0× | Pass | BRD governs per binding priority. |
| N-SEC-06 | integration | API backward compatibility | 2 | ≥ | major versions | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.3, line 422 | APOC/CCC APIs | Match | V2 line 260, V3 line 314 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-INT-01 | sla | RTO | 4 | ≤ | hours | AirportEye_Requirements_Register_v5.xlsx.md | NFR row "RTO 4 hours" | O&M | Match | V4 line 516, V5 line 573 | n/a | n/a | 1.0× | Pass | Matches register NFR. |
| N-INT-02 | sla | RPO | 24 | ≤ | hours | AirportEye_Requirements_Register_v5.xlsx.md | NFR row "RPO 24 hours" | O&M | Match | V4 line 516, V5 line 573 | n/a | n/a | 1.0× | Pass | Matches register NFR. |
| N-COM-01 | commercial | Payment milestones (6, % split) | 15/10/20/25/20/10 | = | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §7, lines 645–651 | Commercial | Match | V5 lines 557–565 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-COM-02 | commercial | Warranty period | 12 | ≥ | months | Airport_Eye_RFP_v5.docx.md | §9.5, line 788 | Warranty | Match | V5 line 569 | n/a | n/a | 1.0× | Pass | Matches RFP. |
| N-COM-03 | commercial | O&M period | 5 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | Table 8 / §8 | O&M | Match | V4 line 516, V5 line 573 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-COM-04 | commercial | Proposal validity | 180 | ≥ | days | Airport_Eye_RFP_v5.docx.md | §9.1, line 760 | Commercial | Match | V5 line 581 | n/a | n/a | 1.0× | Pass | Matches RFP. |
| N-COM-05 | commercial | Exit transition support | 6 | ≥ | months | Change Request Aiport Eye - APOC Phase 2.pdf.md | §9.12, line 711 | Exit | Match | V4 line 519 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-COM-06 | commercial | Costing tables (count) | 8 | = | tables | Change Request Aiport Eye - APOC Phase 2.pdf.md | §6, Tables 1–8 | Commercial | Structure committed (8 tables listed), all pricing blank | V5 lines 540–549 | No (flagged "pending bidder input") | — | unpriced | Partial | 8-table structure present but every table is unpriced. Commercial proposal not evaluable. Blocking. |
| N-PRE-01 | prequal | Years digital-twin/BIM/geospatial experience | 5 | ≥ | years | Airport_Eye_RFP_v5.docx.md | App. E, line 816 | Pre-qualification | Met (incumbent since 2019 CA) | V6 line 613 | n/a | n/a | ≥1.0× | Pass | Met. |
| N-PRE-02 | prequal | Comparable deployments | 2 | ≥ | count | Airport_Eye_RFP_v5.docx.md | App. E, line 817 | Pre-qualification | 1 of 2 evidenced (RGIA only) | V6 line 614 | No (flagged) | — | 0.5× | Fail | Pre-qualification gate not met. Declared but still a mandatory gate failure. Blocking. |
| N-PRE-03 | prequal | ISO 9001:2015 | held | = | cert | Airport_Eye_RFP_v5.docx.md | App. E, line 818 | Pre-qualification | Met | V6 line 615 | n/a | n/a | — | Pass | Held. |
| N-PRE-04 | prequal | ISO/IEC 27001:2013 | held | = | cert | Airport_Eye_RFP_v5.docx.md | App. E, line 819 | Pre-qualification | Met | V6 line 616 | n/a | n/a | — | Pass | Held. |
| N-PRE-05 | prequal | Annual turnover | [X] | ≥ | INR crore | Airport_Eye_RFP_v5.docx.md | App. E, line 820 | Pre-qualification | Cannot confirm (source placeholder unfilled) | V6 line 617 | n/a | n/a | — | Ambiguous | Source itself carries `[X] crore`; neither binding value nor proposal value can be fixed. |
| N-PLATFORM-01 | platform | Operational lifecycle | 15 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | Objective 6, line 202 | Platform architecture | no explicit commitment | V2 (absent), RTM R-020 "no explicit 15-year commitment evidenced" | No | — | — | Fail | Binding BRD Objective 6 "minimum 15-year operational lifecycle" not committed anywhere in proposal. Undeclared. Blocking. |
| N-SUB-01 | submission | Case studies (minimum) | 3 | ≥ | count | Airport_Eye_RFP_v5.docx.md | §9.3, line 638 | Submission | 1 of 3 (2 placeholders) | V6 lines 641–647 | No (flagged) | — | 0.33× | Fail | Mandatory submission minimum not met. Blocking. |
| N-SUB-02 | submission | CVs / key personnel | present | = | content | Airport_Eye_RFP_v5.docx.md | §9.3, line 639 | Submission | complete blank (skeleton only, no named personnel) | V7 lines 670–721 | No (flagged) | — | 0× | Fail | Mandatory submission content absent. Blocking. |
| N-SUB-03 | submission | Volume 1 page limit | 10 | ≤ | pages | Airport_Eye_RFP_v5.docx.md | §9.3, line 633 | Submission | ~5 pages | Pre-Flight line 65 | n/a | n/a | 0.5× | Pass | Within limit. |
| N-DEL-01 | delivery | Numbered deliverables | 15 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §4.2, lines 483–492 | Delivery | Match (D-01–D-15) | V4 line 484 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-DEL-02 | delivery | DIAL review period per deliverable | 14 | = | calendar days | Change Request Aiport Eye - APOC Phase 2.pdf.md | §4.2, line 483 | Delivery | Match | V4 line 488 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-DEL-03 | delivery | Programme phases / duration | 5 / ~15 | = / ≈ | phases / months | Change Request Aiport Eye - APOC Phase 2.pdf.md | §4.1, lines 474–479 | Delivery | Match (5 phases ~3mo each, ~15mo) | V4 lines 472–478 | n/a | n/a | 1.0× | Pass | BRD 15-month structure adopted. |

## Numeric inventory summary

| Verdict | Count |
|---|---|
| Pass | 43 |
| Partial | 4 (N-SUR-02, N-AI-08, N-AI-09, N-COM-06) |
| Fail | 5 (N-SUR-07, N-PRE-02, N-PLATFORM-01, N-SUB-01, N-SUB-02) |
| Ambiguous | 1 (N-PRE-05) |
| N/A | 1 (N-AI-05) |
| **Total rows** | **54** |

## Notes on hierarchy / contradictions resolved

- **Critical incident response (N-KPI-06):** BRD §2.3 KPI-6 = ≤10 min; RFP v5 §2.3 KPI-6 = ≤1 hour. Per binding priority (CR/BRD overrides base RFP), ≤10 min is binding. Proposal adopts ≤10 min → Pass. Internal inconsistency flagged: V4 O&M ladder states "Sev1 ≤30min response" alongside the ≤10min critical-incident KPI; proposal claims no contradiction but the two figures coexist without a clear reconciliation of "critical incident" vs "Sev1".
- **TLS (N-SEC-05):** BRD §3.4.4 = TLS 1.3; requirements register = "TLS 1.2+". Per binding priority, BRD's TLS 1.3 governs. Proposal adopts TLS 1.3 → Pass.
- **Indoor scanning density (R-028):** RFP v5 §3.2.1 carries an unfilled `[X] pts/m²` placeholder — no binding numeric value exists. Categorical entry R-028 is Ambiguous; no numeric row generated.
- **Water & Drainage agent (N-AI-05):** No performance target in BRD §3.5.4 or RFP §6.5. Genuine source gap → N/A.
- **No formal deviation register exists in the proposal.** The proposal uses `[GAP]` RTM markers and an "Unresolved Items" list as an informal declaration mechanism, but there is no register with unique deviation IDs, rationale, and mitigation/acceptance requirements. Per skill graceful-degradation rule, below-binding shortfalls that are not in a formal deviation register are scored Fail (undeclared) where they are not even informally flagged, and Partial where informally flagged with a carve-out. This increases compliance risk and is itself a blocking structural finding.