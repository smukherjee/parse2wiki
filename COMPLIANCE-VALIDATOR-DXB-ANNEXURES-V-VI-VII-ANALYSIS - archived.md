# DXB RFP Annexures V, VI, VII — Complete Extraction & Validation

**Date:** 2026-08-10  
**Status:** All three annexures extracted and cross-validated

---

## ANNEXURE V: System Integration Register (17 Integrations)

### Complete Integration Inventory

| Ref | System / Interface | Source Sections | Integration Purpose | Data Exchanged | Primary Stakeholders | Coverage in My Inventory |
|---|---|---|---|---|---|---|
| **INT-01** | CCTV / Camera Feeds | Sections 4, 5, 13, 14, 19 | Live visual feeds + derived analytics | Live/recorded video, insights, object tracks, events, alerts, evidence | Crowd mgmt, intrusion detection, tracking, security, AOCC, Police | ✓ FR-SYS-001 |
| **INT-02** | Kayvan Airside Maps | Sections 8, 19 | Airside map data, geospatial references | Map layers, geospatial refs, map services, location context | Airside visualization, surface movement, AOCC, Engineering | ⚠ **GAP** — Not in inventory (identified as gap in glossary reconciliation) |
| **INT-03** | Platform Outbound Data Exchange | Sections 10, 14, 15, 16, 19 | Expose approved outputs to downstream systems | Passenger tracks, events, alerts, predictions, exports, streams, APIs | Analytics platforms, reporting, dashboards, stakeholders, BT teams | ✓ FR-035, NFR-030 (partial) |
| **INT-04** | Genetec SDK | Section 4, 14, 19 | Incident-linked event alignment | Incident video, event logs, aligned playback | AOCC, security stakeholders | ✓ FR-SYS-014 |
| **INT-05** | LiDAR | Sections 4, 5, 10, 14, 15, 17 | Point-cloud visualization, movement analysis, fused views | Point clouds, calibrated geometry, tracked objects, fused tracks | Curb-to-gate tracking, crowd mgmt, AOCC, Terminal Service | ✓ FR-SYS-002 |
| **INT-06** | Xovis | Sections 5, 13, 14 | Passenger counting, queue, flow insights | Counts, queue lengths, wait times, throughput, events | Queue mgmt, real-time monitoring, AOCC, GDRFA | ✓ FR-SYS-003 |
| **INT-07** | AODB | Sections 5, 13, 14, 15 | Flight, schedule, stand, gate, operational context | Flight schedules, actuals, assignments, status, timestamps | Disruption mgmt, turnaround, resource allocation, AOCC, Airlines | ✓ FR-SYS-009 |
| **INT-08** | Quintiq / QRMS | Sections 5, 13, 15 | Gate, stand, reclaim, desk, lane allocation + simulation | Resource plans, allocations, capacities, constraints, availability | Resource optimization, disruption mgmt, planning, AOCC | ✓ FR-SYS-012 |
| **INT-09** | Passenger Flow Model | Sections 5, 13, 14, 15 | Predicted demand, LoS impact, resource requirements | 15-min forecasts, LoS predictions, required resources | Forecasting, real-time monitoring, disruption, AOCC | ✓ FR-SYS-007 |
| **INT-10** | Assaia AI Turnaround | Sections 4, 5, 13 | Aircraft turnaround milestones + predictive insight | Turnaround events, forecasts, insight, gate/stand data | Turnaround optimization, stand allocation, AOCC | ✓ FR-SYS-024 |
| **INT-11** | A-CDM / RealTimeDXB / ATFM | Sections 5, 13, 14 | TTOT/CTOT coordination with ANSP | TTOT, CTOT updates, ATC constraints | AOCC, Airlines, ATC coordination | ⚠ **GAP** — Not in inventory (identified as architectural conflict with SSOV mandate in glossary reconciliation) |
| **INT-12** | FIDS / Community App / Communication Channels | Sections 5, 13, 19 | Wayfinding, queue, disruption, flight-status passenger info | Display updates, wait times, alerts, rerouting msgs | Dynamic wayfinding, disruption comms, passengers | ✓ FR-SYS-025 (partial), FR-031 |
| **INT-13** | Airport Pass DB / Mohaqiq / BioHub / GDRFA / Biometric Systems | Sections 4, 5, 14, 18 | Identity-linked use cases, journey continuity, access verification | Identity events, biometric verification, access records | Passenger continuity, transfer tracking, GDRFA, AOCC, Airlines, Police | ✓ FR-SYS-015, FR-SYS-016 |
| **INT-14** | BHS / BRS / DCS / Airline Ops | Sections 5, 14 | Baggage visibility, baggage-passenger linkage, boarding readiness | Bag status, sortation, reclaim, passenger/bag linkage | Baggage mgmt, passenger correlation, dnata, Airlines | ✓ FR-SYS-011, FR-SYS-019 |
| **INT-15** | BMS / HVAC / Lighting / UPS / IoT | Sections 5, 19 | Asset health, temperature, energy, alarm, predictive maintenance | Temp data, alarms, device status, energy, UPS events | Asset monitoring, energy mgmt, Engineering, Facilities | ✓ FR-SYS-004, FR-SYS-008 |
| **INT-16** | MS Teams / WhatsApp / SMS / Outlook / Productivity | Sections 4, 19 | Alert distribution, workflows, operational updates | Alert payloads, notifications, workflow tasks, disruption msgs | Cross-stakeholder comms, disruption alerts, AOCC teams | ✓ FR-SYS-025 |
| **INT-17** | ESB / APIs | Sections 10, 13, 14, 16 | System-to-system real-time integration backbone | API payloads, event streams, data exchange | BT integration, system connectivity, enterprise middleware | ✓ NFR-005 (partial) |

### Annexure V Validation Summary

**Total Integrations in Register:** 17  
**Integrations in My Inventory (FR-SYS-001 to FR-SYS-026):** 15 covered  
**Gap Integrations:**
- ⚠ INT-02: Kayvan (airside maps) — identified as gap in glossary reconciliation
- ⚠ INT-11: RealTimeDXB/A-CDM — identified as architectural conflict

**Coverage:** 88% (15/17)

---

## ANNEXURE VI: Consolidated Use Case Compliance Matrix (A1–A8)

### Comparison with Annexure IV

**Finding: ANNEXURES IV & VI ARE IDENTICAL**

Both contain the exact same 8 use cases (A1–A8) with identical requirement summaries, stakeholders, and expected outcomes:

| A# | Use Case | Source | IV Status | VI Status | Match |
|---|---|---|---|---|---|
| A1 | End-to-end passenger tracking | Sections 5 & 6 | ✓ Present | ✓ Present | **IDENTICAL** |
| A2 | Passenger identity + baggage linkage | Sections 5 & 6 | ✓ Present | ✓ Present | **IDENTICAL** |
| A3 | Security monitoring + intrusion detection | Sections 5 & 6 | ✓ Present | ✓ Present | **IDENTICAL** |
| A4 | Disruption mgmt + resource optimization | Sections 5 & 6 | ✓ Present | ✓ Present | **IDENTICAL** |
| A5 | Stakeholder-specific use cases + KPIs | Sections 5 & 6 | ✓ Present | ✓ Present | **IDENTICAL** |
| A6 | Commercial analytics + concession intelligence | Sections 5 & 6 | ✓ Present | ✓ Present | **IDENTICAL** |
| A7 | Engineering + asset health monitoring | Sections 5 & 6 | ✓ Present | ✓ Present | **IDENTICAL** |
| A8 | Scalability + extensibility + future onboarding | Sections 5, 6 & 7 | ✓ Present | ✓ Present | **IDENTICAL** |

### Annexure VI Validation Summary

**Conclusion:** Annexure VI is a **DUPLICATE** of Annexure IV; no new requirements introduced.

**Action:** Do NOT count VI separately in compliance validation; it adds no new requirements beyond IV.

**Coverage (vs. My Inventory):** Same as IV — 68% average (5.5 of 8 use cases fully addressed)

---

## ANNEXURE VII: Technical Capability Compliance Matrix (23 Capabilities)

### Complete Technical Capability List

| # | Technical Capability | Requirement Summary | Coverage in My Inventory |
|---|---|---|---|
| 1 | **Digital Twin Visualization** | Use Unreal Engine for 3D visualization; intuitive, accurate, collaborative experience | ✓ FR-001, FR-002, FR-003, FR-004 |
| 2 | **System Integration** | Integrate with IT, OT, IoT, CCTV, LiDAR, streaming, structured/unstructured data | ✓ FR-006, FR-007, NFR-001, NFR-005 |
| 3 | **Real-Time Monitoring** | Real-time passenger flow, operations, tracking, forecasting, bottleneck detection | ✓ FR-008, FR-009, FR-010, FR-011, FR-012 |
| 4 | **Historical Data Analysis & Playback** | Playback, retrospective analysis, Digital Twin views with recorded footage | ✓ FR-020, FR-021 |
| 5 | **Integration with Genetec SDK** | Recorded video playback, synchronized incident review, aligned Digital Twin | ✓ FR-019 |
| 6 | **What-If Simulation** | Model operational scenarios, assess impact before implementation | ✓ FR-017, FR-018 |
| 7 | **Data Stitching / Unified View** | Stitch/merge multiple sources (camera, LiDAR) into unified operational/visual view | ✓ FR-005 |
| 8 | **Biometric & Stakeholder System Integration** | Integrate biometric data, Airport Pass DB, authorized stakeholder systems | ✓ FR-005, FR-015, FR-016, NFR-029 |
| 9 | **Assaia AI Integration** | Consume turnaround milestones, events, alerts, insights from Assaia | ✓ FR-SYS-024 |
| 10 | **Canonical Data & Event Model** | Provide canonical model for flights, stands, gates, passengers, bags, queues, assets, incidents | ✓ FR-007 |
| 11 | **Governed Spatial & Model Management** | Manage spatial models, zones, hierarchies, sensor geometry, calibration, metadata, versioning | ✓ FR-023, FR-024 |
| 12 | **Data Quality & Confidence Monitoring** | Source-health visibility, stale-feed detection, completeness checks, confidence scoring | ✓ NFR-003, NFR-004 |
| 13 | **Explainability & Traceability** | Explain alerts, forecasts, recommendations (source, thresholds, assumptions, confidence) | ✓ NFR-004, NFR-035 |
| 14 | **Sustainability Analytics** | Correlate energy, utilities, assets, passenger flow for resource optimization + environmental reporting | ⚠ PARTIAL — NFR-003 covers data quality but not sustainability-specific KPIs |
| 15 | **Operational Case & Incident Workflow** | Convert alerts to cases, assign ownership, escalate, log actions, capture closure evidence | ⚠ PARTIAL — FR-016 covers decision support but not formal case management workflow |
| 16 | **Planning-Mode Capability** | Compare current vs. future scenarios, validate changes, assess impact before implementation | ✓ FR-017, FR-018 |
| 17 | **Digital Twin Domain Maturity Roadmap** | Provide phased roadmap (visibility → prediction → optimization → automation) | ⚠ PARTIAL — NFR-022 covers extensibility but not formal domain maturity roadmap |
| 18 | **Business Rules & Workflow Configuration** | Configurable business rules, thresholds, workflows, routing, alerts, approvals, low-code | ✓ FR-027, FR-028, NFR-023, NFR-037 |
| 19 | **Alerting, Simulation, Prediction** | Provide alerting, simulation models, prediction capabilities, feedback loops | ✓ FR-010, FR-015, FR-016, FR-017 |
| 20 | **Data Archival & Reporting** | Data archival, reporting capabilities, historical records, analysis | ⚠ PARTIAL — NFR-020/021 cover DR but not detailed archival/reporting SLAs |
| 21 | **Security & Deployment** | Comply with Dubai Airports ISR/cybersecurity; support on-premise/cloud/hybrid | ✓ NFR-025, NFR-026 |
| 22 | **Multi-Channel Information Sharing** | Share dashboards, alerts, visualizations across videowalls, desktops, tablets, mobile | ✓ FR-031, FR-032, FR-033, NFR-028 |
| 23 | **Communication Tool Integration** | Integrate MS Teams, WhatsApp, SMS, Outlook, other tools for operational alerts/workflows | ✓ FR-034, FR-SYS-025 |

### Annexure VII Validation Summary

**Total Technical Capabilities:** 23  
**Fully Covered in My Inventory:** 16 (70%)  
**Partially Covered:** 4 (17%)  
**Gaps:** 3 (13%) — sustainability-specific KPIs, formal case management workflow, domain maturity roadmap

**Coverage:** 87% (20/23 adequately addressed)

---

## CROSS-VALIDATION MATRIX: V, VI, VII vs. My FR/NFR Inventory

| Annexure | Items | My Inventory Coverage | Gap Count | Gap Severity |
|---|---|---|---|---|
| **V. System Integration Register** | 17 integrations | 15 covered (88%) | 2 | 🟡 Medium (Kayvan, RealTimeDXB) |
| **VI. Use Case Compliance Matrix** | 8 use cases | 5.5 covered (69%) | 2.5 | 🟡 Medium (A2, A3, A7) |
| **VII. Technical Capability Matrix** | 23 capabilities | 20 covered (87%) | 3 | 🟡 Medium (sustainability, case mgmt, maturity roadmap) |

---

## NEW GAPS IDENTIFIED FROM V, VI, VII

### From Annexure V (System Integration Register)

#### GAP-INT-02: Kayvan Airside Mapping Platform

| Attribute | Specification |
|---|---|
| **Integration ID** | INT-02 (Annexure V) |
| **System** | Kayvan Airside Maps Platform |
| **Purpose** | Provide approved airside map data, geospatial references for airside visualization + operational context |
| **Data Exchanged** | Map layers, geospatial references, map services, location context |
| **Stakeholders** | AOCC, Airside Operations, Engineering Services |
| **Coverage in My Inventory** | ⚠ IDENTIFIED AS GAP in Glossary-to-Integration reconciliation; NOT in FR-SYS list |
| **Scope Tier** | base (explicitly in Annexure V as core integration) |
| **Modal Verb** | **shall** (core integration capability) |
| **Remediation** | Proposal must address: "Kayvan airside mapping integration: [native API / custom integration / not supported]. Map data flow: [real-time / batch]. Integration timing: [Phase 1 / Phase 2 / Phase 3]." |
| **Blocking?** | 🟡 HIGH — Core to airside visualization requirement |

#### GAP-INT-11: A-CDM / RealTimeDXB / ATFM Integration

| Attribute | Specification |
|---|---|
| **Integration ID** | INT-11 (Annexure V) |
| **System** | A-CDM / RealTimeDXB Platform + ATFM ANSP Coordination |
| **Purpose** | Coordinate TTOT/CTOT with ANSP; align with existing RealTimeDXB A-CDM visualization |
| **Data Exchanged** | TTOT, CTOT updates, ATC constraints, collaborative decision data |
| **Stakeholders** | AOCC, Airlines, ATC |
| **Coverage in My Inventory** | ⚠ IDENTIFIED AS ARCHITECTURAL CONFLICT in Glossary reconciliation; RealTimeDXB vs. Digital Twin SSOV mandate unclear |
| **Scope Tier** | base (explicitly in Annexure V as core integration) |
| **Modal Verb** | **shall** (core A-CDM support) |
| **Remediation** | Proposal must address: "RealTimeDXB coexistence with Digital Twin: [subsumption / parallel operation / integration as data source]. TTOT/CTOT coordination: [native A-CDM support / via RealTimeDXB / via AODB]. Clarify SSOV mandate interaction." |
| **Blocking?** | 🔴 CRITICAL — Architectural conflict with SSOV ("single operational source of visualization") mandate in Section 4 |

### From Annexure VII (Technical Capability Matrix)

#### GAP-CAP-14: Sustainability Analytics

| Attribute | Specification |
|---|---|
| **Capability ID** | CAP-14 (Annexure VII) |
| **Requirement** | Correlate energy, utilities, asset utilization, passenger flow for resource optimization + environmental reporting |
| **Coverage in My Inventory** | ⚠ PARTIAL — NFR-003 covers data quality but no sustainability-specific KPIs extracted |
| **Scope Tier** | base (explicitly in Annexure VII) |
| **Modal Verb** | **shall** (core capability) |
| **Remediation** | Proposal must address: "Sustainability analytics: [energy correlation / utility tracking / asset efficiency metrics]. Reporting: [carbon footprint / energy spend / optimization recommendations]. Baseline: [measurement period TBD]." |
| **Blocking?** | 🟡 MEDIUM — Environmental reporting may be regulatory/stakeholder requirement |

#### GAP-CAP-15: Operational Case & Incident Workflow

| Attribute | Specification |
|---|---|
| **Capability ID** | CAP-15 (Annexure VII) |
| **Requirement** | Convert alerts to cases, assign ownership, track escalation, log actions, capture evidence, support after-action review |
| **Coverage in My Inventory** | ⚠ PARTIAL — FR-016/036 cover decision-support recommendations but not formal case management |
| **Scope Tier** | base (explicitly in Annexure VII) |
| **Modal Verb** | **shall** (core capability) |
| **Remediation** | Proposal must address: "Case management workflow: [alert → case creation / ownership assignment / escalation routing / closure tracking]. Evidence capture: [screenshot / video clip / logs]. After-action: [post-incident review support]." |
| **Blocking?** | 🟡 MEDIUM — Case workflow critical for operational governance |

#### GAP-CAP-17: Digital Twin Domain Maturity Roadmap

| Attribute | Specification |
|---|---|
| **Capability ID** | CAP-17 (Annexure VII) |
| **Requirement** | Provide phased roadmap progress (visibility → prediction → optimization → automation) across domains |
| **Coverage in My Inventory** | ⚠ PARTIAL — NFR-022 covers extensibility/scalability but not formal maturity roadmap |
| **Scope Tier** | base (explicitly in Annexure VII) |
| **Modal Verb** | **shall** (core capability) |
| **Remediation** | Proposal must address: "Domain maturity roadmap: [visibility phase: when? / prediction phase: when? / optimization phase: when? / automation phase: when?]. Domains covered: [all / subset]. Progression criteria: [defined / TBD]." |
| **Blocking?** | 🟡 MEDIUM — Maturity roadmap critical for scope and timing expectations |

---

## FINAL CONSOLIDATED VALIDATION SUMMARY

### Complete Requirements Count Across ALL Annexures

| Source | Items | My Coverage | Gaps | Gap % |
|---|---|---|---|---|
| **Annexure III (Non-Functional Compliance)** | 43 questions | 15 addressed | 28 | 65% |
| **Annexure IV (Use Case Compliance)** | 8 use cases | 5.5 | 2.5 | 31% |
| **Annexure V (System Integration Register)** | 17 integrations | 15 | 2 | 12% |
| **Annexure VI (Technical Capability)** | 23 capabilities | 20 | 3 | 13% |
| **Annexure VI (Duplicate of IV)** | 8 use cases | 5.5 | 2.5 | 31% |
| **TOTAL (Unique)** | **91 items** | **55.5** | **35.5** | **39%** |

---

## UPDATED CRITICAL GAPS LIST (All Annexures)

### TIER 1: BLOCKING GAPS (7 from Annexure III + 2 new from V + 1 from IV/VI)

1. ✓ UAE Datacentre Residency (Annexure III, BU1)
2. ✓ RTO/RPO Targets (Annexure III, BU2–BU5)
3. ✓ Concurrent User Limits (Annexure III, PF2)
4. ✓ WCAG Accessibility (Annexure III, UC7)
5. ✓ Multi-Language/RTL (Annexure III, UC9–UC11)
6. ✓ API/Bandwidth Pricing (Annexure III, IN4)
7. ✓ DR Provider Disclosure (Annexure III, BU16)
8. 🔴 **NEW: RealTimeDXB/A-CDM Architectural Conflict** (Annexure V, INT-11)
9. 🟡 **NEW: Kayvan Airside Mapping Integration** (Annexure V, INT-02)

### TIER 2: HIGH-RISK GAPS (8+ from Annexure III + 4 new from VII)

- Referential integrity mechanisms
- Data format transparency
- Audit trail granularity
- Multi-tenant isolation
- Third-party tool integrations (IN1)
- Performance monitoring SLAs
- Concurrent-edit conflict resolution
- Data retention after contract end
- **NEW: Sustainability Analytics** (Annexure VII, CAP-14)
- **NEW: Case Management Workflow** (Annexure VII, CAP-15)
- **NEW: Domain Maturity Roadmap** (Annexure VII, CAP-17)
- **NEW: Data Archival/Reporting SLAs** (Annexure VII, CAP-20)

---

## CONCLUSION & NEXT STEPS

**Validation Complete:** All 7 annexures have been extracted and cross-validated.

**Key Finding:** Annexure VI is a **DUPLICATE of Annexure IV** — no new requirements.

**Updated Requirement Count:** 91 unique items (not 131 after removing VI duplication + consolidating overlaps)

**Updated Coverage:** 55.5/91 = **61% current inventory coverage**

**Action Items Before Proposal Validation:**
1. Add INT-02 (Kayvan) and INT-11 (RealTimeDXB) to system integration list
2. Clarify RealTimeDXB/Digital Twin SSOV architectural conflict
3. Add 4 new capability gaps from Annexure VII (sustainability, case mgmt, maturity roadmap, archival SLAs)
4. Update master FR/NFR inventory to 91 items with complete gap registry
5. Create consolidated proposal checklist against all 7 annexures

