# 04 — Scope Coverage and Deliverables

## What this section answers

BAC requires a single-source-of-truth underwing analytics solution covering the full scope in RFP §3.3 and Tab.F. This section maps the scope to deliverables, states what is in scope, and is explicit about the rows we cannot fully ground.

## Scope coverage by Tab.F domain

### Camera and video ingestion (FR01–FR12)

- FR01 onboard fixed cameras (BAC-supported models), FR02 grouping by airport/terminal/gate/stand/airline/handler, FR03 FOV & parking-zone configuration — Edge Data Ingestor low-code onboarding and Turnwise grouping dimensions. [ASSERTION: UTAM Edge Vision Controller ingests CCTV/edge cameras; Turnwise airline/GHA/stand management implies grouping — coverage-matrix FR01–FR03]
- FR04 geofenced zones (safety envelope, equipment staging, personnel walk zones) — Turnwise Airport Geofence. [GROUNDED: Turnwise Airport Geofence — coverage-matrix FR04]
- FR05 live video ingest — Edge Vision Controller / HTTPS Gateway. [GROUNDED: UTAM Edge Vision Controller — coverage-matrix FR05]
- FR06 buffering during network interruptions — Edge Data Ingestor buffering and retry. [GROUNDED: UTAM Edge Data Ingestor — coverage-matrix FR06]
- FR07 configurable frame rates/resolutions per camera. [GAP — coverage-matrix FR07]
- FR08 timestamp via synchronised airport time source. [ASSERTION: UTAM NTP/time-synchronised logging — coverage-matrix FR08]
- FR09 continuous camera availability/signal monitoring; notify vendor on failure. [ASSERTION: UTAM Monitoring Dashboard checks data-sync health; camera-specific not shown — coverage-matrix FR09]
- FR10 detect occlusion/lens obstruction/glare. [GAP — coverage-matrix FR10]
- FR11 alerts for AI-accuracy degradation. [ASSERTION: UTAM Rules Engine could raise such alerts; not pre-built — coverage-matrix FR11]
- FR12 camera health dashboard. [ASSERTION: Turnwise Monitoring Dashboard adjacent — coverage-matrix FR12]

**Deliverable:** Edge Vision Controller configuration pack (FR01–FR05, FR08), camera health and AI-degradation alerting rules (FR09, FR11, FR12), and a committed delivery workstream for FR07 (per-camera frame-rate/resolution configuration) and FR10 (occlusion/glare detection) with acceptance criteria. [ASSERTION: standard delivery commitment for the two gap rows — coverage-matrix FR07/FR10 action]

### Aircraft detection (FR13–FR16)

- FR13/FR14 arrival/departure detection and on-block/off-block confirmation. [ASSERTION: Turnwise stand/flight tracking detects arrival; on-block via camera to be confirmed — coverage-matrix FR13/FR14]
- FR15 AIDX identification of aircraft type/reg/flight/airline. [ASSERTION: Turnwise shows fields via AODB/ADS-B; AIDX connector not named — coverage-matrix FR15]
- FR16 correlation with AODB flight info. [GROUNDED: Turnwise AODB integration — coverage-matrix FR16]

### GSE, personnel, and zones (FR17–FR23)

- FR17 camera-based GSE type classification (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, tractors, golf carts). [GAP — disqualifying — coverage-matrix FR17; see Section 03]
- FR18 GSE ready/arrival/departure timestamps per type. [ASSERTION: Turnwise GSE movement timestamps via telematics — coverage-matrix FR18]
- FR19 equipment presence on stand. [GROUNDED: Turnwise stand + GSE tracking — coverage-matrix FR19]
- FR20 personnel presence in apron zones (excluding passengers). [GAP — disqualifying — coverage-matrix FR20; see Section 03]
- FR21 personnel entering restricted zones. [GAP — manageable — coverage-matrix FR21; depends on FR20]
- FR22 unsafe dwell times in high-risk areas. [ASSERTION: UTAM Edge Vision Controller derives dwell times — coverage-matrix FR22]
- FR23 PPE detection where camera quality allows. [GAP — manageable — coverage-matrix FR23; see Section 03]

### Turnaround activities and sequencing (FR24–FR32)

- FR24 auto-detect start/end of chocking, aerobridge dock/undock, stair position/removal, GPU connect/disconnect, baggage load/unload, catering, refuelling on bay, pushback readiness, cabin cleaning. [ASSERTION: Turnwise turnaround Gantt shows activities with start/end; camera-AI auto-detection of each listed activity to be confirmed — coverage-matrix FR24]
- FR25 sequence activities into a single turnaround timeline. [GROUNDED: Turnwise turnaround Gantt + CDM milestones — coverage-matrix FR25]
- FR26 per-event confidence scores. [GAP — coverage-matrix FR26]
- FR27 manual validation/correction. [GAP — coverage-matrix FR27]
- FR28 learn from corrections. [ASSERTION: UTAM AI/ML platform implies; no specific feature shown — coverage-matrix FR28]
- FR29 airline-specific, movement-type turnaround workflows (Originator/Turnaround/Terminator I/D). [ASSERTION: Turnwise airline management + turnaround workflows — coverage-matrix FR29]
- FR30 aircraft-type-specific turnaround sequences. [ASSERTION: platform configurable; not explicitly evidenced — coverage-matrix FR30]
- FR31 mandatory vs optional activities. [ASSERTION: workflow engine supports — coverage-matrix FR31]
- FR32 dependencies & precedence rules. [ASSERTION: UTAM Workflow Engine — coverage-matrix FR32]

### Planned vs actual, alerts, dashboards, reporting, integration, administration (FR33–FR73)

These rows are covered in Section 03. Grounded subset: FR33, FR34, FR35, FR36, FR37, FR40, FR41, FR45, FR46, FR47, FR49, FR52, FR53, FR55, FR58, FR59, FR60, FR61, FR62, FR63, FR64, FR65, FR66, FR67. Assertable subset: FR38, FR42, FR43, FR44, FR48, FR50, FR51, FR54, FR56, FR57, FR68, FR70, FR71, FR73. Gaps: FR39, FR69, FR72. [GROUNDED/ASSERTION/GAP — coverage-matrix FR33–FR73]

## Deliverables

The following deliverables map to PMR-06 (project documentation) and PMR-06a/06b/06c/06d:

| # | Deliverable | RFP ref | Evidence |
|---|-------------|--------|----------|
| D1 | Project Management Plan (PM plan, stakeholders, risk analysis, schedule) | PMR-02a, PMR-06 | [ASSERTION: standard PM deliverable — coverage-matrix PMR-02a/06] |
| D2 | Detailed Design Document with full FR traceability | PMR-02b, PMR-06a | [ASSERTION: UTAM detailed-design approach — coverage-matrix PMR-02b/06a] |
| D3 | Built/configured platform across DEV/TST/PROD per design | PMR-02c | [GROUNDED: UTAM IaC env parity — coverage-matrix PMR-02c] |
| D4 | Comprehensive Test Plan with requirement traceability | PMR-02d, PMR-06b | [ASSERTION: UTAM automated testing pyramid; methodology doc not provided — coverage-matrix PMR-02d/06b] |
| D5 | Implementation/Migration Plan with roles, validation, rollback | PMR-02e, PMR-06c | [GROUNDED: UTAM implementation plan + rollback — coverage-matrix PMR-02e/06c] |
| D6 | As-built documentation reflecting final solution | PMR-02f, PMR-06d | [ASSERTION: standard — coverage-matrix PMR-02f/06d] |
| D7 | End-user training in Test environment with cheat sheets | PMR-07 | [ASSERTION: UTAM training commitment generic — coverage-matrix PMR-07] |
| D8 | Technical training for BAC personnel (architecture, fault-finding, config) | PMR-08 | [ASSERTION: UTAM training commitment generic — coverage-matrix PMR-08] |
| D9 | Practical completion package (cutover + tests + docs + training) | PMR-09 | [ASSERTION: contractual; not in collateral — coverage-matrix PMR-09] |
| D10 | 6-month defects liability + maintenance agreement | PMR-10 | [GAP — coverage-matrix PMR-10; accepted contractual term] |
| D11 | AIDX connector via API Gateway | FR15, FR43, FR54 | [ASSERTION: AIDX publication via API Gateway — coverage-matrix FR43/FR54] |
| D12 | FR17 GSE-type CV classifier with per-class acceptance criteria | FR17 | [GAP — committed delivery — coverage-matrix FR17; see Section 03] |
| D13 | FR20 personnel-presence CV model with acceptance criteria | FR20, FR21, FR23 | [GAP — committed delivery — coverage-matrix FR20; see Section 03] |
| D14 | FR26/27/28/69 AI-governance pack (confidence scores, validation UI, learning loop, per-model accuracy) | FR26, FR27, FR28, FR69 | [GAP/ASSERTION — committed delivery — coverage-matrix] |
| D15 | Support SLA matrix (Sev-1 ≤1h 24×7×365) priced in Schedule E | NF19, NF20, NF17 | [GAP — committed matrix — see Section 10] |
| D16 | Australian hosting commitment (AWS Sydney ap-southeast-2 or BAC private cloud) with address | ISRA-19, ISRA-25 | [GAP — reconciled via commitment — see Section 08] |
| D17 | BAC ISRA completed | NF01, ISRA 1–29 | [ASSERTION: ISRA tab provided for completion; UTAM security architecture supports — coverage-matrix NF01] |
| D18 | Customised quick-reference guides (state if extra cost) | NF26 | [GAP — coverage-matrix NF26] |
| D19 | Help & knowledge artefacts, field-level help | NF18, NF23 | [GAP — coverage-matrix NF18/NF23] |
| D20 | 3-year availability history | NF05 | [GAP — coverage-matrix NF05; commit to SLA reporting going forward] |

## Out of scope

- Fabricated team bios, referees, case studies, pricing values, and certifications are not in scope of this draft. All such content is marked `[GAP] / placeholder` and must be supplied before submission. [GAP: Schedule C referees; Schedule E pricing — brief.md Evidence Map]
- Phase-2 items FR72 (aerobridge pax counting; airline data integration) are committed as a roadmap deliverable rather than a Phase-1 deliverable. [GAP: FR72 — coverage-matrix FR72]

> The methodology by which these deliverables are produced is described in Section 05.