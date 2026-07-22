# Volume 2 — Technical Approach and Solution Architecture

## Understanding of the Problem

DIAL's PE_OT inventory documents 19 OT systems across HVAC, FDAS, VHT, ECMS, LCMS, PBB, VDGS, WTP/STP, MRSS, BHS, ATRS, GPU/PCA, AGL CMS and more — spanning 10+ OEMs (Honeywell, JCI/TKE, ABB, Schneider, Safegate, Edwards, GE, Vanderlande and others) and 10 named internal DIAL system owners, with "Not integrated with T3 ITBMS" the dominant per-row remark. [GROUNDED: PE_OT System_09.06.pptx.md — 19-system inventory, all 19 rows confirmed by direct re-read] The requirements registers quantify the integration challenge concretely: T3 HVAC alone carries ~54,000 points, T3 FDAS ~65,000 points, T3 ECMS ~66,000 tags, MRSS 60,000 tags. [GROUNDED: AirportEye_Requirements_Register_v5.xlsx.md — per-terminal point/tag counts, confirmed by direct re-read]

The binding BRD frames this as a growth-and-modernization evolution toward "a global benchmark for intelligent, data-driven airport operations," with a survey-grade geospatial/BIM foundation as the prerequisite infrastructure (the largest single section of the BRD by deliverable count, D-01 through D-10) and a federated, governed AI-agent monitoring layer as "the most technologically advanced and operationally transformative component." [GROUNDED: CR/BRD v1.5 §1.2, §3.1, §3.5] DIAL's tone rewards governed, auditable capability over novelty for its own sake — the enforceable mechanics in the BRD's contractual back half are conservative and vendor-unfavorable, even where the vision vocabulary is aspirational. [GROUNDED: brief.md — Vocabulary & Tone Notes]

## Proposed Solution — Two-Layer Architecture

Our architecture comprises two tightly integrated layers, directly aligned to DIAL's six primary objectives (BRD §2.2): a **Geo Digital Twin** (survey-grade geospatial/BIM foundation, Phase 1–3) and an **Operational Digital Twin / AI Operations Platform (AIOP)** that ingests live BMS/IoT telemetry and hosts the eight federated AI agents (Phase 4–5). [GROUNDED: Airport_Eye_Consolidated_Proposal_FINAL.docx.md — two-layer architecture description]

**Key Architectural Decisions:**

| Decision | Rationale | Alternative Considered | Why Rejected |
|---|---|---|---|
| Two-layer Geo DT + Operational DT/AIOP separation | Lets the geospatial/BIM foundation be built and approved before AI agents consume spatially-enriched telemetry — matches the BRD's 5-phase sequencing | Single unified platform from day 1 | Forces AI build to wait on survey completion; loses the BRD's phase-gate review structure |
| Hub-and-spoke BMS/IoT ingestion middleware | Proven at RGIA across 40+ systems with mixed protocols; matches DIAL's multi-OEM estate reality | Point-to-point integrations per system | Unmanageable across 19 systems / 10+ OEMs; conflicts with BRD §3.4.2 protocol list |
| India-only data residency (all storage/processing) | Hard binding requirement (BRD §9.10); material breach if violated | Hybrid with overseas DR | Directly contradicts §9.10; one of our own prior proposals was discarded for this reason |
| BRD's 8-agent table as the authoritative AI roster | Most specific, most recent, binding source | RFP v5's 5/6/7-agent variants or the registers' 17 AI-* rows | RFP v5 is internally inconsistent; registers mix platform/governance items with functional agents — see Volume 3 |

## Component 1 — Geospatial & LiDAR Foundation (BRD §3.1)

**Client requirement addressed:** R-021 through R-031 — airborne LiDAR ≥ 20 pts/m² core, 8 pts/m² buffer, horizontal RMSE ≤ 5cm, vertical RMSE ≤ 3cm, orthophoto GSD ≤ 5cm, DTM/DSM 10cm grid, indoor positional accuracy ≤ 5cm, LOD 200–350 BIM, ISO 19650 compliance.

**Approach:** GEOKNO delivers airborne and mobile/indoor LiDAR, RGB orthophotography, DTM/DSM, and LOD 200–350 BIM models across the ~5,000+ acre IGIA campus, the Aerocity precinct, and a 5km buffer. [GROUNDED: CR/BRD v1.5 §3.1; Airport_Eye_Consolidated_Proposal_FINAL.docx.md — matching figures]

**Specific commitments:**

| Parameter | BRD Requirement | Our Commitment | Status |
|---|---|---|---|
| Core LiDAR density | ≥ 20 pts/m² within airport boundary | Match | [GROUNDED: CR/BRD §3.1.1] |
| Buffer-zone LiDAR density | 8 pts/m² | Match, **pending DIAL confirmation** | [ASSERTION: Consolidated FINAL itself annotates this figure "pending DIAL confirmation" — not fully settled even in our newest document; flagged as open per R-022] |
| Horizontal accuracy | RMSE ≤ 5cm vs GCPs | Match | [GROUNDED: CR/BRD §3.1.1] |
| Vertical accuracy | RMSE ≤ 3cm vs benchmarks | Match | [GROUNDED: CR/BRD §3.1.1] |
| Orthophotography GSD | ≤ 5cm | Match | [GROUNDED: CR/BRD §3.1.1] |
| DTM/DSM grid | 10cm | Match | [GROUNDED: CR/BRD §3.1.1] |
| Indoor positional accuracy | ≤ 5cm RMSE post cloud-to-cloud registration | Match | [GROUNDED: CR/BRD §3.1.5] |
| LOD range | 200–350 per asset category, 10-category BIM standards | Match | [GROUNDED: CR/BRD §3.1.8 / RFP v5 §3.2.3, identical] |
| ISO 19650 compliance | Full | Commit | [ASSERTION: GEOKNO is our BIM/LiDAR delivery partner; no named ISO 19650-specific certification evidence cited — standard capability for a specialist BIM partner, flagged per R-030] |
| IFC 4.0 (ISO 16739) open exchange | Required (RFP v5 §3.2.2) | Commit | [ASSERTION: industry-standard capability for a BIM delivery partner; no specific certification cited, per R-031] |

**Items we flag rather than guess:**

- **Indoor scanning density at internal surfaces (R-028):** RFP v5 §3.2.1 carries an unfilled `[X] pts/m²` placeholder. We do not treat this as a settled figure. [GAP: R-028 — unfilled placeholder in the source document itself; flagged to DIAL for confirmation]
- **Appendix A — Schedule of Buildings/Areas (R-032):** currently "[To be completed by DIAL]" in the BRD. This underlies all area-based BIM/LiDAR costing. [GAP: R-032 — genuinely unavailable in any form reviewed; commercial costing cannot be finalized without it]
- **Appendix B — BIM Execution Plan requirements (R-038):** similarly "[To be completed by DIAL]." [GAP: R-038 — unavailable; flagged for DIAL input]

## Component 2 — GIS–BIM Integration & Federated BIM Platform (BRD §3.2)

**Client requirement addressed:** R-033 through R-038 — automated clash detection, version control with audit trail, RBAC, API integration to DT viewer and AI platform, legacy CAD/DWG migration to IFC-compliant BIM.

**Approach:** A federated BIM Common Data Environment with API-based integration to the Digital Twin viewer and the AI monitoring platform, matching the BRD §3.2.3 architecture. [GROUNDED: Airport_Eye_Consolidated_Proposal_FINAL.docx.md — two-layer architecture directly addresses R-036]

**Capabilities asserted as standard for a federated-BIM platform of this scale:** automated clash detection and multi-discipline coordination [ASSERTION: standard federated-BIM capability, no named evidence — R-033]; full version control, change management and audit trail [ASSERTION: R-034]; RBAC for internal staff, contractors, and consultants [ASSERTION: RBAC is evidenced at the DT viewer layer (§3.4.4) but not specifically for the BIM CDE — R-035]; legacy CAD/DWG migration to IFC-compliant BIM with a Data Quality Report [ASSERTION: adjacent — RGIA plausibly included similar migration work, not specifically evidenced — R-037].

## Component 3 — Facilities Maintenance Management (BRD §3.3, Phase 3)

**Client requirement addressed:** R-039 through R-043 — digital footprint of land/space with DIAL-specific legal vocabulary ("demised premises / additional demised premises / excluded premises / carved-out assets / MCD and DCB area bifurcation"), CLM integration, unified BMS/LCMS/ECMS/CMS/FDAS/BHS/HBS/VDGS/VHT/ATRS/DFMD/PBB/WTP-STP/AGL-CMS/IoT platform, specific IoT sensor inventories, environmental monitoring.

**Single-platform unification** across the 13+ named system families is directly grounded in our RGIA proof point: 40+ integrated systems on a "hub-and-spoke" integration fabric, 18+ months live. [GROUNDED: RGIA case study, per Consolidated FINAL — R-041]

**IoT sensor ingestion** for the DIAL-specified inventory (40 machine-room pump sensors across T1–T3, 12 T1 roof water-level sensors, Dissolved Gas Analysis in transformers) is supported by our BMS/IoT ingestion middleware (§3.4.2). [GROUNDED: CR/BRD §3.3.4 sensor inventory + our middleware capability — R-042; sensor counts are DIAL-provided facts, not our claims]

**Gaps we flag explicitly:**

- **Land/space management module with DIAL's legal vocabulary (R-039):** no land/space-management module evidenced anywhere in our collateral. [GAP: R-039 — if drafted, we mirror DIAL's exact "demised premises / additional demised premises / excluded premises / carved-out assets / MCD and DCB area bifurcation" vocabulary per the brief, but we cannot assert a capability we have not evidenced]
- **CLM tool integration (R-040):** no named CLM integration evidence. [GAP: R-040]
- **Environmental monitoring** (noise contours, flood zones, air quality, disaster-prone zone mapping) (R-043): plausible extension of the GIS platform, no named evidence of environmental-layer delivery. [ASSERTION: adjacent GIS capability, per R-043]

## Component 4 — Digital Twin Platform Architecture (BRD §3.4, Phase 4)

**Modular, cloud-native (or cloud-ready hybrid) platform (R-044):** [GROUNDED: two-layer architecture description in Evidence Map / Consolidated FINAL]

**Web 3D GIS+BIM viewer with seamless indoor/outdoor navigation, AR/VR output, full mobile offline responsiveness (R-045):** core 3D viewer capability is [GROUNDED: architecture description]; AR/VR output and full offline-mobile responsiveness are [ASSERTION: not independently evidenced in our collateral — flagged per R-045].

**BMS/IoT ingestion middleware supporting BACnet/IP, BACnet MSTP, Modbus TCP/RTU, MQTT v3.1.1/v5.0, SNMP, OPC-UA, REST (R-046):** [GROUNDED: RGIA proof point — 40+ systems, protocol-agnostic hub-and-spoke fabric]

**Unified semantic data model conforming to DTDL or equivalent (R-047):** [ASSERTION: no DTDL-specific evidence cited — standard capability for a modern DT platform, flagged per R-047]

**Every BMS data point mapped to a corresponding BIM element for 3D spatial visualisation (R-048):** [GROUNDED: core to the two-layer DT architecture already evidenced]

**Historical BMS data archiving, minimum 5-year retention (R-049):** [GROUNDED: Consolidated FINAL commits; note this is distinct from the 5-year AI-alert audit log (§3.5.5) and the 2-year user-activity log (§3.4.4) — three separate logs, three separate retention periods, not a contradiction]

**APOC/CCC integration via REST/GraphQL/WebSocket, ≥ 2 major versions backward compatibility (R-050):** [GROUNDED: `DIAL APOC Phase II Proposal 1.pdf.md` is a real, named prior APOC/AODB integration engagement — genuine adjacent precedent for the integration itself. Per task constraint, we do **not** reuse that proposal's AWS Singapore-region hosting language, its P1–P4 SLA ladder, or its commercial figures (which were for a materially different, narrower engagement).]

**Access control (R-051, R-052):** MFA + RBAC with 5 defined user roles (Executive, Operations, Maintenance, Security, Guest/Visitor) — [GROUNDED: Consolidated FINAL commits, matches BRD §3.4.4 language exactly]. SSO via SAML 2.0 or OAuth 2.0 integrated with DIAL's IdP — [ASSERTION: standard capability, no named evidence — R-052].

**Encryption (R-053):** TLS 1.3 in transit, AES-256 at rest — [GROUNDED: Consolidated FINAL commits to BRD's TLS 1.3 figure]. We note the requirements register independently states "TLS 1.2+" for the same control; per the binding-priority order we adopt the BRD's TLS 1.3 figure and do not blend. [GROUNDED: coverage-matrix R-053 — source inconsistency flagged, BRD governs]

**Activity audit logging, minimum 2-year retention (R-054):** [GROUNDED: Consolidated FINAL commits]

**Outdoor 3D GIS Platform with multi-department data layering, planning/scenario visualisation, collaborative redlining, secure sharing/publishing (R-055):** [ASSERTION: GEOKNO's GIS/LiDAR/BIM delivery role is adjacent evidence; no named evidence of the specific multi-department-layering/redlining collaboration features — R-055]

## Component 5 — Cybersecurity & Data Governance (BRD §3.4.5, §9.10–9.11)

DIAL's requirement language here is explicit and detailed, and the governance emphasis is repeated across Objectives, §3.4.5, §9.x, and Appendix E — signaling that DIAL wants innovation bounded by rigorous compliance rather than novelty for its own sake. [GROUNDED: brief.md — Stated Priorities, Trustworthy/auditable OT/IT integration]

**Grounded commitments:**

- **Data sovereignty (R-061):** all data stored/processed exclusively in India; no transfer without prior written DIAL approval; breach = material breach. [GROUNDED: CR/BRD §9.10; Consolidated FINAL commits. The APOC Phase II proposal's Singapore-region DR hosting is explicitly excluded from reuse.]
- **DPDP Act 2023 compliance (R-062):** [GROUNDED: Consolidated FINAL commits]
- **12-hour breach notification to DIAL (R-063):** [GROUNDED: CR/BRD §9.11; Consolidated FINAL matches exactly]
- **DIAL ownership of all AI model weights and training data (R-092):** [GROUNDED: CR/BRD §3.5.5; Consolidated FINAL commits — covered in detail in Volume 3]

**Asserted standard-practice commitments:**

- Network segmentation between IT/OT/internet-facing components, defence-in-depth (R-057): [ASSERTION: standard practice for an OT integrator of WAISL's scale; no named evidence]
- Penetration testing of internet-facing components prior to go-live (R-058): [ASSERTION: standard vendor practice; tied to Deliverable D-12]
- Full cybersecurity risk assessment prior to deployment, findings submitted for DIAL approval (R-060): [ASSERTION: standard practice; tied to Deliverable D-12]
- Vendor bears all breach-related costs; negligence-caused breaches attract penalties/termination (R-064): [ASSERTION: standard contract-term acceptance, not an evidence-based claim]

**Gaps we acknowledge honestly:**

- **IEC 62443 compliance for OT/IT integration components (R-056):** no IEC 62443 certification or compliance evidence found anywhere in our collateral. WAISL's ISO 27001/22301 are adjacent (information security / business continuity) but do not substitute for an ICS/OT-specific standard. [GAP: R-056 — Manageable severity. We propose an IEC 62443 compliance roadmap with a named specialist subcontractor/partner rather than asserting a certification we do not hold; this would become Disqualifying only if DIAL requires certification in hand at bid time, which we request DIAL confirm.]
- **SOC & SIEM capability for continuous security monitoring (R-059):** no SOC/SIEM operational track record cited anywhere in our collateral. [GAP: R-059 — Manageable. We propose a partner-led SOC/SIEM service as part of the 5-year O&M plan rather than asserting an in-house capability we have not evidenced.]

## Component 6 — OT/BMS System Integration (BRD §3.3.2, registers, PE_OT)

**T1 integration (R-095):** HVAC (20,000 pts), FDAS (17,400 pts), VHT, ECMS, PBB, VDGS, LCMS, BHS, ATRS, GPU — [GROUNDED: middleware capability R-046 + RGIA precedent supports feasibility; point counts are DIAL-provided facts from the register]

**T3 integration (R-096):** HVAC (~54,000 pts), FDAS (~65,000 pts), ECMS (~66,000 tags), MRSS (60,000 tags) and others — the largest scale in the estate. [GROUNDED: same basis as R-095; point counts confirmed by direct re-read of the register]

**T2 integration (R-097):** the register marks OEM and/or point count as "X" ("Doesn't exist" / "Not Present" / "Upcoming in 3 mo") for most T2 rows. [GAP: R-097 — genuinely undefined scope in the source register itself, not an evidence gap on our side. We flag these T2 items explicitly to DIAL rather than guessing counts or assuming zero scope.]

**Common integrations (R-098):** WTP, STP, MRSS (SCADA upgrade GE → Schneider ongoing), Airside Solar SCADA (Trinity/Locus), AGL CMS, ITBMS — [GROUNDED: register and PE_OT, with one flagged dependency]. MRSS integration is explicitly gated on a server-upgrade DIAL is completing; this is a DIAL-side prerequisite, not a vendor gap. [GROUNDED: coverage-matrix R-098 — MRSS upgrade flagged as external dependency/timeline risk]

**IT-side integrations (R-099):** UTAM, Telematics, AODB, ADS-B, ARC, RMS, Kloudspot, XOVIS, PTM, SAC, ITOM — all marked "Part of OneAPOC program" in the register. [GAP: R-099 — unclear whether these fall inside Airport Eye's scope or a separate OneAPOC workstream; a genuine scope-boundary question raised by the source document's own annotation. We seek DIAL clarification before committing to these integrations.]

## Integration Approach — Systems to Integrate

| System family | Integration method | Data flow | Complexity |
|---|---|---|---|
| HVAC (T1/T2/T3, ~74,000 pts total) | BACnet/IP, BACnet MSTP, Modbus TCP, OPC-UA via hub-and-spoke middleware | Bidirectional telemetry + commands | High (scale) |
| FDAS (~82,400 pts total) | Vendor-specific + OPC-UA | Telemetry in, advisory out (advisory never replaces certified fire system) | High (life-safety) |
| ECMS (~66,000+ tags T3) | Modbus TCP, MQTT, REST | Telemetry in | Medium |
| MRSS (60,000 tags T3) | SCADA migration GE→Schneider in progress; OPC-UA post-upgrade | Telemetry in | High (gated on DIAL upgrade) |
| BHS / ATRS / VDGS / PBB / LCMS / VHT / GPU / AGL CMS / WTP / STP | Mixed protocols per OEM | Telemetry in | Medium–High |
| APOC / CCC / AODB | REST/GraphQL/WebSocket, ≥ 2 major versions backward compatibility | Bidirectional | Medium |

[ASSERTION: complexity ratings are our assessment based on OEM diversity, scale, and life-safety criticality — not directly evidenced per-system]

## Development Methodology

We follow the BRD's 5-phase programme structure (Phase 1 Geospatial/LiDAR survey → Phase 2 GIS–BIM integration → Phase 3 Facilities maintenance management → Phase 4 Digital Twin platform → Phase 5 AI agents), with a 14-calendar-day DIAL review/sign-off period per deliverable (BRD §4.2) and 15 numbered deliverables D-01 through D-15. [GROUNDED: CR/BRD §4.1, §4.2; RFP v5 §5.1, §5.2 — identical structure confirmed by direct re-read] Volume 4 details the phase plan, deliverable acceptance, and roles/RACI.

## Testing & Quality Assurance

Per-agent acceptance testing against the individual BRD §6.5 / §3.5.4 performance rows on a rolling 90-day window, tied to Milestone M5 / Deliverable D-10. [ASSERTION: standard acceptance-testing practice — register AI-17, R-079] Penetration testing of internet-facing components prior to go-live is tied to Deliverable D-12. [ASSERTION: R-058] MLOps lifecycle: monthly drift monitoring, quarterly retraining, DIAL approval before release, rolling 90-day KPI window. [ASSERTION: standard MLOps practice, no named evidence of this specific cadence — register AI-05, R-078]

## Scalability & Performance

DIAL's scale is concretely evidenced: 5,000+ acre campus, three terminals (T3 interior alone ~588,000 m²), 4 runways / 180+ stands, an Aerocity precinct, and ~200+ sq.km total survey area. [GROUNDED: brief.md Client Summary; Consolidated FINAL acreage detail] Our RGIA proof point — 40+ integrated systems, 100+ KPIs, 18+ months live — is a direct operational scale analog. [GROUNDED: RGIA case study]

---

**Bridge.** The technical architecture above is the foundation; the federated AI-driven agents that DIAL calls "the most technologically advanced and operationally transformative component" of it are detailed in Volume 3.