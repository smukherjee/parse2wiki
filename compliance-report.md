# Compliance Report — BAC Underwing Analytics vs WAISL Turnwise

**Run date:** 2026-07-01
**Validator:** /compliance-validator (auto)
**Inputs:**
- `sources/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md` — 73 Functional Requirements (69 Must Have, 2 Should, 1 Could) + 48 Non-Functional + 12 PMR + 30 ISRA
- `sources/Turnwise Product Document 1.pdf.md` — 23 product modules for WAISL Turnaround Management ("Turnwise")

---

## Executive Summary

**BLOCKING: 49 of 73 Functional Requirements are NOT met by Turnwise out-of-the-box (67%).** The two products solve different problems:

- **BAC RFP (Underwing Analytics)** — fixed-camera based AI/ML **computer vision** platform that detects aircraft, GSE, personnel, PPE, and turnaround activities **from video**, with on-block/off-block auto-detection, AIDX integration, video buffering, occlusion detection, and continuous model retraining.
- **WAISL Turnwise** — **aviation data integration + visualization** product that ingests flight/GSE data from external sources (AODB, sensors, airlines) and displays it on dashboards. It does **no on-board computer vision**, **no camera ingestion**, and **no AI-based activity detection**.

Turnwise can be a strong **adjacent / complementary** product, but on its own it does not satisfy the BAC Underwing Analytics RFP. The product reads as a different domain (passenger/operational dashboards) layered over the same airport, not a vision system.

**Headline counts:**

| Category | Total | Met | Partial | Gap | Conform % |
|---|---:|---:|---:|---:|---:|
| FR — Video Capture & Camera Mgmt (FR01–FR04) | 4 | 0 | 0 | 4 | 0% |
| FR — Video Stream Mgmt (FR05–FR08) | 4 | 0 | 0 | 4 | 0% |
| FR — Camera Health & Diagnostics (FR09–FR12) | 4 | 0 | 0 | 4 | 0% |
| FR — Aircraft ID & Positioning (FR13–FR16) | 4 | 1 | 1 | 2 | 38% |
| FR — GSE Detection (FR17–FR19) | 3 | 0 | 1 | 2 | 17% |
| FR — Personnel Detection & Safety (FR20–FR23) | 4 | 0 | 0 | 4 | 0% |
| FR — Turnaround Activity Detection (FR24–FR25) | 2 | 0 | 1 | 1 | 50% |
| FR — Confidence & Validation (FR26–FR28) | 3 | 0 | 0 | 3 | 0% |
| FR — Turnaround Workflow & Business Logic (FR29–FR32) | 4 | 0 | 1 | 3 | 25% |
| FR — Schedule vs Actual Tracking (FR33–FR39) | 7 | 2 | 2 | 3 | 43% |
| FR — Real-Time Alerts (FR40–FR44) | 5 | 1 | 1 | 3 | 40% |
| FR — Dashboards & Visualisations (FR45–FR48) | 4 | 0 | 1 | 3 | 25% |
| FR — Analytics & Insights (FR49–FR53) | 5 | 1 | 1 | 3 | 30% |
| FR — Integration & Data Mgmt (FR54–FR56) | 3 | 0 | 1 | 2 | 17% |
| FR — Data Storage & Retention (FR57–FR59) | 3 | 0 | 2 | 1 | 33% |
| FR — User & Role Management (FR60–FR67) | 8 | 1 | 3 | 4 | 31% |
| FR — AI Governance & Operations (FR68–FR71) | 4 | 0 | 0 | 4 | 0% |
| FR — Phase 2 (FR72–FR73) | 2 | 0 | 0 | 2 | 0% |
| **TOTAL FUNCTIONAL** | **73** | **6** | **15** | **52** | **19%** |

**Pre-flight status: NOT COMPLIANT — DO NOT ASSEMBLE.** 52 Functional Requirements have no Turnwise coverage. Recommend escalating to WAISL Bid Manager: either (a) confirm a CV/ML partner is in scope (the Response Sheet's Sheet1 row already names "kloudspot" as the joint WAISL+Vendor owner of the Functional Req line), (b) re-scope RFP, or (c) submit Turnwise as complementary product with explicit gap disclosure.

---

## Per-Requirement Validation

Legend: ✅ Pass | ⚠️ Partial | ❌ Fail

### FR01–FR04 Video Capture & Camera Management

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR01 | Onboard fixed cameras (BAC-supported models) | Must | No camera ingestion in Turnwise; tracking is via external feeds (AODB/IoT) | ❌ |
| FR02 | Group cameras by airport/terminal/gate/stand/airline/handler | Must | No camera entity; Turnwise has "Airline Management" + "GHA Management" + geofence areas, but these are operational entities, not camera groupings | ❌ |
| FR03 | Configure camera FOV and aircraft parking zones | Must | Not in Turnwise scope (no cameras) | ❌ |
| FR04 | Geofenced operational zones (safety envelope, equipment staging, personnel walk) | Must | Turnwise has "Airport Geofence" (lists configured geofence areas) and "Restricted Zone Monitoring" — partially aligned but no aircraft safety envelope, equipment staging, or personnel walk zone taxonomy | ❌ |

**Block:** 4/4 Must-Have failures. No camera, no FOV, no parking zone concept.

### FR05–FR08 Video Stream Management

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR05 | Ingest live video streams | Must | Not in scope | ❌ |
| FR06 | Video buffering for network interruptions | Should | Not in scope | ❌ |
| FR07 | Configurable frame rates and resolutions per camera | Must | Not in scope | ❌ |
| FR08 | Timestamp video frames using synchronised airport time | Must | Not in scope | ❌ |

**Block:** 4/4 failures. Turnwise is not a video platform.

### FR09–FR12 Camera Health & Diagnostics

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR09 | Continuously monitor camera availability/signal quality; notify vendor on stream issues | Must | "Monitoring Dashboard helps users monitor data synchronization between source data providers and application" — covers data sync, not camera health; no vendor notification on stream failure | ⚠️ |
| FR10 | Detect camera occlusion, lens obstruction, glare | Must | Not in scope | ❌ |
| FR11 | Generate alerts for camera degradation impacting AI accuracy | Must | Not in scope (no AI accuracy) | ❌ |
| FR12 | Camera health dashboard | Could | No camera health dashboard | ❌ |

**Block:** 3/3 Must-Have failures.

### FR13–FR16 Aircraft Identification & Positioning

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR13 | Detect aircraft arrival at stand and confirm on-block time | Must | Turnwise does NOT auto-detect on-block from video; "Flight Summary and POBT calculates the off block time" — this is computed from inbound data, not detected from a camera. On-block requires BAC AODB IRR/BRR data, not vision. | ❌ |
| FR14 | Detect aircraft departure and confirm off-block time | Must | Computed POBT only, not auto-detected from stand | ❌ |
| FR15 | Use AIDX to identify aircraft type/registration/flight number/airline | Must | Turnwise ingests flight information and displays "airline logos" via Airline Management; AIDX consumption not explicit | ⚠️ |
| FR16 | Correlate aircraft presence with flight information from AODB | Must | Turnwise ingests from AODB and shows "arriving to and departing from designated airport" flights | ✅ |

**Block:** 2/4 Must-Have failures. On/off-block MUST be auto-detected per RFP ("detect" language). Turnwise is data-feed derived only.

### FR17–FR19 GSE Detection

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR17 | Detect and classify 10 GSE types (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, support vehicles) | Must | Turnwise has "GSE Master report" + "GSE Usage Master Report" + "Vehicle Last Location Report" + "Speed Violation Report" — tracks GSE movement from telematics, NOT vision-based detection or classification. Cannot distinguish loader vs tug. | ❌ |
| FR18 | Detect equipment ready, arrival, departure timestamps per GSE type | Must | Not from vision; derived from external telemetry only | ❌ |
| FR19 | Track equipment presence on the stand | Must | Vehicle tracking by geofence provides stand presence approximation; not vision-confirmed | ⚠️ |

**Block:** 2/3 Must-Have failures. GSE detection is the core competency the RFP demands, and Turnwise cannot do it from video.

### FR20–FR23 Personnel Detection & Safety Monitoring

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR20 | Detect personnel presence within apron zones (excluding PAX) | Must | Not in scope (no personnel CV) | ❌ |
| FR21 | Detect personnel entering restricted zones | Must | "Airside Safety and Restricted Zone Monitoring" + speed violation alerts — covers vehicle violations, not personnel entry | ❌ |
| FR22 | Identify unsafe dwell times in high-risk areas (PAX) | Must | Not in scope | ❌ |
| FR23 | PPE detection where camera quality allows | Must | Not in scope (no PPE model) | ❌ |

**Block:** 4/4 Must-Have failures.

### FR24–FR25 Turnaround Activity Detection

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR24 | Auto-detect 13 turnaround activities (chocking, aerobridge, stairs, GPU, baggage U/L, catering, refuelling, pushback readiness, cabin cleaning) | Must | Turnwise has "Critical Activity Tracking" and "Turnaround Time Monitoring" but tracks via external milestones/data, not auto-detect from video. "Critical Activity Tracking — Teams can instantly see what is completed, what is pending, and what needs attention now" — sourced from external signals. | ❌ |
| FR25 | Sequence activities into a single turnaround timeline | Must | "Turnaround SLA Report indicates if the turnaround is delayed/on time/early" + "Turnaround Time Monitoring" implies a timeline view; sequence construction depends on input signals | ⚠️ |

**Block:** 1/2 Must-Have failures. FR24's auto-detection from video is the deal-breaker.

### FR26–FR28 Confidence & Validation

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR26 | Assign confidence scores to all detected events by stand | Must | No confidence scoring (no detections) | ❌ |
| FR27 | Manual validation or correction of detected timestamps | Must | Turnwise "Playback" supports replay; not explicit on timestamp validation UI | ⚠️ |
| FR28 | Learn from corrections/adjustments to improve accuracy | Must | Not in scope (no model learning) | ❌ |

**Block:** 2/3 Must-Have failures.

### FR29–FR32 Turnaround Workflow & Business Logic

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR29 | Airline-specific, Movement-Type turnaround workflows (Originator-Terminator I/D) | Must | "Airline Management" + "Flight Summary" suggest airline-specific handling; Movement-Type not specified | ⚠️ |
| FR30 | Aircraft-type-specific turnaround sequences | Must | Not in scope | ❌ |
| FR31 | Define mandatory vs optional activities | Must | Not specified | ❌ |
| FR32 | Dependencies and precedence rules between activities | Must | Not specified | ❌ |

**Block:** 3/4 Must-Have failures.

### FR33–FR39 Schedule vs Actual Tracking

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR33 | Ingest planned and estimated times from AODB/airline systems | Must | "Flight Summary and POBT" ingests scheduled flights; AODB consumption implied | ✅ |
| FR34 | Compare planned vs actual activity timestamps | Must | "Turnaround SLA Report" + "Flight wise OTP Report" + "Airline Wise OTP Report" do this | ✅ |
| FR35 | Calculate delay attribution per activity | Must | "Calculate delay attribution" — not explicit in Turnwise; only aggregate delay | ❌ |
| FR36 | Configurable tolerance thresholds | Must | SLA thresholds mentioned ("Turnaround SLA alert is raised when actual turnaround time exceeds set threshold") but not explicit per activity | ⚠️ |
| FR37 | Detect deviations from defined workflows | Must | "Turnaround SLA Report" + critical activity tracking surfaces deviation in time, not in workflow conformance | ⚠️ |
| FR38 | Flag root causes for missed SLAs | Must | Not in scope | ❌ |
| FR39 | Exception annotations by operational staff | Should | Not specified | ❌ |

**Block:** 3/7 Must-Have failures.

### FR40–FR44 Real-Time Alerts & Operational Response

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR40 | Configurable alerts when activities exceed planned duration | Must | "Turnaround SLA alert is raised when actual turnaround time exceeds set threshold" — exists | ✅ |
| FR41 | Configurable alerts for unsafe or prohibited activity | Must | Speed violation alert exists; unsafe/prohibited activity not covered | ⚠️ |
| FR42 | Alerts for camera or AI confidence degradation | Must | Not in scope (no camera/AI) | ❌ |
| FR43 | Alerts via dashboard, email, API (AIDX) | Must | Dashboard ✓; Email and AIDX not explicit | ❌ |
| FR44 | Alerts include context, severity, recommended actions | Must | Severity implied; context + recommended action not specified | ❌ |

**Block:** 3/5 Must-Have failures.

### FR45–FR48 Dashboards & Visualisations

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR45 | Live turnaround status board per gate | Must | "Dashboard-KPI and Slot Performance" + "Monitoring Dashboard" are airport-wide, not per-gate turnarounds | ❌ |
| FR46 | Visualise current activity state and next expected milestone | Must | "Critical Activity Tracking" suggests current state; next milestone not explicit | ⚠️ |
| FR47 | Colour-coded delay indicators | Must | Not specified; standard in dashboards but not confirmed | ❌ |
| FR48 | Live and historical video playback per event | Should | "Playback" exists (replay past movement) but not video playback per event — no video source | ❌ |

**Block:** 3/4 Must-Have failures.

### FR49–FR53 Analytics & Insights Dashboard

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR49 | Turnaround KPIs by Airline / Aircraft type / Gate / Service provider | Must | Airline, gate covered; aircraft type and service provider not explicit | ⚠️ |
| FR50 | Trend and variance analysis | Must | Not specified | ❌ |
| FR51 | AI-driven improvement insights | Must | Not in scope (no AI) | ❌ |
| FR52 | Ad-hoc queries and filters | Must | "report can be filtered and viewed by airline" — limited ad-hoc | ⚠️ |
| FR53 | Historical analysis | Must | Operational reports support this | ✅ |

**Block:** 2/5 Must-Have failures.

### FR54–FR56 Integration & Data Management

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR54 | Integrate with AODB, FIDS, A-CDM (AIDX) | Must | "Systems Integration" — generic; AIDX explicit consumption not confirmed | ⚠️ |
| FR55 | REST and event-based APIs | Must | Not specified | ❌ |
| FR56 | Publish actual timestamps back to consuming systems | Must | Not specified | ❌ |

**Block:** 2/3 Must-Have failures.

### FR57–FR59 Data Storage & Retention

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR57 | Store event metadata separate from video data | Must | No video data in Turnwise; metadata storage implied | ⚠️ |
| FR58 | Configurable data retention policies | Must | Not specified | ❌ |
| FR59 | Forensic replay for incident investigation | Should | "Playback" exists; not forensic-grade | ⚠️ |

**Block:** 1/2 Must-Have failures.

### FR60–FR67 User & Role Management

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR60 | Role-based access control | Must | "User Management" module exists; RBAC implied | ✅ |
| FR61 | Airline- and service-provider-specific data segregation | Must | "Airline Management" + "GHA Management" exist but not explicit data segregation enforcement | ⚠️ |
| FR62 | Configurable permissions per role | Must | Not specified | ❌ |
| FR63 | Administrative tools for configuration management | Must | Not specified | ❌ |
| FR64 | Environment separation (Dev/Test/Prod) | Must | "Hybrid Deployment" — secure, scalable hybrid cloud; env separation not specified | ❌ |
| FR65 | Operational monitoring and health dashboards | Must | "Monitoring Dashboard" covers data sync; system health not explicit | ⚠️ |
| FR66 | Admin ability to configure alerts, reports, dashboard view, users | Must | Partially covered by User Management + Alert modules | ⚠️ |
| FR67 | BAC users — SSO; Non-BAC — local accounts; BAC defines password/MFA params | Must | SSO not specified; MFA not specified | ❌ |

**Block:** 4/8 Must-Have failures.

### FR68–FR71 AI Governance & Operations

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR68 | Versioned AI models | Must | No AI models | ❌ |
| FR69 | Track detection accuracy per model | Must | No detection | ❌ |
| FR70 | Airport-specific model tuning | Must | No models | ❌ |
| FR71 | Continual improvement / learning of models | Must | No models | ❌ |

**Block:** 4/4 Must-Have failures.

### FR72–FR73 Phase 2 (Future Requirements)

| ID | Requirement | MoSCoW | Turnwise Coverage | Status |
|---|---|---|---|---|
| FR72 | Airline data integration; Aerobridge camera for PAX counting / crew boarding | Must | "Airline Management" exists; aerobridge camera for PAX counting not in scope | ❌ |
| FR73 | Remote access via mobile and tablet devices | Must | "Hybrid Deployment" — secure, scalable; mobile not explicit | ❌ |

**Block:** 2/2 Must-Have failures.

---

## Functional Gaps Summary — Top 10 Critical

These are the gaps most likely to result in RFP disqualification:

1. **No computer vision platform** — Turnwise is data-integration / dashboard, not a CV/ML system. FR01–FR28 (28 requirements) demand vision-based detection of aircraft, GSE, personnel, PPE, activities.
2. **No camera ingestion / FOV / parking zones** — FR01–FR08.
3. **No on/off-block auto-detection from video** — FR13, FR14 specifically require "detect" and "confirm" from the stand. Turnwise only computes POBT from inbound data feeds.
4. **No GSE classification** — FR17 lists 10 specific GSE classes. Turnwise tracks vehicles but cannot classify loader vs tug vs water cart.
5. **No PPE detection** — FR23.
6. **No AI governance** — FR68–FR71 require model versioning, accuracy tracking, and continuous learning. Turnwise has no model layer.
7. **No event-metadata + video separation or retention** — FR57–FR59. No video in Turnwise.
8. **No BAC-specific SSO / password / MFA policies** — FR67.
9. **No video playback per event** — FR48.
10. **No AI-driven insights or activity-level delay attribution** — FR35, FR38, FR51.

---

## Cross-Document Findings

- **Naming overlap, not capability overlap**: Turnwise covers Turnaround Time Monitoring, GSE Tracking, Stand Tracking, CDM Milestone Tracking, Alerts, Dashboards, Airline Management, and Reports — eight BAC FR areas. But the BAC RFP asks for **vision-derived** turnaround, GSE, stand, and activity data. Turnwise derives all of this from external feeds, not from cameras. The product names line up; the underlying technical approach does not.
- **Hybrid Deployment (Turnwise §22)** satisfies the "secure, scalable" deployment expectation only superficially. NF04 (RPO/RTO) and NF06/NF07 (RTO ≤ 4 hrs) are not addressed in the product document and must come from the proposal narrative.
- **No mention of AIDX consumption in Turnwise** — FR15, FR54, FR56 require AIDX. This is a clear gap and must be confirmed in WAISL's integration roadmap.
- **Phase 2 (FR72) aerobridge camera for PAX counting** explicitly asks for camera-based PAX counting, which Turnwise does not do.
- **The Response Sheet's Sheet1 row "Functional Req — WAISL (and vendor kloudspot)"** signals that BAC already knows WAISL is partnering with a CV vendor. This validates the need for a kloudspot capability document to close the gaps above.

---

## Recommended Actions (Pre-Assembly)

1. **BLOCKING — Escalate to WAISL Bid Manager.** Confirm with the bid team whether Turnwise is being positioned as:
   - (a) The full Underwing Analytics solution — **NOT FEASIBLE** based on this review.
   - (b) A complementary data-integration / dashboard layer on top of a CV/ML partner (e.g. kloudspot per the Sheet1 row "WAISL (and vendor kloudspot)") — **FEASIBLE** if the partner covers FR01–FR28, FR57–FR59, FR68–FR71.
   - (c) An alternate proposal — clarify with Leighton Walker (BAC) before submission.
2. **Obtain kloudspot CV/ML capability deck.** Re-run this validation against the combined solution.
3. **Disclose gaps explicitly in the Supplier Response Sheet** (Conformance column: "Partial — Turnwise covers X, Y, Z; partner covers A, B, C; out of scope: D, E, F"). BAC is explicit that 69 of 73 FRs are Must-Have; silent gap-failures are disqualifying.
4. **Fill the NFR / PMR / ISRA sheets** which are not in scope of this Turnwise-vs-FR comparison but are part of the response pack.
5. **Re-validate** after kloudspot or another CV partner is confirmed.

---

## Pre-flight Status

**NOT COMPLIANT — 52 Functional Requirements unmet (71%).** Proposal assembly should be paused until the CV/ML partner is confirmed and the combined capability is re-validated. If WAISL intends to submit Turnwise alone, escalate to Leighton Walker (BAC Key Contact, [Leighton.Walker@bne.com.au](mailto:Leighton.Walker@bne.com.au)) for an explicit scope conversation before 2026-07-10 (Response Due Date).
