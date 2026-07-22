# Numeric / Quantitative Requirements Inventory — Track A

**Target artefact:** `eval/airport-eye/trackA/proposal-trackA.md`
**Authoritative sources (binding priority):**
1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` (CR/BRD v1.5, issued 05-June-2026) — binding
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` (ABR)
3. `PE_OT System_09.06.pptx.md` (PE_OT)
4. `Airport_Eye_RFP_v5.docx.md` (base RFP)
5. `AirportEye_Requirements_Register_v5.xlsx.md` / `Final requirements.xlsx.md`

**Scorer note:** BRD KPI values override the base RFP where they differ. The single divergence is KPI #6 (critical incident response): BRD = ≤10 min, RFP = ≤1 hour. The BRD (≤10 min) is binding and is the value used for parity. The proposal correctly adopts ≤10 min.

## Survey / Geospatial

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-SUR-01 | survey | Airborne LiDAR point density (airport boundary) | 20 | ≥ | pts/m² | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 230 | Airborne LiDAR | 20 pts/m² | §4.1, line 83 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-02 | survey | Airborne LiDAR point density (buffer) | 8 | ≥ | pts/m² | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 230 | Buffer zones | 8 pts/m² | §4.1, line 83 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-03 | survey | Horizontal RMSE | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 231 | Geospatial accuracy | 5 cm RMSE | §4.1, line 83; §11 KPI 5, line 231 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-04 | survey | Vertical RMSE | 3 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 232 | Geospatial accuracy | 3 cm RMSE | §4.1, line 83; §11 KPI 5, line 231 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-05 | survey | Orthophoto GSD | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 233 | Orthophotography | 5 cm GSD | §4.1, line 83 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-06 | survey | DTM/DSM grid resolution | 10 | = | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 235 | DTM/DSM | 10 cm grid | §4.1, line 83 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-07 | survey | Contour interval | 10 | = | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 236; §3.1.9 D-04, line 306 | Contour dataset | not stated | — | No | — | — | Fail | 10 cm contour dataset never mentioned in technical narrative or deliverables table (D-02 omits contours). Undeclared shortfall. |
| N-SUR-08 | survey | 3D mesh model (deliverable) | required | = | deliverable | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 236; §3.1.9 D-05, line 308 | Survey deliverable | viewer "supports" 3D mesh; production as deliverable not committed | §4.4/§4.6 (display only) | No | — | — | Fail | Mesh appears only as a viewer display input, not as a produced LAS-derived deliverable (BRD §3.1.9 D-05). Undeclared shortfall. |
| N-SUR-09 | survey | Indoor positional RMSE | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.5, line 259 | Indoor LiDAR | 5 cm RMSE | §4.1, line 83 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-10 | survey | Survey buffer / total area | 5 / 200 | = | km / sq.km | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 228 | Survey extent | 5 km buffer, ~200 sq.km | §4.1, line 83 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SUR-11 | survey | Point cloud format | ASPRS LAS 1.4 | = | format | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 234 | Point cloud | ASPRS LAS 1.4 | §4.1, line 83 | n/a | n/a | — | Pass | Matches BRD. |
| N-SUR-12 | survey | Indoor point density | [X] | ≥ | pts/m² | Airport_Eye_RFP_v5.docx.md | §3.2.1, line 301 | Indoor scanning | not stated | — | n/a | n/a | — | Ambiguous | Source itself leaves value as "[X]" (unspecified). No comparable figure. |
| N-SUR-13 | survey | Landside spot level interval | 3x3 | = | m grid | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.2, line 243 | Landside coverage | not stated | — | No | — | — | Fail | BRD requires DTM/DSM/DEM/contours/spot levels at 3x3 m intervals; not addressed anywhere in proposal. Undeclared shortfall. |
| N-SUR-14 | survey | Survey accuracy metadata standard | ISO 19115 | = | standard | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.9 D-07, line 310 | Accuracy report | not stated | — | No | — | — | Fail | BRD Phase-1 deliverable D-07 (ISO 19115 metadata) not reflected in proposal deliverable table. Undeclared shortfall. |

## AI Agents

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-AI-01 | ai | Mandatory domain AI agents | 8 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.3, lines 436–448 | AI agent estate | 8 named | §4.5, line 101 | n/a | n/a | 1.0× | Pass | All 8 agents itemised. |
| N-AI-02 | ai | Mechanical & HVAC — precision | 82 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 454 | Mechanical agent | ≥82% | §11 table, line 239 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-03 | ai | Mechanical & HVAC — recall | 78 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 454 | Mechanical agent | ≥78% | §11 table, line 239 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-04 | ai | Mechanical & HVAC — prediction horizon | 72 | ≥ | hours | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 454 | Mechanical agent | up to 72 h | §11 table, line 239 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-05 | ai | Mechanical & HVAC — alert latency | 30 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 454 | Mechanical agent | ≤30 s | §11 table, line 239 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-06 | ai | Electrical — precision | 80 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 455 | Electrical agent | ≥80% | §11 table, line 240 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-07 | ai | Electrical — recall | 75 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 455 | Electrical agent | ≥75% | §11 table, line 240 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-08 | ai | Electrical — prediction horizon | 48 | ≥ | hours | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 455 | Electrical agent | up to 48 h | §11 table, line 240 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-09 | ai | Electrical — alert latency | 30 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 455 | Electrical agent | ≤30 s | §11 table, line 240 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-10 | ai | Passenger Flow — precision | 85 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 456 | Passenger Flow agent | ≥85% | §11 table, line 241 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-11 | ai | Passenger Flow — recall | 80 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 456 | Passenger Flow agent | ≥80% | §11 table, line 241 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-12 | ai | Passenger Flow — prediction horizon | 45 | ≥ | min | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 456 | Passenger Flow agent | up to 45 min | §11 table, line 241 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-13 | ai | Passenger Flow — alert latency | 15 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 456 | Passenger Flow agent | ≤15 s | §11 table, line 241 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-14 | ai | Structural — precision | 90 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 457 | Structural agent | ≥90% | §11 table, line 242 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-15 | ai | Structural — recall | 85 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 457 | Structural agent | ≥85% | §11 table, line 242 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-16 | ai | Structural — prediction horizon | 7 | ≥ | days | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 457 | Structural agent | up to 7 days | §11 table, line 242 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-17 | ai | Structural — alert latency | 60 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 457 | Structural agent | ≤60 s | §11 table, line 242 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-18 | ai | Fire Safety — precision | 95 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 458 | Fire Safety agent | ≥95% | §11 table, line 243 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-19 | ai | Fire Safety — recall | 95 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 458 | Fire Safety agent | ≥95% | §11 table, line 243 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-20 | ai | Fire Safety — prediction horizon | real-time | = | mode | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 458 | Fire Safety agent | real-time | §11 table, line 243 | n/a | n/a | — | Pass | Matches BRD. |
| N-AI-21 | ai | Fire Safety — alert latency | 5 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 458 | Fire Safety agent | ≤5 s | §11 table, line 243 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-22 | ai | Energy — precision | 80 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 459 | Energy agent | ≥80% | §11 table, line 244 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-23 | ai | Energy — recall | 75 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 459 | Energy agent | ≥75% | §11 table, line 244 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-24 | ai | Energy — prediction horizon | 24 | ≥ | hours | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 459 | Energy agent | up to 24 h | §11 table, line 244 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-25 | ai | Energy — alert latency | 60 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 459 | Energy agent | ≤60 s | §11 table, line 244 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-26 | ai | Security — precision | 88 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 460 | Security agent | ≥88% | §11 table, line 245 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-27 | ai | Security — recall | 82 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 460 | Security agent | ≥82% | §11 table, line 245 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-28 | ai | Security — prediction horizon | real-time / 15 min | = | mode | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 460 | Security agent | real-time / 15 min | §11 table, line 245 | n/a | n/a | — | Pass | Matches BRD. |
| N-AI-29 | ai | Security — alert latency | 10 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 460 | Security agent | ≤10 s | §11 table, line 245 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-30 | ai | Water & Drainage — performance targets | not specified in BRD | — | — | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.3 vs §3.5.4 (gap in source) | Water & Drainage agent | platform baseline (≥80% / ≥75%) proposed | §11 note, line 247; DC-03, line 298 | Yes | DC-03 | — | Ambiguous | Source itself omits this agent from the §3.5.4 table. Proposal declares the gap (DC-03) and proposes baseline pending DIAL confirmation. Assumed compliant subject to DIAL acceptance. |
| N-AI-31 | ai | Model rollback time | 4 | ≤ | hours | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.5, line 468 | Model governance | within 4 hours | §9, line 207 | n/a | n/a | 1.0× | Pass | Matches BRD. |

## SLA / Platform KPIs

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-SLA-01 | sla | Platform uptime | 99.5 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 1, line 207 | Platform | ≥99.5% | §11 KPI 1, line 227 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SLA-02 | sla | Real-time data latency | 5 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 2, line 208 | Data pipeline | ≤5 s | §11 KPI 2, line 228 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SLA-03 | sla | BIM LOD compliance | 100 | = | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 3, line 209 | BIM | 100% | §11 KPI 3, line 229 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SLA-04 | sla | Predictive alert precision | 80 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 4, line 210 | AI alerts | ≥80% | §11 KPI 4, line 230 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SLA-05 | sla | Predictive alert recall | 75 | ≥ | % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 4, line 210 | AI alerts | ≥75% | §11 KPI 4, line 230 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SLA-06 | sla | Geospatial horizontal RMSE | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 5, line 211 | Geospatial | ≤5 cm | §11 KPI 5, line 231 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SLA-07 | sla | Geospatial vertical RMSE | 3 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 5, line 211 | Geospatial | ≤3 cm | §11 KPI 5, line 231 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SLA-08 | sla | Critical incident response | 10 | ≤ | min | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 6, line 212 | Incident response | ≤10 min | §11 KPI 6, line 232 | n/a | n/a | 1.0× | Pass | Proposal adopts stricter BRD value (RFP says ≤1 hour). Correct precedence. |
| N-SLA-09 | sla | System integration coverage | 100 | = | % within 3 months | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 7, line 213 | BMS/IoT integration | 100% within 3 months of go-live | §11 KPI 7, line 233 | n/a | n/a | 1.0× | Pass | Matches BRD. |

## Security / Platform / Data Governance

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-SEC-01 | security | Defined user roles | 5 | ≥ | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 425 | RBAC | 5 roles | §9, line 203 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-02 | security | Activity audit log retention | 2 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 429 | Audit logging | ≥2 years | §9, line 203 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-03 | security | AI alert audit log retention | 5 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.5, line 465 | AI governance | ≥5 years | §9, line 207; §11, line 249 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-04 | platform | BMS historical archive retention | 5 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.2, line 414 | BMS archive | ≥5 years | §4.4, line 97; §8, line 187 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-05 | platform | API backwards compatibility | 2 | ≥ | major versions | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.3, line 422 | APIs | ≥2 major versions | §4.4, line 97; §8, line 193 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-06 | security | Breach notification time | 12 | ≤ | hours | Change Request Aiport Eye - APOC Phase 2.pdf.md | §9.11, line 699 | Incident notification | within 12 hours | §9, line 205 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-07 | security | Data sovereignty | India-only | = | jurisdiction | Change Request Aiport Eye - APOC Phase 2.pdf.md | §9.10, line 692; RFP §9.6, line 792 | Data residency | no data outside India without written approval | §9, line 205 | n/a | n/a | — | Pass | Matches BRD. |
| N-SEC-08 | platform | Platform operational lifecycle | 15 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §1.4/§2.2 Obj 6, lines 137, 202 | Platform architecture | ≥15 years | §4.4, line 95; §8, line 195 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-09 | platform | Transition support | 6 | ≥ | months | Change Request Aiport Eye - APOC Phase 2.pdf.md | §9.12, line 711 | Exit management | ≥6 months | §11, line 255 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-10 | procedural | Proposal validity | 180 | ≥ | days | Airport_Eye_RFP_v5.docx.md | §9.1, line 760 | Submission | ≥180 days | §13, line 288 | n/a | n/a | 1.0× | Pass | Matches RFP. |
| N-SEC-11 | platform | Warranty period | 12 | ≥ | months | Airport_Eye_RFP_v5.docx.md | §9.5, line 788 | Warranty | 12 months | §11, line 251; DC-04 | Yes | DC-04 | 1.0× | Pass | BRD silent; RFP 12 months adopted and declared for DIAL confirmation. |
| N-SEC-12 | platform | IoT machine-room pump sensors | 40 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.3.4, line 379 | IoT sensors | 40 | §4.3, line 91 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-13 | platform | T1 roof-drain water-level sensors | 12 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.3.4, line 380 | IoT sensors | 12 | §4.3, line 91 | n/a | n/a | 1.0× | Pass | Matches BRD. |

## Commercial

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-COM-01 | commercial | Completed 8-part pricing rate card | required (8 tables, INR excl. GST) | = | deliverable | Change Request Aiport Eye - APOC Phase 2.pdf.md | §6 Tables 1–8, lines 541–625; Airport_Eye_RFP_v5.docx.md §10, lines 645–736 | Commercial submission | not filled; deferred | §13, line 275; §12 | Yes (deferred) | DC-06 (GST); §12 open items | — | Fail | Pricing envelope explicitly deferred pending Appendix A/B/D and hosting decision. Deferral is declared, but the rate card is a mandatory Volume 5 deliverable; a submission without itemised pricing is non-compliant. |

## Numeric inventory summary

| Verdict | Count |
|---|---|
| Pass | 61 |
| Fail | 5 (N-SUR-07, N-SUR-08, N-SUR-13, N-SUR-14, N-COM-01) |
| Ambiguous | 2 (N-SUR-12, N-AI-30) |
| **Total numeric rows** | **68** |

**Key finding:** Every BRD numeric KPI and all seven itemised AI-agent performance standards are met at full parity (1.0×). The single BRD/RFP divergence (critical incident response: ≤10 min vs ≤1 hour) is correctly resolved in favour of the stricter BRD value. Numeric failures cluster in (a) Phase-1 data deliverables silently dropped from the deliverables table (10 cm contours, 3D mesh model, ISO 19115 metadata, 3×3 m spot levels) and (b) the unfilled commercial rate card.