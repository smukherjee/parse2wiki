# Numeric Requirements Inventory — Airport Eye (APOC Phase 2) Proposal DRAFT

**Authoritative sources (hierarchy order):**
1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` — CR/BRD v1.5
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` — ABR
3. `PE_OT System_09.06.pptx.md` — final OT-systems list

**Target artefact:** `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`

**Cross-check artefact:** `AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`

All columns follow the schema in `.claude/skills/compliance-validator/assets/numeric-inventory-template.md`.

---

## Survey and geospatial accuracy

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-AIR-01 | survey | Airborne LiDAR point density (boundary) | 20 | ≥ | pts/m² | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 230 | Airborne LiDAR | ≥ 20 pts/m² | Proposal lines 147, 210 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AIR-02 | survey | Airborne LiDAR point density (buffer) | 8 | ≥ | pts/m² | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 230 | Airborne LiDAR buffer | 8 pts/m² | Proposal lines 148, 210 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AIR-03 | survey | Horizontal RMSE | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1 / KPI 5, lines 231, 211 | Geospatial accuracy | ≤ 10 cm | Proposal lines 151, 215, 989 | Yes | Deviation 1 | 2× worse | Partial | Declared deviation; needs DIAL written acceptance. |
| N-AIR-04 | survey | Vertical RMSE | 3 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1 / KPI 5, lines 232, 211 | Geospatial accuracy | ≤ 20 cm | Proposal lines 151, 215, 989 | Yes | Deviation 1 | 6.7× worse | Partial (blocking) | Declared deviation but most consequential downstream gap; requires DIAL acceptance. |
| N-AIR-05 | survey | Orthophoto GSD | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 233; D-03 line 305 | Orthophoto | ≤ 10 cm | Proposal lines 150, 212 | No | — | 2× coarser | Fail | Undeclared shortfall against BRD ≤ 5 cm. |
| N-AIR-06 | survey | DTM/DSM grid resolution | 10 | = | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 235; D-02 line 304 | DTM/DSM | 50 cm | Proposal lines 149, 211 | No | — | 5× coarser | Fail | Undeclared shortfall; proposal omits 10 cm grid. |
| N-AIR-07 | survey | Contour interval | 10 | = | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 236; D-04 line 306 | Contour dataset | not mentioned (50 cm contours only at D-20 line 182) | Proposal line 182 | No | — | missing | Fail | 10 cm contour deliverable absent from proposal; only 50 cm underground-utility contours referenced. |
| N-AIR-08 | survey | Indoor positional RMSE | 5 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.5, line 259 | Indoor LiDAR | not restated | Proposal lines 237–238 | No | — | missing | Fail | Proposal states scans registered to airborne coordinate system but does not repeat ≤ 5 cm RMSE. |
| N-AIR-09 | survey | Underground utility scanning methods | GPR + DGPS + GNSS + 12D | = | methods | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.2, line 242 | Landside utilities | GPR only | Proposal line 214 | No | — | 1 of 4 methods | Partial / Fail | DGPS, GNSS, 12D drainage model not mentioned; missing methods are a scope shortfall. |
| N-AIR-10 | survey | Airside NAVAID GIS layers | AGL, PAPI, DVOR, Signage, RVR, MSSR, AMSR | = | layer set | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.3, line 250 | Airside NAVAIDs | not enumerated | Proposal line 405 (sensitive data class only) | No | — | missing | Fail | NAVAID layer catalogue not mirrored as a survey deliverable. |
| N-AIR-11 | survey | Point cloud format | ASPRS LAS 1.4 | = | format | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 234 | Point cloud | "Classified LAS/LAZ per ASPRS classes" | Proposal lines 218, 1009 | No | — | ambiguous | Partial / Ambiguous | LAS 1.4 appears in architecture section (line 1009) but not explicitly in D-02 deliverable spec. |
| N-AIR-12 | survey | Landside GIS topographic layers | 10-layer catalogue (land use, parcels, roads, street view, zoning, topography, wetlands, demographics, land cover, imagery, basemap) | = | layer set | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.2, line 245 | Landside GIS | not enumerated | Proposal §2.2 | No | — | missing | Fail | 10-layer catalogue not restated in proposal. |
| N-AIR-13 | survey | Landside 3×3 m spot levels | required | = | interval | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.2, line 243 | Landside topography | not mentioned | — | No | — | missing | Fail | BRD requires spot levels at 3×3 m intervals. |
| N-AIR-14 | survey | Landside DEM | required | = | deliverable | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.2, line 243 | Landside topography | not mentioned | — | No | — | missing | Fail | BRD requires DEM alongside DTM/DSM. |

---

## AI agent estate

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-AI-01 | ai | Mandatory domain AI agents | 8 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.3, lines 441–448 | AI agent estate | 3 itemised (Mechanical & HVAC, Passenger Flow, NLP query agent) | Proposal lines 500–503 | n/a | n/a | 37.5% | Fail | Six mandatory agents missing from proposal technical narrative. |
| N-AI-02–04 | ai | Mechanical & HVAC precision / recall / prediction horizon / alert latency | ≥ 82% / ≥ 78% / ≤ 72 h / ≤ 30 s | ≥ / ≥ / ≤ / ≤ | % / % / h / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 454 | Mechanical & HVAC agent | Same as binding | Proposal line 511 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-05–07 | ai | Electrical Systems precision / recall / prediction horizon / alert latency | ≥ 80% / ≥ 75% / ≤ 48 h / ≤ 30 s | ≥ / ≥ / ≤ / ≤ | % / % / h / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 455 | Electrical Systems agent | Agent absent; no targets | — | n/a | n/a | missing | Fail | Agent not itemised in proposal §3.2 table. |
| N-AI-08–10 | ai | Passenger Flow precision / recall / prediction horizon / alert latency | ≥ 85% / ≥ 80% / ≤ 45 min / ≤ 15 s | ≥ / ≥ / ≤ / ≤ | % / % / min / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 456 | Passenger Flow agent | Same as binding | Proposal line 512 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AI-11–13 | ai | Structural Integrity precision / recall / prediction horizon / alert latency | ≥ 90% / ≥ 85% / ≤ 7 d / ≤ 60 s | ≥ / ≥ / ≤ / ≤ | % / % / d / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 457 | Structural Integrity agent | Agent absent; no targets | — | n/a | n/a | missing | Fail | Agent not itemised. |
| N-AI-14–16 | ai | Fire Safety precision / recall / prediction horizon / alert latency | ≥ 95% / ≥ 95% / real-time / ≤ 5 s | ≥ / ≥ / = / ≤ | % / % / status / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 458 | Fire Safety agent | Agent absent; no targets | — | n/a | n/a | missing | Fail | Agent not itemised. |
| N-AI-17–19 | ai | Energy Management precision / recall / prediction horizon / alert latency | ≥ 80% / ≥ 75% / ≤ 24 h / ≤ 60 s | ≥ / ≥ / ≤ / ≤ | % / % / h / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 459 | Energy Management agent | Agent absent; no targets | — | n/a | n/a | missing | Fail | Agent not itemised. |
| N-AI-20–22 | ai | Security precision / recall / prediction horizon / alert latency | ≥ 88% / ≥ 82% / real-time / ≤ 15 min / ≤ 10 s | ≥ / ≥ / = / ≤ / ≤ | % / % / status / min / s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 460 | Security agent | Agent absent; no targets | — | n/a | n/a | missing | Fail | Agent not itemised. |
| N-AI-23 | ai | Aggregate predictive alert accuracy | ≥ 80% precision / ≥ 75% recall | ≥ / ≥ | % / % | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 4, line 210 | All predictive agents | "Per-agent standards, each at or above the BRD threshold — Compliant" | Proposal line 988 | n/a | n/a | over-claim | Partial / Ambiguous | Only 2 of 7 predictive agents have per-agent targets in the proposal; "Compliant" is unsubstantiated for 5 agents. |

---

## SLA / KPIs

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-SLA-01 | sla | Platform uptime | 99.5 | ≥ | % (excl. planned maintenance) | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 1, line 207 | Platform availability | ≥ 99.5% excl. planned maintenance **and Excluded Events** | Proposal lines 985, 917, 995 | No | — | widened exclusion | Partial / carve-out | Adds force majeure, DIAL/sub-vendor, third-party feed/API, and planned maintenance exclusions beyond BRD. |
| N-SLA-02 | sla | Data latency | 5 | ≤ | s (sensor → dashboard) | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 2, line 208 | Data pipeline | ≤ 5 s "measured at the platform boundary" | Proposal lines 985, 291–292 | No | — | scope narrowed | Partial / carve-out | Source-side polling/publication latency excluded from measurement. |
| N-SLA-03 | sla | BIM LOD compliance | 100 | = | % of specified assets at agreed LOD | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 3, line 209 | BIM models | 100% at agreed LOD | Proposal line 986 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SLA-04 | sla | Incident response (critical) | 10 | ≤ | min from notification | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 6, line 212 | Incident response | ≤ 30 min | Proposal lines 990, 931 | Yes | Deviation 2 | 3× slower | Partial (blocking) | Declared deviation; needs DIAL written acceptance. |
| N-SLA-05 | sla | Integration coverage | 100 | = | % of agreed BMS/IoT points within 3 months | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 7, line 213 | BMS/IoT integration | 100% of agreed **baseline** within 3 months | Proposal lines 991, 993 | No | — | scope narrowed | Partial / carve-out | Baseline freeze excludes not-present / not-commissioned / not-exposed points. |
| N-SLA-06 | sla | Breach notification | 12 | ≤ | h for any cybersecurity incident/data breach | Change Request Aiport Eye - APOC Phase 2.pdf.md | §9.11, line 699 | Cybersecurity incident response | 2 h for CERT-In-reportable incidents; no blanket 12 h stated | Proposal line 425 | No | — | mixed | Partial / Fail | Better for CERT-In-reportable incidents, but BRD covers *any* incident. |
| N-SLA-07 | sla | Penalty / material default threshold | 3 | ≥ | breaches/quarter | Change Request Aiport Eye - APOC Phase 2.pdf.md | §9.9, line 682 | SLA enforcement | ≥ 3 breaches/quarter accepted in principle | Proposal lines 1001–1003 | n/a | n/a | 1.0× | Pass | Mechanism accepted; liability cap and Excluded Events remain contract-negotiation risks. |

---

## Security and platform NFRs

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-SEC-01 | security | User roles | 5 | ≥ | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 425 | RBAC | 5 default + additional AOCC/P&E/etc. | Proposal line 343; RTM ROW-943 | n/a | n/a | exceeds | Pass | Matches and expands default role set. |
| N-SEC-02 | security | TLS in transit | 1.3 | = | TLS version | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 428 | Data in transit | TLS 1.3 minimum | Proposal line 398 | n/a | n/a | 1.0× | Pass | Matches BRD (stricter than RTM TLS 1.2+). |
| N-SEC-03 | security | Encryption at rest | AES-256 | = | cipher | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 428 | Data at rest | AES-256 | Proposal line 399 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-04 | security | Audit log retention | 2 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.4, line 429 | Audit logs | ≥ 5 years | Proposal line 411 | n/a | n/a | 2.5× longer | Pass | Exceeds BRD minimum. |
| N-SEC-05 | security | Historical BMS data retention | 5 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.4.2, line 414 | BMS/IoT historical data | ≥ 5 years | Proposal line 960 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-SEC-06 | security | AI audit log retention | 5 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.5, line 465 | AI audit logs | ≥ 5 years | Proposal line 534 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-PLAT-01 | platform | Platform design life | 15 | ≥ | years | Change Request Aiport Eye - APOC Phase 2.pdf.md | Objective 6, line 202 | Platform lifecycle | 15-year architecture; 5-year O&M renewable | Proposal lines 1009–1011 | n/a | n/a | conditional | Partial | 15-year architecture but renewal pricing/mechanism for 2nd/3rd 5-year terms is "to be agreed at renewal", creating continuity risk. |
| N-PLAT-02 | platform | Recovery Time Objective (RTO) | 4 | ≤ | h | AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md | §5.3, line 938 (addition) | Disaster recovery | < 4 h | Proposal line 938 | n/a | n/a | favourable | Pass | Proposal adds explicit RTO better than typical expectation. |
| N-PLAT-03 | platform | Recovery Point Objective (RPO) | 24 | ≤ | h | AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md | RTM ROW-964 | Disaster recovery | < 1 h | Proposal line 938 | n/a | n/a | 24× better | Pass | Proposal exceeds RTM/BRD expectation. |

---

## ABR and OT integration

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-ABR-01 | abr | Simulation-engine components | 4 | = | count | Airport Eye Additional Busines Requirements- 2-July-2026.docx.md | §4.1, lines 67–73 | Spatial Decision & Simulation engine | 4 components | Proposal lines 550–557 | n/a | n/a | 1.0× | Pass | Matches ABR four-component architecture. |
| N-ABR-02 | integration | IoT machine-room pumps | 40 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.3.4, line 379 | Mechanical & HVAC sensor base | 40 | Proposal line 263; CR/BRD line 379 | n/a | n/a | 1.0× | Pass | Matches BRD/RTM. |
| N-ABR-03 | integration | T1 roof sensors | 12 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.3.4, line 380 | Water & Drainage sensor base | 12 | Proposal line 263; CR/BRD line 380 | n/a | n/a | 1.0× | Pass | Matches BRD/RTM. |
