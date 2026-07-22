# Gold Score — Track B Proposal

**Proposal scored:** `eval/airport-eye/trackB/proposal-trackB.md` (WAISL Limited + GEOKNO, Track B Stage 5 assembler output, dated 17-July-2026)
**Gold inventory used:** `eval/airport-eye/gold-requirements.md` (189 requirements: 125 categorical + 64 numeric)
**Scoring date:** 17-July-2026
**Scorer:** SCORING agent (controlled eval, fixed gold set)

**Scoring rules applied:**
- Pass = clearly addressed at/above binding value with checkable evidence.
- Partial = addressed but weaker than binding, OR declared deviation/carve-out/conditional, OR some elements present and others missing.
- Fail = not addressed, or below binding with no declaration; placeholder/"to be confirmed" on a mandatory requirement counts as Fail (honesty is not compliance).
- Declared shortfalls in the proposal's RTM `[GAP]` markers / "Honest Gaps" section are treated as declared deviations → Partial.
- Explicit `[Placeholder — bidder input]` slots for mandatory content → Fail.
- Carve-out weakening phrases ("pending DIAL confirmation", "subject to CISF approval", "conditional scope") → downgrade to Partial.

---

## 1. Summary Table

| Verdict | Count |
|---|---|
| Pass | 90 |
| Partial | 70 |
| Fail | 28 |
| Ambiguous | 1 |
| N/A | 0 |
| **Total** | **189** |

| Metric | Value |
|---|---|
| Pass rate (Pass / (189 − N/A)) | 90 / 189 = **47.6%** |
| Blocking count (mandatory Fails) | **28** |
| Overall verdict | **BLOCKING** |

**Bottom line:** The proposal is structurally complete (all 7 volumes present) and unusually honest about its own gaps, but it fails to address 28 mandatory requirements (chiefly the Operational Digital Twin functional layer G-121..G-132, detailed survey/underground-utility deliverables, environmental monitoring, and the ≥3 case-studies / CV submission gates) and only partially addresses a further 70. It is not submission-ready.

---

## 2. Blocking Issues List (Mandatory Fails)

| G-ID | Requirement (short) | Binding value | Proposal position | Why blocking |
|---|---|---|---|---|
| G-006 | Vol 6 — ≥3 case studies + client references | ≥3 case studies | Only RGIA evidenced; CS 2 & 3 are `[Placeholder — bidder input]` | Mandatory submission-content gate unmet; placeholders = Fail |
| G-015 | Pre-qualification: no pending insolvency/legal/adverse regulatory | shall satisfy | Not addressed anywhere in V6 | Mandatory pre-qualification gate, undeclared omission |
| G-037 | PAS 1192-2:2013 + BS EN ISO 19650-2:2019 compliance | shall comply | Not mentioned | Mandatory standard, undeclared |
| G-049 | 3D mesh models (OBJ/FBX, georeferenced) + 10 cm contours | shall deliver | Not addressed | Mandatory substantive deliverable, undeclared |
| G-050 | Flight report, sensor calibration certificate, GCP survey report | shall deliver | Not addressed | Mandatory deliverable, undeclared |
| G-051 | Raw/processed data compatible with ESRI ArcGIS and Autodesk | shall deliver | Not addressed | Mandatory interoperability, undeclared |
| G-053 | Underground utility scanning using GPR + DGPS + GNSS + 12D | shall deliver (all 4) | Not addressed (no underground-utility scanning described) | All four methods binding; complete omission |
| G-054 | Landside GIS 10-layer catalogue | shall provide | Not addressed | Mandatory catalogue, undeclared |
| G-055 | Airside layer-wise scanning (Runway/Taxiway/Apron/etc.) | shall deliver | Not detailed beyond generic "airside" mention | Mandatory, undeclared |
| G-056 | Airside GIS layers (AGL, PAPI, DVOR, NAVAIDs, etc.) | shall provide | Not addressed | Mandatory, undeclared |
| G-060 | Indoor scans registered to airborne coordinate system | shall | Not addressed | Mandatory continuity requirement, undeclared |
| G-072 | Pre-maintenance & planning (terrain, soil, noise, flood, evacuation) | shall | Environmental monitoring flagged as gap; remainder not addressed | Mandatory substantive, largely undeclared |
| G-074 | Environmental monitoring (Shahabad MdPur, NMT, Nursery CAQM) | shall | Not addressed | Mandatory, undeclared |
| G-121 | Ops DT — Airside ops (GSE, turnaround, RVR, NOTAM, etc.) | shall | Not addressed (Ops DT functional layer not described) | Mandatory register requirement, undeclared |
| G-122 | Ops DT — Terminal ops (KPIs, queue mgmt, heatmaps, dwell) | shall | Not addressed | Mandatory, undeclared |
| G-123 | Ops DT — Curbside (vehicle monitoring, parking, trolley) | shall | Not addressed | Mandatory, undeclared |
| G-124 | Ops DT — Security (intrusion, unattended baggage, smart trolley) | shall | Not addressed | Mandatory, undeclared |
| G-125 | Ops DT — Airport/Terminal/Airside summary KPIs + facility roll-up | shall | Not addressed | Mandatory, undeclared |
| G-126 | OT/IT asset widgets (per-equipment KPI widgets) | shall | Not addressed | Mandatory, undeclared |
| G-127 | DT visualization — Desktop GPU thick-client + Web-GL browser | shall | Not addressed | Mandatory, undeclared |
| G-128 | IT asset visualization cap | =3000 units | Not addressed | Mandatory numeric, undeclared |
| G-129 | Multi-level navigation airport→terminal→zone→floor→system→asset | shall | Not addressed | Mandatory, undeclared |
| G-130 | OT asset visualization at LOD 350 + LOD 200 interiors | shall | Not addressed | Mandatory, undeclared |
| G-131 | Asset registry & modeling (CLG, CAI, taxonomy, ontology) | shall | Not addressed | Mandatory, undeclared |
| G-132 | Asset federation (IT, SAP, ArcGIS, RMS, VMS) | shall | Not addressed | Mandatory, undeclared |
| G-171 | Min case studies in Volume 6 | ≥3 | Only 1 evidenced; 2 placeholders | Mandatory numeric gate unmet |
| G-175 | Underground utility scanning area (landside) | =225 acres | Not addressed | Mandatory numeric, undeclared |
| G-186 | T1 ECMS tags (Schneider) | =20,000 tags | Not addressed (only T3 ECMS stated) | Mandatory numeric, undeclared |

---

## 3. Full Per-Requirement Verdict Table

| G-ID | Verdict | Note |
|---|---|---|
| G-001 | Pass | V1 ~5 pages, within ≤10 page limit. |
| G-002 | Pass | V2 present — architecture, methodology, compliance. |
| G-003 | Pass | V3 present — per-agent approach, governance, data-readiness. Training-data strategy light but covered. |
| G-004 | Partial | Programme + QA present; resource plan is skeleton (V7); no formal risk register. |
| G-005 | Partial | 8-table structure committed; INR/GST assumptions declared; final unit pricing placeholder. |
| G-006 | Fail | ≥3 case studies mandatory; only RGIA evidenced, CS 2 & 3 `[Placeholder — bidder input]`. |
| G-007 | Partial | ISO certs listed; CVs/key personnel complete blank; subcontractor declarations "to be named". |
| G-008 | Partial | Submission method/deadline "to be confirmed"; electronic-portal commitment not confirmed. |
| G-009 | Pass | V5 states ≥180 calendar days validity. |
| G-010 | Pass | WAISL incumbent since 30-Sep-2019 CA; >5 yrs met. |
| G-011 | Partial | ≥2 comparable deployments; only 1 (RGIA) evidenced — declared shortfall. |
| G-012 | Pass | ISO 9001:2015 held. |
| G-013 | Pass | ISO/IEC 27001:2013 held. |
| G-014 | Ambiguous | Binding threshold is unfilled `[X] crore` in RFP; proposal "Cannot confirm" — value undefined in source itself. |
| G-015 | Fail | No insolvency/legal-dispute declaration; not addressed. |
| G-016 | Partial | INR excl GST + table structure + assumptions committed; pricing unpopulated. |
| G-017 | Partial | 3-stage evaluation acknowledged but conditional on R-001 procurement framing. |
| G-018 | Partial | Weights referenced (Commercial 15% stated); full 30/25/20/15/10 asserted in RTM, conditional on R-001. |
| G-019 | Pass | SBOM committed in V5. |
| G-020 | Partial | D-01 acknowledged; BEP gated on Appendix B "[To be completed by DIAL]". |
| G-021 | Pass | D-02 airborne LiDAR point cloud, DTM, DSM, orthophoto committed. |
| G-022 | Partial | Accuracy report implied; ISO 19115 metadata conformance not mentioned. |
| G-023 | Pass | D-04 indoor LiDAR datasets committed. |
| G-024 | Pass | D-05 IFC-compliant BIM to LOD 200–350 committed. |
| G-025 | Partial | D-06 Asset Attribute Register; CAFM/CMMS import not explicitly confirmed. |
| G-026 | Partial | D-07 migration report + data quality report mentioned in Component 2; not detailed as deliverable. |
| G-027 | Partial | D-08 DT platform acknowledged; UAT sign-off not explicitly detailed. |
| G-028 | Partial | D-09 BMS/IoT integration report acknowledged; "all points verified" not confirmed. |
| G-029 | Partial | D-10 AI platform acknowledged; "all agents operational" conditional on agent waves. |
| G-030 | Partial | D-11 API docs acknowledged; integration test reports not detailed. |
| G-031 | Partial | D-12 cybersecurity report + pen test tied to D-12; report content not detailed. |
| G-032 | Partial | D-13 training materials acknowledged; not detailed. |
| G-033 | Partial | D-14 as-built docs acknowledged; not detailed. |
| G-034 | Partial | D-15 PIR acknowledged; 90-day window not specified. |
| G-035 | Pass | IFC 4.0 (ISO 16739) committed. |
| G-036 | Pass | ISO 19650 "Full" compliance committed (asserted). |
| G-037 | Fail | PAS 1192-2:2013 + BS EN ISO 19650-2:2019 not mentioned. |
| G-038 | Partial | BEP/AIR compliance gated on DIAL-issued Appendix B "[To be completed by DIAL]". |
| G-039 | Pass | RTM present in appendix mapping R-001..R-135. |
| G-040 | Pass | Airborne LiDAR airport + Aerocity + 5 km buffer, ~200+ sq km committed. |
| G-041 | Pass | Core ≥20 pts/m² — "Match". |
| G-042 | Partial | Buffer 8 pts/m² "Match, pending DIAL confirmation" — weakening phrase. |
| G-043 | Pass | Horizontal RMSE ≤5 cm — Match. |
| G-044 | Pass | Vertical RMSE ≤3 cm — Match. |
| G-045 | Pass | Orthophoto GSD ≤5 cm — Match. |
| G-046 | Partial | Point cloud committed; ASPRS LAS 1.4 format not specified. |
| G-047 | Pass | DTM/DSM 10 cm grid — Match. |
| G-048 | Partial | Contour interval not in commitments table; 10 cm contours only implied via G-049. |
| G-049 | Fail | 3D mesh models (OBJ/FBX) + 10 cm contours not addressed. |
| G-050 | Fail | Flight report / sensor calibration / GCP survey report not addressed. |
| G-051 | Fail | ESRI ArcGIS / Autodesk format compatibility not addressed. |
| G-052 | Partial | Landside coverage mentioned generically; 225 acres, DEM, 3×3 m spot levels not confirmed. |
| G-053 | Fail | Underground utility scanning (GPR+DGPS+GNSS+12D) not addressed; all four binding. |
| G-054 | Fail | Landside GIS 10-layer catalogue not addressed. |
| G-055 | Fail | Airside layer-wise scanning not detailed. |
| G-056 | Fail | Airside GIS NAVAID layers not addressed. |
| G-057 | Partial | Terminal coverage/building mapping mentioned via BIM; updates/additions not detailed. |
| G-058 | Partial | Indoor mobile+terrestrial LiDAR committed; "all structures" enumeration not given. |
| G-059 | Pass | Indoor positional RMSE ≤5 cm — Match. |
| G-060 | Fail | Indoor-to-airborne coordinate registration not addressed. |
| G-061 | Pass | LOD 200–350 per 10-category BIM standards — Match. |
| G-062 | Partial | T1 BIM mentioned; specific floor areas (17085/77581/43228/64007/11495) not restated. |
| G-063 | Partial | T2 BIM mentioned; areas (27028/2061/33429) not restated. |
| G-064 | Pass | T3 ~588,000 m² referenced (≈ binding 588,158). |
| G-065 | Partial | Building-specific LOD schedule gated on Appendix A "[To be completed by DIAL]". |
| G-066 | Partial | Legacy CAD audit + CAD-to-BIM + data quality report mentioned; CAFM/CMMS population not fully detailed. |
| G-067 | Partial | GIS-BIM integration asserted; interactive pop-ups / multi-scale viz not detailed. |
| G-068 | Partial | Federated BIM with clash detection, version control, RBAC, CDE, API asserted; native IFC/ISO 19650 not separately evidenced. |
| G-069 | Partial | Outdoor 3D GIS platform listed; NL query for GIS committed; redlining/sharing not detailed. |
| G-070 | Partial | Declared GAP — no land/space-management module with DIAL legal vocabulary evidenced. |
| G-071 | Partial | Single-platform unification asserted via RGIA 40+ systems; full system list coverage asserted not detailed. |
| G-072 | Fail | Pre-maintenance/planning (terrain, soil, noise, flood, evacuation) not addressed; environmental flagged as gap. |
| G-073 | Pass | 40 pump sensors + 12 T1 roof sensors + DGA referenced. |
| G-074 | Fail | Environmental monitoring (Shahabad MdPur, NMT, Nursery CAQM) not addressed. |
| G-075 | Partial | Core 3D viewer committed; AR/VR + full offline-mobile responsiveness asserted not evidenced. |
| G-076 | Pass | Full protocol list (BACnet/IP, MSTP, Modbus TCP/RTU, MQTT, SNMP, OPC-UA, REST) committed. |
| G-077 | Partial | DTDL asserted; BMS→BIM mapping grounded; geofencing/zone monitoring not mentioned. |
| G-078 | Partial | APOC/CCC REST/GraphQL/WebSocket committed; third-party airline/Smart City platforms not detailed. |
| G-079 | Pass | ≥2 major versions backward compatibility stated. |
| G-080 | Partial | REST/GraphQL/WebSocket versioned; OpenAPI 3.0 interactive portal not mentioned. |
| G-081 | Partial | Only 5 default roles listed; 10 additional register roles (AOCC, P&E, etc.) not addressed. |
| G-082 | Pass | SSO SAML 2.0/OAuth 2.0 + MFA committed. |
| G-083 | Pass | TLS 1.3 adopted (BRD overrides register TLS 1.2+). |
| G-084 | Pass | AES-256 at rest committed. |
| G-085 | Pass | ≥2-year activity audit log retention committed. |
| G-086 | Partial | Risk assessment, segmentation, pen test asserted; IEC 62443 declared GAP; SOC/SIEM declared GAP. |
| G-087 | Pass | AI orchestration engine described (data routing, alert aggregation, zero-downtime versioning). |
| G-088 | Pass | 8 agents adopted per BRD §3.5.3. |
| G-089 | Pass | Mech & HVAC agent scope + performance detailed. |
| G-090 | Pass | Electrical agent detailed; DGA conditional on MRSS upgrade noted. |
| G-091 | Pass | Fire Safety agent detailed; advisory-only framing preserved. |
| G-092 | Partial | Water & Drainage agent scoped; no performance target (acknowledged source-doc gap). |
| G-093 | Pass | Energy Management agent detailed. |
| G-094 | Pass | Passenger Flow agent detailed. |
| G-095 | Partial | Structural Integrity agent conditional on DIAL SHM sensor procurement + 6–12 mo baseline (non-mandatory). |
| G-096 | Pass | Security & Perimeter agent detailed; CISF-approval dependency flagged. |
| G-097 | Partial | Broader NL-query-over-platform interpretation flagged as open; narrower GIS-NL line item committed. |
| G-098 | Partial | Explainability + confidence committed; SHAP/LIME/attention technique mandate caveated as RFP-only. |
| G-099 | Pass | Complete AI audit log committed. |
| G-100 | Pass | Feedback loop committed. |
| G-101 | Pass | Model version control + 4 hr rollback committed. |
| G-102 | Pass | DIAL ownership of model weights/training data committed. |
| G-103 | Partial | Data Readiness Gate described; ≥12 mo usable history not specified. |
| G-104 | Pass | Shared AI Platform (historian, feature store, MLflow, explainability, alert pipeline) described. |
| G-105 | Pass | MLOps (monthly drift, quarterly retrain, DIAL approval, 90-day KPI) described. |
| G-106 | Pass | Per-agent acceptance on rolling 90-day window described. |
| G-107 | Pass | ≥82/78/72 h/30 s stated. |
| G-108 | Pass | ≥80/75/48 h/30 s stated. |
| G-109 | Pass | ≥85/80/45 min/15 s stated. |
| G-110 | Partial | ≥90/85/7 d/60 s stated but agent is conditional on SHM procurement. |
| G-111 | Pass | ≥95/95/real-time/5 s stated. |
| G-112 | Pass | ≥80/75/24 h/60 s stated. |
| G-113 | Pass | ≥88/82/15 min/10 s stated. |
| G-114 | Pass | Aggregate ≥80%/75% floor committed. |
| G-115 | Partial | T1 OT integration asserted with point counts; LCMS conditional; full system set asserted not individually evidenced. |
| G-116 | Partial | T2 OT integration declared TBD/X by register — flagged to DIAL. |
| G-117 | Partial | T3 OT integration asserted with point counts; not all systems individually evidenced. |
| G-118 | Partial | Common OT (WTP/STP/MRSS/Solar/AGL CMS/ITBMS) asserted; noise monitoring + access control not mentioned. |
| G-119 | Partial | LCMS/ECMS T3 + VDGS/MRSS upgrade dependencies flagged; conditional on OEM upgrade. |
| G-120 | Partial | IT/OneAPOC integrations flagged as scope-boundary unclear — declared gap. |
| G-121 | Fail | Ops DT Airside ops not addressed. |
| G-122 | Fail | Ops DT Terminal ops not addressed. |
| G-123 | Fail | Ops DT Curbside not addressed. |
| G-124 | Fail | Ops DT Security not addressed. |
| G-125 | Fail | Ops DT summary KPIs + facility roll-up not addressed. |
| G-126 | Fail | OT/IT asset widgets not addressed. |
| G-127 | Fail | DT visualization (desktop GPU + Web-GL) not addressed. |
| G-128 | Fail | IT asset visualization cap =3000 not addressed. |
| G-129 | Fail | Multi-level navigation not addressed. |
| G-130 | Fail | OT asset visualization LOD 350 not addressed. |
| G-131 | Fail | Asset registry & modeling (CLG/CAI) not addressed. |
| G-132 | Fail | Asset federation not addressed. |
| G-133 | Partial | Simulation engine asserted as IROPs/Decision-Engine precedent; "full 24-use-case not built" — declared. |
| G-134 | Partial | SPG use cases (10/8/5) flagged as GAP/illustrative; coverage incomplete (non-mandatory). |
| G-135 | Partial | ABR departmental asks mapped; several flagged adjacent/gap (fog nav, DigiYatra, space-allocation). |
| G-136 | Pass | 5-phase programme committed. |
| G-137 | Pass | ~3 months/phase (~15 mo) committed. |
| G-138 | Pass | M1–M6 = 15/10/20/25/20/10 committed. |
| G-139 | Pass | 14-calendar-day review/sign-off committed. |
| G-140 | Partial | End-to-end delivery responsibility implied; not explicitly stated as a binding commitment. |
| G-141 | Partial | Integration responsibility implied; not explicitly stated. |
| G-142 | Partial | SLA/material-default framework accepted; penalty-formula numbers placeholder. |
| G-143 | Pass | India-only data sovereignty + DIAL exclusive data + no external training committed. |
| G-144 | Pass | ≤12 h breach notification + vendor bears costs committed. |
| G-145 | Pass | ≥6-month transition support at no cost committed. |
| G-146 | Pass | WAISL incumbent under BCAS/AAI approvals since 2019; obtains/maintains at own cost. |
| G-147 | Partial | RACI structure committed; DEC/POD undefined; skeleton only. |
| G-148 | Partial | DIAL reserved rights not explicitly acknowledged (non-mandatory procedural). |
| G-149 | Pass | DIAL exclusive IP on deliverables + SBOM committed. |
| G-150 | Pass | 12-month warranty + AMC committed. |
| G-151 | Partial | 5-year O&M committed; comprehensive plan (upgrades, reporting, data lifecycle) light. |
| G-152 | Partial | Modular cloud-native committed; HA/DR not detailed beyond RTO/RPO. |
| G-153 | Partial | 15-year design life not explicitly committed — RTM flags "no explicit 15-year commitment evidenced." |
| G-154 | Partial | Training/KT/docs mentioned; comprehensiveness not evidenced. |
| G-155 | Pass | ≥5-year BMS historical retention committed. |
| G-156 | Pass | ≥5-year AI audit log retention committed. |
| G-157 | Pass | ≤4 h model rollback committed. |
| G-158 | Pass | ≥99.5% uptime — Match. |
| G-159 | Pass | ≤5 s latency — Match. |
| G-160 | Pass | 100% BIM LOD compliance — Match. |
| G-161 | Pass | 100% integration coverage within 3 months — Match. |
| G-162 | Pass | ≤10 min critical incident response — Match (BRD overrides RFP ≤1 h). |
| G-163 | Pass | ≤12 h breach notification committed. |
| G-164 | Pass | ≥3 breaches/quarter material-default threshold accepted. |
| G-165 | Pass | ≥6-month transition support committed. |
| G-166 | Pass | 40 machine-room pump sensors referenced. |
| G-167 | Pass | 12 T1 roof water-level sensors referenced. |
| G-168 | Pass | RTO ≤4 h committed. |
| G-169 | Pass | RPO ≤24 h committed. |
| G-170 | Pass | 24×7 support committed. |
| G-171 | Fail | ≥3 case studies; only 1 evidenced + 2 placeholders. |
| G-172 | Pass | Horizontal RMSE ≤5 cm — Match. |
| G-173 | Pass | Vertical RMSE ≤3 cm — Match. |
| G-174 | Pass | ~200 sq km survey area committed. |
| G-175 | Fail | 225-acre underground utility scanning area not addressed. |
| G-176 | Pass | ~5,000+ acre campus referenced. |
| G-177 | Partial | T1 total area ~213,396 sq m not restated/confirmed. |
| G-178 | Partial | T2 total area ~62,519 sq m not restated/confirmed. |
| G-179 | Pass | T3 ~588,000 sq m referenced (≈ binding 588,158). |
| G-180 | Pass | T3 HVAC ~54,000 pts stated. |
| G-181 | Pass | T3 FDAS ~65,000 pts stated. |
| G-182 | Pass | T1 HVAC 20,000 pts stated. |
| G-183 | Pass | T1 FDAS 17,400 pts stated. |
| G-184 | Pass | MRSS 60,000 tags stated. |
| G-185 | Pass | T3 ECMS ~66,000 tags stated. |
| G-186 | Fail | T1 ECMS 20,000 tags not addressed. |
| G-187 | Partial | T2 FDAS 5,000 pts — T2 scope declared TBD by register. |
| G-188 | Partial | T3 BHS 1,300 pts — BHS integration mentioned; point count not stated. |
| G-189 | Pass | 19 OT systems referenced (PE_OT). |

---

## 4. Numeric Parity Sub-Table

Binding values per gold inventory §2. Proposal value "not stated" = the figure could not be located in the proposal text.

| G-ID | Parameter | Binding | Operator | Proposal value | Ratio / Delta | Verdict |
|---|---|---|---|---|---|---|
| G-009 | Proposal validity | 180 | ≥ days | 180 | = | Pass |
| G-018 | Eval weight Technical | 30 | = % | asserted 30 (conditional on R-001) | — | Partial |
| G-018 | Eval weight Experience | 25 | = % | asserted 25 (conditional) | — | Partial |
| G-018 | Eval weight AI | 20 | = % | asserted 20 (conditional) | — | Partial |
| G-018 | Eval weight Commercial | 15 | = % | 15 stated in V1 | — | Partial |
| G-018 | Eval weight Implementation | 10 | = % | asserted 10 (conditional) | — | Partial |
| G-041 | LiDAR density (boundary) | 20 | ≥ pts/m² | 20 | = | Pass |
| G-042 | LiDAR density (buffer) | 8 | ≥ pts/m² | 8 ("pending DIAL confirmation") | = but conditional | Partial |
| G-043 | Horizontal RMSE | 5 | ≤ cm | 5 | = | Pass |
| G-044 | Vertical RMSE | 3 | ≤ cm | 3 | = | Pass |
| G-045 | Orthophoto GSD | 5 | ≤ cm | 5 | = | Pass |
| G-047 | DTM/DSM grid | 10 | = cm | 10 | = | Pass |
| G-048 | Contour interval | 10 | = cm | not stated | — | Partial |
| G-059 | Indoor positional RMSE | 5 | ≤ cm | 5 | = | Pass |
| G-079 | API backwards compat | 2 | ≥ major ver | 2 | = | Pass |
| G-083 | TLS version | 1.3 | = | 1.3 | = | Pass |
| G-084 | Encryption at rest | AES-256 | = | AES-256 | = | Pass |
| G-085 | Activity audit log retention | 2 | ≥ years | 2 | = | Pass |
| G-088 | Mandatory AI agents | 8 | = count | 8 | = | Pass |
| G-107 | Mech&HVAC p/r/hor/lat | 82/78/72/30 | ≥/≥/≤/≤ | 82/78/72h/30s | = | Pass |
| G-108 | Electrical p/r/hor/lat | 80/75/48/30 | ≥/≥/≤/≤ | 80/75/48h/30s | = | Pass |
| G-109 | Passenger Flow p/r/hor/lat | 85/80/45/15 | ≥/≥/≤/≤ | 85/80/45min/15s | = | Pass |
| G-110 | Structural p/r/hor/lat | 90/85/7/60 | ≥/≥/≤/≤ | 90/85/7d/60s (conditional) | = but conditional | Partial |
| G-111 | Fire Safety p/r/hor/lat | 95/95/rt/5 | ≥/≥/=/≤ | 95/95/rt/5s | = | Pass |
| G-112 | Energy p/r/hor/lat | 80/75/24/60 | ≥/≥/≤/≤ | 80/75/24h/60s | = | Pass |
| G-113 | Security p/r/hor/lat | 88/82/15/10 | ≥/≥/≤/≤ | 88/82/15min/10s | = | Pass |
| G-114 | Aggregate alert accuracy | 80/75 | ≥/≥ % | 80/75 | = | Pass |
| G-128 | IT asset visualization cap | 3000 | = units | not stated | — | Fail |
| G-137 | Phase duration | 3 | ~ mo/phase | 3 | = | Pass |
| G-138 | Payment milestones M1–M6 | 15/10/20/25/20/10 | = % | 15/10/20/25/20/10 | = | Pass |
| G-139 | Deliverable review period | 14 | = days | 14 | = | Pass |
| G-150 | Warranty period | 12 | ≥ months | 12 | = | Pass |
| G-153 | Platform design life | 15 | ≥ years | not committed | — | Partial |
| G-155 | BMS data retention | 5 | ≥ years | 5 | = | Pass |
| G-156 | AI audit log retention | 5 | ≥ years | 5 | = | Pass |
| G-157 | AI model rollback | 4 | ≤ hours | 4 | = | Pass |
| G-158 | Platform uptime | 99.5 | ≥ % | 99.5 | = | Pass |
| G-159 | Real-time latency | 5 | ≤ s | 5 | = | Pass |
| G-160 | BIM LOD compliance | 100 | = % | 100 | = | Pass |
| G-161 | Integration coverage | 100 | = % within 3 mo | 100 | = | Pass |
| G-162 | Incident response (critical) | 10 | ≤ min | 10 | = | Pass |
| G-163 | Breach notification | 12 | ≤ hours | 12 | = | Pass |
| G-164 | Material-default threshold | 3 | ≥ breaches/Q | 3 | = | Pass |
| G-165 | Transition support | 6 | ≥ months | 6 | = | Pass |
| G-166 | IoT machine-room pumps | 40 | = units | 40 | = | Pass |
| G-167 | T1 roof sensors | 12 | = units | 12 | = | Pass |
| G-168 | RTO | 4 | ≤ hours | 4 | = | Pass |
| G-169 | RPO | 24 | ≤ hours | 24 | = | Pass |
| G-170 | Service & support | 24x7 | = | 24x7 | = | Pass |
| G-171 | Min case studies | 3 | ≥ count | 1 | 0.33× binding | Fail |
| G-172 | Geospatial H RMSE (KPI 5) | 5 | ≤ cm | 5 | = | Pass |
| G-173 | Geospatial V RMSE (KPI 5) | 3 | ≤ cm | 3 | = | Pass |
| G-174 | Airborne LiDAR total area | 200 | ~ sq km | ~200+ | ≈ | Pass |
| G-175 | Underground utility area | 225 | = acres | not stated | — | Fail |
| G-176 | Airport campus area | 5000 | ~ acres | ~5,000+ | ≈ | Pass |
| G-177 | T1 BIM total area | 213396 | ~ sq m | not restated | — | Partial |
| G-178 | T2 BIM total area | 62519 | ~ sq m | not restated | — | Partial |
| G-179 | T3 BIM total area | 588158 | ~ sq m | ~588,000 | ≈ | Pass |
| G-180 | T3 HVAC points | 54000 | = pts | ~54,000 | ≈ | Pass |
| G-181 | T3 FDAS points | 65000 | = pts | ~65,000 | ≈ | Pass |
| G-182 | T1 HVAC points | 20000 | = pts | 20,000 | = | Pass |
| G-183 | T1 FDAS points | 17400 | = pts | 17,400 | = | Pass |
| G-184 | MRSS points | 60000 | = pts | 60,000 | = | Pass |
| G-185 | T3 ECMS tags | 66000 | = tags | ~66,000 | ≈ | Pass |
| G-186 | T1 ECMS tags | 20000 | = tags | not stated | — | Fail |
| G-187 | T2 FDAS points | 5000 | = pts | not stated (T2 TBD) | — | Partial |
| G-188 | T3 BHS points | 1300 | = pts | not stated (BHS mentioned) | — | Partial |
| G-189 | OT systems count | 19 | = systems | 19 | = | Pass |

**Numeric parity summary:** of 63 unique numeric G-IDs (G-018 comprises 5 evaluation-weight components): Pass 47, Partial 10, Fail 4 (G-128, G-171, G-175, G-186). Where the proposal states a numeric commitment, it overwhelmingly matches the binding value (often literal "Match"). The numeric failures are omissions (value not located) rather than below-binding figures, except G-171 (1 vs ≥3 case studies = 0.33× binding).

---

**End of gold score — Track B.**