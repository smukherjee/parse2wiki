# Skill-Derived Gap Inventory — Airport Eye (APOC Phase 2)

**Run:** Compliance-validator skill, 12-step process, run against:
- **Source requirements:** `Change Request Aiport Eye - APOC Phase 2.pdf.md` (BRD v1.5), `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` (ABR), `PE_OT System_09.06.pptx.md` (PE_OT list), `Airport_Eye_RFP_v5.docx.md` (base RFP), `AirportEye_Requirements_Register_v5.xlsx.md` + `Final requirements.xlsx.md`.
- **Target artefact:** `Airport_Eye_Consolidated_Proposal_FINAL.docx.md` (the WAISL+Geokno consolidated proposal, dated 14-July-2026).
- **Client gap document:** `client gaps.md` was **not** read during this run. (The skill is run independently of the client's gap list; the eval below compares the two outputs.)

**Extraction method:** Full 12-step process (Steps 1-12 of `SKILL.md`). Every gap below was surfaced by the skill from the source-vs-proposal delta using one of:
- Step 3 — categorical validation (Pass/Partial/Fail/Ambiguous).
- Step 4 — numeric parity (binding value vs proposal value).
- Step 5 — semantic carve-out / over-claim.
- Step 6 — scope-coverage completeness.
- Step 9 — deviation-register completeness audit.

**Total count:** 78 gap findings (`S-001`..`S-078`). These are the "skill's gap list" that the eval scores against the client-gap inventory (46 client gaps).

**Notation:** Each row records what the skill observed. The `evidence` field is the proposal section or table that fails the check, with the source clause the check is against. The `severity` follows the skill's modal-verb-driven verdict logic: `binding` for `shall`/`must`, `scored` for `should`, `optional` for `may`.

---

## 1. Master Skill-Gap Table

| id | category | applies_to | gap_text | evidence | severity | source |
|---|---|---|---|---|---|---|
| S-001 | survey | LiDAR horizontal accuracy | Proposal commits ≤5 cm RMSE horizontal, but Table 1 line 1.1 "Airborne LiDAR acquisition (≥ 20 pts/m² within boundary)" is unpriced and dependent on a "DGCA permit facilitation" lot; if the 20 pts/m² re-baseline is not achieved, accuracy envelope is at risk | Programme-at-a-glance table vs §2.2.2 | binding | BRD §3.1.1 |
| S-002 | survey | LiDAR vertical accuracy | ≤3 cm RMSE vertical stated; same re-baseline risk as S-001 | Programme-at-a-glance | binding | BRD §3.1.1 / KPI 5 |
| S-003 | survey | Orthophoto GSD | ≤5 cm GSD committed in §2.1.2; relies on Table 1 line 1.5 (unpriced) | §2.1.2 vs Table 1.5 | binding | BRD §3.1.1 |
| S-004 | survey | DTM/DSM grid | 10 cm grid committed in §2.1.2; relies on Table 1 line 1.6 (unpriced) | §2.1.2 vs Table 1.6 | binding | BRD §3.1.1 |
| S-005 | survey | Buffer-zone LiDAR density | "Bidder commitment, to be confirmed with DIAL in the Month-1 workshop (bidder proposes 8 pts/m²)" — carve-out weakening a binding BRD figure | §2.1.2 (programme-at-a-glance table) | binding | BRD §3.1.1 |
| S-006 | survey | 10 cm contours | Not addressed anywhere; §3.1.1 of Solution Proposal v9 references 50 cm contours; Consolidated Final has no contour-interval commitment | §2.2 / Table 1 | binding | BRD §3.1.1 |
| S-007 | survey | 3D mesh models (OBJ/FBX, georeferenced) | Not addressed; Table 1 line 1.7 ("3D mesh models") is unpriced and unstipulated | Table 1.7 | binding | BRD §3.1.1 |
| S-008 | survey | Independent accuracy assessment + survey metadata (D-03) | Table 1 line 1.9 unpriced; deliverable not described | Table 1.9 | binding | BRD §3.1.9 D-03 |
| S-009 | survey | Flight report, sensor calibration, GCP report (D-06 equivalent) | Not addressed anywhere | n/a | binding | BRD §3.1.9 D-06 |
| S-010 | survey | Data compatibility (ESRI ArcGIS, Autodesk) | Not explicitly committed | n/a | binding | BRD §3.1.1 |
| S-011 | survey | Landside 225 acres LiDAR coverage | 225 acres committed but the 4-method underground utility set (GPR + DGPS + GNSS + 12D) is reduced to GPR only | §2.1.2 | binding | BRD §3.1.2 |
| S-012 | survey | 10-layer landside GIS catalogue | Not addressed (no layer catalogue enumerated) | n/a | binding | BRD §3.1.2 |
| S-013 | survey | Airside layer-wise scanning | Mentioned generically; not layer-enumerated per BRD §3.1.3 | n/a | binding | BRD §3.1.3 |
| S-014 | survey | Airside GIS layers (AGL, PAPI, DVOR, NAVAIDs) | Not addressed | n/a | binding | BRD §3.1.3 |
| S-015 | bim | IFC standard (4.0 vs 4.3) | Proposal commits IFC 4.0 (line 486, Table 2.2) but BRD §3.2.2 / RFP §3.2.2 + ISO 19650 lifecycle governance implies IFC 4.3 for new delivery; IFC 4.0 is below the current openBIM standard | §2.3.2 / Table 2.2 | scored | RFP §3.2.2 / OpenBIM 4.3 |
| S-016 | bim | BIM-IFC Data Architecture section | No RTM section titled "BIM IFC Data Architecture" — the architecture, governance, ownership, IFC GUID↔CAI↔CLG↔SAP mapping, and long-term stewardship of IFC data are not defined | n/a | binding | BRD §3.2.2 (implied) |
| S-017 | bim | Airport Asset Information Model (AIM) | Not defined as a static asset model | n/a | binding | BRD §3.2.2 (implied) |
| S-018 | bim | Ontology / relationship model | Not articulated across terminal/floor/space/system/equipment/sensor | n/a | binding | BRD §3.2.2 |
| S-019 | bim | BIM lifecycle management (version control, as-built, change mgmt, DT sync) | Not specified | n/a | binding | BRD §3.2.2 / §3.2.3 |
| S-020 | bim | BIM-GIS federation rules / georeferencing standards | Not specified; only "integrated into ESRI" stated | §2.3.2 / §2.7 | binding | BRD §3.2.2 |
| S-021 | bim | Open BIM standards mandate (IFC 4.3, bSDD) | IFC 4.0 cited; IFC 4.3 + bSDD not mandated | §2.3.2 | binding | OpenBIM 4.3 (industry norm) |
| S-022 | bim | Digital thread (BIM↔GIS↔SAP↔BMS↔IoT↔APOC↔AI agents) | Not defined as an end-to-end thread | n/a | binding | BRD §3.2.3 / §3.4.3 |
| S-023 | bim | Long-term BIM governance / ownership | DIAL ownership of BIM models not explicitly stated; "DIAL ownership of all model weights and training data" is about AI, not BIM | §3.4 | binding | BRD §3.2.2 / §9.10 |
| S-024 | asset_registry | Complete asset registry (hierarchy, parent-child, traceability) | No registry with hierarchy, relationship, type, parent-child, location, traceability; only §2.3.2 "asset attribution" and §2.7 "asset register" mention | §2.3.2 / §2.7 | binding | BRD §3.2.3 |
| S-025 | asset_registry | IFC↔CAI↔CLG↔SAP↔OT/BMS mapping | Not addressed | n/a | binding | BRD §3.2.3 (implied) |
| S-026 | asset_registry | IT/OT hardware for full Pax journey (Departure + Arrival) | §2.5.8 + Table 4 line 4.5 list 13 systems; "2D Barcode Scanners, SBD, Check-in Counters, Boarding Gate Scanners, Baggage Scanners" added under 4.16 — but pax-journey hardware is not explicitly mapped Departure AND Arrival | §2.5.8 / Table 4.13 | binding | ABR §3.4 (Operations) |
| S-027 | asset_registry | CCTV + video analytics + all pax-journey IT in scope | §2.5.6 covers PSIM/VMS/CCTV/ACS; video analytics is not explicitly itemised as a passenger-journey item beyond security | §2.5.6 | binding | ABR §3.4 |
| S-028 | integration | 2D Barcode / DigiYatra / E-gate / CUSS / CUPPS / DFMD / ATRS / Baggage scanner / Boarding gate | DigiYatra and CUSS/CUPPS/DFMD/ATRS covered in 4.5; 2D Barcode, SBD, Boarding Gate, Baggage Scanner added in 4.16; but "E-gate" appears only in §3.2.1 as part of passenger flow — not in the costed integration estate as a named line | Table 4.5/4.13/4.16 | binding | ABR §3.4 |
| S-029 | integration | T2 OT integration exclusion | §4.1.2 records "T2 OT estate status and OEM-planned controller upgrade exclusions" and §4.3.4 lists T2 OT estate as excluded pending DIAL confirmation (C-16); the client gap C-006 says T2 OT cannot be excluded (FAS is operational) | §4.1.2 / §4.3.4 | binding | Client gap C-006 / PE_OT slide 2 row 10 |
| S-030 | integration | OT data point count | §2.5.3 states "~196,000+ OT data points"; client expects 5,00,000+; mismatch of ~3,00,000 data points | §2.5.3 | binding | Client gap C-013 / PE_OT |
| S-031 | integration | ITBMS / JCI / Honeywell integration approach | T3 ITBMS aggregator stated as "integrated first"; but no per-OEM, per-site integration approach (T1 JCI, T3 Honeywell, ITBMS aggregator) is laid out; T2 ITBMS not present | §2.5.7 | binding | PE_OT slide 2 / BRD §3.3.2 |
| S-032 | integration | APOC integration control rights | §3.6.1 covers KPI/feed consumption; control rights for specific functions (e.g., AGL ON/OFF) are not stated; client gap C-028 explicitly requires "Control of Lights ON/OFF from APOC" | §3.6.1 | binding | BRD §3.4.3 / Client gap C-027 / C-028 |
| S-033 | integration | Medallion Lakehouse architecture | "Unified Geospatial Data Lake" and "Bronze/Silver/Gold" medallion terms appear (§4.5.6) but the architecture (Bronze/Silver/Gold/Platinum layers, Delta/Parquet, Unity Catalog, lineage, access control) is not described | §4.5.6 | binding | Client gap C-020 |
| S-034 | integration | Change detection (Google Maps / satellite, D+1) | "External basemap integration | Google Maps / satellite landside integration (ABR Section 3.3) - candidate; DIAL confirmation" — deferred to confirmation; client gap C-014 says "do not mark as gap / future" | §2.7 | binding | Client gap C-014 / ABR §3.3 |
| S-035 | security | DIAL IT Security Policy | Not explicitly cited; only generic IEC 62443 / SOC / SIEM / ISO 27001 mentioned | §2.5.10 / §4.4.5 | binding | Client gap C-015 |
| S-036 | sla | Platform availability | §1.4.10 says "≥99.5% (platform); ≥99.9% target (infrastructure)" — 99.5% for platform ≠ 99.9% as the client requests (C-016: "SLA availability should be 99.9%") | §1.4.10 / §4.5.2 | binding | Client gap C-016 / BRD §2.3 KPI 1 |
| S-037 | sim | Simulation engine architecture | §3.5.2 four-component architecture (DT + scenario UI + decision engine + results UI) is referenced but architecture details (data flow, model registry, scenario library, versioning, what-if validation) are not detailed | §3.5.2 | binding | ABR §4.1 |
| S-038 | sim | Commercial SPG what-if use cases | §3.5.3 lists "Scenario families" generically (IROPS, evacuation, retail); the 10 ABR §4.2 Commercial use cases (Store Mix, Shelf Merchandising, Store Location, Dwell Monetization, Campaign, Queue vs Revenue, Gate Allocation, Lounge vs Retail, Staffing vs Sales, Disruption Monetization) are not enumerated | §3.5.3 | binding | ABR §4.2 |
| S-039 | sim | Operational SPG what-if use cases (workforce, capacity, curbside) | Same gap; the 8 ABR §4.2 Operational use cases are not enumerated, and curbside / workforce / capacity explicitly absent | §3.5.3 | binding | ABR §4.2 |
| S-040 | sim | Engineering SPG what-if use cases (thermal load, HVAC, energy) | Same gap; the 5 ABR §4.2 Engineering use cases not enumerated | §3.5.3 | binding | ABR §4.2 |
| S-041 | ai | All 8 AI Agents explicitly detailed | §3.2 lists 8 agents; but the client expects "explicitly detailed" with data sources, model approach, performance targets, explainability, governance; consolidated proposal has the agent list at table 3.2 only | §3.2 | binding | BRD §3.5.3 / Client gap C-011 |
| S-042 | ai | AI modelling for system stress, partial failure, service degradation | The 8 agents cover domain-specific monitoring but a horizontal "system stress, partial failure, service degradation" modelling layer (cross-domain correlation) is not described | §3.1.4 / §3.2 | scored | Client gap C-012 |
| S-043 | ai | AI↔BIM/IFC access pattern | No description of how AI agents will access/query BIM/IFC data + relationships for granular analytics | §3.2 / §2.3 | scored | Client gap C-042 |
| S-044 | racing | OneAPOC / APOC Phase-2 complete accountability to WAISL | RACI summary in §4.4.2 records "APOC integration (monitoring): Vendor R, DIAL A, Smart City A, DEC I" — Vendor is R, not A; client gap C-007 says accountability must be with WAISL | §4.4.2 | binding | Client gap C-007 / BRD §1.3 |
| S-045 | racing | Complete IT Infrastructure (on-prem / cloud) provisioning owned by WAISL | §1.4.10 records "DIAL-provided infrastructure (GPU on-prem server, GPU laptops, networking, security, IT support, IoT/OT field and infra support)"; RACI for IT infrastructure not assigned to WAISL; client gap C-010 requires WAISL R+A | §1.4.10 / Table 5 / §4.3.2 | binding | Client gap C-010 |
| S-046 | racing | RACI — WAISL Accountable + Responsible | §4.4.2 RACI summary has "Vendor R, DIAL A" for most activities (including mobilisation, regulatory approvals, surveys, BIM modelling, integration); client gap C-023 requires RACI revision with WAISL as R+A | §4.4.2 | binding | Client gap C-023 |
| S-047 | racing | DIAL Vendors / OEM coordination owned by WAISL | RACI does not list OEM coordination as a WAISL activity; the dependency is implicit through DIAL; client gap C-033 requires explicit ownership | §4.4.2 / §4.3.3 | binding | Client gap C-033 |
| S-048 | racing | AEP/access coordination owned by WAISL | §4.4.2 RACI has AEP permits under customer dependencies (DIAL); no WAISL AEP/access coordination role; client gap C-034 requires WAISL ownership | §4.3.2 / §4.4.2 | binding | Client gap C-034 |
| S-049 | racing | Risk register elaboration | §4.3.5 lists 8 risks at top level; client gap C-022 requires "elaboration for some points as highlighted in attached doc" | §4.3.5 | scored | Client gap C-022 |
| S-050 | platform | Mobile + offline for all capabilities | §2.6.3 AR/VR device list; §1.3.2 mentions "iOS/Android mobile applications" but mobile + offline is not stated as a blanket capability for all roles | §1.3.2 / §2.6.3 | binding | Client gap C-003 / BRD §3.4.6 |
| S-051 | platform | DT visibility on end-user machines (democratise) | §2.6 lists Unity/Unreal desktop thick-client + WebGL + mobile; "end-user machines" democratisation (browser access by leadership / end users) is not explicit | §2.6.1-§2.6.5 | scored | Client gap C-008 |
| S-052 | commercial_aero | DIAL department-wise use-case mapping / KPIs / dashboard | §2.5.8 + Addendum A map IT asset to pax journey; department-wise (P&E / S&V / Commercial Aero / Operations) use-case → KPI → dashboard mapping is not provided | §2.5.8 / Addendum A | scored | Client gap C-004 |
| S-053 | dashboard | Leadership reporting dashboards | No leadership-specific dashboard spec; role-based access lists Executive role but no leadership dashboard definition | §3.4.4 / §4.4.1 | scored | Client gap C-005 |
| S-054 | environmental | Borewell recharge monitoring in base scope | §2.5.11 says "Smart City IoT systems onboarding (borewell, environmental)" — listed under Smart City integration Table 4.14 (CIO Review C-27); not in base scope as client requires | §2.5.11 / Table 4.14 | binding | Client gap C-031 / ABR §3.1 |
| S-055 | environmental | Stormwater analysis data feed and implementation in base scope | §2.7 reference list includes "Walter P Moore stormwater report (Annexure K.5 (14))" — listed as a dependency / source confirmation; implementation not in base scope | §2.7 | binding | Client gap C-032 / ABR §3.1 |
| S-056 | training | Training & adoption democratised across departments | §4.6.4 lists "Role-based end-user training for Executive, Operations, Maintenance, Security, Guest/Visitor roles" + admin + AI/ML + train-the-trainer; no department-specific training plan | §4.6.4 | scored | Client gap C-029 |
| S-057 | exclusion | Exclusions explicitly accepted by business owners | §4.3.4 lists 8 exclusions (T2 OT, OEM upgrades, GPU on-prem, DIAL-provided infra, OneAPOC platform, etc.); no record of business-owner acceptance | §4.3.4 | scored | Client gap C-030 |
| S-058 | platform | Generic Digital framework aspiration documented | Proposal is technical / commercial; the strategic "Generic Digital framework" / platform-aspiration narrative is not documented as a top-level section | n/a (whole proposal) | scored | Client gap C-035 |
| S-059 | survey | Indoor scans registered to airborne coordinate system | §2.3.1 "registered to the airborne coordinate system" — committed; but the deliverable is not enumerated (no D-04 cross-reference) | §2.3.1 | binding | BRD §3.1.5 |
| S-060 | platform | Phase 1 environmental monitoring (Shahabad MdPur, NMT, CAQM) | §3.3.5 "Environmental monitoring" referenced; specific sites (Shahabad MdPur STP/ISWMC/IMD, Noise Monitoring Terminals, Nursery CAQM) not itemised | n/a | binding | BRD §3.3.5 |
| S-061 | platform | Pre-maintenance & planning (terrain, soil, noise contours, flood, evacuation) | §2.7 mentions land utilisation, flood simulation, emergency response planning generically; the BRD §3.3.3 detailed list (soil/hydrological, urban heat island, noise contour maps, disaster-prone mapping) not itemised | §2.7 | binding | BRD §3.3.3 |
| S-062 | asset_registry | Land & Space Management digital footprint | §2.7 "Space Management Application for landside and airside" + §3.7 "Landside Coverage" — but BRD §3.3.1 detailed list (digital footprint with area, dimensions, usage, licensee, contract periods, historical trail, allotment repository, CLM integration, master plan overlay) is reduced to "Space Management Application" | §2.7 / §3.7 | binding | BRD §3.3.1 |
| S-063 | platform | Operational Digital Twin — Airside ops (GSE, turnaround, RAG, RVR, NOTAM) | Not addressed as a separate operational DT capability | n/a | binding | Register FR-DTW-AOPS-* |
| S-064 | platform | Operational Digital Twin — Terminal ops (KPI summary, queue, heatmap, dwell, retail) | Not addressed as a separate operational DT capability | n/a | binding | Register FR-DTW-TOPS-* |
| S-065 | platform | Operational Digital Twin — Curbside (vehicle, dwell, parking, trolley) | Not addressed | n/a | binding | Register FR-DTW Curbside |
| S-066 | platform | Operational Digital Twin — Security (intrusion, unattended baggage, smart trolley) | §3.2.1 Security & Perimeter agent covers; but Smart Buggy / Smart Trolley / Smart Traffic / Restroom Mgmt UI-based asset registry as a DT layer not addressed | n/a | binding | Register FR-DTW-SEC-* |
| S-067 | platform | DT visualization — Desktop GPU thick-client + WebGL browser | §2.6 + §3.4 — Unity/Unreal desktop (thick-client) + WebGL browser mentioned; but "follow-the-sun, layer show/hide, selectable areas/zones, ITBMS equipment/sensor details via web page launched from DT" not all enumerated | §2.6 | binding | Register Ops DT Visualization |
| S-068 | platform | Multi-level navigation airport→terminal→zone→floor→system→asset | Not enumerated as a capability | n/a | binding | Register Ops DT Visualization |
| S-069 | platform | OT asset visualisation at LOD 350 (no schematics) | Not described; §2.3.1 says LOD 350 BIM for T3 Domestic Departure; OT asset visualisation at LOD 350 across HVAC/FDAS/VHT/ECMS/LCMS/PBB/GPU/PCA/VDGS/WTP/STP/MRSS/BHS/ATRS/Solar/AGL not enumerated | §2.3 | binding | Register Ops DT Equipment |
| S-070 | platform | Asset federation (IT assets, SAP, ArcGIS, RMS, VMS) | §3.4.3 APOC integration + Table 4.7 mention SAP/ARM/GIS/ARC; "live VMS federation" not explicitly stated | §3.4.3 / Table 4.7 | binding | Register Asset Federation |
| S-071 | platform | Asset onboarding workflow / UI-based asset registry | §2.3.2 CAFM/CMMS data migration; "UI-based asset registry" with name/serial/type/subgroup/location not explicitly described | §2.3.2 | binding | Register Asset Registry |
| S-072 | commercial | IT asset visualisation cap =3000 units | Not stated | n/a | binding | Register IT Assets |
| S-073 | platform | Common Location Grid (CLG) / Common Asset ID (CAI) framework | Not defined; CAI / CLG not mentioned | n/a | binding | Register Asset Registry & Modeling |
| S-074 | sim | EWS (early warning signals for wait-time breach & flight-delay-at-origin) | §3.2.2 Passenger Flow agent covers; but EWS as a separate ABR §4.1 simulation capability is not itemised | §3.2.2 | binding | ABR §4.1 |
| S-075 | integration | Notam display on DT banner / disruption cascading impact | §3.6.1 IROPs / disruption engine referenced; NOTAM display and cascading impact not itemised | §3.6.1 | binding | ABR §4.1 |
| S-076 | commercial | Commercial proposal unpriced | All 8 commercial tables fully unpriced (every cell "TBC") | Tables 1-7 | binding | BRD §6 / RFP §10 |
| S-077 | submission | ≥3 case studies | Only RGIA Hyderabad (1 of 3) evidenced; 2 are `[Placeholder - bidder input]` | §6.4.1-§6.4.3 | binding | RFP App. E |
| S-078 | submission | CVs / key personnel | §4.4.5 team table is "indicative; CVs in Annexure K.1" — Annexure K.1 not present in the proposal | §4.4.5 | binding | RFP §9.3 |

---

## 2. Category distribution (skill)

| Category | Count |
|---|---|
| survey | 15 (S-001..S-014, S-059 → 15) |
| bim | 9 (S-015..S-023) |
| asset_registry | 5 (S-024..S-028 → 5) |
| integration | 8 (S-029..S-034, S-070, S-075 → 8) |
| security | 1 (S-035) |
| sla | 1 (S-036) |
| sim | 6 (S-037..S-040, S-074 → 5) |
| ai | 3 (S-041..S-043) |
| racing | 6 (S-044..S-049) |
| platform | 13 (S-050, S-051, S-058, S-060..S-069, S-071, S-073 → 13) |
| commercial_aero | 1 (S-052) |
| dashboard | 1 (S-053) |
| environmental | 2 (S-054, S-055) |
| training | 1 (S-056) |
| exclusion | 1 (S-057) |
| commercial | 2 (S-072, S-076) |
| submission | 2 (S-077, S-078) |
| **Total** | **78** |

---

## 3. Severity distribution (skill)

| Severity | Count |
|---|---|
| binding (mandatory) | ~57 |
| scored (deduction) | ~21 |
| optional (informational) | 0 |
| **Total** | **78** |

The 21 scored items are predominantly the items the client marked as "deduction" rather than "disqualifying" (e.g., department-wise dashboard mapping, leadership dashboards, RACI elaboration, training democratisation, exclusion acceptance, generic digital framework narrative, AI cross-domain correlation, AI↔BIM/IFC access pattern, BIM-IFC openBIM 4.3 standards).

---

## 4. Notes on the run

1. The skill did not read the client gap document. The gaps above were derived solely from the source-requirements vs proposal delta.
2. The skill flagged gaps the client may not have explicitly called out (e.g., S-006 10 cm contours, S-008 D-03 survey metadata, S-009 flight report, S-013 airside layers, S-060 environmental monitoring sites, S-063..S-069 Operational DT layer) — these are "skill-only" gaps the client did not enumerate but the source documents do bind.
3. The skill also did not flag every client gap (e.g., C-009 complete asset registry, C-024 simulation engine architecture detail — the skill flagged the latter as S-037, a "binding" gap on architecture detail; whether the client gap is "the same" is for the eval to compute).
4. The skill's 78 gaps include 14 categorical submission gates (S-076, S-077, S-078 + others) that the gold-requirements eval also flagged; the client gap document does not list these as gaps because they are in the proposal already (e.g., commercial tables exist, team structure exists) — they are execution gaps, not design gaps.

**End of skill-derived gap inventory.**
