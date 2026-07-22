# Gold Score — Track A Proposal

**Proposal scored:** `eval/airport-eye/trackA/proposal-trackA.md` (WAISL Limited, APOC Phase 2 / Airport Eye)
**Gold inventory:** `eval/airport-eye/gold-requirements.md` (189 requirements: 125 categorical + 64 numeric)
**Date:** 2026-07-17
**Scorer:** SCORING agent (controlled eval), rigorous/unbiased standard

---

## 1. Summary

| Verdict | Count |
|---|---|
| Pass | 108 |
| Partial | 51 |
| Fail | 21 |
| Ambiguous | 9 |
| N/A | 0 |
| **Total** | **189** |

- **Pass rate** = 108 / (189 − 0) = **57.1%**
- **Blocking count (mandatory Fails)** = **21**
- **Verdict: BLOCKING**

Rationale: 21 mandatory requirements are unaddressed or below binding with no declaration, including pre-qualification gates (turnover, insolvency declaration, ≥2 deployments), SBOM, RTM, PAS 1192 / BS EN ISO 19650-2, contour interval, flight/sensor/GCP reports, AI Data Readiness Gate, MLOps cadence, OT asset widgets, OT asset LOD-350 visualization, asset registry/federation framework, RTO/RPO/24x7, ≥3 case studies (only 1 evidenced), and 225-acre utility-scanning area.

---

## 2. Blocking Issues (mandatory Fails only)

| G-ID | Requirement (short) | Binding value | Proposal position | Why blocking |
|---|---|---|---|---|
| G-006 | Vol 6 ≥3 case studies | ≥3 | Only 1 evidenced (RGIA Hyderabad); 2nd/3rd "to be confirmed" | Below binding + placeholder on mandatory |
| G-011 | Pre-qual ≥2 comparable deployments | ≥2 | Only 1 evidenced | Below binding on disqualifying gate |
| G-014 | Pre-qual turnover ≥ INR [X] crore | shall satisfy | "Not specified in selected source; to be confirmed" | Not addressed on mandatory pre-qual gate |
| G-015 | No pending insolvency/legal disputes | shall satisfy | "To be confirmed from bidder input" | Placeholder on mandatory declaration |
| G-019 | SBOM for all 3rd-party components | shall provide | Not addressed | Missing mandatory deliverable |
| G-037 | PAS 1192-2:2013 + BS EN ISO 19650-2:2019 | shall comply | Not addressed | Required standards not cited |
| G-039 | Requirements Traceability Matrix | shall provide | No RTM included (consolidated narrative only) | Mandatory submission artifact absent |
| G-048 | Contour dataset interval =10 cm | =10 cm | Not mentioned | Binding numeric not addressed |
| G-050 | Flight report, sensor calibration cert, GCP survey report | shall deliver | Not addressed | Mandatory survey deliverables missing |
| G-103 | AI Data Readiness Gate (≥12mo history, readiness report) | shall | Not addressed | Material to M5 acceptance; absent |
| G-105 | AI MLOps (monthly drift, quarterly retrain, 90-day KPI window) | shall | Not addressed | Mandatory governance cadence absent |
| G-126 | OT/IT asset widgets (per-equipment KPI widgets) | shall | Not addressed | Mandatory DT capability absent |
| G-128 | IT asset visualization cap =3000 units | =3000 | Not addressed | Binding numeric not addressed |
| G-130 | OT asset visualization at LOD 350 | shall | Not addressed | Mandatory DT capability absent |
| G-131 | Asset registry & modeling (CLG, CAI, taxonomy, ontology) | shall | Not addressed | Mandatory framework absent |
| G-132 | Asset federation (IT/SAP/ArcGIS/RMS/VMS) | shall | Not addressed | Mandatory federation absent |
| G-168 | RTO ≤4 hours | ≤4h | Not addressed | Binding NFR not addressed |
| G-169 | RPO ≤24 hours | ≤24h | Not addressed | Binding NFR not addressed |
| G-170 | Service & support =24x7 | =24x7 | Not addressed | Binding NFR not addressed |
| G-171 | Min case studies ≥3 | ≥3 | 1 evidenced | Below binding (same root as G-006) |
| G-175 | Underground utility scanning area =225 acres | =225 acres | Not mentioned | Binding scope numeric absent |

---

## 3. Numeric Parity Sub-Table (64 numeric rows)

| G-ID | Parameter | Binding | Proposal value | Delta/ratio | Verdict |
|---|---|---|---|---|---|
| G-009 | Proposal validity (days) | ≥180 | 180 | 0 | Pass |
| G-018 | Eval weight Technical (%) | =30 | not restated (framework acknowledged DC-01) | n/a | Pass |
| G-018 | Eval weight Experience (%) | =25 | not restated | n/a | Pass |
| G-018 | Eval weight AI (%) | =20 | not restated | n/a | Pass |
| G-018 | Eval weight Commercial (%) | =15 | not restated | n/a | Pass |
| G-018 | Eval weight Implementation (%) | =10 | not restated | n/a | Pass |
| G-041 | LiDAR point density boundary (pts/m²) | ≥20 | 20 | 0 | Pass |
| G-042 | LiDAR point density buffer (pts/m²) | ≥8 | 8 | 0 | Pass |
| G-043 | Horizontal RMSE (cm) | ≤5 | 5 | 0 | Pass |
| G-044 | Vertical RMSE (cm) | ≤3 | 3 | 0 | Pass |
| G-045 | Orthophoto GSD (cm) | ≤5 | 5 | 0 | Pass |
| G-047 | DTM/DSM grid resolution (cm) | =10 | 10 | 0 | Pass |
| G-048 | Contour interval (cm) | =10 | not addressed | — | Fail |
| G-059 | Indoor positional RMSE (cm) | ≤5 | 5 | 0 | Pass |
| G-079 | API backwards compat (major versions) | ≥2 | 2 | 0 | Pass |
| G-083 | TLS version | =1.3 | 1.3 | 0 | Pass |
| G-084 | Encryption at rest | =AES-256 | AES-256 | 0 | Pass |
| G-085 | Activity audit log retention (years) | ≥2 | 2 | 0 | Pass |
| G-088 | Mandatory AI agents (count) | =8 | 8 | 0 | Pass |
| G-107 | Mech/HVAC p/r/horizon/latency | 82/78/72h/30s | 82/78/72h/30s | 0 | Pass |
| G-108 | Electrical p/r/horizon/latency | 80/75/48h/30s | 80/75/48h/30s | 0 | Pass |
| G-109 | Passenger Flow p/r/horizon/latency | 85/80/45min/15s | 85/80/45min/15s | 0 | Pass |
| G-110 | Structural p/r/horizon/latency | 90/85/7d/60s | 90/85/7d/60s | 0 | Pass |
| G-111 | Fire Safety p/r/horizon/latency | 95/95/rt/5s | 95/95/rt/5s | 0 | Pass |
| G-112 | Energy Mgmt p/r/horizon/latency | 80/75/24h/60s | 80/75/24h/60s | 0 | Pass |
| G-113 | Security p/r/horizon/latency | 88/82/15min/10s | 88/82/rt-15min/10s | 0 | Pass |
| G-114 | Aggregate alert accuracy p/r | 80/75 | 80/75 | 0 | Pass |
| G-128 | IT asset visualization cap (units) | =3000 | not addressed | — | Fail |
| G-137 | Phase duration (months/phase) | ~3 | ~3 | 0 | Pass |
| G-138 | Payment milestones M1–M6 (%) | 15/10/20/25/20/10 | 15/10/20/25/20/10 | 0 | Pass |
| G-139 | Deliverable review period (days) | =14 | 14 | 0 | Pass |
| G-150 | Warranty period (months) | ≥12 | 12 | 0 | Pass |
| G-153 | Platform design life (years) | ≥15 | 15 | 0 | Pass |
| G-155 | Historical BMS retention (years) | ≥5 | 5 | 0 | Pass |
| G-156 | AI audit log retention (years) | ≥5 | 5 | 0 | Pass |
| G-157 | AI model rollback (hours) | ≤4 | 4 | 0 | Pass |
| G-158 | Platform uptime (%) | ≥99.5 | 99.5 | 0 | Pass |
| G-159 | Real-time latency (s) | ≤5 | 5 | 0 | Pass |
| G-160 | BIM LOD compliance (%) | =100 | 100 | 0 | Pass |
| G-161 | Integration coverage (%) | =100 | 100 | 0 | Pass |
| G-162 | Incident response critical (min) | ≤10 | 10 | 0 | Pass |
| G-163 | Breach notification (hours) | ≤12 | 12 | 0 | Pass |
| G-164 | Material-default threshold (breaches/qtr) | ≥3 | 3 | 0 | Pass |
| G-165 | Transition support (months) | ≥6 | 6 | 0 | Pass |
| G-166 | IoT machine-room pumps (units) | =40 | 40 | 0 | Pass |
| G-167 | T1 roof sensors (units) | =12 | 12 | 0 | Pass |
| G-168 | RTO (hours) | ≤4 | not addressed | — | Fail |
| G-169 | RPO (hours) | ≤24 | not addressed | — | Fail |
| G-170 | Service & support coverage | =24x7 | not addressed | — | Fail |
| G-171 | Min case studies (count) | ≥3 | 1 | −2 | Fail |
| G-172 | Geospatial horizontal RMSE (cm) | ≤5 | 5 | 0 | Pass |
| G-173 | Geospatial vertical RMSE (cm) | ≤3 | 3 | 0 | Pass |
| G-174 | Airborne LiDAR total area (sq km) | ~200 | 200 | 0 | Pass |
| G-175 | Underground utility scanning area (acres) | =225 | not addressed | — | Fail |
| G-176 | Airport campus survey area (acres) | ~5000 | not locatable | — | Ambiguous |
| G-177 | T1 BIM total area (sq m) | ~213,396 | not locatable | — | Ambiguous |
| G-178 | T2 BIM total area (sq m) | ~62,519 | not locatable | — | Ambiguous |
| G-179 | T3 BIM total area (sq m) | ~588,158 | not locatable | — | Ambiguous |
| G-180 | T3 HVAC points | =54,000 | ~54,000 | 0 | Pass |
| G-181 | T3 FDAS points | =65,000 | ~65,000 | 0 | Pass |
| G-182 | T1 HVAC points | =20,000 | "tens of thousands" (imprecise) | ~? | Partial |
| G-183 | T1 FDAS points | =17,400 | not locatable | — | Ambiguous |
| G-184 | MRSS points | =60,000 | "tens of thousands" (imprecise) | ~? | Partial |
| G-185 | T3 ECMS tags | =66,000 | ~66,000 | 0 | Pass |
| G-186 | T1 ECMS tags | =20,000 | not locatable | — | Ambiguous |
| G-187 | T2 FDAS points | =5,000 | not locatable | — | Ambiguous |
| G-188 | T3 BHS points | =1,300 | not locatable | — | Ambiguous |
| G-189 | OT systems in PE_OT list (count) | =19 | 19 | 0 | Pass |

Numeric-row tally within parity table: Pass 47 | Partial 2 | Fail 7 | Ambiguous 8 (rows = 64; G-018 counted as 5 rows all Pass).

---

## 4. Non-Pass Per-Requirement List (Partial / Fail / Ambiguous only — Pass rows skipped)

### Fail (21)

| G-ID | Note |
|---|---|
| G-006 | Vol 6: only 1 of ≥3 case studies evidenced; 2nd/3rd "to be confirmed" placeholder. |
| G-011 | Pre-qual ≥2 deployments: only 1 evidenced (RGIA). |
| G-014 | Pre-qual turnover threshold not addressed ("to be confirmed from bidder input"). |
| G-015 | No-pending-insolvency declaration not addressed ("to be confirmed"). |
| G-019 | SBOM for 3rd-party components not mentioned anywhere. |
| G-037 | PAS 1192-2:2013 and BS EN ISO 19650-2:2019 not cited. |
| G-039 | No Requirements Traceability Matrix provided (consolidated narrative only). |
| G-048 | 10 cm contour interval not mentioned. |
| G-050 | Flight report / sensor calibration certificate / GCP survey report not addressed. |
| G-103 | AI Data Readiness Gate (≥12mo history, tag-to-asset mapping, readiness report) absent. |
| G-105 | AI MLOps cadence (monthly drift, quarterly retrain, 90-day KPI window, quarterly report) absent. |
| G-126 | Per-equipment OT/IT asset widgets not addressed. |
| G-128 | IT asset visualization cap of 3000 units not addressed. |
| G-130 | OT asset visualization at LOD 350 (with listed equipment types) not addressed. |
| G-131 | Asset registry & modeling (CLG, CAI, taxonomy, ontology, sync framework) not addressed. |
| G-132 | Asset federation (IT/SAP/ArcGIS/RMS/VMS live video) not addressed. |
| G-168 | RTO ≤4h not addressed. |
| G-169 | RPO ≤24h not addressed. |
| G-170 | 24x7 service & support coverage not stated. |
| G-171 | Min case studies ≥3: only 1 evidenced (numeric restatement of G-006). |
| G-175 | 225-acre underground utility scanning area not mentioned. |

### Partial (51)

| G-ID | Note |
|---|---|
| G-001 | Vol 1 Exec Summary present (§2) but ≤10-page limit not declared; consolidated doc, not 7-volume. |
| G-005 | Vol 5 Commercial: INR-ex-GST/structure committed but pricing is placeholder ("to be provided"). |
| G-007 | Vol 7 Appendices: CVs "to be confirmed", ISO certs "to be attached"; subcontractor declarations absent. |
| G-010 | Pre-qual ≥5y experience: claimed via APOC role but "formal write-up to be confirmed". |
| G-022 | D-03 listed but ISO 19115 metadata conformance not cited. |
| G-035 | "IFC-compliant" stated but IFC 4.0 / ISO 16739 not specified. |
| G-038 | BEP addressed via D-01; AIR compliance not explicitly stated (BEP/AIR "to be issued by DIAL"). |
| G-049 | 3D mesh mentioned; OBJ/FBX format and 10 cm contours not stated. |
| G-051 | GIS overlay formats (SHP/GeoJSON/KML/IFC/CAD) mentioned; ESRI ArcGIS / Autodesk raw-data compatibility not explicit. |
| G-052 | Landside coverage mentioned generically; 225 acres, DEM, 3×3 m spot levels, external building mapping not stated. |
| G-053 | Underground utility: only GPR mentioned; DGPS, GNSS, 12D model missing (1 of 4 methods). |
| G-054 | Multi-department layering mentioned; 10-layer landside GIS catalogue not enumerated. |
| G-056 | Airside GIS layers (AGL, PAPI, DVOR, NAVAIDs, ancillary buildings) not enumerated. |
| G-061 | LOD 350/200 bands mentioned; full per-asset-category LOD table (Structural 300, HVAC 350, etc.) not given. |
| G-062 | T1 BIM mentioned; specific floor areas (Basement 17085, Apron 77581, etc.) not stated. |
| G-063 | T2 BIM mentioned; specific areas (Departure 27028, etc.) not stated. |
| G-064 | T3 BIM mentioned; specific areas (Departure 159126, etc.) not stated. |
| G-065 | References BRD LOD schedule but Appendix A flagged "to be completed by DIAL" — dependency declared. |
| G-068 | Federated BIM mentioned; clash detection, CDE, version control, granular RBAC not explicitly detailed. |
| G-070 | Land & Space Management module not detailed (demised/additional demised/carved-out classification, allotment repository, CLM integration absent). |
| G-074 | Environmental monitoring mentioned generally; Shahabad MdPur, NMT funnel areas, Nursery CAQM station not named. |
| G-080 | REST/GraphQL/WebSocket versioned; OpenAPI 3.0 not cited. |
| G-081 | 5 default roles listed; register's 10 additional roles (AOCC, P&E, Airside Ops, etc.) not listed. |
| G-086 | IEC 62443, segmentation, pen-test, SIEM, risk assessment, DPDP Act covered; privileged access management not mentioned. |
| G-091 | Fire Safety agent listed with ≤5s latency; edge inference and "advisory only, never suppresses FACP" not stated. |
| G-095 | Structural Integrity agent listed (mandatory=No) but SHM-sensor procurement dependency / 6–12mo baseline condition not addressed. |
| G-096 | Security agent listed; CISF-approval dependency and privacy-preserving/role-scoped read-only framing not stated. |
| G-097 | NL query mentioned for GIS data only; dedicated platform-data NL agent (assets/telemetry/CMMS/O&M, citations, role filtering) not presented as a distinct agent. |
| G-098 | Plain-language explanation + % confidence stated; SHAP/LIME/attention visualisation not mentioned. |
| G-104 | Orchestration framework described; TimescaleDB historian, shared feature store, MLflow registry, CMMS work-order connector not named. |
| G-106 | M5 agent-operational gate mentioned; rolling 90-day per-agent acceptance window and wave-gate logic not stated. |
| G-116 | T2 OT integration declared contingent on DIAL/OEM deployment ("doesn't exist"/"not present") — conditional. |
| G-120 | Many OneAPOC feeds listed (AODB/UTAM/ADS-B/ARC/RMS/Kloudspot/XOVIS/PTM/ITOM/SAP/VMS); SBD, FIDS, AFTN, check-in/boarding/baggage scanners not named. |
| G-121 | Ops DT Airside ops (GSE positions, flight-position chain, turnaround TOBT/EIBT/POBT/PRBT/PIBT, NOTAM banner) not detailed. |
| G-122 | Ops DT Terminal ops (touchpoint KPIs, queue mgmt, crowd heatmaps, dwell/journey time, retail performance, playback) not detailed. |
| G-123 | Ops DT Curbside (vehicle classification, curb occupancy RAG, dwell, trolley alerts, facility status) not detailed. |
| G-124 | Ops DT Security (reverse-entry, unattended baggage, smart buggy/trolley, SAC washroom) referenced only at use-case level via ABR. |
| G-125 | Airport/Terminal/Airside summary KPI roll-up and RBAC-persona curation not detailed. |
| G-127 | Web 3D viewer addressed; desktop GPU thick-client and Chrome/Safari browser specificity not stated. |
| G-129 | Indoor/outdoor nav mentioned; multi-level airport→terminal→zone→floor→system→asset with shortcuts not detailed. |
| G-133 | Simulation/decision-engine addressed but declared conditional on joint-scoping workshops (not a fixed commitment). |
| G-134 | SPG simulation use cases (10 commercial / 8 operational / 5 engineering) addressed at conceptual level only (mandatory=No). |
| G-135 | ABR departmental requirements (P&E, S&V, Commercial, Operations) referenced but not built out to functional spec. |
| G-140 | End-to-end delivery responsibility implied but not stated as explicit contractual commitment per BRD §9.7. |
| G-141 | Integration & interoperability responsibility implied; BRD §9.8 "any integration failure is vendor responsibility" not explicitly accepted. |
| G-146 | Regulatory approvals (BCAS/AAI) mentioned; indemnity against non-compliance not explicit. |
| G-148 | DIAL reserved rights (accept/reject/negotiate/cancel/split) not explicitly acknowledged (mandatory=No). |
| G-149 | DIAL exclusive IP ownership stated; SBOM / 3rd-party licence identification not addressed. |
| G-152 | Modular cloud-native + 15-year lifecycle stated; HA, DR, and vendor-independence continuity rights not detailed. |
| G-182 | T1 HVAC: "tens of thousands" — imprecise vs binding 20,000. |
| G-184 | MRSS: "tens of thousands" — imprecise vs binding 60,000. |

### Ambiguous (9)

| G-ID | Note |
|---|---|
| G-008 | Electronic portal submission by deadline not addressed; consolidated draft format makes submission mechanism unclear. |
| G-176 | Airport campus survey area ~5000 acres not locatable in proposal (only 200 sq km total stated). |
| G-177 | T1 BIM total area ~213,396 sq m not locatable. |
| G-178 | T2 BIM total area ~62,519 sq m not locatable. |
| G-179 | T3 BIM total area ~588,158 sq m not locatable. |
| G-183 | T1 FDAS 17,400 pts not locatable. |
| G-186 | T1 ECMS 20,000 tags not locatable. |
| G-187 | T2 FDAS 5,000 pts not locatable. |
| G-188 | T3 BHS 1,300 pts not locatable. |

---

**End of score file.**