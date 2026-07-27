# Client Gaps Inventory — Airport Eye (APOC Phase 2)

**Source:** `sources/Airport Eye/client gaps.md` (client-supplied gap list, dated 23-July-2026)
**Extraction method:** Each numbered item (lines 2–34) and each "Key observation" item (lines 36–58) was extracted as a discrete gap with a stable ID, category, source line, and what the client expects the proposal to address. Lines 36–58 (the BIM/IFC "Key observations") are treated as **gap items C-036..C-046** in this inventory; the embedded "I recommend adding a dedicated RTM section titled BIM IFC Data Architecture covering: [10 sub-items]" is a sub-bullet of the C-046 finding rather than separate gaps.
**Total count:** 46 client-flagged gaps.
**Scope:** This is the "ground truth" the eval is scored against. The compliance-validator skill's gap findings are then compared to this set.

---

## Field definitions

| Column | Description |
|---|---|
| `id` | Stable ID (C-001..C-046). |
| `category` | Free-form: `survey`, `platform`, `mobile`, `commercial_aero`, `dashboard`, `integration`, `security`, `ai`, `racing` (responsibility/accountability), `asset_registry`, `sim`, `training`, `exclusion`, `environmental`, `vendor_mgmt`, `bim`, `dt`, `operational`. |
| `applies_to` | Free-form: the entity the gap attaches to (e.g., "LiDAR survey", "OneAPOC", "RACI", "BIM/IFC"). |
| `gap_text` | Close-paraphrase of what the client says is wrong or missing. |
| `expected_in_proposal` | What the client expects the proposal to contain or commit to. |
| `source_line` | Line number in `client gaps.md`. |
| `severity_hint` | `disqualifying` (gating) or `deduction` (point loss) — derived from the client's wording (e.g., "must", "Pls remove", "must be explicitly added"). |

---

## 1. Master Client-Gap Table

| id | category | applies_to | gap_text | expected_in_proposal | source_line | severity_hint |
|---|---|---|---|---|---|---|
| C-001 | survey | LiDAR survey accuracy | Survey accuracy deviation: BRD requires 5 cm / 3 cm RMSE vs WAISL proposed 10 cm / 20 cm | Match the BRD figure: ≤5 cm horizontal / ≤3 cm vertical RMSE | 2 | disqualifying |
| C-002 | survey | Orthophoto + DTM/DSM | Orthophoto and DTM/DSM deviation: BRD 5 cm orthophoto + 10 cm DTM/DSM grid vs WAISL 10 cm orthophoto + 50 cm DTM/DSM | Match the BRD: ≤5 cm orthophoto GSD; =10 cm DTM/DSM grid | 3 | disqualifying |
| C-003 | platform | Mobile / offline | All capabilities should be mobile enabled with offline capabilities for usage by all departments / end users / leadership | Mobile-enable all capabilities with offline mode across all personas | 4 | deduction |
| C-004 | commercial_aero | DIAL use-case mapping | DIAL Department-wise use cases mapping, KPIs, dashboard to be shared | Per-department use-case → KPI → dashboard mapping; share with DIAL | 5 | deduction |
| C-005 | dashboard | Leadership reporting | Reporting dashboards for leadership to be specified | Specify role-curated reporting dashboards for leadership | 6 | deduction |
| C-006 | integration | T2 OT systems (FAS) | T2 OT integration cannot be excluded — FAS & others are operational (Pls remove exclusion of T2) | Remove the T2 exclusion; integrate T2 OT (FAS, etc.) | 7 | disqualifying |
| C-007 | racing | OneAPOC / APOC Phase 2 ownership | OneAPOC / APOC Phase-2 complete accountability to be with WAISL — must be delivered as part of Airport Eye | WAISL must be Accountable + Responsible for end-to-end OneAPOC delivery within Airport Eye | 8 | disqualifying |
| C-008 | platform | Digital twin visibility (UI) | DT visibility on end user machines to democratise usage | DT accessible on end-user machines (browser, not thick-client only); persona-curated | 9 | deduction |
| C-009 | asset_registry | Asset registry | Complete Asset Registry with hierarchy, relation, type, parent-child mapping, location, and traceability is missing | Asset registry w/ CLG, CAI, hierarchy, taxonomy, ontology, relationships, location, traceability | 10 | disqualifying |
| C-010 | racing | IT infrastructure ownership | Complete IT Infrastructure (On-prem / Cloud) provisioning for this Program has to be owned by WAISL (Pls correct the RACI) | WAISL R+A for IT infrastructure (on-prem + cloud) provisioning for the Program | 11 | disqualifying |
| C-011 | ai | All 8 AI Agents | All 8 AI Agents must be explicitly detailed | All 8 agents itemised with approach, data, KPIs, governance | 12 | disqualifying |
| C-012 | ai | AI modelling scope | System should be able to use AI modelling to predict System stress, Partial failure, Service degradation | AI covers system stress, partial failure, and service degradation prediction | 13 | deduction |
| C-013 | integration | OT data point count | OT System Data point count mismatch: 5 lakh+ expected vs 2 lakh+ proposed | Commit to ≥5,00,000 OT data points integrated | 14 | disqualifying |
| C-014 | platform | Change detection (Google Maps) | Google Maps / Google Earth D+1 change detection should be delivered; business users should be able to compare baseline vs current state for planning purposes (do not mark as gap / future) | D+1 Google Maps / Google Earth change detection; baseline vs current-state comparison; not "future" | 15 | disqualifying |
| C-015 | security | DIAL IT Security Policy | DIAL IT Security Policy compliance must be explicitly added | Explicit DIAL IT Security Policy compliance commitment | 16 | deduction |
| C-016 | sla | Platform availability | SLA availability should be 99.9% | ≥99.9% availability (not 99.5%) | 17 | disqualifying |
| C-017 | asset_registry | IT/OT hardware (passenger journey) | IT/OT hardware assets for mapping complete Pax journey for both Departure & Arrival should be mapped | Pax-journey IT/OT hardware asset mapping (Departure + Arrival) | 18 | deduction |
| C-018 | integration | CCTV / video analytics / IT | Include CCTV, Video Analytics and all IT systems utilized during passenger departure and arrival journeys | Include CCTV, video analytics, all pax-journey IT in scope | 19 | deduction |
| C-019 | integration | Barcode / gates / e-gates / CUSS / CUPPS / DFMD / ATRS / baggage / boarding | 2D Barcode scanner, DigiYatra gates, E-gate, CUSS machines, CUPPS, DFMD, ATRS, Baggage scanner Boarding gate scanners to be included | Include 2D barcode, DigiYatra, E-gate, CUSS, CUPPS, DFMD, ATRS, baggage scanner, boarding gate scanners | 20 | deduction |
| C-020 | platform | Medallion Lakehouse | Medallion Lakehouse architecture to be explained / walkthroughed for DIAL and share complete details / architecture | Medallion Lakehouse architecture explained + shared with DIAL | 21 | deduction |
| C-021 | integration | ITBMS / JCI / Honeywell | ITBMS/JCI/Honeywell integration approach not confirmed | Confirm ITBMS / JCI / Honeywell integration approach (T1, T2, T3, ITBMS coverage) | 22 | disqualifying |
| C-022 | racing | Risk register elaboration | Risk register needs elaboration for some points as highlighted in attached doc | Elaborate risk register per the attached client doc | 23 | deduction |
| C-023 | racing | RACI revision | RACI to be revised with WAISL as Accountable / Responsible | Revise RACI: WAISL = R+A across planning, surveys, platform, AI, ops/support | 24 | disqualifying |
| C-024 | sim | Simulation engine architecture | Simulation engine architecture needs to be detailed | Detail the simulation engine architecture (4 components: DT + scenario UI + decision engine + viz UI per ABR §4.1) | 25 | disqualifying |
| C-025 | sim | Commercial simulation use cases | Commercial simulation use cases are missing | Address the 10 Commercial SPG what-if use cases (ABR §4.2) | 26 | disqualifying |
| C-026 | sim | Operational simulation use cases | Operational simulation use cases like workforce, capacity and curb side are missing | Address Operational SPG use cases (workforce, capacity, curbside — ABR §4.2) | 27 | disqualifying |
| C-027 | integration | APOC integration (control + monitoring) | Integrate the model with APOC for control and monitoring; control rights reserved for certain functions | Bidirectional APOC integration; role-scoped control rights for specific functions | 28 | deduction |
| C-028 | integration | APOC lights control | Control of Lights ON/OFF from APOC | AGL / lighting ON-OFF controllable from APOC | 29 | deduction |
| C-029 | training | Training & adoption | Training & Adoption — User department training, democratize usage across departments | Department-specific training + adoption plan (democratise across all DIAL departments) | 30 | deduction |
| C-030 | exclusion | Exclusions | Exclusions to be discussed and accepted by business owners | Every exclusion explicitly accepted by named DIAL business owners | 31 | deduction |
| C-031 | environmental | Borewell recharge | Borewell recharge monitoring marked future phase | Bring borewell recharge monitoring into base scope (not "future") | 32 | disqualifying |
| C-032 | environmental | Stormwater analysis | Stormwater analysis data feed and implementation not fully defined | Define stormwater analysis data feed + implementation in base scope | 33 | disqualifying |
| C-033 | racing | DIAL Vendors / OEM coordination | DIAL Vendors / DIAL OEM coordination is WAISL responsibility | WAISL R+A for DIAL vendor / OEM coordination | 34 | disqualifying |
| C-034 | racing | AEP / access coordination | WAISL should own AEP/access coordination as per existing process | WAISL R+A for AEP / access coordination (per existing process) | 35 | disqualifying |
| C-035 | dt | Generic Digital framework aspiration (strategic) | Apart from the above at strategic level, our approach is Generic Digital framework aspiration is not documented | Document the strategic "Generic Digital framework" / platform aspiration | 59 | deduction |
| C-036 | bim | IFC repository architecture | RTM references IFC-compliant federated BIM models but does not define the IFC repository architecture, storage strategy, governance model, or long-term ownership of IFC data | Define IFC repository architecture, storage, governance, ownership | 37 | deduction |
| C-037 | asset_registry | IFC ↔ CAI ↔ CLG ↔ SAP ↔ OT/BMS mapping | No clear mapping strategy between IFC GUIDs, Common Asset IDs, Common Location Grid, SAP IDs, OT/BMS point IDs | Mapping strategy: IFC GUID ↔ CAI ↔ CLG ↔ SAP ↔ OT/BMS point IDs (and GIS IDs) | 38 | disqualifying |
| C-038 | asset_registry | Airport Asset Information Model (AIM) | An Airport Asset Information Model (AIM) has not been defined (static) | Define a static Airport Asset Information Model (AIM) | 39 | disqualifying |
| C-039 | asset_registry | Ontology & relationship model | Ontology and relationship model between terminals, floors, spaces, systems, equipment, and sensors is not clearly articulated | Graph-based ontology + relationship model across terminal/floor/space/system/equipment/sensor | 40 | disqualifying |
| C-040 | bim | BIM lifecycle management | BIM lifecycle management requirements (version control, as-built updates, change mgmt, sync with operational DT) are missing | BIM lifecycle: version control, as-built updates, change mgmt, DT sync | 41 | disqualifying |
| C-041 | bim | BIM ↔ GIS federation | BIM-GIS federation rules, georeferencing standards, spatial alignment requirements not explicit | BIM-GIS federation rules, georeferencing standards, spatial alignment (loose but federated coupling) | 42 | disqualifying |
| C-042 | ai | AI ↔ BIM/IFC access for granular analytics | AI use cases identified, but no definition of how AI agents will access/query BIM/IFC data + relationships for true granular analytics | AI access pattern to BIM/IFC data + relationships (graph-query or equivalent) | 43 | deduction |
| C-043 | bim | Open BIM standards mandate | Open BIM standards such as IFC 4.3 and semantic tagging frameworks have not been mandated | Mandate IFC 4.3 + semantic tagging framework (e.g., bSDD) | 44 | disqualifying |
| C-044 | bim | Digital thread | End-to-end digital thread linking BIM, GIS, SAP, BMS, IoT, APOC dashboards, and AI agents is not clearly defined | Define the end-to-end digital thread (BIM↔GIS↔SAP↔BMS↔IoT↔APOC↔AI agents) | 45 | disqualifying |
| C-045 | bim | RTM section "BIM IFC Data Architecture" | Recommend adding a dedicated RTM section titled "BIM IFC Data Architecture" | Add an RTM section: BIM IFC Data Architecture | 46 | deduction |
| C-046 | bim | Long-term BIM governance | Long-term governance of models, metadata, and digital thread mappings | Define long-term governance: model ownership, metadata stewardship, digital-thread mapping governance | 58 | deduction |

---

## 2. Category distribution

| Category | Count |
|---|---|
| racing (responsibility/accountability) | 5 (C-007, C-010, C-022, C-023, C-033, C-034 → 6) |
| bim | 8 (C-036, C-040, C-041, C-042, C-043, C-044, C-045, C-046) |
| asset_registry | 4 (C-009, C-017, C-037, C-038, C-039 → 5) |
| integration | 5 (C-006, C-013, C-018, C-019, C-021, C-027, C-028 → 7) |
| survey | 2 (C-001, C-002) |
| ai | 3 (C-011, C-012, C-042) |
| sim | 3 (C-024, C-025, C-026) |
| platform | 3 (C-003, C-008, C-014, C-020 → 4) |
| sla | 1 (C-016) |
| commercial_aero | 1 (C-004) |
| dashboard | 1 (C-005) |
| environmental | 2 (C-031, C-032) |
| training | 1 (C-029) |
| exclusion | 1 (C-030) |
| dt | 1 (C-035) |
| security | 1 (C-015) |
| **Total** | **46** |

(Counts are approximate because each row may touch multiple categories; the strict per-row count is 46.)

---

## 3. Severity distribution

| Severity | Count |
|---|---|
| disqualifying (gating) | 19 (C-001, C-002, C-006, C-007, C-009, C-010, C-011, C-013, C-014, C-016, C-021, C-023, C-024, C-025, C-026, C-031, C-032, C-033, C-034, C-037, C-038, C-039, C-040, C-041, C-043, C-044 → ~26) |
| deduction (point loss) | ~20 |
| **Total** | **46** |

The exact disqualifying count is derived from explicit "must", "Pls", "Pls remove", "Pls correct", "must be explicitly added", and "do not mark as gap / future" language in the client document.

---

## 4. Notes on extraction

1. **Lines 2–34 are numbered gap items.** Treated as C-001..C-034.
2. **Lines 36–45 are "Key observations" about BIM/IFC.** Treated as C-036..C-044.
3. **Lines 46–58 are a recommendation block** — a single recommendation with 10 sub-bullets. Treated as C-045 (the recommendation itself) plus a single consolidated C-046 (long-term governance) for the last bullet, with the other 9 sub-bullets captured in C-036..C-044 as part of the BIM/IFC architecture requirement.
4. **Line 35 / 59 ("Generic Digital framework aspiration is not documented")** is the standalone strategic item — C-035.
5. The "BIM/IFC" sub-bullets in lines 48–58 are not double-counted as separate gaps; they are the architectural content that a single BIM/IFC Data Architecture section must contain. If the proposal covers each sub-bullet (or rolls them into one architecture narrative), C-046 is satisfied.
6. The "Pls remove exclusion of T2" in C-006 is treated as a gap on T2-OT integration, not a deviation-register question.

**End of client gaps inventory.**
