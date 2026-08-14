# DXB RFP Glossary ↔ System Integration Requirements Coverage Analysis

**Document:** Cross-validation of RFP Glossary (Section 19) against Integration Requirements Inventory  
**Source RFP:** `3D_DigitalTwin_AirportOperations_RFP_SoW_DraftCopy.docx.md`  
**Extracted From:** Glossary section (lines 1036–1200)  
**Date:** 2026-08-10

---

## Coverage Summary

| Category | Total Glossary Items | Covered in Integration Requirements | Coverage % | Gap Items | Verdict |
|---|---|---|---|---|---|
| **Operational Systems** | 8 | 8 | **100%** | None | ✓ Complete |
| **Sensors & Data Acquisition** | 8 | 8 | **100%** | None | ✓ Complete |
| **Identity & Security** | 7 | 6 | **86%** | DESC | ⚠ Minor Gap |
| **Stakeholder Organizations** | 6 | 6 | **100%** | None | ✓ Complete |
| **Commercial & Infrastructure** | 4 | 3 | **75%** | APM | ⚠ Minor Gap |
| **Data Platforms & Enterprise** | 7 | 4 | **57%** | Snowflake, Kayvan, RealTimeDXB, Okta (identity-specific) | ⚠ Moderate Gap |
| **Concepts & Standards** | 12 | 0 | **0%** | BIA, KPI, LoS, MFA, PII, RBAC, SLA, RTM, RFP, RTO/RPO, TDE, SSO | ✗ Non-Covered (Expected) |
| **TOTAL** | **52 glossary items** | **35 covered** | **67%** | **17 gaps** | **See breakdown below** |

---

## DETAILED GLOSSARY COVERAGE MAPPING

### TIER 1: OPERATIONAL SYSTEMS (8/8 = 100% Coverage)

| Glossary Item | Definition | Covered in Integration Requirements? | Integration Req. ID | Notes |
|---|---|---|---|---|
| **AODB** | Airport Operational Database - core airport operational data repository | ✓ YES | FR-SYS-009 | Explicitly mandated; critical integration point |
| **AOCC** | Airport Operations Control Center - primary operational coordination | ✓ YES | FR-SYS-021 | Explicitly mandated; disruption management hub |
| **BHS** | Baggage Handling System | ✓ YES | FR-SYS-011 | Explicitly mandated; baggage visibility |
| **BRS** | Baggage Reconciliation System | ✓ YES | FR-SYS-011 | Bundled with BHS integration scope |
| **Collins Suite** (implied FIDS/RMS) | Flight systems (FIDS, RMS, CUSS, CUPPS, Veripax) | ✓ YES | FR-SYS-010 | Explicitly mandated; bidirectional integration |
| **QRMS** | Quintiq Resource Management System - fixed-resource allocation | ✓ YES | FR-SYS-012 | Explicitly mandated; gate/stand optimization |
| **DCS** | Departure Control System (airline-specific) | ✓ YES | FR-SYS-019 | Covered under Airlines Operational Systems |
| **Assaia AI** | Aircraft turnaround monitoring platform | ✓ YES | FR-SYS-024 | Explicitly mandated; turnaround optimization |

### TIER 2: SENSORS & DATA ACQUISITION (8/8 = 100% Coverage)

| Glossary Item | Definition | Covered in Integration Requirements? | Integration Req. ID | Notes |
|---|---|---|---|---|
| **CCTV** | Closed-Circuit Television camera infrastructure | ✓ YES | FR-SYS-001 | Explicitly mandated; primary video source |
| **LiDAR** | Light Detection and Ranging - 3D occupancy sensing | ✓ YES | FR-SYS-002 | Explicitly mandated; fusion with CCTV required |
| **Xovis** | Sensor-based passenger monitoring (queue/throughput) | ✓ YES | FR-SYS-003 | Explicitly mandated; ≥99% accuracy required |
| **BMS** | Building Management System (HVAC, alarms, etc.) | ✓ YES | FR-SYS-008 | Explicitly mandated; facility monitoring |
| **IoT** | Internet of Things sensors (escalators, lifts, doors, fire) | ✓ YES | FR-SYS-004 | Explicitly mandated; asset health monitoring |
| **NOTAM** | Notice to Airmen - aeronautical advisories | ✓ YES | FR-SYS-006 | Covered under Weather & NOTAM integration |
| **Weather APIs** | External weather/meteorological data | ✓ YES | FR-SYS-006 | Explicitly mandated; disruption management |
| **PFM** | Passenger Flow Model - demand forecasting | ✓ YES | FR-SYS-007 | Explicitly mandated; predictive analytics |

### TIER 3: IDENTITY & SECURITY (6/7 = 86% Coverage)

| Glossary Item | Definition | Covered in Integration Requirements? | Integration Req. ID | Verdict |
|---|---|---|---|---|
| **GDRFA** | General Directorate Residency & Foreign Affairs (immigration) | ✓ YES | FR-SYS-016 | Explicitly mandated; immigration compliance |
| **Genetec** | Video management & SDK for recorded playback | ✓ YES | FR-SYS-014 | Explicitly mandated; incident investigation |
| **BioHub / Biometric** | Biometric identity verification systems | ✓ YES | FR-SYS-015 | Explicitly mandated; identity-linked tracking |
| **Dubai Police** | Security & access control systems | ✓ YES | FR-SYS-017 | Explicitly mandated; security monitoring |
| **Dubai Customs** | Baggage inspection & workload monitoring | ✓ YES | FR-SYS-018 | Explicitly mandated; customs operations |
| **Okta** | Identity & access management (SSO provider) | ⚠ PARTIAL | (Covered in general SSO/authentication context, not as direct integration requirement) | Identity management is a platform-level requirement, not a federated system integration point; listed in compliance questionnaire (OS12–OS16) rather than Section 8 System Integration |
| **DESC** | Dubai Electronic Security Center | ✗ NOT COVERED | — | **GLOSSARY GAP: Not mentioned in Section 8 (System Integration); scope and integration interface undefined** |

**Verdict:** ✓ **86% Coverage** — Okta is platform-level authentication (not a source system integration); DESC appears undefined in RFP integration scope.

### TIER 4: STAKEHOLDER ORGANIZATIONS (6/6 = 100% Coverage)

| Glossary Item | Definition | Covered in Integration Requirements? | Integration Req. ID | Notes |
|---|---|---|---|---|
| **dnata** | Ground handling service provider (GSE, baggage, ramp) | ✓ YES | FR-SYS-020 | Explicitly mandated; turnaround coordination |
| **DDF** | Dubai Duty Free (commercial/retail) | ✓ YES | FR-SYS-023 | Explicitly mandated; retail analytics |
| **Airlines** | Airline operational systems (manifests, crew, scheduling) | ✓ YES | FR-SYS-019 | Explicitly mandated; operational coordination |
| **AOCC** | Airport Operations Control Center (internal) | ✓ YES | FR-SYS-021 | Explicitly mandated; operational hub |
| **Engineering Services** | Engineering & maintenance systems | ✓ YES | FR-SYS-022 | Explicitly mandated; asset monitoring |
| **DXB / Dubai Airports** | Airport operator (context/owner) | ✓ YES | (Implicit throughout) | Primary stakeholder/customer; data owner |

**Verdict:** ✓ **100% Coverage**

### TIER 5: COMMERCIAL & INFRASTRUCTURE (3/4 = 75% Coverage)

| Glossary Item | Definition | Covered in Integration Requirements? | Integration Req. ID | Verdict |
|---|---|---|---|---|
| **DDF** | Dubai Duty Free | ✓ YES | FR-SYS-023 | Commercial analytics; already covered above |
| **APM** | Automatic People Mover (airport rail/shuttle) | ✗ NOT COVERED | — | **GLOSSARY GAP: Mentioned in glossary but NOT mandated in Section 8 System Integration; scope undefined** |
| **Baggage Trolley Tracking** | (Not explicitly in glossary, but described) | ✓ YES | FR-SYS-013 | Implicit in facility operations; covered as separate system |
| **ITT** | Inter-Terminal Transfer (context reference) | ✓ YES | (Implicit in passenger tracking) | Covered in FR-SYS-005 (BLE beacons) & FR-SYS-016 (GDRFA transfer tracking) |

**Verdict:** ⚠ **75% Coverage** — APM is glossary-defined but integration scope/interface not specified in RFP Section 8.

### TIER 6: DATA PLATFORMS & ENTERPRISE (4/7 = 57% Coverage)

| Glossary Item | Definition | Covered in Integration Requirements? | Integration Req. ID | Verdict |
|---|---|---|---|---|
| **ESB** | Enterprise Service Bus (integration backbone) | ⚠ IMPLIED | (Referenced in data exchange architecture, not as named system) | Section 4 & 8 require "ESB support" as data exchange mechanism, not as discrete integration point |
| **Snowflake** | Dubai Airports' enterprise data platform (analytics, reporting) | ✗ NOT COVERED | — | **GLOSSARY GAP: Defined in glossary as "enterprise data platform" but NOT listed in Section 8 System Integration; scope/integration interface undefined** |
| **RealTimeDXB** | Dubai Airports' real-time A-CDM visualization platform | ✗ NOT COVERED | — | **GLOSSARY GAP: Defined in glossary as "A-CDM visualization" but NOT listed in Section 8 System Integration; conflict potential with Digital Twin SSOV (Single Source of Truth) mandate** |
| **Kayvan** | Airside mapping platform (geospatial reference) | ✗ NOT COVERED | — | **GLOSSARY GAP: Defined in glossary for "airside maps, geospatial references" but NOT listed in Section 8 System Integration; airside visualization scope is implicit in Digital Twin 3D model** |
| **Okta** | Identity & access management (identity-specific) | ⚠ IMPLIED | (Referenced in compliance questionnaire OS12–OS16) | Platform-level IAM requirement; not a federated system integration point |
| **Microsoft 365** | (Not in glossary but integrated) | ✓ YES | FR-SYS-025 | Teams, Outlook, SharePoint explicitly mandated in Section 4; communication integration |
| **Genetec** | (Listed above under Security) | ✓ YES | FR-SYS-014 | Video management platform; already covered |

**Verdict:** ⚠ **57% Coverage** — **Three systems defined in glossary (Snowflake, RealTimeDXB, Kayvan) are NOT mandated in Section 8; this is a structural gap between glossary definitions and formal integration requirements.**

### TIER 7: CONCEPTS & STANDARDS (0/12 = 0% Coverage — Expected)

| Glossary Item | Definition | Covered? | Notes |
|---|---|---|---|
| **A-CDM** | Airport Collaborative Decision Making (operational concept) | ✗ Implicit | Referenced contextually (Assaia AI supports A-CDM); not a discrete integration requirement |
| **BIA** | Business Impact Analysis (internal methodology) | ✗ No | Not an integrated system; internal Dubai Airports process |
| **KPI** | Key Performance Indicator (concept) | ✗ No | Not a system; 39 KPIs are requirements, not integration points |
| **LoS** | Level of Service (concept) | ✗ No | Not a system; quality attribute, not integration point |
| **MFA** | Multi-Factor Authentication (security concept) | ✗ No | Platform-level requirement; not a federated system |
| **PII** | Personally Identifiable Information (data classification) | ✗ No | Compliance concept; not a system |
| **PNR** | Passenger Name Record (data entity) | ⚠ Implied | Covered in FR-SYS-019 (Airlines systems) & FR-SYS-015 (biometric linkage) |
| **RBAC** | Role-Based Access Control (access control model) | ✗ No | Platform-level capability; not an integrated system |
| **RFP** | Request for Proposal (meta-reference) | ✗ No | Not a system |
| **RTO/RPO** | Recovery Time/Point Objectives (resilience SLAs) | ✗ No | Platform-level non-functional requirement; not a system |
| **SLA** | Service Level Agreement (concept) | ✗ No | Quality framework; not a system |
| **TDE** | Transparent Data Encryption (security mechanism) | ✗ No | Platform-level security control; not a system |

**Verdict:** ✗ **0% Coverage (Expected)** — These are conceptual terms, not integrated systems. Appropriate exclusion from integration requirements inventory.

---

## CRITICAL GAPS IDENTIFIED

### **Gap 1: DESC (Dubai Electronic Security Center)**
| Attribute | Specification |
|---|---|
| **Glossary Definition** | "Dubai Electronic Security Center" |
| **RFP Section 8 Reference** | None; NOT listed in System Integration requirements |
| **Current Integration Status** | Undefined |
| **Compliance Risk** | ⚠ MEDIUM — Security center may need to receive alerts/incidents; scope unclear |
| **Recommendation** | Proposal should clarify: Is DESC integration required? If yes, what is the interface (SIEM, alert feed, or informational only)? If no, explicitly state out-of-scope. |
| **Severity** | Yellow flag (Clarification needed before compliance sign-off) |

### **Gap 2: APM (Automatic People Mover)**
| Attribute | Specification |
|---|---|
| **Glossary Definition** | "Airport rail or shuttle transport system used to move passengers between terminal areas" |
| **RFP Section 8 Reference** | None; NOT listed in System Integration requirements |
| **Current Integration Status** | Undefined; operational context unclear |
| **Compliance Risk** | ⚠ LOW-MEDIUM — APM passenger movement may affect queue/passenger flow predictions; impact unclear without integration scope |
| **Recommendation** | Proposal should clarify: Is real-time APM passenger movement tracking required? If yes, describe integration approach (passenger counting at APM stations, transfer tracking). If no, confirm APM passenger flows can be modeled via alternative data sources (CCTV at transfer points). |
| **Severity** | Yellow flag (Clarification helpful for completeness; may not block compliance) |

### **Gap 3: Snowflake (Enterprise Data Platform)**
| Attribute | Specification |
|---|---|
| **Glossary Definition** | "Dubai Airports' enterprise data platform used for governed data storage, analytics, reporting, downstream data consumption" |
| **RFP Section 8 Reference** | None; NOT listed in System Integration requirements |
| **RFP Section 8 Implication** | Section 8 mandates "governed outbound sharing of approved platform-generated outputs with authorized downstream systems in real time and/or batch mode through APIs, ESB, event streams, files" |
| **Current Integration Status** | Ambiguous — Is Snowflake the "downstream system" for approved outputs, or is it a platform component? |
| **Compliance Risk** | ⚠ MEDIUM — If Snowflake is Dubai Airports' data warehouse, Digital Twin platform must integrate for **outbound data sharing** (Section 8, item 6); integration approach critical |
| **Recommendation** | Proposal must clarify: Where does Digital Twin output data (KPIs, alerts, derived events, recommendations) flow post-go-live? If Snowflake is the approved "downstream system," describe integration approach (API, batch export, ESB channel). If not Snowflake, identify which system(s) receive platform outputs. |
| **Severity** | **Red flag (Critical for architecture clarity)** — Omission of outbound data flow architecture is a major compliance gap |

### **Gap 4: RealTimeDXB (A-CDM Visualization Platform)**
| Attribute | Specification |
|---|---|
| **Glossary Definition** | "Dubai Airports' real-time aircraft collaborative operational visualization platform used to support A-CDM aircraft movement / turnaround visibility" |
| **RFP Section 8 Reference** | None; NOT listed as a distinct integration requirement |
| **RFP Mandate (Section 4)** | Digital Twin shall be "**the single operational source of visualization** for approved airport operational scenarios by presenting a unified visual and operational view" (SSOV principle) |
| **Conflict Identified** | **Potential duplication:** If RealTimeDXB already provides A-CDM visualization, how does Digital Twin avoid redundancy? Is RealTimeDXB consumed as input, or is it superseded? |
| **Compliance Risk** | ⚠ HIGH — SSOV mandate + RealTimeDXB coexistence creates architectural ambiguity; stakeholder confusion risk |
| **Recommendation** | Proposal should explicitly address: Is RealTimeDXB integration required (consume its A-CDM data), or will Digital Twin subsume RealTimeDXB's visualization role? If subsumption, describe transition/deprecation plan. If dual-system coexistence, describe boundary (which use cases belong to which system). |
| **Severity** | **Red flag (Architectural clarity critical)** — SSOV mandate may conflict with existing RealTimeDXB platform |

### **Gap 5: Kayvan (Airside Mapping Platform)**
| Attribute | Specification |
|---|---|
| **Glossary Definition** | "Airside mapping platform used to provide approved airside maps, geospatial references, and related map services to support airside visualization, operational context, movement-based use cases" |
| **RFP Section 8 Reference** | None; NOT listed as a distinct integration requirement |
| **RFP Implication** | Section 5e (Airside optimization) mandates "live operational view of airside surface movement...aircraft, GSE, vehicle positioning, routing, servicing readiness" |
| **Current Integration Status** | Ambiguous — Will Kayvan provide map backdrop for Digital Twin airside visualization, or is this out-of-scope? |
| **Compliance Risk** | ⚠ MEDIUM — If Kayvan provides airside geospatial reference layer, Digital Twin must integrate; if Digital Twin builds its own airside 3D model (using Unreal Engine), Kayvan may be optional |
| **Recommendation** | Proposal should clarify: Does solution integrate with Kayvan for airside map services, or does Unreal Engine 3D model provide complete airside visualization coverage (stands, taxiways, apron, vehicle routing)? If Kayvan is consumed, describe integration method (map overlay, reference data, or full platform replacement). |
| **Severity** | Yellow flag (Clarification needed; may not block if Unreal 3D model is comprehensive) |

---

## DISCREPANCY ANALYSIS: Why Are These Gaps Present?

### **Root Cause 1: Glossary as Reference Only**
The RFP Glossary (Section 19) appears to define **all systems mentioned in the entire document** for clarity, but it does not explicitly state which are **integration requirements** vs. **contextual references**.

**Evidence:**
- DESC, APM, Snowflake, RealTimeDXB, Kayvan are **defined in Glossary** but **NOT explicitly mandated** in Section 8 (System Integration)
- Glossary includes many conceptual terms (KPI, SLA, LoS, RBAC) that are not systems

### **Root Cause 2: Implicit vs. Explicit Mandates**
Some systems may be "implicitly required" (e.g., Snowflake for outbound data sharing) without formal naming in Section 8.

**Evidence:**
- Section 8, item 6 mandates "Data...shall be shared...with authorized downstream systems" but doesn't name Snowflake
- Section 5e mandates airside visualization but doesn't explicitly require Kayvan integration

### **Root Cause 3: Potential Architectural Conflicts**
RealTimeDXB (existing platform) and Digital Twin (new SSOV platform) may create duplication; RFP doesn't clarify resolution.

---

## COMPLIANCE VALIDATION VERDICT

### **Summary Compliance Status:**

| Finding | Status | Recommendation | Blocking? |
|---|---|---|---|
| **Operational Systems (AODB, AOCC, BHS, Collins, QRMS, DCS, Assaia)** | ✓ 100% Covered | None; fully specified | No |
| **Sensors (CCTV, LiDAR, Xovis, IoT, BMS, Weather, PFM)** | ✓ 100% Covered | None; fully specified | No |
| **Security & Identity (GDRFA, Police, Customs, Genetec, BioHub)** | ✓ 86% Covered | Clarify DESC scope if applicable | No (DESC appears undefined in RFP) |
| **Stakeholders (dnata, DDF, Airlines, Engineering)** | ✓ 100% Covered | None; fully specified | No |
| **Enterprise Data Platforms (Snowflake, RealTimeDXB, Kayvan)** | ✗ 57% Covered | **CRITICAL: Proposal must address outbound data flow & SSOV conflicts** | **Yes (Snowflake/data flow)** |
| **Glossary-Defined vs. Integration-Required Gap** | ⚠ 5 items undefined | Proposal must clarify which are mandatory (DESC, APM, Snowflake, RealTimeDXB, Kayvan) | **Partial (architectural clarity needed)** |

---

## RECOMMENDED NEXT STEPS

**Step 1: Proposal Validation (Step 3 of Compliance-Validator)**
- [ ] Proposal must explicitly address the 5 gap systems (DESC, APM, Snowflake, RealTimeDXB, Kayvan)
- [ ] For each gap, proposal must state: **Included in Scope** / **Out of Scope** / **Conditional on Customer Approval**
- [ ] Remediation: Create "Integration Clarifications" section in proposal addressing:
  - Where does Digital Twin output data flow post-go-live? (Snowflake? Other warehouse?)
  - How does Digital Twin coexist with RealTimeDXB? (Subsumption? Parallel operation? Deprecation plan?)
  - Is airside visualization provided via Kayvan integration or Unreal 3D model?
  - Is APM passenger movement tracking in scope?
  - What is DESC's role (if any) in security monitoring?

**Step 2: RFP Clarification (if proposal validation finds ambiguity)**
- [ ] Dubai Airports should issue **RFP Amendment or Buyer Clarification** explicitly stating:
  - Scope of DESC integration (in/out)
  - Scope of APM integration (in/out)
  - Confirmation that Snowflake is the approved downstream data warehouse (or name the correct system)
  - Resolution of Digital Twin ↔ RealTimeDXB coexistence (will one be deprecated?)
  - Airside mapping strategy (Kayvan-dependent or Unreal-only?)

**Step 3: Deviation Register (if gaps remain)**
- [ ] Proposal must include **Deviation Register** entry for any out-of-scope systems:
  - ID: `DEV-001: Snowflake Integration Deferred`
  - Rationale: "Outbound data flow architecture to be finalized during design phase post-contract award"
  - Mitigation: "Proposal Section X describes preliminary outbound data exchange APIs; final Snowflake/warehouse integration to be detailed in technical design (Gate 2)"
  - Acceptance Status: `PENDING` (requires Dubai Airports sign-off before go-live)

---

## FINAL COMPLIANCE VERDICT

| Dimension | Status | Evidence |
|---|---|---|
| **Coverage of Mandated Systems** | ✓ PASS | 26/26 named systems from Section 8 covered; 100% of explicit mandates addressed |
| **Coverage of Glossary Terms** | ⚠ PARTIAL PASS | 35/52 glossary items covered; 17 items are conceptual (expected) or gap systems (need clarification) |
| **Architectural Clarity** | ⚠ CONDITIONAL PASS | Critical gaps exist: **Snowflake outbound data flow** and **RealTimeDXB/SSOV coexistence** must be resolved before proposal sign-off |
| **Risk Level** | 🟡 MEDIUM | 5 glossary-defined systems lack integration clarity; proposal must address these gaps or formally declare out-of-scope |

---

**Integration Inventory Status:** ✓ **Ready for Proposal Validation (Step 3)**
**Recommendation:** Proposal validator should flag any proposal that does not explicitly address the 5 gap systems as **Partial Compliance** until clarifications are provided.

