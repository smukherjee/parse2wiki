# Pre-Flight Checklist

**Assembly Date:** 17-July-2026
**Assembler Stage:** Track B Stage 5 (proposal-assembler)
**Status:** ACTION REQUIRED — assemble-ready, but multiple unresolved items and unvalidated compliance must be addressed before submission

> **WARNING — COMPLIANCE NOT VALIDATED.** No `compliance-report.md` has been produced for this draft. The external compliance scoring for this eval runs AFTER assembly. Run the compliance-validator against this assembled document before any submission. Do not treat this document as compliance-cleared.

## Document Completeness

- [x] All RFP v5 7-volume sections present (Volumes 1–7 + Appendices)
- [x] Cover page complete
- [x] Table of contents generated
- [x] Contact information placeholder included (named SPOC pending DIAL nomination)
- [ ] All referenced appendices included — the RTM appendix (this proposal's Appendix A) is included; CR/BRD Appendices A, B, and D remain "[To be completed by DIAL]" in the source and are flagged as open items, not authored here
- [ ] Volume 7 (Team & Staffing) — CVs/key personnel NOT drafted (complete blank; skeleton only, no fabrication per task instruction)

## Compliance Status

- [ ] Compliance validation passed — **NOT RUN.** `compliance-report.md` was not produced for this draft. Run compliance-validator before submission.
- Warnings: unable to enumerate — no compliance report exists yet.

## Evidence Quality

- Grounded claims (inline annotations stripped from final): **124**
- Assertions (inline, stripped from final): **56**
- Review notes (stripped from final — see Unresolved Items): **19**
- Gap annotations (inline, stripped from final): **43**
- Bare `[GAP]` / `[GROUNDED]` / `[ASSERTION]` classification labels preserved in the RTM table and legend: **25** `[GAP]` labels (RTM content, not drafter annotations)
- **Grounding ratio: 124/180 = 68.9%** (grounded / (grounded + assertions))

## Unresolved Items

**Unresolved review notes (empathy-reviewer comments not integrated into final text):**
- [ ] 19 `[REVIEW: ...]` notes were left in the reviewed sections as reviewer suggestions (tone/vendor-centric framing refinements, passive-accountability naming, generic-language upgrades, minor empathy additions). They were stripped from this assembled document per skill instruction but were NOT individually integrated into the prose. A human authoring pass should action them before submission. Affected volumes: V1 (4), V2 (4), V3 (2), V4 (2), V5 (1), V6 (2), V7 (2), Appendices (1); one V7 note overlaps on the same passage.

**Placeholder appendices / sections:**
- [ ] **Volume 6 Case Studies 2 & 3** — explicit `[Placeholder — bidder input]`; only RGIA (Case Study 1) is evidenced. R-128 (≥3 case studies submission minimum) and R-007 (≥2 comparable deployments pre-qualification) are unmet — conditional-Disqualifying if R-001 resolves to competitive framing.
- [ ] **Volume 7 Team & Staffing** — staffing-plan skeleton only; no named personnel, CVs, or certifications. R-129 unmet — conditional-Disqualifying if RFP v5 submission structure is operative.
- [ ] **IEC 62443 specialist subcontractor** — "to be named"; R-056 mitigation partner not yet identified.
- [ ] **SOC/SIEM service partner** — "to be named"; R-059 mitigation partner not yet identified.

**Open items from gap-report.md (unresolved at assembly):**
- [ ] **R-001 — Procurement-mechanism ambiguity (Disqualifying, unconditional).** Competitively scored RFP vs. negotiated Change Request to incumbent — not reconciled anywhere in the corpus. Drives whether page limits, evaluation weights, and pre-qualification gates apply. Highest-priority escalation.
- [ ] **R-129 — Team/staffing complete blank** (see placeholder above).
- [ ] **R-128 / R-007 — Case-study / comparable-deployment shortfall** (see placeholder above).
- [ ] **R-007 — Comparable deployments** — only RGIA evidenced of the ≥2 required.
- [ ] **Unpriced commercial tables** — R-123 (final unit pricing across all 8 costing tables pending bidder cost-modeling input); R-124 (3 of 8 AI agents unpriced in BRD's own Table 6 — Energy Management, Passenger Flow, Structural Integrity); R-010 (minimum annual-turnover threshold is an unfilled `[X] crore` placeholder in RFP v5 Appendix E).

**Other source-document gaps flagged in the proposal text:**
- [ ] R-032 / R-038 — CR/BRD Appendices A & B "[To be completed by DIAL]" — underlie area-based costing and BEP.
- [ ] R-028 — Indoor scanning density `[X] pts/m²` unfilled in RFP v5 §3.2.1.
- [ ] R-087 — Water & Drainage Agent has no performance target anywhere in the requirement corpus (source-document gap, not extraction error).
- [ ] R-097 — T2 OT integration scope marked TBD/"X" in the registers.
- [ ] R-099 / R-116 — Airport Eye / OneAPOC scope boundary unclear (UTAM/AODB/DigiYatra/E-Gates/CUSS/CUPPS).
- [ ] R-065 / R-074 — AI-agent roster ambiguity (BRD's 8 vs RFP v5's 6/7 vs registers' 17 AI-* rows incl. NL Query Agent AI-10).
- [ ] R-119 — 15-month BRD programme vs 9-month Consolidated FINAL delivery figure unreconciled.
- [ ] R-053 / R-017 — Internal source contradictions (TLS 1.3 vs TLS 1.2+; incident response ≤10min vs ≤1hr) — BRD adopted as binding, but flag remains.
- [ ] R-122 — "DEC" and "POD" abbreviations undefined in the BRD glossary.

## Page Count Estimate

| Volume | Estimated Pages | RFP v5 Limit | Status |
|---|---|---|---|
| Volume 1 — Executive Summary | ~5 | 10 (max) | OK |
| Volume 2 — Technical Approach | ~12 | None stated | OK |
| Volume 3 — AI & Analytics | ~10 | None stated | OK |
| Volume 4 — Implementation Methodology | ~5 | None stated | OK |
| Volume 5 — Commercial Proposal | ~4 | None stated | OK |
| Volume 6 — Qualifications & References | ~4 | None stated | OK (content-short: 2 of 3 case studies placeholder) |
| Volume 7 — Team & Staffing | ~3 | None stated | At Risk (skeleton only) |
| Appendices — RTM | ~9 | None stated | OK |
| **Total** | **~52** | **10 (only V1 stated)** | V1 within limit; other limits unspecified |

## Before Submission

- [ ] Run compliance-validator against this assembled document
- [ ] Human review of all 56 assertions for accuracy and DIAL-checkable specificity
- [ ] Integrate the 19 stripped empathy-reviewer notes (tone/accountability/DIAL-centricity refinements)
- [ ] Resolve R-001 procurement-mechanism ambiguity with DIAL
- [ ] Obtain and insert Case Studies 2 & 3 (R-128/R-007)
- [ ] Obtain and insert Volume 7 CVs / named personnel (R-129)
- [ ] Populate final unit pricing across 8 costing tables (R-123) and resolve AI-agent costing for 3 unpriced agents (R-124)
- [ ] Identify named IEC 62443 and SOC/SIEM partners (R-056, R-059)
- [ ] Confirm buffer-zone LiDAR density (R-022) and obtain CR/BRD Appendices A & B (R-032, R-038)
- [ ] Final formatting in submission format (PDF/Word as required by DIAL)
- [ ] Authorized signature on required forms
- [ ] Submission method and deadline confirmed (BRD gives a 10-day submission window; RFP v5 deadline stated on cover page)

---

# Airport Eye — APOC Phase 2

**Proposal in Response to Change Request / Business Requirements Document (CR/BRD v1.5, DIAL-AE-BRD-001) and Base RFP v5**

**Submitted To:** Delhi International Airport Limited (DIAL) — operating Indira Gandhi International Airport (IGIA)

**Submitted By:** WAISL Limited (Incumbent Concessionaire under the Concession Agreement dated 30-September-2019), with GEOKNO as geospatial/LiDAR/BIM delivery partner

**Date:** 17-July-2026

**Procurement Reference:** CR/BRD v1.5 (DIAL-AE-BRD-001, 05-June-2026) issued to the Concessionaire under the 2019 Concession Agreement; base RFP v5 (competitive structure preserved as superset default — see Volume 1 §Procurement Framing).

**Primary Contact:**
WAISL Limited — Proposal Team
(Designated single point of contact to be confirmed on DIAL's nomination)

**Structural Assumption (flagged, not silently chosen):** The binding CR/BRD v1.5 frames this cycle as a Change Request to the incumbent Concessionaire under the existing CA, while the base RFP v5 carries a full competitively-scored 7-volume submission structure. No document in the corpus explicitly reconciles the two. This submission is drafted against the more complete RFP v5 7-volume structure as a conservative default (a formal submission is a strict superset that can be trimmed to a CA-referenced quotation letter if DIAL confirms the negotiated-CR framing). We request DIAL confirmation and will reformat accordingly.

---

# Table of Contents

- Volume 1 — Executive Summary
- Volume 2 — Technical Approach and Solution Architecture
- Volume 3 — AI and Analytics Capability
- Volume 4 — Implementation Methodology and Timeline
- Volume 5 — Commercial Proposal
- Volume 6 — Qualifications and References
- Volume 7 — Team & Staffing
- Appendices — Requirements Traceability Matrix

---

# Volume 1 — Executive Summary

## Procurement Framing and Structural Assumption

This submission is prepared by **WAISL Limited**, the incumbent Concessionaire under the Concession Agreement (CA) dated 30-September-2019, with GEOKNO as geospatial/LiDAR/BIM delivery partner. The binding Change Request / Business Requirements Document (CR/BRD v1.5, DIAL-AE-BRD-001, 05-June-2026) frames this cycle as a Change Request against that existing Concession Agreement, stating in §1.2 that "the Concessionaire is requested to submit its quotation in accordance with the provisions of the Concession Agreement."

A structural ambiguity must be flagged honestly at the outset: the base RFP v5 carries a full competitively-scored apparatus (3-stage evaluation panel, weighted scoring, 7-volume submission structure, pre-qualification gates), and no document in the corpus explicitly states whether that apparatus remains operative under the CR framing or has been superseded. **We draft this submission against the more complete RFP v5 structure as a conservative default** — a formal 7-volume response is a strict superset that can be trimmed to a CA-referenced quotation letter if DIAL confirms the negotiated-CR framing, whereas a quotation letter cannot retroactively acquire evaluation-compliant structure. We request DIAL confirmation on this point and will reformat accordingly.

## DIAL's Problem, In DIAL's Words

IGIA's OT/BMS estate is fragmented and largely unintegrated. The authoritative PE_OT system inventory lists 19 distinct OT systems (HVAC, FDAS, VHT, ECMS, LCMS, PBB, VDGS, WTP/STP, MRSS, BHS, ATRS, GPU/PCA, AGL CMS, and others) across 10+ OEMs and integrators, with the remark **"Not integrated with T3 ITBMS"** recurring across nearly every row. Operations today are reactive: incidents, equipment failures, and safety/security events are discovered after the fact rather than predicted or pre-empted.

DIAL's desired outcome, stated verbatim in the binding BRD §2.1, is "a living, dynamic, and spatially accurate digital replica of the entire airport ecosystem, including the Aerocity precinct... a network of federated AI-driven agents with spatial intelligence, operating continuously (24/7), that act as the 'digital eye' of the airport" — transitioning operations "from reactive management to predictive and autonomous intelligence."

## Our Response, In Summary

As the incumbent Concessionaire operating under these approvals at IGIA since 2019, WAISL with GEOKNO offers a two-layer architecture directly aligned to DIAL's vision: a **Geo Digital Twin** (survey-grade geospatial/BIM foundation) underlying an **Operational Digital Twin / AIOP layer** hosting the eight federated AI-driven agents the BRD §3.5.3 names as mandatory.

Our strongest evidenced proof point is the **Rajiv Gandhi International Airport (RGIA), Hyderabad** deployment: 18+ months live operation, 40+ integrated systems, 100+ KPIs tracked — a direct operational analog for the multi-system unification DIAL requires.

## Headline Commitments (Binding KPIs)

| KPI | BRD Target | Our Commitment | Source |
|---|---|---|---|
| Platform Uptime | ≥ 99.5% (excl. planned maintenance) | Match | |
| Real-time data latency | ≤ 5 seconds sensor-to-dashboard | Match | |
| BIM LOD compliance | 100% of specified assets | Match | |
| Predictive alert accuracy | ≥ 80% precision / ≥ 75% recall | Match | |
| Geospatial accuracy | ≤ 5cm H RMSE / ≤ 3cm V RMSE | Match | |
| Critical incident response | ≤ 10 minutes from notification | Match | |
| System integration coverage | 100% of agreed BMS/IoT points within 3 months of go-live | Match | |

We note explicitly that RFP v5's own KPI table states a materially different ≤ 1 hour Critical Incident Response figure for the same metric; per the binding-priority order we adopt the BRD's ≤ 10 minute figure and treat the RFP v5 ≤ 1 hour figure as superseded.

## Honest Gaps We Flag Rather Than Disguise

Four gaps must be named plainly, because an evaluator reading alongside competitors can distinguish a vendor who has done this from one improvising:

1. **Procurement mechanism ambiguity (R-001)** — flagged above; this submission's structural assumption is labelled, not silently chosen.
2. **Comparable deployments / case studies (R-007, R-128)** — RFP v5 Appendix E requires ≥ 2 comparable deployments for pre-qualification and Volume 6 requires ≥ 3 case studies. Only **RGIA (Hyderabad)** is fully evidenced in our current collateral; two of three case-study slots are explicit placeholders pending bidder input.
3. **Team & staffing (R-129)** — no named personnel, CVs, or staffing plan exist in any reviewed collateral. We do not fabricate bios.
4. **IEC 62443 OT cybersecurity certification (R-056) and SOC/SIEM track record (R-059)** — not held or evidenced in our collateral; addressed via a compliance roadmap and named-partner mitigation rather than a false assertion of certification in hand.

One additional self-inflicted risk is worth naming: one of our own prior proposals (`DIAL APOC Phase II Proposal 1.pdf.md`) proposed AWS Singapore-region DR hosting, which directly contradicts the BRD's binding India-only data-sovereignty clause (§9.10). We explicitly exclude that hosting language from this submission and commit to India-only data residency throughout.

## Where This Submission Goes Next

Volume 2 details our technical approach and solution architecture. Volume 3 addresses the AI and analytics capability that DIAL's own evaluation emphasis (the most granular numeric tables in the corpus) marks as the technologically transformative core. Volume 4 covers implementation methodology and timeline. Volume 5 presents the commercial structure. Volume 6 presents qualifications and the available case study. Volume 7 addresses team & staffing honestly. Appendices carry the requirements traceability matrix.

---

# Volume 2 — Technical Approach and Solution Architecture

## Understanding of the Problem

DIAL's PE_OT inventory documents 19 OT systems across HVAC, FDAS, VHT, ECMS, LCMS, PBB, VDGS, WTP/STP, MRSS, BHS, ATRS, GPU/PCA, AGL CMS and more — spanning 10+ OEMs (Honeywell, JCI/TKE, ABB, Schneider, Safegate, Edwards, GE, Vanderlande and others) and 10 named internal DIAL system owners, with "Not integrated with T3 ITBMS" the dominant per-row remark. The requirements registers quantify the integration challenge concretely: T3 HVAC alone carries ~54,000 points, T3 FDAS ~65,000 points, T3 ECMS ~66,000 tags, MRSS 60,000 tags.

The binding BRD frames this as a growth-and-modernization evolution toward "a global benchmark for intelligent, data-driven airport operations," with a survey-grade geospatial/BIM foundation as the prerequisite infrastructure (the largest single section of the BRD by deliverable count, D-01 through D-10) and a federated, governed AI-agent monitoring layer as "the most technologically advanced and operationally transformative component." DIAL's tone rewards governed, auditable capability over novelty for its own sake — the enforceable mechanics in the BRD's contractual back half are conservative and vendor-unfavorable, even where the vision vocabulary is aspirational.

## Proposed Solution — Two-Layer Architecture

Our architecture comprises two tightly integrated layers, directly aligned to DIAL's six primary objectives (BRD §2.2): a **Geo Digital Twin** (survey-grade geospatial/BIM foundation, Phase 1–3) and an **Operational Digital Twin / AI Operations Platform (AIOP)** that ingests live BMS/IoT telemetry and hosts the eight federated AI agents (Phase 4–5).

**Key Architectural Decisions:**

| Decision | Rationale | Alternative Considered | Why Rejected |
|---|---|---|---|
| Two-layer Geo DT + Operational DT/AIOP separation | Lets the geospatial/BIM foundation be built and approved before AI agents consume spatially-enriched telemetry — matches the BRD's 5-phase sequencing | Single unified platform from day 1 | Forces AI build to wait on survey completion; loses the BRD's phase-gate review structure |
| Hub-and-spoke BMS/IoT ingestion middleware | Proven at RGIA across 40+ systems with mixed protocols; matches DIAL's multi-OEM estate reality | Point-to-point integrations per system | Unmanageable across 19 systems / 10+ OEMs; conflicts with BRD §3.4.2 protocol list |
| India-only data residency (all storage/processing) | Hard binding requirement (BRD §9.10); material breach if violated | Hybrid with overseas DR | Directly contradicts §9.10; one of our own prior proposals was discarded for this reason |
| BRD's 8-agent table as the authoritative AI roster | Most specific, most recent, binding source | RFP v5's 5/6/7-agent variants or the registers' 17 AI-* rows | RFP v5 is internally inconsistent; registers mix platform/governance items with functional agents — see Volume 3 |

## Component 1 — Geospatial & LiDAR Foundation (BRD §3.1)

**Client requirement addressed:** R-021 through R-031 — airborne LiDAR ≥ 20 pts/m² core, 8 pts/m² buffer, horizontal RMSE ≤ 5cm, vertical RMSE ≤ 3cm, orthophoto GSD ≤ 5cm, DTM/DSM 10cm grid, indoor positional accuracy ≤ 5cm, LOD 200–350 BIM, ISO 19650 compliance.

**Approach:** GEOKNO delivers airborne and mobile/indoor LiDAR, RGB orthophotography, DTM/DSM, and LOD 200–350 BIM models across the ~5,000+ acre IGIA campus, the Aerocity precinct, and a 5km buffer.

**Specific commitments:**

| Parameter | BRD Requirement | Our Commitment | Status |
|---|---|---|---|
| Core LiDAR density | ≥ 20 pts/m² within airport boundary | Match | |
| Buffer-zone LiDAR density | 8 pts/m² | Match, **pending DIAL confirmation** | |
| Horizontal accuracy | RMSE ≤ 5cm vs GCPs | Match | |
| Vertical accuracy | RMSE ≤ 3cm vs benchmarks | Match | |
| Orthophotography GSD | ≤ 5cm | Match | |
| DTM/DSM grid | 10cm | Match | |
| Indoor positional accuracy | ≤ 5cm RMSE post cloud-to-cloud registration | Match | |
| LOD range | 200–350 per asset category, 10-category BIM standards | Match | |
| ISO 19650 compliance | Full | Commit | |
| IFC 4.0 (ISO 16739) open exchange | Required (RFP v5 §3.2.2) | Commit | |

**Items we flag rather than guess:**

- **Indoor scanning density at internal surfaces (R-028):** RFP v5 §3.2.1 carries an unfilled `[X] pts/m²` placeholder. We do not treat this as a settled figure.
- **Appendix A — Schedule of Buildings/Areas (R-032):** currently "[To be completed by DIAL]" in the BRD. This underlies all area-based BIM/LiDAR costing.
- **Appendix B — BIM Execution Plan requirements (R-038):** similarly "[To be completed by DIAL]."

## Component 2 — GIS–BIM Integration & Federated BIM Platform (BRD §3.2)

**Client requirement addressed:** R-033 through R-038 — automated clash detection, version control with audit trail, RBAC, API integration to DT viewer and AI platform, legacy CAD/DWG migration to IFC-compliant BIM.

**Approach:** A federated BIM Common Data Environment with API-based integration to the Digital Twin viewer and the AI monitoring platform, matching the BRD §3.2.3 architecture.

**Capabilities asserted as standard for a federated-BIM platform of this scale:** automated clash detection and multi-discipline coordination; full version control, change management and audit trail; RBAC for internal staff, contractors, and consultants; legacy CAD/DWG migration to IFC-compliant BIM with a Data Quality Report.

## Component 3 — Facilities Maintenance Management (BRD §3.3, Phase 3)

**Client requirement addressed:** R-039 through R-043 — digital footprint of land/space with DIAL-specific legal vocabulary ("demised premises / additional demised premises / excluded premises / carved-out assets / MCD and DCB area bifurcation"), CLM integration, unified BMS/LCMS/ECMS/CMS/FDAS/BHS/HBS/VDGS/VHT/ATRS/DFMD/PBB/WTP-STP/AGL-CMS/IoT platform, specific IoT sensor inventories, environmental monitoring.

**Single-platform unification** across the 13+ named system families is directly grounded in our RGIA proof point: 40+ integrated systems on a "hub-and-spoke" integration fabric, 18+ months live.

**IoT sensor ingestion** for the DIAL-specified inventory (40 machine-room pump sensors across T1–T3, 12 T1 roof water-level sensors, Dissolved Gas Analysis in transformers) is supported by our BMS/IoT ingestion middleware (§3.4.2).

**Gaps we flag explicitly:**

- **Land/space management module with DIAL's legal vocabulary (R-039):** no land/space-management module evidenced anywhere in our collateral.
- **CLM tool integration (R-040):** no named CLM integration evidence.
- **Environmental monitoring** (noise contours, flood zones, air quality, disaster-prone zone mapping) (R-043): plausible extension of the GIS platform, no named evidence of environmental-layer delivery.

## Component 4 — Digital Twin Platform Architecture (BRD §3.4, Phase 4)

**Modular, cloud-native (or cloud-ready hybrid) platform (R-044):**

**Web 3D GIS+BIM viewer with seamless indoor/outdoor navigation, AR/VR output, full mobile offline responsiveness (R-045):** core 3D viewer capability is; AR/VR output and full offline-mobile responsiveness are.

**BMS/IoT ingestion middleware supporting BACnet/IP, BACnet MSTP, Modbus TCP/RTU, MQTT v3.1.1/v5.0, SNMP, OPC-UA, REST (R-046):**

**Unified semantic data model conforming to DTDL or equivalent (R-047):**

**Every BMS data point mapped to a corresponding BIM element for 3D spatial visualisation (R-048):**

**Historical BMS data archiving, minimum 5-year retention (R-049):**

**APOC/CCC integration via REST/GraphQL/WebSocket, ≥ 2 major versions backward compatibility (R-050):**

**Access control (R-051, R-052):** MFA + RBAC with 5 defined user roles (Executive, Operations, Maintenance, Security, Guest/Visitor) —. SSO via SAML 2.0 or OAuth 2.0 integrated with DIAL's IdP —.

**Encryption (R-053):** TLS 1.3 in transit, AES-256 at rest —. We note the requirements register independently states "TLS 1.2+" for the same control; per the binding-priority order we adopt the BRD's TLS 1.3 figure and do not blend.

**Activity audit logging, minimum 2-year retention (R-054):**

**Outdoor 3D GIS Platform with multi-department data layering, planning/scenario visualisation, collaborative redlining, secure sharing/publishing (R-055):**

## Component 5 — Cybersecurity & Data Governance (BRD §3.4.5, §9.10–9.11)

DIAL's requirement language here is explicit and detailed, and the governance emphasis is repeated across Objectives, §3.4.5, §9.x, and Appendix E — signaling that DIAL wants innovation bounded by rigorous compliance rather than novelty for its own sake.

**Grounded commitments:**

- **Data sovereignty (R-061):** all data stored/processed exclusively in India; no transfer without prior written DIAL approval; breach = material breach.
- **DPDP Act 2023 compliance (R-062):**
- **12-hour breach notification to DIAL (R-063):**
- **DIAL ownership of all AI model weights and training data (R-092):**

**Asserted standard-practice commitments:**

- Network segmentation between IT/OT/internet-facing components, defence-in-depth (R-057):
- Penetration testing of internet-facing components prior to go-live (R-058):
- Full cybersecurity risk assessment prior to deployment, findings submitted for DIAL approval (R-060):
- Vendor bears all breach-related costs; negligence-caused breaches attract penalties/termination (R-064):

**Gaps we acknowledge honestly:**

- **IEC 62443 compliance for OT/IT integration components (R-056):** no IEC 62443 certification or compliance evidence found anywhere in our collateral. WAISL's ISO 27001/22301 are adjacent (information security / business continuity) but do not substitute for an ICS/OT-specific standard.
- **SOC & SIEM capability for continuous security monitoring (R-059):** no SOC/SIEM operational track record cited anywhere in our collateral.

## Component 6 — OT/BMS System Integration (BRD §3.3.2, registers, PE_OT)

**T1 integration (R-095):** HVAC (20,000 pts), FDAS (17,400 pts), VHT, ECMS, PBB, VDGS, LCMS, BHS, ATRS, GPU —

**T3 integration (R-096):** HVAC (~54,000 pts), FDAS (~65,000 pts), ECMS (~66,000 tags), MRSS (60,000 tags) and others — the largest scale in the estate.

**T2 integration (R-097):** the register marks OEM and/or point count as "X" ("Doesn't exist" / "Not Present" / "Upcoming in 3 mo") for most T2 rows.

**Common integrations (R-098):** WTP, STP, MRSS (SCADA upgrade GE → Schneider ongoing), Airside Solar SCADA (Trinity/Locus), AGL CMS, ITBMS —. MRSS integration is explicitly gated on a server-upgrade DIAL is completing; this is a DIAL-side prerequisite, not a vendor gap.

**IT-side integrations (R-099):** UTAM, Telematics, AODB, ADS-B, ARC, RMS, Kloudspot, XOVIS, PTM, SAC, ITOM — all marked "Part of OneAPOC program" in the register.

## Integration Approach — Systems to Integrate

| System family | Integration method | Data flow | Complexity |
|---|---|---|---|
| HVAC (T1/T2/T3, ~74,000 pts total) | BACnet/IP, BACnet MSTP, Modbus TCP, OPC-UA via hub-and-spoke middleware | Bidirectional telemetry + commands | High (scale) |
| FDAS (~82,400 pts total) | Vendor-specific + OPC-UA | Telemetry in, advisory out (advisory never replaces certified fire system) | High (life-safety) |
| ECMS (~66,000+ tags T3) | Modbus TCP, MQTT, REST | Telemetry in | Medium |
| MRSS (60,000 tags T3) | SCADA migration GE→Schneider in progress; OPC-UA post-upgrade | Telemetry in | High (gated on DIAL upgrade) |
| BHS / ATRS / VDGS / PBB / LCMS / VHT / GPU / AGL CMS / WTP / STP | Mixed protocols per OEM | Telemetry in | Medium–High |
| APOC / CCC / AODB | REST/GraphQL/WebSocket, ≥ 2 major versions backward compatibility | Bidirectional | Medium |

## Development Methodology

We follow the BRD's 5-phase programme structure (Phase 1 Geospatial/LiDAR survey → Phase 2 GIS–BIM integration → Phase 3 Facilities maintenance management → Phase 4 Digital Twin platform → Phase 5 AI agents), with a 14-calendar-day DIAL review/sign-off period per deliverable (BRD §4.2) and 15 numbered deliverables D-01 through D-15. Volume 4 details the phase plan, deliverable acceptance, and roles/RACI.

## Testing & Quality Assurance

Per-agent acceptance testing against the individual BRD §6.5 / §3.5.4 performance rows on a rolling 90-day window, tied to Milestone M5 / Deliverable D-10. Penetration testing of internet-facing components prior to go-live is tied to Deliverable D-12. MLOps lifecycle: monthly drift monitoring, quarterly retraining, DIAL approval before release, rolling 90-day KPI window.

## Scalability & Performance

DIAL's scale is concretely evidenced: 5,000+ acre campus, three terminals (T3 interior alone ~588,000 m²), 4 runways / 180+ stands, an Aerocity precinct, and ~200+ sq.km total survey area. Our RGIA proof point — 40+ integrated systems, 100+ KPIs, 18+ months live — is a direct operational scale analog.

---

**Bridge.** The technical architecture above is the foundation; the federated AI-driven agents that DIAL calls "the most technologically advanced and operationally transformative component" of it are detailed in Volume 3.

---

# Volume 3 — AI and Analytics Capability

## Understanding of the Problem

DIAL's CR/BRD v1.5 §3.5 calls the federated AI-agent monitoring layer "the most technologically advanced and operationally transformative component" of Airport Eye — and backs that emphasis with the only granular, numeric, per-item performance tables in the entire corpus (§3.5.4 precision/recall/latency/prediction-horizon targets for 7 of the 8 named agents). Both the BRD and RFP v5 devote disproportionate detail to this section; cybersecurity/data-governance language is repeated across at least four separate sections in each document. The signal is unambiguous: DIAL's real evaluation emphasis is AI-agent credibility plus governance/compliance trustworthiness, not price (Commercial is weighted lowest at 15% in the one document that gives explicit weights).

## Roster Ambiguity — Flagged, Not Silently Resolved

We adopt the **BRD §3.5.3 eight-agent table as the authoritative working roster** per the binding-priority order. We flag explicitly that this is not the only enumeration in the corpus:

- **RFP v5 §6.3** describes only 6 of the 8 (no subsection for Passenger Flow or Structural Integrity — confirmed by direct re-read: §6.3.1, .2, .4, .5, .6, .7 exist; §6.3.3 is a numbering gap with no corresponding text).
- **RFP v5 §6.5 performance table** scores 7 agents (adds Passenger Flow and Structural Integrity, but — like the BRD — omits Water & Drainage entirely).
- **BRD/RFP v5 commercial Table 6** prices only 5 of the 8 named types as a single lump sum ("Generic and Configurable AI Agent — Mechanical & HVAC, Electrical, Fire Safety, Security and Perimeter, Water and Drainage"), leaving Energy Management, Passenger Flow, and Structural Integrity unpriced.
- **The requirements registers carry 17 `AI-*` rows** (AI-01–AI-17): 6 are platform/governance items, 11 are agent-functional rows that collapse onto the BRD's 8 named agents **except AI-10, a Natural-Language Query Agent with no named counterpart in the BRD's 8-agent table** — though a narrower "GIS Data Viewer... with Natural Language Query Capabilities" line item does appear as a priced deliverable in BRD/RFP v5 Table 1 / Section 1.
- **One stale prior proposal (v9, May-2025) committed to only 7 agents** and is not reused.

We do not average, blend, or silently pick a different count.

## The Eight Federated AI-Driven Agents (BRD §3.5.3)

### 1. Mechanical & HVAC Monitoring Agent (R-066)
**Scope:** AHUs, chillers, cooling towers, BAS. Register AI-06/07/08/09 give a staged go-live scope: load forecasting → waste/fault anomaly detection → degradation trending/RUL → advisory optimisation.
**Performance (R-080):** ≥ 82% precision, ≥ 78% recall, up to 72hr prediction horizon, ≤ 30s alert latency.

### 2. Electrical Systems Monitoring Agent (R-067)
**Scope:** transformers, UPS, switchgear. Register AI-11 notes DGA/insulation-failure prediction is deferred until the MRSS server upgrade completes. The MRSS upgrade is a DIAL-side prerequisite, not a vendor gap.
**Performance (R-081):** ≥ 80% precision, ≥ 75% recall, up to 48hr, ≤ 30s.

### 3. Fire Safety & Life Safety Monitoring Agent (R-068)
**Scope:** multi-sensor correlation, suppression monitoring, evacuation modelling. Register AI-14 clarifies this is **advisory analytics layered over, never replacing, the certified fire system**. We preserve this "advisory, never replacing" framing throughout.

**Performance (R-084):** ≥ 95% precision, ≥ 95% recall, real-time, ≤ 5s — the tightest targets in the table, consistent with life-safety criticality.

### 4. Water & Drainage Monitoring Agent (R-069, R-087)
**Scope:** potable/chilled/grey water, stormwater. Register AI-12 gives go-live scope: roof alerts, pump health, leak indication, stormwater forecasting benchmarked against the Walter P Moore hydrology study.
**Performance target:** **No numeric target exists for this agent anywhere in the requirement corpus.** Confirmed by direct re-read: absent from BRD §3.5.4 **and** independently absent from RFP v5 §6.5 — a genuine gap in the source documents themselves, not an extraction error.

### 5. Energy Management & Sustainability Agent (R-070)
**Scope:** EUI by zone, waste detection, carbon tracking.
**Performance (R-085):** ≥ 80% precision, ≥ 75% recall, up to 24hr, ≤ 60s. Note: this agent is one of the 3 unpriced in BRD Table 6 — see R-124 gap above.

### 6. Passenger Flow Monitoring Agent (R-071)
**Scope:** congestion prediction, ATRS/DFMD monitoring. Register AI-13 adds XOVIS/Kloudspot counter data sources, 45-min forecast horizon. Directly relevant to the ABR Operations department's queue-management asks (R-116).
**Performance (R-082):** ≥ 85% precision, ≥ 80% recall, up to 45min, ≤ 15s. Also unpriced in BRD Table 6 — see R-124.

### 7. Structural Integrity Monitoring Agent (R-072, R-083)
**Scope:** settlement/movement analysis. Register AI-16 flags **"CONDITIONAL SCOPE: cannot start until DIAL procures and installs the SHM sensor network,"** needing a further 6–12 month baseline.
**Deliverability caveat:** roster inclusion is; actual deliverability is.
**Performance (R-083):** ≥ 90% precision, ≥ 85% recall, up to 7 days, ≤ 60s.

### 8. Security & Perimeter Monitoring Agent (R-073)
**Scope:** PSIM/access control/CCTV correlation, crowd density. Register AI-15 flags **"all scope subject to CISF approval before build starts."** CISF approval is an external dependency we flag explicitly.
**Performance (R-086):** ≥ 88% precision, ≥ 82% recall, real-time/15min, ≤ 10s.

## AI Platform & Orchestration Layer

### AI Orchestration Engine (R-075)
Data routing, alert aggregation, priority scoring, cross-agent correlation, zero-downtime agent versioning.

### Shared AI Platform (R-077)
Common ingestion, historian, feature store, model registry, explainability service, alert pipeline, CMMS/AMMS connector — built once.

### Data Readiness Gate (R-076)
Per-domain data audit before any agent build; publish a Data Readiness Report; agree realistic day-1 benchmarks with DIAL.

### MLOps Lifecycle (R-078)
Monthly drift monitoring, quarterly retraining, DIAL approval before release, rolling 90-day KPI window.

### Per-Agent Acceptance (R-079)
Per-agent acceptance against individual §6.5 performance rows on a rolling 90-day window, tied to Milestone M5 / Deliverable D-10.

## AI Model Governance & Transparency (BRD §3.5.5)

DIAL's governance emphasis — repeated across §3.5.5, RFP v5 §6.4, and §9.x — signals that DIAL wants innovation bounded by auditable, explainable, DIAL-owned AI.

| Governance requirement | Our commitment | Marker |
|---|---|---|
| Explainability: plain-language explanation + confidence score (%) on every alert (R-088) | Match | |
| Auditability: complete audit log (input data, model version, timestamp, operator response), minimum 5-year retention (R-089) | Match — distinct from the 2-year user-activity log and the 5-year BMS-historical log (three separate logs) | |
| Feedback loop: operator feedback on alert accuracy feeds retraining (R-090) | Match | |
| Model version control; rollback to prior version within 4 hours (R-091) | Match | |
| DIAL owns all AI model weights and training data generated under contract (R-092) | Match | |
| "No Black Box": deep-learning models must use SHAP/LIME/attention-visualisation interpretability techniques (R-093) | Commit to general explainability per R-088; the specific technique mandate (SHAP/LIME/attention) appears in RFP v5 §6.4 only, not with this specificity in the binding BRD §3.5.5 (which speaks more generally of "contributing factors") | |

## NL Query Agent — Scope-Boundary Flag (R-074)

The requirements registers' AI-10 describes a Natural-Language Query Agent with no counterpart in the BRD's 8-agent table. A narrower "NL query for GIS data retrieval" line item does appear separately as a priced deliverable in BRD/RFP v5 Table 1 / §3.4.6, which we commit to delivering. We **flag the broader platform-wide NL-query-over-full-platform-data interpretation (assets, telemetry, alerts, CMMS, docs) as an open scope-boundary question**, not a silent scope addition or a silent scope drop.

## SPG "What-If" Simulation / Decision-Engine Scope (ABR §4)

The ABR (2-July-2026) devotes its largest section to a dynamic digital twin decision-support / "what-if" simulation engine spanning Commercial/Operational/Engineering domains (24 use cases), with a 4-part architecture (DT for simulation, scenario-control UI, decision engine, visualisation UI). We track this as **its own distinct scope item**, not folded into the 8 AI agents, per coverage-matrix guidance.

**Adjacent precedent:** the Consolidated FINAL proposal references an "IROPs/Disruption Decision Engine," cross-referencing prior Solution Proposal v9 §5.2 — real, if partial and unresolved, adjacent evidence.

**Use-case clusters:**

- **10 Commercial use cases (R-101)** — store-mix optimisation, shelf merchandising, dwell-time monetisation, queue-vs-revenue trade-off, gate allocation, etc.
- **8 Operational use cases (R-102)** — passenger flow optimisation, queue management, check-in/security capacity planning, disruption management, workforce deployment, baggage flow, curbside management.
- **5 Engineering use cases (R-103)** — thermal load simulation, HVAC demand modelling, power infrastructure stress testing.

## Additional ABR Departmental Asks Mapped to the AI Platform

| ABR ask | Agent / capability | Marker |
|---|---|---|
| Borewell recharge monitoring via IoT (P&E, R-104) | General IoT-ingestion capability (R-046) | |
| Storm water analysis with Walter P Moore (P&E, R-105) | Water & Drainage Agent register AI-12 names "benchmarked against the Walter P Moore hydrology study" | |
| Reverse-entry detection in restricted zones (S&V, R-106) | Security & Perimeter Agent access-pattern analytics (R-073) | |
| Unattended baggage detection via video analytics (S&V, R-107) | General video-analytics/AI framing | |
| Behaviour analytics for threat detection (S&V, R-108) | Security & Perimeter Agent (R-073) | |
| Predictive security monitoring (S&V, R-109) | Security & Perimeter Monitoring Agent (R-073) | |
| Security asset mapping (S&V, R-110) | Adjacent GIS capability | |
| Google Maps / satellite integration for landside monitoring (Commercial Aero, R-111) | BRD §3.1.2 Landside Coverage explicitly specifies "aircraft and satellite scans" | |
| Identification of space-allocation changes (Commercial Aero, R-112) | Depends on the land/space-management capability already flagged as a gap (R-039) | |
| GIS-based analytics for planning and utilisation (Commercial Aero, R-113) | Core GIS platform capability | |
| Surface navigation in low-visibility/fog (Operations, R-114) | No evidence of this specific capability anywhere else in the corpus | |
| What-if scenario analytics (Operations, R-115) | Same IROPs/Disruption Decision Engine precedent as R-100 | |
| Monitoring/alerting of DigiYatra, E-Gates, CUSS, CUPPS (Operations, R-116) | These named systems do not appear in PE_OT's 19-system inventory or the BRD's scope at all | |
| Live operations monitoring dashboard (Operations, R-117) | Core APOC/CCC dashboard capability (R-050) | |
| Identification of overstaying/unidentified passengers (Operations, R-118) | Passenger Flow Agent (R-071) + general video-analytics framing | |

## Scalability & Performance

Our RGIA proof point — 40+ integrated systems, 100+ KPIs tracked, 18+ months live operation — is the strongest available evidence that a federated, governed AI-agent layer of this scope has been operated at airport scale. We commit to the BRD's platform-wide predictive accuracy KPI (≥ 80% precision / ≥ 75% recall, BRD §2.3 KPI-4) as the floor for the agent layer as a whole.

---

**Bridge.** The AI architecture above is delivered through the 5-phase implementation methodology and 15-deliverable plan detailed in Volume 4.

---

# Volume 4 — Implementation Methodology and Timeline

## Understanding of the Problem

DIAL's BRD prescribes a structured, phase-gated delivery: 5 phases of approximately 3 months each (~15 months total), 15 numbered deliverables D-01 through D-15, and a 14-calendar-day DIAL review/sign-off period per deliverable. The programme is not a greenfield build — it is an evolution of an existing Concession Agreement toward a digital-twin/agentic-AI capability, layered onto a live, multi-vendor OT estate that must not be disrupted during integration.

## Programme Structure — 5 Phases

| Phase | Months | Scope | Key deliverables |
|---|---|---|---|
| Phase 1 — Geospatial & LiDAR Survey | ~3 mo | Airborne + mobile/indoor LiDAR, orthophotography, DTM/DSM, survey-grade foundation | D-01 to D-03 (LiDAR datasets, survey report) |
| Phase 2 — GIS–BIM Integration & Federated BIM | ~3 mo | LOD 200–350 BIM models, CDE, legacy CAD/DWG migration, clash detection | D-04 to D-06 (BIM models, BEP, migration report) |
| Phase 3 — Facilities Maintenance Management | ~3 mo | Land/space digital footprint, CLM integration, unified BMS/LCMS/ECMS/CMS/FDAS/BHS/HBS/VDGS/VHT/ATRS/DFMD/PBB/WTP-STP/AGL-CMS/IoT platform | D-07 (facilities platform) |
| Phase 4 — Digital Twin Platform | ~3 mo | Modular cloud-native platform, 3D GIS+BIM viewer, BMS/IoT ingestion middleware, APOC/CCC integration, access control, audit logging | D-08 to D-10 (DT platform, integration report, API docs) |
| Phase 5 — AI Agents & Agentic Monitoring | ~3 mo | Shared AI platform, orchestration engine, 8 federated agents, governance/explainability, MLOps | D-10/D-11 (AI platform, agent acceptance) |

**Authoritative schedule caveat:** we adopt the BRD's 15-month structure as authoritative for compliance purposes. We flag explicitly that the Consolidated FINAL proposal's own stated "9-month delivery (Mo1–Mo9), re-baselined to March 2027" does not obviously reconcile with this 15-month structure — possibly a fast-track T2 subset vs. the full programme.

## Deliverables D-01 through D-15 (R-120)

The 15 numbered deliverables span: Project Execution Plan / BIM Execution Plan, LiDAR datasets, BIM models, DT platform, BMS/IoT integration report, AI platform, API documentation, cybersecurity report, training materials, as-built documentation, and post-implementation review. Our RGIA delivery track record supports the process capability to deliver against this deliverable-based structure.

## Deliverable Acceptance (R-121)

Each deliverable is subject to a 14-calendar-day DIAL review/sign-off period before it is accepted and milestone payment is released.

## Dependencies and External Prerequisites We Flag

Honest delivery planning requires naming the prerequisites that sit outside our control:

- **Structural Integrity Agent (R-072, R-083):** cannot start until DIAL procures and installs the SHM sensor network, with a further 6–12 month baseline collection period before predictions are meaningful.
- **Security & Perimeter Agent (R-073):** all scope subject to CISF approval before build starts.
- **Electrical Systems Agent DGA/insulation-failure prediction (R-067):** register AI-11 notes this is deferred until the MRSS server upgrade DIAL is completing.
- **MRSS integration (R-098):** gated on the same GE→Schneider SCADA upgrade.
- **Appendix A (Schedule of Buildings/Areas, R-032) and Appendix B (BEP, R-038):** both "[To be completed by DIAL]" — underlie area-based BIM/LiDAR costing and the BIM execution plan respectively.
- **T2 OT integration scope (R-097):** register marks OEM and/or point count as "X" / "TBD" for most T2 rows.
- **IT-side OneAPOC integrations (R-099) and DigiYatra/E-Gates/CUSS/CUPPS (R-116):** scope boundary with the OneAPOC program unclear.
- **Buffer-zone LiDAR density (R-022):** 8 pts/m² stated in the BRD/RFP but Consolidated FINAL itself annotates "pending DIAL confirmation."
- **Cross-register BIM-modeling schedule conflict:** the two requirements registers systematically disagree on delivery month/phase for nearly every shared `BIMM-*` line item — in one case by ~4 months. Neither file is a clean superset of the other.

## Roles & RACI (R-122)

We commit to a RACI matrix across Planning/Surveys, Platform Development, AI/Analytics, and Operations workstreams, with Vendor (WAISL/GEOKNO) / DIAL / Smart City / DEC roles per BRD §5.

**Term-definition flag:** the BRD uses the abbreviations **"DEC"** and **"POD"** in its RACI tables and body text but does not define either in its own glossary. "DEC" is likely "Design/Engineering Consultant" but unconfirmed; "POD" is undefined. We flag these rather than guess their meaning and request DIAL confirmation.

## Testing & Quality Assurance

Per-agent acceptance testing against the individual BRD §3.5.4 / §6.5 performance rows on a rolling 90-day window, tied to Milestone M5 / Deliverable D-10. Penetration testing of internet-facing components prior to go-live, tied to Deliverable D-12. Full cybersecurity risk assessment prior to deployment, findings submitted for DIAL approval.

## O&M and Support (R-127)

5-year O&M plan with 24×7 support, RTO 4hr / RPO 24hr. Our RGIA 18+ month live O&M track record supports this commitment. The full O&M support ladder (Sev1 ≤ 30min response / 4hr workaround, Sev2 ≤ 1hr / 8hr, Sev3 ≤ 4 business hrs / 5 business days, Sev4 ≤ 1 business day / 30 days) elaborates on the BRD's ≤ 10-minute Critical/Severity-1 headline KPI without contradicting it.

## Exit Management (R-131)

6-month minimum transition support at contract end, no additional cost.

## Regulatory Approvals (R-134)

WAISL is the incumbent Concessionaire already operating under the necessary BCAS, AAI, and other regulatory approvals at IGIA since the 2019 CA; we obtain and maintain all such approvals at our own cost.

---

**Bridge.** The implementation plan above is costed and milestone-structured in Volume 5.

---

# Volume 5 — Commercial Proposal

## Understanding of the Problem

The BRD §6 and RFP v5 §10 define a detailed 8-table costing structure and a 6-milestone payment schedule. This is a negotiated Change Request against an existing Concession Agreement (per BRD §1.2), but the BRD nonetheless specifies a structured commercial framework — this is not a price-only quotation.

## Costing Table Structure (R-123)

We commit to the BRD's 8-table costing structure:

1. **LiDAR survey** — airborne + mobile/indoor, per area unit
2. **BIM modeling by LOD** (200–350) — per asset category, per area unit
3. **Legacy CAD/DWG migration** — per drawing/file or per area unit
4. **BIM–BMS integration** — per data point / per system
5. **Digital Twin viewer** — platform license / build
6. **AI agentic framework** — per agent + shared platform
7. **Infrastructure** — cloud/hosting (India-only), network, security tooling
8. **5-year O&M** — annual recurring]

## AI-Agent Costing Gap (R-124)

The BRD's own Table 6 prices only 5 of the 8 mandatory agent types as a single lump sum ("Generic and Configurable AI Agent — Mechanical & HVAC, Electrical, Fire Safety, Security and Perimeter, Water and Drainage"), leaving **Energy Management, Passenger Flow, and Structural Integrity unpriced**.

## Payment Milestone Schedule (R-125)

| Milestone | % of contract value | Trigger |
|---|---|---|
| M1 | 15% | Project Kick-off / PEP & BEP acceptance (D-01) |
| M2 | 10% | LiDAR survey & BIM models acceptance (D-02–D-04) |
| M3 | 20% | Federated BIM platform / DT platform acceptance (D-05–D-08) |
| M4 | 25% | BMS/IoT integration & APOC/CCC integration acceptance (D-09) |
| M5 | 20% | AI platform & 8-agent acceptance on rolling 90-day window (D-10/D-11) |
| M6 | 10% | Final deliverables, as-built docs, post-implementation review (D-12–D-15) |
| **Total** | **100%** | |

## Warranty and AMC (R-126)

12-month warranty from go-live, with structured Annual Maintenance Contract (AMC) thereafter.

## 5-Year O&M (R-127)

5-year O&M plan, 24×7 support, RTO 4hr / RPO 24hr. Our RGIA 18+ month live O&M track record supports the operational capability. Final O&M unit pricing flagged as placeholder pending bidder input per R-123.

## Material Default and SLA-Linked Penalties (R-135)

We accept the BRD §9.9 material-default framework (3+ SLA breaches in a quarter) and the BRD's breach-related cost/penalty structure as contractual terms. The specific penalty-formula numbers in the Consolidated FINAL proposal are self-labelled "placeholder pending bidder finalisation" and are not committed here.

## Proposal Validity (R-011)

Minimum 180 calendar days from submission.

## IP and SBOM (R-132, R-133)

All deliverables become DIAL's exclusive IP upon milestone payment. Software Bill of Materials (SBOM) for all third-party components.

## Items We Flag as Open for Commercial Finalisation

- Final unit pricing across all 8 costing tables — pending bidder cost-modeling input
- AI-agent costing for the 3 unpriced agents (Energy Management, Passenger Flow, Structural Integrity) — pending DIAL clarification on structure
- Appendix A (Schedule of Buildings/Areas) — pending DIAL input; underlies all area-based BIM/LiDAR costing
- Minimum annual-turnover pre-qualification threshold — unfilled `[X] crore` placeholder in RFP v5 Appendix E
- Buffer-zone LiDAR density (8 pts/m²) — pending DIAL confirmation per R-022

---

**Bridge.** The commercial structure above is underpinned by the qualifications, case study, and organisational evidence presented in Volume 6.

---

# Volume 6 — Qualifications and References

## Understanding of the Problem

RFP v5 Appendix E specifies pre-qualification gates: ≥ 5 years' demonstrated experience in digital twin/BIM/geospatial, ≥ 2 comparable deployments in airport/transport infrastructure/large-scale built environment, ISO 9001:2015 and ISO/IEC 27001:2013 certification, and a minimum annual-turnover threshold (figure unfilled in the source). Volume 6 of the submission additionally requires a minimum of 3 case studies.

We address these honestly, including where evidence is incomplete.

## Pre-Qualification Compliance

| Criterion | Requirement | Our Status | Marker |
|---|---|---|---|
| Years of experience in digital twin/BIM/geospatial (R-006) | ≥ 5 years | **Met** — WAISL is the incumbent Concessionaire at IGIA under the CA dated 30-Sep-2019, well over 5 years by any reading | |
| Comparable deployments (R-007) | ≥ 2 in airport/transport/large-scale built environment | **Partially met — 1 of 2 evidenced.** Only RGIA (Hyderabad) is fully evidenced. | |
| ISO 9001:2015 QMS (R-008) | Current and valid | **Met** | |
| ISO/IEC 27001:2013 ISMS (R-009) | Current and valid | **Met** | |
| Annual turnover ≥ INR [X] crore (R-010) | Each of last 3 FY, audited | **Cannot confirm** — the threshold is an unfilled `[X] crore` placeholder in the source document itself | |

## Organisational Profile (R-130)

**WAISL Limited** is the incumbent IT-services Concessionaire at IGIA, operating under the Concession Agreement dated 30-September-2019, with **GEOKNO** as its geospatial/LiDAR/BIM delivery partner.

WAISL's multi-country footprint spans India, UAE, US, UK, Singapore, Greece, and Kuwait. WAISL holds ISO 9001, ISO 20000, ISO 27001, ISO 22301, and CMMI ML3 certifications.

## Case Studies (R-128)

RFP v5 §9.3 / Volume 6 requires a minimum of 3 case studies. We present what we have and explicitly mark what we do not.

### Case Study 1 — Rajiv Gandhi International Airport (RGIA), Hyderabad

**Relevance to this engagement:** RGIA is a direct operational analog — a live airport digital-twin/AIOP deployment integrating a heterogeneous, multi-vendor OT estate into a unified monitoring platform with federated AI agents.

**Scope:** Airport Eye platform deployment — Geo Digital Twin + Operational Digital Twin / AIOP architecture, hub-and-spoke BMS/IoT integration fabric.

**Scale:** 40+ integrated systems, 100+ KPIs tracked, 18+ months live operation.

**Outcome:** Live, stable operation across a multi-OEM OT estate comparable in complexity (though smaller in absolute scale) to IGIA's 19-system estate.

**Key parallel:** The hub-and-spoke integration fabric proven at RGIA is the direct architectural precedent for the BMS/IoT ingestion middleware DIAL requires (BRD §3.4.2 — BACnet/IP, BACnet MSTP, Modbus TCP/RTU, MQTT, SNMP, OPC-UA, REST).

### Case Study 2 — [Placeholder — bidder input]

**Relevance to this engagement:** [To be evidenced.]". We do not fabricate a case study. We seek additional case-study collateral from the capture team before the proposal-assembler stage. This is a conditional-Disqualifying gap if the RFP v5 competitive submission structure is operative (per R-001).]

### Case Study 3 — [Placeholder — bidder input]

**Relevance to this engagement:** [To be evidenced.]

## Adjacent Prior Engagement — APOC/AODB Integration (narrower scope)

The `DIAL APOC Phase II Proposal 1.pdf.md` documents a real, named prior WAISL + KloudSpot engagement at DIAL for a KPI-dashboard / video-analytics / AODB integration project. This is genuine adjacent precedent for the APOC/CCC integration requirement (R-050) — but it is **not** a comparable Airport Eye deployment (no digital twin, no LiDAR, no AI agents in the current sense) and is therefore not counted toward the ≥ 2 comparable-deployment pre-qualification gate.

## Certifications Summary

| Certification | Held | Relevance |
|---|---|---|
| ISO 9001:2015 (QMS) | Yes | Pre-qualification R-008; general delivery maturity |
| ISO 20000 (IT Service Management) | Yes | O&M / service-management maturity |
| ISO/IEC 27001:2013 (ISMS) | Yes | Pre-qualification R-009; information-security baseline |
| ISO 22301 (Business Continuity) | Yes | Adjacent to OT resilience requirements |
| CMMI ML3 | Yes | Process maturity |
| IEC 62443 (OT/ICS cybersecurity) | **No** | Required by BRD §3.4.5 / RFP v5 §4.2 — see Volume 2 Cybersecurity gap (R-056) |

---

**Bridge.** The qualifications above are delivered by the team presented — honestly, including its gaps — in Volume 7.

---

# Volume 7 — Team & Staffing

## Understanding of the Problem

RFP v5 §9.3 (Volume 7) requires CVs of key personnel, technical architects, and named project leads. A competent response names the individuals who will deliver the Airport Eye platform, with their qualifications and relevant prior experience.

## The Honest Gap

**No named personnel, CVs, role-specific qualifications, or staffing plan for our own delivery team appear in any of the reviewed collateral documents.** This is a complete blank, not a thin spot.

We do not fabricate placeholder bios. The task instruction is explicit: do not invent names or CVs. Fabrication is the single most damaging thing a proposal can do — an evaluator reading alongside competitors can tell the difference between a vendor who has done this and one improvising.

## What We Can Commit To — Staffing-Plan Skeleton

While we cannot name individuals without capture-team input, we commit to the following staffing-plan structure and role coverage, aligned to the 5-phase programme and 15 deliverables in Volume 4:

| Role | Phase coverage | Key responsibilities | Required qualifications |
|---|---|---|---|
| Programme Director / Project Lead | All phases | Overall delivery accountability, DIAL single-point-of-contact, milestone sign-off | ≥ 15 years airport/OT programme delivery; prior WAISL/GEOKNO airport engagement |
| BIM / Geospatial Delivery Lead (GEOKNO) | Phase 1–3 | LiDAR survey, BIM modeling, ISO 19650 compliance, CDE | ISO 19650 experience; survey-grade LiDAR/BIM delivery track record |
| Digital Twin Platform Architect | Phase 4 | Cloud-native architecture, 3D GIS+BIM viewer, ingestion middleware, APOC/CCC integration | DTDL/semantic-data-model expertise; prior DT platform build |
| AI/ML Lead | Phase 5 | Shared AI platform, orchestration engine, 8-agent build, MLOps, governance | Production ML/AI at airport/OT scale; explainability/audit experience |
| Cybersecurity Lead | All phases | IEC 62443 roadmap, network segmentation, SOC/SIEM, penetration testing, breach response | IEC 62443 (or roadmap to certify); ISO 27001 background |
| OT/BMS Integration Lead | Phase 3–4 | 19-system integration, protocol handling (BACnet/Modbus/MQTT/OPC-UA), point migration | Multi-OEM OT integration experience |
| Operations & O&M Lead | Phase 5 + 5-year O&M | 24×7 support, SLA management, MLOps drift monitoring, exit management | Live airport O&M track record |

## Subcontractor / Partner Roles

| Partner | Role | Relevant qualification |
|---|---|---|
| GEOKNO | Geospatial/LiDAR/BIM delivery partner | |
| IEC 62443 specialist subcontractor (to be named) | OT cybersecurity compliance roadmap | |
| SOC/SIEM service partner (to be named) | Continuous security monitoring | |

## RACI Commitment (R-122)

We commit to a RACI matrix across Planning/Surveys, Platform Development, AI/Analytics, and Operations workstreams with Vendor (WAISL/GEOKNO) / DIAL / Smart City / DEC roles per BRD §5, to be populated with named individuals once capture-team input is received. We flag that the BRD's "DEC" and "POD" abbreviations are undefined in its glossary and request DIAL confirmation of their meaning.

## Path to Close This Gap

This section cannot be completed from assertion alone. We request from the capture team, before the proposal-assembler stage:

1. Named Programme Director / Project Lead with CV
2. Named BIM/Geospatial Delivery Lead (GEOKNO) with CV and ISO 19650 evidence
3. Named Digital Twin Platform Architect with CV
4. Named AI/ML Lead with CV and prior airport/OT AI deployment evidence
5. Named Cybersecurity Lead with IEC 62443 certification or documented roadmap
6. Named OT/BMS Integration Lead with CV
7. Named Operations & O&M Lead with CV
8. Named IEC 62443 specialist subcontractor/partner
9. Named SOC/SIEM service partner

---

**Bridge.** The team above, once populated, delivers the 15 deliverables across 5 phases costed in Volumes 4 and 5. Appendices carry the requirements traceability matrix that maps every requirement in this submission to its evidence marker.

---

# Appendices — Requirements Traceability Matrix

## Purpose

This appendix maps the 135 requirements (R-001 through R-135) classified in the coverage matrix to the volume, section, and evidence marker where each is addressed in this submission. It is the compliance validator's index.

## Evidence-Marker Legend

- `[GROUNDED: <source>]` — claim directly supported by evidence in the brief, coverage matrix, or named collateral.
- `[ASSERTION: <rationale>]` — reasonable claim without direct evidentiary support; rationale stated.
- `[GAP]` — requirement cannot be credibly addressed with current evidence; acknowledged honestly, not fabricated.

## Requirements Traceability Matrix

| ID | Requirement (short) | Volume / Section | Marker | Notes |
|---|---|---|---|---|
| R-001 | Procurement mechanism (competitive RFP vs negotiated CR) | V1 §Procurement Framing | [GAP] | Flagged, not silently resolved; conservative RFP v5 structure adopted as default |
| R-002 | Evaluation weights 30/25/20/15/10 | V1 §Procurement Framing | [ASSERTION] | Operative pending R-001 resolution |
| R-003 | 3-stage evaluation panel | V1 §Procurement Framing | [ASSERTION] | Same R-001 caveat |
| R-004 | 7-volume submission structure | V1–V7 | [ASSERTION] | Followed as structural default per gap-report recommendation |
| R-005 | Volume 1 page limit 10 pages | V1 | [ASSERTION] | Complied with; no other limits stated |
| R-006 | ≥5 years digital twin/BIM/geospatial experience | V6 §Pre-Qualification | [GROUNDED] | WAISL incumbent since 30-Sep-2019 CA |
| R-007 | ≥2 comparable deployments | V6 §Pre-Qualification, §Case Studies | [GAP] | Only RGIA evidenced — conditional Disqualifying |
| R-008 | ISO 9001:2015 | V6 §Pre-Qualification, §Certifications | [GROUNDED] | WAISL holds |
| R-009 | ISO/IEC 27001:2013 | V6 §Pre-Qualification, §Certifications | [GROUNDED] | WAISL holds |
| R-010 | Annual turnover ≥ INR [X] crore | V6 §Pre-Qualification, V5 §Open Items | [GAP] | Unfilled placeholder in source itself |
| R-011 | 180-day proposal validity | V5 §Proposal Validity | [ASSERTION] | Standard commercial commitment |
| R-012 | Uptime ≥ 99.5% | V1 §Headline Commitments | [GROUNDED] | BRD §2.3 KPI-1 |
| R-013 | Latency ≤ 5s | V1 §Headline Commitments | [GROUNDED] | BRD §2.3 KPI-2 |
| R-014 | BIM LOD compliance 100% | V1 §Headline Commitments | [GROUNDED] | BRD §2.3 KPI-3 |
| R-015 | Predictive alert accuracy ≥80%/≥75% | V1 §Headline Commitments, V3 §Scalability | [GROUNDED] | BRD §2.3 KPI-4; register AI-05 |
| R-016 | Geospatial accuracy ≤5cm/≤3cm RMSE | V1 §Headline Commitments, V2 §Component 1 | [GROUNDED] | BRD §2.3 KPI-5 |
| R-017 | Critical incident response ≤10 min | V1 §Headline Commitments, V4 §O&M | [GROUNDED] | BRD §2.3 KPI-6; RFP v5 ≤1hr superseded |
| R-018 | Integration coverage 100% within 3 months | V1 §Headline Commitments | [GROUNDED] | BRD §2.3 KPI-7 |
| R-019 | Six primary objectives | V2 §Proposed Solution | [GROUNDED] | Consolidated FINAL addresses all six |
| R-020 | 15-year lifecycle, modular cloud-native | V2 §Component 4 | [ASSERTION] | Architecture direction plausible; no explicit 15-year commitment evidenced |
| R-021 | LiDAR core ≥20 pts/m² | V2 §Component 1 | [GROUNDED] | BRD §3.1.1 |
| R-022 | Buffer 8 pts/m² | V2 §Component 1, V5 §Open Items | [ASSERTION] | Pending DIAL confirmation per Consolidated FINAL |
| R-023 | Horizontal RMSE ≤5cm | V2 §Component 1 | [GROUNDED] | BRD §3.1.1 |
| R-024 | Vertical RMSE ≤3cm | V2 §Component 1 | [GROUNDED] | BRD §3.1.1 |
| R-025 | Orthophoto GSD ≤5cm | V2 §Component 1 | [GROUNDED] | BRD §3.1.1 |
| R-026 | DTM/DSM 10cm grid | V2 §Component 1 | [GROUNDED] | BRD §3.1.1 |
| R-027 | Indoor positional accuracy ≤5cm | V2 §Component 1 | [GROUNDED] | BRD §3.1.5 |
| R-028 | Indoor scanning density [X] pts/m² | V2 §Component 1 | [GAP] | Unfilled placeholder in RFP v5 §3.2.1 |
| R-029 | LOD 200–350, 10-category BIM | V2 §Component 1 | [GROUNDED] | BRD §3.1.8 / RFP v5 §3.2.3 |
| R-030 | ISO 19650 compliance | V2 §Component 1 | [ASSERTION] | GEOKNO as BIM partner; no named certification |
| R-031 | IFC 4.0 (ISO 16739) | V2 §Component 1 | [ASSERTION] | Industry-standard; no specific certification |
| R-032 | Appendix A Schedule of Buildings/Areas | V2 §Component 1, V5 §Open Items | [GAP] | "[To be completed by DIAL]" |
| R-033 | Automated clash detection | V2 §Component 2 | [ASSERTION] | Standard federated-BIM capability |
| R-034 | Version control / audit trail | V2 §Component 2 | [ASSERTION] | Standard |
| R-035 | RBAC on BIM CDE | V2 §Component 2 | [ASSERTION] | RBAC evidenced at DT viewer, not specifically BIM CDE |
| R-036 | API integration BIM/DT/AI | V2 §Component 2 | [GROUNDED] | Two-layer architecture |
| R-037 | Legacy CAD/DWG migration | V2 §Component 2 | [ASSERTION] | Adjacent — RGIA plausibly included similar |
| R-038 | Appendix B BEP | V2 §Component 2, V5 §Open Items | [GAP] | "[To be completed by DIAL]" |
| R-039 | Land/space digital footprint (DIAL legal vocabulary) | V2 §Component 3 | [GAP] | No land/space module evidenced |
| R-040 | CLM integration | V2 §Component 3 | [GAP] | No named CLM evidence |
| R-041 | Single platform 13+ system families | V2 §Component 3 | [GROUNDED] | RGIA 40+ systems hub-and-spoke |
| R-042 | IoT sensor inventory ingestion | V2 §Component 3 | [GROUNDED] | Middleware capability; sensor counts DIAL-provided |
| R-043 | Environmental monitoring | V2 §Component 3 | [ASSERTION] | Adjacent GIS extension |
| R-044 | Modular cloud-native platform | V2 §Component 4 | [GROUNDED] | Two-layer architecture |
| R-045 | 3D GIS+BIM viewer, AR/VR, offline mobile | V2 §Component 4 | [ASSERTION] | Core viewer Grounded; AR/VR + offline asserted |
| R-046 | BMS/IoT middleware protocol list | V2 §Component 4, §Integration | [GROUNDED] | RGIA proof point |
| R-047 | DTDL semantic data model | V2 §Component 4 | [ASSERTION] | No DTDL-specific evidence |
| R-048 | BMS point → BIM element mapping | V2 §Component 4 | [GROUNDED] | Core to two-layer DT |
| R-049 | 5-year BMS historical retention | V2 §Component 4 | [GROUNDED] | Consolidated FINAL commits |
| R-050 | APOC/CCC integration REST/GraphQL/WebSocket | V2 §Component 4 | [GROUNDED] | APOC Phase II proposal is real adjacent precedent (hosting language excluded) |
| R-051 | MFA + RBAC 5 roles | V2 §Component 4 | [GROUNDED] | Consolidated FINAL matches BRD |
| R-052 | SSO SAML 2.0 / OAuth 2.0 | V2 §Component 4 | [ASSERTION] | Standard capability |
| R-053 | TLS 1.3 / AES-256 | V2 §Component 4 | [GROUNDED] | BRD governs over register's TLS 1.2+ |
| R-054 | 2-year activity audit log | V2 §Component 4 | [GROUNDED] | Consolidated FINAL commits |
| R-055 | Outdoor 3D GIS multi-department layering | V2 §Component 4 | [ASSERTION] | Adjacent GEOKNO GIS capability |
| R-056 | IEC 62443 compliance | V2 §Component 5 | [GAP] | No certification; roadmap + partner mitigation |
| R-057 | Network segmentation | V2 §Component 5 | [ASSERTION] | Standard OT practice |
| R-058 | Penetration testing pre-go-live | V2 §Component 5, V4 §Testing | [ASSERTION] | Standard; tied to D-12 |
| R-059 | SOC/SIEM | V2 §Component 5, V7 §Partners | [GAP] | No track record; partner-led mitigation |
| R-060 | Cybersecurity risk assessment | V2 §Component 5, V4 §Testing | [ASSERTION] | Standard; tied to D-12 |
| R-061 | India-only data sovereignty | V2 §Component 5 | [GROUNDED] | Consolidated FINAL; APOC Phase II Singapore hosting excluded |
| R-062 | DPDP Act 2023 | V2 §Component 5 | [GROUNDED] | Consolidated FINAL commits |
| R-063 | 12-hour breach notification | V2 §Component 5 | [GROUNDED] | BRD §9.11; Consolidated FINAL matches |
| R-064 | Vendor bears breach costs | V2 §Component 5 | [ASSERTION] | Contract-term acceptance |
| R-065 | Authoritative AI-agent roster | V3 §Roster Ambiguity | [ASSERTION] | BRD 8 adopted; divergences flagged |
| R-066 | Mechanical & HVAC Agent | V3 §Agent 1 | [GROUNDED] | BRD §3.5.3; register AI-06/07/08/09 |
| R-067 | Electrical Systems Agent | V3 §Agent 2 | [GROUNDED] | BRD §3.5.3; register AI-11; MRSS dependency flagged |
| R-068 | Fire Safety Agent (advisory, never replacing) | V3 §Agent 3 | [GROUNDED] | BRD §3.5.3; register AI-14 |
| R-069 | Water & Drainage Agent (scope) | V3 §Agent 4 | [GROUNDED] | BRD §3.5.3; register AI-12; Walter P Moore |
| R-070 | Energy Management Agent | V3 §Agent 5 | [GROUNDED] | BRD §3.5.3; register AI-06 |
| R-071 | Passenger Flow Agent | V3 §Agent 6 | [GROUNDED] | BRD §3.5.3; register AI-13 |
| R-072 | Structural Integrity Agent (SHM-dependent) | V3 §Agent 7 | [ASSERTION] | Roster Grounded; deliverability contingent on DIAL SHM network |
| R-073 | Security & Perimeter Agent (CISF-dependent) | V3 §Agent 8 | [GROUNDED] | CISF approval flagged |
| R-074 | NL Query Agent (AI-10) | V3 §NL Query Agent | [GAP] | Broader interpretation flagged; narrower GIS-NL line item Grounded |
| R-075 | AI Orchestration Engine | V3 §Orchestration | [GROUNDED] | BRD §3.5.2; register AI-03 |
| R-076 | Data Readiness Gate | V3 §Platform | [ASSERTION] | Standard practice; register AI-01 |
| R-077 | Shared AI Platform | V3 §Platform | [GROUNDED] | Register AI-02; same as R-075 |
| R-078 | MLOps lifecycle | V3 §Platform, V4 §Testing | [ASSERTION] | Standard MLOps; register AI-05 |
| R-079 | Per-agent acceptance | V3 §Platform, V4 §Testing | [ASSERTION] | Standard; register AI-17 |
| R-080 | Mech&HVAC performance SLAs | V3 §Agent 1 | [GROUNDED] | BRD §3.5.4; verify-flag caveat |
| R-081 | Electrical performance SLAs | V3 §Agent 2 | [GROUNDED] | BRD §3.5.4; verify-flag caveat |
| R-082 | Passenger Flow performance SLAs | V3 §Agent 6 | [GROUNDED] | BRD §3.5.4; verify-flag caveat |
| R-083 | Structural Integrity performance SLAs | V3 §Agent 7 | [GROUNDED] | BRD §3.5.4; verify-flag + SHM dependency |
| R-084 | Fire Safety performance SLAs | V3 §Agent 3 | [GROUNDED] | BRD §3.5.4; verify-flag caveat |
| R-085 | Energy Management performance SLAs | V3 §Agent 5 | [GROUNDED] | BRD §3.5.4; verify-flag caveat |
| R-086 | Security performance SLAs | V3 §Agent 8 | [GROUNDED] | BRD §3.5.4; verify-flag caveat |
| R-087 | Water & Drainage performance target | V3 §Agent 4 | [GAP] | Absent from source documents themselves |
| R-088 | Explainability + confidence | V3 §Governance | [GROUNDED] | BRD §3.5.5; Consolidated FINAL |
| R-089 | Auditability 5-year AI-alert log | V3 §Governance | [GROUNDED] | BRD §3.5.5; Consolidated FINAL |
| R-090 | Feedback loop | V3 §Governance | [GROUNDED] | BRD §3.5.5; Consolidated FINAL |
| R-091 | Model version control + 4hr rollback | V3 §Governance | [GROUNDED] | BRD §3.5.5; Consolidated FINAL |
| R-092 | DIAL owns model weights/training data | V3 §Governance | [GROUNDED] | BRD §3.5.5; Consolidated FINAL |
| R-093 | SHAP/LIME/attention "No Black Box" | V3 §Governance | [ASSERTION] | Technique mandate is RFP v5-specific; BRD speaks generally |
| R-094 | 19-system "Not integrated" estate | V2 §Understanding, V3 §Scalability | [GROUNDED] | PE_OT inventory — best-evidenced problem-statement fact |
| R-095 | T1 OT integration | V2 §Integration | [GROUNDED] | Middleware + RGIA; point counts DIAL-provided |
| R-096 | T3 OT integration | V2 §Integration | [GROUNDED] | Same; largest scale |
| R-097 | T2 OT integration | V2 §Integration, V4 §Dependencies | [GAP] | Register marks TBD/X — flagged to DIAL |
| R-098 | Common integrations (WTP/STP/MRSS/AGL CMS/ITBMS) | V2 §Integration | [GROUNDED] | MRSS upgrade dependency flagged |
| R-099 | IT-side OneAPOC integrations | V2 §Integration, V4 §Dependencies | [GAP] | Scope boundary unclear; seek DIAL clarification |
| R-100 | SPG what-if simulation engine | V3 §SPG | [ASSERTION] | IROPs/Decision Engine precedent; full 24-use-case not built |
| R-101 | 10 Commercial use cases | V3 §SPG | [GAP] | Illustrative; phased roadmap proposed |
| R-102 | 8 Operational use cases | V3 §SPG | [GAP] | Partially adjacent to Passenger Flow Agent |
| R-103 | 5 Engineering use cases | V3 §SPG | [GAP] | No simulation capability evidenced |
| R-104 | Borewell recharge IoT | V3 §ABR Mapping | [ASSERTION] | Adjacent IoT ingestion |
| R-105 | Storm water + Walter P Moore | V3 §ABR Mapping | [GROUNDED] | Register AI-12 names Walter P Moore |
| R-106 | Reverse-entry detection | V3 §ABR Mapping | [ASSERTION] | Adjacent Security Agent |
| R-107 | Unattended baggage detection | V3 §ABR Mapping | [ASSERTION] | Adjacent video analytics |
| R-108 | Behaviour analytics | V3 §ABR Mapping | [ASSERTION] | Adjacent Security Agent |
| R-109 | Predictive security monitoring | V3 §ABR Mapping | [GROUNDED] | Overlaps Security Agent R-073 |
| R-110 | Security asset mapping | V3 §ABR Mapping | [ASSERTION] | Adjacent GIS |
| R-111 | Google Maps/satellite landside | V3 §ABR Mapping | [GROUNDED] | BRD §3.1.2 "aircraft and satellite scans" |
| R-112 | Space-allocation changes | V3 §ABR Mapping | [GAP] | Depends on R-039 land/space gap |
| R-113 | GIS analytics for planning | V3 §ABR Mapping | [GROUNDED] | Core GIS capability |
| R-114 | Fog/low-visibility surface navigation | V3 §ABR Mapping | [GAP] | Niche ABR-only ask |
| R-115 | What-if scenario analytics (Ops) | V3 §ABR Mapping | [ASSERTION] | Same as R-100 |
| R-116 | DigiYatra/E-Gates/CUSS/CUPPS | V3 §ABR Mapping, V4 §Dependencies | [GAP] | Not in PE_OT or BRD scope; seek clarification |
| R-117 | Live ops dashboard | V3 §ABR Mapping | [GROUNDED] | Core APOC/CCC dashboard (R-050) |
| R-118 | Overstaying/unidentified passengers | V3 §ABR Mapping | [ASSERTION] | Adjacent Passenger Flow Agent |
| R-119 | 5-phase ~15-month programme | V4 §Programme Structure | [ASSERTION] | BRD structure authoritative; 9-month Consolidated FINAL figure flagged |
| R-120 | 15 deliverables D-01–D-15 | V4 §Deliverables | [GROUNDED] | BRD §4.2 / RFP v5 §5.2 identical |
| R-121 | 14-day DIAL review per deliverable | V4 §Deliverable Acceptance | [ASSERTION] | Standard per BRD §4.2 |
| R-122 | RACI matrix | V4 §RACI, V7 §RACI | [ASSERTION] | Structure committed; DEC/POD undefined in BRD glossary |
| R-123 | 8-table costing structure | V5 §Costing Structure | [ASSERTION] | Structure solid; final pricing requires bidder input |
| R-124 | AI-agent costing (3 unpriced) | V5 §AI-Agent Costing Gap | [GAP] | Source-document internal inconsistency |
| R-125 | 6-milestone payment 15/10/20/25/20/10 | V5 §Payment Milestones | [GROUNDED] | BRD §7 / RFP v5 §9.4 identical |
| R-126 | 12-month warranty + AMC | V5 §Warranty | [ASSERTION] | Standard per RFP v5 §9.5 |
| R-127 | 5-year O&M, 24×7, RTO 4hr/RPO 24hr | V4 §O&M, V5 §5-Year O&M | [GROUNDED] | Register NFR; RGIA track record supports |
| R-128 | ≥3 case studies | V6 §Case Studies | [GAP] | Only RGIA evidenced; 2 placeholders |
| R-129 | CVs / key personnel | V7 | [GAP] | Complete blank; skeleton only, no fabrication |
| R-130 | Company profile / org references | V6 §Org Profile | [ASSERTION] | WAISL footprint asserted, not tied to comparable deployments |
| R-131 | 6-month exit support | V4 §Exit Management | [GROUNDED] | BRD §9.12; Consolidated FINAL commits |
| R-132 | DIAL exclusive IP on deliverables | V5 §IP | [ASSERTION] | Standard legal commitment |
| R-133 | SBOM | V5 §IP | [ASSERTION] | Standard practice |
| R-134 | Regulatory approvals at vendor cost | V4 §Regulatory Approvals | [GROUNDED] | WAISL incumbent under these approvals since 2019 |
| R-135 | Material default 3+ SLA breaches/quarter | V5 §Material Default | [ASSERTION] | Contractual risk-term acceptance |

## Summary of Evidence Markers Across This Submission

| Marker type | Approximate count |
|---|---|
| `[GROUNDED: ...]` | ~95 |
| `[ASSERTION: ...]` | ~55 |
| `[GAP]` | ~22 (covering the 22 Gap-classified requirements, several referenced in multiple volumes) |

## Excluded Sources (per task constraint)

The following sources were not read or used anywhere in this submission:
- `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`
- `AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`

The following source was used only for non-hosting, non-SLA-ladder, non-commercial content, per task constraint:
- `DIAL APOC Phase II Proposal 1.pdf.md` — its AWS Singapore-region DR hosting language (contradicts BRD §9.10), its P1–P4 SLA ladder (incompatible with BRD §9.11 / §2.3 ≤10-min), and its commercial figures (₹9.02cr/₹11.08cr for a narrower engagement) were explicitly excluded from reuse.
