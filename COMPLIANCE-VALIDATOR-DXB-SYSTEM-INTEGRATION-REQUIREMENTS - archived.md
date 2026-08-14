# DXB 3D Digital Twin RFP — System Integration Requirements & Data Sources

**Source Document:** `3D_DigitalTwin_AirportOperations_RFP_SoW_DraftCopy.docx.md`  
**Extraction Date:** 2026-08-10  
**Status:** Step 6a - Architecture-Completeness Heuristics - System Integration Points

---

## Executive Summary

The DXB 3D Digital Twin platform is a **federated, multi-system architecture** requiring integration with **38 distinct systems, platforms, sensors, and data sources** across airport operations, stakeholder agencies, and external providers. This document catalogues every named integration point, data exchange requirement, and federated-system dependency extracted from the RFP.

### Integration Categories:
- **Sensor & Data Acquisition (8)** — CCTV, LiDAR, Xovis, BLE, IoT, weather
- **Airport Operational Systems (7)** — AODB, Collins, BHS, QRMS, CUPPS, CUSS, Veripax
- **Security & Identity (5)** — Genetec, BioHub, GDRFA, biometric systems, access control
- **Stakeholder Agencies (6)** — GDRFA, Police, Customs, AOCC, Airlines, Engineering
- **Commercial (2)** — DDF (Dubai Duty Free), retail analytics
- **Third-Party Integrations (6)** — Assaia AI, Microsoft ecosystem, SMS/WhatsApp, weather API
- **Facility & Infrastructure (3)** — Building Management Systems, HVAC, escalators
- **Video & Recording (2)** — Genetec VMS, CCTV analytics engines

---

## TIER 1: SENSOR & DATA ACQUISITION SYSTEMS

### FR-SYS-001: CCTV Video Management & Analytics
| Attribute | Specification |
|---|---|
| **System Name** | CCTV Video Management System + Video Analytics |
| **Integration Type** | Real-time video feed ingestion + analytics output consumption |
| **Data Flow** | Live camera feeds → video analytics engines → insights/alerts → Digital Twin |
| **Protocol/Interface** | ONVIF (IP cameras), RTSP, MJPEG, or vendor-specific APIs |
| **Latency Requirement** | Real-time (< specified SLA, pending) |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 4 (Technical Capabilities), Section 8 (System Integration), Section 5a (Real-Time Monitoring), Section 5e (Passenger Tracking) |
| **Key Requirements** | • Live CCTV feed integration into Digital Twin platform<br>• Convert CCTV raw feeds into insights/detections<br>• Integrate CCTV analytics module outputs into platform<br>• Support curb-to-gate passenger tracking via camera fusion<br>• Genetec VMS integration for video playback + incident sync |
| **Specific Use Cases** | Real-time passenger flow, crowd behavior analysis, queue monitoring, end-to-end tracking, security/intrusion detection, baggage tracking, vehicle monitoring |
| **Notes** | Primary video source; multiple camera types (4MP IP minimum); geographic distribution across 3 terminals |

### FR-SYS-002: LiDAR Sensors & 3D Occupancy
| Attribute | Specification |
|---|---|
| **System Name** | LiDAR Sensors (3D occupancy, depth mapping) |
| **Integration Type** | Real-time point-cloud feed ingestion + 3D model fusion |
| **Data Flow** | LiDAR point clouds → calibration/coordinate alignment → sensor fusion → 3D visualization |
| **Protocol/Interface** | UDP/TCP streaming, vendor SDK, or point-cloud standard formats (e.g., PCL) |
| **Latency Requirement** | Real-time; synchronized with CCTV (time-sync required) |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 4 (Technical Capabilities), Section 8 (System Integration), Section 5a (Real-Time Monitoring), Section 5e (Passenger Tracking) |
| **Key Requirements** | • Live LiDAR feed integration for 3D occupancy monitoring<br>• Sensor calibration & coordinate alignment with CCTV<br>• Time synchronization between LiDAR & camera feeds<br>• Data fusion to render point clouds + camera overlay in unified visual layer<br>• Support dense crowd/occupancy heatmaps<br>• Optional: LiDAR + camera unit co-location to optimize deployment cost |
| **Specific Use Cases** | End-to-end curb-to-gate tracking, crowd density heatmaps, occupancy monitoring, anomaly detection, 3D journey visualization |
| **Architecture Options Required** | Supplier must explain 3+ LiDAR processing architectures:<br>• Edge compute (cameras + LiDAR at source)<br>• Centralized processing (feeds to central processor)<br>• Hybrid (edge + central)<br>Each with: latency implications, network dependency, resilience, maintainability |
| **Notes** | Complementary to CCTV; 99% tracking accuracy target includes LiDAR fusion |

### FR-SYS-003: Xovis Passenger Counting & Queue Monitoring
| Attribute | Specification |
|---|---|
| **System Name** | Xovis Sensor Technology (thermal people counting, queue management) |
| **Integration Type** | Real-time sensor data feed ingestion + analytics output |
| **Data Flow** | Xovis sensors (overhead thermal counters) → queue/flow metrics → Digital Twin KPI engines |
| **Protocol/Interface** | Vendor SDK, REST API, or direct data feed (format TBD in proposal) |
| **Latency Requirement** | Real-time; supports dynamic queue alerts |
| **Accuracy Requirement** | ≥99% passenger counting accuracy (mandated in RFP) |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 4 (Technical Capabilities), Section 5b (Queue Management), Section 8 (System Integration) |
| **Key Requirements** | • Xovis raw sensor outputs normalized & integrated within Digital Twin<br>• Real-time queue length, throughput, wait-time metrics<br>• Support at 5+ key checkpoints: check-in, emigration, security, boarding, immigration<br>• Integrate with AODB data for throughput forecasting<br>• Automated alerts for queue threshold breaches (>20 min, configurable)<br>• Dynamic staff recommendation engine based on Xovis throughput data |
| **Specific Use Cases** | Queue length monitoring, passenger throughput optimization, staff headcount recommendations, security checkpoint efficiency, crowding alerts |
| **Deployment Scope** | Check-in (2), security (per-lane, 4–6), gates (boarding queues), baggage claim, immigration |
| **Notes** | Non-negotiable for queue-related KPIs (#1–7, #10–11 = 40% of mandatory KPIs); existing Xovis sensors at DXB must be leveraged |

### FR-SYS-004: IoT Sensors & Smart Devices
| Attribute | Specification |
|---|---|
| **System Name** | IoT Sensors (environmental, infrastructure monitoring) |
| **Integration Type** | Real-time feed ingestion via MQTT, CoAP, or REST |
| **Data Flow** | IoT devices (HVAC, escalators, lifts, doors, fire alarms) → sensor hub → Digital Twin |
| **Scope** | IT infrastructure, OT infrastructure, building automation, facility sensors |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 4 (Technical Capabilities), Section 5f (Engineering Services), Section 8 (System Integration) |
| **Key Requirements** | • Support ingestion from disparate IoT platforms (not limited to single vendor)<br>• Real-time monitoring of escalators, lifts, HVAC, doors, fire alarms, UPS systems<br>• Asset health monitoring for predictive maintenance<br>• Alert generation for equipment malfunction or degradation |
| **Specific Use Cases** | Escalator fall detection, lift malfunction alerts, HVAC temperature monitoring, door status (stuck open), fire system monitoring, UPS availability tracking |
| **Notes** | Used by Engineering Services use case; enabler for asset health & predictive maintenance KPIs |

### FR-SYS-005: Bluetooth Low Energy (BLE) Beacons
| Attribute | Specification |
|---|---|
| **System Name** | BLE Beacon Infrastructure |
| **Integration Type** | Beacon broadcast signal ingestion + proximity detection |
| **Data Flow** | BLE beacons → gateway aggregators → Digital Twin passenger tracking engine |
| **Deployment Scope** | Strategic checkpoints: check-in, security, gates, baggage claim, exit points |
| **Modal Verb** | **should** (recommended, not mandatory for base scope) |
| **Scope Tier** | **base** (per Intervención 8 mandate for CTG-analogue; DXB RFP treats as optional enhancement) |
| **Source RFP Location** | Section 4 (Technical Capabilities), Section 8 (System Integration) |
| **Key Requirements** | • Passive BLE beacon deployment (no passenger app required)<br>• Beacon triggers captured at strategic touchpoints (gate podiums, security exits)<br>• Handoff events generated to complement video/LiDAR tracking<br>• NOT continuous tracking; event-based identification only |
| **Integration Note** | Hybrid approach: video/LiDAR primary; BLE secondary for event correlation |
| **Notes** | Optional enhancement for journey continuity; CTG Intervención 8 specifies BLE mandate (may differ from DXB scope tier) |

### FR-SYS-006: Weather & NOTAM Data Integration
| Attribute | Specification |
|---|---|
| **System Name** | Weather API + NOTAM Data Feed |
| **Integration Type** | Real-time data ingestion from external provider |
| **Data Flow** | Weather service (e.g., OpenWeatherMap, NOAA, METAR) + ANSP NOTAM → disruption management engine |
| **Modal Verb** | **shall** (mandatory for disruption management) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5a (Real-Time Monitoring), Section 5d (Disruption Management), Section 8 (System Integration) |
| **Key Requirements** | • Real-time weather monitoring for runway/apron conditions<br>• NOTAM feed integration for ATC constraints<br>• Used to trigger disruption classification & recovery recommendations<br>• Support scenario modeling (weather impact on passenger demand) |
| **Specific Use Cases** | Disruption management, flight delay prediction, resource allocation during adverse weather, apron safety monitoring |
| **Notes** | External data provider; ensure cybersecurity & API availability SLA |

### FR-SYS-007: Passenger Flow Model (PFM) Integration
| Attribute | Specification |
|---|---|
| **System Name** | Passenger Flow Model (existing or supplier-provided) |
| **Integration Type** | Model input/output data exchange |
| **Data Flow** | Real-time passenger counts (CCTV, Xovis) + flight data (AODB) → PFM prediction engine → congestion forecast |
| **Modal Verb** | **shall** (mandatory for predictive KPIs) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 3 (Scope), Section 8 (System Integration) |
| **Key Requirements** | • Integrate existing passenger flow models (if available)<br>• Support demand forecasting 10–15 min ahead<br>• Use real-time counts + AODB schedule to refine predictions<br>• Output: predicted queue lengths, occupancy forecasts, bottleneck alerts |
| **Specific Use Cases** | Predictive congestion alerts (#10–11 KPIs), dynamic wayfinding, staff pre-positioning |
| **Notes** | May be supplier-delivered component; must be externally validated against real passenger behavior |

### FR-SYS-008: Building Management System (BMS) & Facility Monitoring
| Attribute | Specification |
|---|---|
| **System Name** | Building Management System (HVAC, lighting, power, water, environmental controls) |
| **Integration Type** | Real-time sensor data & system status feed |
| **Data Flow** | BMS devices → facility monitoring dashboard within Digital Twin |
| **Modal Verb** | **shall** (mandatory for facility operations) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5f (Engineering Services), Section 8 (System Integration) |
| **Key Requirements** | • Temperature monitoring across passenger areas (with color-coded heatmaps)<br>• HVAC status & alerts for inefficiency<br>• Lighting control & optimization recommendations<br>• Power monitoring (UPS status, load distribution)<br>• Water supply & sanitation system monitoring |
| **Specific Use Cases** | Climate control optimization, energy efficiency, facility resilience during disruptions |
| **Notes** | Engineering Services stakeholder integration; supports asset health & energy management KPIs |

---

## TIER 2: AIRPORT OPERATIONAL SYSTEMS

### FR-SYS-009: AODB (Airport Operational Database)
| Attribute | Specification |
|---|---|
| **System Name** | Airport Operational Database (AODB) - Primary flight & operational data repository |
| **Integration Type** | Real-time flight schedule, status, passenger load, delay, stand/gate context |
| **Data Flow** | AODB → Digital Twin operational context engine |
| **Interfaces** | AODB vendor API (e.g., Inform, SITA, Collins), SOAP/REST, direct database connection (if approved) |
| **Latency Requirement** | Real-time; flight updates within 1–2 min of AODB status change |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 8 (System Integration), Section 5a (Real-Time Monitoring), Section 5d (Disruption Management) |
| **Key Requirements** | • Core source of flight context, movement state, operational reference data<br>• Synchronization within live operational, historical, predictive, & simulation workflows<br>• Flight schedule (scheduled, estimated, actual times)<br>• Stand/gate assignments & changes<br>• Passenger loads by flight, carrier<br>• Delay codes & duration forecasts<br>• Aircraft type & configuration<br>• Link passenger counts (from CCTV/Xovis) to flight data for boarding readiness verification |
| **Specific Use Cases** | Flight-aware queue forecasting, turnaround optimization, disruption classification, baggage SLA tracking, on-time performance, boarding efficiency |
| **Data Entities Mapped** | Flights, stands, gates, aircraft, passengers, turnaround milestones, operational events |
| **Notes** | Core integration; mandatory for >15 KPIs (#19–26, #25–31 turnaround/baggage suite) |

### FR-SYS-010: Collins Systems (FIDS, RMS, CUSS, CUPPS, Veripax, AODB)
| Attribute | Specification |
|---|---|
| **System Name** | Collins Airport Systems Suite |
| **Sub-Systems** | • FIDS (Flight Information Display System)<br>• RMS (Resource Management System)<br>• CUSS (Common Use Self-Service kiosks)<br>• CUPPS (Common Use Passenger Processing System)<br>• Veripax (Passenger verification)<br>• AODB (Airport Operational Database) |
| **Integration Type** | Real-time bidirectional data exchange |
| **Data Flow** | Collins systems → Digital Twin context engine; platform outputs → downstream Collins consumers |
| **Interfaces** | Collins REST APIs, event streams, file-based exports (where real-time APIs unavailable) |
| **Latency Requirement** | Real-time (API dependent; typically <2 sec for FIDS, RMS events) |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 8 (System Integration), Section 3 (Scope), Section 5a–5e (all operational use cases) |
| **Key Requirements** | • FIDS: Display status, gate assignments, flight information<br>• RMS: Resource allocation, stand/gate availability, conflict detection<br>• CUSS: Check-in data, baggage tag generation, passenger stats<br>• CUPPS: Airline counter assignments, processing time tracking<br>• Veripax: Passenger validation at key checkpoints (immigration, boarding)<br>• AODB: Flight & operational context (see FR-SYS-009)<br>• Validate operational state consistency across all subsystems |
| **Data Entities** | Flights, stands, gates, check-in desks, security lanes, passengers, baggage, boarding status |
| **Use Cases Enabled** | Queue optimization, gate/stand allocation, turnaround tracking, boarding readiness, staff headcount balancing, OTP monitoring |
| **Critical Dependencies** | Bidirectional integration mandatory; one-way feeds insufficient for disruption management & what-if simulation |
| **Notes** | Collins is primary operational system; co-sell / joint positioning opportunity; integration testing mandatory in Pilot Phase Week 11–12 |

### FR-SYS-011: Baggage Handling System (BHS) & Baggage Tracking
| Attribute | Specification |
|---|---|
| **System Name** | Baggage Handling System (BHS) + Baggage Tracking |
| **Integration Type** | Real-time baggage events, status, tracking data |
| **Data Flow** | Baggage system → baggage status engine → Digital Twin baggage visibility layer |
| **Interfaces** | BHS vendor API (e.g., Vanderlande, Siemens, Beumer), SOAP/REST, message queues |
| **Events** | Baggage induction, sorting, carousel assignment, loading, first-bag, last-bag, exceptions (misroute, delay, missing) |
| **Latency Requirement** | Near real-time (<5 sec); critical for SLA compliance |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5c (Baggage Visibility), Section 8 (System Integration) |
| **Key Requirements** | • Near real-time visibility of baggage flow across check-in → make-up → transfer → sortation → reclaim<br>• Link baggage to passenger identity (checked & hand baggage)<br>• Capture baggage images & quantity at check-in<br>• Monitor first-bag & last-bag timing against flight SLAs<br>• Exception detection: misroutes, delays, missing bags, piling<br>• Predict baggage readiness for boarding<br>• Alert baggage handlers on delay/exception events |
| **Specific Use Cases** | Baggage visibility, boarding readiness, baggage SLA tracking, exception management, turnaround optimization |
| **KPIs Supported** | #29–31 (First-bag time, belt availability, bag piling detection), #25–26 (Turnaround milestones with baggage load status) |
| **Notes** | Baggage exceptions often cascade into disruptions; real-time visibility is critical for recovery decisions |

### FR-SYS-012: Fixed-Resource Management (QRMS / Equivalent)
| Attribute | Specification |
|---|---|
| **System Name** | Fixed-Resource Management System (QRMS or equivalent) |
| **Integration Type** | Real-time resource availability, allocation, scheduling |
| **Data Flow** | QRMS resource data → Digital Twin allocation optimizer |
| **Scope** | Check-in desks, security lanes, gates, reclaim belts, boarding bridges, baggage carts, GSE |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5g (Gate/Stand/Resource Optimization), Section 8 (System Integration) |
| **Key Requirements** | • Live view of resource occupancy, availability, predicted contention<br>• Support scenario modeling (gate closures, checkpoint outages, resource restrictions)<br>• Allocation optimization recommendations<br>• Conflict detection (double-bookings, under-utilization) |
| **Specific Use Cases** | Gate/stand optimization, resource conflict resolution, disruption recovery planning, capacity planning |
| **Notes** | Enables what-if simulation for infrastructure changes & disruption scenarios |

### FR-SYS-013: Existing Baggage Trolley Tracking System
| Attribute | Specification |
|---|---|
| **System Name** | Baggage Trolley Tracking & Availability System |
| **Integration Type** | Real-time trolley location & availability feed |
| **Data Flow** | Trolley tracking data → Digital Twin facility management dashboard |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5c (Baggage Visibility - Trolley Availability Monitoring), Section 8 (System Integration) |
| **Key Requirements** | • ≥99% accuracy in monitoring trolley availability & location across airport<br>• Real-time alerts when trolley numbers fall below threshold in high-demand areas<br>• Integration with baggage service team mobile apps for dispatch optimization<br>• Predictive model for trolley demand by area/time |
| **Specific Use Cases** | Passenger service, baggage handling efficiency, facility operations |
| **Notes** | Helps reduce manual patrols; enables proactive trolley replenishment |

---

## TIER 3: SECURITY & IDENTITY SYSTEMS

### FR-SYS-014: Genetec Video Management & SDK Integration
| Attribute | Specification |
|---|---|
| **System Name** | Genetec Platform (VMS + SDK) - Video Security & Analytics |
| **Integration Type** | Video playback, incident correlation, synchronized review |
| **Data Flow** | Genetec archive → recorded video retrieval → Digital Twin incident investigation workflow |
| **Interfaces** | Genetec SDK (C#/.NET), REST APIs, direct archive access (where approved) |
| **Latency Requirement** | Near real-time for playback sync; archive retrieval <5 sec |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 4 (Technical Capabilities - Integration with Genetec SDK), Section 8 (System Integration) |
| **Key Requirements** | • Enable recorded video playback synchronized with Digital Twin events<br>• Support incident review: search by timestamp, location, event type<br>• Retrieve historical video footage alongside Digital Twin operational timeline<br>• Integration with investigation workflows & evidence retention |
| **Specific Use Cases** | Incident investigation, security breach response, operational review, compliance documentation |
| **Notes** | Critical for forensic analysis; enables historical correlation of anomalies with recorded behavior |

### FR-SYS-015: BioHub / Biometric Identity Integration
| Attribute | Specification |
|---|---|
| **System Name** | BioHub / Biometric Identity Systems (iris, fingerprint, facial) |
| **Integration Type** | Identity verification at key checkpoints, passenger linking |
| **Data Flow** | Biometric capture → identity verification → passenger profile linkage → journey tracking |
| **Interfaces** | BioHub APIs, biometric sensor SDKs, identity database queries |
| **Modal Verb** | **shall** (mandatory for identity-linked journey continuity) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5f (Passenger Identification & Journey Continuity), Section 8 (System Integration) |
| **Key Requirements** | • Authorized biometric data integration with Airport Pass Database<br>• Support identity verification at emigration, immigration, boarding gates<br>• Maintain passenger profile linkage across journey stages<br>• No facial recognition or individual tracking; aggregate-level analytics only<br>• Comply with biometric privacy regulations |
| **Specific Use Cases** | Transfer passenger tracking, identity-linked journey continuity, staff access verification, Red Carpet eligibility detection |
| **Data Entities** | Passenger identity, access permissions, biometric templates (hashed, not stored by platform) |
| **Notes** | GDRFA & Police stakeholder integration; sensitive regulatory requirements |

### FR-SYS-016: GDRFA Systems (General Directorate for Residency & Foreign Affairs)
| Attribute | Specification |
|---|---|
| **System Name** | GDRFA Systems (Immigration, passport control, traveler records) |
| **Integration Type** | Real-time passenger movement & procedural compliance tracking |
| **Data Flow** | GDRFA checkpoint events → Digital Twin immigration monitoring layer |
| **Interfaces** | GDRFA APIs, biometric integration (BioHub), event streams |
| **Modal Verb** | **shall** (mandatory for immigration stakeholder) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 6a (GDRFA Use Cases), Section 8 (System Integration) |
| **Key Requirements** | • Queue visibility & demand prediction at immigration checkpoints<br>• Lane utilization monitoring & staffing coordination<br>• Passenger journey tracking from curb to gate across immigration touchpoints<br>• Anomaly detection: no actual traveling movement, transit deviations, staff pass misuse, reverse-direction movement, overstays, procedural deviations, restricted access attempts<br>• Alert: unattended immigration counter, gate barrier malfunction<br>• Red Carpet eligibility identification (proactive "May I Help You" assistance) |
| **Specific Use Cases** | Immigration queue optimization, security anomaly detection, compliance monitoring, passenger assistance routing |
| **Proposed KPIs** | Average immigration wait time, lane utilization rate, prediction accuracy, passenger continuity rate, anomaly detection accuracy, alert-to-intervention time |
| **Notes** | Stakeholder-specific use case; high regulatory sensitivity; requires careful data governance |

### FR-SYS-017: Dubai Police Access & Security Systems
| Attribute | Specification |
|---|---|
| **System Name** | Dubai Police Systems (Security, incident response, access control) |
| **Integration Type** | Incident alerts, access control events, security monitoring |
| **Data Flow** | Security events → Police incident management → Digital Twin security dashboard |
| **Modal Verb** | **shall** (mandatory for security stakeholder) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 6b (Dubai Police Use Cases), Section 8 (System Integration) |
| **Key Requirements** | • Real-time crowd anomaly detection & intervention support<br>• Restricted-area intrusion detection with immediate alerts<br>• Abandoned object & unattended baggage monitoring<br>• Passenger tracking from curb to gate for movement continuity & anomaly detection<br>• Historic playback & incident evidence availability<br>• Biometric identity linkage (authorized personnel only) |
| **Specific Use Cases** | Security event detection, intrusion response, crowd management, incident investigation |
| **Proposed KPIs** | Incident detection accuracy, average response initiation time, passenger continuity rate, false positive rate |
| **Notes** | High-priority stakeholder; real-time alerting critical for security posture |

### FR-SYS-018: Dubai Customs Systems
| Attribute | Specification |
|---|---|
| **System Name** | Dubai Customs Systems (Baggage inspection, prohibited goods detection) |
| **Integration Type** | Real-time passenger & baggage movement tracking, inspection workload monitoring |
| **Data Flow** | Baggage movement data + passenger flow + video analytics → Customs operations dashboard |
| **Modal Verb** | **shall** (mandatory for customs stakeholder) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 6c (Dubai Customs Use Cases), Section 8 (System Integration) |
| **Key Requirements** | • Passenger journey attributes (destination, transit/direct status)<br>• Passenger demographic data (nationality, age group)<br>• Baggage details, count, IDs, images<br>• Flight data & passenger volume context<br>• Baggage movement tracking linked to passengers<br>• Video analytics for suspicious baggage detection<br>• Workload & passenger density measurement across customs/baggage/inspection zones<br>• Smart CCTV for alerting on suspicious behavior<br>• Unified alert sharing & mobile app access for inspectors |
| **Specific Use Cases** | Customs inspection optimization, workload balancing, suspect detection, SLA compliance |
| **Proposed KPIs** | Detection accuracy, response time, crowd management, queue wait time, passengers processed per lane, inspection area occupancy |
| **Notes** | High-sensitivity stakeholder; data sharing carefully governed; supports dual security/commercial objectives |

---

## TIER 4: STAKEHOLDER AGENCIES & OPERATIONAL PARTNERS

### FR-SYS-019: Airlines Operational Systems
| Attribute | Specification |
|---|---|
| **System Name** | Airline Systems (Flight planning, crew management, ground operations) |
| **Integration Type** | Real-time flight data, passenger manifests, operational constraints |
| **Data Flow** | Airline systems → Digital Twin flight context engine |
| **Interfaces** | Airline APIs, NDC (New Distribution Capability), IATA messaging (e.g., ACARS) |
| **Modal Verb** | **shall** (mandatory for operational coordination) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 8 (System Integration), Section 5d (Disruption Management) |
| **Key Requirements** | • Passenger manifest data (for boarding readiness, special needs, crew duty limits)<br>• Crew duty time limits (impacts flight prioritization during disruptions)<br>• Aircraft size & configuration (impacts gate/stand allocation)<br>• Destination curfews & operational criticality ranking<br>• Integration into disruption decision support (which flights to delay/divert/consolidate) |
| **Specific Use Cases** | Disruption prioritization, crew duty compliance, boarding coordination, operational decision support |
| **Notes** | Multiple airline partners; data governance via Master Service Agreements |

### FR-SYS-020: Ground Handler (dnata) Systems
| Attribute | Specification |
|---|---|
| **System Name** | Ground Handler Systems (dnata) - GSE dispatch, cargo, catering, baggage loading |
| **Integration Type** | Real-time ground service events, GSE status, turnaround progress |
| **Data Flow** | Ground handler events → Digital Twin turnaround optimization engine |
| **Modal Verb** | **shall** (mandatory for turnaround optimization) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5e (Resource, Turnaround, Airside Optimization), Section 8 (System Integration) |
| **Key Requirements** | • GSE dispatch status & readiness<br>• Service sequencing (fuelling, catering, cleaning, baggage loading order)<br>• Turnaround milestone events (arrive, gates open, pushback)<br>• Resource utilization (crew, equipment availability)<br>• Integration into turnaround optimization & what-if simulation |
| **Specific Use Cases** | Turnaround time optimization, GSE dispatch sequencing, service conflict resolution, OTP improvement |
| **Notes** | Critical for stand utilization & departure punctuality KPIs |

### FR-SYS-021: AOCC (Airport Operations Control Center) Coordination Systems
| Attribute | Specification |
|---|---|
| **System Name** | AOCC Operational Coordination & Decision Support |
| **Integration Type** | Bi-directional workflow integration, alerts, recommendations, approvals |
| **Data Flow** | Digital Twin → AOCC recommendations; AOCC decisions → Digital Twin operational adjustments |
| **Modal Verb** | **shall** (mandatory) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5d (Disruption Management), Section 8 (System Integration) |
| **Key Requirements** | • Centralized disruption overview dashboard<br>• Collaborative decision-support environment capturing inputs from AOCC, airlines, ATC, terminals, baggage, security<br>• Workflow-driven approval gates for major decisions (flight delay, divert, consolidation)<br>• Task routing & escalation (alerts to relevant operators)<br>• Recorded decision audit trail for post-event analysis |
| **Specific Use Cases** | Disruption management, recovery planning, cross-stakeholder coordination, decision traceability |
| **Notes** | AOCC is the primary daily user; platform success depends on intuitive AOCC integration |

### FR-SYS-022: Engineering Services & Maintenance Systems
| Attribute | Specification |
|---|---|
| **System Name** | Engineering Services & Predictive Maintenance Systems |
| **Integration Type** | Asset health data, maintenance schedules, alert escalation |
| **Data Flow** | Equipment sensor data → asset health engine → Engineering maintenance prioritization |
| **Modal Verb** | **shall** (mandatory for asset management) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5f (Commercial & Engineering), Section 6e (Engineering Services Use Cases), Section 8 (System Integration) |
| **Key Requirements** | • Real-time asset condition monitoring (escalators, lifts, HVAC, doors, BHS, ground equipment)<br>• Predictive maintenance alerts (before material failure)<br>• Prioritization by operational criticality & passenger impact<br>• Maintenance job scheduling & tracking<br>• Historical trend analysis for root-cause identification |
| **Specific Use Cases** | Unplanned downtime reduction, predictive maintenance, asset lifecycle optimization, disruption prevention |
| **Notes** | Supports Engineering KPIs & operational resilience |

---

## TIER 5: COMMERCIAL & THIRD-PARTY SYSTEMS

### FR-SYS-023: DDF (Dubai Duty Free) Retail Systems
| Attribute | Specification |
|---|---|
| **System Name** | Dubai Duty Free (DDF) Point-of-Sale (POS) & Retail Analytics |
| **Integration Type** | Footfall analytics, retail conversion tracking, merchandise movement |
| **Data Flow** | Passenger movement data + retail POS data → commercial performance dashboard |
| **Modal Verb** | **should** (scored for commercial stakeholder) |
| **Scope Tier** | **base** (commercial use case) |
| **Source RFP Location** | Section 6d (Commercial/DDF Use Cases), Section 8 (System Integration) |
| **Key Requirements** | • Footfall counting & heatmaps across retail zones<br>• Conversion analytics (pass-by vs. entry vs. purchase)<br>• Drive-to-store attribution (media exposure → store visit)<br>• Zone-based tracking for layout optimization<br>• Demographic analysis (nationality, destination, age group)<br>• Attention mapping for advertising screens<br>• Dwell-time analysis by retail area<br>• High-dwell / low-conversion zone identification |
| **Specific Use Cases** | Retail performance optimization, media valuation, dynamic promotions, store layout decisions, staffing alignment to peak conversion periods |
| **Proposed KPIs** | Footfall by zone, conversion rate, store-entry correlation, attention time, drive-to-store attribution, ad engagement metrics |
| **Notes** | Commercial value-add for airport concessions; data privacy carefully governed (anonymized passenger profiles only) |

### FR-SYS-024: Assaia AI Turnaround Solution
| Attribute | Specification |
|---|---|
| **System Name** | Assaia AI - Aircraft Turnaround Optimization |
| **Integration Type** | Real-time turnaround milestones, predictive insights, operational events |
| **Data Flow** | Assaia outputs (turnaround forecast, delay drivers, service completion status) → Digital Twin turnaround dashboard |
| **Interfaces** | Assaia APIs, event streams, real-time data feeds |
| **Modal Verb** | **shall** (mandatory for turnaround optimization) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 5e (Aircraft Turnaround Optimization), Section 8 (System Integration) |
| **Key Requirements** | • Real-time visibility of turnaround milestone performance (stand arrival, ground handling, fuelling, catering, baggage, boarding, pushback readiness)<br>• Early identification of delay drivers & predicted downstream impact on stand occupancy, departure punctuality, gate readiness<br>• Improved coordinated intervention by AOCC, airlines, dnata<br>• Extend turnaround insights into adjacent terminal & baggage processes |
| **Specific Use Cases** | Turnaround time reduction, OTP improvement, disruption prevention, resource optimization |
| **Notes** | Existing Dubai Airports solution; integration critical for operational value delivery |

### FR-SYS-025: Microsoft Productivity & Communication Tools
| Attribute | Specification |
|---|---|
| **System Name** | Microsoft 365 Ecosystem (Teams, Outlook, SharePoint) + SMS/WhatsApp |
| **Integration Type** | Alert distribution, workflow collaboration, team communication |
| **Data Flow** | Digital Twin operational alerts → Teams/SMS/WhatsApp notifications → stakeholder action |
| **Interfaces** | Microsoft Teams API, Outlook API, SMS gateway, WhatsApp Business API |
| **Modal Verb** | **shall** (mandatory for multi-channel alerting) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 4 (Technical Capabilities), Section 8 (System Integration) |
| **Key Requirements** | • Operational alerts routed to Teams channels (by stakeholder role)<br>• Email notifications via Outlook (incident summaries, escalations)<br>• SMS / WhatsApp for critical alerts (when Teams unavailable)<br>• Workflow integration: decision-support collaboration within Teams<br>• Incident tracking & post-event documentation via SharePoint |
| **Specific Use Cases** | Alert distribution, incident response coordination, documented decision-making, stakeholder notification |
| **Notes** | Multi-channel is critical for ensuring alerts reach users across office/field environments |

### FR-SYS-026: External Weather & Meteorological APIs
| Attribute | Specification |
|---|---|
| **System Name** | Weather API (OpenWeatherMap, NOAA, METAR, ANSP) |
| **Integration Type** | Real-time weather feed + forecast data |
| **Data Flow** | Weather service → disruption management engine → scenario modeling |
| **Modal Verb** | **shall** (mandatory for disruption classification) |
| **Scope Tier** | **base** |
| **Source RFP Location** | Section 8 (System Integration), Section 5d (Disruption Management) |
| **Key Requirements** | • Real-time visibility of weather conditions affecting runway, apron, terminal<br>• METAR data integration for ATC constraints<br>• Weather forecast (3–6 hr horizon) for predictive modeling<br>• Support scenario modeling: weather impact on passenger demand, flight operations, resource needs |
| **Specific Use Cases** | Disruption management, predictive resource allocation, scenario testing, recovery planning |
| **Notes** | External dependency; ensure API reliability & data refresh cadence |

---

## TIER 6: INTEGRATION ARCHITECTURE REQUIREMENTS (Step 6a - Heuristics)

### Architecture-Completeness Probe: Cross-System Data Governance

For the federated multi-system architecture above, the following integration governance probes are **explicitly recommended** (though not all are formally mandated in RFP language):

#### Probe 1: Identifier & Cross-Reference Mapping
| Requirement | Specification | Applies To |
|---|---|---|
| **Cross-System Entity Linking** | How are passengers, baggage, flights, stands, gates, and assets identified and linked across systems? | All systems (AODB ↔ CCTV ↔ Xovis ↔ BHS ↔ Customs ↔ GDRFA) |
| **Unique ID Governance** | Who owns the master ID for each entity type (flight, passenger, baggage, stand)? Are there collisions or misalignment between AODB flight ID, airline PNR, baggage barcode, GDRFA record ID? | Flight: AODB (authoritative); Passenger: PNR + biometric ID; Baggage: BHS barcode; Stand: RMS code |
| **Audit Trail Requirement** | Can entity linkages be traced end-to-end (e.g., passenger ID → GDRFA clearance → boarding gate → flight departure)? | All journeys; mandatory for compliance tracing |
| **Verdict** | **Advisory (expectation risk):** The RFP does not explicitly mandate cross-system identity reconciliation governance, but operational success depends on it. Proposal should describe entity master-record strategy. |

#### Probe 2: Lifecycle & Version Governance
| Requirement | Specification | Applies To |
|---|---|---|
| **Shared Object Versioning** | When a flight record (scheduled time, stand assignment, gate assignment) changes, who is authoritative? How is the change propagated across all consuming systems (Digital Twin, display systems, mobile apps)? | Flights (AODB), stands (RMS), gates (FIDS), passenger manifests (airlines) |
| **Change Audit Trail** | Can every change to a critical operational object (flight delay, stand reallocation, gate change) be traced with timestamp, change reason, approver? | Disruption-critical objects; required for post-event analysis |
| **Conflict Resolution** | If AODB and Collins RMS disagree on gate assignment, which is authoritative? How are conflicts detected & resolved in real-time? | Stand/gate allocation; RMS likely authoritative (live system) vs. AODB (planning) |
| **Verdict** | **Advisory (addressed):** Proposal should explain change propagation architecture & conflict resolution for critical objects. Section 5d (Disruption Management) implies this requirement. |

#### Probe 3: Relationship & Structural Model
| Requirement | Specification | Applies To |
|---|---|---|
| **System Dependency Mapping** | What is the formal dependency graph? E.g., which systems must be available for Digital Twin to function? Which can degrade gracefully? | Criticality ranking: AODB, Collins, CCTV, Xovis (tier 1); BHS, GDRFA, Customs (tier 2); weather, DDF, Assaia (tier 3) |
| **Hierarchical Relationships** | Are entities organized hierarchically (e.g., flight → passengers → baggage → carousel)? How does the hierarchy enforce data consistency? | Flight → passengers, baggage, stands, gates, resources |
| **Composition vs. Association** | Which relationships are composition (part-of; can't exist independently) vs. association (reference; can be reassigned)? | Composition: flight has passengers, baggage; Association: passenger can be re-gated, baggage re-routed |
| **Verdict** | **Advisory (expectation risk):** Proposal should document system architecture diagram showing tier-1 vs. tier-2 vs. optional dependencies. Failure mode analysis (what happens if BHS is offline?) mandatory. |

#### Probe 4: Long-Term Ownership & Handover
| Attribute | Specification | Applies To |
|---|---|---|
| **Data Ownership After Go-Live** | For each integrated system's data, who owns the relationship maintenance post-deployment? (E.g., if Xovis sensor fails, who installs replacement? Who owns version updates to Collins AODB schema?) | Each source system: vendor responsible for their system; airport responsible for contractual maintenance |
| **Support Model Clarity** | Is L1/L2/L3 support split clear between vendor (Digital Twin) and system owners (AODB vendor, Collins, BHS vendor)? | L1: vendor troubleshoots Digital Twin integration; L2: escalates to source system vendor; L3: source system vendor core support |
| **Data SLA Accountability** | For critical data flows (AODB → Digital Twin turnaround KPI), who is accountable if the data is stale, inaccurate, or missing? Vendor? System owner? Airport? | Vendor: responsible for integration quality; system owner: responsible for their system's data accuracy; Airport: responsible for SLA enforcement |
| **Verdict** | **Advisory (expectation risk):** Proposal should include RACI matrix clarifying accountability for each data flow. Post-implementation issues will otherwise lead to finger-pointing. |

#### Probe 5: End-to-End Lineage & Data Provenance
| Requirement | Specification | Applies To |
|---|---|---|
| **Value Traceability** | Can a KPI value (e.g., "Queue wait time = 18.5 min") be traced back to its source sensor (Xovis #3 at security lane 5)? Timestamp? Processing transformations? | All KPIs; mandatory for audit & root-cause analysis |
| **Confidence Indicators** | For derived values (e.g., "predicted queue length = 25 pax"), what is the confidence interval? (±5 pax, ±10 pax?) Which sensor/model contributed most to the prediction? | ML predictions; required for operational decision credibility |
| **Audit Capabilities** | Can airport audit teams query: "Who accessed this baggage record? When? Why? What downstream systems consumed it?" | Compliance, security, GDPR/privacy investigations |
| **Verdict** | **Advisory (addressed):** Section 4 (Technical Capabilities) and Section 9 (Decision Explainability) mandate confidence indicators and provenance. Proposal should explain provenance tracking architecture. |

---

## INTEGRATION DEPENDENCY CRITICALITY RANKING

### Tier 1 (Blocking for Core Operations) — If unavailable, platform cannot function
- AODB (flight context)
- CCTV + video analytics (primary tracking)
- LiDAR (3D occupancy)
- Collins RMS/FIDS (resource allocation)
- Xovis (queue metrics)

### Tier 2 (Degradation Mode) — Platform operates with reduced capability
- BHS (baggage tracking partial; manual override possible)
- GDRFA (identity tracking partial; proceed without biometric)
- Customs (inspection support offline; manual processes continue)
- Assaia (turnaround optimization unavailable; manual planning)

### Tier 3 (Optional Enhancements) — Platform operates fully; stakeholder experience reduced
- DDF retail analytics (commercial value lost)
- Weather API (scenario modeling unavailable; rule-based disruption only)
- Genetec (video playback unavailable; live analytics continue)
- BLE beacons (event-based tracking partial; camera-only mode)

---

## INTEGRATION SCHEDULE & PHASING

| Phase | Primary Systems | Secondary Systems | Optional Systems |
|---|---|---|---|
| **Pilot (Q1–Q2 2027, 12 weeks)** | AODB, CCTV, LiDAR, Xovis, Collins RMS | BHS (baggage area integration testing) | Assaia (read-only integration validation) |
| **Full Deployment (Q2–Q3 2027, 12 weeks)** | All Tier 1 + Tier 2 | GDRFA, Customs, DDF, Engineering systems | Weather API, Genetec video playback |
| **Maturity (Q3–Q4 2027, 8 weeks)** | Optimization & tuning | Advanced analytics enablement | Future use-case onboarding capability |

---

## NUMERIC INTEGRATION REQUIREMENTS

| Parameter | Binding Value | Operator | Applies To | Source |
|---|---|---|---|---|
| System integration latency | <2 seconds | ≤ | Real-time feeds (AODB, Collins, Xovis) | Section 4 (Technical Capabilities) |
| Data quality checks | Mandatory | presence | All data sources | Section 4 (Technical Capabilities) |
| Source-health monitoring | Mandatory | presence | All feeds | Section 4 (Technical Capabilities) |
| Stale-feed detection | Mandatory | presence | All time-sensitive data | Section 4 (Technical Capabilities) |
| Integration protocol support | API + ESB + file-based | =  | Multi-channel data exchange | Section 4 (Technical Capabilities) |
| Xovis accuracy | 99% | ≥ | Queue monitoring | Section 5b (Queue Management) |
| CCTV + LiDAR fusion accuracy | 99% | ≥ | Passenger tracking | Section 5e (Passenger Tracking) |
| Data synchronization frequency | Real-time | = | Live operational feeds | Section 8 (System Integration) |

---

## COMPLIANCE VALIDATION NOTES

This inventory is input to **Step 6a (Architecture-Completeness Heuristics)** of the compliance-validator. 

**Next Steps:**
1. **Proposal must address each of 26 systems** with specific integration approach (interface method, data flow diagram, error handling, failover strategy).
2. **Proposal must explain RACI matrix** for cross-system data accountability (who owns master record? Who reconciles conflicts? Who escalates failures?).
3. **Proposal must provide 3–5 architecture options** for federated data harmonization (centralized hub vs. distributed/edge vs. hybrid).
4. **Proposal must define SLAs** for each critical data flow (latency, availability, data freshness).
5. **Deviation register** should list any systems proposed to be integrated via degraded mode (read-only, batch instead of real-time, optional components).

---

**Total Systems Extracted: 26 named systems + 7 sensor families = 38+ integration points identified from RFP text.**

**Status:** Ready for proposal compliance validation (Step 3: Validate Categorical FRs).
