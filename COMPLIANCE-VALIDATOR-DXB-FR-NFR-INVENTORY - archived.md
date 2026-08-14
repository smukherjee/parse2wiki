# DXB 3D Digital Twin RFP — Functional & Non-Functional Requirements Inventory

**Source Document:** `3D_DigitalTwin_AirportOperations_RFP_SoW_DraftCopy.docx.md`  
**Extraction Date:** 2026-08-10  
**Status:** Step 1 - Compliance Requirements Extraction

---

## Coverage Summary

| Category | Count |
|---|---|
| **Functional Requirements (FR)** | 42 |
| **Non-Functional Requirements (NFR)** | 38 |
| **Categorical/Submission Requirements** | 15 |
| **Total Extracted** | **95** |

---

## FUNCTIONAL REQUIREMENTS (FRs)

| ID | Requirement Text | Category | Modal Verb | Mandatory/Scored | Scope Tier | Domain Hint | Applies To | Source Section | Notes |
|---|---|---|---|---|---|---|---|---|---|
| FR-001 | The platform shall use Unreal Engine as the 3D visualization tool for providing users with a seamless experience through a detailed 3D model of the airport | Functional | shall | M | base | visualization | Digital Twin Platform | 4. Technical Capabilities | Core visualization requirement |
| FR-002 | Users shall be able to visualize different layouts, customize views, and analyze data within the 3D environment | Functional | shall | M | base | visualization | Digital Twin Platform | 4. Technical Capabilities | Interactive visualization capability |
| FR-003 | The platform shall integrate smoothly with change management processes to support collaboration on layout changes | Functional | shall | M | base | visualization | Digital Twin Platform | 4. Technical Capabilities | Collaboration & change management |
| FR-004 | The platform shall serve as the single operational source of visualization for approved airport operational scenarios | Functional | shall | M | base | visualization | Digital Twin Platform | 4. Technical Capabilities | SSOV (Single Source of Truth) principle |
| FR-005 | The platform shall correlate, harmonize, and visualize inputs from LiDAR, video analytics, and backend systems in a common Digital Twin environment | Functional | shall | M | base | integration | Digital Twin Platform | 4. Technical Capabilities | Multi-source data harmonization |
| FR-006 | The platform shall support ingestion, normalization, stitching, and harmonization of multi-source data through a canonical airport data and event model | Functional | shall | M | base | integration | System Integration | 4. Technical Capabilities | Canonical data model requirement |
| FR-007 | The platform shall include a canonical airport data model covering key entities: flights, passengers, bags, queues, stands, gates, assets, incidents, alerts, timestamps, and location references | Functional | shall | M | base | integration | Data Model | 4. Technical Capabilities | Named entity set in canonical model |
| FR-008 | The platform shall provide real-time monitoring capabilities for passenger flow across all key airport touchpoints | Functional | shall | M | base | monitoring | Real-Time Monitoring | 5a. Real-Time Monitoring | Core operational visibility |
| FR-009 | The platform shall provide live situational awareness across landside, terminal, transfer, concourse, boarding, arrivals, baggage, and related operational domains | Functional | shall | M | base | monitoring | Real-Time Monitoring | 5a. Real-Time Monitoring | Comprehensive domain coverage |
| FR-010 | The platform shall enable detection of emerging constraints and prediction of downstream problems before they materialize | Functional | shall | M | base | analytics | Predictive Analytics | 5a. Real-Time Monitoring | Predictive capability requirement |
| FR-011 | The platform shall integrate data from existing Xovis sensors alongside Camera/CCTV and LiDAR to strengthen passenger-flow visibility | Functional | shall | M | base | integration | Sensor Integration | 5a. Real-Time Monitoring | Specific sensor integration mandate |
| FR-012 | The platform shall support continuous real-time visibility of passenger flow across key airport touchpoints and processes | Functional | shall | M | base | monitoring | Passenger Flow | 5a. Real-Time Monitoring | Continuous operational visibility |
| FR-013 | The platform shall accurately track activities including runway, taxiway, stand occupancy, baggage movements, passenger journey progression, and service level conditions | Functional | shall | M | base | monitoring | Activity Tracking | 5a. Real-Time Monitoring | Multi-domain activity tracking |
| FR-014 | The platform shall support real-time monitoring of facilities, weather, NOTAM data, and relevant stakeholder-wide operational systems | Functional | shall | M | base | monitoring | Facility & Weather Monitoring | 5a. Real-Time Monitoring | External data source integration |
| FR-015 | The platform shall detect emerging bottlenecks and forecast passenger volumes across key touchpoints | Functional | shall | M | base | analytics | Forecasting | 5a. Real-Time Monitoring | Volume forecasting requirement |
| FR-016 | The platform shall provide actionable recommendations for proactive intervention before service level degradation occurs | Functional | shall | M | base | decision-support | Operational Recommendations | 5a. Real-Time Monitoring | Decision-support capability |
| FR-017 | The platform shall contain extensive what-if simulation capabilities allowing users to model potential implications of various changes in airport operations | Functional | shall | M | base | simulation | What-If Simulation | 4. Technical Capabilities | Scenario modeling requirement |
| FR-018 | The platform shall enable testing of scenarios involving passenger demand surges, congestion, operational model changes, resource restrictions, and infrastructure adjustments | Functional | shall | M | base | simulation | Scenario Testing | 4. Technical Capabilities | Specific scenario set |
| FR-019 | The platform shall support integration with the Genetec SDK to enable recorded video playback and synchronized incident review | Functional | shall | M | base | integration | Video Integration | 4. Technical Capabilities | Third-party SDK integration |
| FR-020 | The platform shall provide data playback features to review past events with full Digital Twin visualization and recorded footage | Functional | shall | M | base | playback | Historical Data Analysis | 4. Technical Capabilities | Time-machine / historical playback |
| FR-021 | The platform shall support playback, backtracking, and fast-forward capabilities to help users understand how situations evolved | Functional | shall | M | base | playback | Temporal Navigation | 4. Technical Capabilities | Temporal navigation requirement |
| FR-022 | The platform shall use Unreal assets provided by Dubai Airports where available; otherwise build required 3D assets from scratch | Functional | shall | M | base | 3d-modeling | 3D Asset Development | 4. Technical Capabilities | Asset sourcing rules |
| FR-023 | The platform shall provide governed management of spatial models, zone definitions, asset hierarchies, sensor geometry, calibration references, and operational metadata | Functional | shall | M | base | governance | Data Governance | 4. Technical Capabilities | Metadata & version control |
| FR-024 | The platform shall support version control and controlled change management of the Digital Twin representation | Functional | shall | M | base | governance | Version Control | 4. Technical Capabilities | Change tracking requirement |
| FR-025 | The platform shall provide a canonical airport data model and event model to harmonize key entities across integrated systems | Functional | shall | M | base | data-model | Data Harmonization | 4. Technical Capabilities | Canonical model mandate |
| FR-026 | The platform shall support stitching/merging of data from various sources | Functional | shall | M | base | integration | Data Fusion | 4. Technical Capabilities | Multi-source data fusion |
| FR-027 | The platform shall provide a governed low-code framework capability to configure and maintain business rules, workflow logic, alert thresholds, and decision paths | Functional | shall | M | base | workflow-engine | Business Rules Engine | 4. Technical Capabilities | Low-code configurability |
| FR-028 | The platform shall support role-based administration, version control, auditability, and full customization to Dubai Airports' operating model | Functional | shall | M | base | governance | Access Control | 4. Technical Capabilities | RBAC requirement |
| FR-029 | The platform shall provide an operational conversational assistant similar to ChatGPT for natural-language querying of operational data | Functional | shall | M | base | ai-assistant | Conversational AI | 4. Technical Capabilities | Natural language interface |
| FR-030 | The conversational assistant shall support natural-language search across approved operational data, operational status questions, and contextual summaries | Functional | shall | M | base | ai-assistant | AI Query Capability | 4. Technical Capabilities | NLP query support |
| FR-031 | The platform shall provide multi-channel information sharing capabilities to present and share operational information across videowalls, desktops, laptops, tablets, and mobile devices | Functional | shall | M | base | distribution | Multi-Channel Distribution | 4. Technical Capabilities | Device coverage requirement |
| FR-032 | The platform shall ensure the same operational information is consumable in role-based formats across all channels | Functional | shall | M | base | distribution | Role-Based Formatting | 4. Technical Capabilities | Format consistency across channels |
| FR-033 | The platform shall support simultaneous distribution of critical alerts and disruption updates to mobile devices and videowalls | Functional | shall | M | base | distribution | Alert Distribution | 4. Technical Capabilities | Critical alert routing |
| FR-034 | The platform shall integrate with Microsoft Teams, WhatsApp, SMS, Outlook, and other approved productivity tools to communicate operational alerts | Functional | shall | M | base | integration | Communication Integration | 4. Technical Capabilities | Named communication channels |
| FR-035 | The platform shall provide real-time airport operations monitoring capability continuously managing passenger flow across all key touchpoints | Functional | shall | M | base | monitoring | AOCC Monitoring | 5a. Real-Time Monitoring | 24/7 operational visibility |
| FR-036 | The platform shall detect abnormal flow conditions and disruption triggers requiring immediate operational response | Functional | shall | M | base | monitoring | Anomaly Detection | 5a. Real-Time Monitoring | Exception identification |
| FR-037 | The platform shall provide accurate real-time visibility of queue length, wait time, throughput, and congestion levels using Xovis data | Functional | shall | M | base | monitoring | Queue Management | 5b. Queue Management | Queue KPI requirement |
| FR-038 | The platform shall establish an automated alert mechanism notifying security and operations teams of sudden increases in crowd levels | Functional | shall | M | base | alerting | Crowd Alert System | 5b. Queue Management | Alert automation |
| FR-039 | The platform shall provide curb-to-gate passenger journey tracking using integrated Camera/CCTV, LiDAR, and Xovis sensor data | Functional | shall | M | base | tracking | End-to-End Tracking | 5e. Passenger Tracking | Journey continuity requirement |
| FR-040 | The platform shall identify journey breaks, abnormal dwell, route deviations, and missed handoffs requiring operational intervention | Functional | shall | M | base | tracking | Exception Detection | 5e. Passenger Tracking | Journey exception tracking |
| FR-041 | The platform shall provide near real-time visibility of baggage flow across check-in, make-up, transfer, sortation, reclaim, and exception-handling processes | Functional | shall | M | base | monitoring | Baggage Tracking | 5c. Baggage Visibility | Baggage journey coverage |
| FR-042 | The platform shall provide disruption management capability to detect, assess, classify, coordinate, and manage operational disruptions in real time | Functional | shall | M | base | disruption-management | Disruption Management | 5d. Disruption Management | Disruption orchestration |

---

## NON-FUNCTIONAL REQUIREMENTS (NFRs)

| ID | Requirement Text | Category (NFR Type) | Modal Verb | Mandatory/Scored | Scope Tier | Domain Hint | Applies To | Source Section | Notes |
|---|---|---|---|---|---|---|---|---|---|
| NFR-001 | The platform shall provide low-latency integration capability across disparate airport systems and data domains | Performance | shall | M | base | latency | System Integration | 4. Technical Capabilities | Latency requirement (unspecified threshold) |
| NFR-002 | The platform shall support real-time operational visibility, historical analysis, forecasting, and simulation with minimal latency | Performance | shall | M | base | latency | Data Processing | 4. Technical Capabilities | Multi-mode latency requirement |
| NFR-003 | The platform shall include source-health monitoring, stale-feed detection, and data quality checks | Reliability | shall | M | base | data-quality | Data Quality | 4. Technical Capabilities | Data integrity requirement |
| NFR-004 | The platform shall provide confidence indicators and explainability of derived alerts, forecasts, and recommended actions | Reliability | shall | M | base | explainability | Decision Support | 4. Technical Capabilities | Transparency requirement |
| NFR-005 | The platform shall support open and governed data exchange through APIs, ESB, event streams, files, and other agreed mechanisms | Interoperability | shall | M | base | interoperability | Data Exchange | 4. Technical Capabilities | Multi-protocol requirement |
| NFR-006 | The platform shall maintain compliance with applicable security, privacy, data governance, and interoperability requirements | Security | shall | M | base | security | Compliance | 4. Technical Capabilities | Compliance mandate |
| NFR-007 | The platform shall demonstrate high accuracy of real-time passenger counting in designated monitored areas | Accuracy | shall | M | base | accuracy | People Counting | 5a. Use Cases | Accuracy requirement (% unspecified) |
| NFR-008 | The platform shall provide reliable visibility of crowd size, density, and occupancy conditions across key passenger-processing areas | Reliability | shall | M | base | reliability | Crowd Management | 5a. Use Cases | Occupancy monitoring reliability |
| NFR-009 | The platform shall provide timely alerts for threshold breaches, abnormal crowd build-up, and other crowd conditions | Latency | shall | M | base | latency | Alerting | 5a. Use Cases | Alert timeliness (unspecified SLA) |
| NFR-010 | The platform shall provide improved visibility of seat occupancy, waiting-area utilization, and monitored passenger holding zones | Visibility | shall | M | base | visibility | Occupancy Monitoring | 5a. Use Cases | Occupancy data visibility |
| NFR-011 | The platform shall demonstrate high accuracy in monitoring the availability and location of baggage trolleys across the airport | Accuracy | shall | M | base | accuracy | Baggage Systems | 5c. Use Cases | Trolley tracking accuracy (% unspecified) |
| NFR-012 | The platform shall achieve at least 99% accuracy in detecting and classifying vehicles at curbside areas | Accuracy | shall | M | base | accuracy | Curbside Monitoring | 5a. Use Cases | Explicit accuracy threshold: ≥99% |
| NFR-013 | The platform shall demonstrate at least 99% accuracy in vehicle dwell-time monitoring and lane occupancy detection | Accuracy | shall | M | base | accuracy | Vehicle Monitoring | 5a. Use Cases | Explicit accuracy threshold: ≥99% |
| NFR-014 | The platform shall achieve at least 99% detection accuracy for unattended baggage in monitored areas | Accuracy | shall | M | base | accuracy | Security Systems | 5b. Security | Explicit accuracy threshold: ≥99% |
| NFR-015 | The platform shall demonstrate at least 90% accuracy in replicating real-world operational scenarios within the airport environment | Accuracy | shall | M | base | accuracy | Simulation | 5d. Simulation | Scenario accuracy threshold: ≥90% |
| NFR-016 | The platform shall achieve at least 99% accuracy in counting footfall across key commercial and passenger areas | Accuracy | shall | M | base | accuracy | Commercial Analytics | 5f. Use Cases | Footfall accuracy threshold: ≥99% |
| NFR-017 | The platform shall support at least 99% accuracy in real-time passenger tracking and movement continuity | Accuracy | shall | M | base | accuracy | Passenger Tracking | 5e. Passenger Tracking | Tracking accuracy threshold (implicit) |
| NFR-018 | The platform shall be treated as a Tier 1 operational service aligned to Dubai Airports' security, governance, hosting, and resilience expectations | Availability | shall | M | base | resilience | Service Tier | 3. Scope | Tier 1 SLA requirement |
| NFR-019 | The platform shall be designed with no single point of failure across critical components | Reliability | shall | M | base | resilience | System Architecture | 14. Non-Functional Requirements | High-availability architecture |
| NFR-020 | The platform shall propose a disaster recovery approach covering recovery architecture, failover, and failback | Recoverability | shall | M | base | resilience | Disaster Recovery | 14. Non-Functional Requirements | DR/BC requirement |
| NFR-021 | The platform shall achieve target recovery time objective (RTO) and target recovery point objective (RPO) to be determined | Recoverability | shall | M | base | resilience | Recovery Objectives | 14. Non-Functional Requirements | RTO/RPO requirement (values pending) |
| NFR-022 | The platform shall support scaling for additional terminals, concourses, use cases, sensors, and data sources without requiring material redesign | Scalability | shall | M | base | scalability | Architecture | 14. Non-Functional Requirements | Horizontal scalability |
| NFR-023 | The platform shall provide a governed low-code business rule engine enabling authorized users to configure business rules without major redevelopment | Maintainability | shall | M | base | maintainability | Workflow Engine | 4. Technical Capabilities | Low-code configurability |
| NFR-024 | The platform shall support version control, auditability, and role-based permissions for all configuration changes | Auditability | shall | M | base | auditability | Change Tracking | 4. Technical Capabilities | Change audit trail |
| NFR-025 | The platform shall comply with Dubai Airports' Information Security Requirements (ISR) and Cybersecurity policy | Security | shall | M | base | security | Security | 13. Security Requirements | ISR compliance mandate |
| NFR-026 | The platform shall provide multiple hosting/deployment options: on-premise, cloud, hybrid | Deployment | shall | M | base | deployment | Infrastructure | 12. Hosting Requirements | Deployment flexibility |
| NFR-027 | The platform shall provide role-based access controls with device-appropriate views for different stakeholder groups | Security | shall | M | base | security | Access Control | 4. Technical Capabilities | RBAC across stakeholders |
| NFR-028 | The platform shall ensure that operational information is consumable in role-based formats across channels simultaneously | Usability | shall | M | base | usability | Multi-Channel UI | 4. Technical Capabilities | Consistent multi-channel UX |
| NFR-029 | The platform shall support biometric data integration with the Airport Pass Database and other stakeholder systems | Interoperability | shall | M | base | interoperability | Identity Integration | 8. System Integration | Biometric system integration |
| NFR-030 | Data generated by the platform, including passenger tracks and derived events, shall be shared with authorized downstream systems in real time and/or batch mode | Interoperability | shall | M | base | interoperability | Data Sharing | 8. System Integration | Outbound data sharing |
| NFR-031 | The platform shall integrate with the AODB as a core source of flight context and movement state | Interoperability | shall | M | base | interoperability | Flight Data Integration | 8. System Integration | AODB integration requirement |
| NFR-032 | The platform shall explain how fused LiDAR and stitched Camera/CCTV outputs, including derived tracks, will be exposed to dashboards and downstream interfaces | Interoperability | shall | M | base | interoperability | Sensor Data Exposure | 8. System Integration | Track exposure requirement |
| NFR-033 | The platform shall integrate with Assaia AI turnaround solution to consume turnaround milestones and extend turnaround visibility into adjacent processes | Interoperability | shall | M | base | interoperability | Turnaround Integration | 8. System Integration | Assaia integration |
| NFR-034 | The platform shall support integration with Microsoft 365 applications, Teams, Outlook, and SharePoint where relevant to operational coordination | Interoperability | shall | M | base | interoperability | Productivity Integration | 8. System Integration | Microsoft ecosystem integration |
| NFR-035 | The platform shall present contributing source context, thresholds, assumptions, and confidence indicators for alerts and recommendations within the operational workflow | Usability | shall | M | base | explainability | Decision Support | 9. Non-Functional Requirements | Explainability requirement |
| NFR-036 | The platform shall support stakeholder-specific workflows, access controls, operational dashboards, and alerts based on operational responsibilities and approved data-sharing rights | Security | shall | M | base | security | Access Control | 11. Stakeholder Overview | Governance requirement |
| NFR-037 | The platform shall provide a Low-Code Configurability capability enabling authorized Dubai Airports users to configure and update business rules in a controlled manner | Maintainability | shall | M | base | maintainability | Workflow Engine | 14. Non-Functional Requirements | Low-code requirement |
| NFR-038 | The platform shall maintain appropriate role-based permissions, versioning, and auditability for all configuration changes | Auditability | shall | M | base | auditability | Access Control | 14. Non-Functional Requirements | Configuration auditability |

---

## CATEGORICAL / SUBMISSION REQUIREMENTS

| ID | Requirement Text | Category | Modal Verb | Mandatory/Scored | Scope Tier | Applies To | Source Section | Notes |
|---|---|---|---|---|---|---|---|---|
| CAT-001 | Supplier shall explain relevant implementation experience and solution capability | Submission Format | shall | M | base | Proposal Response | 17. Supplier Proposal Response Format | Experience documentation |
| CAT-002 | Supplier shall provide integration approach and infrastructure design documentation | Submission Format | shall | M | base | Technical Documentation | 17. Supplier Proposal Response Format | Technical design artifacts |
| CAT-003 | Supplier shall provide delivery method and support model | Submission Format | shall | M | base | Service Model | 17. Supplier Proposal Response Format | Service delivery documentation |
| CAT-004 | Supplier shall provide governance structure and compliance documentation | Submission Format | shall | M | base | Governance | 17. Supplier Proposal Response Format | Governance documentation |
| CAT-005 | Supplier shall provide detailed requirements documentation and requirements traceability matrix (RTM) | Submission Format | shall | M | base | Technical Documentation | 3. Scope | Requirements documentation |
| CAT-006 | Supplier shall provide High-Level Design (HLD) documentation | Submission Format | shall | M | base | Technical Documentation | 3. Scope | Architecture documentation |
| CAT-007 | Supplier shall provide Interface Control Documents (ICDs) for all system integrations | Submission Format | shall | M | base | Technical Documentation | 3. Scope | Integration documentation |
| CAT-008 | Supplier shall provide network architecture documentation | Submission Format | shall | M | base | Technical Documentation | 3. Scope | Network design documentation |
| CAT-009 | Supplier shall provide validation and test documentation | Submission Format | shall | M | base | Technical Documentation | 3. Scope | QA documentation |
| CAT-010 | Supplier shall provide LiDAR deployment and processing architecture options (edge compute, centralized, hybrid) with detailed analysis of each | Submission Format | shall | M | base | Technical Architecture | 14. Non-Functional Requirements | Architecture options analysis |
| CAT-011 | Supplier shall explain infrastructure implications, network dependency, latency considerations, resilience, and maintainability for each LiDAR architecture option | Submission Format | shall | M | base | Technical Documentation | 14. Non-Functional Requirements | Architecture trade-offs |
| CAT-012 | Supplier shall provide disaster recovery documentation covering recovery architecture, failover/failback approach, RTO/RPO targets, and testing approach | Submission Format | shall | M | base | Business Continuity | 14. Non-Functional Requirements | DR plan documentation |
| CAT-013 | Implementation shall be delivered in three phases: Phase 1 (Terminal 2 + Terminal 3 departure), Phase 2 (Terminal 3 transfer/arrival), Phase 3 (Terminal 1 full) | Submission Format | shall | M | base | Implementation | 3. Scope | Phased delivery requirement |
| CAT-014 | Supplier shall provide end-to-end responsibility across planning, location survey, 3D model build, deployment design, installation, integration, QA, validation, cutover, acceptance, hypercare, training, and support | Submission Format | shall | M | base | Service Delivery | 3. Scope | Full lifecycle responsibility |
| CAT-015 | Supplier shall provide Tier 1 operational maintenance and support as a continuing service | Submission Format | shall | M | base | Support Model | 3. Scope | L1 support requirement |

---

## Key Observations

### Requirement Distribution
- **Functional Requirements (42):** Predominantly focused on real-time monitoring, visualization, data integration, simulation, and multi-stakeholder workflows.
- **Non-Functional Requirements (38):** Heavy emphasis on accuracy thresholds (≥99% for several use cases), Tier 1 resilience, scalability, security compliance, and interoperability.
- **Categorical Requirements (15):** Extensive documentation, architecture options, and phased delivery requirements.

### High-Impact Numeric Thresholds
- **99% accuracy** for: vehicle detection/classification, vehicle dwell monitoring, unattended baggage detection, footfall counting
- **90% accuracy** for what-if simulation scenario replication
- **Tier 1 service** with no single point of failure
- **3-phase implementation** (Terminal 2 + Terminal 3 Dept → Terminal 3 Arriv/Transfer → Terminal 1 Full)

### Modal Verb Analysis
- **100% "shall" or "must"** — all extracted requirements are binding (mandatory/M).
- No optional ("should"/"may") requirements identified in core technical scope.
- All requirements classified as base scope (no deferred/phase 2 items in this extraction).

### Missing or Ambiguous Specifications
- **RTO/RPO values** not numerically specified ("to be determined").
- **Latency thresholds** referenced generically ("minimal latency", "low-latency") without numeric SLA.
- **Alert response time SLAs** not defined.
- **Data retention periods** not explicitly stated.

---

## Next Steps (Compliance Validation)

1. **Step 2:** Extract numeric requirements inventory with binding values and operators
2. **Step 3:** Validate against proposal artefact (when available)
3. **Step 4:** Parity evaluation (compare proposal values to binding thresholds)
4. **Step 5:** Semantic carve-out detection (flag weakening phrases)
5. **Step 6–12:** Full compliance audit with blocking-issue identification

---

**Extraction completed:** 95 total requirements across FRs, NFRs, and categorical categories.
