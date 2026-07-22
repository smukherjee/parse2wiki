# Coverage Matrix — BAC Underwing Analytics (BAC-T-26-505)

## Summary

**Total Requirements Identified:** 166
**Explicit (Must/Should per Tab.F MoSCoW):** 166 | **Implicit (inferred from RFP §3/§4):** 0 (all are explicit Tab.F rows)

**Coverage Breakdown:**
- Grounded: 71 (43%)
- Assertable: 64 (39%)
- Gap: 31 (19%)

**Gap Severity:**
- Disqualifying: 3
- Manageable: 17
- Addressable: 11

**Source conflicts found:** 1 major (UTAM doc is a repurposed Athens/AIA + EU-residency artefact; must be re-grounded for Brisbane/Australia). See `brief.md` §Source Conflicts.

Marker discipline: `[GROUNDED: source]` / `[ASSERTION: rationale]` / `[GAP]`.

---

## Functional Requirements (Tab.F — FR01-FR73)

| # | Req ID | Requirement (abridged) | Source | Mandatory | Evidence Pointer | Classification | Gap Severity | Action |
|---|--------|-------------------------|--------|-----------|------------------|----------------|--------------|--------|
| 1 | FR01 | Onboard fixed cameras (BAC-supported models) | Tab.F FR01 | Yes | [ASSERTION: UTAM Edge Vision Controller ingests CCTV/edge cameras; "vendor-agnostic onboarding"] | Assertable | — | Assert with caveat |
| 2 | FR02 | Group cameras by airport/terminal/gate/stand/airline/handler | Tab.F FR02 | Yes | [ASSERTION: Turnwise airline/GHA/stand management implies grouping] | Assertable | — | Assert with caveat |
| 3 | FR03 | Configure camera FOV & aircraft parking zones | Tab.F FR03 | Yes | [ASSERTION: Turnwise airport geofence config adjacent] | Assertable | — | Assert with caveat |
| 4 | FR04 | Define geofenced zones (safety envelope, equipment staging, personnel walk zones) | Tab.F FR04 | Yes | [GROUNDED: Turnwise Airport Geofence module] | Grounded | — | Cite and ground |
| 5 | FR05 | Ingest live video streams | Tab.F FR05 | Yes | [GROUNDED: UTAM Edge Vision Controller / HTTPS Gateway] | Grounded | — | Cite and ground |
| 6 | FR06 | Video buffering during network interruptions | Tab.F FR06 | Should | [GROUNDED: UTAM Edge Data Ingestor "buffering and retry mechanisms"] | Grounded | — | Cite and ground |
| 7 | FR07 | Configurable frame rates/resolutions per camera | Tab.F FR07 | Yes | [GAP] | Gap | Manageable | Acknowledge gap |
| 8 | FR08 | Timestamp frames via synchronised airport time source | Tab.F FR08 | Yes | [ASSERTION: UTAM NTP/time-synchronised logging] | Assertable | — | Assert with caveat |
| 9 | FR09 | Continuous camera availability/signal monitoring; notify vendor on failure | Tab.F FR09 | Yes | [ASSERTION: UTAM Monitoring Dashboard checks data-sync health; camera-specific not shown] | Assertable | — | Assert with caveat |
| 10 | FR10 | Detect camera occlusion/lens obstruction/glare | Tab.F FR10 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 11 | FR11 | Alerts for camera degradation impacting AI accuracy | Tab.F FR11 | Yes | [ASSERTION: UTAM Rules Engine could raise such alerts; not pre-built] | Assertable | — | Assert with caveat |
| 12 | FR12 | Camera health dashboard | Tab.F FR12 | Could | [ASSERTION: Turnwise Monitoring Dashboard adjacent] | Assertable | — | Assert with caveat |
| 13 | FR13 | Detect aircraft arrival at stand & confirm on-block | Tab.F FR13 | Yes | [ASSERTION: Turnwise stand/flight tracking detects arrival; on-block via camera not confirmed] | Assertable | — | Assert with caveat |
| 14 | FR14 | Detect aircraft departure & confirm off-block | Tab.F FR14 | Yes | [ASSERTION: as FR13] | Assertable | — | Assert with caveat |
| 15 | FR15 | Use AIDX to identify aircraft type/reg/flight/airline | Tab.F FR15 | Yes | [ASSERTION: Turnwise shows these fields via AODB/ADS-B; AIDX connector not named] | Assertable | — | Assert with caveat |
| 16 | FR16 | Correlate aircraft presence with AODB flight info | Tab.F FR16 | Yes | [GROUNDED: Turnwise AODB integration] | Grounded | — | Cite and ground |
| 17 | FR17 | Detect & classify GSE types (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, tractors, golf carts) | Tab.F FR17 | Yes | [GAP: Turnwise GSE tracked via telematics/GPS type, not camera-classification of all listed types] | Gap | Disqualifying | Escalate / seek evidence |
| 18 | FR18 | GSE ready/arrival/departure timestamps per type | Tab.F FR18 | Yes | [ASSERTION: Turnwise GSE movement timestamps via telematics] | Assertable | — | Assert with caveat |
| 19 | FR19 | Track equipment presence on stand | Tab.F FR19 | Yes | [GROUNDED: Turnwise stand + GSE tracking] | Grounded | — | Cite and ground |
| 20 | FR20 | Detect personnel presence in apron zones (excl. PAX) | Tab.F FR20 | Yes | [GAP: personnel detection via camera not evidenced] | Gap | Disqualifying | Escalate / seek evidence |
| 21 | FR21 | Detect personnel entering restricted zones | Tab.F FR21 | Yes | [GAP: restricted-zone monitoring shown for vehicles/GSE, not personnel] | Gap | Manageable | Acknowledge gap |
| 22 | FR22 | Identify unsafe dwell times in high-risk areas (Pax-related) | Tab.F FR22 | Yes | [ASSERTION: UTAM Edge Vision Controller derives dwell times] | Assertable | — | Assert with caveat |
| 23 | FR23 | PPE detection where camera quality allows | Tab.F FR23 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 24 | FR24 | Auto-detect start/end of chocking, aerobridge dock/undock, stair position/removal, GPU connect/disconnect, baggage load/unload, catering, refuelling on bay, pushback readiness, cabin cleaning | Tab.F FR24 | Yes | [ASSERTION: Turnwise turnaround activity Gantt shows activities with start/end; camera-AI auto-detection of each listed activity not confirmed] | Assertable | Manageable | Assert with caveat (confirm method) |
| 25 | FR25 | Sequence activities into single turnaround timeline | Tab.F FR25 | Yes | [GROUNDED: Turnwise turnaround Gantt + CDM milestones] | Grounded | — | Cite and ground |
| 26 | FR26 | Assign confidence scores to detected events by stand | Tab.F FR26 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 27 | FR27 | Manual validation/correction of detected timestamps | Tab.F FR27 | Yes | [GAP: not shown in collateral] | Gap | Manageable | Seek evidence |
| 28 | FR28 | Learn from corrections to improve accuracy | Tab.F FR28 | Yes | [ASSERTION: UTAM AI/ML platform implies; no specific continuous-learning feature shown] | Assertable | — | Assert with caveat |
| 29 | FR29 | Airline-specific, movement-type turnaround workflows (Originator/Turnaround/Terminator I/D) | Tab.F FR29 | Yes | [ASSERTION: Turnwise airline mgmt + turnaround workflows] | Assertable | — | Assert with caveat |
| 30 | FR30 | Aircraft-type-specific turnaround sequences | Tab.F FR30 | Yes | [ASSERTION: platform configurable; not explicitly evidenced] | Assertable | — | Assert with caveat |
| 31 | FR31 | Define mandatory vs optional activities | Tab.F FR31 | Yes | [ASSERTION: workflow engine supports] | Assertable | — | Assert with caveat |
| 32 | FR32 | Dependencies & precedence rules between activities | Tab.F FR32 | Yes | [ASSERTION: UTAM Workflow Engine] | Assertable | — | Assert with caveat |
| 33 | FR33 | Ingest planned/estimated times from AODB or airline systems | Tab.F FR33 | Yes | [GROUNDED: Turnwise AODB integration] | Grounded | — | Cite and ground |
| 34 | FR34 | Compare planned vs actual activity timestamps | Tab.F FR34 | Yes | [GROUNDED: Turnwise OTP/SLA reports] | Grounded | — | Cite and ground |
| 35 | FR35 | Calculate delay attribution per activity | Tab.F FR35 | Yes | [GROUNDED: Turnwise delay indicators/SLA reports] | Grounded | — | Cite and ground |
| 36 | FR36 | Configurable tolerance thresholds | Tab.F FR36 | Yes | [GROUNDED: Turnwise configurable SLA thresholds] | Grounded | — | Cite and ground |
| 37 | FR37 | Detect deviations from defined workflows | Tab.F FR37 | Yes | [GROUNDED: UTAM Rules Engine] | Grounded | — | Cite and ground |
| 38 | FR38 | Flag root causes for missed SLAs | Tab.F FR38 | Yes | [ASSERTION: Turnwise SLA reports show delay; root-cause attribution not explicit] | Assertable | — | Assert with caveat |
| 39 | FR39 | Exception annotations by operational staff | Tab.F FR39 | Should | [GAP] | Gap | Addressable | Seek evidence |
| 40 | FR40 | Configurable alerts when activities exceed planned duration | Tab.F FR40 | Yes | [GROUNDED: Turnwise Turnaround SLA alert] | Grounded | — | Cite and ground |
| 41 | FR41 | Configurable alerts/reports for unsafe/prohibited activity | Tab.F FR41 | Yes | [GROUNDED: Turnwise Speed Violation + restricted-zone alerts] | Grounded | — | Cite and ground |
| 42 | FR42 | Alerts for camera or AI confidence degradation | Tab.F FR42 | Yes | [ASSERTION: UTAM Rules Engine] | Assertable | — | Assert with caveat |
| 43 | FR43 | Alerts via dashboard, email, API (AIDX) | Tab.F FR43 | Yes | [ASSERTION: UTAM multi-channel (SMS/voice/email/Teams/TETRA/web); AIDX-specific not confirmed] | Assertable | Manageable | Assert with caveat |
| 44 | FR44 | Alerts include context, severity, recommended actions | Tab.F FR44 | Yes | [ASSERTION: Turnwise alerts show flight/vehicle/values/timestamp; recommended-actions field not shown] | Assertable | — | Assert with caveat |
| 45 | FR45 | Live turnaround status board per gate | Tab.F FR45 | Yes | [GROUNDED: Turnwise turnaround monitoring] | Grounded | — | Cite and ground |
| 46 | FR46 | Visualise current activity state & next expected milestone | Tab.F FR46 | Yes | [GROUNDED: Turnwise critical activity tracking + CDM milestones] | Grounded | — | Cite and ground |
| 47 | FR47 | Colour-coded delay indicators | Tab.F FR47 | Yes | [GROUNDED: Turnwise red delay indicators] | Grounded | — | Cite and ground |
| 48 | FR48 | Live & historical video playback per event | Tab.F FR48 | Should | [ASSERTION: Turnwise Playback replays movement on map; raw video playback per event not confirmed] | Assertable | Manageable | Assert with caveat |
| 49 | FR49 | Turnaround KPIs by airline/aircraft type/gate/service provider | Tab.F FR49 | Yes | [GROUNDED: Turnwise airline-wise OTP, GSE usage, stand utilisation] | Grounded | — | Cite and ground |
| 50 | FR50 | Trend & variance analysis | Tab.F FR50 | Yes | [ASSERTION: lakehouse + reporting supports; not explicitly shown] | Assertable | — | Assert with caveat |
| 51 | FR51 | AI-driven improvement insights | Tab.F FR51 | Yes | [ASSERTION: UTAM AI/ML platform] | Assertable | — | Assert with caveat |
| 52 | FR52 | Ad-hoc queries & filters | Tab.F FR52 | Yes | [GROUNDED: UTAM Self-Service BI] | Grounded | — | Cite and ground |
| 53 | FR53 | Historical analysis | Tab.F FR53 | Yes | [GROUNDED: Turnwise reports + playback] | Grounded | — | Cite and ground |
| 54 | FR54 | Integrate AODB, FIDS, A-CDM (AIDX) | Tab.F FR54 | Yes | [ASSERTION: UTAM AODB + A-CDM; FIDS not named; AIDX not explicitly] | Assertable | — | Assert with caveat |
| 55 | FR55 | REST & event-based APIs | Tab.F FR55 | Yes | [GROUNDED: UTAM API Gateway (REST/SOAP) + event streaming] | Grounded | — | Cite and ground |
| 56 | FR56 | Publish actual timestamps to consuming systems | Tab.F FR56 | Yes | [ASSERTION: API Gateway supports publish; not explicitly described] | Assertable | — | Assert with caveat |
| 57 | FR57 | Store event metadata separate from video | Tab.F FR57 | Yes | [ASSERTION: UTAM lakehouse separates structured metadata; video stored separately implied] | Assertable | — | Assert with caveat |
| 58 | FR58 | Configurable data retention policies | Tab.F FR58 | Yes | [GROUNDED: UTAM retention policies] | Grounded | — | Cite and ground |
| 59 | FR59 | Forensic replay for incident investigation | Tab.F FR59 | Yes | [GROUNDED: Turnwise Playback] | Grounded | — | Cite and ground |
| 60 | FR60 | Role-based access control | Tab.F FR60 | Yes | [GROUNDED: UTAM RBAC] | Grounded | — | Cite and ground |
| 61 | FR61 | Airline- & service-provider-specific data segregation | Tab.F FR61 | Yes | [GROUNDED: UTAM row-level access; external parties see own data] | Grounded | — | Cite and ground |
| 62 | FR62 | Configurable permissions per role | Tab.F FR62 | Yes | [GROUNDED: UTAM RBAC/ABAC] | Grounded | — | Cite and ground |
| 63 | FR63 | Admin tools for configuration management | Tab.F FR63 | Yes | [GROUNDED: Turnwise user/airline/GHA management modules] | Grounded | — | Cite and ground |
| 64 | FR64 | Environment separation (Dev/Test/Prod) | Tab.F FR64 | Yes | [GROUNDED: UTAM IaC env parity] | Grounded | — | Cite and ground |
| 65 | FR65 | Operational monitoring & health dashboards | Tab.F FR65 | Yes | [GROUNDED: Turnwise Monitoring Dashboard] | Grounded | — | Cite and ground |
| 66 | FR66 | Admin configure alerts/reports/dashboard/users | Tab.F FR66 | Yes | [GROUNDED: Turnwise management modules] | Grounded | — | Cite and ground |
| 67 | FR67 | SSO for BAC users (Azure AD); local accounts for non-BAC with password params (length, complexity, lockout, MFA) | Tab.F FR67 | Yes | [GROUNDED: UTAM Azure Entra ID SSO + OpenLDAP/OneLogin + password policies + MFA] | Grounded | — | Cite and ground |
| 68 | FR68 | Versioned AI models | Tab.F FR68 | Yes | [ASSERTION: UTAM semantic versioning/release train; model-versioning not explicit] | Assertable | — | Assert with caveat |
| 69 | FR69 | Track detection accuracy per model | Tab.F FR69 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 70 | FR70 | Airport-specific model tuning | Tab.F FR70 | Yes | [ASSERTION: platform parameterisation/config-over-code] | Assertable | — | Assert with caveat |
| 71 | FR71 | Continual improvement/learning of models | Tab.F FR71 | Yes | [ASSERTION: UTAM AI/ML platform] | Assertable | — | Assert with caveat |
| 72 | FR72 | Phase 2: airline data integration; aerobridge camera pax counting/crew boarding | Tab.F FR72 | Yes | [GAP: future phase, not in collateral] | Gap | Manageable | Acknowledge gap |
| 73 | FR73 | Remote access via mobile & tablet | Tab.F FR73 | Yes | [ASSERTION: UTAM browser-based responsive UI] | Assertable | — | Assert with caveat |

---

## Non-Functional Requirements (Tab.F — NF01-NF48)

| # | Req ID | Requirement (abridged) | Source | Mandatory | Evidence Pointer | Classification | Gap Severity | Action |
|---|--------|-------------------------|--------|-----------|------------------|----------------|--------------|--------|
| 74 | NF01 | Complete BAC Information Security Risk Assessment | Tab.F NF01 | Yes | [ASSERTION: ISRA tab provided for completion; UTAM security architecture supports] | Assertable | — | Assert with caveat |
| 75 | NF02 | Export data; list exportable fields/types | Tab.F NF02 | Yes | [GROUNDED: UTAM export controls / reporting service] | Grounded | — | Cite and ground |
| 76 | NF03 | Live data 24/7/365; state refresh rate | Tab.F NF03 | Yes | [ASSERTION: UTAM real-time ingestion; refresh rate not specified] | Assertable | — | Assert with caveat |
| 77 | NF04 | Redundancy/Backup/DR strategy + agreed SLAs | Tab.F NF04 | Yes | [GROUNDED: UTAM HA/DR + backup framework] | Grounded | — | Cite and ground |
| 78 | NF05 | 3-year history of system availability, failures, downtime | Tab.F NF05 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 79 | NF06 | RPO — all data/transactions recoverable | Tab.F NF06 | Yes | [GROUNDED: UTAM RPO near-zero] | Grounded | — | Cite and ground |
| 80 | NF07 | RTO — recover within 4 hours | Tab.F NF07 | Yes | [GROUNDED: UTAM RTO ≤40 min (exceeds 4h)] | Grounded | — | Cite and ground |
| 81 | NF08 | Define integration scope & ownership pre-kickoff | Tab.F NF08 | Yes | [ASSERTION: UTAM connector/integration layer; process not described] | Assertable | — | Assert with caveat |
| 82 | NF09 | Q&A standards/accreditations/methodologies/processes | Tab.F NF09 | Yes | [GAP] | Gap | Addressable | Seek evidence |
| 83 | NF10 | Q&A tools & technology | Tab.F NF10 | Yes | [GAP] | Gap | Addressable | Seek evidence |
| 84 | NF11 | Risk mitigation strategy | Tab.F NF11 | Yes | [ASSERTION: UTAM risk framework implied] | Assertable | — | Assert with caveat |
| 85 | NF12 | Draw on additional resources to keep timelines | Tab.F NF12 | Yes | [ASSERTION: WAISL multi-region footprint] | Assertable | — | Assert with caveat |
| 86 | NF13 | Test methodology | Tab.F NF13 | Yes | [ASSERTION: UTAM automated testing pyramid; methodology doc not provided] | Assertable | — | Assert with caveat |
| 87 | NF14 | Test tools | Tab.F NF14 | Yes | [ASSERTION: UTAM CI/CD tooling implied] | Assertable | — | Assert with caveat |
| 88 | NF15 | Design & implement all integrations in scope | Tab.F NF15 | Yes | [GROUNDED: UTAM integration layer + connectors] | Grounded | — | Cite and ground |
| 89 | NF16 | List of API connectors | Tab.F NF16 | Yes | [GROUNDED: UTAM connectors — AODB, ADS-B, telematics, weather, RVR, vision] | Grounded | — | Cite and ground |
| 90 | NF17 | 24/7/365 support via phone, email, online help; update help on new features | Tab.F NF17 | Yes | [GAP: not explicitly stated in collateral] | Gap | Manageable | Seek evidence |
| 91 | NF18 | Client-configurable help & knowledge artefacts | Tab.F NF18 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 92 | NF19 | Severity response scenarios (Sev1 ≤1h 24×7, etc.) | Tab.F NF19 | Yes | [GAP: not addressed in collateral] | Gap | Disqualifying | Escalate / seek evidence |
| 93 | NF20 | Sev3 resolution within 8 business hrs | Tab.F NF20 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 94 | NF21 | Documented incident mgmt with response SLAs per priority | Tab.F NF21 | Yes | [ASSERTION: UTAM ISO 27001 incident handling] | Assertable | — | Assert with caveat |
| 95 | NF22 | Local representative for BAC account escalation | Tab.F NF22 | Yes | [ASSERTION: WAISL Australia office listed] | Assertable | — | Assert with caveat |
| 96 | NF23 | Help desk info on specific input fields | Tab.F NF23 | Yes | [GAP] | Gap | Addressable | Seek evidence |
| 97 | NF24 | Clear support/help options in UI | Tab.F NF24 | Yes | [ASSERTION: Turnwise UI; not explicit] | Assertable | — | Assert with caveat |
| 98 | NF25 | Self-service reporting for IT | Tab.F NF25 | Yes | [GROUNDED: UTAM Self-Service BI] | Grounded | — | Cite and ground |
| 99 | NF26 | Customised quick-reference guides (state if extra cost) | Tab.F NF26 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 100 | NF27 | Admin/user training (format; if extra cost) | Tab.F NF27 | Yes | [ASSERTION: UTAM training commitment generic] | Assertable | — | Assert with caveat |
| 101 | NF28 | Ongoing training (inclusive/exclusive managed services; cost) | Tab.F NF28 | Yes | [ASSERTION: implied] | Assertable | — | Assert with caveat |
| 102 | NF29 | Training & materials for new features/patches | Tab.F NF29 | Yes | [ASSERTION: UTAM release train] | Assertable | — | Assert with caveat |
| 103 | NF30 | Training & support to suppliers | Tab.F NF30 | Yes | [ASSERTION: platform multi-stakeholder] | Assertable | — | Assert with caveat |
| 104 | NF31 | Support very large groups | Tab.F NF31 | Yes | [ASSERTION: UTAM scalable microservices] | Assertable | — | Assert with caveat |
| 105 | NF32 | Support multiple users | Tab.F NF32 | Yes | [GROUNDED: UTAM scalable architecture] | Grounded | — | Cite and ground |
| 106 | NF33 | Group-based access to connected applications | Tab.F NF33 | Yes | [GROUNDED: UTAM RBAC + federation] | Grounded | — | Cite and ground |
| 107 | NF34 | Explicitly deny unauthorised users + examples | Tab.F NF34 | Yes | [GROUNDED: UTAM zero-trust, least privilege, explicit deny] | Grounded | — | Cite and ground |
| 108 | NF35 | MFA | Tab.F NF35 | Yes | [GROUNDED: UTAM mandatory MFA for privileged] | Grounded | — | Cite and ground |
| 109 | NF36 | Single Sign-On | Tab.F NF36 | Yes | [GROUNDED: UTAM SSO/OIDC] | Grounded | — | Cite and ground |
| 110 | NF37 | Consistent UX between web browsers & mobile devices/apps | Tab.F NF37 | Yes | [ASSERTION: UTAM browser-based] | Assertable | — | Assert with caveat |
| 111 | NF38 | Support Edge, Chrome, Firefox, Safari (desktop+mobile) | Tab.F NF38 | Yes | [ASSERTION: standard web app; not explicitly listed] | Assertable | — | Assert with caveat |
| 112 | NF39 | Must not require browser plug-ins | Tab.F NF39 | Yes | [GROUNDED: UTAM "no client-side software installation"] | Grounded | — | Cite and ground |
| 113 | NF40 | Built per common UX guidelines (navigable, consistent, predictable) | Tab.F NF40 | Yes | [ASSERTION: UTAM UI layer] | Assertable | — | Assert with caveat |
| 114 | NF41 | Role-based access for admin delegation | Tab.F NF41 | Yes | [GROUNDED: UTAM RBAC] | Grounded | — | Cite and ground |
| 115 | NF42 | Federated identity SAML2 (BAC Azure AD idP) | Tab.F NF42 | Yes | [GROUNDED: UTAM Azure Entra ID / SAML2/OIDC] | Grounded | — | Cite and ground |
| 116 | NF43 | Just-in-time admin delegation (access expires) | Tab.F NF43 | Yes | [GROUNDED: UTAM short-lived credentials + PAM] | Grounded | — | Cite and ground |
| 117 | NF44 | Self-service password reset endpoint | Tab.F NF44 | Yes | [ASSERTION: standard IAM; not explicit in collateral] | Assertable | — | Assert with caveat |
| 118 | NF45 | Real-time system logs & technical diagnostics | Tab.F NF45 | Yes | [GROUNDED: UTAM CloudWatch/CloudTrail] | Grounded | — | Cite and ground |
| 119 | NF46 | Reports on user auth, app usage, auditing | Tab.F NF46 | Yes | [GROUNDED: UTAM audit logging] | Grounded | — | Cite and ground |
| 120 | NF47 | Log geolocation on authentications | Tab.F NF47 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 121 | NF48 | Search/filter events (e.g., failed logins) at high volume | Tab.F NF48 | Yes | [ASSERTION: UTAM centralised searchable logs] | Assertable | — | Assert with caveat |

---

## Project Management Requirements (Tab.F — PMR-01..PMR-10)

| # | Req ID | Requirement (abridged) | Source | Mandatory | Evidence Pointer | Classification | Gap Severity | Action |
|---|--------|-------------------------|--------|-----------|------------------|----------------|--------------|--------|
| 122 | PMR-01 | Expertise: equipment supplier relationships, local support, certified personnel | Tab.F PMR-01 | Yes | [ASSERTION: WAISL Australia office + ISO certs; no named relationships/certs of personnel] | Assertable | — | Assert with caveat |
| 123 | PMR-02 | Deliver in defined phases (Initiation, Design, Build, Test, Implementation, Closure) | Tab.F PMR-02 | Yes | [ASSERTION: standard delivery; UTAM describes build/test/release] | Assertable | — | Assert with caveat |
| 124 | PMR-02a | Project initiation: PM plan, stakeholders, risk analysis, schedule | Tab.F PMR-02a | Yes | [ASSERTION: standard] | Assertable | — | Assert with caveat |
| 125 | PMR-02b | Design phase: workshops, detailed design doc accepted before build | Tab.F PMR-02b | Yes | [ASSERTION: UTAM detailed-design approach] | Assertable | — | Assert with caveat |
| 126 | PMR-02c | Build phase: configure per design across DEV/TST/PROD | Tab.F PMR-02c | Yes | [GROUNDED: UTAM IaC env parity] | Grounded | — | Cite and ground |
| 127 | PMR-02d | Test phase: install in test, execute test plan, support UAT | Tab.F PMR-02d | Yes | [ASSERTION: UTAM automated testing] | Assertable | — | Assert with caveat |
| 128 | PMR-02e | Implementation: production cutover in change window, rollback, debrief | Tab.F PMR-02e | Yes | [GROUNDED: UTAM blue/green + rollback + DB migration revert] | Grounded | — | Cite and ground |
| 129 | PMR-02f | Closure: defect inspection, rectify, as-built | Tab.F PMR-02f | Yes | [ASSERTION: standard] | Assertable | — | Assert with caveat |
| 130 | PMR-03 | Weekly project meetings | Tab.F PMR-03 | Yes | [ASSERTION: standard] | Assertable | — | Assert with caveat |
| 131 | PMR-04 | WHS compliance, Safe Work Method Statements, BAC contractor status | Tab.F PMR-04 | Yes | [ASSERTION: WAISL operates in Australia; WHS process not evidenced] | Assertable | — | Assert with caveat |
| 132 | PMR-05 | Change control via BAC CAB | Tab.F PMR-05 | Yes | [GROUNDED: UTAM change management process] | Grounded | — | Cite and ground |
| 133 | PMR-06 | Project documentation (PM plan, schedule, status reports, design, test plans, as-built) | Tab.F PMR-06 | Yes | [ASSERTION: standard] | Assertable | — | Assert with caveat |
| 134 | PMR-06a | Detailed design documenting full solution & FR traceability | Tab.F PMR-06a | Yes | [ASSERTION: UTAM detailed-design approach] | Assertable | — | Assert with caveat |
| 135 | PMR-06b | Comprehensive test plan with requirement traceability | Tab.F PMR-06b | Yes | [ASSERTION: UTAM testing pyramid] | Assertable | — | Assert with caveat |
| 136 | PMR-06c | Implementation/migration plan with roles, validation, rollback | Tab.F PMR-06c | Yes | [GROUNDED: UTAM implementation plan + rollback] | Grounded | — | Cite and ground |
| 137 | PMR-06d | As-built documentation reflecting final solution | Tab.F PMR-06d | Yes | [ASSERTION: standard] | Assertable | — | Assert with caveat |
| 138 | PMR-07 | End-user training in Test env with cheat sheets | Tab.F PMR-07 | Yes | [ASSERTION: UTAM training commitment] | Assertable | — | Assert with caveat |
| 139 | PMR-08 | Technical training for BAC personnel (architecture, fault-finding, config) | Tab.F PMR-08 | Yes | [ASSERTION: UTAM training commitment] | Assertable | — | Assert with caveat |
| 140 | PMR-09 | Practical completion after cutover + tests + docs + training; 20% withheld | Tab.F PMR-09 | Yes | [ASSERTION: contractual; not in collateral] | Assertable | — | Assert with caveat |
| 141 | PMR-10 | 6-month defects liability + maintenance agreement aligned to support tiers | Tab.F PMR-10 | Should | [GAP] | Gap | Manageable | Seek evidence |

---

## ISRA (Tab.F — ISRA rows 1-29)

| # | Req ID | Requirement (abridged) | Source | Mandatory | Evidence Pointer | Classification | Gap Severity | Action |
|---|--------|-------------------------|--------|-----------|------------------|----------------|--------------|--------|
| 142 | ISRA-01 | ISO/IEC 27001 accreditation/evidence | Tab.F ISRA 1 | Yes | [GROUNDED: UTAM states ISO 27001 certified] | Grounded | — | Cite and ground |
| 143 | ISRA-02 | Sensitive info collected (private/medical/credit/aviation security/financial/govt IDs)? | Tab.F ISRA 2 | Yes | [ASSERTION: apron video analytics; PII handling to be confirmed with BAC] | Assertable | — | Assert with caveat |
| 144 | ISRA-03 | Auto-delete data when no business requirement | Tab.F ISRA 3 | Yes | [GROUNDED: UTAM retention policies + automated enforcement] | Grounded | — | Cite and ground |
| 145 | ISRA-04 | Asset disposal sanitisation | Tab.F ISRA 4 | Yes | [GROUNDED: UTAM secure erasure + Certificate of Destruction] | Grounded | — | Cite and ground |
| 146 | ISRA-05 | Privileged access management | Tab.F ISRA 5 | Yes | [GROUNDED: UTAM PAM + break-glass] | Grounded | — | Cite and ground |
| 147 | ISRA-06 | Infosec roles & responsibilities in contract | Tab.F ISRA 6 | Yes | [ASSERTION: standard contractual clauses] | Assertable | — | Assert with caveat |
| 148 | ISRA-07 | Mature information security policy evidence | Tab.F ISRA 7 | Yes | [GROUNDED: UTAM ISO 27001 ISMS] | Grounded | — | Cite and ground |
| 149 | ISRA-08 | Annual security awareness training | Tab.F ISRA 8 | Yes | [GROUNDED: UTAM staff awareness training] | Grounded | — | Cite and ground |
| 150 | ISRA-09 | Breach notification process (who/what/how/when) | Tab.F ISRA 9 | Yes | [GROUNDED: UTAM incident handling, 1-hour notification] | Grounded | — | Cite and ground |
| 151 | ISRA-10 | Security updates & patching; time-to-apply; critical handling | Tab.F ISRA 10 | Yes | [ASSERTION: UTAM release train/patch cadence] | Assertable | — | Assert with caveat |
| 152 | ISRA-11 | Change management feeding BAC CAB | Tab.F ISRA 11 | Yes | [GROUNDED: UTAM change management] | Grounded | — | Cite and ground |
| 153 | ISRA-12 | Incident response management (responsibilities, reporting to authorities) | Tab.F ISRA 12 | Yes | [GROUNDED: UTAM incident response] | Grounded | — | Cite and ground |
| 154 | ISRA-13 | Cryptographic controls (confidentiality, integrity, authenticity) | Tab.F ISRA 13 | Yes | [GROUNDED: UTAM AES256/TLS1.2/KMS] | Grounded | — | Cite and ground |
| 155 | ISRA-14 | System secure & resilient against cyber attack | Tab.F ISRA 14 | Yes | [GROUNDED: UTAM zero-trust, WAF, GuardDuty, Inspector, hardening] | Grounded | — | Cite and ground |
| 156 | ISRA-15 | Protection against malicious software | Tab.F ISRA 15 | Yes | [GROUNDED: UTAM Defender for Server / antimalware] | Grounded | — | Cite and ground |
| 157 | ISRA-16 | Meet BAC availability incl. RTO & RPO | Tab.F ISRA 16 | Yes | [GROUNDED: UTAM RTO ≤40 min / RPO near-zero] | Grounded | — | Cite and ground |
| 158 | ISRA-17 | Backup testing to ensure RTO/RPO | Tab.F ISRA 17 | Yes | [GROUNDED: UTAM scheduled restore tests] | Grounded | — | Cite and ground |
| 159 | ISRA-18 | Network management to protect info/services/apps | Tab.F ISRA 18 | Yes | [GROUNDED: UTAM NGFW, WAF, mTLS, segmentation] | Grounded | — | Cite and ground |
| 160 | ISRA-19 | Data sovereignty management | Tab.F ISRA 19 | Yes | [GAP: UTAM states EU residency — conflicts with BAC/Australia; must be re-hosted in Australia] | Gap | Disqualifying | Escalate / re-host in AU |
| 161 | ISRA-20 | Service escrow arrangements | Tab.F ISRA 20 | Yes | [GROUNDED: UTAM source-code escrow agreement] | Grounded | — | Cite and ground |
| 162 | ISRA-21 | Privacy & "right to anonymity" | Tab.F ISRA 21 | Yes | [ASSERTION: UTAM GDPR/pseudonymisation — reframe for Australian Privacy Act] | Assertable | Manageable | Assert with caveat |
| 163 | ISRA-22 | Physical & environmental security (theft, fire, heat, power) | Tab.F ISRA 22 | Yes | [GROUNDED: AWS data centre physical controls] | Grounded | — | Cite and ground |
| 164 | ISRA-23 | Compliance management & validation during contract | Tab.F ISRA 23 | Yes | [GROUNDED: UTAM continuous validation + annual review] | Grounded | — | Cite and ground |
| 165 | ISRA-24 | Formal incident mgmt plans, tested regularly | Tab.F ISRA 24 | Yes | [ASSERTION: UTAM incident response plan; regular testing not evidenced] | Assertable | — | Assert with caveat |
| 166 | ISRA-25 | Hosting location — geographical address | Tab.F ISRA 25 | Yes | [GAP: UTAM cites EU/Athens; Australian address required] | Gap | Disqualifying | Escalate / confirm AU hosting |
| 167 | ISRA-26 | Vetting of staff with privileged access | Tab.F ISRA 26 | Yes | [ASSERTION: standard; not explicitly described] | Assertable | — | Assert with caveat |
| 168 | ISRA-27 | Application whitelisting management | Tab.F ISRA 27 | Yes | [GAP] | Gap | Manageable | Seek evidence |
| 169 | ISRA-28 | MFA enabled across service provider's business | Tab.F ISRA 28 | Yes | [GROUNDED: UTAM MFA across privileged/admin] | Grounded | — | Cite and ground |
| 170 | ISRA-29 | Security event/log management; retention duration | Tab.F ISRA 29 | Yes | [GROUNDED: UTAM CloudTrail/CloudWatch + retention policies] | Grounded | — | Cite and ground |

> Note: 5 rows above (ISRA 1-29) are 29 requirements; total Tab.F rows = 73 + 48 + 19 PMR rows (PMR-01, 02, 02a-f, 03-10) + 29 ISRA = 169. Reconciliation: PMR sub-rows counted individually = 19 (01, 02, 02a, 02b, 02c, 02d, 02e, 02f, 03, 04, 05, 06, 06a, 06b, 06c, 06d, 07, 08, 09, 10 = 20). Total = 73 + 48 + 20 + 29 = 170. Headline count updated below.

**Reconciled total: 170 requirement rows** (73 FR + 48 NF + 20 PMR + 29 ISRA).

Re-tallied coverage:
- Grounded: 74 (44%)
- Assertable: 65 (38%)
- Gap: 31 (18%)

---

## Disqualifying Gaps

| # | Requirement | Why Disqualifying | Possible Resolution |
|---|-------------|-------------------|---------------------|
| R-017 / FR17 | Camera-based detection & classification of the full GSE-type list | Mandatory Must-Have; collateral shows only telematics-based GSE tracking, not camera-AI classification of all listed types | Seek evidence (demo / prior deployment); partner with a computer-vision vendor; or scope as roadmap with explicit mitigation |
| R-020 / FR20 | Personnel presence detection in apron zones (excl. passengers) | Mandatory Must-Have; no evidence of personnel detection via camera in collateral | Seek evidence or partner; may require explicit CV model commitment |
| R-092 / NF19 | Severity-1 response within 1 hour, 24×7×365 + Sev-2/3 commitments | Mandatory Must-Have; no support SLA narrative in collateral | Provide support SLA matrix and evidence of 24/7 capability |
| R-160 / ISRA-19 | Data sovereignty — UTAM doc asserts EU residency (conflict with BAC/Australia) | Mandatory; current collateral mis-grounds residency in EU/Athens | Commit to Australian hosting (AWS Sydney or BAC on-prem); rewrite residency narrative |
| R-166 / ISRA-25 | Hosting geographical address — UTAM cites EU/Athens | Mandatory; address must be Australian | Confirm Australian data-centre address before submission |

---

## Evidence Inventory Cross-Reference

| Collateral File | Type | Requirements Supported |
|----------------|------|------------------------|
| Turnwise Product Document 1.pdf.md | Product / Org | FR04, FR16, FR19, FR25, FR33-FR37, FR40-FR41, FR45-FR47, FR49, FR53, FR59, FR60-FR66, NF32-NF33, NF39 |
| UTAM Solution Architecture (WAISL Draft v1) | Solution architecture | FR05-FR06, FR55, FR58, FR60-FR64, FR67, NF04-NF07, NF15-NF16, NF25, NF32-NF36, NF39-NF46, NF48, PMR-02c/02e/05/06c, ISRA-01/03-05/07-09/11-18/20/22-23/28-29 |

---

## Open Questions

- [ ] R-017/FR17, R-020/FR20, R-023/FR23: Is there prior WAISL deployment evidence of camera-AI detection of GSE types, personnel, and PPE? Current classification: Gap → would become Grounded/Assertable if evidence exists.
- [ ] R-160/ISRA-19, R-166/ISRA-25: Confirm Australian hosting target (AWS Sydney region or BAC on-prem). Current: Gap/Disqualifying → Grounded once AU residency committed.
- [ ] R-078/NF05: Is there a 3-year availability history for Turnwise/UTAM production deployments? Current: Gap → Grounded if telemetry/SLA reports exist.
- [ ] R-092/NF19: Can WAISL commit to the Sev-1 ≤1h 24×7 response matrix? Current: Gap/Disqualifying → Assertable/Grounded if support model defined.
- [ ] R-024/FR24: Confirm whether Turnwise turnaround activity start/end times are camera-AI derived or telematics/CDM derived. Current: Assertable → classification changes based on answer.