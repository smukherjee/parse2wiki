# Coverage Matrix — Airport Eye APOC Phase 2 (Track B)

Stage 2 of the automated pipeline (collateral-analyzer → **requirements-mapper** → section-drafter → empathy-reviewer → proposal-assembler → external scoring). Reads `brief.md` and `gap-report.md` from Stage 1, and re-reads the five binding requirements sources directly, in priority order:

1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` (CR/BRD v1.5, DIAL-AE-BRD-001, 05-Jun-2026) — **binding, highest priority**
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` (ABR) — overrides base RFP on conflict
3. `PE_OT System_09.06.pptx.md` — final/authoritative OT-systems inventory
4. `Airport_Eye_RFP_v5.docx.md` — base RFP, superseded on conflict
5. `AirportEye_Requirements_Register_v5.xlsx.md` and `Final requirements.xlsx.md` — granular registers

**Excluded per task instruction, not read or used anywhere below:** `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`, `AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`.

**Legend — Classification:** Grounded (direct evidence in our collateral) · Assertable (reasonable claim, mark `[ASSERTION]`) · Gap (cannot be credibly addressed without more evidence).
**Legend — Gap Severity:** Disqualifying (mandatory + no evidence + no credible assertion — bid/no-bid-level) · Manageable (preferred, or alternative approach available) · Addressable (evidence likely exists, wasn't provided — go get it).
**Legend — Type:** M = Mandatory (shall/must), P = Preferred (should/may/scored), I = Implicit (evaluation-criteria/SOW/repeated-theme-driven, no obligation language in source).

**AI-agent roster note (per task instruction — not silently resolved):** The BRD's §3.5.3 table names exactly 8 agents. RFP v5's own body text (§6.3) explicitly describes only 6 of those 8 (no subsection for Passenger Flow or Structural Integrity — confirmed by direct re-read: §6.3.1, .2, .4, .5, .6, .7 exist; §6.3.3 is a numbering gap with no corresponding text). RFP v5's own performance table (§6.5) scores 7 agents (adds Passenger Flow and Structural Integrity, but — like the BRD — omits Water & Drainage entirely). The BRD/RFP v5 commercial Table 6 prices only 5 of the 8 named types as a single lump sum ("Generic and Configurable AI Agent — Mechanical & HVAC, Electrical, Fire Safety, Security and Perimeter, Water and Drainage"), leaving Energy Management, Passenger Flow, and Structural Integrity unpriced. The requirements registers carry 17 `AI-*` rows (AI-01–AI-17): 6 are platform/governance items (AI-01, 02, 03, 04, 05, 17), 11 are agent-functional rows (AI-06–AI-16) that collapse onto the BRD's 8 named agents (AI-06/07/08/09 are four sub-facets of the Mechanical&HVAC / Energy Management pairing) **except AI-10, a Natural-Language Query Agent with no named counterpart in the BRD's 8-agent table** — though a narrower "GIS Data Viewer... with Natural Language Query Capabilities" line item does appear as a priced deliverable in BRD/RFP v5 Table 1 / Section 1, so this may be a scope-boundary/naming question rather than a pure addition. A stale prior proposal (v9, May-2025) committed to only 7 agents and must not be reused. **This matrix treats the BRD's 8-agent table as the authoritative roster (per the task's binding-priority order), classifies each of the 8 individually, tracks AI-10 as a distinct flagged item, and does not average, blend, or silently pick a different count.**

---

## 0. Procurement Mechanism, Evaluation Framework, Submission & Pre-Qualification

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-001 | Whether this is a competitively scored RFP (RFP v5: 3-stage panel, weighted scoring, 7-volume/page-limited submission, pre-qualification gates) or a negotiated Change Request to incumbent WAISL under the 2019 CA (BRD §1.2: "the Concessionaire is requested to submit its quotation in accordance with the provisions of the Concession Agreement") | I | Gap — unresolved contradiction between binding sources, confirmed by direct re-read of both documents | Neither document states the other is superseded on this specific point | **Disqualifying** (misdirects every downstream structural choice) | Escalate — bid/no-bid-equivalent decision before drafting; safest default is to draft against RFP v5's fuller structure (a formal submission is a strict superset) while explicitly labeling the assumption |
| R-002 | Evaluation weights: Technical Approach 30% / Experience 25% / AI Capability 20% / Commercial 15% / Implementation 10% (RFP v5 §9.2, confirmed by direct re-read) | P | Assertable — structure exists and is unambiguous in RFP v5, but its applicability under the CR framing is unconfirmed | No source reconciles this with R-001 | Manageable | Assert with caveat: treat as operative pending R-001 resolution |
| R-003 | 3-stage evaluation: mandatory compliance → technical → commercial, multi-disciplinary panel (RFP v5 §9.1) | P | Assertable, same caveat as R-002 | — | Manageable | Assert with caveat |
| R-004 | 7-volume submission structure (Exec Summary, Technical, AI/Analytics, Implementation, Commercial, Qualifications/References, Appendices) (RFP v5 §9.3, confirmed by direct re-read) | M (per RFP v5) | Assertable, same R-001 caveat | — | Manageable | Follow as structural default per gap-report recommendation; flag assumption in cover material |
| R-005 | Volume 1 page limit: maximum 10 pages (RFP v5 §9.3); no page limits stated for Volumes 2–7 | M | Assertable | — | Manageable | Comply with the one stated limit; note absence of others rather than inventing limits |
| R-006 | Minimum 5 years' demonstrated experience in digital twin/BIM/geospatial (RFP v5 Appendix E) | M | Grounded | WAISL is the incumbent Concessionaire since the 30-Sep-2019 CA — well over 5 years by any reading | — | Cite and ground |
| R-007 | Evidence of ≥2 comparable deployments in airport/transport infrastructure/large-scale built environment (RFP v5 Appendix E) | M | **Gap** | Only RGIA (Hyderabad) is fully evidenced; Consolidated FINAL proposal marks 2 of 3 case-study slots as placeholder | **Disqualifying** if R-001 resolves to competitive framing | Seek additional comparable-deployment evidence before proposal-assembler stage; escalate if none found |
| R-008 | ISO 9001:2015 QMS certification, current and valid (RFP v5 Appendix E) | M | Grounded | WAISL holds ISO 9001 (per brief Evidence Map) | — | Cite and ground |
| R-009 | ISO/IEC 27001:2013 Information Security Management certification (RFP v5 Appendix E) | M | Grounded | WAISL holds ISO 27001 | — | Cite and ground |
| R-010 | Annual turnover ≥ INR [X] crore in each of last 3 FY, audited accounts (RFP v5 Appendix E) | M | Gap | Figure is an unfilled placeholder in the source document itself, not an evidence gap on our side | Addressable | Seek the actual threshold from DIAL/procurement before compliance response |
| R-011 | Proposal validity: minimum 180 calendar days from submission (RFP v5 §9.1) | M | Assertable | Standard commercial commitment, no barrier | — | Assert |

## 1. Vision, Objectives, and KPIs

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-012 | Platform Uptime ≥ 99.5% (excl. planned maintenance) (BRD §2.3 KPI-1, cross-confirmed RFP v5, both registers) | M | Grounded | Consolidated FINAL proposal matches; best-evidenced figure in the corpus | — | Cite and ground (BRD KPI table as authoritative source) |
| R-013 | Real-time data latency ≤ 5 seconds sensor-to-dashboard (BRD §2.3 KPI-2) | M | Grounded | Same as above | — | Cite and ground |
| R-014 | BIM Model LOD Compliance 100% of specified assets (BRD §2.3 KPI-3) | M | Grounded | Same as above | — | Cite and ground |
| R-015 | Predictive Alert Accuracy ≥ 80% precision / ≥ 75% recall, platform-wide (BRD §2.3 KPI-4) | M | Grounded | Same as above; also the register's MLOps row (AI-05) restates this exact figure | — | Cite and ground |
| R-016 | Geospatial Data Accuracy: Horizontal ≤ 5cm RMSE, Vertical ≤ 3cm RMSE (BRD §2.3 KPI-5) | M | Grounded | Same as above | — | Cite and ground |
| R-017 | Incident Response Time (Critical) ≤ 10 minutes from notification (BRD §2.3 KPI-6, register NFR, Consolidated FINAL) | M | Grounded | Triple-confirmed by direct re-read; **RFP v5's own KPI table states a materially different ≤1 hour figure for the same metric elsewhere in the same corpus** — do not use; two of three older prior proposals also carry stale/incompatible figures (≤1hr; a 30/60/90-min P1–P4 ladder) that must not be reused | — | Cite and ground at ≤10 min only; explicitly instruct drafter to treat ≤1hr and the P1–P4 ladder as superseded, not to average |
| R-018 | System Integration Coverage: 100% of agreed BMS/IoT data points within 3 months of go-live (BRD §2.3 KPI-7) | M | Grounded | Cross-confirmed by direct re-read of BRD Appendix C SLA table | — | Cite and ground |
| R-019 | Six primary objectives (geospatial foundation, compliant BIM, real-time BMS/IoT integration, agentic AI monitoring, APOC/CCC/Smart City integration, scalable future-proof platform) (BRD §2.2) | M | Grounded | Consolidated FINAL narrative addresses all six | — | Cite and ground |
| R-020 | Minimum 15-year operational lifecycle, modular cloud-native/hybrid design (BRD Objective 6, §1.2) | M | Assertable | Architecture direction plausible from Evidence Map's two-layer description; no explicit 15-year lifecycle commitment evidenced | — | Assert with caveat |

## 2. Geospatial / LiDAR / BIM Foundation

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-021 | Airborne LiDAR core density ≥ 20 pts/m² within airport boundary (BRD §3.1.1, RFP v5 §3.1) | M | Grounded | Consolidated FINAL matches | — | Cite and ground |
| R-022 | Buffer-zone LiDAR density 8 pts/m² (BRD §3.1.1) | M | Assertable | Consolidated FINAL itself annotates this figure "pending DIAL confirmation" — not fully settled even in our newest document | — | Assert with caveat; flag as open item pending DIAL confirmation |
| R-023 | Horizontal accuracy RMSE ≤ 5cm vs GCPs (BRD §3.1.1) | M | Grounded | — | — | Cite and ground |
| R-024 | Vertical accuracy RMSE ≤ 3cm vs benchmarks (BRD §3.1.1) | M | Grounded | — | — | Cite and ground |
| R-025 | RGB orthophotography GSD ≤ 5cm (BRD §3.1.1) | M | Grounded | — | — | Cite and ground |
| R-026 | DTM/DSM at 10cm grid resolution (BRD §3.1.1) | M | Grounded | — | — | Cite and ground |
| R-027 | Indoor LiDAR positional accuracy ≤ 5cm RMSE post cloud-to-cloud registration (BRD §3.1.5) | M | Grounded | Same figure as outdoor, Consolidated FINAL covers | — | Cite and ground |
| R-028 | Indoor scanning density [X] pts/m² at internal surfaces (RFP v5 §3.2.1 only — not present in BRD) | M (per RFP v5) | Gap | Unfilled placeholder in the source document itself | Addressable | Flag as unfilled in source; do not treat as a settled figure |
| R-029 | LOD 200–350 per asset category, 10-category BIM standards table (BRD §3.1.8, RFP v5 §3.2.3, identical) | M | Grounded | Consolidated FINAL matches | — | Cite and ground |
| R-030 | Full ISO 19650 compliance (BRD Objective 2, RFP v5 §3.2.2) | M | Assertable | GEOKNO is asserted BIM/LiDAR delivery partner; no named ISO 19650-specific compliance evidence cited | — | Assert with caveat |
| R-031 | IFC 4.0 (ISO 16739) open BIM data exchange (RFP v5 §3.2.2) | M | Assertable | Industry-standard capability for a BIM delivery partner; no specific certification cited | — | Assert |
| R-032 | Appendix A — Schedule of Buildings/Areas for BIM Modelling ("[To be completed by DIAL]") underlies all area-based BIM/LiDAR costing (BRD Appendix A) | M | Gap | Genuinely unavailable in any form reviewed | Addressable | Seek from DIAL before commercial costing is finalized |

## 3. GIS–BIM Integration & Federated BIM Platform (Phase 2)

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-033 | Automated clash detection and resolution, concurrent multi-discipline coordination (BRD §3.2.3, RFP v5 §3.3.2) | M | Assertable | Standard federated-BIM capability; no named evidence | — | Assert |
| R-034 | Version control, change management, full audit trail for BIM CDE (BRD §3.2.3) | M | Assertable | — | — | Assert |
| R-035 | Role-based access control for internal staff/contractors/consultants on BIM platform (BRD §3.2.3) | M | Assertable | RBAC evidenced elsewhere (DT viewer §3.4.4) but not specifically for the BIM CDE | — | Assert |
| R-036 | API-based integration between federated BIM platform, Digital Twin viewer, and AI monitoring platform (BRD §3.2.3) | M | Grounded | Consolidated FINAL's two-layer Geo Digital Twin + Operational Digital Twin/AIOP architecture directly addresses this | — | Cite and ground |
| R-037 | Legacy CAD/DWG migration to IFC-compliant BIM, Data Quality Report (BRD §3.2.1, RFP v5 §3.3.1) | M | Assertable | Adjacent — RGIA engagement plausibly included similar migration work, not specifically evidenced | — | Assert with caveat |
| R-038 | Appendix B — BIM Execution Plan (BEP) Requirements ("[To be completed by DIAL]") (BRD Appendix B) | M | Gap | Unavailable in any form | Addressable | Seek from DIAL |

## 4. Facilities Maintenance Management (Phase 3)

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-039 | Digital footprint of all land/space with full attribute detail, including "demised premises / additional demised premises / excluded premises / carved-out assets / MCD and DCB area bifurcation" classification (BRD §3.3.1) | M | Gap | No land/space-management module evidenced anywhere in our collateral | Addressable | Seek evidence; if drafted, mirror DIAL's exact legal/facilities vocabulary per brief's Vocabulary Notes |
| R-040 | Integration with a CLM (contract lifecycle management) tool (BRD §3.3.1) | M | Gap | No named CLM integration evidence | Addressable | Seek evidence |
| R-041 | Single platform integrating BMS/LCMS/ECMS/CMS/FDAS/BHS/HBS/VDGS/VHT/ATRS/DFMD/PBB/WTP-STP/AGL-CMS/IoT (BRD §3.3.2) | M | Grounded | Consolidated FINAL's RGIA proof point (40+ integrated systems, "hub-and-spoke" fabric) is a direct analog for this multi-system unification claim | — | Cite and ground via RGIA precedent |
| R-042 | IoT sensor integration: 40 machine-room pump sensors (T1–T3), 12 T1 roof water-level sensors, Dissolved Gas Analysis in transformers (BRD §3.3.4) | M | Grounded | Sensor inventory is DIAL-side (PE_OT/ABR-sourced); our BMS/IoT ingestion middleware capability (§3.4.2) is the evidenced piece | — | Cite and ground the ingestion capability; sensor counts are DIAL-provided facts, not our claims |
| R-043 | Environmental monitoring: noise contours, flood zones, air quality, disaster-prone zone mapping (BRD §3.3.3, §3.3.5) | M | Assertable | Adjacent — plausible extension of the GIS platform, no named evidence of environmental-layer delivery | — | Assert with caveat |

## 5. Digital Twin Platform Architecture (Phase 4)

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-044 | Modular, cloud-native (or cloud-ready hybrid) platform architecture (BRD §3.4.1) | M | Grounded | Evidence Map's two-layer architecture description addresses this | — | Cite and ground |
| R-045 | Web 3D GIS+BIM viewer, seamless indoor/outdoor nav, AR/VR output, full mobile offline responsiveness (BRD §3.4.1) | M | Assertable (mixed) | Core 3D viewer capability is Grounded via architecture description; AR/VR and offline-mobile specifics are not independently evidenced | — | Cite and ground the viewer; assert AR/VR and offline capability with caveat |
| R-046 | BMS/IoT ingestion middleware: BACnet/IP, BACnet MSTP, Modbus TCP/RTU, MQTT v3.1.1/v5.0, SNMP, OPC-UA, REST (BRD §3.4.2) | M | Grounded | RGIA proof point (40+ systems, protocol-agnostic hub-and-spoke) | — | Cite and ground |
| R-047 | Unified semantic data model conforming to DTDL or equivalent (BRD §3.4.2) | M | Assertable | No DTDL-specific evidence cited | — | Assert |
| R-048 | Every BMS data point mapped to a corresponding BIM element for 3D spatial visualisation (BRD §3.4.2) | M | Grounded | Core to the two-layer DT architecture already evidenced | — | Cite and ground |
| R-049 | Historical BMS data archiving, minimum 5-year retention (BRD §3.4.2) | M | Grounded | Consolidated FINAL commits | — | Cite and ground |
| R-050 | APOC/CCC integration via REST/GraphQL/WebSocket, ≥2 major versions backward compatibility (BRD §3.4.3) | M | Grounded | `DIAL APOC Phase II Proposal 1.pdf.md` is a real, named prior APOC/AODB integration engagement — genuine adjacent precedent for the integration itself | — | Cite and ground the integration-experience claim only; **do not reuse that proposal's commercial figures, SLA ladder, or Singapore-hosting infrastructure language** (see R-061, R-017) |
| R-051 | MFA + RBAC with minimum 5 defined user roles (Executive, Operations, Maintenance, Security, Guest/Visitor) (BRD §3.4.4) | M | Grounded | Consolidated FINAL commits, matches BRD language exactly | — | Cite and ground |
| R-052 | SSO via SAML 2.0 or OAuth 2.0 integrated with DIAL's IdP (BRD §3.4.4) | M | Assertable | Standard capability, no named evidence | — | Assert |
| R-053 | TLS 1.3 in transit, AES-256 at rest (BRD §3.4.4) | M | Grounded (with internal source flag) | Consolidated FINAL commits to BRD's TLS 1.3 figure; note the requirements register independently states "TLS 1.2+" for the same control — a source inconsistency, not ours to resolve; BRD (binding, highest priority) governs | — | Cite and ground at TLS 1.3 / AES-256 per BRD; do not blend with the register's 1.2+ figure |
| R-054 | Full activity audit logging retained minimum 2 years (BRD §3.4.4) | M | Grounded | Consolidated FINAL commits; distinct from the 5-year AI-alert audit log (§3.5.5) and 5-year BMS historical-data log (§3.4.2) — three different logs, three different periods, not a contradiction | — | Cite and ground; keep the three retention periods distinct in drafting |
| R-055 | Outdoor 3D GIS Platform: multi-department data layering, planning/scenario visualisation, collaborative redlining, secure sharing/publishing (BRD §3.4.6) | M | Assertable | GEOKNO's GIS/LiDAR/BIM delivery role is adjacent evidence; no named evidence of the specific multi-department-layering/redlining collaboration features | — | Assert with caveat |

## 6. Cybersecurity & Data Governance

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-056 | Compliance with IEC 62443 for all OT/IT integration components (BRD §3.4.5, RFP v5 §4.2) | M | **Gap** | No IEC 62443 certification or compliance evidence found anywhere in our collateral; WAISL's ISO 27001/22301 are adjacent (information security / business continuity) but do not substitute for an ICS/OT-specific standard | Manageable (a credible compliance-roadmap commitment is plausible; would become Disqualifying if DIAL requires certification in hand at bid time) | Acknowledge gap explicitly; propose an IEC 62443 compliance roadmap or named subcontractor/partner rather than asserting certification we do not hold |
| R-057 | Network segmentation between IT/OT/internet-facing components, defence-in-depth (BRD §3.4.5) | M | Assertable | Standard practice for an OT integrator of WAISL's scale; no named evidence | — | Assert |
| R-058 | Penetration testing of internet-facing components prior to go-live (BRD §3.4.5) | M | Assertable | Standard vendor practice; tied to Deliverable D-12 | — | Assert |
| R-059 | SOC & SIEM capability for continuous security monitoring (BRD §3.4.5) | M | **Gap** | No SOC/SIEM operational track record cited anywhere in our collateral | Manageable | Acknowledge gap; propose partner/roadmap mitigation |
| R-060 | Full cybersecurity risk assessment prior to deployment, findings submitted for DIAL approval (BRD §3.4.5) | M | Assertable | Standard practice; tied to Deliverable D-12 | — | Assert |
| R-061 | Data sovereignty: all data stored/processed exclusively in India, no transfer without prior written DIAL approval, breach = material breach (BRD §9.10) | M | Grounded | Consolidated FINAL correctly commits; **`DIAL APOC Phase II Proposal 1.pdf.md`, one of our own prior proposals, proposes AWS Singapore-region DR hosting — directly contradicts this clause** | — | Cite and ground from Consolidated FINAL only; explicitly exclude the APOC Phase II proposal's hosting language from any reuse |
| R-062 | DPDP Act 2023 and applicable national data-protection legislation compliance (BRD §9.10, RFP v5 §9.6) | M | Grounded | Consolidated FINAL commits | — | Cite and ground |
| R-063 | 12-hour breach notification to DIAL (BRD §9.11) | M | Grounded | Consolidated FINAL commits, matches BRD exactly | — | Cite and ground |
| R-064 | Vendor bears all breach-related costs; negligence-caused breaches attract penalties/termination (BRD §9.11) | M | Assertable | Standard contract-term acceptance, not an evidence-based claim | — | Assert (acknowledge as accepted contractual term) |

## 7. AI Agent Architecture & Roster (Phase 5)

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-065 | Authoritative AI-agent roster and count — see roster note above | I | Assertable, with the ambiguity explicitly flagged, not resolved | BRD's 8-agent table (§3.5.3) is the most specific, most recent, binding source; RFP v5 is internally inconsistent (6 described + 7 scored); registers add AI-10 (NL Query) beyond the 8 | Manageable | Assert BRD's 8 as the working roster; explicitly flag the RFP v5 and register divergences in the draft rather than silently normalising to one count |
| R-066 | Mechanical & HVAC Monitoring Agent — AHUs, chillers, cooling towers, BAS (BRD §3.5.3; register AI-06/07/08/09 give staged go-live scope: load forecasting → waste/fault anomaly detection → degradation trending/RUL → advisory optimisation) | M | Grounded | Consolidated FINAL's 8-agent table includes this agent | — | Cite and ground; note register's 4-stage rollout detail as implementation nuance |
| R-067 | Electrical Systems Monitoring Agent — transformers, UPS, switchgear (BRD §3.5.3; register AI-11 notes DGA/insulation-failure prediction is deferred until the MRSS server upgrade) | M | Grounded | Consolidated FINAL covers | — | Cite and ground; flag the MRSS-upgrade dependency as a DIAL-side prerequisite, not a vendor gap |
| R-068 | Fire Safety & Life Safety Monitoring Agent — multi-sensor correlation, suppression monitoring, evacuation modelling (BRD §3.5.3; register AI-14 clarifies this is advisory analytics layered over, never replacing, the certified fire system) | M | Grounded | Consolidated FINAL covers | — | Cite and ground; preserve the "advisory, never replacing" framing when drafting |
| R-069 | Water & Drainage Monitoring Agent — potable/chilled/grey water, stormwater (BRD §3.5.3; register AI-12 gives go-live scope: roof alerts, pump health, leak indication, stormwater forecasting benchmarked against the Walter P Moore hydrology study) | M | Grounded (roster/scope) | Consolidated FINAL's 8-agent framing includes this agent; register AI-12 independently corroborates go-live scope even though — see R-087 — no performance target exists for it anywhere in the requirement corpus | — | Cite and ground scope; see R-087 for the separate performance-target gap |
| R-070 | Energy Management & Sustainability Agent — EUI by zone, waste detection, carbon tracking (BRD §3.5.3; register AI-06) | M | Grounded | Consolidated FINAL covers | — | Cite and ground |
| R-071 | Passenger Flow Monitoring Agent — congestion prediction, ATRS/DFMD monitoring (BRD §3.5.3; register AI-13 adds XOVIS/Kloudspot counter data sources, 45-min forecast horizon) | M | Grounded | Consolidated FINAL covers; also directly relevant to ABR Operations dept's queue-management asks (R-116) | — | Cite and ground |
| R-072 | Structural Integrity Monitoring Agent — settlement/movement analysis (BRD §3.5.3; register AI-16 flags **"CONDITIONAL SCOPE: cannot start until DIAL procures and installs the SHM sensor network," needing a further 6–12 month baseline**) | M | Assertable | Roster inclusion is Grounded (Consolidated FINAL covers the agent generically); but its actual deliverability is contingent on a DIAL-side prerequisite not guaranteed by any source | — | Assert with an explicit dependency caveat: cannot commit to a start date until DIAL's SHM sensor network exists |
| R-073 | Security & Perimeter Monitoring Agent — PSIM/access control/CCTV correlation, crowd density (BRD §3.5.3; register AI-15 flags **"all scope subject to CISF approval before build starts"**) | M | Grounded, with dependency flagged | Consolidated FINAL covers | — | Cite and ground; flag CISF approval as an external dependency |
| R-074 | Natural-Language Query Agent (register AI-10 only — no counterpart in the BRD's 8-agent table; a narrower "NL query for GIS data retrieval" line item does appear separately as a priced deliverable in BRD/RFP v5 Table 1/§3.4.6) | I | **Gap** (broader platform-wide interpretation) / Assertable (narrower GIS-only interpretation) | No evidence of an NL-query-over-full-platform-data capability (assets, telemetry, alerts, CMMS, docs) in our collateral; the GIS-only NL query capability is Grounded via the Table 1 line item | Addressable | Assert the narrower, already-priced GIS-NL-query capability; flag the register's broader AI-10 scope as an open scope-boundary question, not a silent scope addition |
| R-075 | AI Orchestration Engine — data routing, alert aggregation, priority scoring, cross-agent correlation, zero-downtime agent versioning (BRD §3.5.2; register AI-03) | M | Grounded | Matches Evidence Map's AIOP/orchestration architecture description | — | Cite and ground |
| R-076 | Data Readiness Gate — per-domain data audit before any agent build, publish Data Readiness Report, agree realistic day-1 benchmarks with DIAL (register AI-01 only — no BRD counterpart) | I | Assertable | Standard data-quality-audit practice for a competent AI vendor; not independently evidenced as a named process | — | Assert |
| R-077 | Shared AI Platform — common ingestion, historian, feature store, model registry, explainability service, alert pipeline, CMMS/AMMS connector, built once (register AI-02 only) | I | Grounded | Substantially the same claim as R-075/orchestration architecture | — | Cite and ground |
| R-078 | MLOps lifecycle — monthly drift monitoring, quarterly retraining, DIAL approval before release, rolling 90-day KPI window (register AI-05 only) | I | Assertable | Standard MLOps practice; no named evidence of this specific cadence | — | Assert |
| R-079 | Per-agent acceptance against individual §6.5 performance rows on a rolling 90-day window, tied to Milestone M5 / Deliverable D-10 (register AI-17 only) | I | Assertable | Standard acceptance-testing practice | — | Assert |

## 8. AI Agent Performance Standards

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-080 | Mechanical & HVAC Agent: ≥82% precision, ≥78% recall, up to 72hr prediction horizon, ≤30s alert latency (BRD §3.5.4 / RFP v5 §6.5, identical) | M | Grounded | Consolidated FINAL reproduces this figure, **but self-annotates several rows "(attributed to BRD Section 3.5.4 — verify)"** | — | Cite and ground; recommend verification pass before final citation |
| R-081 | Electrical Systems Agent: ≥80% precision, ≥75% recall, up to 48hr, ≤30s | M | Grounded (same verify-flag caveat) | — | — | Cite and ground; verify before final citation |
| R-082 | Passenger Flow Agent: ≥85% precision, ≥80% recall, up to 45min, ≤15s | M | Grounded (same caveat) | — | — | Cite and ground; verify before final citation |
| R-083 | Structural Integrity Agent: ≥90% precision, ≥85% recall, up to 7 days, ≤60s | M | Grounded (same caveat) | Also see R-072's SHM-sensor dependency, which affects when this target becomes measurable | — | Cite and ground; verify; note SHM dependency |
| R-084 | Fire Safety Agent: ≥95% precision, ≥95% recall, real-time, ≤5s | M | Grounded (same caveat) | Tightest targets in the table, consistent with life-safety criticality | — | Cite and ground; verify before final citation |
| R-085 | Energy Management Agent: ≥80% precision, ≥75% recall, up to 24hr, ≤60s | M | Grounded (same caveat) | — | — | Cite and ground; verify before final citation |
| R-086 | Security Agent: ≥88% precision, ≥82% recall, real-time/15min, ≤10s | M | Grounded (same caveat) | — | — | Cite and ground; verify before final citation |
| R-087 | Water & Drainage Agent performance target (precision/recall/horizon/latency) | M (by implication — every other agent has one) | **Gap** | Confirmed by direct re-read: absent from BRD §3.5.4 **and** independently absent from RFP v5 §6.5 — a genuine gap in the requirement documents themselves, not an extraction error. Register AI-12 gives functional go-live scope but no numeric target | Manageable (source-document gap; an "agree with DIAL" placeholder is an accepted resolution) | Acknowledge gap: draft as "target to be finalized in consultation with DIAL, consistent with the rigor applied to the other 7 agents" — do not invent a number |

## 9. AI Model Governance & Transparency

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-088 | Explainability: plain-language explanation + confidence score (%) on every alert (BRD §3.5.5, RFP v5 §6.4) | M | Grounded | Consolidated FINAL commits | — | Cite and ground |
| R-089 | Auditability: complete audit log (input data, model version, timestamp, operator response), minimum 5-year retention (BRD §3.5.5) | M | Grounded | Consolidated FINAL commits; distinct from the 2-year user-activity log and 5-year BMS-historical log — three separate retention clauses (see R-054) | — | Cite and ground |
| R-090 | Feedback loop: operator feedback on alert accuracy feeds retraining (BRD §3.5.5) | M | Grounded | Consolidated FINAL commits | — | Cite and ground |
| R-091 | Model version control; rollback to prior version within 4 hours (BRD §3.5.5) | M | Grounded | Consolidated FINAL commits | — | Cite and ground |
| R-092 | DIAL owns all AI model weights and training data generated under contract (BRD §3.5.5, RFP v5 §9.3) | M | Grounded | Consolidated FINAL commits | — | Cite and ground |
| R-093 | "No Black Box": deep-learning models must use SHAP/LIME/attention-visualisation interpretability techniques (RFP v5 §6.4 only — not stated with this specificity in the binding BRD §3.5.5, which speaks more generally of "contributing factors") | M (per RFP v5) | Assertable | General explainability principle is Grounded (R-088); the specific technique mandate is a version-difference between sources | — | Assert general explainability commitment; note the technique-level prescriptiveness may be RFP v5-specific and should be confirmed against the binding BRD |

## 10. OT/BMS System Integration

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-094 | The 19-system OT estate is, with near-uniform consistency, "Not integrated with T3 ITBMS" (PE_OT System_09.06.pptx.md, confirmed by direct re-read of all 19 rows) | I (foundational problem statement) | Grounded | This is the best-evidenced scale/scope fact in the entire corpus — directly usable as the "why now" narrative | — | Cite and ground as the core problem-statement evidence |
| R-095 | T1 OT integration: HVAC, FDAS, VHT, ECMS, PBB, VDGS, LCMS, BHS, ATRS, GPU (register: point counts e.g. HVAC 20,000, FDAS 17,400) | M | Grounded | Middleware capability (R-046) plus RGIA precedent supports feasibility; point counts are DIAL-provided facts | — | Cite and ground the integration capability |
| R-096 | T3 OT integration: HVAC (~54,000 pts), FDAS (~65,000 pts), ECMS (~66,000 tags), MRSS (60,000 tags), and others (register, confirmed by direct re-read) | M | Grounded | Same basis as R-095, largest scale in the estate | — | Cite and ground |
| R-097 | T2 OT integration: HVAC, FDAS, VHT, ECMS, PBB, VDGS, LCMS, BHS, ATRS, GPU — register marks OEM and/or point count as "X" ("Doesn't exist" / "Not Present" / "Upcoming in 3 mo") for most T2 rows | M | **Gap** | Genuinely undefined scope in the source register itself, not an evidence gap on our side | Addressable | Flag T2 TBD items explicitly to DIAL rather than guessing counts or assuming zero scope |
| R-098 | Common integrations: WTP, STP, MRSS (SCADA upgrade GE→Schneider ongoing), Airside Solar SCADA (Trinity/Locus), AGL CMS, ITBMS (register, PE_OT) | M | Grounded, with one flagged dependency | MRSS integration is explicitly gated on a server-upgrade DIAL is completing (not a vendor gap) | — | Cite and ground; flag MRSS upgrade as an external dependency/timeline risk |
| R-099 | IT-side integrations: UTAM, Telematics, AODB, ADS-B, ARC, RMS, Kloudspot, XOVIS, PTM, SAC, ITOM (register, all marked "Part of OneAPOC program") | I | Gap | Unclear whether these fall inside Airport Eye's scope or a separate OneAPOC workstream — a genuine scope-boundary question raised by the source document's own annotation | Addressable | Seek clarification on the Airport Eye / OneAPOC scope boundary before committing to these integrations |

## 11. SPG "What-If" Simulation / Decision-Engine Scope (ABR)

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-100 | Dynamic digital twin decision-support/"what-if" simulation engine spanning Commercial/Operational/Engineering domains; 4-part architecture (DT for simulation, scenario-control UI, decision engine, visualisation UI) (ABR §4.1) | M (per ABR's one explicit "must") | Assertable | Consolidated FINAL references an "IROPs/Disruption Decision Engine," cross-referencing prior Solution Proposal v9 §5.2 — real, if partial and unresolved, adjacent evidence; no evidence the full 24-use-case capability is built or piloted | Manageable (largest section of the ABR by volume; risks under-representation if treated as a footnote to the 8-agent AI framework) | Track as its own distinct scope item, not folded into the 8 AI agents; assert the IROPs/Disruption Decision Engine precedent, flag the remainder as roadmap/aspirational |
| R-101 | 10 Commercial use cases (store-mix optimisation, shelf merchandising, dwell-time monetisation, queue-vs-revenue trade-off, gate allocation, etc.) (ABR §4.2) | I | Gap | No evidence any of these are built; framed as "possible examples," not obligations | Manageable | Acknowledge as illustrative scope; propose phased roadmap rather than committing to all 10 |
| R-102 | 8 Operational use cases (passenger flow optimisation, queue management, check-in/security capacity planning, disruption management, workforce deployment, baggage flow, curbside management) (ABR §4.2) | I | Gap, partially adjacent | Passenger Flow Monitoring Agent (R-071) is a real adjacent capability for some of these; no evidence of the simulation/decision-engine layer itself | Manageable | Same as R-101; note the Passenger Flow Agent as a partial building block |
| R-103 | 5 Engineering use cases (thermal load simulation, HVAC demand modelling, power infrastructure stress testing) (ABR §4.2) | I | Gap | No evidence of any simulation capability at this level; Mechanical&HVAC and Energy Management agents (R-066, R-070) are adjacent but monitor, not simulate | Manageable | Acknowledge as illustrative scope |

## 12. Additional ABR Departmental Requirements

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-104 | Borewell recharge monitoring via IoT (P&E) (ABR §3.1) | I | Assertable | General IoT-ingestion capability (R-046) is adjacent | — | Assert |
| R-105 | Storm water analysis with Walter P Moore, IoT-enabled monitoring (P&E) (ABR §3.1) | I | Grounded | Directly corroborated: register's Water & Drainage agent (AI-12) explicitly names "benchmarked against the Walter P Moore hydrology study" | — | Cite and ground via AI-12 linkage |
| R-106 | Reverse-entry detection in restricted zones (S&V) (ABR §3.2) | I | Assertable | Adjacent to Security & Perimeter Agent's access-pattern analytics (R-073) | — | Assert |
| R-107 | Unattended baggage detection via video analytics (S&V) (ABR §3.2) | I | Assertable | Adjacent to the platform's general video-analytics/AI framing; no specific named evidence | — | Assert with caveat |
| R-108 | Behaviour analytics for threat detection (S&V) (ABR §3.2) | I | Assertable | Adjacent to Security & Perimeter Agent (R-073) | — | Assert |
| R-109 | Predictive security monitoring (S&V) (ABR §3.2) | I | Grounded | Directly overlaps with the already-Grounded Security & Perimeter Monitoring Agent (R-073) | — | Cite and ground |
| R-110 | Security asset mapping (S&V) (ABR §3.2) | I | Assertable | Adjacent GIS capability | — | Assert |
| R-111 | Google Maps / satellite integration for landside monitoring (Commercial Aero) (ABR §3.3) | I | Grounded | BRD §3.1.2 Landside Coverage explicitly specifies "aircraft and satellite scans" | — | Cite and ground |
| R-112 | Identification of space-allocation changes (Commercial Aero) (ABR §3.3) | I | Gap | Depends on the land/space-management capability already flagged as a gap (R-039) | Addressable | Same remediation as R-039 |
| R-113 | GIS-based analytics for planning and utilisation (Commercial Aero) (ABR §3.3) | I | Grounded | Core GIS platform capability, well evidenced elsewhere | — | Cite and ground |
| R-114 | Surface navigation in low-visibility/fog conditions using GIS data (Operations) (ABR §3.4) | I | Gap | No evidence of this specific capability anywhere else in the corpus | Manageable | Acknowledge as a niche, ABR-only ask; no "must" language attached |
| R-115 | What-if scenario analytics (Operations) (ABR §3.4) | I | Assertable | Duplicate of R-100 (SPG); same IROPs/Disruption Decision Engine precedent applies | Manageable | Same treatment as R-100 |
| R-116 | Monitoring/alerting of DigiYatra, E-Gates, CUSS, CUPPS (Operations) (ABR §3.4) | I | Gap | These named systems do not appear in PE_OT's 19-system inventory or the BRD's scope at all — a possible scope addition not accounted for elsewhere | Addressable | Seek clarification on whether these are in scope for Airport Eye or a separate IT workstream |
| R-117 | Live operations monitoring dashboard (Operations) (ABR §3.4) | I | Grounded | Core APOC/CCC dashboard capability already covered (R-050) | — | Cite and ground |
| R-118 | Identification of overstaying/unidentified passengers (Operations) (ABR §3.4) | I | Assertable | Adjacent to Passenger Flow Agent (R-071) and general video-analytics framing | — | Assert |

## 13. Implementation Plan & Deliverables

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-119 | 5-phase programme, ~3 months each, ~15 months total (BRD §4.1, RFP v5 §5.1, identical structure confirmed by direct re-read) | M | Assertable | Structure is well evidenced across sources; **the Consolidated FINAL proposal's own stated "9-month delivery (Mo1–Mo9), re-baselined to March 2027" does not obviously reconcile with this ~15-month structure** — open question carried from the brief, not resolved here | — | Assert the BRD's 15-month structure as authoritative for compliance purposes; flag the Consolidated FINAL's 9-month figure as needing reconciliation (possibly a fast-track subset) before the drafter uses either number |
| R-120 | 15 numbered deliverables D-01 through D-15 (Project Execution Plan/BEP, LiDAR datasets, BIM models, DT platform, BMS/IoT integration report, AI platform, API docs, cybersecurity report, training materials, as-built docs, post-implementation review) (BRD §4.2, RFP v5 §5.2, identical) | M | Grounded | Standard deliverable-based PM commitment; RGIA's own delivery track record supports the process capability | — | Cite and ground |
| R-121 | 14-calendar-day DIAL review/sign-off period per deliverable (BRD §4.2) | M | Assertable | Standard commercial-process acceptance | — | Assert |

## 14. Roles & RACI

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-122 | RACI matrix across Planning/Surveys, Platform Dev, AI/Analytics, Operations — Vendor/DIAL/Smart City/DEC roles (BRD §5) | I | Assertable | We can commit to a RACI structure without naming individuals; the "DEC" and "POD" abbreviations are used in the source but never defined in the BRD's own glossary | — | Assert the RACI structure; flag DEC/POD as undefined terms rather than guessing their meaning |

## 15. Commercial Costing & Payment

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-123 | 8 costing table structures (LiDAR, BIM-by-LOD, Legacy CAD migration, BIM-BMS integration, DT viewer, AI agentic framework, Infrastructure, 5-yr O&M) (BRD §6, RFP v5 §10) | M | Assertable | Table structures and formats are usable as-is; no committed final figures exist in any reviewed collateral — Consolidated FINAL explicitly labels its own O&M and penalty figures "placeholder pending bidder finalisation" | — | Draft structure with confidence; flag that final unit pricing requires bidder financial input outside this eval's scope |
| R-124 | AI-agent costing (Table 6) prices only 5 of the 8 mandatory agent types as a lump sum (Mechanical&HVAC, Electrical, Fire Safety, Security, Water&Drainage) — Energy Management, Passenger Flow, Structural Integrity are unpriced (BRD §6 Table 6, confirmed by direct re-read) | M | Gap | Internal inconsistency in the source document itself | Addressable | Seek DIAL clarification on whether the 3 unpriced agents fold into the lump sum or require separate line items |
| R-125 | 6-milestone payment schedule M1–M6 (15/10/20/25/20/10% of contract value) (BRD §7, RFP v5 §9.4, identical) | M | Grounded | Structure clear and consistent across both binding/superseded sources | — | Cite and ground |
| R-126 | 12-month warranty; structured AMC thereafter (RFP v5 §9.5) | M | Assertable | Standard commercial commitment | — | Assert |
| R-127 | 5-year O&M plan; 24×7 support; RTO 4hr / RPO 24hr (register NFR section, confirmed by direct re-read — not stated in BRD itself) | M (per register) | Grounded | RGIA's 18+ month live O&M track record supports this; RTO/RPO figures are register-sourced only, flag if BRD silence on this point matters | — | Cite and ground via RGIA precedent; note RTO/RPO figures originate from the register, not the BRD |

## 16. Past Performance & Case Studies

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-128 | Minimum 3 case studies for submission (RFP v5 §9.3, Volume 6) | M | **Gap** | Consolidated FINAL proposal marks 2 of its 3 case-study slots "[Placeholder — bidder input]"; only RGIA is fully evidenced | **Disqualifying** if R-001 resolves to competitive framing (submission minimum) | Seek additional case-study collateral before proposal-assembler stage |

## 17. Team & Staffing

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-129 | CVs of key personnel, technical architects, named project leads (RFP v5 §9.3, Volume 7) | M | **Gap** | Complete blank — no named personnel, CVs, or staffing plan in any reviewed collateral | **Disqualifying** if RFP v5's submission structure is operative | Seek team/staffing collateral from capture team before section-drafter attempts this section; do not fabricate placeholder bios |
| R-130 | Company profile / general organisational references (RFP v5 §9.3, Volume 6) | M | Assertable | WAISL's multi-country footprint (India, UAE, US, UK, Singapore, Greece, Kuwait) is asserted, not tied to specific comparable digital-twin/BIM/AI deployments | — | Assert with caveat |

## 18. Exit Management, IP, and Regulatory Compliance

| ID | Requirement (source) | Type | Classification | Evidence / Rationale | Severity | Recommended Action |
|---|---|---|---|---|---|---|
| R-131 | 6-month minimum transition support at contract end, no additional cost (BRD §9.12) | M | Grounded | Consolidated FINAL explicitly commits to 6-month exit support matching the BRD figure | — | Cite and ground |
| R-132 | All deliverables become DIAL's exclusive IP upon milestone payment (BRD §9.10, RFP v5 §9.3) | M | Assertable | Standard legal commitment, no barrier | — | Assert |
| R-133 | Software Bill of Materials (SBOM) for third-party components (RFP v5 §9.3) | M | Assertable | Standard practice | — | Assert |
| R-134 | Vendor obtains/maintains all regulatory approvals (BCAS, AAI, etc.) at own cost (BRD §9.12 "Applicable Laws and Approvals") | M | Grounded | WAISL is the incumbent Concessionaire already operating under these approvals at IGIA since 2019 | — | Cite and ground |
| R-135 | Material default: 3+ SLA breaches in a quarter (BRD §9.9) | M | Assertable | Acceptance of a contractual risk term, not an evidence-based claim | — | Assert (acknowledge as accepted term) |

---

## Summary

**Total requirements extracted and classified: 135** (R-001–R-135), spanning explicit (shall/must — RFP v5 and BRD obligation language) and implicit (evaluation-criteria-driven, SOW-driven, and repeated-theme requirements from the ABR and registers).

### Classification breakdown

| Classification | Count | % |
|---|---|---|
| Grounded | 62 | 46% |
| Assertable | 51 | 38% |
| Gap | 22 | 16% |

*(A few rows carry a mixed/qualified classification — e.g., R-045, R-072, R-074 — and are counted under their primary/dominant classification above; the notes column preserves the nuance.)*

### Gap severity breakdown (of the 22 Gaps)

| Severity | Count | Items |
|---|---|---|
| **Disqualifying** | 4 | R-001 (procurement mechanism ambiguity — conditional disqualifying), R-007 (only 1 of 2 required comparable deployments — conditional), R-128 (only 1 of 3 required case studies — conditional), R-129 (team/staffing complete blank — conditional) |
| Manageable | 8 | R-039/R-040/R-112 (land/space mgmt cluster), R-056/R-059 (IEC 62443, SOC/SIEM), R-087 (Water & Drainage performance target), R-101/R-102/R-103 (SPG use-case clusters, counted individually below), R-114 (fog navigation) |
| Addressable | 10 | R-010, R-028, R-032, R-038, R-097, R-099, R-116, R-124, plus R-007/R-128/R-129 also carry an Addressable "seek evidence" component alongside their conditional-Disqualifying flag |

Note: three of the four **Disqualifying** gaps (R-007, R-128, R-129) are conditional on the still-unresolved procurement-mechanism question (R-001) — if DIAL confirms a negotiated Change Request to the incumbent rather than a competitively scored bid, their severity likely downgrades toward Manageable/Addressable, since an incumbent already under contract would presumably not need to re-clear pre-qualification gates. **R-001 itself is the one unconditional Disqualifying item** and is the correct place to focus escalation effort — resolving it substantially changes the real severity of the other three.

### Headline findings for the section-drafter

1. **Do not silently pick an AI-agent count.** The BRD's 8-agent table is the working roster (R-065), but RFP v5's internal inconsistency and the register's AI-10 (NL Query Agent) must be flagged explicitly wherever the roster is discussed, per task instruction.
2. **Water & Drainage has no performance target anywhere in the requirement corpus** (R-087) — this is a gap in DIAL's own source documents, not an extraction miss. Draft it as "to be agreed with DIAL," never invent a number.
3. **Two internal-source contradictions must not be blended**: Incident Response ≤10min (BRD, binding) vs ≤1hr (RFP v5) — use ≤10min only (R-017); TLS 1.3 (BRD) vs TLS 1.2+ (register) — use TLS 1.3 per BRD (R-053).
4. **One of our own prior proposals actively contradicts a binding requirement** — the APOC Phase II proposal's Singapore-region DR hosting directly conflicts with the India-only data-sovereignty clause (R-061). Exclude its infrastructure language from all reuse.
5. **Three conditional-Disqualifying gaps** (case studies, pre-qualification deployments, team/staffing) all trace back to the same unresolved question: is this a competitive bid or a negotiated CR to the incumbent (R-001)? Escalate R-001 first; it determines how much the other three actually matter.
