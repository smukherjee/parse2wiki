# 03 — Technical Solution

## The problem this section answers

BAC needs camera-and-AI-driven automatic detection, classification, timestamping, sequencing, and analysis of underwing activities, fused with operational flight data, with real-time and historical visibility, configurable alerts, and enterprise-grade security. This section describes the Turnwise/UTAM technical architecture, grounds what is evidenced, and is explicit about the disqualifying gaps in camera-AI detection (FR17, FR20) and how we will close them.

## Architecture overview

WAISL proposes the UTAM (Unified Total Airside Management) platform, productised as Turnwise, deployed for BAC. UTAM is an AI-enabled airport operations platform built on a layered architecture. [GROUNDED: UTAM Solution Architecture v1 — Executive Summary; Turnwise Product Document 1]

- **Edge Layer**: Edge Data Ingestor integrates airport operational, IoT, and OT systems (AODB, CCTV cameras, BAS, IoT sensors, TETRA radio, third-party vendor systems) with protocol adaptation (REST, SOAP, file-based, streaming, OPC-UA), schema normalisation, buffering and retry for intermittent connectivity, and encrypted transmission. Edge Vision Controller processes video streams from CCTV and edge cameras using computer vision models to extract structured metadata (queue length, dwell time, wait times, processing times, security incidents) and publishes events to the platform via streaming interfaces. [GROUNDED: UTAM Edge Layer table]
- **Platform Ingestion & Messaging**: HTTPS Gateway (TLS, mutual auth), Platform Data Ingestion (batch/micro-batch/streaming, schema evolution, quality checks), Message Queue (event backbone, topic streaming, replay, horizontal scaling), Message Service. [GROUNDED: UTAM Platform Ingestion table]
- **Core Data & Processing**: Lakehouse (medallion: Bronze/Silver/Gold), Operational Database (low-latency current state), Data Catalogue & Governance (lineage, schema registry, quality enforcement), Workflow Engine (event-driven, retry, escalation, audit), Rules Engine (threshold/pattern/correlation anomaly detection, aggregation, prioritisation), Reporting Service. [GROUNDED: UTAM Core Data table]
- **External Interfacing**: API Gateway (REST/SOAP routing, auth, rate limiting), Application Load Balancer, Route 53, SSO/OIDC via Azure Entra ID. [GROUNDED: UTAM External Interfacing table]
- **UI Layer**: operational dashboards, alerts view, user management & configuration, reports. [GROUNDED: UTAM UI table]
- **Security & Monitoring**: AWS KMS, Secrets Manager, WAF, GuardDuty, CloudTrail, CloudWatch, Inspector. [GROUNDED: UTAM Security & Monitoring table]

The platform is "deployment agnostic": it can run in AWS cloud or in BAC's private cloud, with all functional, security, and performance commitments remaining identical. [GROUNDED: UTAM Deployment Architecture note]

## What the architecture already does, grounded against Tab.F

The Turnwise product document evidences the operational backbone BAC requires:

- **Flight tracking & flight information**, flight miles view (70/40/10-mile countdown), flight summary and POBT. [GROUNDED: Turnwise — Flight Tracking; Flight Miles; Flight Summary]
- **Stand tracking** with real-time occupancy, next-allocated flights, actual/planned stand utilisation, gate utilisation reports. [GROUNDED: Turnwise — Stand Tracking; Stand Utilization]
- **GSE, vehicle tracking and utilisation**: movement monitoring, path traversal (last 15 min), vehicle cards, GSE usage master, vehicle last location, GSE master, speed violation reports. [GROUNDED: Turnwise — GSE/Vehicle Tracking; GSE Usage Master; Speed Violation]
- **Taxi time monitoring (VTT)**, runway occupancy time (ROT), turnaround time monitoring with a graphical Gantt of ground-handling activities against CDM milestones and a live "NOW" marker. [GROUNDED: Turnwise — Taxi Time Monitoring; Runway Occupancy; Turnaround Time Monitoring]
- **CDM milestone tracking** across inbound/turnaround/outbound (EOBT-3 through ATOT). [GROUNDED: Turnwise — CDM Milestone Tracking]
- **Critical activity tracking** showing completed/pending/needs-attention. [GROUNDED: Turnwise — Critical Activity Tracking]
- **Airside safety and restricted-zone monitoring** with speed violation and restricted-zone entry alerts. [GROUNDED: Turnwise — Airside Safety; Alerts]
- **Operational reports**: TMO, VTT, ROT, stand utilisation, turnaround SLA, flight SLA, flight performance, GSE usage, speed violations, restricted-zone entry leaders, airline-wise OTP. [GROUNDED: Turnwise — Operational Reports]
- **Playback**: replay past movement/activity (Pause/Rewind, 1x/2x/4x) for delay analysis, incident review, training. [GROUNDED: Turnwise — Playback]
- **Weather and RVR visibility** alongside operations. [GROUNDED: Turnwise — Weather/RVR]
- **Dashboard, KPI and slot performance** (flights arrived/departed/cancelled, OTP %, avg delay, taxi times, stand occupancy). [GROUNDED: Turnwise — Dashboard]
- **Airport geofence**: configured geofence areas (name, address, group, category, coordinates polygon). [GROUNDED: Turnwise — Airport Geofence]
- **Monitoring dashboard**: data-sync health across AODB, ADS-B, Video Events, Vehicle Data. [GROUNDED: Turnwise — Monitoring Dashboard]
- **User, airline, GHA management**; **alerts** (speed violation, turnaround SLA); **hybrid deployment**; **system integrations**. [GROUNDED: Turnwise — User/Airline/GHA Management; Alerts; Hybrid Deployment; System Integrations]

This grounds FR04, FR16, FR19, FR25, FR33–FR37, FR40–FR41, FR45–FR47, FR49, FR53, FR59, FR60, FR61–FR66 and the operational-reporting/dashboard portions of the RFP. [GROUNDED: coverage-matrix.md Evidence Inventory]

## Camera onboarding, aircraft detection, and the activity-detection backbone

UTAM's Edge Vision Controller performs inference at the edge on CCTV/edge camera streams and publishes structured events for real-time alerts, DCB, and situational-awareness dashboards. [GROUNDED: UTAM Edge Vision Controller] The Edge Data Ingestor onboards new cameras and systems via low-code vendor-agnostic onboarding. [GROUNDED: UTAM Edge Data Ingestor — "vendor-agnostic onboarding of new systems with minimal configuration effort, through its low-code ability"]

For FR01–FR03 (onboarding fixed cameras, grouping by airport/terminal/gate/stand/airline/handler, configuring FOV and parking zones), the Edge layer provides the mechanism. [ASSERTION: UTAM Edge Vision Controller ingests CCTV/edge cameras; Turnwise airline/GHA/stand management implies the grouping dimension — coverage-matrix FR01–FR03]

For FR13/FR14 (aircraft arrival/departure detection and on-block/off-block confirmation), Turnwise stand/flight tracking detects arrival and correlates with AODB; camera-based on-block confirmation is the asserted extension. [ASSERTION: Turnwise stand/flight tracking detects arrival; on-block via camera to be confirmed in detailed design — coverage-matrix FR13/FR14]

For FR15 (AIDX identification of aircraft type/reg/flight/airline), Turnwise displays these fields via AODB/ADS-B; a named AIDX connector is an asserted addition via the API Gateway. [ASSERTION: Turnwise shows these fields via AODB/ADS-B; AIDX connector to be added via API Gateway — coverage-matrix FR15, FR43, FR54]

## Disqualifying gap 1, FR17: camera-based GSE type classification

**Requirement (FR17, Must-Have):** detect and classify GSE types via camera (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, tractors, golf carts).

**Evidence position:** Turnwise tracks GSE via telematics/GPS and exposes a "vehicle type" field, but our collateral does not evidence camera-based classification of the full enumerated list. [GAP: FR17 — gap-report.md §1]

**How we address it:** We will not claim capability we have not evidenced. Our approach is to combine telematics-sourced GSE identity (already grounded) with a computer-vision classification model trained on the FR17 enumerated classes, delivered as a committed Phase-1 workstream with acceptance criteria tied to per-class precision/recall thresholds agreed with BAC. [ASSERTION: combining grounded telematics identity with a CV classifier for the enumerated classes is a feasible delivery path given UTAM's Edge Vision Controller already runs CV inference for queue/dwell/security metadata — coverage-matrix FR17 action]

We acknowledge that, absent a demonstrated prior deployment of this specific classifier, this remains a gap that we propose to close through delivery commitment rather than claim of existing capability. The risk to BAC is mitigated by: (a) phased acceptance, where the classifier must pass per-class accuracy criteria in the Test phase before the corresponding Tab.F row is marked conformant; (b) the 20% practical-completion withhold (PMR-09) protecting BAC financially; (c) a named CV delivery partner in the detailed design. [ASSERTION: standard delivery-risk mitigation pattern for a committed-but-not-yet-deployed CV model — coverage-matrix FR17 action; gap-report.md §1]

## Disqualifying gap 2, FR20: personnel presence in apron zones (excluding passengers)

**Requirement (FR20, Must-Have):** detect personnel presence in apron zones, excluding passengers.

**Evidence position:** no personnel-detection capability is evidenced in either Turnwise or UTAM. UTAM's Edge Vision Controller extracts "queue length, dwell time, wait times, processing times, security incidents", not personnel presence in defined apron zones. [GAP: FR20 — gap-report.md §1; coverage-matrix FR20]

**How we address it:** We will deliver a personnel-detection CV model on the Edge Vision Controller, scoped to apron zones (excluding passenger terminal zones), with the same acceptance-criteria discipline as FR17. This is also a prerequisite for FR21 (personnel entering restricted zones) and FR23 (PPE detection where camera quality allows), both of which are currently gaps. [ASSERTION: extending the Edge Vision Controller's existing CV inference pipeline to a person-detection/classification model is architecturally consistent — coverage-matrix FR20/FR21/FR23] [GAP: FR23 — PPE detection not evidenced — gap-report.md §1]

We are explicit: these three rows (FR17, FR20, FR23) are the areas where our existing collateral is weakest relative to the RFP's core camera-AI ask. We propose to close them through delivery, not through assertion in this proposal.

## Turnaround activity detection (FR24) and AI governance (FR26–FR28, FR68–FR71)

**FR24 (Must-Have):** auto-detect start/end of chocking, aerobridge dock/undock, stair position/removal, GPU connect/disconnect, baggage load/unload, catering, refuelling on bay, pushback readiness, cabin cleaning.

Turnwise's turnaround Gantt shows activities with start/end times and a completion check, sequenced into a single turnaround timeline (FR25, grounded). Whether each listed activity's start/end is camera-AI derived or telematics/CDM derived is to be confirmed in detailed design. [ASSERTION: Turnwise turnaround activity Gantt shows activities with start/end; camera-AI auto-detection of each listed activity to be confirmed — coverage-matrix FR24]

**FR26 (confidence scores per event):** not evidenced. [GAP: FR26 — coverage-matrix]
**FR27 (manual validation/correction of detected timestamps):** not shown in collateral. [GAP: FR27 — coverage-matrix]
**FR28 (learn from corrections):** UTAM's AI/ML platform implies a learning loop but no specific continuous-learning feature is shown. [ASSERTION: UTAM AI/ML platform implies continuous learning; no specific feature shown — coverage-matrix FR28]
**FR68 (versioned AI models), FR69 (per-model accuracy tracking), FR70 (airport-specific tuning), FR71 (continual improvement):** versioned release train is asserted; per-model accuracy tracking is a gap. [ASSERTION: UTAM semantic versioning/release train; model-versioning not explicit — coverage-matrix FR68] [GAP: FR69 — coverage-matrix]

We commit to a per-event confidence score, a manual validation/correction UI, a learning loop feeding model retraining, and per-model accuracy tracking, all delivered as Phase-1 capabilities with acceptance criteria, rather than claimed as existing. [ASSERTION: standard AI-governance capability committed for delivery — coverage-matrix FR26–FR28, FR69 action]

## Alerts, dashboards, and analytics (FR40–FR53)

Configurable alerts when activities exceed planned duration (FR40), unsafe/prohibited activity alerts (FR41), and camera/AI-confidence-degradation alerts (FR42) are grounded in Turnwise's Turnaround SLA alert, Speed Violation alert, and UTAM Rules Engine respectively. [GROUNDED: Turnwise Alerts; UTAM Rules Engine — coverage-matrix FR40, FR41] [ASSERTION: UTAM Rules Engine could raise AI-confidence-degradation alerts; not pre-built — coverage-matrix FR42]

Alert channels (FR43): UTAM supports SMS, voice, email, Microsoft Teams, TETRA radio, mobile/web notifications; an AIDX-specific API alert channel is an asserted addition via the API Gateway. [GROUNDED: UTAM Multi-Channel Notification — coverage-matrix FR43] [ASSERTION: AIDX alert publication via API Gateway — coverage-matrix FR43]

Live turnaround status board per gate (FR45), current activity state and next expected milestone (FR46), colour-coded delay indicators (FR47), live/historical video playback per event (FR48), turnaround KPIs by airline/aircraft type/gate/service provider (FR49), trend/variance analysis (FR50), AI-driven improvement insights (FR51), ad-hoc queries/filters (FR52), and historical analysis (FR53) are grounded or assertable from Turnwise and UTAM Self-Service BI. [GROUNDED: Turnwise turnaround monitoring, critical activity tracking, red delay indicators, airline-wise OTP, Self-Service BI — coverage-matrix FR45–FR53] [ASSERTION: lakehouse + reporting supports trend/variance; not explicitly shown — coverage-matrix FR50] [ASSERTION: UTAM AI/ML platform implies AI-driven insights — coverage-matrix FR51]

Live & historical video playback per event (FR48): Turnwise Playback replays movement on the map; raw video playback per event is to be confirmed. [ASSERTION: Turnwise Playback replays movement on map; raw video per event to be confirmed — coverage-matrix FR48] [GAP: FR39 — exception annotations by operational staff not shown — coverage-matrix]

## Integration and data architecture (FR54–FR59, NF15–NF16)

UTAM's integration layer provides an API Gateway (REST/SOAP), event streaming, and a connector framework. Listed connectors include AODB, ADS-B, telematics, vision analytics, weather, RVR. [GROUNDED: UTAM Integration Layer; UTAM connectors table — coverage-matrix FR55, NF15, NF16]

AODB integration is grounded (FR33, FR16). FIDS and an explicit AIDX connector are asserted additions. [GROUNDED: Turnwise AODB integration — coverage-matrix FR33, FR16] [ASSERTION: UTAM AODB + A-CDM; FIDS not named; AIDX not explicitly — coverage-matrix FR54]

Configurable data retention (FR58) is grounded in UTAM retention policies; event metadata stored separate from video (FR57) is asserted from the lakehouse separation; publishing actual timestamps to consuming systems (FR56) is asserted via the API Gateway. [GROUNDED: UTAM retention policies — coverage-matrix FR58] [ASSERTION: UTAM lakehouse separates structured metadata; video stored separately — coverage-matrix FR57] [ASSERTION: API Gateway supports publish — coverage-matrix FR56] Forensic replay for incident investigation (FR59) is grounded in Turnwise Playback. [GROUNDED: Turnwise Playback — coverage-matrix FR59]

## Administration, access control, and environments (FR60–FR67)

RBAC (FR60), airline/service-provider data segregation (FR61), configurable permissions per role (FR62), admin tools for configuration management (FR63), environment separation Dev/Test/Prod (FR64), operational monitoring/health dashboards (FR65), admin configuration of alerts/reports/dashboard/users (FR66), and SSO for BAC users via Azure AD with local accounts and password policies/MFA for non-BAC users (FR67) are all grounded in UTAM's RBAC/ABAC, row-level access, IaC environment parity, and Azure Entra ID / OpenLDAP / OneLogin SSO. [GROUNDED: UTAM RBAC/ABAC, row-level access, IaC env parity, Azure Entra ID SSO + OpenLDAP/OneLogin + password policies + MFA — coverage-matrix FR60–FR67]

## Future-phase items (FR72, FR73)

FR72 (Phase-2 airline data integration; aerobridge camera pax counting/crew boarding) is a future-phase gap. [GAP: FR72 — future phase, not in collateral — coverage-matrix FR72]
FR73 (remote access via mobile and tablet) is asserted from UTAM's browser-based responsive UI. [ASSERTION: UTAM browser-based responsive UI — coverage-matrix FR73]

## Extensibility

The platform's configuration-over-code principle (every operationally variable element is parameterised, version-controlled, and manageable by authorised business users) provides the extensibility RFP §3.3 requires. [GROUNDED: UTAM Parameterization, Configuration & Self-Service] The Lakehouse medallion architecture supports schema evolution, time travel, and high-performance query, enabling future operational and analytical use cases. [GROUNDED: UTAM Lakehouse]

> How this technical solution maps to scope coverage and deliverables is set out in Section 04.