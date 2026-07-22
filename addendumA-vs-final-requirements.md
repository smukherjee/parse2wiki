# Addendum A vs. Final Requirements Register — Coverage Comparison

## 1. Source Note

**Selected sources:**
- `/Users/sujoymukherjee/code/doc2md/parse2wiki/sources/Airport Eye/_analysis/proposal_v11/AddendumA_Use_Case_Coverage_Matrix.md` — Bidder-prepared use-case coverage matrix (48 rows mapped from ABR and CIO Scope Review).
- `/Users/sujoymukherjee/code/doc2md/parse2wiki/sources/Airport Eye/Final requirements.xlsx.md` — Internal requirements register containing detailed BIM, integration, IT/OT asset, Digital Twin widget, functional requirement, and asset-registry rows.

**Scope restriction:** Analysis is restricted to these two files. The Addendum A matrix is an interpretation of the ABR/CIO Review, while the Final Requirements Register is a more granular, internal delivery-oriented register. They serve different purposes, but the comparison reveals whether the high-level use-case coverage in Addendum A is traceable to the detailed requirements the delivery team has captured.

**Files excluded by user selection:**
- Buyer-issued BRD v1.5 / RFP v5 / ABR document
- Volume 2 (Components 1–6) and Volume 3 (AI agents & simulation)
- Comprehensive Gap Analysis
- DIAL CIO Scope Review minutes
- Appendix K.5 Clarification Log

**Gaps due to source limitation:**
- Cannot verify whether the Final Requirements Register is the authoritative DIAL requirements baseline or an internal bidder work product.
- Cannot confirm whether missing matches mean a requirement is genuinely absent or simply expressed differently in the register.
- Cannot validate technical implementation claims without the volume responses.

---

## 2. Executive Summary

The comparison shows that **Addendum A does not fully cover the detailed requirements in the Final Requirements Register**. Addendum A is strong on the ABR/CIO Review use-case library (its stated purpose), but it omits or under-represents a large number of granular Digital Twin functional requirements, OT/IT asset visualization requirements, widget requirements, and asset-registry requirements that appear in the Final Requirements Register. Conversely, several ABR use cases are either not expressed in the Final Requirements Register or are expressed at a higher level of abstraction. The two documents appear to have been prepared from different baselines: Addendum A from the ABR/CIO Review narrative, and the Final Requirements Register from a system-by-system delivery breakdown. Before submission, the bidder must reconcile these two views into a single, traceable requirements map so that evaluators can verify every use case against a concrete requirement and acceptance criterion.

---

## 3. Addendum A Coverage Summary

| Addendum A domain | Rows mapped | Delivered | Delivered (data feed TBC) | Future (Phase 2) | TBC |
|-------------------|-------------|-----------|---------------------------|--------------------|-----|
| P&E (§3.1) | 2 | 0 | 1 | 1 | 0 |
| S&V (§3.2) | 5 | 5 | 0 | 0 | 0 |
| Commercial Aero (§3.3) | 3 | 1 | 1 | 1 | 0 |
| Operations (§3.4) | 5 | 2 | 2 | 1 | 0 |
| SPG §4.1 | 5 | 3 | 2 | 0 | 0 |
| SPG §4.2 Commercial | 10 | 2 | 7 | 1 | 0 |
| SPG §4.2 Operational | 8 | 5 | 2 | 1 | 0 |
| SPG §4.2 Engineering | 5 | 4 | 1 | 0 | 0 |
| Passenger-journey IT monitoring (CIO Review) | 6 | 0 | 6 | 0 | 0 |
| APOC / APOC Phase-2 integration (CIO Review) | 2 | 0 | 2 | 0 | 0 |
| **Total** | **48** | **16** | **24** | **5** | **3** |

---

## 4. Final Requirements Register Summary

The Final Requirements Register contains at least **459 markdown table rows** across the following broad categories (identified from structure and content):

| Category | Approximate row count | Key contents |
|----------|----------------------|--------------|
| BIM modelling (T1, T2, T3, asset attribution, MEP) | ~70 | Floor-by-floor BIM scope, areas, LOD, dependencies |
| OT integrations — Facilities (HVAC, FDAS, VHT, ECMS, PBB, VDGS, LCMS, BHS, ATRS, GPU, WTP, STP, MRSS, etc.) | ~90 | System-by-system point counts, OEMs, delivery months, phases |
| OT integrations — Common / airside (AGL, solar, noise, access control) | ~20 | Shared infrastructure |
| IT integrations (UTAM, Telematics, AODB, ADS-B, ARC, RMS, Kloudspot, XOVIS, PTM, SAC, ITOM, VMS/CCTV, GIS, SAP, DigiYatra, CUSS, CUPPS, E-Gates, SBD, etc.) | ~60 | OneAPOC feeds, passenger-processing systems |
| Ops DT: Visualization — structure, interiors, equipment (LOD 200/350) | ~100 | Asset-level visualization requirements for T1/T2/T3 |
| IT Assets visualization | ~15 | FIDS/CUPPS/E-Gates per terminal, capped at 3,000 |
| Functional Requirements — DT Widgets & Use Cases (FR-DTW-*) | ~40 | Airport/terminal/airside/curbside/security summary, KPIs, queue, crowd, dwell, camera access, playback, etc. |
| SAC / Smart City / IoT Gateway | ~15 | Smart washroom, smart buggy, smart trolley, smart traffic, asset registry, IoT onboarding |
| Simulation functional requirements | ~10 | NOTAM, EWS, what-if, disruption, passenger-journey monitoring |
| Functional Requirements — OT/IT Widgets | ~50+ | Per-equipment KPIs and widgets for HVAC, FDAS, VHT, PBB, VDGS, GPU, PCA, ATRS, BHS, WTP, STP, MRSS |
| Asset Registry & Modeling | ~10 | OT asset counts and modelling scope |

The register contains **20 explicitly tagged FR-DTW requirement IDs**:
`FR-DTW-01`, `FR-DTW-02`, `FR-DTW-03`, `FR-DTW-04`, `FR-DTW-15`, `FR-DTW-AOPS-01` through `AOPS-12`, `FR-DTW-SEC-01`, `FR-DTW-TOPS-01`, `FR-DTW-TOPS-02`.

---

## 5. Coverage Match Analysis

### 5.1 Addendum A use cases that **are** clearly reflected in the Final Requirements Register

| Addendum A use case | Final Requirements Register evidence | Match quality |
|---------------------|--------------------------------------|---------------|
| Reverse-entry detection | FR-DTW-SEC-01 "Intrusion and Reverse-entry Detection" | Direct |
| Unattended-baggage detection | FR-DTW-SEC-01 "Unattended Baggage alert" | Direct |
| Behaviour analytics / suspicious behaviour | FR-DTW-SEC-01 "Suspicious Behaviour Detection" | Direct |
| Google Maps / satellite integration | Not explicitly found, but GIS and external basemap layers are implied | Indirect |
| What-if scenario analytics | Simulation section "What if Simulation" | Direct |
| Monitoring / alerting of IT systems | Passenger-journey monitoring section + IT assets (DigiYatra, CUSS, CUPPS, E-Gates, SBD, etc.) | Direct |
| Live operations monitoring dashboard | FR-DTW-01/03/04 (Airport/Terminal/Airside summary) | Direct |
| Overstaying / unidentified passengers | Simulation section "Passenger journey — Availability monitoring" / Reverse PaxFlow | Direct |
| Gate allocation optimization | FR-DTW-AOPS-05 (stand/gate utilization), RMS integration | Direct |
| Queue management optimization | FR-DTW-TOPS-02 "Queue Management across all touch points" | Direct |
| Baggage flow optimization | BHS integration rows (INTF-T1/T2/T3-BHS) | Direct |
| Thermal load simulation | HVAC widget requirements / engineering use case | Indirect |
| Zone-based cooling optimization | HVAC AHU/zone telemetry | Indirect |
| Power infrastructure stress testing | MRSS / ECMS integration rows | Indirect |
| APOC integration | Multiple FR-DTW-* references to OneAPOC | Direct |

### 5.2 Addendum A use cases that are **weakly represented or absent** in the Final Requirements Register

| Addendum A use case | Why it is weak/absent in register | Risk |
|---------------------|----------------------------------|------|
| **Borewell recharge monitoring** | Not found in register. Only stormwater/WTP/STP appear. | Phase 2 classification may be correct, but register does not support it. |
| **IROPS Simulation** | Simulation section mentions "Disruption Management" and "What if", but not IROPS specifically. | IROPS is a specific operational term; needs explicit mapping. |
| **Evacuation & Fire Scenarios** | FDAS integration exists, but no explicit evacuation/fire simulation requirement. | Safety-critical; needs dedicated FR or test case. |
| **Shelf Merchandising Optimisation** | No shelf-level retail data requirement in register. | Correctly Phase 2, but should be traceable to a retail/F&B line item. |
| **Dwell Time Monetisation** | Dwell and journey time is in FR-DTW-TOPS-02, but monetisation link to retail/F&B is not explicit. | Commercial value proposition is weak in register. |
| **Campaign & Promotion Simulation** | No POS/campaign data requirement visible. | Phase 2/TBC status plausible but unsupported by register. |
| **Queue vs Revenue Trade-off** | Queue management exists; revenue/POS trade-off does not. | Commercial optimisation not captured in register. |
| **Lounge vs Retail Trade-off** | No lounge access/retail data requirement. | Phase 2/TBC status plausible. |
| **Disruption Monetisation Strategy** | Disruption management exists; monetisation link not explicit. | Commercial angle missing in register. |
| **Thermal Load Simulation** | HVAC telemetry exists, but "thermal load simulation" as a use case is not explicitly named. | Engineering use case traceability is weak. |
| **Security asset mapping** | Access control and security assets are in OT integration, but no explicit "security asset mapping" use case. | Could be inferred from 3D Space Management; needs explicit mapping. |
| **Google Maps / satellite integration** | GIS basemap is mentioned, but Google Maps specifically not found. | Phase 2 due to licence; needs confirmation. |
| **Surface navigation in low visibility (fog)** | RVR/weather feeds exist, but no explicit low-visibility navigation use case. | Phase 2 plausible; safety evaluators may ask for it. |
| **Staffing vs Sales Optimisation** | WFM integration exists in register, but not tied to sales/retail simulation. | Cross-domain use case not explicit. |
| **Retail Expansion Energy Impact** | Energy/ECMS and retail exist separately; combined simulation not explicit. | Engineering-commercial cross-over missing. |

### 5.3 Detailed Final Requirements Register items that are **not explicitly covered** by Addendum A

The following requirement categories from the Final Requirements Register have **no direct counterpart** in the 48 Addendum A use cases:

| Register category | Examples | Coverage gap |
|-------------------|----------|--------------|
| **BIM modelling floor-by-floor scope** | BIMM-T1-01 to T3MEP-01, LOD 200/300/350 | Addendum A assumes BIM deliverables but does not map use cases to specific floor/model scope. |
| **OT asset visualization at LOD 350** | T1 HVAC 1,000 assets, T3 BHS 1,300 assets, PESC 800 assets | Addendum A does not enumerate asset-level visualization requirements. |
| **Per-equipment KPI widgets** | HVAC chiller/pump/cooling tower/AHU/PAHU/FCU; FDAS detectors; VHT lifts/escalators; PBB; VDGS; GPU; PCA; ATRS; BHS conveyors/sorters/screening; WTP/STP/MRSS | Addendum A covers higher-level agents but not the per-asset widget requirements that dominate the register. |
| **Curbside functional requirements** | Vehicle classification, curb occupancy, dwell time, incident identification, congestion heatmap, ground transport availability, meet-and-greet crowd, parking, trolley availability | Only "landside traffic & curbside management" is in Addendum A as Phase 2. The register has 10+ detailed curbside requirements. |
| **Terminal Operations widgets** | Retail/F&B store performance trends, store location analysis, historical playback, counter/desk allocation | Partially covered by commercial use cases, but many register items are not mapped. |
| **Airside Ops widgets** | GSE position, flight position, turnaround activities, airside alerts, predictive turnaround metrics (POBT/PRBT/PIBT), airside playback, NOTAM | Addendum A has IROPS and gate allocation, but misses detailed airside widget requirements. |
| **SAC / Smart City / IoT onboarding** | Smart washroom, smart buggy, smart trolley, smart traffic, asset registry, IoT gateway onboarding | Not covered in Addendum A. |
| **ITOM / Manage engine integration** | IT infrastructure health telemetry | Not covered. |
| **Asset registry requirements** | Asset unique name, serial number, type, subgroup, location, OT critical info widgets | Not covered in Addendum A. |
| **Early Warning System (EWS)** | Wait-time threshold breach, delay prediction | Mentioned in register's simulation section but not in Addendum A. |
| **T2 OT estate** | Most T2 integrations marked "Doesn't exist", "Not Present", "Upcoming" | Addendum A does not address the T2 dormant-binding implications visible in the register. |

---

## 6. Inconsistencies Between the Two Sources

| Topic | Addendum A position | Final Requirements Register position | Implication |
|-------|---------------------|--------------------------------------|-------------|
| **Borewell recharge** | Future (Phase 2) | Not present | Addendum A introduces a scope boundary the register does not confirm. |
| **Google Maps / satellite** | Future (Phase 2) | GIS basemap implied, not specified | Phase 2 classification depends on licence/API, not register. |
| **Low-visibility / fog navigation** | Future (Phase 2) | RVR/weather feeds exist, but no use case | Exclusion is an Addendum A interpretation; register does not support or contradict it. |
| **Curbside capabilities** | One Phase-2 line item | 10+ detailed curbside requirements in Phase 1b/1c and Phase 2 | Addendum A under-represents curbside scope complexity. |
| **Retail / commercial use cases** | 10 commercial simulation use cases | Retail/F&B store performance and store location analysis listed as Phase 2 | Addendum A includes several commercial cases the register only partially supports. |
| **IROPS simulation** | Delivered | Disruption management / what-if in register, IROPS not named | Terminology mismatch; may confuse evaluators. |
| **Evacuation / fire scenarios** | Delivered | FDAS integration only | Safety simulation not explicitly in register. |
| **Passenger-journey IT monitoring** | 6 Delivered (data feed TBC) use cases | DigiYatra, CUSS, CUPPS, E-Gates, SBD, etc. listed but mostly undetailed | Addendum A is more specific than the register for this area. |
| **T2 scope** | Not explicitly addressed | Many T2 systems marked "Doesn't exist" / "Not Present" / "Upcoming" | Addendum A does not reflect T2 delivery risk visible in register. |
| **OT asset visualization LOD 350** | Not explicitly enumerated | Detailed asset counts and delivery months per terminal | Addendum A is too abstract to prove LOD 350 coverage. |
| **Per-equipment widgets** | Not covered | Dominates the register (~50+ rows) | Addendum A misses the bulk of operational DT functionality. |

---

## 7. Compliance and Traceability Assessment

### 7.1 Traceability strengths

- Addendum A maps high-level ABR/CIO Review use cases to owner modules/agents.
- The Final Requirements Register provides the detailed system-by-system and asset-by-asset delivery scope.
- Where both documents overlap (e.g., security use cases, queue management, APOC integration), the match is direct.

### 7.2 Traceability weaknesses

- **Two separate baselines:** Addendum A is use-case-driven; the register is system/integration-driven. They are not cross-referenced to each other.
- **Addendum A is too high-level** to prove compliance with the detailed register requirements.
- **Register lacks use-case framing:** many register items are not tied back to the ABR stakeholder use cases, making it hard for evaluators to see business value.
- **Missing bidirectional traceability:** there is no single matrix that maps every FR-DTW requirement and every integration row to an Addendum A use case and an acceptance test.

---

## 8. Proposal Gaps, Risks, and Clarifications

### 8.1 Critical gaps

1. **Addendum A does not cover the bulk of the Final Requirements Register.** The register contains ~459 rows; Addendum A covers only 48 use-case themes. Many detailed functional, widget, and asset-visualization requirements are absent from Addendum A.
2. **No bidirectional traceability matrix.** Neither document cross-references the other. Evaluators cannot verify that every register requirement is addressed by a use case, or that every use case is backed by detailed requirements.
3. **Commercial use cases are weakly grounded.** Several ABR commercial use cases are not reflected in the register, making their base-scope delivery claim hard to justify.
4. **Safety-critical use cases lack register support.** Evacuation/fire scenarios and low-visibility navigation are either absent or not explicitly tied to detailed requirements.
5. **T2 delivery risk is not visible in Addendum A.** The register shows many T2 systems as "Doesn't exist" / "Not Present" / "Upcoming"; Addendum A does not acknowledge this.

### 8.2 High-priority partials / scoring risks

6. **Curbside requirements** are under-represented in Addendum A.
7. **SAC / Smart City / IoT onboarding** requirements are not covered.
8. **Per-equipment KPI widgets** (the core of operational monitoring) are not mapped to use cases.
9. **Asset registry requirements** are not linked to use cases.
10. **Early Warning System (EWS)** and predictive turnaround metrics are not in Addendum A.

### 8.3 Clarification questions for DIAL

| # | Question | Urgency |
|---|----------|---------|
| Q-01 | Is the Final Requirements Register the authoritative requirements baseline for evaluation, or is the ABR/CIO Review the primary baseline? | High |
| Q-02 | Are the 5 Phase-2 use cases in Addendum A (borewell, Google Maps, fog navigation, shelf merchandising, landside traffic) acceptable as out-of-scope? | High |
| Q-03 | Should the detailed functional/widget requirements in the register (curbside, SAC, EWS, per-equipment widgets) be explicitly traced to Addendum A use cases? | Medium |
| Q-04 | Is T2 scope contingent on DIAL-provided OT systems, as the register implies? | Medium |

### 8.4 Internal questions for bidder teams

| # | Question | Owner |
|---|----------|-------|
| I-01 | Was the Final Requirements Register prepared from the same ABR baseline as Addendum A, or from a separate workshop/assessment? | BA / delivery |
| I-02 | Can every FR-DTW requirement in the register be mapped to an Addendum A use case? | BA / proposal |
| I-03 | Are the commercial use cases in Addendum A actually costed in the commercial proposal? | Commercial |
| I-04 | How do we demonstrate LOD 350 OT asset visualization for the asset counts in the register? | BIM / DT team |
| I-05 | What is the fallback if T2 OT systems are not commissioned as per the register? | Delivery / PM |

---

## 9. Recommended Response Structure

To close the gap between Addendum A and the Final Requirements Register, the bidder should produce a single, consolidated **Requirements Traceability Matrix (RTM)** with the following columns:

1. **Requirement ID** (from Final Requirements Register, e.g., FR-DTW-*, INTF-*, BIMM-*, ODT-*)
2. **Requirement description**
3. **Stakeholder use case** (from Addendum A / ABR)
4. **Owner module / agent**
5. **Coverage status** (Delivered / Delivered (data feed TBC) / Future Phase 2 / TBC / Not addressed)
6. **Delivery phase / milestone**
7. **Data / integration dependency**
8. **Acceptance criterion / test case**
9. **Commercial inclusion** (base cost / optional / change request)
10. **Source reference** (Addendum A row + Final Requirements Register row)

This RTM should be placed in the **Appendices** and referenced in the main proposal's **Scope Alignment and Compliance Matrix** section.

---

## 10. Missing Internal Inputs

Before the response can be finalized, the bidder must:

- [ ] Confirm which document is the authoritative requirements baseline (ABR/CIO Review vs. Final Requirements Register).
- [ ] Produce a bidirectional traceability matrix linking every register requirement to an Addendum A use case or explicitly marking it out-of-scope.
- [ ] Resolve terminology mismatches (e.g., IROPS vs. disruption management; evacuation/fire scenarios vs. FDAS integration).
- [ ] Add coverage for register items not in Addendum A: curbside, SAC/Smart City/IoT, per-equipment widgets, asset registry, EWS, T2 scope.
- [ ] Confirm commercial inclusion of all Addendum A "Delivered" and "Delivered (data feed TBC)" use cases.
- [ ] Define acceptance criteria and test cases for each use case.
- [ ] Document T2 dormant-binding fallback and DIAL confirmation process.

---

## 11. Aviation Regulatory Matrix

*Aviation overlay is active because both documents relate to airport operations, airside/landside systems, and aviation security.*

| Regulation / Standard | Requirement Summary | Addendum A coverage | Register coverage | Gap |
|-----------------------|---------------------|---------------------|-------------------|-----|
| **ICAO Annex 14** | OLS monitoring | Not covered in Addendum A | OLS application implied in Geo DT functionality ("Measure lengths & distances across the airport") | Addendum A misses OLS. |
| **BCAS / AAI security** | Reverse-entry, unattended baggage, suspicious behaviour, breach detection | Covered | FR-DTW-SEC-01 covered | Good alignment. |
| **DGCA / AAI airside access** | Airside ops, GSE tracking, flight position, NOTAM | Partial (IROPS, gate allocation) | FR-DTW-AOPS-* covered in detail | Addendum A too high-level. |
| **Safety / fire** | Evacuation/fire scenarios | Covered in Addendum A | FDAS integration only | Register lacks explicit evacuation simulation. |
| **DPDPA 2023** | Passenger flow, DigiYatra, Wi-Fi/RTLS | Passenger Flow agent covers | IT asset monitoring covers | Privacy controls not explicit in either. |
| **CERT-In** | IT/OT integration security | Not explicit | ITOM / security implied | Needs explicit cybersecurity mapping. |

---

## 12. Aviation Safety and Operational Constraints

| Constraint | Addendum A treatment | Register treatment | Implication |
|------------|----------------------|--------------------|-------------|
| **24×7 live operations** | Assumed via platform architecture | Detailed cutover/phase dependencies | Register better reflects operational risk. |
| **Airside work restrictions** | Not addressed | T2 systems "Not Present" / "Upcoming" | Register shows T2 risk; Addendum A does not. |
| **Safety systems (fire / evacuation)** | Evacuation/fire scenario use case | FDAS integration and BIM | Need explicit tie between FDAS data and evacuation simulation. |
| **Low-visibility operations** | Phase 2 | RVR/weather feeds in Phase 1c | Phase 2 exclusion may be questioned by ops. |
| **Curbside/landside congestion** | Phase 2 | Multiple Phase 1b/1c + Phase 2 requirements | Addendum A under-represents curbside complexity. |

---

## 13. Aviation Integration and Acceptance

| System / Integration | Addendum A use case | Register requirement | Coverage assessment |
|----------------------|---------------------|----------------------|---------------------|
| **OneAPOC / APOC Phase-2** | APOC integration (data feed TBC) | FR-DTW-01/03/04, AOPS/TOPS widgets | Addendum A high-level; register detailed. |
| **AODB / RMS** | Gate allocation optimization | FR-DTW-AOPS-05, RMS integration | Good. |
| **BHS / BRS** | Baggage flow optimization | BHS integration rows (T1/T2/T3) | Good. |
| **XOVIS / Kloudspot** | Queue management, dwell time | FR-DTW-TOPS-02 queue, crowd, dwell | Good. |
| **DigiYatra** | IT systems monitoring | DigiYatra row in IT integrations | Good, but DigiYatra status is TBC. |
| **SAC / Smart City** | Not covered | SAC smart washroom/buggy/trolley/traffic, IoT gateway | **Gap.** |
| **VMS/CCTV** | Security use cases | VMS/CCTV live feed to DT | Register covers; Addendum A assumes PSIM/CCTV. |
| **ITOM / Manage engine** | Not covered | IT infrastructure health telemetry | **Gap.** |

---

## 14. Aviation Risk Flags

| Risk Category | Risk | Severity | Source |
|---------------|------|----------|--------|
| **Regulatory / safety** | Evacuation/fire scenarios claimed in Addendum A but register only shows FDAS integration | Medium | Addendum A §6; Register FDAS rows |
| **Regulatory / safety** | Low-visibility navigation pushed to Phase 2 while register has RVR/weather feeds in Phase 1c | Medium | Addendum A §5; Register FR-DTW-AOPS-08 |
| **Operational** | Addendum A does not reflect T2 OT estate "Not Present" / "Upcoming" risk | High | Register T2 integration rows |
| **Integration** | 24 data-feed-TBC use cases depend on third-party/API readiness | High | Addendum A summary counts |
| **Commercial** | Many commercial use cases not explicitly in register | Medium | Addendum A §7 |
| **Acceptance** | No bidirectional traceability between 48 use cases and ~459 register rows | **High** | Both documents |

---

## 15. Evidence Mapping for Proposal Use

| Requirement / theme | Addendum A evidence | Register evidence | Strength | Best response section |
|---------------------|---------------------|-------------------|----------|---------------------|
| ABR stakeholder use cases | 48 mapped rows | N/A | Medium | Scope alignment / Addendum A |
| Detailed functional requirements | N/A | FR-DTW-* rows | High | Technical solution / widget specs |
| OT asset visualization | High-level agent coverage | Per-asset counts and LOD 350 rows | High | Technical solution §2.6 |
| Integration estate | Data feed TBC list | System-by-system point counts and OEMs | High | Integration approach |
| Commercial use cases | Simulation engine claims | Retail/F&B rows (Phase 2) | Medium | Commercial proposal / scope |
| T2 delivery risk | Not addressed | T2 rows marked absent/upcoming | High | Assumptions / dependencies |
| SAC / Smart City | Not addressed | SAC/IoT gateway rows | Low | Gap to be filled |

---

## 16. Differentiators and Proof Gaps

### Differentiators that can be claimed

1. **Comprehensive ABR use-case coverage** — 48 use cases mapped across stakeholder domains.
2. **Detailed integration inventory** — register shows system-by-system point counts and OEMs.
3. **LOD 200/300/350 BIM and asset visualization scope** — register provides floor/area/asset detail.

### Proof gaps

1. **Two disconnected documents** — no single traceability matrix.
2. **Addendum A too abstract** — does not prove coverage of the detailed register.
3. **Register lacks business framing** — many technical requirements are not tied to stakeholder use cases.
4. **Commercial/safety use cases weakly grounded** — several ABR use cases are not in the register.
5. **T2 risk not surfaced** — register shows problems Addendum A ignores.

### Recommendation

The bidder should not rely on Addendum A alone for compliance. Create a consolidated **Requirements Traceability Matrix** that links:
- ABR/CIO Review use case → Addendum A row → Final Requirements Register row(s) → owner module/agent → acceptance criterion → commercial inclusion.

This will convert two disconnected documents into a defensible compliance story.

---

**End of comparison.**
