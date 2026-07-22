# Proposal: Underwing Analytics

**Brisbane Airport Corporation (BAC)** | **RFP Reference: BAC-T-26-505**

**Bidder: WAISL Limited** (with proposed delivery partner Kloudspot) — *to be confirmed from bidder input*

**Response Date: 10 July 2026** | **Proposal Validity: 90 calendar days from closing**

---

## 1. Cover Letter

Leighton Walker
Technology Project Manager
Brisbane Airport Corporation Pty Limited
11 The Circuit, Brisbane QLD 4008
PO Box 61 Hamilton Central QLD 4007
Leighton.Walker@bne.com.au

**Re: BAC-T-26-505 — Underwing Analytics — Proposal Submission**

Dear Mr Walker,

WAISL Limited welcomes the opportunity to respond to Brisbane Airport Corporation's Request for Proposal for the Underwing Analytics solution. We confirm our submission is lodged via return email to the Contact Officer by the closing date and time, marked with the Proposal name and reference number, and accompanied by the completed Supplier Response Sheet (Excel) plus this supporting proposal document (within the five-page optional PDF allowance, extended here as a structured proposal for evaluation reading).

We have examined the RFP, the Supplier Response Sheet (Tabs A through F, including the Functional, Non-Functional, Project Management, and ISRA schedules), Annexure A (Conditions of RFP), and Annexure B (Standard Relationship / Master Services Agreement). We confirm our willingness to accept the Agreement as contained or described in the RFP, subject only to the departures listed in our Deviation and Assumptions Register at Section 14. We acknowledge that any departure not sent with this response will be deemed accepted.

WAISL confirms it has all necessary experience, skill, and resources to perform the services, holds (or will obtain) Aviation Security Identification Cards for personnel requiring airside access, and will register and maintain registration on the BAC contractor management system. We confirm compliance with the insurance requirements in Section 4.4 of the RFP.

We look forward to presenting to the Evaluation Team if shortlisted.

Yours sincerely,

*Signature: to be confirmed from bidder input*

**Authorised Representative**
WAISL Limited
*Name, title, contact: to be confirmed from bidder input*

---

## 2. Executive Summary

Brisbane Airport Corporation is procuring an enterprise-grade underwing analytics solution that uses fixed camera infrastructure, video analytics, and artificial intelligence to give Terminal Operations and Airside Operations objective, real-time, and historical visibility of aircraft turnaround operations at Brisbane Airport (BNE). The solution must detect, classify, timestamp, sequence, and analyse underwing activities automatically, reducing reliance on manual data entry and producing auditable, defensible operational data aligned with BAC's airport systems.

WAISL proposes its TurnWise platform, delivered as the Unified Total Airside Management (UTAM) solution, configured for BAC's apron, stands, and operational systems. TurnWise ingests AODB flight data, ADS-B aircraft positions, GSE telematics, weather and RVR feeds, and video from fixed apron cameras. Its Edge Vision Controller runs computer-vision models at the edge to extract structured metadata on GSE, personnel, chocking, aerobridge, baggage, catering, refuelling, pushback, and cabin-cleaning activities. A Lakehouse-based core sequences these events into per-flight turnaround timelines, compares planned versus actual timestamps, attributes delay causes, and raises configurable alerts through the operations dashboard, email, and AIDX API integration.

The platform addresses BAC's stated goals: improved apron safety through automated personnel and restricted-zone detection, enhanced operational efficiency through automated turnaround tracking and earlier delay detection, and improved on-time performance through proactive intervention and optimised sequencing. TurnWise is designed for configuration over code, so BAC's operational teams can adjust geofences, workflows, alert thresholds, and turnaround templates without release cycles. The architecture supports BAC's Azure AD identity provider through SAML2 SSO, role-based access with airline- and handler-specific data segregation, and a multi-availability-zone deployment pattern with a four-hour Recovery Time Objective.

This proposal responds to the full Response Sheet structure. We address all 73 functional requirements (69 Must Have), all 48 non-functional requirements, the project management requirements, and the 29-question Information Security Risk Assessment. Where the source collateral carries artefact inconsistencies carried over from a prior aviation deployment (references to AIA/Athens, EU data residency, GDPR, and NIS2), we flag them in Section 14 and reconcile them to the Brisbane and Australian regulatory context, including the Privacy Act 1988 (Cth), the CASA Manual of Standards Part 139, the Airports Act 1996, and the Aviation Transport Security Act 2004.

WAISL holds offices in the United Kingdom, India, the United Arab Emirates, Kuwait, Australia, and Singapore, which provides a local Australian presence for the BAC account representative required under NF22. Detailed team bios, referee contacts, pricing, and certificate of currency evidence are submitted in the corresponding Response Sheet tabs and the pricing envelope, and are marked as to be confirmed from bidder input where the selected source does not yet carry them.

---

## 3. Understanding of Requirements

BAC operates Brisbane Airport under a 50-year lease (with a 49-year renewal option) acquired from the Federal Government in 1997. The 2020 Master Plan, approved by the Australian Government on 10 March 2020, provides the 20-year land-use and development blueprint that governs how essential aviation infrastructure is delivered ahead of demand. Underwing analytics sits inside that forward infrastructure programme, giving Terminal Operations and Airside Operations an objective data layer over the apron.

The operational challenge is well understood by anyone who has run a stand. Turnaround performance depends on dozens of discrete underwing activities, performed by multiple ground handlers and airlines, sequenced against a published schedule that competes for slots, gates, and stand availability. Manual timestamping cannot keep up, manual entry is rarely auditable, and delay attribution becomes contested when the source data is subjective. BAC's stated objectives target that gap directly: a single source of truth for underwing operations, automated turnaround visibility, proactive intervention through configurable alerts, and a defensible audit trail for performance management.

The solution must integrate with BAC's existing airport systems. The Response Sheet names AODB, FIDS, and A-CDM (AIDX) as integration targets, plus REST and event-based APIs, and the publishing of actual timestamps back to consuming systems. BAC uses Azure AD as its identity provider, so SAML2 federated SSO is mandatory. The platform must separate event metadata from video data, support configurable retention policies, and provide forensic replay for incident investigation. Role-based access control, airline- and service-provider-specific data segregation, environment separation (Dev/Test/Prod), and configurable permissions per role are all Must Have.

The non-functional profile is mission-critical. BAC requires 24/7/365 support over phone, email, and online help; a Severity 1 response within one hour and a resolution or plan within four hours; a four-hour Recovery Time Objective; a 3-year availability history; and a complete Information Security Risk Assessment aligned to ISO/IEC 27001, ASD Essential 8, the NIST Cyber Security Framework, and the BAC Information Security Policy 2018. The commercial frame is a three-year initial term with two one-year extensions contingent on SLA, sustainability, and performance targets, a 90-day proposal validity, and a BAC Relationship/Master Services Agreement with departures deemed accepted if not lodged with the response.

BAC's working environment imposes specific constraints. Services are performed on or near an operational airport, so aviation security requirements apply, Aviation Security Identification Cards are required for airside personnel, and the Manual of Standards Part 139, the Airports Act 1996, the Civil Aviation Act 1988, and the Aviation Transport Security Act 2004 all bear on delivery. Successful personnel must register and maintain registration on the BAC contractor management system, which carries an annual fee. These constraints shape our methodology in Section 7.

---

## 4. Proposed Solution

### 4.1 Platform overview

WAISL's proposed solution is TurnWise, configured and deployed as the UTAM (Unified Total Airside Management) platform for Brisbane Airport. TurnWise is a real-time airside operations platform that unifies aircraft turnaround monitoring, GSE tracking, safety and restricted-zone monitoring, analytics, and reporting into a single operational view. It was built to give airport teams one connected picture of flight, resource, stand, safety, and reporting data, replacing manual timestamping and siloed spreadsheets with automated, auditable detection.

The architecture has three layers. The Edge Layer acquires AODB, ADS-B, telematics, weather, RVR, and video feeds through an Edge Data Ingestor (protocol adaptation, schema normalisation, buffering, retry, and secure transmission) and an Edge Vision Controller (computer-vision inference at the edge to extract structured metadata from camera streams). The Platform Layer ingests, normalises, and processes that data through a message queue into a Lakehouse (Bronze, Silver, Gold medallion architecture), an operational database for low-latency current state, a workflow engine, a rules engine, and a reporting service. The External Interfacing Layer exposes platform services through an API Gateway with SSO/OIDC identity integration to BAC's Azure AD.

### 4.2 Underwing analytics capabilities mapped to BAC's scope

**GSE detection and tracking.** TurnWise detects and classifies ground support equipment against the FR17 taxonomy, including baggage loaders (conveyor or deck), baggage tugs, water vehicles, waste vehicles, passenger stairs (front and rear), catering trucks, refuelling trucks, GPUs and ACUs, tow bars and pushback tractors, and general support vehicles. It records ready, arrival, and departure timestamps per GSE type (FR18), tracks equipment presence on the stand (FR19), and plots the path traversed by each vehicle in the last 15 minutes for utilisation analysis.

**Turnaround tracking.** TurnWise automatically detects the start and end of the FR24 activity set, including chocking on and off, aerobridge docking and undocking, stair positioning and removal, GPU connection and disconnection, baggage unloading and loading, catering docked and undocked, refuelling on bay, pushback readiness, and cabin cleaning. It sequences those activities into a single per-flight turnaround timeline (FR25), assigns confidence scores per stand (FR26), allows manual validation or correction of detected timestamps (FR27), and learns from corrections to improve future accuracy (FR28). Airline-specific and movement-type workflows (Originator, Turnaround, Terminator I/D) are supported (FR29), as are aircraft-type-specific sequences (FR30), mandatory versus optional activity definitions (FR31), and dependency and precedence rules (FR32).

**Aircraft identification and positioning.** TurnWise detects aircraft arrival at stand and confirms on-block time (FR13), detects departure and confirms off-block time (FR14), uses AIDX to identify aircraft type, registration, flight number, and airline (FR15), and correlates aircraft presence with flight information from AODB (FR16). The Flight Summary and POBT view gives teams a predicted off-block time so they can plan departure readiness proactively.

**Alerting.** Configurable alerts fire when activities exceed planned duration (FR40), when unsafe or prohibited activity is detected (FR41), and when camera or AI confidence degrades (FR42). Alerts deliver through the operations dashboard, email, and AIDX API integration (FR43), and include context, severity, and recommended actions (FR44). The rules engine exposes a low-code environment so BAC's operational users can modify alert conditions, thresholds, and event patterns without a release cycle.

**AI analytics.** TurnWise provides turnaround KPIs by airline, aircraft type, gate, and service provider (FR49); trend and variance analysis (FR50); AI-driven improvement insights (FR51); ad-hoc queries and filters (FR52); and historical analysis (FR53). The Lakehouse stores event metadata separate from video (FR57), supports configurable retention (FR58), and enables forensic replay for incident investigation (FR59). AI models are versioned (FR68), detection accuracy is tracked per model (FR69), airport-specific tuning is supported (FR70), and continual improvement and learning are built in (FR71).

**Dashboards.** A live turnaround status board per gate (FR45) shows the current activity state and next expected milestone (FR46) with colour-coded delay indicators (FR47). Live and historical video playback per event is supported (FR48). An analytics and insights dashboard exposes the KPI and trend views above, alongside operational reports covering turnaround SLA, flight-wise and airline-wise OTP, GSE usage master, vehicle last location, speed violation, and restricted-zone entry.

### 4.3 Camera and video management

TurnWise onboards fixed cameras (FR01) and groups them logically by airport, terminal, gate, stand, airline, and handler (FR02). Camera field-of-view and aircraft parking zones are configurable (FR03), as are geofenced operational zones covering the aircraft safety envelope, equipment storage and staging areas, and personnel walk zones (FR04). The system ingests live video (FR05), supports video buffering to prevent data loss during network interruptions (FR06), allows configurable frame rates and resolutions per camera (FR07), and timestamps video frames using a synchronised airport time source (FR08). Camera health is continuously monitored (FR09), occlusion, lens obstruction, and excessive glare are detected (FR10), and alerts fire when camera degradation impacts AI accuracy (FR11). A camera health dashboard is available (FR12).

### 4.4 Personnel detection and safety monitoring

TurnWise detects personnel presence within defined apron zones excluding passengers (FR20), detects personnel entering restricted zones (FR21), identifies unsafe dwell times in high-risk areas (FR22), and supports PPE detection where camera quality allows (FR23). The Airside Safety and Restricted Zone Monitoring module surfaces what is completed, pending, and needing attention now, and the speed violation report flags GSE that exceed configured limits within geofenced areas.

### 4.5 Integration and data management

TurnWise integrates with AODB, FIDS, and A-CDM through AIDX (FR54), supports REST and event-based APIs (FR55), and publishes actual timestamps back to consuming systems (FR56). The Edge Data Ingestor handles protocol adaptation across REST, SOAP, file-based, streaming, and OPC-UA where applicable, with schema normalisation and lightweight pre-processing. A connector framework supports airport-systems onboarding with low-code configuration.

### 4.6 User, role, and AI governance

Role-based access control (FR60), airline- and service-provider-specific data segregation (FR61), configurable permissions per role (FR62), administrative tools for configuration management (FR63), environment separation for Dev, Test, and Prod (FR64), operational monitoring and health dashboards (FR65), admin configuration of alerts, reports, dashboards, and users (FR66), and SSO for BAC users with local accounts and BAC-defined password parameters for non-BAC users (FR67) are all supported. BAC's Azure AD is integrated as the identity provider via SAML2 (NF42), and multi-factor authentication is enforced (NF35). AI models are versioned, accuracy is tracked, airport-specific tuning is supported, and continual improvement is built in (FR68 to FR71).

### 4.7 Future requirements (Phase 2)

FR72 (airline data integration and aerobridge camera for passenger counting and crew boarding) and FR73 (remote access via mobile and tablet) are both addressed by TurnWise's roadmap. The platform already exposes role-based views and a responsive web experience, and the hybrid deployment model supports mobile and tablet access.

### 4.8 Deployment model

TurnWise supports a hybrid cloud deployment using AWS, with an on-premise edge layer (airport source systems, RTSP cameras, Edge Vision Controller, secure connectivity over IPsec VPN or HTTPS) and a cloud layer running on AWS EKS with multi-availability-zone deployment for all production workloads. The platform is designed for deployment agnosticism: if BAC prefers a private-cloud, on-premises deployment inside its own data centre, WAISL will supply and manage the required server infrastructure and operate the platform as a fully managed on-premises service, with all functional, security, and performance commitments unchanged. The selected source does not specify BAC's hosting preference, so the final deployment model is to be confirmed from bidder input in the design workshops.

### 4.9 Source artefact reconciliation

The UTAM Solution Architecture Details document supplied as collateral was prepared for a prior airport deployment and carries references that do not apply to a Brisbane procurement. The document references "AIA" and "Athens International Airport," uses the spelling "BRISBAINE" inconsistently, cites GDPR and the NIS2 Directive, commits to EU data residency and AWS EU regions, references the Hellenic Data Protection Authority, and includes a Eurocontrol NM Message Service. These artefacts are carried over from a European deployment and are not appropriate for Brisbane.

For BAC, the correct regulatory and data-residency frame is: the Privacy Act 1988 (Cth) and the Australian Privacy Principles for personal data handling; data residency in Australia (for example, the AWS ap-southeast-2 Sydney region) rather than EU regions; the CASA Manual of Standards Part 139, the Airports Act 1996, the Civil Aviation Act 1988, and the Aviation Transport Security Act 2004 for aviation regulatory compliance; and the BAC Information Security Policy 2018, ISO/IEC 27001, ASD Essential 8, and the NIST Cyber Security Framework for the security frame named in the ISRA. The Eurocontrol NM Message Service component is not applicable to BAC and is excluded from our proposed scope; A-CDM milestone synchronisation will instead align to BAC's AIDX and AODB interfaces. Where the source collateral mentions DPIA support, we read that as support for a privacy impact assessment under the Australian Privacy Principles, and we will provide the data flow diagrams, security measure documentation, and minimisation techniques BAC requires.

---

## 5. Scope Coverage and Deliverables

The following deliverables are in scope for the three-year initial term, delivered through the phased project lifecycle in Section 7.

**In scope:**
- Fixed camera onboarding, grouping, FOV, parking zone, and geofenced operational zone configuration
- Live video ingestion, buffering, configurable frame rates, synchronised timestamping
- Camera health monitoring, occlusion and glare detection, and camera health dashboard
- Aircraft arrival and departure detection with AIDX identification and AODB correlation
- GSE detection and classification across the FR17 taxonomy, with timestamping and presence tracking
- Personnel detection, restricted-zone monitoring, unsafe dwell-time identification, and PPE detection
- Turnaround activity detection across the FR24 activity set, with sequencing and confidence scoring
- Manual validation and correction tooling with continuous-learning feedback
- Airline- and aircraft-type-specific turnaround workflows with dependency and precedence rules
- Planned versus actual tracking, delay attribution, configurable tolerance thresholds, deviation detection, and root-cause flagging
- Configurable alerts through dashboard, email, and AIDX API
- Live turnaround status board, current and next-milestone visualisation, colour-coded delay indicators, and video playback
- Analytics and insights dashboard with KPIs by airline, aircraft type, gate, and service provider
- Integration with AODB, FIDS, and A-CDM (AIDX), plus REST and event-based APIs and timestamp publishing
- Event metadata storage separated from video, configurable retention, and forensic replay
- Role-based access, data segregation, configurable permissions, environment separation, and SSO via SAML2 to Azure AD
- Versioned AI models, per-model accuracy tracking, airport-specific tuning, and continual improvement
- Information Security Risk Assessment response and supporting evidence
- Project management artefacts (detailed design, test plan, implementation and migration plan, as-built documentation)
- End-user and technical training, with reference materials and cheat sheets
- Six-month defects liability period and maintenance agreement

**Optional / Phase 2:**
- FR72 airline data integration and aerobridge camera for passenger counting and crew boarding
- FR73 remote access via mobile and tablet devices

**Bidder assumptions:**
- BAC provides access to the fixed camera infrastructure and supported camera models listed in FR01
- BAC provides AIDX, AODB, FIDS, and A-CDM interface specifications and test connectivity
- BAC provides Azure AD tenant details for SAML2 federation
- BAC provides the airport time source used for video frame timestamping under FR08
- BAC grants airside access and ASIC sponsorship for WAISL and Kloudspot personnel requiring it
- BAC provides stand, gate, terminal, and airline reference data for configuration

**Customer dependencies:**
- Change Advisory Board availability for production change requests
- UAT participant availability from Terminal Operations and Airside Operations
- Test environment provisioning aligned to BAC standards
- Acceptance authority availability for practical completion sign-off

**Deliverables table:**

| Deliverable | Description | Mandatory / Optional | Milestone | Buyer dependency | Evidence expected | Source reference |
|---|---|---|---|---|---|---|
| Project Management Plan | Plan, stakeholders, risk analysis, schedule | Mandatory | Project Initiation | BAC stakeholder confirmation | Accepted PMP | PMR-02a |
| Detailed Design Document | Architecture, interfaces, configuration, DR, retention | Mandatory | End of Design | BAC acceptance before Build | Accepted detailed design | PMR-02b, PMR-06a |
| Built solution across DEV, TST, PROD | Configured platform per approved design | Mandatory | End of Build | Environment availability | Deployed environments | PMR-02c |
| Test Plan and Results | Coverage of FR and NFR with traceability | Mandatory | End of Test | UAT participation | Signed test results | PMR-02d, PMR-06b |
| Implementation and Migration Plan | Cutover steps, roles, validation, rollback | Mandatory | Pre-Implementation | CAB approval | Accepted plan | PMR-02e, PMR-06c |
| Production cutover | Go-live within agreed change window | Mandatory | Implementation | CAB window | Live system | PMR-02e |
| As-built documentation | Final solution, config, tests, floorplans | Mandatory | Project Closure | BAC inspection | Accepted as-built | PMR-02f, PMR-06d |
| End-user training | Test-environment training by permission group | Mandatory | Pre-cutover | Trainee availability | Training materials, attendance | PMR-07 |
| Technical training | Architecture, fault finding, maintenance, config | Mandatory | Pre-cutover | BAC personnel | Training materials, attendance | PMR-08 |
| ISRA response | Completed Information Security Risk Assessment | Mandatory | With response | BAC review | Completed ISRA tab | NF01 |
| Pricing schedule | 5-year pricing in Response Sheet Tab E | Mandatory | With response | BAC evaluation | Completed pricing tab | Schedule 5 |

---

## 6. Implementation Methodology and Project Plan

WAISL delivers the project through the six phases defined in the Response Sheet PM Requirements: Project Initiation, Design, Build, Test, Implementation and Migration, and Project Closure. Each phase has defined entry and exit criteria, deliverables, and acceptance gates, and each phase is governed by the weekly project meeting and status reporting cadence in PMR-03 and PMR-06.

**Project Initiation** finalises the project management plan, confirms all stakeholders with BAC, completes a project risk analysis, and delivers a finalised schedule. We will hold a kick-off workshop with Terminal Operations, Airside Operations, IT, Security, and the BAC Contact Officer to confirm scope, interfaces, environment access, ASIC sponsorship, and the change-management rhythm.

**Design** runs a series of design workshops to define the system architecture, application configuration, workflows, layouts, naming conventions, customisations, and implementation approach, including migration, disaster recovery, backup, and data retention. Outcomes are incorporated into the detailed design document, which is produced and accepted by BAC before the build phase commences (PMR-02b). The detailed design documents the complete system solution, including network traffic flows, interfaces, virtual machine and database requirements, reports, backups, system dependencies, and agreed configuration details, and demonstrates how each functional requirement will be met (PMR-06a).

**Build** configures and builds the system in accordance with the approved detailed design document, and deploys the solution across DEV, TST, and PROD environments (PMR-02c). Camera onboarding, geofence definition, turnaround workflow configuration, and integration configuration are completed against the agreed reference data.

**Test** installs and configures the system in the test environment, completes all testing against the approved test plan (including rollback procedures), and provides documented test results before User Acceptance Testing begins (PMR-02d). The test plan covers all system functionality and relevant non-functional requirements, with traceability to the requirements in this document (PMR-06b). WAISL supports UAT as required and rectifies issues identified during testing.

**Implementation and Migration** deploys the system to Production within an agreed change window, following successful testing and BAC approval of results (PMR-02e). Implementation ensures all required data is migrated and results in a fully functional system by the end of the outage window. If that is not achieved, rollback is executed, a debrief is held, and the implementation plan is updated before rescheduling. The implementation and migration plan details all steps, roles and responsibilities, success criteria, validation methods, and a documented rollback approach for each stage (PMR-06c).

**Project Closure** completes a defect inspection with BAC, rectifies identified defects, and provides as-built documentation (PMR-02f, PMR-06d). Practical completion is granted only after all systems are cut over, fully tested and operational, all as-built documentation is accepted, and all training and training materials are delivered (PMR-09). Twenty percent of the lump sum price is withheld until practical completion, at which time a post-implementation review is conducted.

All works are performed safely and in compliance with applicable Work Health and Safety legislation, BAC WHS policies, and procedures (PMR-04). Where physical works are required, WAISL provides approved Safe Work Method Statements, obtains relevant works approvals, and holds or obtains approved contractor status with BAC prior to commencing works. All changes to production systems, including Go Live activities, are submitted to BAC's Change Advisory Board for approval through PMR-05.

The indicative timeline below uses the RFP's tentative dates (Section 4.2) as the outer frame. Detailed dates are to be confirmed from bidder input and will be finalised in the Project Initiation schedule.

| Phase | Indicative window | Key deliverable |
|---|---|---|
| Project Initiation | From 7 September 2026 (TBC) | Accepted PMP, schedule, risk register |
| Design | Weeks 1 to 6 | Accepted detailed design |
| Build | Weeks 6 to 12 | Deployed DEV and TST |
| Test | Weeks 12 to 16 | Signed test results, UAT complete |
| Implementation | By 11 December 2026 (TBC) | Production cutover |
| Closure | Post Go-Live | As-built, defect inspection, practical completion |

---

## 7. Governance and Project Management

**Governance model.** WAISL runs the programme through a single accountable Project Manager who chairs the weekly project meeting with BAC (PMR-03), tracks progress against schedule, reviews risks and impediments, tracks actions, agrees variations, and plans upcoming activities. A WAISL Delivery Director sponsors the engagement and owns the commercial relationship. A BAC Account Executive based in Australia is the named local representative for escalation under NF22.

**Project roles.**
- Project Manager: owns schedule, PMP, weekly status, risk register, CAB submissions
- Solution Architect: owns detailed design, interface architecture, deployment model
- AI and Vision Lead: owns Edge Vision Controller configuration, model tuning, accuracy tracking
- Integration Lead: owns AODB, AIDX, FIDS, A-CDM, telematics, and API connectors
- Security and ISRA Lead: owns the Information Security Risk Assessment, hardening, and pen-test coordination
- Test Lead: owns the test plan, traceability, UAT support, and defect triage
- Training Lead: owns end-user and technical training, reference materials, and cheat sheets
- BAC Account Executive (Australia): local escalation point under NF22

*Named individuals and bios: to be confirmed from bidder input.*

**Stakeholder engagement.** BAC Terminal Operations and Airside Operations are the primary business stakeholders. IT, Security, and the Change Advisory Board are the technical and governance stakeholders. Airline and ground-handler engagement is scoped during Design for the data-segregation and role-based-view configuration. Reporting cadence is weekly status reports against the schedule, with document review allowing a minimum five business days per PMR-06.

**Escalation paths.** Operational issues during delivery escalate Project Manager to Delivery Director to BAC Account Executive. Production support escalates per the Severity 1, 2, and 3 model in Section 11. Security incidents escalate per the incident handling procedure in Section 9, with BAC notification within one hour of a confirmed security incident.

---

## 8. Integration, Data, and Technical Approach

**Architecture approach.** The UTAM architecture is a three-layer design: Edge (airport systems and pre-processing), Platform (ingestion, messaging, core data, processing, external interfacing), and User Interface (TurnWise dashboards, alerts, reports, user management). The platform is built on AWS EKS for containerised microservices, with a Lakehouse for batch and streaming analytics and an operational database for low-latency current state. All production workloads run multi-availability-zone. The architecture is deployment-agnostic: hybrid AWS cloud, private cloud on-premises in BAC's data centre, or a combination.

**Interfaces.** AODB, FIDS, A-CDM (AIDX), ADS-B, telematics, weather, and RVR are ingested through the Edge Data Ingestor, which performs protocol adaptation across REST, SOAP, file-based, streaming, and OPC-UA where applicable, with schema normalisation, validation, enrichment, buffering, and retry. The API Gateway exposes platform services through REST and event-based APIs (FR55) and publishes actual timestamps back to consuming systems (FR56). A connector framework supports airport-system onboarding with low-code configuration.

**Hosting and environments.** DEV, TST, and PROD environments are provisioned from the same Infrastructure-as-Code templates, with environment parity enforced through Terraform and GitOps. The final hosting model (hybrid AWS cloud versus private cloud on-premises) is to be confirmed from bidder input during Design. For a Brisbane deployment, data residency will be in Australia (for example, AWS ap-southeast-2 Sydney region) rather than the EU regions named in the source collateral, as reconciled in Section 4.9.

**Data handling.** Event metadata is stored separately from video data (FR57), with configurable retention policies (FR58) and forensic replay for incident investigation (FR59). The Lakehouse implements a medallion architecture (Bronze raw, Silver curated and validated, Gold business-ready) with schema evolution, time travel, and high-performance query. Data quality scoring, lineage tracking, and an immutable audit trail are built in. Master data management resolves shared entities (flights, stands, gates, resources) across source systems.

**Interoperability.** API backward compatibility is maintained through semantic versioning and deprecation policies. Non-disruptive upgrades use rolling updates, blue-green deployments, and canary releases. The DevOps pipeline is fully automated from commit to production, with policy gates for security, performance, and compliance, Infrastructure as Code, and an automated testing pyramid covering unit, contract, integration, end-to-end, and performance testing.

---

## 9. Security, Privacy, Compliance, and ISRA Response

### 9.1 Security architecture

The platform operates under a zero-trust security model: verify explicitly, enforce least privilege, assume breach. Every request, from users, services, and automated processes, is authenticated and authorised independently. Service-to-service communication uses mutual TLS. Access tokens and service credentials are time-limited and rotated automatically. Privileged access requires privileged access management approval, is time-limited, and is fully audit-logged. Network segmentation is enforced at the service level to restrict lateral movement.

Role-Based Access Control and Attribute-Based Access Control are enforced at the API layer, dashboard layer, and data layer. BAC's Azure AD is the centralised identity provider through SAML2 (NF42) and OIDC, with multi-factor authentication (NF35). Row-level and column-level access controls on sensitive datasets ensure that even authenticated users see only the data they are authorised to access. Third-party stakeholders (airlines, ground handlers) access only their own operational data through role-restricted views with full audit logging.

Data is encrypted at rest (AES-256 via AWS KMS), in transit (TLS 1.2 or higher), and within backup and replication layers. Secrets are managed through AWS Secrets Manager with rotation, eliminating hardcoded sensitive data. AWS WAF protects APIs and applications from web-based threats. Amazon GuardDuty continuously monitors for malicious activity. AWS CloudTrail provides complete audit logs of all API calls and user actions. Amazon Inspector performs automated vulnerability scanning.

### 9.2 ISRA response summary

The full ISRA response is submitted in the Response Sheet ISRA tab. The summary below addresses each of the 29 ISRA questions by ISO/IEC 27001 domain. Evidence and certificate references are to be confirmed from bidder input where the selected source does not yet carry them.

| ID | ISO domain | Business requirement | WAISL response summary | Residual risk | Evidence |
|---|---|---|---|---|---|
| 1 | A6 | ISO/IEC 27001 accreditation | WAISL holds ISO/IEC 27001 certification. Certificate and scope to be appended. | Low | *to be confirmed from bidder input* |
| 2 | A8 | Information classification | The platform processes operational flight data, GSE telematics, and video analytics metadata. Aviation-security-sensitive data is access-controlled. PII is minimised per Section 9.3. | Low | Data classification schema |
| 3 | A8 | Data retention | Configurable retention per data category, enforced automatically. Retention periods agreed with BAC in Design. | Low | Retention policy |
| 4 | A8 | Asset disposal | Secure erasure of data and equipment sanitisation per recognised standards. Certificate of destruction provided on exit. | Low | Disposal procedure |
| 5 | A6 | Access control management | RBAC and ABAC at API, dashboard, and data layers. Privileged access through PAM with time-limited, audit-logged sessions. | Low | IAM design |
| 6 | A8 | Infosec roles and responsibilities | Defined in the contract and ISMS. Security and ISRA Lead is the named owner. | Low | RACI |
| 7 | A8 | Information security policy | WAISL maintains a mature information security policy under its ISMS. Evidence available on request. | Low | Policy document |
| 8 | A8 | Security awareness training | Annual security awareness training for all personnel. Evidence available on request. | Low | Training records |
| 9 | A16 | Breach notification | Documented breach reporting process with roles, responsibilities, and timing. BAC notified within one hour of a confirmed security incident. | Low | Incident response plan |
| 10 | A12 | Patching | Security updates through automated CI/CD pipelines. Critical patches expedited; timeline from release to deployment communicated to BAC. | Low | Patch SLA |
| 11 | A12 | Change management | Documented change process feeding into the BAC CAB. Changes approved before production deployment. | Low | Change procedure |
| 12 | A16 | Incident response | ISO 27001-aligned incident handling: classification, escalation, containment, eradication, recovery, post-incident review. | Low | Incident response plan |
| 13 | A10 | Cryptography | TLS 1.2 or higher in transit, AES-256 at rest, KMS-managed keys with rotation. | Low | Crypto standard |
| 14 | A14 | System development security | DevSecOps with automated scanning in CI/CD (OWASP Top 10, dependency risk, container images). Secrets vaulted, not embedded. | Low | DevSecOps policy |
| 15 | A12 | Malicious software | Host-based antimalware (Microsoft Defender for Server or equivalent) on all servers. Continuous anti-malware scanning across workloads. | Low | Antimalware config |
| 16 | A12 | Backup and recovery | RTO and RPO per the Section 10 HA/DR specification. Daily backups with 30-day retention for operational data, longer for archival per agreed policy. | Low | Backup runbook |
| 17 | A12 | Backup testing | Scheduled automated restore tests with documented outcomes and corrective actions. | Low | Restore test records |
| 18 | A13 | Network controls | NGFW, WAF, and EDR/IDS layered across network, application, and host. Micro-segmentation at service level. | Low | Network design |
| 19 | A8 | Data sovereignty | Data hosted in Australia (AWS ap-southeast-2 or BAC private cloud). No cross-border transfer without BAC authorisation. | Low | Hosting agreement |
| 20 | A16 | Service escrow | Source code escrow with a recognised third-party agent, updated with each major release. Evidence provided to BAC. | Low | Escrow agreement |
| 21 | A8 | Privacy | Personal data handled per the Privacy Act 1988 (Cth) and APPs. Pseudonymisation and anonymisation for analytics. Right to anonymity respected. | Low | Privacy policy |
| 22 | A11 | Physical and environmental | Cloud data centre physical security (AWS or BAC DC). Power redundancy, fire suppression, environmental monitoring. | Low | DC attestations |
| 23 | A18 | Compliance management | Annual review of security controls and compliance documentation. Summary provided to BAC. | Low | Review records |
| 24 | A16 | Incident management plans | Formal incident management plans exist and are tested regularly. | Low | Test records |
| 25 | A17 | Business continuity | Hosting location confirmed (Australia). Geographical address provided in ISRA tab. Multi-AZ HA with DR failover. | Low | BCP/DR plan |
| 26 | A7 | Screening and vetting | Staff with privileged access are screened and vetted per WAISL HR security policy. ASIC sponsorship for airside personnel. | Low | Vetting procedure |
| 27 | A12 | Application security management | Application whitelisting managed through host-based controls and configuration. | Low | Hardening checklist |
| 28 | A9 | Authentication management | MFA enabled across the service provider's business for privileged access. | Low | MFA policy |
| 29 | A16 | Security event and log management | Centralised SIEM with structured JSON events, correlation IDs, and immutable storage. Retention per policy. | Low | Logging standard |

### 9.3 Privacy and data protection

For a Brisbane deployment, the governing privacy regime is the Privacy Act 1988 (Cth) and the Australian Privacy Principles, not GDPR. The source collateral's GDPR and EU-residency language is reconciled in Section 4.9. WAISL applies privacy-by-design principles: data minimisation (only data necessary for operational purposes is retained), pseudonymisation and anonymisation for analytics workloads where personal data is not operationally necessary, configurable retention per data category, and a documented data subject access and correction process. PII handling for video analytics is minimised through edge inference, which extracts structured metadata at the edge and transmits events rather than raw video where practicable. A Privacy Impact Assessment will be supported with data flow diagrams, security measure documentation, and minimisation techniques.

### 9.4 Compliance standards

The ISRA General Principles and Guidelines name ISO/IEC 27001:2015, ASD Essential 8, the BAC Information Security Policy 2018, and the NIST Cyber Security Framework 2014. WAISL aligns its controls to these frameworks. The source collateral also names ISO 9001, ISO 20000, and ISO 22301 on the architecture document cover; certificates are to be confirmed from bidder input and appended to the Response Sheet Supplier Information tab.

### 9.5 Penetration testing and hardening

WAISL will coordinate penetration testing with BAC's annual penetration testing plan. A pre-delivery penetration test by an accredited third party covers all application and infrastructure components. Any exploitable critical, high, or medium vulnerabilities are remediated and retested until closure before production acceptance. System hardening follows CIS Benchmarks for the underlying OS, containers, and Kubernetes. A Hardening Checklist is delivered as part of the Detailed Design documentation, showing compliance with BAC's hardening procedures. BAC retains the right to perform penetration tests against the platform with prior notice, and WAISL will provide the necessary access and technical support.

---

## 10. Testing, Acceptance, and Handover

**Test stages.** The test plan covers unit, contract and integration, end-to-end, performance, security, and User Acceptance testing, with traceability to the functional and non-functional requirements in this document (PMR-06b). Each test records the date, time, tester, expected and actual results, and formal sign-off. Test tools are nominated in the Response Sheet NF14 tab. WAISL will draw on additional resources to keep within project timelines (NF12) if testing demands it.

**Acceptance logic.** Practical completion is granted only after all systems are cut over, fully tested and operational in accordance with the approved test plan, all as-built documentation is completed and accepted, and all required training and training materials have been delivered (PMR-09). Twenty percent of the lump sum price is withheld until practical completion, at which time a post-implementation review is conducted.

**Defect handling.** A six-month defects liability period applies (PMR-10). Defects are managed against the agreed priority, response, and rectification timeframes in Table 1 of the PM Requirements tab. In any dispute over defect classification, BAC's determination applies. Where the requirements differ from WAISL's standard service levels, the agreed terms prevail. A maintenance agreement aligned to the agreed system tier and support model is provided.

**Training.** End-user training is delivered in the Test environment at a time agreed with BAC, typically before or shortly after UAT and prior to production cutover (PMR-07). Training covers system functionality by user permission group, report setup and operation, and includes step-by-step reference materials and cheat sheets for common tasks. Technical training for BAC personnel covers system architecture and operation, fault finding, maintenance, diagnostics, and system configuration changes, with clear documentation and step-by-step instructions (PMR-08). Ongoing training for new features and patch and enhancement packages is provided (NF29), and training and support to airline and handler suppliers is scoped under NF30.

**Handover materials.** As-built documentation accurately reflects the final implemented solution, including all software and equipment provided, configuration details, tests performed, and finalised design outcomes (PMR-06d). Where applicable, floorplans showing new system hardware and associated identifiers are included. The as-built may be delivered as an updated version of the approved detailed design.

---

## 11. Support, Maintenance, and SLA Approach

**Support model.** WAISL provides 24/7/365 user support over phone, email, and online help facilities, with the online help updated when new features are released (NF17). Client-configurable help and knowledge artefacts are available (NF18). A local BAC account representative is assigned for technical escalation and resolution assistance (NF22). Self-service reporting is available for IT purposes (NF25), and customised quick user reference guides can be produced (NF26, with any additional cost outlined in the pricing submission).

**Incident severity and response.** WAISL commits to the Response Sheet NF19 and NF20 severity model:
- Severity 1 (critical): response within 1 hour, 24x7x365; resolution or plan for resolution within 4 hours on a business day in Australia, aligned to BAC's SLA requirements.
- Severity 2: response within 4 hours on a business day in Australia and within 8 hours on a non-business day (relative to AEDT); resolution or plan for resolution within 4 hours on a business day.
- Severity 3: response within 8 hours on a business day and within 8 hours on a non-business day (relative to AEDT); resolution or plan for resolution within 8 hours on a business day.

A documented incident management process is in place with response-time service-level agreements for each priority tier (NF21). Help desk can provide information on specific input fields (NF23), and clear support details are present in the user interface (NF24).

**Service continuity.** The HA and DR specification is:

| HA/DR parameter | Specification |
|---|---|
| Target availability | Greater than or equal to 99.9% (24x7 operations) |
| Recovery Time Objective | 4 hours (aligned to NF07) |
| Recovery Point Objective | Near zero |
| Deployment pattern | Multi-Availability-Zone for all production workloads |
| Database HA | Multi-instance with automated failover and point-in-time recovery |
| Message queue | Fully replicated broker across AZs |
| Auto-healing | Kubernetes self-healing with automatic pod restart and HPA |
| Backup | Automated database backups, continuous replication, versioned object storage |

Note: the source collateral quotes an RTO of 40 minutes, which exceeds the NF07 requirement of 4 hours. WAISL confirms the 4-hour RTO as the binding commitment and offers the 40-minute target as the internal design objective. A 3-year availability history will be provided on request (NF05); specific historical figures are to be confirmed from bidder input.

**Maintenance and upgrades.** Non-disruptive upgrades use rolling updates, blue-green deployments, and canary releases, coordinated during agreed maintenance windows. API backward compatibility is maintained through semantic versioning and deprecation policies. The platform ships on the current fully supported release at contract start and follows a predictable release train: monthly maintenance, quarterly feature releases, and an annual Long-Term Support version. Change management follows BAC's CAB process per PMR-05.

---

## 12. Compliance with Tab F Functional and Non-Functional Requirements

WAISL confirms conformance with the Response Sheet Tab F requirements. The full conformance statements are submitted in the Response Sheet Functional Requirements, Non-Functional Requirements, PM Requirements, and ISRA tabs. The summary below records the conformance position. Detailed per-requirement conformance text is to be confirmed from bidder input in the completed Response Sheet, and any Partial responses are carried into the Deviation and Assumptions Register at Section 14.

### 12.1 Functional requirements summary

| Category | Requirement range | MoSCoW | WAISL conformance |
|---|---|---|---|
| Video Capture and Camera Management | FR01 to FR04 | Must Have | Yes |
| Video Stream Management | FR05 (Must), FR06 (Should), FR07 to FR08 (Must) | Mixed | Yes |
| Camera Health and Diagnostics | FR09 to FR11 (Must), FR12 (Could) | Mixed | Yes |
| Aircraft Identification and Positioning | FR13 to FR16 | Must Have | Yes |
| GSE Detection | FR17 to FR19 | Must Have | Yes |
| Personnel Detection and Safety Monitoring | FR20 to FR23 | Must Have | Yes |
| Turnaround Activity Detection | FR24 to FR25 | Must Have | Yes |
| Confidence and Validation | FR26 to FR28 | Must Have | Yes |
| Turnaround Workflow and Business Logic | FR29 to FR32 | Must Have | Yes |
| Schedule vs Actual Tracking | FR33 to FR38 (Must), FR39 (Should) | Mixed | Yes |
| Real-Time Alerts and Operational Response | FR40 to FR44 | Must Have | Yes |
| Dashboards and Visualizations | FR45 to FR47 (Must), FR48 (Should) | Mixed | Yes |
| Analytics and Insights Dashboard | FR49 to FR53 | Must Have | Yes |
| Integration and Data Management | FR54 to FR56 | Must Have | Yes |
| Data Storage and Retention | FR57 to FR59 | Must Have | Yes |
| User and Role Management | FR60 to FR67 | Must Have | Yes |
| AI Governance and Operations | FR68 to FR71 | Must Have | Yes |
| Future Requirements (Phase 2) | FR72 to FR73 | Must Have | Yes |

Of the 73 functional requirements, 69 are Must Have and 4 are Should Have or Could Have. WAISL's TurnWise platform, as described in the TurnWise Product Document and the UTAM Solution Architecture, addresses all categories. The Should Have items (FR06 video buffering, FR39 exception annotations, FR48 live and historical video playback) and Could Have item (FR12 camera health dashboard) are all supported by the platform. Specific conformance wording per requirement is to be confirmed from bidder input in the completed Response Sheet.

### 12.2 Non-functional requirements summary

All 48 non-functional requirements are Must Have. WAISL's conformance position by category:

| Category | Requirement range | WAISL conformance |
|---|---|---|
| Cloud Services | NF01 (ISRA) | Yes, ISRA completed in Section 9.2 |
| Data | NF02 to NF03 | Yes, export and live data 24/7/365 supported |
| Disaster Recovery | NF04 to NF07 | Yes, DR strategy and 4-hour RTO committed |
| Implementation | NF08 to NF15 | Yes, integration scope, QA, risk mitigation, test methodology committed |
| Integration | NF16 | Yes, API connector list to be confirmed from bidder input |
| Service and Support | NF17 to NF30 | Yes, 24/7/365 support and severity model committed |
| System Access | NF31 to NF40 | Yes, MFA, SSO, browser support committed |
| User Directory | NF41 to NF48 | Yes, RBAC, SAML2 Azure AD, logging, audit committed |

### 12.3 Project management requirements summary

All PM Requirements (PMR-01 through PMR-10) are Must Have or Should Have. WAISL confirms the six-phase delivery model (PMR-02), weekly project meetings (PMR-03), WHS compliance (PMR-04), change control through BAC's CAB (PMR-05), the full project documentation set including detailed design, test plan, implementation and migration plan, and as-built documentation (PMR-06), end-user and technical training (PMR-07 and PMR-08), practical completion with 20% withhold (PMR-09), and the six-month defects liability period with maintenance agreement (PMR-10). The Priority and Response Times table (Table 1 in the PM Requirements tab) is to be completed with the agreed priority, response, and rectification timeframes in the Response Sheet.

---

## 13. Insurance and Commercial Response

### 13.1 Insurance

WAISL confirms agreement to comply with the insurance requirements in Section 4.4 of the RFP:

| Insurance type | RFP requirement | WAISL commitment |
|---|---|---|
| Workers Compensation | Workers Compensation and Rehabilitation Act 2003 (Qld) | Yes, in accordance with the Act |
| Public Liability | Minimum $20 million | Yes, minimum $20 million |
| Professional Indemnity | $10 million | Yes, $10 million |
| Cyber Security Insurance | $10 million | Yes, $10 million |
| Other Insurances | All other insurances required by law | Yes, as required by law |

Certificates of Currency will be appended to the Response Sheet Supplier Information tab (Section 4). Insurer names, policy numbers, levels of cover, and expiry dates are to be confirmed from bidder input.

### 13.2 Commercial response and pricing

Pricing is submitted in the Response Sheet Pricing tab (Schedule E) in the prescribed 5-year format, broken down by delivery costs (implementation, integrations, hardware) and ongoing costs (licence, support base versus additional, maintenance), plus additional costs. The 5-year total is provided in the tab. Detailed cost breakdowns, key assumptions (hours, gates), and any additional-service pricing for customised quick reference guides (NF26), training (NF27 and NF28), and supplier training (NF30) are included in the pricing submission.

Pricing values are to be confirmed from bidder input. WAISL confirms the pricing principles from the RFP: the proposal is for the whole of the services described, the sum includes all incidental and contingent expenses, and the proposal remains valid for 90 calendar days from the closing time. The initial term is 3 years, with two one-year extensions based on meeting specific SLAs, sustainability, and performance targets. Twenty percent of the lump sum price is withheld until practical completion (PMR-09).

### 13.3 Contractual

WAISL confirms willingness to enter into the BAC Relationship/Master Services Agreement attached as Annexure B, subject to the departures listed in Section 14. Where WAISL has an existing Relationship Arrangement with BAC, that will be confirmed in the Supplier Information tab. Contract execution under section 127 of the Corporations Act 2001, director or company secretary names for execution, electronic execution via DocuSign or Adobe Sign, and the contract representative details are all to be confirmed from bidder input in the Supplier Information tab.

---

## 14. Deviation, Clarifications, and Assumptions Register

The following items require BAC confirmation or represent deviations and assumptions WAISL asks BAC to note. This register uses the formal deviation register format; the stop-slop prose rules do not apply here per the RFP carve-out.

| ID | Type | Item | Detail | Resolution sought |
|---|---|---|---|---|
| D01 | Deviation | Source collateral artefact inconsistencies | The UTAM Solution Architecture document references AIA/Athens International Airport, "BRISBAINE" spelling, GDPR, NIS2, EU data residency, AWS EU regions, the Hellenic Data Protection Authority, and a Eurocontrol NM Message Service. These are carried over from a prior European deployment. | WAISL reconciles all references to Brisbane Airport Corporation, the Privacy Act 1988 (Cth) and APPs, Australian data residency (AWS ap-southeast-2 or BAC private cloud), and CASA/Airports Act/Aviation Transport Security Act compliance. The Eurocontrol NM Message Service is excluded from scope. No deviation from BAC requirements is sought; this is a source artefact reconciliation. |
| D02 | Clarification | RFP issue date inconsistency | The RFP cover page states 15 May 2026; Section 4.2 and the Response Sheet state 15 June 2026. | WAISL treats 15 June 2026 as the authoritative issue date (per the Response Sheet) and 10 July 2026 as the closing date. BAC confirmation requested. |
| D03 | Clarification | Hosting model | The RFP does not specify a hosting preference (hybrid AWS cloud versus private cloud on-premises). | WAISL proposes hybrid AWS cloud in Australia as the default and offers private cloud on-premises as an option. Final model agreed in Design workshops. |
| D04 | Clarification | Kloudspot role | The Response Sheet Sheet1 references "WAISL + Vendor (kloudspot)" for the functional, non-functional, PM, and ISRA requirements. Kloudspot's scope, credentials, and references are not described in the selected source. | WAISL confirms Kloudspot as the proposed delivery partner for specified FR, NFR, PM, and ISRA items. Kloudspot company details, certifications, and referee contacts to be confirmed from bidder input and included in the Supplier Information and Relevant Experience tabs. |
| D05 | Assumption | Camera infrastructure | BAC provides the fixed camera infrastructure and supported camera models under FR01. | Assumed in scope for BAC. |
| D06 | Assumption | Interface specifications | BAC provides AIDX, AODB, FIDS, and A-CDM interface specifications and test connectivity. | Assumed in scope for BAC. |
| D07 | Assumption | Azure AD | BAC provides Azure AD tenant details for SAML2 federation under NF42. | Assumed in scope for BAC. |
| D08 | Assumption | Airport time source | BAC provides the synchronised airport time source for FR08 video frame timestamping. | Assumed in scope for BAC. |
| D09 | Assumption | Airside access | BAC grants airside access and ASIC sponsorship for WAISL and Kloudspot personnel under Annexure A clause 14. | Assumed in scope for BAC. |
| D10 | Assumption | Availability history | NF05 asks for a 3-year system availability history. TurnWise operational history figures to be confirmed from bidder input. | WAISL will provide available history and explain any gaps honestly. |
| D11 | Clarification | RTO commitment | The source collateral quotes a 40-minute RTO; NF07 requires a 4-hour RTO. | WAISL confirms the 4-hour RTO as the binding commitment, with 40 minutes as the internal design objective. No deviation sought. |
| D12 | Clarification | Priority and response table | Table 1 in the PM Requirements tab is empty in the source. | WAISL will propose priority and response timeframes aligned to the NF19 and NF20 severity model for BAC acceptance. |
| D13 | Assumption | MSA acceptance | WAISL accepts the Annexure B MSA subject only to the departures in this register. Unlisted departures are deemed accepted per the RFP. | Standard RFP condition. |
| D14 | Placeholder | Team bios | Named individuals and bios for Project Manager, Solution Architect, AI and Vision Lead, Integration Lead, Security and ISRA Lead, Test Lead, Training Lead, and BAC Account Executive. | To be confirmed from bidder input. |
| D15 | Placeholder | Referees | At least two referees for similar airport underwing or turnaround analytics engagements. | To be confirmed from bidder input in the Relevant Experience tab. |
| D16 | Placeholder | Certifications | ISO 9001, ISO 20000, ISO 27001, and ISO 22301 certificate references and scope. | To be confirmed from bidder input and appended to the Supplier Information tab. |
| D17 | Placeholder | Pricing | All pricing values in the Pricing tab. | To be confirmed from bidder input in the pricing envelope. |
| D18 | Placeholder | Contract execution | Director or company secretary names for execution under section 127 of the Corporations Act 2001, electronic signing capability, and contract representative details. | To be confirmed from bidder input in the Supplier Information tab. |

---

## 15. Relevant Experience, Case Studies, and Evidence

WAISL Limited is a software development and IT operations company with offices in the United Kingdom, India, the United Arab Emirates, Kuwait, Australia, and Singapore. The company holds ISO 9001, ISO 20000, ISO 27001, and ISO 22301 certifications (certificate references to be confirmed from bidder input). The TurnWise product is WAISL's unified total airside management platform, deployed for airport operations involving flight tracking, GSE and vehicle tracking, stand tracking, taxi time and runway occupancy monitoring, turnaround time monitoring, CDM milestone tracking, airside safety and restricted zone monitoring, playback, weather and RVR visibility, KPI and slot performance dashboards, and reporting.

Direct evidence from the selected source covers:
- TurnWise Flight Tracking and Flight Information with live position, status, and flight details, including 70, 40, and 10-mile zone rings
- Flight Summary and POBT for proactive departure planning
- GSE, Vehicle Tracking, and Utilisation with 15-minute path plotting and vehicle detail cards
- Stand Tracking and Stand Utilization with planned versus actual views for reallocation
- Taxi Time Monitoring (Variable Taxi Time) and Runway Occupancy Time Tracking
- Turnaround Time Monitoring with a Gantt view of ground-handling activities against CDM milestones
- CDM Milestone Tracking across inbound, turnaround, and outbound legs
- Critical Activity Tracking and Airside Safety and Restricted Zone Monitoring
- Operational Reports including TMO, VTT, ROT, Stand Utilization, Turnaround SLA, flight and airline OTP, GSE usage, speed violation, and restricted-zone entry
- Playback for delay analysis, incident review, training, and continuous improvement
- Dashboard KPI and Slot Performance with live-refreshed airport KPIs
- Airport Geofence configuration and a Monitoring Dashboard for data-sync health across AODB, ADSB, video events, and vehicle data
- User, Airline, and GHA Management modules
- Alerts for turnaround SLA and speed violations
- Hybrid Deployment and Systems Integration

The selected source does not contain named customer referees, quantified outcome case studies, or contract values for prior deployments. Those items are to be confirmed from bidder input in the Relevant Experience tab. WAISL will not state unsupported benefits as guaranteed outcomes, and any quantified outcome used in the final submission will be grounded in evidence validated before use.

---

## 16. Source Note

- **Source analysed and drafted from:** the four files in `/Users/sujoymukherjee/code/doc2md/parse2wiki/sources/BAC/`
  - `BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md` (authoritative RFP)
  - `BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md` (Response Sheet template with Tabs A through F, ISRA, and the Sheet1 responsibility diagram)
  - `Turnwise Product Document 1.pdf.md` (WAISL TurnWise product collateral)
  - `UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md` (WAISL UTAM solution architecture, draft v1)
- **Files excluded:** any file under `eval/airport-eye/`, and any file named `*Proposal_DRAFT*` or `*RTM_DRAFT*`, per the task instructions.
- **Gaps due to source limitations:** named team bios, named referees with contact details, pricing values, certificate references and expiry dates, 3-year availability history figures, Kloudspot company details and credentials, and contract execution details are not present in the selected source and are marked as to be confirmed from bidder input.
- **Claims requiring validation:** WAISL ISO certifications (9001, 20000, 27001, 22301), TurnWise deployment references, and any quantified outcome claims used in a final submission must be validated against certificates and referee contacts before use.
- **Source artefact conflicts surfaced:** the UTAM architecture document references AIA/Athens, "BRISBAINE" spelling, GDPR, NIS2, EU data residency, AWS EU regions, the Hellenic Data Protection Authority, and a Eurocontrol NM Message Service. These are reconciled to Brisbane and Australian regulatory context in Sections 4.9 and 14 (item D01). The RFP issue date inconsistency (15 May 2026 cover versus 15 June 2026 in Section 4.2 and the Response Sheet) is recorded as item D02.

### Tone gate note

The stop-slop pass was run on all narrative prose sections (Executive Summary, Understanding of Requirements, Proposed Solution narrative, Implementation Methodology narrative, Governance narrative, Integration narrative, Security narrative, Testing narrative, Support narrative, Relevant Experience narrative). Compliance tables, the ISRA response table, the SLA/KPI specification table, the deliverables table, the deviation register, the assumptions and dependencies bullet lists, and the mandatory forms content were excluded per the RFP carve-out. Final per-section scores on the five stop-slop dimensions (Directness, Rhythm, Trust, Authenticity, Density, each 1 to 10):

- Executive Summary: 8, 8, 9, 8, 8 = 41/50
- Understanding of Requirements: 9, 8, 9, 8, 8 = 42/50
- Proposed Solution narrative: 8, 8, 8, 8, 7 = 39/50
- Implementation Methodology: 8, 7, 8, 8, 8 = 39/50
- Governance and Project Management: 8, 8, 8, 8, 8 = 40/50
- Integration, Data, and Technical Approach: 8, 7, 8, 8, 8 = 39/50
- Security, Privacy, Compliance: 8, 7, 8, 8, 8 = 39/50
- Testing, Acceptance, and Handover: 8, 7, 8, 8, 8 = 39/50
- Support, Maintenance, and SLA: 8, 7, 8, 8, 8 = 39/50
- Relevant Experience: 8, 8, 8, 8, 7 = 39/50

All narrative sections cleared the 35/50 stopping condition. No section required revision after the initial pass. Em dashes were removed from narrative prose throughout; commas and periods are used instead. Technical adverbs (operationally, commercially, technically) were retained where they carry meaning. The formal third-person buyer-facing voice was preserved per the softened rules for the B2B register.

---

*End of proposal. This document is submitted with the completed Supplier Response Sheet (Excel) per Section 6 of the RFP. The optional PDF supporting document allowance (Section 8, not more than 5 pages) is addressed by the structured proposal above; the Response Sheet remains the authoritative response format and the completed tabs take precedence over any narrative summary here in case of conflict.*