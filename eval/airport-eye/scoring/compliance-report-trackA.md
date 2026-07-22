# Compliance Validation Report — Track A

**Target artefact:** `eval/airport-eye/trackA/proposal-trackA.md`
**Role:** Objective scorer (controlled eval). Rigorous, unbiased — not lenient.
**Authoritative requirements sources (binding priority order):**
1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` (CR/BRD v1.5, issued 05-June-2026) — binding
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` (ABR)
3. `PE_OT System_09.06.pptx.md` (PE_OT)
4. `Airport_Eye_RFP_v5.docx.md` (base RFP)
5. `AirportEye_Requirements_Register_v5.xlsx.md` / `Final requirements.xlsx.md`

**Excluded by protocol:** `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`, `AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md` (reserved human baseline), and `eval/airport-eye/trackB/` (other track) were not read.

**Numeric inventory:** see `compliance-report-trackA-numeric-inventory.md`.

---

## BLOCKING ISSUES

**BLOCKING: 7 mandatory requirements not met.**

| # | Blocking issue | Source requirement | Severity |
|---|---|---|---|
| B-1 | **Commercial pricing rate card not completed.** The 8-part INR rate card (BRD §6 / RFP §10 / Volume 5) is explicitly deferred. A submission without itemised pricing fails the mandatory commercial volume. | BRD §6 Tables 1–8; RFP §9.3 Volume 5; RFP §10 | Mandatory |
| B-2 | **Phase-1 deliverables dropped: 10 cm contour dataset, 3D mesh model, ISO 19115 accuracy/metadata report.** Neither the technical narrative (§4.1) nor the deliverables table (D-02) commits to producing these BRD §3.1.9 deliverables. Undeclared in the deviation register. | BRD §3.1.1 / §3.1.9 D-04, D-05, D-07 | Mandatory |
| B-3 | **Land and Space Management (Phase 3) not addressed.** BRD §3.3.1 is a mandatory scope block (digital footprint of land/spaces, licensee/contract attributes, multi-dimensional queries, Master Plan/Revenue Map overlay, land classification demised/additional/excluded/carved-out/MCD/DCB, CLM integration). The proposal's Phase 3 section (§4.3) omits it entirely. Undeclared. | BRD §3.3.1 | Mandatory |
| B-4 | **Environmental Monitoring (Phase 3) not addressed.** BRD §3.3.5 requires digital footprint at Shahabad MdPur (IMD, STP, ISWMC), Noise Monitoring Terminals in funnel areas, and Nursery CAQM Station. Not mentioned anywhere in the proposal. Undeclared. | BRD §3.3.5 | Mandatory |
| B-5 | **Landside spot levels at 3×3 m intervals not addressed.** BRD §3.1.2 requires DTM/DSM/DEM/contours/spot levels at 3×3 m intervals and the full GIS topographic layer set. Not in the proposal. Undeclared. | BRD §3.1.2 | Mandatory |
| B-6 | **Pre-qualification: comparable deployments.** RFP Appendix E requires at least 2 comparable deployments; Volume 6 requires a minimum of 3 case studies. The proposal evidences only 1 (RGIA Hyderabad) and marks the rest "to be confirmed." | RFP Appendix E; RFP §9.3 Volume 6 | Mandatory (pre-qualification gate) |
| B-7 | **Pre-qualification certifications not attached.** ISO 9001:2015 and ISO/IEC 27001:2013 current certificates are required and are only "to be attached." | RFP Appendix E | Mandatory (pre-qualification gate) |

**Pre-flight verdict: BLOCKING — not ready for assembly.** The proposal is a strong draft that achieves full numeric parity on the BRD's KPIs and all seven itemised AI-agent performance standards, but it cannot be assembled into a compliant submission until the seven blocking items above are resolved.

---

## Summary Counts

| Verdict | Numeric | Categorical | Total |
|---|---|---|---|
| Pass | 61 | 20 | 81 |
| Partial | 0 | 14 | 14 |
| Fail | 5 | 5 | 10 |
| Ambiguous | 2 | 1 | 3 |
| **Total** | **68** | **40** | **108** |

**Mandatory failures (blocking):** 7 distinct blocking issues (B-1 to B-7), drawn from the 10 Fail verdicts.
**Declared deviations / clarifications:** DC-01 to DC-07 (Section 14). One numeric gap is declared (DC-03, Water & Drainage agent target — source-side gap). The Phase-1 deliverable omissions and the Phase-3 Land/Space and Environmental omissions are **not** declared and are therefore undeclared shortfalls.

---

## Deviation-Register Completeness Audit

| Shortfall / gap | In proposal's deviation register (§14)? | Finding |
|---|---|---|
| Water & Drainage agent — no BRD performance target | Yes — DC-03 | Declared; mitigation (platform baseline) proposed pending DIAL confirmation. Acceptable. |
| Warranty period — BRD silent, RFP 12 months | Yes — DC-04 | Declared; adopts RFP value. Acceptable. |
| Commercial pricing — deferred | Partly — DC-06 (GST only); §12 / §13 state deferral | Deferral is acknowledged, but the rate card is a mandatory deliverable, not a deviation. Treated as Fail (B-1) until filled. |
| 10 cm contour dataset — omitted | No | **Undeclared deviation** — Fail (B-2). |
| 3D mesh model deliverable — omitted | No | **Undeclared deviation** — Fail (B-2). |
| ISO 19115 metadata / accuracy report (BRD D-07) — omitted | No | **Undeclared deviation** — Fail (B-2). |
| Land & Space Management (BRD §3.3.1) — omitted | No | **Undeclared deviation** — Fail (B-3). |
| Environmental Monitoring Shahabad MdPur (BRD §3.3.5) — omitted | No | **Undeclared deviation** — Fail (B-4). |
| 3×3 m spot levels + landside GIS layer catalogue (BRD §3.1.2) — omitted | No | **Undeclared deviation** — Fail (B-5). |
| Airside NAVAID layer catalogue (BRD §3.1.3) — not enumerated | No | Undeclared; counted as Partial (C-21). |
| "No Black Box" interpretability (SHAP/LIME/attention) — not addressed | No | Undeclared; counted as Partial (C-23). |
| Case studies (min 2–3) — only 1 evidenced | Acknowledged in §15/§16 | Gap is acknowledged but a pre-qualification failure until evidenced (B-6). |

---

## Carve-Out / Over-Claim Detection (Step 5)

The proposal does **not** use a "Compliant/Meets/Exceeds" status-word table for numeric commitments; it states values directly. No parenthetical weakening phrases ("subject to", "measured at boundary", "where feasible", etc.) were found attached to the numeric KPI or AI-agent commitments. The following deferral-style phrasing was found and is recorded (none weakens a numeric parity commitment):

- §4.7 simulation engine: "detailed scoping … treated as an item for joint scoping workshops" — a scope-deferral on the ABR/SPG capability, not a numeric carve-out. Counted under C-35 (Partial).
- §11 Water & Drainage agent: "pending DIAL's confirmation" — declared (DC-03). Not a hidden carve-out.
- §7 governance cadence, §8 hosting sizing, §15 case studies, §9 ISO certs: "to be confirmed" — deferrals on evidence/process, not on binding numeric specs.

**Over-claim check:** No "100% coverage" or per-agent "all at/above threshold" over-claims were found where only a subset is substantiated. The agent table substantiates all seven itemised agents at full parity. The eighth (Water & Drainage) is explicitly flagged as a source gap rather than claimed as compliant.

---

## Categorical Requirements Validation

| ID | Requirement (source) | Verdict | Evidence / gap |
|---|---|---|---|
| C-01 | Cover letter (RFP Volume structure) | Pass | §1 present, references CA dated 30 Sep 2019 and BRD v1.5. |
| C-02 | Executive summary (RFP Vol 1, max 10 pp) | Pass | §2 present; concise. Page count within 10 pp for this section. |
| C-03 | Understanding of requirements | Pass | §3 addresses BRD vision, six objectives, PE_OT estate, ABR use cases, procurement-mechanism conflict. |
| C-04 | Proposed solution across 5 phases | Pass | §4 maps all five BRD phases. |
| C-05 | Scope coverage & deliverables D-01–D-15 | Partial | D-01–D-15 listed, but D-02 omits contours, 3D mesh, ISO 19115 metadata (see B-2). |
| C-06 | Implementation methodology & 15-month plan | Pass | §6 phase table matches BRD §4.1; terminal-prioritised rollout consistent with register. |
| C-07 | Governance & team structure | Partial | RACI reflected; but named personnel/CVs "to be confirmed" (RFP Vol 7 requires CVs). |
| C-08 | Integration, data, technical approach | Pass | §8 grounded in PE_OT 19 systems; protocols match BRD §3.4.2; DTDL; 5-yr archive; API versioning. |
| C-09 | Security, privacy, compliance, QA | Pass | §9 covers IEC 62443, segmentation, pen-test, SOC/SIEM, MFA, RBAC 5 roles, SSO, TLS1.3/AES-256, 2-yr audit, India-only sovereignty, 12-hr breach notice. |
| C-10 | Testing, acceptance, handover | Pass | §10 covers 14-day review, UAT M4, AI benchmarks M5, independent audit, D-12 pen-test, D-15 90-day PIR. |
| C-11 | Support, maintenance, SLA | Pass | §11 KPI table matches BRD; 12-mo warranty (RFP), AMC, penalty framework, 6-mo transition. |
| C-12 | Assumptions, dependencies, exclusions | Pass | §12 comprehensive; external dependencies (VDGS/MRSS Mar-2027) flagged. |
| C-13 | Commercial / pricing (Vol 5) | Fail | §13 defers all pricing. Rate card unfilled (B-1). |
| C-14 | Deviations, clarifications register | Pass | §14 DC-01–DC-07 present; covers procurement-mechanism conflict, ABR timing, Water agent, warranty, BG, GST, appendices. |
| C-15 | Relevant experience & case studies (Vol 6) | Fail | Only RGIA Hyderabad evidenced; 2nd/3rd case studies "to be confirmed" (B-6). |
| C-16 | Appendices / mandatory forms / compliance tables | Partial | PE_OT inventory populated (App D); pre-qualification checklist present but incomplete; ISO certs not attached. |
| C-17 | Land & Space Management (BRD §3.3.1) | Fail | Not addressed anywhere in proposal (B-3). |
| C-18 | Environmental Monitoring — Shahabad MdPur / NMT / CAQM (BRD §3.3.5) | Fail | Not addressed (B-4). |
| C-19 | Landside GPR / DGPS / GNSS / 12D underground utility model (BRD §3.1.2) | Partial | GPR mentioned only as a regulatory dependency (§5, §12); not committed as a landside deliverable. |
| C-20 | Landside GIS topographic layers — 10 layers (BRD §3.1.2) | Partial | Layers not enumerated; "land use, parcels, road networks, street view, zoning, topography, wetlands, demographics, land cover, imagery, basemap" absent. |
| C-21 | Airside NAVAID GIS layers — AGL/PAPI/DVOR/Signage/RVR/MSSR/AMSR (BRD §3.1.3) | Partial | Airside extent mentioned; NAVAID layer catalogue not enumerated. |
| C-22 | Federated BIM platform — clash detection, CDE, version control (BRD §3.2.3) | Partial | ISO 19650 and CAFM/CMMS import mentioned; automated clash detection and CDE not explicitly committed. |
| C-23 | "No Black Box" — SHAP/LIME/attention interpretability (RFP §6.4) | Partial | Explainability + confidence score committed (§9); specific interpretability techniques (SHAP/LIME/attention) not named. |
| C-24 | Seven-volume submission structure (RFP §9.3) | Partial | Single consolidated draft with a mapping table to Vols 1–7; physical volumes not produced. Acceptable for a draft; must be restructured for final submission. |
| C-25 | Pre-qualification: min 5 years experience (RFP App. E) | Partial | Claimed via incumbent APOC role; formal write-up "to be confirmed." |
| C-26 | Pre-qualification: min 2 comparable deployments (RFP App. E) | Fail | 1 of 2 evidenced (B-6). |
| C-27 | Pre-qualification: ISO 9001:2015 cert (RFP App. E) | Partial | Evidenced from collateral; current cert "to be attached" (B-7). |
| C-28 | Pre-qualification: ISO/IEC 27001:2013 cert (RFP App. E) | Partial | Evidenced from collateral; current cert "to be attached" (B-7). |
| C-29 | Pre-qualification: turnover threshold (RFP App. E) | Ambiguous | RFP leaves value as INR [X] (blank). No comparable threshold to test against. Assumed compliant pending DIAL issuing the figure. |
| C-30 | Pre-qualification: no insolvency / adverse legal (RFP App. E) | Partial | "To be confirmed from bidder input." |
| C-31 | ABR — P&E borewell recharge & storm-water IoT | Pass | §3 and §4.3 address. |
| C-32 | ABR — S&V reverse-entry, unattended baggage, behaviour analytics, predictive security, asset mapping | Pass | §3 addresses all five. |
| C-33 | ABR — Commercial Aero satellite/GIS space-allocation analytics | Pass | §3 addresses. |
| C-34 | ABR — Operations low-vis navigation, IT monitoring (DigiYatra/E-Gates/CUSS/CUPPS), overstaying passengers | Pass | §3 addresses. |
| C-35 | ABR — SPG simulation / what-if decision engine | Partial | §4.7 commits to architecture (twin + control UI + decision engine + viz UI) but defers detailed scoping to joint workshops. |
| C-36 | Outdoor 3D GIS Platform (BRD §3.4.6) | Pass | §4.6 covers viewer, multi-department layering (SHP/GeoJSON/KML/IFC/CAD), scenario viz, redlining/version control, sharing, NL query. |
| C-37 | Digital Twin viewer (BRD §3.4.1) | Pass | §4.4 covers simultaneous display, indoor/outdoor nav, BMS overlay, dashboards, AR/VR, mobile offline. |
| C-38 | BMS/IoT protocol suite (BRD §3.4.2) | Pass | §4.4/§8 list BACnet/IP, BACnet MSTP, Modbus TCP/RTU, MQTT v3.1.1/v5.0, SNMP, OPC-UA, REST, proprietary. |
| C-39 | APOC/CCC integration — REST/GraphQL/WebSocket (BRD §3.4.3) | Pass | §4.4/§8 address. |
| C-40 | Cybersecurity — IEC 62443, segmentation, pen-test, SOC/SIEM (BRD §3.4.5) | Pass | §9 addresses all four. |

---

## Numeric Parity — Highlights

Full parity (1.0×) is achieved on:
- All 7 platform KPIs (uptime ≥99.5%, latency ≤5 s, LOD 100%, alert precision ≥80%/recall ≥75%, H RMSE ≤5 cm, V RMSE ≤3 cm, critical response ≤10 min, integration 100% within 3 mo).
- All 7 itemised AI-agent performance standards (28 of 28 precision/recall/horizon/latency cells match the BRD §3.5.4 table exactly).
- 8 mandatory agents itemised; model rollback ≤4 h; 5-yr AI audit log; 5-yr BMS archive; 2-yr activity log; 5 user roles; 2-version API compatibility; 12-hr breach notice; India-only sovereignty; 15-yr lifecycle; 6-mo transition; 180-day validity; 12-mo warranty; 40 pump sensors; 12 roof sensors.
- **Precedence handled correctly:** the proposal adopts the stricter BRD ≤10 min critical-incident response over the RFP's ≤1 hour.

Numeric failures are confined to dropped Phase-1 deliverables (contours, mesh, ISO 19115 metadata, 3×3 m spot levels) and the unfilled commercial rate card — see blocking issues B-1, B-2, B-5.

---

## "Addressed Within Narrative" Check (Step 6)

- Land & Space Management: **not found** anywhere in the narrative — Fail (B-3).
- Environmental Monitoring (Shahabad MdPur/NMT/CAQM): **not found** — Fail (B-4).
- 10 cm contours / 3D mesh production: **not found** in §4.1 or deliverables — Fail (B-2).
- "No Black Box" interpretability techniques: mentioned generically via "explainability + confidence score" but SHAP/LIME/attention not named — Partial (C-23).
- Airside NAVAID layers: not enumerated — Partial (C-21).

---

## Page / Word Count Assessment (Step 7)

- The only explicit page limit is RFP Volume 1 (Executive Summary, max 10 pages). The proposal's §2 Executive Summary is well under this limit.
- No other per-volume page limits are stated in the RFP/BRD.
- The draft is a single consolidated document (~5,600 words / ~360 lines), not yet split into the seven physical volumes. Volume structure is a mapping (§16) rather than a produced artefact. No page-limit breach, but the structure must be produced for final submission.

---

## Cross-Reference & Multi-Artefact Consistency (Step 8)

- Internal consistency: the KPI table (§11), AI-agent table (§11), payment-milestone table (§13), and deliverables table (§5) are internally consistent and match the BRD equivalents.
- PE_OT reconciliation: the 19-system inventory in Appendix D (§16) matches the PE_OT source slide 2 exactly (OEMs, owners, integration status, VDGS/MRSS Mar-2027 upgrade notes).
- Register reconciliation: delivery-wave months (3, 5, 8, 12+) and point counts (T3 HVAC 54,000; T3 FDAS 65,000; T3 ECMS 66,000; first 4,000 in 3 months) in §6/§8 match `AirportEye_Requirements_Register_v5.xlsx.md`.
- No internal table-to-table inconsistencies found.
- No cross-check artefact (e.g., RTM) was supplied with this proposal; three-way reconciliation was therefore not possible and is noted as reduced cross-reference capability.

---

## Adversarial Critic Pass (Step 10)

Run after the initial validation. Findings:

1. **Treated as Pass but worth re-checking:** KPI #6 (critical incident response). The proposal states ≤10 min; the RFP says ≤1 hour. Re-checked: BRD §2.3 line 212 and Appendix C line 745 both say ≤10 min. BRD is binding. Proposal is correct — Pass confirmed.
2. **Shortfall missing from deviation register:** the four dropped Phase-1 deliverables (contours, mesh, ISO 19115 metadata, 3×3 m spot levels) and the two dropped Phase-3 blocks (Land & Space, Environmental Monitoring) are not in §14. Confirmed as undeclared deviations — promoted to blocking.
3. **Status-word over-claims:** none found (proposal states values, not status words). Confirmed.
4. **Internal inconsistencies:** none found between §11 KPI table and §4 narrative. Confirmed.

No further new findings on a second pass. Loop terminated.

---

## Remediation Instructions

**Must fix (blocking — before assembly):**
1. **B-1 (Pricing):** Complete all 8 BRD §6 / RFP §10 rate-card tables in INR excl. GST, or obtain DIAL's written agreement to a phased commercial submission. Declare all pricing assumptions (survey areas, BMS point counts, user licences, cloud sizing).
2. **B-2 (Phase-1 deliverables):** Add 10 cm contour dataset, 3D mesh model (OBJ/FBX, georeferenced), and ISO 19115 accuracy-assessment/metadata report to §4.1 and to the deliverables table. Restore BRD §3.1.9 D-04/D-05/D-06/D-07 explicitly.
3. **B-3 (Land & Space):** Add a Phase-3 sub-section addressing BRD §3.3.1 in full — land/space digital footprint, licensee/contract attributes, multi-dimensional queries, Master Plan/Revenue Map/satellite overlay, land classification (demised/additional/excluded/carved-out/MCD/DCB), CLM integration.
4. **B-4 (Environmental Monitoring):** Add BRD §3.3.5 commitments — Shahabad MdPur (IMD/STP/ISWMC), Noise Monitoring Terminals in funnel areas, Nursery CAQM Station.
5. **B-5 (Landside detail):** Add 3×3 m spot-level commitment and enumerate the landside GIS topographic layer set; add GPR/DGPS/GNSS/12D underground-utility model as a landside deliverable (not only a dependency).
6. **B-6 (Case studies):** Provide at least 2 (preferably 3) comparable airport/infrastructure digital-twin case studies with client references, per RFP App. E / Volume 6.
7. **B-7 (Certifications):** Attach current ISO 9001:2015 and ISO/IEC 27001:2013 certificates; confirm turnover threshold and no-insolvency representation once DIAL issues the [X] figures.

**Should fix (non-blocking, points at risk):**
- C-21: enumerate airside NAVAID GIS layers (AGL, PAPI, DVOR, Signage, RVR, MSSR, AMSR).
- C-22: explicitly commit to automated clash detection and CDE in the federated BIM platform.
- C-23: name interpretability techniques (SHAP/LIME/attention visualisation) for the "No Black Box" requirement.
- C-35: convert the SPG simulation deferral into at least a baseline functional spec rather than only a workshop placeholder.
- C-07: attach named personnel CVs for the six key delivery roles.
- C-24: split the consolidated draft into the seven physical volumes for final submission.

---

## Pre-Flight Status

**BLOCKING — 7 mandatory requirements not met.** The proposal demonstrates strong technical compliance (full numeric parity on KPIs and AI-agent standards, correct binding-precedence handling, accurate PE_OT/register reconciliation) but is **not ready for assembly** as a compliant submission. Resolve B-1 through B-7 before the proposal assembler proceeds. Re-run this validator after remediation.