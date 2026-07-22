# Airport Eye — APOC Phase 2 Enhancement Program
## Proposal in Response to DIAL's Business Requirement Document v1.5 and Associated Procurement Package

**Prepared for:** Delhi International Airport Limited (DIAL)
**Prepared by:** WAISL Limited
**Reference:** Concession Agreement between DIAL and WAISL Limited dated 30 September 2019; Business Requirement Document "Airport Eye — Integrated Digital Twin Platform" Version 1.0/1.5 (issued 05-June-2026); Additional Business Requirements & Use Cases (2-July-2026); Airport_Eye_RFP_v5; PE_OT System brief (09-June-2026)

---

## Source Note

**Drafted from (authoritative requirements, in order of precedence):**
1. Change Request — Airport Eye APOC Phase 2 (Business Requirement Document v1.5, issued 05-June-2026) — binding
2. Airport Eye Additional Business Requirements & Use Cases (2-July-2026)
3. PE_OT System brief, 09-June-2026 (final OT systems list at P&E DIAL)
4. Airport_Eye_RFP_v5
5. AirportEye_Requirements_Register_v5 and Final requirements.xlsx (delivery-month/phase detail)

**Used as bidder-capability evidence only (not as requirements):** AirportEye_Solution_Proposal_v9, DIAL APOC Phase II Proposal (Apr 2025), Airport_Eye_Consolidated_Proposal_FINAL, Airport Eye – Scope v5 infographic. Claims sourced from these are explicitly marked as evidence, not requirements.

**Excluded from this draft entirely:** AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT and its associated RTM_DRAFT were not opened and are not reflected anywhere in this document.

**Gaps due to source limitations:** BRD Appendices A (Schedule of Buildings), B (BEP Requirements) and D (Existing System Inventory) are marked in the source itself as "to be completed by DIAL." Commercial rate cards are blank templates in both the BRD and RFP. Several OT integration point-counts and a small number of AI-agent performance targets are not specified. These are flagged as placeholders throughout rather than invented.

---

## 1. Cover Letter

Delhi International Airport Limited
New Delhi

**Subject: Quotation for the Airport Eye — Integrated Digital Twin Platform, APOC Phase 2 Enhancement Program**

Dear Sir/Madam,

WAISL Limited, as the existing Concessionaire under the Concession Agreement executed with Delhi International Airport Limited on 30 September 2019, is pleased to submit this response to DIAL's request for the APOC Phase 2 Enhancement Program, known as Airport Eye. We acknowledge receipt of the Business Requirement Document Version 1.5 (issued 05-June-2026), the Additional Business Requirements & Use Cases document (2-July-2026), the PE_OT System brief (09-June-2026), and Airport_Eye_RFP_v5, and we confirm our understanding that the Business Requirement Document governs scope, sequencing, KPIs, and commercial framework wherever it differs from the base RFP, with the Additional Business Requirements treated as supplementary scope to be confirmed at solution-intent level during early-phase workshops.

We understand DIAL's ask as the evolution of the existing Airport Operations Control Centre into an enterprise-wide, intelligent Airport Digital Operations Platform: a survey-grade geospatial and BIM foundation, real-time BMS/IoT integration, and a suite of domain-specific AI monitoring agents, delivered as a federated Digital Twin covering Indira Gandhi International Airport and the Aerocity precinct. As the incumbent operator of APOC, we bring direct operating knowledge of the current systems landscape described in the PE_OT System brief and are well placed to close the integration gaps it documents.

We commit to delivering this program in accordance with the scope, phasing, KPIs, and Service Level Agreement targets set out in the Business Requirement Document, and we set out in this proposal how we intend to meet each of them. Where the source documents leave a requirement open — commercial rates, certain appendices, or a small number of AI-agent performance targets — we have said so explicitly rather than assume a position on DIAL's behalf.

We appreciate the opportunity to continue our partnership with DIAL on this strategic program and look forward to discussing this proposal further.

Yours sincerely,

*Authorised Signatory*
WAISL Limited

---

## 2. Executive Summary

Delhi International Airport Limited operates one of the world's busiest and most complex airport ecosystems, and its existing Airport Operations Control Centre has delivered real value in operational monitoring and stakeholder coordination since its inception. However, as the Business Requirement Document sets out, several domains — utilities, environmental monitoring, space and land management, and operational technology systems — continue to run on fragmented platforms with limited enterprise-wide integration and heavy reliance on manual processes. Growth in passenger traffic, expansion of infrastructure, and the maturing of digital twin, geospatial, and AI technologies now create the opportunity to close that gap and move APOC from a reactive monitoring tool to a predictive, and eventually prescriptive, operations platform.

Airport Eye is DIAL's response to that opportunity: a five-phase program building a survey-grade GIS-3D and BIM data foundation across the entire airport campus, integrating that foundation with all major Building Management Systems, SCADA platforms, and IoT sensor networks, and layering on top a suite of specialised AI agents that continuously monitor mechanical, electrical, fire-safety, water, energy, passenger-flow, structural, and security systems. The Additional Business Requirements captured from departmental workshops with Projects & Engineering, Security & Vigilance, Commercial Aero, Operations, and the Strategic Planning Group extend this further into simulation and "what-if" scenario planning, reverse-entry and unattended-baggage detection, and IoT-enabled environmental monitoring.

WAISL, as the existing Concessionaire responsible for APOC's day-to-day operation under the Concession Agreement of 30 September 2019, is uniquely positioned to deliver this program without the ramp-up risk a new entrant would carry. We already operate the systems the Business Requirement Document asks Airport Eye to integrate with, and our operational teams hold the institutional knowledge of DIAL's current OT estate — including which systems are already exposed through the existing Terminal 3 IT-BMS, which remain siloed, and which are subject to OEM-driven upgrade programs already under way. Our approach builds the geospatial and BIM foundation first, sequences BMS/IoT integration terminal-by-terminal starting with Terminal 3, and deploys the AI monitoring layer against a data foundation that has already been validated through user acceptance testing.

This proposal sets out our understanding of the requirement, our proposed solution architecture, a phased implementation plan aligned to the Business Requirement Document's five-phase structure and payment milestones, our approach to governance, security, testing, and support, and the commitments we are able to make against the Business Requirement Document's numeric KPIs and AI-agent performance standards. Where the source material leaves an item open — certain appendices, a handful of AI-agent targets, and all commercial rates — we say so plainly rather than fill the gap with assumption, consistent with the rigor DIAL should expect from an accountable delivery partner on a program of this strategic importance.

---

## 3. Understanding of Requirements

DIAL's vision for Airport Eye is to establish Indira Gandhi International Airport as a global benchmark for intelligent, data-driven airport operations by creating a living, spatially accurate digital replica of the airport ecosystem, including the Aerocity precinct. At the heart of that vision is a network of federated, AI-driven agents operating continuously that act as the airport's "digital eye" — continuously monitoring systems and infrastructure, detecting anomalies and emerging risks in real time, predicting operational disruptions, safety hazards and security threats, and providing actionable insight to enable proactive rather than reactive intervention.

We understand this vision to rest on six primary objectives set out in the Business Requirement Document: a comprehensive, survey-grade geospatial and BIM data foundation for the full campus; IFC-compliant, asset-rich BIM models to Level of Development 200–350 as applicable, fully ISO 19650-compliant; real-time, bi-directional integration with all existing and planned BMS, IoT, and OT platforms over standard industrial protocols; a suite of specialised AI monitoring agents; operational integration with APOC, CCC, and Smart City platforms via standardised APIs; and a scalable, cloud-native platform architected for a minimum fifteen-year operational lifecycle.

Behind these objectives sits an operational reality we know well as the current operator of APOC. The PE_OT System brief confirms that DIAL's operational technology estate is extensive but unevenly integrated: nineteen distinct OT system categories spanning HVAC/BMS, fire detection, vertical transport, electrical power monitoring, lighting control, passenger boarding bridges, visual docking guidance, water and sewage treatment SCADA, main receiving substation SCADA, baggage handling, tray-count SCADA, ground power/pre-conditioned air units, airside solar SCADA, and aeronautical ground lighting — the majority of which are explicitly noted as "not integrated with T3 ITBMS" today, with only a subset exposed through the existing IT-BMS interface, and several systems (VDGS, MRSS) already mid-upgrade with OEM-driven completion dates in March 2027. This is the integration debt Airport Eye Phases 3 and 4 are designed to retire, and it is a debt WAISL is already familiar with from day-to-day operation of the current platform.

The Additional Business Requirements gathered from departmental workshops confirm that the scope is not purely an engineering integration exercise. Projects & Engineering want borewell recharge and storm-water IoT monitoring; Security & Vigilance want reverse-entry detection, unattended-baggage detection, behaviour analytics, predictive security monitoring, and security asset mapping; Commercial Aero want satellite/GIS-based space-allocation analytics; Operations want low-visibility surface navigation, IT-systems monitoring across DigiYatra/E-Gates/CUSS/CUPPS, and identification of overstaying or unidentified passengers; and the Strategic Planning Group want a full simulation and "what-if" digital twin capability spanning commercial, operational, and engineering scenario modelling. We read these as an instruction that Airport Eye must be architected from the outset as an extensible platform, not a fixed set of dashboards, since several of these use cases (particularly the SPG simulation and decision-engine requirement) are described at a conceptual level and will need joint scoping to translate into buildable functional specifications.

We also note that the Business Requirement Document frames this engagement explicitly as a request to the existing Concessionaire under the Concession Agreement rather than as an open competitive procurement, while the base RFP (Airport_Eye_RFP_v5) carries a multi-vendor evaluation framework, weighted scoring, and a seven-volume submission structure. We treat the Business Requirement Document's framing as controlling per the stated precedence, and we flag this apparent inconsistency for DIAL's confirmation in Section 14 below rather than silently resolving it.

---

## 4. Proposed Solution

Airport Eye is proposed as a single, integrated platform delivered across the five phases defined in the Business Requirement Document, each building on the deliverables of the phase before it.

### 4.1 Geospatial and GIS-3D Environment (Phase 1)

The foundation layer is a survey-grade geospatial dataset covering the airport and Aerocity areas, runway and taxiway systems, aprons, cargo zones, and perimeter areas, plus a five-kilometre buffer beyond the airport boundary — an estimated 200 square kilometres in total. This is built from an airborne LiDAR survey at a minimum point density of 20 points per square metre within the airport boundary (8 points per square metre in buffer zones), horizontal accuracy of 5 cm RMSE and vertical accuracy of 3 cm RMSE verified against independently surveyed ground control points, RGB orthophotography at 5 cm ground sampling distance, classified point cloud data in ASPRS LAS 1.4 format, and DTM/DSM products at 10 cm grid resolution. Indoor coverage is delivered through mobile and terrestrial LiDAR scanning of all terminal buildings, satellite structures, VIP facilities, cargo warehouses, and maintenance hangars, registered to the airborne coordinate system to a minimum positional accuracy of 5 cm RMSE for seamless indoor-outdoor continuity.

### 4.2 GIS-BIM Integration (Phase 2)

Federated, IFC-compliant BIM models are developed for all built assets at the Level of Development specified against each building and asset category in the Business Requirement Document's LOD schedule (predominantly LOD 200 for landside/airside infrastructure and future-development buildings, LOD 350 for T1/T2/T3 building assets including MEP, PHE, HVAC, and concealed duct services, and LOD 350 for T2 MRSS/substation infrastructure), fully populated with asset attribute data — manufacturer specification, maintenance history, and warranty information — and imported into DIAL's CAFM/CMMS. Legacy CAD drawings are audited and migrated where BIM models do not yet exist, and findings are reconciled against the LiDAR survey.

### 4.3 Facilities Maintenance Application (Phase 3)

This phase links all existing Maintenance Management Systems — BMS, LCMS, ECMS, CMS, FDAS, BHS, HBS, VDGS, VHT, ATRS, DFMD, PBB, WTP/STP, and AGL CMS — into a single platform for both terminal and airside facilities, integrates the resulting model with APOC for monitoring (with control rights reserved for defined functions such as lighting on/off), and layers in environmental and pre-maintenance planning capability: terrain and hydrological assessment, noise-contour and flood-zone mapping, disaster-prone zone mapping with earthquake/wildfire/flood layers, and geospatial evacuation-route planning. IoT sensor integration for predictive maintenance builds on what is already deployed — 40 machine-room pump sensors across T1/T2/T3 monitoring acceleration, velocity, displacement, temperature, and current, 12 roof-drain water-level sensors in T1, and dissolved gas analysis in transformers for insulation-failure prediction — extended in a phased manner in line with project execution.

### 4.4 Digital Twin Platform (Phase 4)

The Digital Twin Platform is the operational core: a modular, cloud-native (or cloud-ready hybrid) web-based 3D GIS and BIM viewer supporting simultaneous display of GIS basemap, aerial imagery, point cloud, textured 3D mesh, and BIM geometry at all scales, with seamless indoor/outdoor navigation and automatic LOD management. Real-time BMS data is overlaid on corresponding BIM elements with colour-coded condition indicators, and the platform provides customisable dashboards, measurement and annotation tools, and task-assignment tools integrated with CAFM/CMMS, together with AR/VR output for maintenance and training use cases and full mobile responsiveness with offline capability for field teams.

Underneath the viewer sits an IoT/BMS ingestion middleware layer connecting to BACnet/IP, BACnet MSTP, Modbus TCP/RTU, MQTT (v3.1.1 and v5.0), SNMP, OPC-UA, RESTful APIs, and proprietary vendor connectors, normalising all ingested data into a unified semantic model conforming to the Digital Twin Definition Language or an equivalent open standard approved by DIAL. Every BMS data point is mapped to a corresponding BIM element for 3D spatial visualisation, with configurable geofencing, zone-level aggregation, and a minimum five-year historical data archive. APOC and CCC integration is delivered through standardised REST and GraphQL APIs with WebSocket support for event-driven feeds, all versioned with a minimum two-major-version backwards-compatibility commitment, alongside third-party airline and ground-handler system integration and national Smart City/urban-mobility platform integration as required by DIAL.

### 4.5 Agentic AI and Predictive Intelligence (Phase 5)

The AI Monitoring and Intelligence layer is the most transformative component of the platform, shifting APOC from reactive monitoring toward proactive and ultimately prescriptive operations. It is implemented as a suite of eight specialised, domain-specific AI agents — Mechanical & HVAC Monitoring, Electrical Systems Monitoring, Fire Safety & Life Safety Monitoring, Water & Drainage Monitoring, Energy Management & Sustainability, Passenger Flow Monitoring, Structural Integrity Monitoring, and Security & Perimeter Monitoring — each responsible for a defined category of airport systems and operating within a unified AI orchestration framework that manages data routing, alert aggregation, priority scoring, and cross-agent correlation; supports deployment, update, retirement, and versioning of individual agents without platform downtime; exposes a Model Management interface for DIAL's technical team to review performance, retrain models, and approve production updates; and enables cross-domain correlation via a common data bus. Section 5 and Section 11 of this proposal set out the specific per-agent numeric performance commitments the Business Requirement Document requires.

### 4.6 Outdoor 3D GIS Platform

A centralised, high-performance web-based 3D GIS viewer forms the geospatial backbone of Airport Eye, supporting LiDAR point clouds, orthophotos, terrain models, 3D mesh, and multi-scale visualisation, with multi-department data layering so different DIAL departments can upload and manage their own geospatial datasets (SHP, GeoJSON, KML, IFC, CAD overlays), planning and scenario visualisation to compare proposed against existing conditions, collaborative redlining and version control, secure link sharing and role-based export, and natural-language query capability for GIS data retrieval.

### 4.7 Spatial Decision and Simulation Capability (responding to the Additional Business Requirements)

The Strategic Planning Group's requirement for a dynamic "what-if" simulation capability is understood as a fourth logical layer sitting atop the Digital Twin and AI layers: a digital-twin simulation engine, a control-variable UI for scenario configuration, a decision engine, and a visualisation UI for outcomes — applied to the commercial, operational, and engineering use cases the Additional Business Requirements document illustrates (store-mix and shelf-merchandising optimisation, queue-versus-revenue trade-offs, passenger-flow and gate-allocation optimisation, HVAC and power-infrastructure stress-testing, and similar scenarios). Because the Additional Business Requirements describe this capability at use-case level rather than as a fully specified functional and data requirement, we treat detailed scoping of the simulation engine's data inputs, modelling techniques, and success criteria as an item for joint scoping workshops early in the program rather than a fixed deliverable we can commit to in full detail today — see Section 12.

### Differentiators

As the incumbent Concessionaire, WAISL already operates the APOC platform this program enhances, already holds the operational relationships with the OT system owners listed in the PE_OT brief, and already understands which of DIAL's systems are and are not exposed through the current T3 IT-BMS. This removes the discovery risk a new vendor would carry into Phase 1 and lets integration sequencing in Phases 3–4 start from a known baseline rather than a from-scratch audit.

---

## 5. Scope Coverage and Deliverables

The Business Requirement Document defines fifteen formal deliverables, each subject to DIAL's written sign-off within a fourteen-calendar-day review period from submission.

| Deliverable | Description |
|---|---|
| D-01 | Project Execution Plan, BIM Execution Plan (BEP), and Data Management Plan |
| D-02 | Airborne LiDAR point cloud (classified LAS/LAZ), DTM, DSM, and orthophoto datasets |
| D-03 | Geospatial accuracy assessment report and survey metadata |
| D-04 | Indoor LiDAR point cloud datasets (all buildings) |
| D-05 | IFC-compliant federated BIM models for all specified assets to agreed LOD |
| D-06 | Asset Attribute Data Register (fully populated, imported to CAFM/CMMS) |
| D-07 | Existing Data Migration Report and Legacy Data Quality Assessment |
| D-08 | Deployed and tested Digital Twin Platform (UAT sign-off) |
| D-09 | BMS/IoT Integration Report (all integrated data points verified) |
| D-10 | AI Monitoring and Predictive Intelligence Platform (all agents operational) |
| D-11 | API documentation portal and integration test reports |
| D-12 | Cybersecurity Assessment Report and Penetration Test Report |
| D-13 | Training Materials, User Manuals, and Administrator Documentation |
| D-14 | As-Built Documentation for all platform components |
| D-15 | Post-implementation review report (90 days after go-live) |

**In-scope, per the Business Requirement Document and Additional Business Requirements:**
- Airborne and indoor LiDAR survey, BIM modelling to specified LOD, and legacy CAD migration across T1, T2, T3, NUB buildings, cargo, ATCs/TBBs, ACLCs, and other listed structures
- BMS/IoT/SCADA integration across the systems enumerated in the PE_OT brief and BRD Appendix E (BMS, CMS, FDAS, BHS, HBS, VDGS, VHT, ATRS, DFMD, LCMS, ECMS, PBB, WTP/STP, AGL CMS)
- Digital Twin Platform, Outdoor 3D GIS Platform, and the eight-agent AI monitoring suite
- Department-specific use cases from the Additional Business Requirements (P&E IoT monitoring, S&V video-analytics use cases, Commercial Aero GIS analytics, Operations dashboards, SPG simulation capability)

**Assumed / requiring DIAL input before scope can be finalised:**
- BRD Appendix A (Schedule of Buildings and Areas), Appendix B (BEP Requirements), and Appendix D (Existing System Inventory) are marked in the source as "to be completed by DIAL" — full LOD-based costing and integration-point finalisation depend on these being issued
- Point counts for several OT systems (T1/T2 LCMS, several T2 systems recorded as "doesn't exist"/"not present" in the requirements register) require DIAL/OEM confirmation of deployment status before an integration commitment can be made

**Customer dependencies:** timely regulatory approvals for drone/LiDAR survey and underground utility scanning (RACI: Vendor Responsible, DIAL Accountable); access to existing utility drawings for LOD-350 areas; SME availability for asset-attribute and KPI validation; and DIAL sign-off turnaround within the stated 14-day review window to keep the payment-milestone schedule on track.

---

## 6. Implementation Methodology and Project Plan

Delivery follows the Business Requirement Document's five-phase structure, each phase approximately three months in duration, for a total program length of approximately fifteen months from mobilisation to final handover.

| Phase | Title | Key Activities | Duration |
|---|---|---|---|
| 1 | Mobilisation and Data Acquisition | Project initiation, DIAL approvals, airborne LiDAR acquisition, indoor scanning commencement, existing data audit | ~3 months |
| 2 | Spatial Data Processing and BIM Development | Point cloud processing, DTM/DSM generation, orthophoto production, BIM modelling of terminals and critical assets | ~3 months |
| 3 | Platform Development and BMS Integration | Digital Twin platform deployment, BMS data integration, IoT sensor onboarding, API development and testing | ~3 months |
| 4 | AI Agent Deployment and System Testing | AI monitoring agent deployment, APOC/CCC integration, User Acceptance Testing | ~3 months |
| 5 | Commissioning, Training, and Handover | Platform commissioning, staff training, operational handover, SLA commencement, warranty period begins | ~3 months |

Within that envelope, the requirements register sets out a more granular, terminal-prioritised rollout: an initial wave (delivery month 3) covering core T3 systems already exposed through the existing IT-BMS (VHT, PBB, VDGS, GPU/PCA), a second wave (month 5) covering T3 HVAC (first 4,000 of an estimated 54,000 points), ATRS, and WTP/STP SCADA, a third wave (month 8) covering T3 FDAS, ECMS, BHS, MRSS, and common IT-integration items (AODB/UTAM-adjacent feeds, ITOM, SAP asset data), and a final wave (month 12 and beyond) covering T1/T2 systems that require OEM upgrades or are not yet deployed. We propose T3 as the lead terminal given its scale and the maturity of its existing IT-BMS exposure, with T1 following and T2 sequenced last, consistent with the register's own phase markers and the PE_OT brief's confirmation that several T2 systems are not yet present or awaiting OEM works.

Mobilisation activities begin with joint discovery workshops to close the gaps left by BRD Appendices A, B, and D, followed by survey permitting, LiDAR acquisition, and parallel commencement of the Project Execution Plan, BIM Execution Plan, and Data Management Plan (D-01). Build and configuration activities in Phases 2–3 run BIM modelling and BMS/IoT integration in parallel workstreams, converging at Phase 4 for AI agent deployment against a validated data foundation. Phase 5 concludes with formal UAT sign-off, training delivery (D-13), as-built documentation (D-14), operational handover, and commencement of the twelve-month warranty and SLA period, with a 90-day post-implementation review (D-15) closing the initial delivery program.

---

## 7. Governance and Team Structure

Governance follows the Roles, Responsibilities, and RACI matrix set out in Section 5 of the Business Requirement Document, under which the Vendor holds Responsible status for project mobilisation, surveys, GIS-BIM integration, platform architecture, BMS/IoT integration, AI agent design and development, and day-to-day platform operations and AMC, while DIAL holds Accountable status throughout, with Smart City and DEC stakeholders consulted or informed depending on activity — Smart City in particular holds Accountable status for GPR/underground utility scanning, GIS data creation and QA, BIM modelling QA, and BMS/IoT data integration, reflecting its role as technical custodian of those domains. Alert thresholds, SOP definition, and AI model deployment approval sit with DIAL as Responsible/Accountable, with the Vendor in a Consulted capacity — a deliberate control point ensuring DIAL retains operational authority over what the AI layer is permitted to alert on and act on.

We propose a three-tier governance cadence: a quarterly executive steering session for strategic direction, relationship review, and change-request discussion; a monthly program review covering delivery progress, integration status, and SLA/KPI performance against the targets in Section 11; and a weekly operational working session for day-to-day execution tracking, escalation management, and action-item closure. *This cadence reflects WAISL's existing governance model for DIAL engagements, evidenced in prior WAISL–DIAL program proposals; the specific committee membership and reporting templates for Airport Eye are to be confirmed with DIAL at program mobilisation.*

Key delivery roles required for this program include a Program Director with overall accountability, a Digital Twin/Platform Architect, a BIM/Geospatial Lead for the survey and modelling workstream, a BMS/IoT Integration Lead, an AI/ML Lead responsible for the eight-agent suite and model governance, a Cybersecurity Lead responsible for IEC 62443 compliance and the SOC/SIEM function, and a Service Delivery Manager for the post-handover support organisation. *Named personnel and CVs are to be confirmed from bidder input — not specified in the selected source.*

---

## 8. Integration, Data, and Technical Approach

Integration is the single largest technical risk on this program, and our approach is built around the concrete OT estate documented in the PE_OT System brief and the requirements register rather than a generic middleware pitch.

**Current-state estate.** The PE_OT brief lists nineteen OT system categories across ASB, T1, T2, and T3: HVAC Building Management Systems (Honeywell at ASB, JCI at T1), Fire Detection & Alarm Systems (Notifire-by-Honeywell at ASB/T3, Edwards at T1/T2), a T3/T1 VHT IT-BMS (TKE, with JCI as integrator), Electrical Power Monitoring (ABB and Schneider Electric), Internal Lighting Control (KNX by ABB and Telematric), Passenger Boarding Bridges (JCI/TKE), Visual Docking Guidance (Safegate/TKE), WTP and STP PLC SCADA (Schneider), Main Receiving Substation SCADA (GE, AREVA-branded), Baggage Handling SCADA (Vanderlande), Automatic Tray Return SCADA (SJK, tray-count only), Ground Power Unit/Pre-Conditioned Air via Metasys (JCI), Airside Electrical SCADA for solar (Trinity, Locus), and Aeronautical Ground Lighting CMS (Honeywell). Critically, the brief records that the majority of these are "not integrated with T3 ITBMS" today, with a smaller subset exposed with limited points; VDGS is mid-upgrade from GOS to AIRPON software with a March 2027 target, and MRSS is mid-upgrade from GE to Schneider on the same timeline. Our integration plan treats these two upgrades as external dependencies outside our direct control and sequences their onboarding accordingly.

**Ingestion architecture.** All BMS/SCADA/IoT sources are connected through a middleware layer supporting BACnet/IP, BACnet MSTP, Modbus TCP/RTU, MQTT v3.1.1 and v5.0, SNMP, OPC-UA, RESTful APIs, and proprietary vendor connectors where an OEM does not expose a standard protocol. Ingested data is normalised into a unified semantic model conforming to the Digital Twin Definition Language (or an equivalent open standard subject to DIAL approval), with every data point mapped to a corresponding BIM element to support 3D spatial visualisation, configurable geofencing and zone-level aggregation, and a minimum five-year historical archive for all BMS streams.

**Representative integration scale.** The requirements register documents point counts that give a sense of scale for planning purposes: T3 HVAC at approximately 54,000 points (first 4,000 delivered within three months), T3 FDAS at approximately 65,000 points, T3 ECMS at approximately 66,000 tags, T1 HVAC and T3 MRSS each in the tens of thousands of points, and smaller but still substantial estates for BHS, ATRS, VDGS, PBB, and GPU/PCA. Several T2 systems are recorded in the register as not yet present or awaiting OEM delivery, which we treat as a DIAL/OEM-dependent scope item rather than a committed integration date.

**IT and operational-data integration.** Beyond OT, the register calls for integration with the AODB, UTAM, ADS-B, ARC, RMS, Kloudspot and XOVIS queue-analytics feeds, PTM transfer-passenger data, and IT-operations telemetry (ITOM/ManageEngine) as part of the broader OneAPOC program, plus SAP asset data and existing VMS/CCTV live feeds for display on the digital twin. Where the register marks a scope item as not yet defined — GSE telematics tracked-asset counts, the Security & Vigilance SAC integration point count — we carry that forward as an open item for Phase-1 discovery rather than assume a figure.

**APOC/CCC and platform APIs.** The Digital Twin Platform exposes standardised REST and GraphQL APIs with WebSocket support for real-time event-driven feeds to APOC and CCC, all versioned with a minimum two-major-version backwards-compatibility guarantee, plus integration with third-party airline/ground-handler systems and national Smart City platforms as required.

**Hosting and lifecycle.** The platform is architected as modular and cloud-native (or cloud-ready hybrid), designed for a minimum fifteen-year operational lifecycle as required by the Business Requirement Document. *Specific compute, storage, and disaster-recovery sizing is to be finalised jointly with DIAL once hosting-model preferences (public cloud, on-premises, or hybrid) are confirmed — not fully specified in the selected source.*

---

## 9. Security, Privacy, Compliance, and Quality Assurance

Security is designed around the Business Requirement Document's explicit OT/IT cybersecurity requirements. All OT/IT integration components will be compliant with IEC 62443, with network segmentation between IT, OT, and internet-facing components delivered through a defence-in-depth architecture, penetration testing of all internet-facing components prior to go-live, and a SOC/SIEM capability for continuous monitoring of platform security events, backed by a full cybersecurity risk assessment prior to deployment with findings submitted for DIAL approval.

Access control is built on multi-factor authentication and role-based access control with a minimum of five defined user roles — Executive, Operations, Maintenance, Security, and Guest/Visitor — with single sign-on integrated into DIAL's existing Identity Provider via SAML 2.0 or OAuth 2.0. All data in transit is encrypted using TLS 1.3 and all data at rest using AES-256, with full activity audit logging retained for a minimum of two years.

On data governance: all data generated, processed, or stored under this program — geospatial data, BIM models, IoT data, operational data, and AI models — remains the exclusive property of DIAL. We will not use DIAL data for purposes outside this contract, will not train or improve any external or third-party AI model using DIAL data, and will not transfer, store, or process DIAL data outside India without DIAL's prior written approval, consistent with the Business Requirement Document's data-ownership clause and the applicable provisions of the Digital Personal Data Protection Act, 2023. In the event of a cybersecurity incident or data breach, we will notify DIAL within twelve hours of detection, take immediate containment and remediation action, and bear the costs of recovery, legal, and reputational mitigation where the breach arises from our negligence or a vulnerability in our systems.

On AI governance specifically: every AI-generated alert will be accompanied by a plain-language explanation of contributing factors and a confidence score expressed as a percentage; a complete audit log of AI-generated alerts (input data, model version, timestamp, operator response) will be retained for a minimum of five years; operators will be able to submit feedback on alert accuracy for use in retraining; all model versions will be documented and retained with rollback to a previous version achievable within four hours; and DIAL will own all AI model weights and training data generated under this contract.

On quality: WAISL holds ISO 9001:2015 Quality Management System and ISO/IEC 27001:2013 Information Security Management certification — evidence from bidder capability material, and, per the base RFP's pre-qualification criteria, current certificates will need to be formally attached to the final submission. BIM deliverables are subject to ISO 19650 compliance and independent model audit against the 100% LOD-compliance KPI, and geospatial deliverables are subject to independent survey verification against the horizontal/vertical accuracy targets in Section 11.

---

## 10. Testing, Acceptance, and Handover

Every deliverable is subject to a formal fourteen-calendar-day DIAL review and written sign-off period from submission, and the Business Requirement Document ties this directly to the payment milestone schedule in Section 13. The Digital Twin Platform itself is gated by User Acceptance Testing at Milestone M4, with the UAT sign-off report as the acceptance instrument (deliverable D-08); AI agents are gated by Milestone M5, which requires all agents to be operational and performance benchmarks — the precision, recall, prediction-horizon, and alert-latency targets in Section 11 — to be met before commissioning is deemed complete (deliverable D-10).

Independent validation is built into the acceptance model: DIAL reserves the right to appoint independent auditors for BIM, geospatial, and AI-related KPIs, with BIM model audits conducted quarterly or at milestone, geospatial accuracy verified against independently surveyed benchmarks at milestone or annual cadence, and AI/ML performance evaluated through quarterly reports. A cybersecurity assessment and penetration test report (D-12) is a precondition of go-live for all internet-facing components. Final handover comprises complete as-built documentation (D-14), training materials, user manuals, and administrator documentation (D-13), followed by a formal ninety-day post-implementation review (D-15) that closes the initial delivery program and confirms readiness to transition into the warranty and SLA period.

---

## 11. Support, Maintenance, and SLA Approach

The following platform-level Service Level Agreement targets are set out in the Business Requirement Document (Section 2.3 and Appendix C) and are contractually binding on this engagement:

| # | KPI | Target | Measurement Basis | Reporting Frequency |
|---|---|---|---|---|
| 1 | Platform Uptime | ≥ 99.5% (excluding planned maintenance) | System availability/uptime monitoring logs | Monthly |
| 2 | Real-time Data Latency | ≤ 5 seconds, sensor to dashboard | System monitoring and data-pipeline logs | Monthly |
| 3 | BIM Model LOD Compliance | 100% of specified assets at agreed LOD | Independent model audit | Quarterly / milestone |
| 4 | Predictive Alert Accuracy | ≥ 80% precision, ≥ 75% recall | AI/ML performance evaluation report | Quarterly |
| 5 | Geospatial Data Accuracy | Horizontal ≤ 5 cm RMSE, Vertical ≤ 3 cm RMSE | Independent survey verification | Milestone / annual |
| 6 | Incident Response Time (Critical) | ≤ 10 minutes from notification | Incident management system logs | Monthly |
| 7 | System Integration Coverage | 100% of agreed BMS/IoT points within 3 months of go-live | Integration commissioning report | One-time (go-live + validation) |

Beneath this platform baseline, the Business Requirement Document sets granular per-agent performance standards for seven of the eight AI agents:

| Agent | Min. Precision | Min. Recall | Prediction Horizon | Alert Latency |
|---|---|---|---|---|
| Mechanical & HVAC Agent | ≥ 82% | ≥ 78% | Up to 72 hours | ≤ 30 seconds |
| Electrical Systems Agent | ≥ 80% | ≥ 75% | Up to 48 hours | ≤ 30 seconds |
| Passenger Flow Agent | ≥ 85% | ≥ 80% | Up to 45 minutes | ≤ 15 seconds |
| Structural Integrity Agent | ≥ 90% | ≥ 85% | Up to 7 days | ≤ 60 seconds |
| Fire Safety Agent | ≥ 95% | ≥ 95% | Real-time | ≤ 5 seconds |
| Energy Management Agent | ≥ 80% | ≥ 75% | Up to 24 hours | ≤ 60 seconds |
| Security Agent | ≥ 88% | ≥ 82% | Real-time / 15 min | ≤ 10 seconds |

*The Water & Drainage Monitoring Agent is named among the eight mandatory agents in Section 3.5.3 of the Business Requirement Document but does not appear in the numeric performance-standards table in Section 3.5.4 — this is a gap in the source itself. We propose the platform baseline (≥ 80% precision, ≥ 75% recall) apply to this agent pending DIAL's confirmation of an agent-specific target.*

Model governance commitments accompanying these targets include explainability with a confidence score on every alert, a five-year audit-log retention for all AI-generated alerts, an operator feedback loop feeding model retraining, and model rollback to a previous version achievable within four hours.

**Warranty and ongoing support.** The base RFP specifies a minimum twelve-month warranty period from formal platform handover, during which defects, errors, and non-conformances are remedied at no additional cost, followed by a structured Annual Maintenance Contract for the full five-year Operations and Maintenance term costed in the commercial framework. The Business Requirement Document does not itself state a warranty duration, so we adopt the RFP's twelve-month figure as the operative commitment, subject to DIAL's confirmation that this is not superseded elsewhere in the Concession Agreement.

**Non-compliance and escalation.** All KPIs above are contractually binding and linked to service-level compliance; non-compliance may attract financial penalties or service credits under the final SLA (Appendix C), three or more breaches in a quarter are treated as a material default, and persistent non-performance may result in termination at DIAL's discretion. SLA performance is reviewed in the monthly governance cadence described in Section 7, with monthly SLA reports, quarterly AI/analytics performance reports, milestone-based integration and commissioning reports, and periodic BIM/geospatial audit reports as the standing reporting package.

**Exit and transition.** On expiry or termination, we will provide complete handover of all deliverables, source code, configurations, and documentation, ensure knowledge transfer to DIAL or its nominated agency, and provide a minimum six months of transition support at no additional cost unless otherwise explicitly agreed.

---

## 12. Assumptions, Dependencies, and Exclusions

- BRD Appendices A (Schedule of Buildings and Areas), B (BIM Execution Plan Requirements), and D (Existing System Inventory) are marked "to be completed by DIAL" in the source document; firm LOD-based BIM pricing and a fully reconciled integration point-count depend on DIAL issuing these.
- The VDGS upgrade (GOS to AIRPON software) and the MRSS upgrade (GE to Schneider), both targeted for completion in March 2027 per the PE_OT brief, are OEM/DIAL-led workstreams outside our control; our integration sequencing treats their completion as an external dependency rather than a date we can commit to independently.
- Several T2 OT systems are recorded in the requirements register as "doesn't exist" or "not present" (T2 ECMS, VDGS, LCMS, BHS, ATRS, GPU/PCA among them); we cannot integrate a system that has not been deployed, and treat T2 scope as contingent on DIAL/OEM confirmation of deployment plans.
- The GSE telematics tracked-asset count and the Security & Vigilance SAC integration scope/point count are recorded in the requirements register as "to be confirmed" — these will be resolved in Phase-1 discovery workshops.
- The Strategic Planning Group's simulation and "what-if" decision-engine requirement is described at use-case level in the Additional Business Requirements rather than as a fully specified functional and data requirement; we assume joint scoping workshops in early Phase 1/Phase 2 will translate the illustrative use cases into a buildable specification.
- Regulatory approvals for drone-based LiDAR survey and underground utility (GPR) scanning are Vendor-responsible to obtain but are subject to third-party regulator timelines (BCAS, AAI, and other applicable authorities) that are outside our direct control.
- Availability of DIAL subject-matter experts for asset-attribute validation, KPI sign-off, and UAT participation is assumed at the cadence needed to hold the fourteen-day deliverable review window and the milestone schedule in Section 13.
- Cloud/on-premises/hybrid hosting model, and associated compute/storage/DR sizing, is assumed to be confirmed jointly with DIAL early in Phase 1; specific infrastructure costs in Section 13 are commercial-framework placeholders pending that decision.
- GST rate applicable to this contract is not specified in the source and is excluded from all cost figures pending confirmation.

---

## 13. Commercial Response or Pricing Narrative

Both the Business Requirement Document's Commercial Costing Framework and the base RFP's equivalent Section 10 present the same eight-part cost structure as blank rate-card templates, to be completed in Indian Rupees exclusive of GST: (1) Outdoor Airborne LiDAR Scanning and Data Preparation, (2) Indoor Scanning and BIM Modelling by LOD band, (3) Existing Data Preparation and Legacy CAD Migration, (4) BIM-to-BMS Integration, (5) Digital Twin Viewer Platform, (6) Agentic-AI Platform, (7) Infrastructure (compute, storage, network, disaster recovery, cybersecurity, middleware), and (8) a five-year Operations and Maintenance plan split by year into COTS software and human-resource cost. **Commercials will be provided in the prescribed pricing format / commercial envelope** once the open items in Section 12 — particularly the unpopulated BRD appendices and the hosting-model decision — are resolved with DIAL, consistent with the rate-card structure both source documents require rather than a free-form quotation.

Payment is milestone-linked per the Business Requirement Document's Section 7 schedule, which is identical to the base RFP's Section 9.4 table:

| Milestone | Description | Trigger / Acceptance Condition | % of Contract |
|---|---|---|---|
| M1 | Contract Award and Mobilisation | Signed contract, project plan accepted | 15% |
| M2 | LiDAR Data Acquisition Complete | Raw data delivered and DIAL-verified | 10% |
| M3 | BIM Models and Spatial Data Deliverables Accepted | Written sign-off by DIAL | 20% |
| M4 | Digital Twin Platform — UAT Passed | UAT sign-off report accepted | 25% |
| M5 | AI Agents Deployed and Commissioned | All agents operational, performance benchmarks met | 20% |
| M6 | Final Handover and Post-Implementation Review | 90-day post-go-live review accepted | 10% |

Proposal validity is a minimum of 180 calendar days from the submission deadline per the base RFP, extendable by mutual agreement. All commercial figures will be exclusive of GST, with GST added separately at the applicable rate once confirmed.

---

## 14. Deviations, Clarifications, and Contractual Notes

| # | Item | Source | Note |
|---|---|---|---|
| DC-01 | Procurement mechanism conflict | BRD frames this as an EOI/quotation request to the existing Concessionaire under the Concession Agreement; the base RFP carries a full multi-vendor evaluation framework (weighted scoring, seven submission volumes, pre-qualification criteria) | We have followed the BRD's incumbent/sole-source framing as controlling per the stated document precedence, but request DIAL's written confirmation of which procurement mechanism governs this engagement |
| DC-02 | ABR issued after stated response window | BRD cover page references dates of 05-June-2026 and 15-June-2026; the Additional Business Requirements document is dated 2-July-2026 | Requests confirmation of the revised submission timeline and whether ABR scope is priced within this response or handled as a subsequent change request |
| DC-03 | Water & Drainage Agent performance target | BRD Section 3.5.3 (agent list) vs. 3.5.4 (performance table) | Not specified for this agent in the performance table; we propose the platform baseline (≥80% precision / ≥75% recall) pending DIAL confirmation — see Section 11 |
| DC-04 | Warranty period | Not stated in the BRD; sourced from base RFP Section 9.5 (12 months from handover) | Requests DIAL confirmation that the RFP's warranty term applies and is not superseded by the Concession Agreement |
| DC-05 | Performance security / bank guarantee | Not specified in either the BRD or the base RFP beyond a general reference to Concession Agreement terms | Form and value to be confirmed |
| DC-06 | GST rate | Left blank in both commercial costing tables | To be confirmed for the final commercial submission |
| DC-07 | Appendices A, B, D | BRD/RFP Appendices A (Schedule of Buildings), B (BEP Requirements), D (Existing System Inventory) marked "to be completed by DIAL" | Required before firm LOD-based pricing and full integration-scope finalisation |

---

## 15. Relevant Experience, Case Studies, and Evidence

WAISL is the existing Concessionaire responsible for the operation of APOC at Indira Gandhi International Airport under the Concession Agreement dated 30 September 2019 — this is a direct fact from the selected requirements source, not bidder marketing material, and it is the basis of our claim to reduced mobilisation and discovery risk on this program.

As supporting capability evidence (drawn from WAISL's own prior proposal collateral for DIAL and marked accordingly, not from the BRD/RFP): WAISL's AIOP operational-intelligence platform is reported to be live in production at Rajiv Gandhi International Airport, Hyderabad, integrating more than 40 systems and surfacing more than 100 KPIs. WAISL is reported to hold ISO 9001, ISO/IEC 20000, ISO/IEC 27001, and ISO 22301 certification, and a prior WAISL proposal for DIAL's APOC Phase II program describes an existing three-tier (L1/L2/L3) support model with defined priority-based response and resolution targets (for example, Priority-1 critical incidents at a 30-minute response and 4-hour resolution target) and an established quarterly/monthly/weekly governance cadence between WAISL and DIAL leadership. *These figures are indicative capability evidence from bidder collateral and should be independently re-verified and formally re-attached (current certificates, reference letters, audited financials) before this proposal is finalised for submission, per the base RFP's Appendix E pre-qualification requirements.*

Geokno is identified in WAISL's prior Airport Eye collateral as the proposed geospatial/BIM delivery partner for the LiDAR survey and BIM modelling workstreams; the specific partnership terms for this program are to be confirmed from bidder input.

Two further airport or comparable large-scale digital-twin case studies are required under the base RFP's Appendix E (a minimum of three case studies). Beyond the Rajiv Gandhi International Airport reference above, additional case studies were not available in the selected evidence collateral and are marked here as **to be confirmed from bidder input** rather than invented.

---

## 16. Appendices / Mandatory Forms / Compliance Tables

### Appendix D (populated) — Existing System Inventory, per the PE_OT System brief (09-June-2026)

| # | System | Location | OEM | OT Owner | Current Integration Status |
|---|---|---|---|---|---|
| 1 | HVAC Building Management System (BMS_ASB) | ASB | Honeywell | Ishan Verma | Not integrated with T3 ITBMS |
| 2 | Fire Detection & Alarm System (FDAS_ASB) | ASB | Notifire by Honeywell | Ishan Verma | GUI available on ITBMS (limited points) |
| 3 | Fire Detection & Alarm System (FDAS_CMS_PTB3) | Terminal 3 | Notifire by Honeywell | Manish Singh | GUI available on ITBMS (limited points) |
| 4 | HVAC Central Monitoring System (HVAC_CMS_PTB3) | Terminal 3 | Honeywell | Manish Singh | Not integrated with T3 ITBMS |
| 5 | VHT ITBMS | Terminal 3 & 1 | TKE (JCI as integrator) | Sumit Vaish | GUI available on ITBMS (T3 only) |
| 6 | Electrical Power Monitoring System (ECMS_PTB3) | Terminal 3 & 1 | ABB & Schneider Electric | Bikash Parida / Priyaranjan Ray | GUI available on ITBMS (T3 only, used for post-paid billing) |
| 7 | Internal Lighting CMS (LCMS_PTB3) | Terminal 3 & 1 | KNX by ABB & Telematric | Bikash Parida / Priyaranjan Ray | Not integrated with T3 ITBMS |
| 8 | PBB | Terminal 1, 2, 3 | JCI (integrator) & TKE | Sumit Vaish | GUI available on ITBMS (T3 only); managed by DIAL IT |
| 9 | VDGS ITBMS | Terminal 3 & 1 | Safegate & TKE | Sumit Vaish | GUI on ITBMS (T3 only); GOS→AIRPON upgrade ongoing, target Mar-2027 |
| 10 | Fire Detection & Alarm System (FDAS_CMS_PTB3) | Terminal 1 & 2 | Edwards | Naveen Saini | Not integrated with T3 ITBMS |
| 11 | HVAC Building Management System (HVAC_BMS_T1) | Terminal 1 | JCI | Naveen Saini | Not integrated with T3 ITBMS |
| 12 | UGR3 / WTP PLC SCADA | WTP | Schneider | Anil Kumar Madineni | Not integrated with T3 ITBMS |
| 13 | STP PLC SCADA | STP | Schneider | Anil Kumar Madineni | Not integrated with T3 ITBMS |
| 14 | MRSS SCADA | MRSS | GE (AREVA-branded) | Atul Kumar Singh / Priyaranjan Ray | Not integrated; awaiting MRSS server upgrade; GE→Schneider, target Mar-2027 |
| 15 | Baggage Handling System (BHS) SCADA | Terminal 1 & 3 | Vanderlande | Sumit Vaish | Not integrated with T3 ITBMS |
| 16 | ATRS SCADA (tray count only) | Terminal 1 & 3 | SJK | Sumit Vaish | Not integrated with T3 ITBMS |
| 17 | GPU & PCA System via Metasys | Terminal 1 & 3 | JCI | Isaac Clive | GUI available on ITBMS (T1 & T3, used for billing) |
| 18 | Airside Electrical SCADA (Solar) | Airside R/W 11R/29L | Trinity (2.84 MW) / Locus (5 MW) | Anand | Not integrated with T3 ITBMS |
| 19 | AGL CMS | Airside ESU 3 | Honeywell | Nitesh Rajkondawar | Not integrated with T3 ITBMS |

### Submission structure cross-reference

The base RFP requests a seven-volume submission (Executive Summary; Technical Proposal; AI and Analytics Proposal; Implementation Plan; Commercial Proposal; Qualifications and References; Appendices). This proposal is organised as a single consolidated document; for a formal submission package it maps as follows: Volume 1 → Section 2; Volume 2 → Sections 3, 4, 8; Volume 3 → Sections 4.5, 4.7, 11; Volume 4 → Sections 6, 10; Volume 5 → Section 13; Volume 6 → Section 15; Volume 7 → this Appendix and Sections 9, 12, 14.

### Pre-qualification checklist (base RFP Appendix E)

| Criterion | Status |
|---|---|
| Minimum 5 years' experience in digital twin/BIM/geospatial platform development | Evidence supports this via existing APOC operating role; formal write-up to be confirmed |
| At least 2 comparable airport/infrastructure deployments | 1 evidenced (RGIA Hyderabad); 2nd and 3rd case studies to be confirmed from bidder input |
| ISO 9001:2015 | Evidenced from bidder collateral; current certificate to be attached |
| ISO/IEC 27001:2013 | Evidenced from bidder collateral; current certificate to be attached |
| Audited turnover threshold | Not specified in selected source (blank in RFP); to be confirmed from bidder input |
| No pending insolvency/adverse legal action | To be confirmed from bidder input |

**— END OF PROPOSAL —**
