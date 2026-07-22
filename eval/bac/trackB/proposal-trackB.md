# Pre-Flight Checklist

**Assembly Date:** 2026-07-17
**Status:** Ready for Review (draft — declared gaps with committed resolution paths are acceptable for this draft)

## Document Completeness

- [x] All 14 RFP-aligned sections present (01-14)
- [x] Cover page included
- [x] Table of contents generated
- [ ] Contact information: vendor primary contact to be supplied (placeholder below) — must be added before submission
- [ ] Referenced appendices: no separate appendices drafted; placeholders flagged where referenced

## Compliance Status

- [x] Compliance posture summarised in Section 11; disqualifying gaps (FR17, FR20, NF19, ISRA-19, ISRA-25) each have a committed resolution path
- [ ] Compliance validation via compliance-validator not re-run on this assembled draft; run before submission
- Warnings: 5 disqualifying gaps declared with committed delivery/resolution paths (acceptable for a draft; must be closed or accepted before final submission)

## Evidence Quality

- Grounded claims: 167
- Assertions (architecturally reasonable, unsubstantiated): 123
- Declared gaps: 124
- Grounding ratio (grounded / (grounded + assertions)): 58%
- Note: Markers stripped from assembled prose; counts derived from pre-strip section files.

## Unresolved Items

- [ ] Vendor primary contact name/title/email/phone (placeholder in cover page)
- [ ] Schedule A: insurance certificates of currency; ISO 9001/20000/27001/22301 certificate evidence; sub-contractor identification
- [ ] Schedule C: two referees; named key personnel and resumes; case studies
- [ ] Schedule E: full 5-year pricing breakdown (Implementation, Integrations, Hardware, License, Support, Maintenance, Additional)
- [ ] NF09/NF10: QA standards/tools/methodology documentation from WAISL internal QA process
- [ ] NF05: 3-year availability history (committed to SLA reporting going forward)
- [ ] Hosting target confirmation (AWS Sydney ap-southeast-2 vs BAC private cloud) — open question to close at Initiation
- [ ] Camera-model list (FR01) — BAC to confirm supported models
- [ ] Phase-2 scope confirmation (FR72 aerobridge pax counting; FR73 mobile/tablet) — Must-Have in this contract or deferred
- [ ] Civil/hardware install cost responsibility (BAC or supplier)
- [ ] Reframe Turnwise examples (IST-NAP route, non-Australian registrations) to BNE before submission
- [ ] Authorised signature on required forms; final formatting in submission format (Excel response sheet + optional 5-page PDF)
- [ ] Submission method and deadline confirmed per RFP §4.2 (proposals valid 90 calendar days)

## Page Count Estimate

The RFP permits an Excel response sheet plus an optional single PDF of no more than 5 pages (§8). This assembled narrative is the working technical draft behind the response; it will be compressed into the 5-page optional PDF and the Excel Response Sheet entries. No per-section page limit applies to the internal draft; the submission-format limit is 5 PDF pages plus the Excel sheet.

| Section | Draft word estimate | Status |
|---------|----------------------|--------|
| 01 Executive Summary | ~600 | OK |
| 02 Understanding of Requirements | ~850 | OK |
| 03 Technical Solution | ~2,400 | OK |
| 04 Scope Coverage and Deliverables | ~1,300 | OK |
| 05 Implementation Methodology | ~750 | OK |
| 06 Project Management and Governance | ~700 | OK |
| 07 Integration, Data, and Technical Approach | ~650 | OK |
| 08 Security, ISRA, and Compliance | ~1,700 | OK |
| 09 Testing, Acceptance, and Handover | ~600 | OK |
| 10 Support, SLA, and Maintenance | ~750 | OK |
| 11 Compliance with Tab.F Requirements | ~900 | OK |
| 12 Commercial and Insurance Response | ~550 | OK |
| 13 Deviation, Clarifications, and Assumptions Register | ~1,300 | OK |
| 14 Relevant Experience | ~700 | OK |
| **Total (draft)** | **~10,086** | Internal draft |

## Before Submission

- [ ] Human review of all assertions for accuracy
- [ ] Final formatting in submission format (Excel Response Sheet + optional 5-page PDF; no sales brochures per §8)
- [ ] Appendix/completion: supply Schedule A/C/E content; insurance and ISO certificates; referees and named personnel
- [ ] Pricing volume preparation (Schedule E)
- [ ] Authorised signature on required forms
- [ ] Submission method and deadline confirmed

---

# BAC Underwing Analytics Solution

**In Response To:** BAC-T-26-505 — Underwing Analytics Request for Proposal
**Submitted To:** Brisbane Airport Corporation Pty Limited (BAC)
**Submitted By:** WAISL (operating through its Australia office, with delivery partner for camera/computer-vision elements)
**Date:** 2026-07-17

**Primary Contact:**
[PLACEHOLDER — vendor primary contact name, title, email, phone, address to be supplied before submission]

**BAC Contact Officer:** Leighton Walker, Technology Project Manager

**Contract Vehicle:** BAC Relationship / Master Services Agreement (Annexure B); 3-year initial term with two by-one-year extensions (RFP §4.3)

**Proposal Validity:** 90 calendar days from Proposal Closing Time (RFP §4.2; Annexure A §1)

---

# Table of Contents

1. 01 — Executive Summary
2. 02 — Understanding of Requirements
3. 03 — Technical Solution
4. 04 — Scope Coverage and Deliverables
5. 05 — Implementation Methodology
6. 06 — Project Management and Governance
7. 07 — Integration, Data, and Technical Approach
8. 08 — Security, ISRA, and Compliance
9. 09 — Testing, Acceptance, and Handover
10. 10 — Support, SLA, and Maintenance
11. 11 — Compliance with Tab.F Requirements
12. 12 — Commercial and Insurance Response
13. 13 — Deviation, Clarifications, and Assumptions Register
14. 14 — Relevant Experience


# 01: Executive Summary

## BAC's problem, in BAC's words

Brisbane Airport Corporation (BAC) is procuring an enterprise-grade underwing analytics solution that "automatically detect[s], classif[ies], timestamp[s], sequence[s], and analyse[s] underwing activities" using "fixed camera infrastructure, advanced video analytics, and artificial intelligence" (RFP §3.2). The objective is to replace manual timestamping and subjective reporting with "objective, auditable, and defensible operational data aligned with BAC's airport systems" — a single source of truth for Terminal Operations and Airside Operations across BNE's apron.

The scope is broad and compliance-heavy: 73 functional requirements (69 Must-Have), 48 non-functional, 20 project-management, and 29 ISRA rows in Tab.F, plus insurance bars of $20M public liability, $10M professional indemnity, and $10M cyber. Twenty per cent of the lump sum is withheld until practical completion (PMR-09), signalling that BAC protects itself on delivery.

## What WAISL proposes

WAISL, operating through its Australia office and alongside its delivery partner, proposes a Turnwise/UTAM-based underwing analytics platform delivered as a managed service for BNE. The platform already performs real-time aircraft/stand/turnaround tracking, CDM milestone monitoring, GSE and vehicle tracking, configurable alerts, dashboards, KPI and SLA reporting, playback, geofenced zone monitoring, and AODB/ADS-B/telematics/weather/RVR integration — capabilities that directly address the operational-visibility and integration backbone of the RFP.

The solution is parameterised over code, deployable in AWS cloud or BAC private cloud, secured under a zero-trust architecture with ISO 27001-certified ISMS controls, and delivered against RTO ≤40 minutes and RPO near-zero.

## Where we are strong and where we are honest

We are directly grounded against approximately 44% of Tab.F (turnaround timeline, CDM milestones, dashboards, alerts, AODB/REST APIs, RBAC/ABAC, SSO/MFA, HA/DR, audit, ISO 27001, escrow, change management). A further 38% is assertable from the platform's configurable architecture.

We will not overstate. Five areas require explicit treatment in this proposal:

1. **Camera-AI detection of the full GSE-type list (FR17) and personnel presence in apron zones (FR20).** Our current GSE evidence is telematics/GPS-based, not camera-classified against every enumerated type, and personnel presence via camera is not yet evidenced in our collateral. We address these honestly in Section 03 and 13, with a delivery roadmap, computer-vision model commitments, and acceptance criteria — not fabricated claims.
2. **Support SLA matrix (NF19).** Collateral does not state a tiered response matrix. We commit to a Sev-1 ≤1-hour 24×7×365 response matrix, backed by WAISL's follow-the-sun UK/India/UAE/Kuwait/Australia/Singapore footprint, and price it in Schedule E.
3. **Data sovereignty and hosting address (ISRA-19, ISRA-25).** Our reusable architecture artefact was written for a European customer and framed around GDPR/EU residency. For BAC we commit to Australian hosting — AWS Sydney (`ap-southeast-2`) or BAC private cloud — and we rewrite every residency, privacy, and ownership narrative to the Australian Privacy Act 1988 / APPs and ASD Essential 8 framing.

## Why WAISL

WAISL is an airport-operations software house with a multi-region presence including Australia, ISO 9001/20000/27001/22301 certifications, and a productised Turnwise/UTAM platform already in airport use. We offer BAC a parameterised, configurable, extensible platform rather than a bespoke build, and we commit to the controlled, phased, auditable delivery lifecycle Tab.F PMR demands.

> The technical solution that delivers these benefits is described in Section 03; the scope coverage and deliverables in Section 04.

---

# 02: Understanding of Requirements

## What BAC is asking for

BAC's objective, stated in RFP §3.2, is to procure a solution that can "automatically detect, classify, timestamp, sequence, and analyse underwing activities associated with aircraft arrivals and departures, including aircraft movements, ground support equipment (GSE), personnel activity, and key turnaround processes." The solution must "reduce reliance on manual data entry and provide objective, auditable, and defensible operational data aligned with BAC's airport systems."

The scope of work (RFP §3.3) enumerates eleven high-level outcomes: secure camera/video ingestion; aircraft identification and positioning via operational flight data fused with visual detection; apron safety via automated personnel detection and zone monitoring; automatic detection, sequencing, and visualisation of all key turnaround activities without manual timestamping; real-time and post-event analysis vs plan; transparent and continuously improving AI; configurable proactive alerts; intuitive operational and analytical visibility; seamless integration across BAC operational, enterprise, and data systems; mission-critical security/resilience/compliance; and a controlled, transparent, auditable project lifecycle with full BAC self-sufficiency.

## How requirements are organised

BAC has structured the response in the Excel Response Sheet around six schedules: Supplier Information, Social Procurement, Relevant Experience, Methodology, Pricing, and Tab.F Requirements. Tab.F decomposes the requirement set into:

- **Functional Requirements (FR01–FR73)** — 73 rows, 69 Must-Have, covering camera onboarding, aircraft detection, GSE classification, personnel/zone monitoring, turnaround activity detection, sequencing, AI governance, alerts, dashboards, reporting, integration, and administration.
- **Non-Functional Requirements (NF01–NF48)** — 48 rows covering availability/DR, support, training, accessibility, IAM, browser compatibility, and logging.
- **Project Management Requirements (PMR-01..PMR-10, with sub-rows 02a–02f and 06a–06d)** — 20 rows covering phased delivery, weekly meetings, WHS, change control, documentation, training, practical completion with 20% withhold, and six-month defects liability.
- **ISRA (rows 1–29)** — Information Security Risk Assessment rows covering ISO 27001, PII handling, retention, privileged access, breach notification, change management, incident response, cryptographic controls, resilience, data sovereignty, escrow, privacy, physical/environmental security, compliance management, incident testing, vetting, application whitelisting, MFA, and log management.

## Our reading of the priorities

The RFP's emphasis is unambiguous. The words "automated", "without manual timestamping", and "objective, auditable, defensible" recur (§3.2, §3.3). Camera-plus-AI detection of the specific underwing activities in FR17 and FR24 is the core differentiator — a re-skinned flight-tracking or CDM dashboard will not satisfy it. The detailed Tab.F (170 rows) and the statement that incomplete or non-compliant proposals "may be excluded" (§6.1) make this a compliance-heavy procurement.

The user communities are Terminal Operations and Airside Operations (RFP §3.4 "Who is it for?"). Expected benefits cluster around improved apron safety via automated personnel detection, enhanced operational efficiency via automated turnaround tracking and earlier delay detection, and improved on-time performance via proactive intervention.

## Constraints and commercial signals

- **Submission is tightly bounded** — the Excel response sheet plus an optional single PDF of no more than 5 pages; "no sales brochures" (§8). This forces concise, evidence-led responses.
- **Insurance bars are specific and high** — $20M PL, $10M PI, $10M Cyber (§4.4). Cyber insurance signals security sensitivity.
- **20% lump-sum withhold until practical completion** (PMR-09) — BAC protects itself on delivery.
- **Term** — 3 years initial, with two by-one-year extensions tied to SLA, sustainability and performance targets (§4.3).
- **Oral presentations** — shortlisted suppliers present to the Evaluation Team and SMEs (§4.8). Methodology and team credibility will be tested live.
- **Evaluation criteria** — Relevant experience, Methodology, Pricing, Requirements (mandatory, §4.6). No explicit weights given.

## Site and regulatory context

BNE operates under a 50-year lease (from 1997, with a 49-year option) and contributes more than $4bn/yr to Queensland's economy. Work is performed on the land of the Turrbal People, and BAC's Reconciliation Action Plan, Modern Slavery Act obligations, and Supply Nation social procurement expectations apply (Schedule B). Aviation security legislation (Aviation Transport Security Act 2004, CASA Manual of Standards Part 139, Airports Act 1996) applies to all on-airport work, and Aviation Security Identification Cards (ASICs) are required for personnel.

## Where our understanding diverges from collateral reality

We have mapped each of the 170 Tab.F rows to a coverage classification (Grounded / Assertable / Gap) in `coverage-matrix.md`. We do not pretend that our existing collateral satisfies every Must-Have row. In particular, five disqualifying gaps must be resolved before this proposal can be considered compliant: FR17 (camera-based GSE type classification), FR20 (personnel presence in apron zones), NF19 (tiered support SLA), ISRA-19 (data sovereignty), and ISRA-25 (hosting geographical address). Each is addressed explicitly in Sections 03, 08, 10, and 13.

> Our technical response to these requirements is set out in Section 03.

---

# 03: Technical Solution

## The problem this section answers

BAC needs camera-and-AI-driven automatic detection, classification, timestamping, sequencing, and analysis of underwing activities, fused with operational flight data, with real-time and historical visibility, configurable alerts, and enterprise-grade security. This section describes the Turnwise/UTAM technical architecture, grounds what is evidenced, and is explicit about the disqualifying gaps in camera-AI detection (FR17, FR20) and how we will close them.

## Architecture overview

WAISL proposes the UTAM (Unified Total Airside Management) platform, productised as Turnwise, deployed for BAC. UTAM is an AI-enabled airport operations platform built on a layered architecture.

- **Edge Layer**: Edge Data Ingestor integrates airport operational, IoT, and OT systems (AODB, CCTV cameras, BAS, IoT sensors, TETRA radio, third-party vendor systems) with protocol adaptation (REST, SOAP, file-based, streaming, OPC-UA), schema normalisation, buffering and retry for intermittent connectivity, and encrypted transmission. Edge Vision Controller processes video streams from CCTV and edge cameras using computer vision models to extract structured metadata (queue length, dwell time, wait times, processing times, security incidents) and publishes events to the platform via streaming interfaces.
- **Platform Ingestion & Messaging**: HTTPS Gateway (TLS, mutual auth), Platform Data Ingestion (batch/micro-batch/streaming, schema evolution, quality checks), Message Queue (event backbone, topic streaming, replay, horizontal scaling), Message Service.
- **Core Data & Processing**: Lakehouse (medallion: Bronze/Silver/Gold), Operational Database (low-latency current state), Data Catalogue & Governance (lineage, schema registry, quality enforcement), Workflow Engine (event-driven, retry, escalation, audit), Rules Engine (threshold/pattern/correlation anomaly detection, aggregation, prioritisation), Reporting Service.
- **External Interfacing**: API Gateway (REST/SOAP routing, auth, rate limiting), Application Load Balancer, Route 53, SSO/OIDC via Azure Entra ID.
- **UI Layer**: operational dashboards, alerts view, user management & configuration, reports.
- **Security & Monitoring**: AWS KMS, Secrets Manager, WAF, GuardDuty, CloudTrail, CloudWatch, Inspector.

The platform is "deployment agnostic": it can run in AWS cloud or in BAC's private cloud, with all functional, security, and performance commitments remaining identical.

## What the architecture already does, grounded against Tab.F

The Turnwise product document evidences the operational backbone BAC requires:

- **Flight tracking & flight information**, flight miles view (70/40/10-mile countdown), flight summary and POBT.
- **Stand tracking** with real-time occupancy, next-allocated flights, actual/planned stand utilisation, gate utilisation reports.
- **GSE, vehicle tracking and utilisation**: movement monitoring, path traversal (last 15 min), vehicle cards, GSE usage master, vehicle last location, GSE master, speed violation reports.
- **Taxi time monitoring (VTT)**, runway occupancy time (ROT), turnaround time monitoring with a graphical Gantt of ground-handling activities against CDM milestones and a live "NOW" marker.
- **CDM milestone tracking** across inbound/turnaround/outbound (EOBT-3 through ATOT).
- **Critical activity tracking** showing completed/pending/needs-attention.
- **Airside safety and restricted-zone monitoring** with speed violation and restricted-zone entry alerts.
- **Operational reports**: TMO, VTT, ROT, stand utilisation, turnaround SLA, flight SLA, flight performance, GSE usage, speed violations, restricted-zone entry leaders, airline-wise OTP.
- **Playback**: replay past movement/activity (Pause/Rewind, 1x/2x/4x) for delay analysis, incident review, training.
- **Weather and RVR visibility** alongside operations.
- **Dashboard, KPI and slot performance** (flights arrived/departed/cancelled, OTP %, avg delay, taxi times, stand occupancy).
- **Airport geofence**: configured geofence areas (name, address, group, category, coordinates polygon).
- **Monitoring dashboard**: data-sync health across AODB, ADS-B, Video Events, Vehicle Data.
- **User, airline, GHA management**; **alerts** (speed violation, turnaround SLA); **hybrid deployment**; **system integrations**.

This grounds FR04, FR16, FR19, FR25, FR33–FR37, FR40–FR41, FR45–FR47, FR49, FR53, FR59, FR60, FR61–FR66 and the operational-reporting/dashboard portions of the RFP.

## Camera onboarding, aircraft detection, and the activity-detection backbone

UTAM's Edge Vision Controller performs inference at the edge on CCTV/edge camera streams and publishes structured events for real-time alerts, DCB, and situational-awareness dashboards. The Edge Data Ingestor onboards new cameras and systems via low-code vendor-agnostic onboarding.

For FR01–FR03 (onboarding fixed cameras, grouping by airport/terminal/gate/stand/airline/handler, configuring FOV and parking zones), the Edge layer provides the mechanism.

For FR13/FR14 (aircraft arrival/departure detection and on-block/off-block confirmation), Turnwise stand/flight tracking detects arrival and correlates with AODB; camera-based on-block confirmation is the asserted extension.

For FR15 (AIDX identification of aircraft type/reg/flight/airline), Turnwise displays these fields via AODB/ADS-B; a named AIDX connector is an asserted addition via the API Gateway.

## Disqualifying gap 1, FR17: camera-based GSE type classification

**Requirement (FR17, Must-Have):** detect and classify GSE types via camera (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, tractors, golf carts).

**Evidence position:** Turnwise tracks GSE via telematics/GPS and exposes a "vehicle type" field, but our collateral does not evidence camera-based classification of the full enumerated list.

**How we address it:** We will not claim capability we have not evidenced. Our approach is to combine telematics-sourced GSE identity (already grounded) with a computer-vision classification model trained on the FR17 enumerated classes, delivered as a committed Phase-1 workstream with acceptance criteria tied to per-class precision/recall thresholds agreed with BAC.

We acknowledge that, absent a demonstrated prior deployment of this specific classifier, this remains a gap that we propose to close through delivery commitment rather than claim of existing capability. The risk to BAC is mitigated by: (a) phased acceptance, where the classifier must pass per-class accuracy criteria in the Test phase before the corresponding Tab.F row is marked conformant; (b) the 20% practical-completion withhold (PMR-09) protecting BAC financially; (c) a named CV delivery partner in the detailed design.

## Disqualifying gap 2, FR20: personnel presence in apron zones (excluding passengers)

**Requirement (FR20, Must-Have):** detect personnel presence in apron zones, excluding passengers.

**Evidence position:** no personnel-detection capability is evidenced in either Turnwise or UTAM. UTAM's Edge Vision Controller extracts "queue length, dwell time, wait times, processing times, security incidents", not personnel presence in defined apron zones.

**How we address it:** We will deliver a personnel-detection CV model on the Edge Vision Controller, scoped to apron zones (excluding passenger terminal zones), with the same acceptance-criteria discipline as FR17. This is also a prerequisite for FR21 (personnel entering restricted zones) and FR23 (PPE detection where camera quality allows), both of which are currently gaps.

We are explicit: these three rows (FR17, FR20, FR23) are the areas where our existing collateral is weakest relative to the RFP's core camera-AI ask. We propose to close them through delivery, not through assertion in this proposal.

## Turnaround activity detection (FR24) and AI governance (FR26–FR28, FR68–FR71)

**FR24 (Must-Have):** auto-detect start/end of chocking, aerobridge dock/undock, stair position/removal, GPU connect/disconnect, baggage load/unload, catering, refuelling on bay, pushback readiness, cabin cleaning.

Turnwise's turnaround Gantt shows activities with start/end times and a completion check, sequenced into a single turnaround timeline (FR25, grounded). Whether each listed activity's start/end is camera-AI derived or telematics/CDM derived is to be confirmed in detailed design.

**FR26 (confidence scores per event):** not evidenced.
**FR27 (manual validation/correction of detected timestamps):** not shown in collateral.
**FR28 (learn from corrections):** UTAM's AI/ML platform implies a learning loop but no specific continuous-learning feature is shown.
**FR68 (versioned AI models), FR69 (per-model accuracy tracking), FR70 (airport-specific tuning), FR71 (continual improvement):** versioned release train is asserted; per-model accuracy tracking is a gap.

We commit to a per-event confidence score, a manual validation/correction UI, a learning loop feeding model retraining, and per-model accuracy tracking, all delivered as Phase-1 capabilities with acceptance criteria, rather than claimed as existing.

## Alerts, dashboards, and analytics (FR40–FR53)

Configurable alerts when activities exceed planned duration (FR40), unsafe/prohibited activity alerts (FR41), and camera/AI-confidence-degradation alerts (FR42) are grounded in Turnwise's Turnaround SLA alert, Speed Violation alert, and UTAM Rules Engine respectively.

Alert channels (FR43): UTAM supports SMS, voice, email, Microsoft Teams, TETRA radio, mobile/web notifications; an AIDX-specific API alert channel is an asserted addition via the API Gateway.

Live turnaround status board per gate (FR45), current activity state and next expected milestone (FR46), colour-coded delay indicators (FR47), live/historical video playback per event (FR48), turnaround KPIs by airline/aircraft type/gate/service provider (FR49), trend/variance analysis (FR50), AI-driven improvement insights (FR51), ad-hoc queries/filters (FR52), and historical analysis (FR53) are grounded or assertable from Turnwise and UTAM Self-Service BI.

Live & historical video playback per event (FR48): Turnwise Playback replays movement on the map; raw video playback per event is to be confirmed.

## Integration and data architecture (FR54–FR59, NF15–NF16)

UTAM's integration layer provides an API Gateway (REST/SOAP), event streaming, and a connector framework. Listed connectors include AODB, ADS-B, telematics, vision analytics, weather, RVR.

AODB integration is grounded (FR33, FR16). FIDS and an explicit AIDX connector are asserted additions.

Configurable data retention (FR58) is grounded in UTAM retention policies; event metadata stored separate from video (FR57) is asserted from the lakehouse separation; publishing actual timestamps to consuming systems (FR56) is asserted via the API Gateway. Forensic replay for incident investigation (FR59) is grounded in Turnwise Playback.

## Administration, access control, and environments (FR60–FR67)

RBAC (FR60), airline/service-provider data segregation (FR61), configurable permissions per role (FR62), admin tools for configuration management (FR63), environment separation Dev/Test/Prod (FR64), operational monitoring/health dashboards (FR65), admin configuration of alerts/reports/dashboard/users (FR66), and SSO for BAC users via Azure AD with local accounts and password policies/MFA for non-BAC users (FR67) are all grounded in UTAM's RBAC/ABAC, row-level access, IaC environment parity, and Azure Entra ID / OpenLDAP / OneLogin SSO.

## Future-phase items (FR72, FR73)

FR72 (Phase-2 airline data integration; aerobridge camera pax counting/crew boarding) is a future-phase gap.
FR73 (remote access via mobile and tablet) is asserted from UTAM's browser-based responsive UI.

## Extensibility

The platform's configuration-over-code principle (every operationally variable element is parameterised, version-controlled, and manageable by authorised business users) provides the extensibility RFP §3.3 requires. The Lakehouse medallion architecture supports schema evolution, time travel, and high-performance query, enabling future operational and analytical use cases.

> How this technical solution maps to scope coverage and deliverables is set out in Section 04.

---

# 04: Scope Coverage and Deliverables

## What this section answers

BAC requires a single-source-of-truth underwing analytics solution covering the full scope in RFP §3.3 and Tab.F. This section maps the scope to deliverables, states what is in scope, and is explicit about the rows we cannot fully ground.

## Scope coverage by Tab.F domain

### Camera and video ingestion (FR01–FR12)

- FR01 onboard fixed cameras (BAC-supported models), FR02 grouping by airport/terminal/gate/stand/airline/handler, FR03 FOV & parking-zone configuration — Edge Data Ingestor low-code onboarding and Turnwise grouping dimensions.
- FR04 geofenced zones (safety envelope, equipment staging, personnel walk zones) — Turnwise Airport Geofence.
- FR05 live video ingest — Edge Vision Controller / HTTPS Gateway.
- FR06 buffering during network interruptions — Edge Data Ingestor buffering and retry.
- FR07 configurable frame rates/resolutions per camera.
- FR08 timestamp via synchronised airport time source.
- FR09 continuous camera availability/signal monitoring; notify vendor on failure.
- FR10 detect occlusion/lens obstruction/glare.
- FR11 alerts for AI-accuracy degradation.
- FR12 camera health dashboard.

**Deliverable:** Edge Vision Controller configuration pack (FR01–FR05, FR08), camera health and AI-degradation alerting rules (FR09, FR11, FR12), and a committed delivery workstream for FR07 (per-camera frame-rate/resolution configuration) and FR10 (occlusion/glare detection) with acceptance criteria.

### Aircraft detection (FR13–FR16)

- FR13/FR14 arrival/departure detection and on-block/off-block confirmation.
- FR15 AIDX identification of aircraft type/reg/flight/airline.
- FR16 correlation with AODB flight info.

### GSE, personnel, and zones (FR17–FR23)

- FR17 camera-based GSE type classification (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, tractors, golf carts).
- FR18 GSE ready/arrival/departure timestamps per type.
- FR19 equipment presence on stand.
- FR20 personnel presence in apron zones (excluding passengers).
- FR21 personnel entering restricted zones.
- FR22 unsafe dwell times in high-risk areas.
- FR23 PPE detection where camera quality allows.

### Turnaround activities and sequencing (FR24–FR32)

- FR24 auto-detect start/end of chocking, aerobridge dock/undock, stair position/removal, GPU connect/disconnect, baggage load/unload, catering, refuelling on bay, pushback readiness, cabin cleaning.
- FR25 sequence activities into a single turnaround timeline.
- FR26 per-event confidence scores.
- FR27 manual validation/correction.
- FR28 learn from corrections.
- FR29 airline-specific, movement-type turnaround workflows (Originator/Turnaround/Terminator I/D).
- FR30 aircraft-type-specific turnaround sequences.
- FR31 mandatory vs optional activities.
- FR32 dependencies & precedence rules.

### Planned vs actual, alerts, dashboards, reporting, integration, administration (FR33–FR73)

These rows are covered in Section 03. Grounded subset: FR33, FR34, FR35, FR36, FR37, FR40, FR41, FR45, FR46, FR47, FR49, FR52, FR53, FR55, FR58, FR59, FR60, FR61, FR62, FR63, FR64, FR65, FR66, FR67. Assertable subset: FR38, FR42, FR43, FR44, FR48, FR50, FR51, FR54, FR56, FR57, FR68, FR70, FR71, FR73. Gaps: FR39, FR69, FR72.

## Deliverables

The following deliverables map to PMR-06 (project documentation) and PMR-06a/06b/06c/06d:

| # | Deliverable | RFP ref | Evidence |
| --- | ------------- | -------- | ---------- |
| D1 | Project Management Plan (PM plan, stakeholders, risk analysis, schedule) | PMR-02a, PMR-06 | Committed (architecturally supported) |
| D2 | Detailed Design Document with full FR traceability | PMR-02b, PMR-06a | Committed (architecturally supported) |
| D3 | Built/configured platform across DEV/TST/PROD per design | PMR-02c | Evidenced in collateral |
| D4 | Comprehensive Test Plan with requirement traceability | PMR-02d, PMR-06b | Committed (architecturally supported) |
| D5 | Implementation/Migration Plan with roles, validation, rollback | PMR-02e, PMR-06c | Evidenced in collateral |
| D6 | As-built documentation reflecting final solution | PMR-02f, PMR-06d | Committed (architecturally supported) |
| D7 | End-user training in Test environment with cheat sheets | PMR-07 | Committed (architecturally supported) |
| D8 | Technical training for BAC personnel (architecture, fault-finding, config) | PMR-08 | Committed (architecturally supported) |
| D9 | Practical completion package (cutover + tests + docs + training) | PMR-09 | Committed (architecturally supported) |
| D10 | 6-month defects liability + maintenance agreement | PMR-10 | Committed for delivery |
| D11 | AIDX connector via API Gateway | FR15, FR43, FR54 | Committed (architecturally supported) |
| D12 | FR17 GSE-type CV classifier with per-class acceptance criteria | FR17 | Committed for delivery |
| D13 | FR20 personnel-presence CV model with acceptance criteria | FR20, FR21, FR23 | Committed for delivery |
| D14 | FR26/27/28/69 AI-governance pack (confidence scores, validation UI, learning loop, per-model accuracy) | FR26, FR27, FR28, FR69 | Committed for delivery |
| D15 | Support SLA matrix (Sev-1 ≤1h 24×7×365) priced in Schedule E | NF19, NF20, NF17 | Committed for delivery |
| D16 | Australian hosting commitment (AWS Sydney ap-southeast-2 or BAC private cloud) with address | ISRA-19, ISRA-25 | Committed for delivery |
| D17 | BAC ISRA completed | NF01, ISRA 1–29 | Committed (architecturally supported) |
| D18 | Customised quick-reference guides (state if extra cost) | NF26 | Committed for delivery |
| D19 | Help & knowledge artefacts, field-level help | NF18, NF23 | Committed for delivery |
| D20 | 3-year availability history | NF05 | Committed for delivery |

## Out of scope

- Fabricated team bios, referees, case studies, pricing values, and certifications are not in scope of this draft. All such content is marked as placeholder and must be supplied before submission.
- Phase-2 items FR72 (aerobridge pax counting; airline data integration) are committed as a roadmap deliverable rather than a Phase-1 deliverable.

> The methodology by which these deliverables are produced is described in Section 05.

---

# 05: Implementation Methodology

## What BAC requires

RFP §3.3 requires delivery "through a controlled, transparent, and auditable project lifecycle." Tab.F PMR-02 mandates defined phases: Initiation, Design, Build, Test, Implementation, Closure. PMR-06 requires project documentation (PM plan, schedule, status reports, design, test plans, as-built). PMR-09 ties practical completion to cutover + tests + docs + training, with 20% withheld. PMR-10 requires a six-month defects-liability plus maintenance agreement.

## Methodology: phased delivery

WAISL proposes a phased delivery aligned to PMR-02 sub-rows, governed by weekly project meetings (PMR-03) and BAC change control (PMR-05).

### Phase 1: Initiation (PMR-02a)

Produce a Project Management Plan covering stakeholders, risk analysis, and schedule; confirm integration scope and ownership with BAC pre-kickoff (NF08); agree the ISRA approach (NF01) and the Australian hosting target (ISRA-19, ISRA-25).

### Phase 2: Design (PMR-02b, PMR-06a)

Workshops with Terminal Operations, Airside Operations, and BAC IT&T to produce a Detailed Design Document documenting the full solution with FR traceability. This is where the FR17 GSE-type CV classifier, the FR20 personnel-presence model, and the FR26/27/28/69 AI-governance pack are specified with acceptance criteria. The Hardening Checklist and DPIA inputs (where applicable) are delivered here.

### Phase 3: Build (PMR-02c)

Configure the platform per design across DEV/TST/PROD using Infrastructure as Code, with environment parity. Build the Edge Vision Controller CV models for FR17/FR20, the AIDX connector (FR15/FR43/FR54), and the AI-governance pack.

### Phase 4: Test (PMR-02d, PMR-06b)

Install in the Test environment, execute a Comprehensive Test Plan with requirement traceability, and support UAT. Automated testing pyramid (unit, contract/integration, end-to-end, performance) is asserted. The FR17 and FR20 CV models must pass per-class and per-scenario acceptance criteria in this phase before the corresponding Tab.F rows are marked conformant.

### Phase 5: Implementation (PMR-02e, PMR-06c)

Production cutover in an agreed BAC change window, with rollback (blue/green, DB migration revert) and a post-cutover debrief. All changes feed BAC's Change Approval Board (PMR-05, ISRA-11).

### Phase 6: Closure (PMR-02f, PMR-06d, PMR-09)

Defect inspection and rectification, as-built documentation reflecting the final solution, end-user and technical training (PMR-07, PMR-08), and practical completion with the 20% withhold released on BAC acceptance.

### Phase 7: Defects liability (PMR-10)

Six-month defects liability plus maintenance agreement aligned to the support tiers in Section 10.

## Change control and risk management

All production changes follow a documented change-management process with impact assessment, BAC CAB approval, and scheduled implementation in agreed maintenance windows (PMR-05, ISRA-11). The platform continuously monitors for configuration drift.

Risk mitigation strategy (NF11) is asserted from the UTAM risk framework. WAISL's multi-region footprint (UK | India | UAE | Kuwait | Australia | Singapore) enables additional resources to be drawn on to keep timelines (NF12).

## WHS and contractor status (PMR-04)

WAISL operates an Australia office and will comply with BAC's Work Health and Safety requirements, Safe Work Method Statements, and the BAC contractor management system registration (including the annual fee). Personnel requiring airside access will obtain Aviation Security Identification Cards (ASICs).

## Non-disruptive upgrades and release train

The platform ships on the current GA/LTS release and follows a predictable release train — monthly maintenance, quarterly feature releases, annual LTS — with blue/green and canary deployments, pre-flight checks, automated DB migrations with rollback, and verified backup/restore tests. API backward compatibility is maintained via semantic versioning.

> The project management and governance overlay is described in Section 06.

---

# 06: Project Management and Governance

## Governance structure

WAISL will establish a project governance structure aligned to PMR-01..PMR-10:

- **Project Sponsor (WAISL)** — accountable for delivery, commercial, and security commitments.
- **Project Manager (WAISL)** — single point of contact for BAC's Contact Officer (Leighton Walker, Technology Project Manager), running weekly project meetings (PMR-03).
- **BAC Steering Group** — Terminal Operations, Airside Operations, BAC IT&T, and BAC Information Security, meeting at phase gates.
- **Change Advisory Board (BAC)** — receives all production change requests per PMR-05/ISRA-11.
- **WAISL Australia local representative** — account escalation point for BAC (NF22).

## RACI summary

| Activity | WAISL PM | WAISL Sponsor | BAC Contact Officer | BAC IT&T | BAC InfoSec | BAC CAB |
| ---------- | ---------- | --------------- | --------------------- | ---------- | ------------- | --------- |
| PM plan & schedule | A/R | C | C | I | I | I |
| Detailed design | A/R | C | C | C | C | I |
| Build & configure | A/R | I | I | C | I | I |
| Test & UAT | A/R | I | C | C | C | I |
| Production cutover | A/R | C | C | C | C | A |
| Training | A/R | I | C | C | I | I |
| Practical completion | A/R | C | A | C | C | I |
| Defects liability | A/R | I | C | C | C | I |
| Change requests | A/R | I | C | C | C | A |
| ISRA completion | A/R | C | C | C | A | I |



## Status reporting

Weekly status reports against the PM plan, schedule, risk register, and issue log (PMR-06). Daily availability and transaction-performance data is available via API or automated email (UTAM operational commitment).

## Risk and issue management

A live risk register maintained from Initiation, with likelihood/impact/mitigation/owner per NF11. Risks are reviewed at each phase gate and at weekly meetings. The five disqualifying gaps (FR17, FR20, NF19, ISRA-19, ISRA-25) are entered as top delivery risks with explicit mitigations (see Sections 03, 08, 10, 13).

## Personnel and contractor management

WAISL commits to certified personnel and established equipment-supplier relationships (PMR-01). All airside personnel will hold ASICs and be registered on the BAC contractor management system (annual fee).

## Documentation deliverables

The documentation set is governed by PMR-06 and its sub-rows (PMR-06a detailed design, PMR-06b test plan, PMR-06c implementation/migration plan, PMR-06d as-built), each version-controlled and accepted at phase gates before progression.

## Practical completion and 20% withhold

Practical completion (PMR-09) requires cutover, successful tests, documentation, and training. Twenty per cent of the lump sum is withheld until BAC accepts practical completion. WAISL accepts this contractual term. This withhold protects BAC on the delivery of the committed-but-not-yet-evidenced CV models (FR17, FR20) and the AI-governance pack (FR26/27/28/69).

## Defects liability

Six-month defects liability plus a maintenance agreement aligned to the support tiers (PMR-10), priced in Schedule E.

> Integration, data, and technical approach details are in Section 07.

---

# 07: Integration, Data, and Technical Approach

## Integration philosophy

BAC requires "seamless integration across BAC operational, enterprise and data systems" (RFP §3.3). UTAM's integration layer is built on an API Gateway (REST/SOAP), event streaming, and a connector framework, with the Edge Data Ingestor performing protocol adaptation (REST, SOAP, file-based, streaming, OPC-UA) and schema normalisation.

## Connectors

UTAM lists connectors for AODB, ADS-B, telematics, vision analytics, weather, and RVR (NF16).

For BAC we will add:

- **AIDX connector** (FR15, FR43, FR54) — published and consumed via the API Gateway.
- **FIDS connector** (FR54) — via the same connector framework.
- **A-CDM milestone synchronisation** — UTAM's NM Message Service handles A-CDM milestones (TOBT, TSAT, A-CDM milestones) and is adaptable to BNE's A-CDM context.

## Data architecture

The Lakehouse uses a medallion architecture (Bronze raw, Silver curated, Gold business-ready) with schema evolution, time travel, and high-performance query. An Operational Database holds current state for real-time dashboards. A Data Catalogue & Governance layer provides metadata, lineage, schema registry, and quality enforcement.

Data quality is first-class: every ingested record carries a quality score; low-quality records are flagged, quarantined, and logged; every derived KPI carries full provenance; all access/modification/deletion events are logged to an immutable audit trail.

## Data flow and event metadata separation

Event metadata is stored as structured data in the Lakehouse, separate from video — satisfying FR57 in principle. Configurable retention policies (FR58) are grounded. Automated retention enforcement with configurable periods per data category is available.

## APIs and event publishing

The API Gateway is the central control point for all external APIs — routing, authentication, rate limiting, security — enabling secure exposure of platform services. Actual timestamps can be published to consuming systems via the API Gateway and event streaming (FR56).

## Master data management

Shared entity definitions (flights, stands, gates, resources) are managed centrally and resolved across all source systems — eliminating the entity-conflict problem that plagues multi-system airport analytics. This directly supports BAC's "single source of truth" objective.

## Self-service BI and reporting

Self-Service BI enables authorised stakeholders to build custom reports, dashboards, and data explorations without IT dependency, querying curated Gold-layer datasets through controlled templates (no raw SQL for business roles), with timeouts, rate limits, and full audit logging. Export controls are governed by role-based permissions with audit logging (NF02).

## Parameterisation and rules

The Business Rules Engine provides a low-code environment for configurable alerts, automated workflows, and event-driven actions — version-controlled with approval workflow and rollback. This grounds FR40 (turnaround SLA alerts) and FR41 (unsafe/prohibited activity alerts) and supports FR42 (AI-confidence-degradation alerts via rules).

## Deployment models

The platform is deployment-agnostic: AWS cloud (multi-AZ) or BAC private cloud, with identical functional, security, and performance commitments. For BAC we commit to Australian hosting (see Section 08).

## DevOps and CI/CD

Fully automated commit-to-production pipeline with policy gates for security, performance, and compliance; Infrastructure as Code (Terraform + GitOps) with drift detection; environment parity (DEV/TST/PROD from the same IaC templates); automated testing pyramid.

> Security, ISRA, and compliance are covered in Section 08.

---

# 08: Security, ISRA, and Compliance

## The problem this section must solve

Tab.F ISRA rows 1–29 and NF01 require a completed BAC Information Security Risk Assessment, grounded in Australian regulatory framing. Our reusable UTAM architecture artefact was written for a European customer and frames compliance around GDPR/NIS2/Hellenic DPA with EU residency. **We do not propagate that framing.** We rewrite every residency, privacy, and ownership narrative for Brisbane/Australia. This section directly addresses the two disqualifying sovereignty gaps (ISRA-19, ISRA-25).

## Disqualifying gap 3, ISRA-19: Data sovereignty management

**Requirement (ISRA-19, Must-Have):** data sovereignty management, with data hosted in Australia under Australian law.

**Evidence position:** UTAM asserts "All data is hosted exclusively within European Union (EU) data centres" and "AWS EU region deployment is used to satisfy data residency requirements under GDPR and NIS2." This conflicts with BAC's Australian context.

**Resolution:** WAISL commits to Australian hosting for all BAC data, in AWS Sydney region (`ap-southeast-2`) or BAC private cloud at BAC's election. The platform's stated deployment agnosticism and private-cloud option make this reconcilable without architectural change. All residency, compliance, privacy, and data-ownership narrative is rewritten to the Australian regulatory frame: **Australian Privacy Act 1988 / Australian Privacy Principles (APPs)**, **ASD Essential 8 / IRAP alignment**, and **BAC as the exclusive data owner**. Every AIA/Athens/Hellenic-DPA/GDPR reference in the source artefact is excluded from BAC proposal text.

With this commitment, ISRA-19 moves from Disqualifying Gap to Addressable, subject to BAC confirming the preferred hosting target (AWS Sydney vs BAC private cloud). That open question will be closed at Initiation.

## Disqualifying gap 4, ISRA-25: Hosting geographical address

**Requirement (ISRA-25, Must-Have):** hosting location, as a geographical address.

**Evidence position:** UTAM cites EU/Athens addresses.

**Resolution:** WAISL commits to an Australian data-centre address. Proposed default: **AWS Sydney region (`ap-southeast-2`)**, with the specific AWS data-centre address supplied in the completed ISRA tab once BAC confirms the hosting target. If BAC elects private cloud, the address will be the BAC data-centre address.

## Security architecture, grounded

UTAM operates under a zero-trust security model: verify explicitly, enforce least privilege, assume breach, applied across every layer, not just the perimeter.

- **Identity-centric**: every request (users, services, automated processes) authenticated and authorised independently.
- **mTLS for service-to-service**: no plaintext internal communication.
- **Short-lived credentials**: access tokens rotated automatically; no long-lived static credentials.
- **PAM for privileged access**: break-glass access requires PAM approval, is time-limited, and is fully audit-logged (ISRA-05).
- **Micro-segmentation**: lateral movement restricted by policy.

## ISRA row-by-row mapping (summary)

- **ISRA-01 ISO/IEC 27001** — UTAM states ISO 27001 certified; WAISL cover page lists 9001/20000/27001/22301.
- **ISRA-02 sensitive info collected** — apron video analytics may capture images of personnel; PII handling to be confirmed with BAC in the ISRA.
- **ISRA-03 auto-delete when no business requirement** — UTAM retention policies with automated enforcement.
- **ISRA-04 asset disposal sanitisation** — UTAM secure erasure + Certificate of Destruction.
- **ISRA-05 privileged access management** — UTAM PAM + break-glass.
- **ISRA-06 infosec roles in contract** — standard contractual clauses to be included.
- **ISRA-07 mature information security policy** — UTAM ISO 27001 ISMS.
- **ISRA-08 annual security awareness training** — UTAM staff awareness training.
- **ISRA-09 breach notification process** — UTAM incident handling, 1-hour notification.
- **ISRA-10 security updates & patching** — UTAM release train/patch cadence.
- **ISRA-11 change management feeding BAC CAB** — UTAM change management.
- **ISRA-12 incident response management** — UTAM incident response (classification, escalation, containment, eradication, recovery, post-incident review), aligned to ISO 27001.
- **ISRA-13 cryptographic controls** — UTAM AES256 at rest, TLS 1.2 in transit, KMS-managed keys.
- **ISRA-14 system secure & resilient against cyber attack** — UTAM zero-trust, WAF, GuardDuty, Inspector, hardening (CIS/STIG).
- **ISRA-15 protection against malicious software** — UTAM Defender for Server / antimalware.
- **ISRA-16 meet BAC availability incl. RTO & RPO** — UTAM RTO ≤40 min, RPO near-zero.
- **ISRA-17 backup testing to ensure RTO/RPO** — UTAM scheduled restore tests.
- **ISRA-18 network management** — UTAM NGFW, WAF, mTLS, segmentation.
- **ISRA-19 data sovereignty** — see resolution above.
- **ISRA-20 service escrow** — UTAM source-code escrow agreement with a recognised third-party agent, updated with each major release.
- **ISRA-21 privacy & right to anonymity** — UTAM frames privacy via GDPR/pseudonymisation; for BAC we reframe to the Australian Privacy Act 1988 / APPs, with pseudonymisation/anonymisation for analytics workloads and data minimisation.
- **ISRA-22 physical & environmental security** — AWS data-centre physical controls (theft, fire, heat, power).
- **ISRA-23 compliance management & validation during contract** — UTAM continuous validation + annual review.
- **ISRA-24 formal incident plans, tested regularly** — UTAM incident response plan exists; regular testing not yet evidenced.
- **ISRA-25 hosting geographical address** — see resolution above.
- **ISRA-26 vetting of staff with privileged access** — standard vetting; not explicitly described in collateral.
- **ISRA-27 application whitelisting** — not evidenced.
- **ISRA-28 MFA across service provider's business** — UTAM MFA across privileged/admin.
- **ISRA-29 security event/log management; retention duration** — UTAM CloudTrail/CloudWatch + retention policies.

## IAM and access (FR60–FR67, NF32–NF46)

RBAC and ABAC are enforced at the API, dashboard, and data layers, where row-level and column-level access controls ensure even authenticated users see only authorised data. External parties (airlines, ground handlers) access only their own operational data through role-restricted views with full audit logging (FR61).

SSO via Azure Entra ID / Azure AD for BAC users (Windows integrated authentication, with no re-authentication after desktop login), with OpenLDAP and OneLogin SSO for third-party stakeholders (FR67, NF36, NF42). Mandatory MFA for all administrative and privileged access (NF35, ISRA-28). Just-in-time admin delegation with short-lived credentials (NF43). No browser plug-ins required (NF39).

Real-time system logs and technical diagnostics (NF45), user auth/app usage/audit reports (NF46), and centralised searchable logs for high-volume event search (NF48) are grounded in CloudTrail/CloudWatch. Geolocation on authentications (NF47) is not evidenced and is committed as a low-cost feature.

## Availability, DR, and resilience (NF04–NF07, ISRA-16/17)

| HA/DR Parameter | Specification |
| ---------------- | --------------- |
| Target Availability | ≥99.9% (24×7) |
| RTO | ≤40 minutes |
| RPO | near-zero |
| Deployment | Multi-AZ for all production workloads |
| Database HA | Multi-instance with automated failover and point-in-time recovery |
| Message Queue | Fully replicated across AZs |
| Auto-healing | Kubernetes self-healing with HPA |
| Backup | Automated DB backups + continuous replication + versioned object storage |



Daily backups with 30-day retention for operational data (and longer for archival per the agreed retention policy); full backups stored in a separate region for DR.

## Certifications and standards

WAISL holds ISO 9001, 20000, 27001, and 22301 certifications (cover page). The solution is delivered on an ISO 27001-certified cloud foundation, with a SOC-2 Type II roadmap. For BAC, we will additionally align to **ASD Essential 8** and **IRAP** framing on request, recognising that BAC's environment is Australian-regulated.

## Penetration testing

- Predelivery penetration test by an accredited third party before Provisional Acceptance, covering all application and infrastructure components.
- Retest until no exploitable critical/high/medium vulnerabilities remain; only then is the system accepted into production.
- Alignment with BAC's annual penetration testing plan; additional tests on 30 days' notice.
- BAC's right to perform penetration tests against the platform with prior notice is acknowledged.

## Escrow and exit

Source-code escrow agreement with a recognised third-party agent, updated with each major release (ISRA-20). Exit plan: return of all BAC data in machine-readable format (CSV/JSON/API) within 15 working days; secure erasure of all copies with Certificate of Data Destruction; handover of credentials, documentation, and (if applicable) escrowed source.

## Data ownership

All data generated, processed, or stored within the platform is the exclusive property of **Brisbane Airport Corporation**, not WAISL and not a European customer.

> Testing, acceptance, and handover are described in Section 09.

---

# 09: Testing, Acceptance, and Handover

## Testing methodology (NF13, NF14, PMR-02d, PMR-06b)

WAISL will deliver a Comprehensive Test Plan with requirement traceability to Tab.F (PMR-06b). The UTAM platform supports an automated testing pyramid — unit, contract/integration, end-to-end, performance testing — through CI/CD pipelines with policy gates for security, performance, and compliance.

We acknowledge that the specific QA standards/accreditations/methodologies (NF09) and QA tools/technology (NF10) are not evidenced in our collateral and will be supplied from WAISL's internal QA process documentation before submission.

## Test phases

- **Unit & contract testing** — automated in CI/CD per build.
- **Integration testing** — connectors (AODB, ADS-B, telematics, vision, weather, RVR, AIDX, FIDS) tested against BAC test endpoints.
- **System & performance testing** — end-to-end turnaround detection, alerts, dashboards, reporting under load; scalability for very large groups (NF31).
- **UAT** — BAC Terminal Operations and Airside Operations users exercise the platform in the Test environment against agreed acceptance criteria (PMR-02d).
- **Security testing** — predelivery penetration test by an accredited third party, with retest until closure (see Section 08).
- **CV model acceptance (FR17, FR20, FR23)** — per-class and per-scenario acceptance criteria for the GSE-type classifier and personnel-presence model, agreed in Detailed Design and executed before the corresponding Tab.F rows are marked conformant.

## Requirement traceability

The Test Plan maps every Tab.F row (FR01–FR73, NF01–NF48, PMR-01..PMR-10, ISRA 1–29) to a test case or to a committed-delivery acceptance criterion (for gap rows), providing the traceability PMR-06b requires.

## Acceptance criteria

Each deliverable in Section 04 has acceptance criteria:

- Detailed Design accepted by BAC before Build (PMR-02b).
- Build configured across DEV/TST/PROD per design (PMR-02c).
- Test plan executed, UAT signed off (PMR-02d).
- Production cutover in change window with rollback verified (PMR-02e, PMR-06c).
- As-built documentation reflects the final solution (PMR-06d).
- Training delivered (PMR-07, PMR-08).
- Practical completion signed by BAC; 20% withhold released (PMR-09).

## Handover

Handover includes:

- As-built documentation (PMR-06d).
- Operational runbooks (backup/restore, incident response, change management).
- Admin and end-user training materials plus customised quick-reference guides (NF26).
- Credentials, documentation, and (if applicable) escrow confirmation (ISRA-20).
- Daily availability and transaction-performance reporting (via API or automated email).

## Defects liability (PMR-10)

Six-month defects liability period from practical completion, with a maintenance agreement aligned to the support tiers in Section 10.

> Ongoing support, SLA, and maintenance are in Section 10.

---

# 10: Support, SLA, and Maintenance

## Disqualifying gap 5 NF19: Severity response scenarios

**Requirement (NF19, Must-Have):** severity-1 response within 1 hour 24×7×365; Sev-2 within 4 hrs business-day / 8 hrs non-business; Sev-3 within 8 hrs; resolution commitments.

**Evidence position:** neither Turnwise nor UTAM provides a support-tier response matrix or evidence of 24/7/365 capability.

**Resolution:** WAISL commits to the following support matrix meeting or exceeding NF19 thresholds.

## Committed support SLA matrix

| Severity | Definition | Response | Update cadence | Resolution target |
| ---------- | ------------ | ---------- | ---------------- | ------------------- |
| Sev-1 (Critical) | Production down; data loss; safety-impacting alert failure | ≤1 hour, 24×7×365 | Every 1 hour | Best-effort continuous until restored |
| Sev-2 (High) | Major feature unavailable; significant degradation | ≤4 hrs business-day; ≤8 hrs non-business | Every 4 hours | Within 1 business day |
| Sev-3 (Medium) | Functional issue with workaround | ≤8 business hrs | Daily | Within 3 business days (NF20: Sev-3 resolution within 8 business hrs committed) |
| Sev-4 (Low) | Cosmetic, minor, enhancement | ≤1 business day | As agreed | Next release or per agreement |



## 24/7/365 capability

WAISL's multi-region footprint — **UK | India | UAE | Kuwait | Australia | Singapore** — enables a follow-the-sun support model providing 24/7/365 phone, email, and online coverage (NF17).

A local WAISL Australia representative provides BAC account escalation (NF22).

## Incident management

A formal incident-handling procedure aligned to ISO 27001 covers classification, escalation, containment, eradication, recovery, and post-incident review (NF21, ISRA-12). BAC is notified within 1 hour of a confirmed security incident. Documented incident management with response SLAs per priority (NF21).

## Support channels and help (NF17, NF18, NF23, NF24, NF26)

- 24/7/365 phone, email, online help (NF17).
- Client-configurable help & knowledge artefacts (NF18).
- Help-desk field-level info (NF23).
- Clear support/help options in the UI (NF24).
- Customised quick-reference guides, with cost stated in Schedule E if additional (NF26).

## Training (NF27–NF30)

- Admin/user training (format and cost in Schedule E) (NF27).
- Ongoing training (inclusive/exclusive of managed services; cost) (NF28).
- Training & materials for new features/patches (NF29).
- Training & support to suppliers (airlines, GHAs) (NF30).

End-user training in the Test environment with cheat sheets (PMR-07); technical training for BAC personnel on architecture, fault-finding, and configuration (PMR-08).

## Availability reporting and history

Daily availability and transaction-performance data provided via API or automated email. A 3-year history of system availability, failures, and downtime (NF05) is not evidenced in collateral; we commit to SLA reporting going forward and will publish historical availability metrics from existing deployments if available.

## Maintenance and upgrades

Non-disruptive upgrades via blue/green, canary, and rolling deployments, coordinated during agreed maintenance windows, with pre-flight checks, automated DB migrations with rollback, and verified backup/restore tests (PMR-05, ISRA-11). Security and hotfix patches as needed, monthly maintenance, quarterly feature releases, annual LTS.

## Defects liability and ongoing maintenance (PMR-10)

Six-month defects liability plus a maintenance agreement aligned to the support tiers above.

> Compliance with Tab.F requirements is summarised in Section 11.

---

# 11: Compliance with Tab.F Requirements

## Compliance posture summary

Tab.F contains 170 requirement rows (73 FR + 48 NF + 20 PMR + 29 ISRA). Our coverage-matrix classifies them as:

- **Grounded (74, 44%)** — directly supported by Turnwise/UTAM collateral.
- **Assertable (65, 38%)** — reasonable from the platform's configurable architecture.
- **Gap (31, 18%)** — not evidenced; acknowledged and committed for delivery or accepted as contractual terms.



This section provides the per-domain compliance declaration that will drive the Tab.F response-sheet entries. The detailed Yes/No/Partial + detail per row will be entered in the Excel Response Sheet; this narrative summarises the posture and the disqualifying-gap handling.

## Functional Requirements (FR01–FR73)

**Grounded (directly evidenced):** FR04, FR05, FR06, FR16, FR19, FR25, FR33, FR34, FR35, FR36, FR37, FR40, FR41, FR45, FR46, FR47, FR49, FR52, FR53, FR55, FR58, FR59, FR60, FR61, FR62, FR63, FR64, FR65, FR66, FR67.

**Assertable (architecturally reasonable):** FR01, FR02, FR03, FR08, FR09, FR11, FR12, FR13, FR14, FR15, FR18, FR22, FR24, FR28, FR29, FR30, FR31, FR32, FR38, FR42, FR43, FR44, FR48, FR50, FR51, FR54, FR56, FR57, FR68, FR70, FR71, FR73.

**Gap (acknowledged / committed for delivery):**

- **FR07** — configurable frame rates/resolutions per camera.
- **FR10** — detect camera occlusion/lens obstruction/glare.
- **FR17** — camera-based GSE type classification (disqualifying).
- **FR20** — personnel presence in apron zones (disqualifying).
- **FR21** — personnel entering restricted zones.
- **FR23** — PPE detection.
- **FR26** — per-event confidence scores.
- **FR27** — manual validation/correction.
- **FR39** — exception annotations.
- **FR69** — per-model accuracy tracking.
- **FR72** — Phase-2 aerobridge pax counting / airline data integration.

## Non-Functional Requirements (NF01–NF48)

**Grounded:** NF02, NF04, NF06, NF07, NF15, NF16, NF25, NF32, NF33, NF34, NF35, NF36, NF39, NF41, NF42, NF43, NF45, NF46.

**Assertable:** NF01, NF03, NF08, NF11, NF12, NF13, NF14, NF21, NF22, NF24, NF27, NF28, NF29, NF30, NF31, NF37, NF38, NF40, NF44, NF48.

**Gap (acknowledged / committed):**

- **NF05** — 3-year availability history.
- **NF09** — QA standards/accreditations/methodologies.
- **NF10** — QA tools & technology.
- **NF17** — 24/7/365 phone/email/online.
- **NF18** — client-configurable help & knowledge artefacts.
- **NF19** — severity response scenarios (disqualifying).
- **NF20** — Sev-3 resolution within 8 business hrs.
- **NF23** — help-desk field-level info.
- **NF26** — customised quick-reference guides.
- **NF47** — geolocation on authentications.

## Project Management Requirements (PMR-01..PMR-10)

**Grounded:** PMR-02c, PMR-02e, PMR-05, PMR-06c.

**Assertable:** PMR-01, PMR-02, PMR-02a, PMR-02b, PMR-02d, PMR-02f, PMR-03, PMR-04, PMR-06, PMR-06a, PMR-06b, PMR-06d, PMR-07, PMR-08, PMR-09.

**Gap:**

- **PMR-10** — 6-month defects liability + maintenance agreement.

## ISRA (rows 1–29)

**Grounded:** ISRA-01, 03, 04, 05, 07, 08, 09, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 28, 29.

**Assertable:** ISRA-02, 06, 10, 21, 24, 26.

**Gap:**

- **ISRA-19** — data sovereignty (disqualifying).
- **ISRA-25** — hosting geographical address (disqualifying).
- **ISRA-27** — application whitelisting.

## Disqualifying-gap handling summary

| Req | Gap | Handling | Where addressed |
| ----- | ----- | ---------- | ----------------- |
| FR17 | Camera-based GSE type classification | Committed CV classifier delivery with per-class acceptance criteria; 20% withhold protects BAC | Sections 03, 04 (D12), 13 |
| FR20 | Personnel presence in apron zones | Committed CV model delivery with acceptance criteria; prerequisite for FR21/FR23 | Sections 03, 04 (D13), 13 |
| NF19 | Sev-1 ≤1h 24×7×365 SLA | Committed support matrix meeting/exceeding thresholds; follow-the-sun via multi-region offices; priced in Schedule E | Sections 10, 04 (D15), 13 |
| ISRA-19 | Data sovereignty | Australian hosting commitment (AWS Sydney ap-southeast-2 or BAC private cloud); rewrite all residency/privacy/ownership to Australian frame | Sections 08, 04 (D16), 13 |
| ISRA-25 | Hosting geographical address | Australian data-centre address supplied in completed ISRA tab once hosting target confirmed | Sections 08, 04 (D16), 13 |



> Commercial and insurance responses are in Section 12.

---

# 12: Commercial and Insurance Response

## Insurance

RFP §4.4 requires the following insurance bars, which WAISL will meet as a condition of contract:

| Insurance | RFP minimum | WAISL commitment |
| ----------- | ------------- | ------------------ |
| Workers Compensation | Per Workers' Compensation and Rehabilitation Act 2003 (Qld) | Committed (architecturally supported) |
| Public Liability | $20 million | Committed (architecturally supported) |
| Professional Indemnity | $10 million | Committed (architecturally supported) |
| Cyber Security Insurance | $10 million | Committed (architecturally supported) |
| Other insurances | As required by law | Committed (architecturally supported) |



## Commercial model

The RFP contemplates a 3-year initial term with two by-one-year extensions tied to SLA, sustainability, and performance targets (§4.3). Schedule E requires a 5-year pricing breakdown across Implementation, Integrations, Hardware, License, Support, Maintenance, and Additional categories.

**Pricing is not in scope of this draft.** No pricing data, rate card, or commercial model exists in the collateral. All pricing values are placeholders to be supplied in Schedule E.

## Commercial commitments we can make

- **20% practical-completion withhold (PMR-09)** — accepted.
- **6-month defects liability (PMR-10)** — accepted.
- **Escrow (ISRA-20)** — source-code escrow with a recognised third-party agent, updated with each major release.
- **Exit plan** — BAC data returned in machine-readable format within 15 working days; secure erasure with Certificate of Data Destruction.
- **Support SLA matrix** — committed matrix meeting/exceeding NF19 (see Section 10); cost implications in Schedule E.
- **Australian hosting (ISRA-19, ISRA-25)** — committed; cost implications (if any for private-cloud option) in Schedule E.
- **Customised quick-reference guides (NF26)** — committed; cost stated in Schedule E if additional.

## Open commercial questions

- Civil/hardware install costs — borne by BAC or supplier? The Response Sheet notes this is unresolved.
- 5-year pricing envelope / target ROI — not specified.
- Phase-2 items (FR72) in this contract or deferred?

## Form of agreement

WAISL will enter into the BAC Relationship / Master Services Agreement (Annexure B). Departures (if any) will be returned with the response; otherwise the contract will be deemed accepted.

## Proposal validity

Proposals remain valid for 90 calendar days from the Proposal Closing Time (RFP §4.2; Annexure A §1).

> Deviations, clarifications, and the assumptions register are in Section 13.

---

# 13: Deviation, Clarifications, and Assumptions Register

## Purpose

This register consolidates every deviation, clarification, and assumption in the proposal so that BAC can evaluate them transparently. It is the honest companion to Section 11's compliance posture: where we cannot ground a requirement, we say so here and state the mitigation.

## Disqualifying-gap deviations

| ID | Req | Deviation / Gap | Mitigation | Disposition |
| ---- | ----- | ----------------- | ------------ | ------------- |
| DEV-01 | FR17 | Collateral evidences telematics-based GSE tracking, not camera-based classification of the full enumerated GSE-type list (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, tractors, golf carts). | Committed CV classifier delivery in Phase 1, with per-class precision/recall acceptance criteria agreed in Detailed Design; telematics identity fused with CV classification; 20% practical-completion withhold (PMR-09) protects BAC financially; named CV delivery partner in Detailed Design. | Gap acknowledged; delivery commitment; Tab.F row marked Partial pending Test-phase acceptance. |
| DEV-02 | FR20 | No personnel-detection capability via camera is evidenced in collateral. | Committed personnel-presence CV model on the Edge Vision Controller, scoped to apron zones (excluding passenger terminal zones), with acceptance criteria; prerequisite for FR21 and FR23. | Gap acknowledged; delivery commitment; Tab.F row marked Partial pending Test-phase acceptance. |
| DEV-03 | NF19 | No tiered support SLA matrix in collateral. | Committed Sev-1 ≤1h 24×7×365, Sev-2 ≤4h business / ≤8h non-business, Sev-3 ≤8 business hrs matrix (Section 10); follow-the-sun via WAISL UK/India/UAE/Kuwait/Australia/Singapore offices; priced in Schedule E. | Gap acknowledged; committed matrix meeting/exceeding NF19 thresholds. |
| DEV-04 | ISRA-19 | UTAM artefact frames data sovereignty as EU residency under GDPR/NIS2 — conflicts with BAC/Australia. | Australian hosting commitment (AWS Sydney ap-southeast-2 or BAC private cloud); all residency/privacy/ownership narrative rewritten to Australian Privacy Act 1988 / APPs / ASD Essential 8 framing; BAC is the exclusive data owner. | Gap reconciled via commitment; subject to BAC confirming hosting target at Initiation. |
| DEV-05 | ISRA-25 | UTAM cites EU/Athens data-centre addresses. | Australian data-centre address (AWS Sydney ap-southeast-2 default, or BAC private-cloud address) supplied in the completed ISRA tab once hosting target confirmed. | Gap reconciled via commitment. |

## Manageable-gap deviations

| ID | Req | Deviation / Gap | Mitigation |
| ---- | ----- | ----------------- | ------------ |
| DEV-06 | FR07 | Per-camera frame-rate/resolution configuration not evidenced. | Committed Edge configuration pack in Detailed Design. |
| DEV-07 | FR10 | Camera occlusion/glare detection not evidenced. | Committed CV pre-processing feature with acceptance criteria. |
| DEV-08 | FR21 | Restricted-zone monitoring shown for vehicles/GSE, not personnel. | Reuses geofence + personnel CV model (depends on FR20). |
| DEV-09 | FR23 | PPE detection not evidenced. | Committed CV model where camera quality allows; acceptance criteria tied to camera-quality survey. |
| DEV-10 | FR26/27/69 | Per-event confidence scores, manual validation/correction UI, per-model accuracy tracking not evidenced. | Committed AI-governance pack (Deliverable D14) in Phase 1. |
| DEV-11 | FR39 | Exception annotations by operational staff not shown. | Committed in Detailed Design; Partial in Tab.F. |
| DEV-12 | FR48 | Raw video playback per event not confirmed (Turnwise Playback replays movement on map). | Committed in Detailed Design; Partial in Tab.F. |
| DEV-13 | FR72 | Phase-2 aerobridge pax counting / airline data integration. | Roadmap commitment for Phase 2. |
| DEV-14 | NF05 | 3-year availability history not provided. | Commit to SLA reporting going forward; publish historical metrics from existing deployments if available. |
| DEV-15 | NF09/NF10 | QA standards/tools/methodology not in collateral. | To be supplied from WAISL internal QA documentation before submission. |
| DEV-16 | NF17 | 24/7/365 phone/email/online not explicitly stated. | Committed via follow-the-sun multi-region model. |
| DEV-17 | NF18/NF23/NF26 | Help/knowledge artefacts, field-level help, quick-reference guides not evidenced. | Committed in PMR-07/PMR-08; cost in Schedule E if additional. |
| DEV-18 | NF47 | Geolocation on authentications not evidenced. | Committed; low-cost feature. |
| DEV-19 | PMR-10 | 6-month defects liability + maintenance agreement not in collateral. | Accepted contractual term. |
| DEV-20 | ISRA-21 | UTAM frames privacy via GDPR; BAC needs Australian Privacy Act / APPs. | Reframed to Australian Privacy Act 1988 / APPs with pseudonymisation/anonymisation. |
| DEV-21 | ISRA-24 | Incident plans exist; regular testing not evidenced. | Committed test cadence. |
| DEV-22 | ISRA-27 | Application whitelisting not evidenced. | Committed in ISRA response. |

## Source-conflict-driven deviations (rewrite, not propagate)

The UTAM architecture document is a repurposed Athens International Airport (AIA) artefact with EU/GDPR/Hellenic-DPA framing. The following passages are **excluded** from BAC proposal text and replaced with Australian-framed equivalents:

- "adapt the platform to Athens Airport needs" → rewritten for BNE.
- "exclusive property of Athens International Airport (AIA)" → BAC is the exclusive data owner.
- "hosted exclusively within European Union (EU) data centres" → committed to Australian hosting.
- "AWS EU region deployment... GDPR and NIS2" → AWS Sydney ap-southeast-2 or BAC private cloud; Australian Privacy Act / APPs / ASD Essential 8.
- "the Hellenic Data Protection Authority" → removed; Australian Privacy Act / OAIC framework.
- "developed and implemented by Brisbaine Airport" (factually incorrect) → WAISL developed UTAM; BAC is the customer.
- Entire GDPR Compliance section (§12) → replaced with Australian Privacy Act compliance narrative.



## Clarifications requested from BAC

1. Hosting target — AWS Sydney (ap-southeast-2) or BAC private cloud? (affects ISRA-19, ISRA-25, NF04, all residency claims)
2. Are camera-based auto-detection of all FR24 sub-activities in scope for Phase 1, or can some be delivered as CDM/telematics-sourced timestamps? (affects FR13/14, FR17/18, FR24–28 classification)
3. Does BAC have a preferred camera model list ("BAC supported camera models", FR01)?
4. Expected 5-year pricing envelope / target ROI?
5. Does BAC require ASD Essential 8 / IRAP alignment explicitly, or is ISO 27001 sufficient? (affects ISRA-01, ISRA-14, NF01)
6. Are Phase-2 items (FR72 aerobridge pax counting, FR73 mobile/tablet) truly Must-Have in this contract or deferred?
7. Civil/hardware install costs — borne by BAC or supplier?

## Assumptions

- A1: BAC will provide AODB, FIDS, A-CDM/AIDX, and camera infrastructure access in the Test and Prod environments per the integration scope agreed at Initiation (NF08).
- A2: BAC will confirm the Australian hosting target (AWS Sydney or BAC private cloud) at Initiation.
- A3: BAC will provide named referees and Schedule C content directly or via WAISL's reference-gathering process.
- A4: The 5-page optional PDF will be used to present the disqualifying-gap mitigations and the FR17/FR20 CV delivery roadmap in summary form.
- A5: WAISL's Australia office provides the local account-representative escalation point (NF22) and local support presence.

## What we will not fabricate

We will not invent team bios, referees, case studies, pricing values, or certifications. Each of these is marked as placeholder in this draft and must be supplied before submission.

> Relevant experience (and the limits of our collateral) is addressed in Section 14.

---

# 14: Relevant Experience

## The honest position

Schedule C requires two referees and relevant-experience evidence for key personnel. Our collateral does not contain named client engagements, quantified metrics for underwing-analytics deployments, Australian airport references, or case studies. We will not fabricate referees, case studies, or named personnel.

## What we can ground

- **WAISL is an airport-operations software house** with a productised Turnwise/UTAM platform already in airport use, evidenced by the Turnwise Product Document (1.0, 29 June) and the UTAM Solution Architecture.
- **WAISL operates a multi-region footprint** — UK | India | UAE | Kuwait | Australia | Singapore — providing local presence in Australia and follow-the-sun support.
- **WAISL holds ISO certifications** — 9001, 20000, 27001, 22301 — covering quality, IT service, information security, and business continuity.
- **The Turnwise product evidences operational capability** in flight tracking, stand tracking, GSE/vehicle tracking, turnaround monitoring, CDM milestone tracking, critical activity tracking, airside safety and restricted-zone monitoring, operational reports, playback, weather/RVR, dashboards/KPIs, airport geofence, monitoring dashboard, user/airline/GHA management, alerts, hybrid deployment, and system integrations.

## What we cannot ground

- **Named client engagements and quantified underwing-analytics deployment metrics** — not in collateral.
- **Australian airport references** — Turnwise infographic uses an Istanbul–Naples (IST–NAP) example route and non-Australian aircraft registration (TCLPO/A21N), signalling the collateral is generic/global, not Brisbane-specific. We will reframe examples for BNE before submission.
- **Named referees (Schedule C requires two)** — not provided in collateral.
- **Named personnel, resumes, and certifications of key staff** — not in collateral.
- **Evidence of established relationships with required equipment suppliers (PMR-01)** — not in collateral.

## Delivery-partner approach

The Response Sheet Start tab indicates the bid is being authored from the WAISL perspective with a vendor partner (kloudspot) for the camera/computer-vision elements. This is consistent with the disqualifying-gap handling in Sections 03 and 13: the FR17 GSE-type CV classifier and the FR20 personnel-presence model are the areas where specialist computer-vision delivery is required, and a named CV delivery partner will be confirmed in the Detailed Design and in Schedule A (sub-contractors).

We will ensure the final response does not leak internal assignment notes (e.g., "WAISL (PQ)", "WAISL + Vendor (kloudspot)") into the submitted Schedules.

## What we will supply before submission

- Two referees with relevant airport/airside-analytics deployment experience (Schedule C).
- Named key personnel and resumes (Schedule A/C).
- Current certificates of currency for insurance (Schedule A).
- ISO 27001 / 9001 / 20000 / 22301 certificate evidence (Schedule A).
- Sub-contractor identification (Schedule C) for the CV delivery partner.

## Limitations acknowledged

This proposal's relevant-experience section is the weakest part of the response, and we acknowledge that honestly. The platform's technical capability is grounded; the commercial and team evidence is not. BAC's evaluation criteria weight Relevant Experience as a mandatory factor (RFP §4.6), and the shortlisted-presentation stage (§4.8) will test team credibility live. We propose to close this gap by supplying named referees, named personnel, and case studies before the shortlist presentation, rather than fabricating them in this written submission.

> This concludes the section draft. Section assembly, empathy review, and compliance validation follow.

---

# Tone-Gate Note

Stop-slop tone gate applied to all narrative sections (exec summary, understanding, technical solution, implementation, governance, integration, security narrative, testing, support, relevant experience). Compliance tables (Section 11), the deviation/assumption register (Section 13), SLA/KPI spec tables, mandatory forms, and deliverable/assumption bullet lists were carved out per the RFP carve-out. Technical adverbs (fully, commercially, operationally, contractually) and formal third-person buyer voice were preserved. Evidence markers ([GROUNDED]/[ASSERTION]/[GAP]) were preserved through review and stripped only at assembly.

Scores (Directness/Rhythm/Trust/Authenticity/Density, out of 10; section passes at >=35/50):

| Section | D | R | T | A | Dn | Total | Revised? |
|---------|---|---|---|---|----|-------|----------|
| 01 Executive Summary | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 02 Understanding of Requirements | 7 | 7 | 8 | 8 | 7 | 37 | No (pass) |
| 03 Technical Solution | 8 | 7 | 8 | 8 | 7 | 38 | Yes (was 30; em-dash heavy, rambling parentheticals) |
| 04 Scope Coverage (deliverables table carved out) | 8 | 7 | 8 | 8 | 7 | 38 | No (pass; table carved out) |
| 05 Implementation Methodology | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 06 Project Management & Governance (RACI carved out) | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 07 Integration, Data, Technical Approach | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 08 Security, ISRA & Compliance (ISRA rows + HA/DR table carved out) | 8 | 7 | 8 | 8 | 7 | 38 | Yes (was 29; narrative em-dash heavy) |
| 09 Testing, Acceptance, Handover | 7 | 7 | 8 | 8 | 7 | 37 | No (pass) |
| 10 Support, SLA & Maintenance (SLA matrix carved out) | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 11 Compliance with Tab.F (carved out — compliance table) | n/a | n/a | n/a | n/a | n/a | n/a | Carved out |
| 12 Commercial & Insurance (insurance table carved out) | 7 | 7 | 8 | 8 | 7 | 37 | No (pass; table carved out) |
| 13 Deviation/Assumptions Register (carved out — register) | n/a | n/a | n/a | n/a | n/a | n/a | Carved out |
| 14 Relevant Experience | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |

Sections revised (score <35 before, >=35 after): 03 (30 -> 38) and 08 (29 -> 38). No section remains below 35 after revision. Em dashes removed from revised narrative prose; markers preserved during review and stripped at assembly. No content fabricated; declared gaps retain committed resolution paths.

