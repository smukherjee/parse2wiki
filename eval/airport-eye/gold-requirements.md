# Gold Requirement Inventory — Airport Eye (APOC Phase 2)

**Purpose:** Independent fixed requirement set for scoring both eval drafts (Track A and Track B) against a single authoritative baseline. Extracted only from authoritative source documents; no draft output was read.

**Sources used (binding priority order — higher overrides lower):**
1. `sources/Airport Eye/Change Request Aiport Eye - APOC Phase 2.pdf.md` — CR / BRD v1.5 (binding)
2. `sources/Airport Eye/Airport Eye Additional Busnes Requirements- 2-July-2026.docx.md` — ABR
3. `sources/Airport Eye/PE_OT System_09.06.pptx.md` — PE_OT final OT-systems list
4. `sources/Airport Eye/Airport_Eye_RFP_v5.docx.md` — base RFP
5. `sources/Airport Eye/AirportEye_Requirements_Register_v5.xlsx.md` and `sources/Airport Eye/Final requirements.xlsx.md` — requirements registers

**Extraction method:** Manual union of explicit + implicit requirements across all five source tiers, deduplicated near-identical items (kept one row, noted the others), conflicts resolved in favour of the higher-priority document with the conflict recorded in Notes. Cross-checked for completeness against `compliance-report-numeric-inventory.md`, `requirements-traceability-matrix.md`, and `build_rtm.py` (source-derived artifacts only).

**Conflict-resolution rule applied:** CR/BRD + ABR override the base RFP. Where the RFP and registers differ from the BRD, the BRD value is binding and the conflict is noted. Register-only values (RTO/RPO, 24x7 support, additional roles, area/point counts) are treated as binding content requirements sourced from the registers (tier 5) where they do not conflict with a higher tier.

**Total count: 189 requirements** (125 categorical + 64 numeric rows that also appear in the parity sub-table).

**Category breakdown:** Submission-format 16 | Content 25 | Substantive 69 | Procedural 15 | Numeric 64 (sum = 189).

**Mandatory breakdown:** Yes 186 | No 3 (G-095 Structural Integrity agent — conditional on SHM sensor procurement; G-134 ABR SPG simulation use cases — coverage graded; G-148 DIAL reserved rights — procedural acknowledgment).

**Category legend:** Submission-format | Content | Substantive | Procedural | Numeric
**Mandatory legend:** Yes = disqualifying if missed; No = points deducted

---

## 1. Master Requirement Table

| ID | Category | Requirement | Binding value / operator | Mandatory? | Source | Notes |
|---|---|---|---|---|---|---|
| G-001 | Submission-format | Submit Volume 1 — Executive Summary, max 10 pages | shall, ≤10 pages | Yes | RFP §9.3 | RFP only; BRD silent. |
| G-002 | Submission-format | Submit Volume 2 — Technical Proposal (architecture, methodology, compliance with all RFP requirements) | shall provide | Yes | RFP §9.3 | |
| G-003 | Submission-format | Submit Volume 3 — AI and Analytics Proposal (per-agent approach, training-data strategy, governance) | shall provide | Yes | RFP §9.3 | |
| G-004 | Submission-format | Submit Volume 4 — Implementation Plan (programme, resource plan, risk register, QA plan) | shall provide | Yes | RFP §9.3 | |
| G-005 | Submission-format | Submit Volume 5 — Commercial Proposal (itemised INR excl. GST, SLA terms, TCO) | shall provide | Yes | RFP §9.3 / §10 | Do not alter table structure; declare assumptions. |
| G-006 | Submission-format | Submit Volume 6 — Qualifications & References (company profile, ≥3 case studies, client references) | shall provide, ≥3 case studies | Yes | RFP §9.3 | Min 3 case studies. |
| G-007 | Submission-format | Submit Volume 7 — Appendices (CVs of key personnel, 3rd-party licences, subcontractor declarations, ISO certs) | shall provide | Yes | RFP §9.3 | |
| G-008 | Submission-format | Electronic submission via procurement portal by stated deadline | shall | Yes | RFP §9.3 / cover page | |
| G-009 | Numeric | Proposal validity ≥180 calendar days from submission deadline | ≥180 days | Yes | RFP §9.1 | RFP only. |
| G-010 | Submission-format | Pre-qualification: ≥5 years demonstrated experience in digital twin / BIM / geospatial platform dev & deployment | shall satisfy | Yes | RFP App. E | Disqualifying gate. |
| G-011 | Submission-format | Pre-qualification: ≥2 comparable deployments in airport / transport infrastructure / large built environment | shall satisfy, ≥2 | Yes | RFP App. E | |
| G-012 | Submission-format | Pre-qualification: ISO 9001:2015 QMS certification current & valid | shall hold | Yes | RFP App. E | |
| G-013 | Submission-format | Pre-qualification: ISO/IEC 27001:2013 ISMS certification current & valid | shall hold | Yes | RFP App. E | |
| G-014 | Submission-format | Pre-qualification: annual turnover ≥ INR [X] crore in each of last 3 financial years (audited) | shall satisfy | Yes | RFP App. E | Threshold value left blank in RFP ([X]). |
| G-015 | Submission-format | Pre-qualification: no pending insolvency / significant legal disputes / adverse regulatory actions | shall satisfy | Yes | RFP App. E | |
| G-016 | Submission-format | All costs in Indian Rupees (INR), exclusive of GST; do not alter commercial table structure; declare assumptions separately | shall | Yes | RFP §10 / BRD §6 | |
| G-017 | Procedural | Three-stage evaluation: mandatory compliance → technical → commercial, in that order | shall | Yes | RFP §9.1 | |
| G-018 | Numeric | Evaluation weights: Technical 30% / Experience 25% / AI 20% / Commercial 15% / Implementation 10% | =30/25/20/15/10 % | Yes | RFP §9.2 | |
| G-019 | Submission-format | Provide Software Bill of Materials (SBOM) for all third-party components, properly licensed for DIAL use | shall provide | Yes | RFP §9.3 (IP) | |
| G-020 | Content | Deliverable D-01: Project Execution Plan, BIM Execution Plan (BEP), Data Management Plan | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-021 | Content | Deliverable D-02: Airborne LiDAR point cloud (classified LAS/LAZ), DTM, DSM, Orthophoto datasets | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-022 | Content | Deliverable D-03: Geospatial accuracy assessment report + survey metadata conforming to ISO 19115 | shall deliver | Yes | BRD §4.2 / §3.1.9 D-07 / RFP §5.2 | |
| G-023 | Content | Deliverable D-04: Indoor LiDAR point cloud datasets (all buildings) | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-024 | Content | Deliverable D-05: IFC-compliant federated BIM models for all specified assets to agreed LOD | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-025 | Content | Deliverable D-06: Asset Attribute Data Register (fully populated, imported to CAFM/CMMS) | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-026 | Content | Deliverable D-07: Existing Data Migration Report + Legacy Data Quality Assessment | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-027 | Content | Deliverable D-08: Deployed & tested Digital Twin Platform (UAT sign-off) | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-028 | Content | Deliverable D-09: BMS/IoT Integration Report (all integrated data points verified) | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-029 | Content | Deliverable D-10: AI Monitoring & Predictive Intelligence Platform (all agents operational) | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-030 | Content | Deliverable D-11: API documentation portal + integration test reports | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-031 | Content | Deliverable D-12: Cybersecurity Assessment Report + Penetration Test Report | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-032 | Content | Deliverable D-13: Training Materials, User Manuals, Administrator Documentation | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-033 | Content | Deliverable D-14: As-Built Documentation for all platform components | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-034 | Content | Deliverable D-15: Post-implementation review report (90 days after go-live) | shall deliver | Yes | BRD §4.2 / RFP §5.2 | |
| G-035 | Content | BIM models IFC 4.0 (ISO 16739) compliant | shall comply | Yes | RFP §3.2.2 / BRD Obj. 2 | |
| G-036 | Content | Full compliance with ISO 19650 for BIM information management across asset lifecycle | shall comply | Yes | BRD Obj. 2 / RFP §3.2.2 | |
| G-037 | Content | Compliance with PAS 1192-2:2013 and BS EN ISO 19650-2:2019 for project delivery | shall comply | Yes | RFP §3.2.2 | |
| G-038 | Content | Comply with DIAL's BIM Execution Plan (BEP) and Asset Information Requirements (AIR) | shall comply | Yes | RFP §3.2.2 / App. B | BEP/AIR to be issued by DIAL. |
| G-039 | Content | Deliver a Requirements Traceability Matrix mapping each requirement to proposal response | shall provide | Yes | RFP §9.3 Vol. 2 / register convention | Implied by "compliance with all RFP requirements"; confirmed by RTM convention. |
| G-040 | Substantive | Airborne LiDAR survey of airport + Aerocity + 5 km buffer beyond boundary (~200 sq km total) | shall conduct | Yes | BRD §3.1.1 / RFP §3.1.1 | |
| G-041 | Numeric | Airborne LiDAR min point density within airport boundary | ≥20 pts/m² | Yes | BRD §3.1.1 / RFP §3.1.2 | |
| G-042 | Numeric | Airborne LiDAR min point density in buffer zones | ≥8 pts/m² | Yes | BRD §3.1.1 / RFP §3.1.2 | |
| G-043 | Numeric | Horizontal accuracy RMSE (verified against independent GCPs) | ≤5 cm | Yes | BRD §3.1.1 / KPI 5 / RFP §3.1.2 | |
| G-044 | Numeric | Vertical accuracy RMSE (verified against independent benchmarks) | ≤3 cm | Yes | BRD §3.1.1 / KPI 5 / RFP §3.1.2 | |
| G-045 | Numeric | RGB orthophotography ground sampling distance (GSD) | ≤5 cm | Yes | BRD §3.1.1 / RFP §3.1.2 | |
| G-046 | Substantive | Classified point cloud in ASPRS LAS 1.4 format | shall deliver | Yes | BRD §3.1.1 / RFP §3.1.2 | |
| G-047 | Numeric | DTM and DSM grid resolution | =10 cm | Yes | BRD §3.1.1 / RFP §3.1.2 | |
| G-048 | Numeric | Contour dataset interval | =10 cm | Yes | BRD §3.1.1 / RFP §3.1.2 | |
| G-049 | Substantive | 3D mesh models (OBJ/FBX, georeferenced) + 10 cm contours | shall deliver | Yes | BRD §3.1.1 / RFP §3.1.2 | |
| G-050 | Substantive | Full flight report, sensor calibration certificate, GCP survey report | shall deliver | Yes | BRD §3.1.9 D-06 / RFP §3.1.3 | |
| G-051 | Substantive | All raw/processed data in formats compatible with ESRI ArcGIS and Autodesk | shall deliver | Yes | BRD §3.1.1 / RFP §3.1.2 | |
| G-052 | Substantive | Landside coverage: aircraft/satellite scans ~225 acres incl. Hospitality/Gateway/Downtown; DTM/DSM/DEM/contours/spot levels + orthophotos; external building mapping | shall deliver | Yes | BRD §3.1.2 | DEM + 3x3 m spot levels required by BRD. |
| G-053 | Substantive | Underground utility scanning using GPR + DGPS + GNSS + 12D model for landside roads | shall deliver (all 4 methods) | Yes | BRD §3.1.2 | All four methods binding; partial = shortfall. |
| G-054 | Substantive | Landside GIS topographic layers: land use, parcels, road networks, street view, zoning, topography, wetlands, demographics, land cover, imagery, basemap | shall provide (10-layer catalogue) | Yes | BRD §3.1.2 | |
| G-055 | Substantive | Airside coverage: layer-wise scanning for Runway, Taxiway, Apron, Isolation Bay, Perimeter Road, associated structures/drains | shall deliver | Yes | BRD §3.1.3 | |
| G-056 | Substantive | Airside GIS layers including AGL, PAPI Lights, DVOR, Signage, RVR, MSSR, AMSR and other NAVAIDs + ancillary buildings | shall provide | Yes | BRD §3.1.3 | |
| G-057 | Substantive | Terminal coverage: building mapping where layouts unavailable; update additions/deletions/modifications on ground | shall deliver | Yes | BRD §3.1.4 | |
| G-058 | Substantive | Indoor mobile + terrestrial LiDAR scanning of all terminals, satellite structures, VIP facilities, cargo warehouses, maintenance hangars, built structures | shall conduct | Yes | BRD §3.1.5 / RFP §3.2.1 | |
| G-059 | Numeric | Indoor positional accuracy RMSE (horizontal & vertical) post cloud-to-cloud registration | ≤5 cm | Yes | BRD §3.1.5 / RFP §3.2.1 | |
| G-060 | Substantive | All indoor scans registered to airborne LiDAR coordinate system for seamless indoor-outdoor continuity | shall | Yes | BRD §3.1.5 / RFP §3.2.1 | |
| G-061 | Content | BIM models to LOD by asset category: Structural 300, Architectural 300, HVAC 350, Electrical 350, Plumbing 300, Fire 350, Security 300, IT 200, Airside 200, Passenger Handling 300 | shall (per LOD table) | Yes | BRD §3.1.8 / RFP §3.2.3 | |
| G-062 | Content | BIM models for T1 (Basement 17085, Apron 77581, Arrival 43228, Departure 64007, Food Court 11495 sq.m) + asset attribution + MEP overlay (HVAC, FDAS, Zonal Temp) | shall deliver | Yes | BRD App. A / Register BIMM-T1 | Areas from register. |
| G-063 | Content | BIM models for T2 (Departure 27028, Mezzanine 2061, Arrival 33429 sq.m) + asset attribution + MEP overlay | shall deliver | Yes | BRD App. A / Register BIMM-T2 | |
| G-064 | Content | BIM models for T3 (Basement-2 32396, Basement-1 35340, Apron 74987, Arrival 84770, Mezzanine 58258, Departure 159126, CIP 30240, Office 10650, Hotel 10608 sq.m) + asset attribution + MEP overlay | shall deliver | Yes | BRD App. A / Register BIMM-T3 | |
| G-065 | Content | BIM models per building-specific LOD schedule in Appendix A (T1/T2/T3, NUB, substations, cargo, ACLCs, ATCs, GA terminal, Centaur, metro, parking, etc.) | shall (per App. A LOD) | Yes | BRD §3.1.6 / §3.1.7 / App. A | 25 landside + 8 airside LOD assignments. |
| G-066 | Substantive | Legacy CAD audit + CAD-to-BIM conversion (architectural + MEP) + reconciliation with LiDAR findings + CAFM/CMMS attribute population + Data Quality Report | shall | Yes | BRD §3.2.1 / RFP §3.3.1 | |
| G-067 | Substantive | GIS-BIM integration: import BIM into GIS; establish DB connections; interactive pop-ups; multi-scale viz (point clouds, orthophotos, terrain, 3D mesh, BIM) | shall | Yes | BRD §3.2.2 / RFP §3.3 | |
| G-068 | Substantive | Federated BIM platform: concurrent multi-discipline coordination w/ clash detection; version control + audit trail; granular RBAC; native IFC + CDE; API integration with DT viewer & AI platform; ISO 19650 | shall | Yes | BRD §3.2.3 / RFP §3.3.2 | |
| G-069 | Substantive | Outdoor 3D GIS Platform: high-perf web 3D viewer (LiDAR/orthophotos/DTM-DSM/3D mesh/multi-scale); multi-department data layering (SHP/GeoJSON/KML/IFC/CAD); planning & scenario viz (existing vs proposed); collaborative redlining + commenting + version control; sharing/publishing (PDF/snapshots/extracts); NL query for GIS data | shall | Yes | BRD §3.4.6 / RFP §3.6 | |
| G-070 | Substantive | Land & Space Management: digital footprint of all land/spaces w/ attributes (area, dimensions, usage, licensee, contract periods, historical trail); allotment repository; multi-dimensional queries; Master Plan overlay; unauthorized-use alerts; CLM integration; Master Plan/Revenue Map/satellite overlay; digital land classification (demised/additional demised/excluded/carved-out/MCD/DCB) | shall | Yes | BRD §3.3.1 | |
| G-071 | Substantive | Systems integration for maintenance: link BMS, LCMS, ECMS, CMS, FDAS, BHS, HBS, VDGS, VHT, ATRS, DFMD, PBB, WTP/STP, AGL CMS, IoT projects; single platform for Terminal & Airside BMS/VHT/BHS/ALS/HVAC/LCMS/ECMS; all IT-BMS KPIs in single platform; control of lights ON/OFF from APOC | shall | Yes | BRD §3.3.2 / App. E | |
| G-072 | Substantive | Pre-maintenance & planning: terrain/topography analysis; soil/hydrological assessments; environmental data (noise contours, flood zones, air quality); Master Plan integration; noise contour maps; flood-prone zones integration; urban heat island analysis; disaster-prone zone mapping w/ basemaps; geospatial evacuation routes | shall | Yes | BRD §3.3.3 | |
| G-073 | Substantive | IoT sensor integration: machine-room pumps (40); T1 roof sensors (12); DGA in transformers; ATRS bag count + DFMD count for passenger flow; uptime monitoring of critical equipment; underground network mapping (cable/drain/RWH); cityside horticulture/streetlights/substations | shall | Yes | BRD §3.3.4 / App. E / Register | |
| G-074 | Substantive | Environmental monitoring: Shahabad MdPur (IMD, STP, ISWMC); Noise Monitoring Terminals in funnel areas + Nursery CAQM Station | shall | Yes | BRD §3.3.5 / App. E | |
| G-075 | Substantive | Digital Twin viewer: web-based 3D GIS+BIM viewer (simultaneous GIS basemap, imagery, point cloud, 3D mesh, BIM geometry); seamless indoor/outdoor nav w/ auto LOD; real-time BMS overlay on BIM w/ colour-coded condition indicators; customisable dashboards/measurement/annotation/task-assignment integrated w/ CAFM/CMMS; AR/VR for maintenance & training; full mobile responsiveness w/ offline capability | shall | Yes | BRD §3.4.1 / RFP §3.5.1 | |
| G-076 | Substantive | BMS/IoT ingestion middleware supporting BACnet/IP, BACnet MSTP, Modbus TCP, Modbus RTU, MQTT v3.1.1 & v5.0, SNMP, OPC-UA, RESTful APIs, proprietary vendor connectors | shall | Yes | BRD §3.4.2 / RFP §3.4.1 | |
| G-077 | Substantive | Normalise all ingested data into unified semantic model conforming to DTDL (or DIAL-approved equivalent); every BMS data point mapped to a BIM element; configurable geofencing + zone monitoring w/ aggregated metrics | shall | Yes | BRD §3.4.2 / RFP §3.4 | |
| G-078 | Substantive | APOC integration: standardised REST + GraphQL APIs bidirectional w/ APOC & CCC; integration w/ third-party airline & ground handler systems; national Smart City & urban mobility platforms; WebSocket real-time feeds | shall | Yes | BRD §3.4.3 / RFP §4.1 | |
| G-079 | Numeric | API backwards compatibility for minimum major versions | ≥2 major versions | Yes | BRD §3.4.3 / RFP §4.1 | |
| G-080 | Substantive | API design: RESTful per OpenAPI 3.0 w/ interactive portal; GraphQL for nested queries; WebSocket for real-time; all versioned | shall | Yes | RFP §4.1 | |
| G-081 | Substantive | RBAC w/ min 5 default roles (Executive, Operations, Maintenance, Security, Guest/Visitor) + additional roles (AOCC, P&E, Airside ops, Terminal Ops, S&V, Commercial & Retail, Env & Sustainability, IT & Digital, Emergency Response & BC) | shall (≥5 + additional) | Yes | BRD §3.4.4 / RFP §3.5.2 / Register NFR | Register expands role set. |
| G-082 | Substantive | SSO integrated w/ DIAL IdP via SAML 2.0 or OAuth 2.0; MFA enabled | shall | Yes | BRD §3.4.4 / RFP §3.5.2 / Register NFR | |
| G-083 | Numeric | Data-in-transit encryption TLS version | =TLS 1.3 | Yes | BRD §3.4.4 / RFP §3.5.2 | Register says "TLS 1.2+"; BRD/RFP bind TLS 1.3. Conflict: binding = TLS 1.3. |
| G-084 | Numeric | Data-at-rest encryption cipher | =AES-256 | Yes | BRD §3.4.4 / RFP §3.5.2 | |
| G-085 | Numeric | Activity audit log retention | ≥2 years | Yes | BRD §3.4.4 / RFP §3.5.2 | |
| G-086 | Substantive | Cybersecurity: full risk assessment prior to deployment (findings to DIAL); IEC 62443 compliance for all OT/IT; network segmentation IT/OT/internet (defence-in-depth); penetration testing of internet-facing components pre-go-live; SIEM continuous monitoring; national data-protection compliance; data backup & security; privileged access management | shall | Yes | BRD §3.4.5 / RFP §4.2 | |
| G-087 | Substantive | AI orchestration framework: centralised engine managing data routing, alert aggregation, priority scoring, cross-agent correlation; deploy/update/retire/version agents without platform downtime; common data bus; AI Model Management interface (review performance, retrain, approve updates) | shall | Yes | BRD §3.5.2 / RFP §6.2 | |
| G-088 | Numeric | Mandatory domain AI agents (BRD §3.5.3 list) | =8 agents | Yes | BRD §3.5.3 / RFP §6.3 | RFP §6.3 lists 6; BRD §3.5.3 lists 8 (adds Passenger Flow + Structural Integrity). Binding = 8. |
| G-089 | Substantive | AI agent — Mechanical & HVAC Monitoring: AHUs, chillers, cooling towers, pressurisation, ventilation fans, BAS controllers; anomaly detection (vibration, temp, airflow, pressure); chiller/compressor failure prediction up to 72h; energy optimisation recommendations; automated CMMS work orders | shall | Yes | BRD §3.5.3 / RFP §6.3.1 | |
| G-090 | Substantive | AI agent — Electrical Systems Monitoring: transformer rooms, UPS, switchgear, distribution boards, emergency power; power-quality analysis; UPS battery SoH; predictive load balancing; transformer DGA insulation-failure prediction (deferred until MRSS upgrade unblocks feed) | shall | Yes | BRD §3.5.3 / RFP §6.3.2 / Register AI-11 | DGA conditional on MRSS upgrade. |
| G-091 | Substantive | AI agent — Fire Safety & Life Safety: multi-sensor correlation (smoke/heat/CO/optical) genuine vs nuisance; suppression pressure/flow monitoring; real-time evacuation modelling; edge inference for ≤5s latency; advisory only, never suppresses FACP alarm | shall | Yes | BRD §3.5.3 / RFP §6.3.4 / Register AI-14 | |
| G-092 | Substantive | AI agent — Water & Drainage: potable/chilled/grey water & stormwater; leak detection (pressure/flow); tank levels, pump health, water quality; stormwater runoff modelling w/ weather forecast; roof high-water alerts from 12 T1 sensors | shall | Yes | BRD §3.5.3 / RFP §6.3.5 / Register AI-12 | |
| G-093 | Substantive | AI agent — Energy Management & Sustainability: real-time EUI by zone/terminal/function; energy waste detection; carbon reduction tracking vs DIAL targets; day-ahead (24h) load forecast | shall | Yes | BRD §3.5.3 / RFP §6.3.6 / Register AI-06 | |
| G-094 | Substantive | AI agent — Passenger Flow Monitoring: real-time flow mapping; congestion prediction; ATRS bag count + DFMD count; queue build-up 45min ahead; SLA-breach early warnings; advisory staffing/lane-opening | shall | Yes | BRD §3.5.3 / Register AI-13 | Not in RFP §6.3 but in BRD §3.5.3 + RFP §6.5 table. Binding = mandatory. |
| G-095 | Substantive | AI agent — Structural Integrity Monitoring: long-term structural performance; modal/frequency analysis; settlement & movement; 7-day risk early warnings. CONDITIONAL: cannot start until DIAL procures/installs SHM sensor network + ≥6-12 month baseline | shall (conditional) | No | BRD §3.5.3 / Register AI-16 | Conditional scope; points deducted if unaddressed, not disqualifying. |
| G-096 | Substantive | AI agent — Security & Perimeter: PSIM/access-control/CCTV/perimeter integration; anomalous access behaviour analytics; perimeter-CCTV correlation; crowd density; read-only, privacy-preserving, role-scoped; subject to CISF approval | shall | Yes | BRD §3.5.3 / RFP §6.3.7 / Register AI-15 | |
| G-097 | Substantive | AI agent — NL Query: natural-language query over platform data (assets, telemetry, alerts, CMMS work orders, O&M docs); read-only, grounded w/ citations, explicit "I don't have that data" path, role-based filtering | shall | Yes | Register AI-10 | Register-only; supports RFP §6.2 intent. |
| G-098 | Substantive | AI governance — Explainability: every Agentic alert accompanied by plain-language explanation + % confidence score; deep learning uses SHAP/LIME/attention visualisation (no black box) | shall | Yes | BRD §3.5.5 / RFP §6.4 | |
| G-099 | Substantive | AI governance — Auditability: complete audit log of all AI alerts (input data, model version, timestamp, operator response) | shall | Yes | BRD §3.5.5 / RFP §6.4 | |
| G-100 | Substantive | AI governance — Feedback Loop: operators can provide feedback on alert accuracy/relevance, used in retraining cycles | shall | Yes | BRD §3.5.5 / RFP §6.4 | |
| G-101 | Substantive | AI governance — Model Version Control: all versions documented & retained; rollback achievable within 4 hours | shall | Yes | BRD §3.5.5 / RFP §6.4 | |
| G-102 | Substantive | AI governance — DIAL Ownership: DIAL owns all AI model weights and training data generated under contract | shall (DIAL exclusive) | Yes | BRD §3.5.5 / §9.10 / RFP §9.3 | |
| G-103 | Substantive | AI Data Readiness Gate: per-domain data audit before agent build (≥12mo usable history, tag-to-asset mapping, data quality); publish Data Readiness Report; agree day-1 benchmarks w/ DIAL | shall | Yes | Register AI-01 | Register-only; material to M5 acceptance. |
| G-104 | Substantive | Shared AI Platform: ingestion from middleware, TimescaleDB historian, shared feature store, MLflow model registry, explainability service, alert pipeline, CMMS/AMMS work-order connector | shall | Yes | Register AI-02 | |
| G-105 | Substantive | AI MLOps: monthly drift monitoring; quarterly retraining (or drift/feedback-triggered); DIAL approval before every production release; rolling 90-day KPI window; Quarterly AI Performance Report | shall | Yes | Register AI-05 | |
| G-106 | Substantive | AI per-agent acceptance: each agent accepted individually against its §6.5 row on rolling 90-day window; M5 + D-10 achieved when all wave gates passed | shall | Yes | Register AI-17 | |
| G-107 | Numeric | Mechanical & HVAC agent — min precision / recall / prediction horizon / alert latency | ≥82% / ≥78% / ≤72h / ≤30s | Yes | BRD §3.5.4 / RFP §6.5 | |
| G-108 | Numeric | Electrical Systems agent — min precision / recall / horizon / latency | ≥80% / ≥75% / ≤48h / ≤30s | Yes | BRD §3.5.4 / RFP §6.5 | |
| G-109 | Numeric | Passenger Flow agent — min precision / recall / horizon / latency | ≥85% / ≥80% / ≤45min / ≤15s | Yes | BRD §3.5.4 / RFP §6.5 | |
| G-110 | Numeric | Structural Integrity agent — min precision / recall / horizon / latency | ≥90% / ≥85% / ≤7d / ≤60s | Yes | BRD §3.5.4 / RFP §6.5 | Conditional agent (G-095). |
| G-111 | Numeric | Fire Safety agent — min precision / recall / horizon / latency | ≥95% / ≥95% / real-time / ≤5s | Yes | BRD §3.5.4 / RFP §6.5 | |
| G-112 | Numeric | Energy Management agent — min precision / recall / horizon / latency | ≥80% / ≥75% / ≤24h / ≤60s | Yes | BRD §3.5.4 / RFP §6.5 | |
| G-113 | Numeric | Security agent — min precision / recall / horizon / latency | ≥88% / ≥82% / real-time-15min / ≤10s | Yes | BRD §3.5.4 / RFP §6.5 | |
| G-114 | Numeric | Aggregate predictive alert accuracy (KPI 4) | ≥80% precision, ≥75% recall | Yes | BRD §2.3 KPI 4 / App. C | Overall KPI; per-agent standards in G-107..G-113 are stricter per-agent. |
| G-115 | Substantive | Integrate T1 OT systems: HVAC (JCI), FDAS (Edwards), VHT (TKE), ECMS (Schneider), PBB (TKE), VDGS (TKE), BHS (Vanderlande), ATRS (SJK), GPU/PCA (JCI) | shall integrate | Yes | Register INTF-T1-* / PE_OT | Point counts in numeric sub-table. |
| G-116 | Substantive | Integrate T2 OT systems: HVAC, FDAS (Edwards), VHT, PBB (upcoming), BHS; (ECMS/VDGS/LCMS/ATRS/GPU not present — Phase 2) | shall integrate (where present) | Yes | Register INTF-T2-* / PE_OT | Some systems not present at T2. |
| G-117 | Substantive | Integrate T3 OT systems: HVAC (Honeywell), FDAS (Notifire), VHT (TKE), PBB (TKE/Shinmawya), VDGS (SafeGate), BHS (Vanderlande), ATRS (SJK), GPU/PCA (JCI) | shall integrate | Yes | Register INTF-T3-* / PE_OT | |
| G-118 | Substantive | Integrate Common OT systems: WTP (Schneider), STP (Schneider), MRSS (GE), Airside Solar SCADA (Trinity + Locus), AGL CMS (Honeywell), ITBMS (JCI multi-system incl. partial FDAS), Noise monitoring, Access Control | shall integrate | Yes | Register INTF-CM-* / PE_OT | |
| G-119 | Substantive | LCMS (T1/T3) and ECMS T3 integration (systems need upgrade — Phase 2); VDGS upgrade Mar 2027; MRSS upgrade Mar 2027 | shall (when upgrade complete) | Yes | Register INTF-T*-LCMS / PE_OT | Conditional on OEM upgrade. |
| G-120 | Substantive | IT/OneAPOC integrations: UTAM, Telematics, AODB, ADS-B, ARC, RMS, Kloudspot, XOVIS, PTM, SAC, ITOM/ManageEngine, Reverse PaxFlow, VMS/CCTV, GIS (ArcGIS), SAP, DigiYatra, CUSS, CUPPS, SBD, check-in counters, boarding gate scanners, baggage scanners, FIDS, AFTN | shall integrate | Yes | Register Integrations-IT | Part of OneAPOC program. |
| G-121 | Substantive | Ops DT — Airside ops: GSE near-realtime positions; flight position 10mi→landing→runway→taxiway→stand (& reverse); turnaround monitoring w/ RAG; airside alerts; airside KPIs (ATM/OTP/stand & gate utilization/slot); turnaround metrics (TOBT/EIBT); predictive turnaround (POBT/PRBT/PIBT); RVR/weather; live CCTV; safety & compliance (speed violation/path deviation/geofence breach/GSE route adherence); airside playback; NOTAM alerts w/ highlighted area | shall | Yes | Register FR-DTW-AOPS-* | |
| G-122 | Substantive | Ops DT — Terminal ops: consolidated KPI summary (entry/check-in/security/immigration/emigration/transfer/customs/gates/retail/F&B); spatial navigation terminal→floor→zone→touchpoint w/ KPIs; queue management (length/wait/processing across touchpoints); crowd heatmaps; dwell & journey time; retail/F&B store performance; store location analysis; camera access; counter/desk allocation & utilization; historical terminal playback | shall | Yes | Register FR-DTW-TOPS-* | |
| G-123 | Substantive | Ops DT — Curbside: KPI summary; live vehicle monitoring; vehicle classification; curb occupancy & RAG; vehicle dwell time; incident identification (overstay/violations); congestion heatmap; ground transport availability; crown monitoring (meet-and-greet); parking monitoring; trolley availability w/ alerts; facility status (lifts/escalators/washrooms) | shall | Yes | Register FR-DTW Curbside | |
| G-124 | Substantive | Ops DT — Security: intrusion & reverse-entry detection; unattended baggage alert; suspicious behaviour detection; camera access; SAC smart washroom (IoT BLE); smart buggy; smart trolley (CV); smart traffic (video analytics); restroom management alerts; UI-based asset registry | shall | Yes | Register FR-DTW-SEC-* / SAC | |
| G-125 | Substantive | Ops DT — Airport/Terminal/Airside summary KPIs + facility-status roll-up (RBAC-persona-curated) | shall | Yes | Register FR-DTW-01..04 | |
| G-126 | Substantive | OT/IT asset widgets: on click of any asset display widget w/ critical values/KPIs per equipment type (HVAC chiller/pump/AHU/FCU/etc., FDAS, VHT, PBB, VDGS, GPU, PCA, ATRS, BHS, WTP, STP, MRSS, Solar, AGL, ECMS, LCMS, CUSS, CUPPS, E-Gates) — one widget per equipment | shall | Yes | Register FR-DTW-15 + OT widgets | Equipment-level KPIs enumerated in register. |
| G-127 | Substantive | DT visualization — Desktop GPU thick-client application + Web-GL browser DT (Chrome & Safari); zoom/tilt/turnaround; follow-the-sun; layer show/hide; selectable areas/zones; ITBMS equipment/sensor details via web page launched from DT | shall | Yes | Register Ops DT capabilities | |
| G-128 | Numeric | IT asset visualization cap | =3000 units | Yes | Register IT Assets / OUT OF SCOPE | Assets above 3000 explicitly out of scope. |
| G-129 | Substantive | Multi-level navigation airport→terminal→zone→floor→system→asset for T1, T2, T3 w/ zoom & shortcuts | shall | Yes | Register Ops DT Visualization | |
| G-130 | Substantive | OT asset visualization at LOD 350 (no schematics) for HVAC, FDAS, VHT, ECMS, LCMS, PBB, GPU, PCA, VDGS, WTP, STP, MRSS, BHS, ATRS, Solar-Panels, AGL; LOD 200 interiors using structural BIM for all floors; terminal-zone asset display (check-in/security/immigration/boarding/retail at asset level only) | shall | Yes | Register Ops DT Equipment | |
| G-131 | Substantive | Asset registry & modeling: Common Location Grid (CLG); Common Asset Id (CAI) framework; metadata store; query by location/type/id/state; sync framework; asset onboarding workflow; taxonomy; hierarchy; ontology/relationships; UI-based asset registry w/ asset name/serial/type/subgroup/location | shall | Yes | Register Asset Registry & Modeling | |
| G-132 | Substantive | Asset federation: IT assets, SAP, ArcGIS, RMS, VMS (live video) federation | shall | Yes | Register Asset Federation | |
| G-133 | Substantive | Simulation: IROGS/disruption simulation; evacuation & fire scenarios; breach detection; retail optimization; what-if scenario analytics; decision engine + UI for scenario management + visualization; EWS (early warning signals for wait-time breach & flight-delay-at-origin); disruption management w/ cascading impact; NOTAM display on DT banner | shall | Yes | ABR §4.1 / Register Functional-Simulation | ABR mandates 4-component simulation architecture (digital twin + scenario UI + decision engine + viz UI). |
| G-134 | Substantive | ABR SPG simulation use cases — Commercial (10: store mix, shelf merchandising, store location, dwell monetization, campaign, queue-vs-revenue, gate allocation, lounge-vs-retail, staffing-vs-sales, disruption monetization); Operational (8: passenger flow, queue mgmt, check-in capacity, gate allocation, disruption mgmt, workforce, baggage flow, landside traffic); Engineering (5: thermal load, passenger load vs HVAC, retail expansion energy, zone cooling, power stress testing) | shall (address use-case set) | No | ABR §4.2 | Points deducted if use-case coverage incomplete; not every use case is individually disqualifying. |
| G-135 | Substantive | ABR departmental requirements: P&E (borewell recharge IoT, storm water analysis Walter P Moore); S&V (reverse-entry, unattended baggage, behavior analytics, predictive security, security asset mapping); Commercial Aero (Google Maps/satellite, space-allocation change ID, GIS analytics); Operations (fog low-vis surface navigation, what-if, IT-system monitoring/alerting for DigiYatra/E-Gates/CUSS/CUPPS, live ops dashboard, overstaying/unidentified passengers) | shall | Yes | ABR §3.1–§3.4 | |
| G-136 | Procedural | Five-phase implementation programme: P1 Mobilisation & Data Acquisition → P2 Spatial Data Processing & BIM → P3 Platform Dev & BMS Integration → P4 AI Agent Deployment & UAT → P5 Commissioning, Training & Handover | shall | Yes | BRD §4.1 / RFP §5.1 | |
| G-137 | Numeric | Phase duration (each of 5 phases) | ~3 months each (~15 mo total) | Yes | BRD §4.1 | RFP leaves duration blank; BRD binds ~3mo/phase. |
| G-138 | Numeric | Payment milestones M1–M6 percentages of contract value | =15/10/20/25/20/10 % | Yes | BRD §7 / RFP §9.4 | M1 Mobilisation, M2 LiDAR, M3 BIM/Spatial, M4 DT UAT, M5 AI Agents, M6 Final Handover/PIR. |
| G-139 | Numeric | Deliverable review/sign-off period | =14 calendar days | Yes | BRD §4.2 / RFP §5.2 | |
| G-140 | Procedural | End-to-end delivery responsibility: vendor fully responsible for delivery, integration, performance, operationalisation incl. all 3rd-party/legacy/data-quality dependencies; ambiguity interpreted to include all activities to meet objectives | shall | Yes | BRD §9.7 | |
| G-141 | Procedural | Integration & interoperability responsibility: API readiness/testing, data mapping/transformation/validation, semantic model alignment, real-time exchange & sync; any integration failure is vendor responsibility unless excluded in writing | shall | Yes | BRD §9.8 | |
| G-142 | Procedural | Service levels & penalty framework: all KPIs contractually binding; financial penalties per SLA breach; repeated breaches (≥3/quarter) = material default; persistent non-performance may = termination | shall | Yes | BRD §9.9 / App. C | |
| G-143 | Procedural | Data ownership, usage & AI restrictions: all data DIAL exclusive; no use outside contract; no training external AI models w/ DIAL data; no data transfer/storage/processing outside India without prior written approval; breach = material breach | shall | Yes | BRD §9.10 / RFP §9.6 | |
| G-144 | Procedural | Cybersecurity & data-breach liability: vendor responsible for platform security; on incident — notify DIAL ≤12h, immediate containment/remediation, bear all costs (recovery/legal/reputational); vendor negligence may = penalties/termination | shall | Yes | BRD §9.11 | |
| G-145 | Procedural | Exit management & transition: complete handover of deliverables, source code, configs, docs; knowledge transfer to DIAL/nominated agency; transition support ≥6 months at no additional cost unless explicitly agreed | shall | Yes | BRD §9.12 | |
| G-146 | Procedural | Applicable laws & approvals: vendor obtains/maintains all regulatory approvals (BCAS, AAI, etc.) at own cost; continuous compliance; indemnify DIAL against non-compliance | shall | Yes | BRD (Applicable Laws) | |
| G-147 | Procedural | RACI matrix adherence across planning/surveys, platform dev, AI/analytics, operations/support (vendor R for delivery; DIAL A for approvals) | shall | Yes | BRD §5 | |
| G-148 | Procedural | DIAL reserved rights: accept/reject any/all proposals; negotiate w/ any/multiple; cancel/modify RFP; award to one/multiple or split scope | acknowledged | No | RFP §9.2 | Procedural; not scored for substantive compliance. |
| G-149 | Procedural | Intellectual property: all deliverables become DIAL exclusive IP upon milestone payment; vendor retains no ownership; 3rd-party components identified in SBOM & properly licensed | shall | Yes | RFP §9.3 | |
| G-150 | Numeric | Warranty period from formal platform handover | ≥12 months | Yes | RFP §9.5 | Followed by structured AMC. |
| G-151 | Procedural | Five-year O&M plan covering platform, infrastructure, AI models, integrations, data lifecycle; SLAs, support structure, upgrades, reporting, exit/transition strategy | shall | Yes | RFP §8 / BRD Table 8 | |
| G-152 | Procedural | Modular, cloud-native (or cloud-ready hybrid) architecture; scalable to add buildings/systems/data sources without re-architecture; high availability; disaster recovery; long-term DIAL usage rights independent of vendor continuity | shall | Yes | BRD Obj. 6 / RFP §2.2 Obj. 6 / §7 | |
| G-153 | Numeric | Platform operational lifecycle (design life) | ≥15 years | Yes | BRD Obj. 6 / RFP §2.2 Obj. 6 | |
| G-154 | Procedural | Comprehensive training, knowledge transfer & documentation to enable DIAL self-management | shall | Yes | BRD Obj. 6 / RFP §2.2 Obj. 6 | |
| G-155 | Numeric | Historical BMS data archiving retention | ≥5 years | Yes | BRD §3.4.2 / RFP §3.4.2 | |
| G-156 | Numeric | AI audit log retention | ≥5 years | Yes | BRD §3.5.5 / RFP §6.4 | |
| G-157 | Numeric | AI model rollback time | ≤4 hours | Yes | BRD §3.5.5 / RFP §6.4 | |
| G-158 | Numeric | Platform uptime (KPI 1, excl. planned maintenance) | ≥99.5% | Yes | BRD §2.3 / RFP §2.3 / App. C | |
| G-159 | Numeric | Real-time data latency (KPI 2, sensor → dashboard) | ≤5 seconds | Yes | BRD §2.3 / RFP §2.3 / App. C | |
| G-160 | Numeric | BIM Model LOD compliance (KPI 3) | =100% of specified assets at agreed LOD | Yes | BRD §2.3 / RFP §2.3 / App. C | |
| G-161 | Numeric | System integration coverage (KPI 7) | =100% of agreed BMS/IoT data points within 3 months of go-live | Yes | BRD §2.3 / RFP §2.3 / App. C | |
| G-162 | Numeric | Incident response time — critical (KPI 6) | ≤10 minutes from notification | Yes | BRD §2.3 / App. C | CONFLICT: RFP §2.3 says ≤1 hour; BRD §2.3 + App. C bind ≤10 mins. Binding = ≤10 min. |
| G-163 | Numeric | Cybersecurity incident/breach notification to DIAL | ≤12 hours of detection | Yes | BRD §9.11 | |
| G-164 | Numeric | SLA material-default threshold (repeated breaches per quarter) | ≥3 breaches/quarter | Yes | BRD §9.9 | |
| G-165 | Numeric | Transition support period at contract expiry/termination | ≥6 months | Yes | BRD §9.12 | No additional cost unless explicitly agreed. |
| G-166 | Numeric | IoT machine-room pumps sensors (T1/T2/T3) | =40 units | Yes | BRD §3.3.4 / App. E / Register | |
| G-167 | Numeric | T1 roof water-level sensors | =12 units | Yes | BRD §3.3.4 / App. E / Register | |
| G-168 | Numeric | Recovery Time Objective (RTO) | ≤4 hours | Yes | Register NFR | Register-only; not in BRD/RFP KPIs. Binding via register tier 5. |
| G-169 | Numeric | Recovery Point Objective (RPO) | ≤24 hours | Yes | Register NFR | Register-only; binding via register tier 5. |
| G-170 | Numeric | Service & support coverage | =24x7 | Yes | Register NFR | Register-only. |
| G-171 | Numeric | Minimum case studies in Volume 6 | ≥3 | Yes | RFP §9.3 | |
| G-172 | Numeric | Geospatial data accuracy — horizontal RMSE (KPI 5 restated for parity) | ≤5 cm | Yes | BRD §2.3 KPI 5 | Same binding value as G-043; listed in KPI form for parity. |
| G-173 | Numeric | Geospatial data accuracy — vertical RMSE (KPI 5 restated for parity) | ≤3 cm | Yes | BRD §2.3 KPI 5 | Same binding value as G-044; listed in KPI form for parity. |
| G-174 | Numeric | Airborne LiDAR survey total area | ~200 sq km | Yes | BRD §3.1.1 / RFP §3.1.1 | |
| G-175 | Numeric | Underground utility scanning area (landside) | =225 acres | Yes | BRD §3.1.2 / Register | |
| G-176 | Numeric | Airport campus survey area | ~5000 acres | Yes | Register Geokno LiDAR | |
| G-177 | Numeric | T1 BIM modelling total area | ~213,396 sq m | Yes | Register Ops DT T1 | Sum of T1 floor areas. |
| G-178 | Numeric | T2 BIM modelling total area | ~62,519 sq m | Yes | Register Ops DT T2 | Sum of T2 floor areas. |
| G-179 | Numeric | T3 BIM modelling total area | ~588,158 sq m | Yes | Register Ops DT T3 | Sum of T3 floor areas. |
| G-180 | Numeric | T3 HVAC integration points (Honeywell) | =54,000 pts | Yes | Register INTF-T3-HVAC | First 4,000 within 3 months. |
| G-181 | Numeric | T3 FDAS integration points (Notifire) | =65,000 pts | Yes | Register INTF-T3-FDAS | |
| G-182 | Numeric | T1 HVAC integration points (JCI) | =20,000 pts | Yes | Register INTF-T1-HVAC | |
| G-183 | Numeric | T1 FDAS integration points (Edwards) | =17,400 pts | Yes | Register INTF-T1-FDAS | |
| G-184 | Numeric | MRSS integration points (GE) | =60,000 pts | Yes | Register INTF-CM-MRSS | |
| G-185 | Numeric | T3 ECMS tags (ABB) | =66,000 tags | Yes | Register INTF-T3-ECMS | Needs upgrade; Phase 2. |
| G-186 | Numeric | T1 ECMS tags (Schneider) | =20,000 tags | Yes | Register INTF-T1-ECMS | |
| G-187 | Numeric | T2 FDAS integration points (Edwards) | =5,000 pts | Yes | Register INTF-T2-FDAS | |
| G-188 | Numeric | T3 BHS integration points (Vanderlande) | =1,300 pts | Yes | Register INTF-T3-BHS | |
| G-189 | Numeric | OT-system count in PE_OT final list | =19 OT systems | Yes | PE_OT §2 | 19 systems across ASB/T1/T2/T3/WTP/STP/MRSS/airside. |

---

## 2. Numeric-Parity Sub-Table

Rows marked Category=Numeric in the master table, restated for direct parity checking. `applies_to` indicates the deliverable/component the scorer checks against the draft.

| G-ID | Parameter | Binding value | Operator | Unit | Applies to | Source |
|---|---|---|---|---|---|---|
| G-009 | Proposal validity | 180 | ≥ | days | Proposal submission | RFP §9.1 |
| G-018 | Eval weight: Technical | 30 | = | % | Evaluation | RFP §9.2 |
| G-018 | Eval weight: Experience | 25 | = | % | Evaluation | RFP §9.2 |
| G-018 | Eval weight: AI | 20 | = | % | Evaluation | RFP §9.2 |
| G-018 | Eval weight: Commercial | 15 | = | % | Evaluation | RFP §9.2 |
| G-018 | Eval weight: Implementation | 10 | = | % | Evaluation | RFP §9.2 |
| G-041 | Airborne LiDAR point density (boundary) | 20 | ≥ | pts/m² | Airborne LiDAR | BRD §3.1.1 |
| G-042 | Airborne LiDAR point density (buffer) | 8 | ≥ | pts/m² | Airborne LiDAR buffer | BRD §3.1.1 |
| G-043 | Horizontal RMSE | 5 | ≤ | cm | Geospatial accuracy | BRD §3.1.1 / KPI 5 |
| G-044 | Vertical RMSE | 3 | ≤ | cm | Geospatial accuracy | BRD §3.1.1 / KPI 5 |
| G-045 | Orthophoto GSD | 5 | ≤ | cm | Orthophoto | BRD §3.1.1 |
| G-047 | DTM/DSM grid resolution | 10 | = | cm | DTM/DSM | BRD §3.1.1 |
| G-048 | Contour interval | 10 | = | cm | Contour dataset | BRD §3.1.1 |
| G-059 | Indoor positional RMSE | 5 | ≤ | cm | Indoor LiDAR | BRD §3.1.5 |
| G-079 | API backwards compatibility | 2 | ≥ | major versions | API layer | BRD §3.4.3 / RFP §4.1 |
| G-083 | TLS version (in transit) | 1.3 | = | TLS ver | Data in transit | BRD §3.4.4 (register "1.2+" overridden) |
| G-084 | Encryption at rest | AES-256 | = | cipher | Data at rest | BRD §3.4.4 |
| G-085 | Activity audit log retention | 2 | ≥ | years | Audit logs | BRD §3.4.4 |
| G-088 | Mandatory domain AI agents | 8 | = | count | AI agent estate | BRD §3.5.3 (RFP 6 overridden) |
| G-107 | Mech & HVAC — precision / recall / horizon / latency | 82 / 78 / 72 / 30 | ≥ / ≥ / ≤ / ≤ | % / % / h / s | Mechanical & HVAC agent | BRD §3.5.4 |
| G-108 | Electrical — precision / recall / horizon / latency | 80 / 75 / 48 / 30 | ≥ / ≥ / ≤ / ≤ | % / % / h / s | Electrical agent | BRD §3.5.4 |
| G-109 | Passenger Flow — precision / recall / horizon / latency | 85 / 80 / 45 / 15 | ≥ / ≥ / ≤ / ≤ | % / % / min / s | Passenger Flow agent | BRD §3.5.4 |
| G-110 | Structural — precision / recall / horizon / latency | 90 / 85 / 7 / 60 | ≥ / ≥ / ≤ / ≤ | % / % / d / s | Structural agent | BRD §3.5.4 |
| G-111 | Fire Safety — precision / recall / horizon / latency | 95 / 95 / real-time / 5 | ≥ / ≥ / = / ≤ | % / % / status / s | Fire Safety agent | BRD §3.5.4 |
| G-112 | Energy Mgmt — precision / recall / horizon / latency | 80 / 75 / 24 / 60 | ≥ / ≥ / ≤ / ≤ | % / % / h / s | Energy agent | BRD §3.5.4 |
| G-113 | Security — precision / recall / horizon / latency | 88 / 82 / 15 / 10 | ≥ / ≥ / ≤ / ≤ | % / % / min / s | Security agent | BRD §3.5.4 |
| G-114 | Aggregate predictive alert accuracy (precision / recall) | 80 / 75 | ≥ / ≥ | % / % | All predictive agents | BRD KPI 4 |
| G-128 | IT asset visualization cap | 3000 | = | units | IT assets in DT | Register |
| G-137 | Phase duration | 3 | ~ | months/phase | Implementation programme | BRD §4.1 |
| G-138 | Payment milestones M1–M6 | 15/10/20/25/20/10 | = | % each | Payment schedule | BRD §7 / RFP §9.4 |
| G-139 | Deliverable review period | 14 | = | calendar days | Deliverable sign-off | BRD §4.2 |
| G-150 | Warranty period | 12 | ≥ | months | Post-handover support | RFP §9.5 |
| G-153 | Platform design life | 15 | ≥ | years | Platform architecture | BRD Obj. 6 |
| G-155 | Historical BMS data retention | 5 | ≥ | years | BMS/IoT archive | BRD §3.4.2 |
| G-156 | AI audit log retention | 5 | ≥ | years | AI alert logs | BRD §3.5.5 |
| G-157 | AI model rollback time | 4 | ≤ | hours | Model governance | BRD §3.5.5 |
| G-158 | Platform uptime | 99.5 | ≥ | % (excl. planned maint.) | Platform availability | BRD KPI 1 |
| G-159 | Real-time data latency | 5 | ≤ | s (sensor→dashboard) | Data pipeline | BRD KPI 2 |
| G-160 | BIM LOD compliance | 100 | = | % of specified assets | BIM models | BRD KPI 3 |
| G-161 | Integration coverage | 100 | = | % within 3 months of go-live | BMS/IoT integration | BRD KPI 7 |
| G-162 | Incident response (critical) | 10 | ≤ | min from notification | Incident response | BRD KPI 6 (RFP ≤1hr overridden) |
| G-163 | Breach notification | 12 | ≤ | hours | Cybersecurity incident | BRD §9.11 |
| G-164 | Material-default threshold | 3 | ≥ | breaches/quarter | SLA enforcement | BRD §9.9 |
| G-165 | Transition support | 6 | ≥ | months | Exit management | BRD §9.12 |
| G-166 | IoT machine-room pumps | 40 | = | units | HVAC sensor base | BRD §3.3.4 |
| G-167 | T1 roof sensors | 12 | = | units | Water & Drainage sensor base | BRD §3.3.4 |
| G-168 | RTO | 4 | ≤ | hours | Disaster recovery | Register NFR |
| G-169 | RPO | 24 | ≤ | hours | Disaster recovery | Register NFR |
| G-170 | Service & support | 24x7 | = | coverage | Operations support | Register NFR |
| G-171 | Min case studies | 3 | ≥ | count | Volume 6 | RFP §9.3 |
| G-172 | Geospatial horizontal RMSE (KPI 5) | 5 | ≤ | cm | Geospatial accuracy | BRD KPI 5 |
| G-173 | Geospatial vertical RMSE (KPI 5) | 3 | ≤ | cm | Geospatial accuracy | BRD KPI 5 |
| G-174 | Airborne LiDAR total survey area | 200 | ~ | sq km | Survey scope | BRD §3.1.1 |
| G-175 | Underground utility scanning area | 225 | = | acres | Landside utilities | BRD §3.1.2 |
| G-176 | Airport campus survey area | 5000 | ~ | acres | Survey scope | Register |
| G-177 | T1 BIM total area | 213396 | ~ | sq m | T1 BIM | Register |
| G-178 | T2 BIM total area | 62519 | ~ | sq m | T2 BIM | Register |
| G-179 | T3 BIM total area | 588158 | ~ | sq m | T3 BIM | Register |
| G-180 | T3 HVAC points | 54000 | = | pts | T3 HVAC integration | Register |
| G-181 | T3 FDAS points | 65000 | = | pts | T3 FDAS integration | Register |
| G-182 | T1 HVAC points | 20000 | = | pts | T1 HVAC integration | Register |
| G-183 | T1 FDAS points | 17400 | = | pts | T1 FDAS integration | Register |
| G-184 | MRSS points | 60000 | = | pts | MRSS integration | Register |
| G-185 | T3 ECMS tags | 66000 | = | tags | T3 ECMS integration | Register |
| G-186 | T1 ECMS tags | 20000 | = | tags | T1 ECMS integration | Register |
| G-187 | T2 FDAS points | 5000 | = | pts | T2 FDAS integration | Register |
| G-188 | T3 BHS points | 1300 | = | pts | T3 BHS integration | Register |
| G-189 | OT systems in PE_OT final list | 19 | = | systems | OT integration scope | PE_OT §2 |

---

## 3. Source Conflicts Resolved

| # | Parameter | RFP / Register value | BRD/ABR value | Binding value | Rationale |
|---|---|---|---|---|---|
| C-1 | Incident response time (critical) | RFP ≤1 hour | BRD §2.3 + App. C ≤10 mins | **≤10 mins** | BRD (tier 1) overrides RFP (tier 4). KPI 6 in BRD and SLA Appendix C both state ≤10 minutes. |
| C-2 | TLS version (in transit) | Register "TLS 1.2+" | BRD §3.4.4 + RFP §3.5.2 "TLS 1.3" | **TLS 1.3** | BRD and RFP both specify TLS 1.3; register's looser "1.2+" is overridden by the higher-specificity BRD value. |
| C-3 | Mandatory AI agent count | RFP §6.3 lists 6 agents | BRD §3.5.3 lists 8 (adds Passenger Flow + Structural Integrity) | **8 agents** | BRD §3.5.3 is binding. RFP §6.5 performance table itself lists 7 agents incl. Passenger Flow & Structural, confirming they are in scope; register AI-13/AI-16 confirms. |
| C-4 | Phase duration | RFP §5.1 leaves Duration blank | BRD §4.1 binds ~3 months/phase | **~3 months/phase (~15 mo total)** | BRD binds what RFP leaves open. |
| C-5 | Activity audit log retention | (no conflict; register = 2 yr) | BRD §3.4.4 ≥2 years | **≥2 years** | Consistent. Note: AI audit logs are separately ≥5 years (BRD §3.5.5). |
| C-6 | RTO / RPO | Register NFR: RTO 4h, RPO 24h | Not in BRD/RFP KPIs | **RTO ≤4h, RPO ≤24h** | Register-only (tier 5); treated as binding content requirement where not contradicted by a higher tier. |
| C-7 | Pre-qualification turnover threshold | RFP App. E "INR [X] crore" (blank) | Not specified elsewhere | **INR [X] crore (value TBD by DIAL)** | RFP leaves blank; scorer should flag any draft that omits the criterion vs. one that fills a placeholder. |
| C-8 | DTM/DSM/orthophoto/contour specs | (no conflict) | BRD §3.1.1 binds 10 cm grid, 10 cm contours, ≤5 cm GSD | **per BRD** | Numeric inventory confirmed drafts sometimes deviate to 50 cm; binding value is BRD's. |
| C-9 | Underground utility methods | (no conflict) | BRD §3.1.2 requires GPR + DGPS + GNSS + 12D | **all four methods** | Partial delivery (GPR only) is a shortfall against binding set. |
| C-10 | Additional RBAC roles | RFP/BRD: min 5 default | Register NFR adds 10 additional roles | **≥5 default + additional roles per register** | Register expands the set; treated as binding since it does not conflict (higher floor). |

---

**End of gold requirement inventory.**