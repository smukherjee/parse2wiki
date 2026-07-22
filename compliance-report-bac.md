# BAC Underwing Analytics — Compliance Validation Report

**Procurement:** Brisbane Airport Corporation (BAC) — Underwing Analytics RFP  
**Authoritative source:** `BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md`  
**Target artefact (proposal under validation):** `BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md`  
**Cross-check artefact:** `UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`  
**Skill version:** compliance-validator (12-step process)  
**Date:** 2026-07-17

---

## Executive summary

This report tests the generic applicability of the `/compliance-validator` skill against a completely different procurement (BAC Underwing Analytics, not Airport Eye). The authoritative RFP directs all functional and non-functional requirements to Tab F of the response sheet, and the response sheet itself is the proposal artefact to be validated.

**Critical finding:** The supplied response sheet is essentially an **unfilled Excel template**. Every conformance/response cell is blank. As a result, the proposal does not currently meet the RFP's submission, insurance, content, or substantive requirements and would likely be deemed incomplete or non-conforming under §6.1 and §8 of the RFP.

| Metric | Count |
|---|---|
| Requirements / requirement groups checked | 34 |
| Pass | 0 |
| Partial | 1 |
| Ambiguous | 2 |
| Fail | 31 |
| Blocking mandatory failures | 31 |

**Pre-flight status:** **BLOCKING** — proposal is not ready for submission. All Tab F and schedule responses must be completed, insurance evidence attached, and the deviation/assumption register populated before assembly.

---

## BLOCKING issues

1. **Tab F conformance cells are entirely blank.** All 73 functional requirements, all non-functional requirements, all project-management requirements and all 30 ISRA rows have empty supplier-response columns. This violates §8 ("All Proposal requirements be completed and returned on the accompanying Excel Spreadsheet") and §6.1 (submissions checked for completion and compliance).
2. **Mandatory insurance evidence missing.** Public liability ($20M minimum), professional indemnity ($10M) and cyber security insurance ($10M) are required by §4.4 / §5.3. The response sheet's insurance table is empty and no Certificate of Currency is referenced.
3. **Submission mechanics incomplete.** The response sheet records "2026-07-10 00:00:00" but omits the RFP's closing time of **2pm AEST**, the required email recipient (`Leighton.Walker@bne.com.au`), confidentiality marking and reference-number labelling.
4. **No numeric parity evidence.** Every measurable requirement (RTO ≤4 h, support response times, 24/7/365 live data, 3-year availability history, 6-month defects liability, 20% practical-completion retention, etc.) is blank. No deviation register exists, so all are undeclared shortfalls.
5. **Cross-check artefact inconsistent with BAC context.** The solution-architecture document repeatedly references **AIA / Athens International Airport**, **"BRISBAINE"** and **EU data residency**, and contains deployment and data-sovereignty language that does not match a Brisbane/Australia procurement. If used as supporting material it must be reconciled and corrected before submission.

---

## Numeric requirements inventory + parity table

See the full inventory at `compliance-report-bac-numeric-inventory.md`.

High-level numeric parity result:

- **24 comparable numeric requirements** extracted from the RFP / Tab F.
- **0 Pass, 0 Partial, 1 Ambiguous, 23 Fail.**
- No deviation register exists; every shortfall is undeclared.

Key numeric gaps:

| ID | Parameter | Binding value | Proposal value | Verdict |
|---|---|---|---|---|
| N-PROC-02 | Proposal validity | 90 calendar days | blank | Fail |
| N-INS-01 | Public liability | ≥$20M | blank | Fail |
| N-INS-02 | Professional indemnity | ≥$10M | blank | Fail |
| N-INS-03 | Cyber insurance | ≥$10M | blank | Fail |
| N-SLA-01 | Live data availability | 24/7/365 | blank | Fail |
| N-SLA-03 | RTO | ≤4 hours | blank (cross-check claims ≤40 min, not transcribed) | Fail |
| N-SUP-01 | Severity 1 response | ≤1 hour 24×7×365 | blank | Fail |
| N-SUP-03 / N-SUP-04 | Severity 2 response | ≤4h business / ≤8h non-business | blank | Fail |
| N-PM-02 | Practical-completion retention | 20% of lump sum | blank | Fail |
| N-PM-03 | Defects liability | 6 months | blank | Fail |

The cross-check artefact (`UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`) states an RTO of ≤40 minutes and RPO of "< Near zero" (lines 584-588), which would meet or exceed the RFP's RTO ≤4 hours. However, these values are **not reflected anywhere in the response sheet**, so they cannot be treated as the supplier's binding BAC commitment.

---

## Deviation-register completeness audit

The response sheet contains **no deviation, exemption, assumption or departure register**. Sections 5.1/Annexure B of the RFP invite suppliers to submit departures with their response; the response sheet does not contain any such register.

| Shortfall category | Count | Declared in register? |
|---|---|---|
| Numeric requirements below/missing binding value | 23 | No — all undeclared |
| Categorical / content requirements not addressed | 31 groups | No — all undeclared |
| Procedural non-compliance | 4 | No — all undeclared |

Because no register exists, every gap is an **undeclared deviation** and therefore a **Fail** under Step 9 of the skill. The absence of a register itself increases compliance risk and should be flagged to evaluators.

---

## Semantic carve-out and over-claim detection

The response sheet contains no status words such as "Compliant" or "Meets" because all conformance cells are blank. Therefore, no parenthetical carve-outs ("subject to", "as available", "to be confirmed", etc.) are present in the response sheet itself.

However, the **cross-check artefact** contains language that narrows or contradicts a BAC commitment if treated as part of the proposal:

| Phrase / pattern | Location in cross-check artefact | Risk |
|---|---|---|
| "AWS EU region deployment" / "All data remains within the EU regulatory boundary" | `UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`, lines 308-313, 478, 832 | Inconsistent with BAC (Australia) data-residency expectations. |
| "If AIA selects the private-cloud-on-premises option..." | lines 143, 305-306, 525-526, 626 | References a different customer (AIA) and creates ambiguity about whether hardware/server commitments apply to BAC. |
| "Data Retention Policy to be agreed with AIA" | line 528 | BAC-specific retention policy is not finalised; same risk applies if document is reused for BAC. |
| "RTO and RPO targets aligned to AIA's business continuity requirements" | line 582 | No BAC-specific RTO/RPO targets committed. |

**Action:** If the architecture document is submitted as the optional 5-page PDF, all AIA/Athens and EU-specific references must be replaced with BAC/Brisbane/Australia equivalents, and any "to be agreed" items must be either resolved or entered in the deviation register.

---

## Per-requirement validation table

| Category | Requirement IDs / summary | Mandatory? | Evidence in response sheet | Verdict | Notes / remediation |
|---|---|---|---|---|---|
| Submission package | §6.1, §8: all requirements returned on Excel spreadsheet; optional 1 PDF ≤5 pages | Mandatory | Excel template present; all tabs present; optional PDF not evidenced | Partial | Ensure any optional PDF is ≤5 pages and labelled with Proposal Name and reference number. |
| Response due date | §4.2 closing 10 July 2026 **2pm AEST** | Mandatory | Cell shows "2026-07-10 00:00:00" | Ambiguous | Add closing time and AEST time zone; confirm receipt method. |
| Submission method | §4.5 / §6.1: email to `Leighton.Walker@bne.com.au`, marked confidential, with Proposal Name & ref no. | Mandatory | Not addressed in response sheet | Fail | Add a transmittal/cover email note. |
| Proposal validity | §4.2: 90 calendar days from closing time | Mandatory | Blank | Fail | Insert 90-day validity statement. |
| Supplier Information | Tab A items 1.1-1.10, 2.1-2.2, 3.1, 4.1-4.3, 5.1-5.3, 6.1-6.6, 7.1, 8.1 | Mandatory | All blank | Fail | Complete business details, contacts, insurance certificates, certifications, contract execution info and conflict-of-interest declaration. |
| Insurance — Public Liability | §4.4: minimum $20M | Mandatory | Blank | Fail | Attach Certificate of Currency and policy details. |
| Insurance — Professional Indemnity | §4.4: $10M | Mandatory | Blank | Fail | Attach Certificate of Currency. |
| Insurance — Cyber | §4.4: $10M | Mandatory | Blank | Fail | Attach Certificate of Currency. |
| Social Procurement | Tab B: Supply Nation, Indigenous business, business size, Modern Slavery Act | Mandatory / Expected | All blank | Fail | Complete all social-procurement fields. |
| Relevant Experience | Tab C: company background + at least 2 referees | Expected | All blank | Fail | Add company background, years of experience, locations, evidence and two referees. |
| Methodology | Tab D: 5 questions (delivery, budget/time management, risks, assumptions, exclusions) | Mandatory | All blank | Fail | Complete methodology responses. |
| Pricing | Tab E: 5-year cost breakdown | Mandatory | All blank | Fail | Complete implementation, integration, hardware, licence, support and maintenance costs plus assumptions. |
| Functional Req — Video Capture & Camera Management | FR01-FR04 (4 Must Have) | Mandatory | All conformance cells blank | Fail | Confirm camera onboarding, grouping, FOV/parking zones and geofenced operational zones. |
| Functional Req — Video Stream Management | FR05-FR08 (3 Must, 1 Should) | Mixed | All blank | Fail / Partial | Complete live ingest, buffering, frame rate/resolution and timestamping cells. |
| Functional Req — Camera Health & Diagnostics | FR09-FR12 (3 Must, 1 Could) | Mixed | All blank | Fail / Partial | Confirm availability monitoring, occlusion/glare detection, AI-accuracy alerts and health dashboard. |
| Functional Req — Aircraft Identification & Positioning | FR13-FR16 (4 Must) | Mandatory | All blank | Fail | Confirm on-block/off-block detection, AIDX identification and AODB correlation. |
| Functional Req — GSE Detection | FR17-FR19 (3 Must) | Mandatory | All blank | Fail | Confirm detection of all 10 GSE categories plus ready/arrival/departure timestamps and presence tracking. |
| Functional Req — Personnel Detection & Safety | FR20-FR23 (4 Must) | Mandatory | All blank | Fail | Confirm apron-zone personnel detection, restricted-zone entry, unsafe dwell times and PPE detection. |
| Functional Req — Turnaround Activity Detection | FR24-FR28 (5 Must) | Mandatory | All blank | Fail | Confirm detection of 14 turnaround activities, sequencing, confidence scoring, manual correction and continuous learning. |
| Functional Req — Workflow & Business Logic | FR29-FR32 (4 Must) | Mandatory | All blank | Fail | Confirm airline/movement-type workflows, aircraft-type sequences, mandatory/optional activities and dependency rules. |
| Functional Req — Schedule vs Actual | FR33-FR39 (6 Must, 1 Should) | Mixed | All blank | Fail / Partial | Confirm AODB/ingest, planned-vs-actual comparison, delay attribution, tolerances, workflow deviation, root-cause flagging and exception annotations. |
| Functional Req — Real-Time Alerts | FR40-FR44 (5 Must) | Mandatory | All blank | Fail | Confirm configurable duration, safety and confidence alerts; multi-channel delivery (dashboard, email, AIDX API); and context/severity/actions. |
| Functional Req — Dashboards & Visualizations | FR45-FR48 (3 Must, 1 Should) | Mixed | All blank | Fail / Partial | Confirm live status board, activity state, colour-coded delays, live/historical playback. |
| Functional Req — Analytics & Insights | FR49-FR53 (5 Must) | Mandatory | All blank | Fail | Confirm KPIs by airline/type/gate/provider, trend/variance analysis, AI-driven insights, ad-hoc queries and historical analysis. |
| Functional Req — Integration & Data Management | FR54-FR56 (3 Must) | Mandatory | All blank | Fail | Confirm AODB/FIDS/A-CDM (AIDX) integration, REST/event APIs and publication of actual timestamps. |
| Functional Req — Data Storage & Retention | FR57-FR59 (3 Must) | Mandatory | All blank | Fail | Confirm event/video separation, configurable retention and forensic replay. |
| Functional Req — User & Role Management | FR60-FR67 (8 Must) | Mandatory | All blank | Fail | Confirm RBAC, airline/service-provider segregation, configurable permissions, admin tools, environment separation, monitoring, alert/report/dashboard configuration and SSO plus local non-BAC accounts with password parameters. |
| Functional Req — AI Governance & Operations | FR68-FR71 (4 Must) | Mandatory | All blank | Fail | Confirm versioned AI models, accuracy tracking, airport-specific tuning and continual learning. |
| Functional Req — Future Requirements / Remote Access | FR72-FR73 (2 Must) | Mandatory | All blank | Fail | Confirm airline data integration / aerobridge pax counting and mobile/tablet remote access. |
| Non-Functional Requirements | NF01-NF48 (all Must Have) | Mandatory | All conformance cells blank | Fail | Complete ISRA attachment, data export, live-data refresh, DR strategy, 3-year availability history, RPO/RTO, implementation/test methodology, API connectors, 24×7 support tiers, training, access controls, MFA, SSO, browser support and UX. |
| Project Management Requirements | PMR-01 to PMR-10 (all Must Have) | Mandatory | All conformance cells blank | Fail | Complete expertise, phase delivery, meetings, WHS, change control, documentation/review periods, training, acceptance criteria (20% retention), defects liability (6 months) and priority response times. |
| ISRA (Information Security Risk Assessment) | ISRA 1-30 | Mandatory | Supplier Response column blank | Fail | Complete all 30 ISRA rows with responses and residual-risk ratings (high/med/low). |
| Addenda acknowledgement | §4.10: receipt of each addendum acknowledged in relevant schedule | Mandatory | Not shown | Ambiguous | If addenda were issued, add acknowledgement; otherwise state "No addenda received at time of submission." |
| MSA / contract departure register | §5.1 / Annexure B: departures to be submitted with response | Mandatory | No register present | Fail | If no departures, add a signed statement: "No departures from the attached MSA." |

---

## Cross-reference and multi-artefact consistency

1. **Response sheet vs RFP.** The response sheet reproduces the Tab F requirement catalogue accurately but provides **no supplier responses**. It does not disagree with the RFP; it simply fails to address it.
2. **Response sheet vs cross-check architecture document.** The architecture document contains technical claims (RTO ≤40 min, RPO near-zero, 99.9% availability, EU hosting, AIA references) that are **not transcribed into the response sheet**. Until they are, they cannot be evaluated as the supplier's BAC commitment.
3. **Customer attribution errors.** The architecture document refers to "AIA" (Athens International Airport) and misspelled "BRISBAINE" throughout. If submitted as supporting material, this undermines the evaluators' confidence that the proposal is BAC-specific.
4. **Data-residency mismatch.** The RFP requires Brisbane Airport operation and integration with BAC systems; the architecture document asserts EU data residency. These are materially inconsistent unless the supplier intends to operate an Australian instance and the document has not been updated.
5. **Pricing cross-reference.** The response sheet's pricing table is blank. The architecture document contains no pricing. No reconciliation is possible.

---

## Remediation roadmap

1. **Populate every blank cell** in `BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md`: Supplier Info, Social Procurement, Relevant Experience, Methodology, Pricing, Functional Req, Non-Functional Req, PM Req and ISRA.
2. **Attach evidence:** Certificates of Currency for public liability ($20M), professional indemnity ($10M) and cyber insurance ($10M); workers compensation compliance; relevant certifications.
3. **Confirm submission mechanics:** record the closing time (2pm AEST on 10 July 2026), email recipient, confidentiality marking and reference number on the transmittal.
4. **State proposal validity** as 90 calendar days from closing time.
5. **Complete numeric parity cells:** RTO ≤4h, all severity response/resolution times, 24/7/365 live data, 3-year availability history, 6-month defects liability, 20% practical-completion retention, 3-year initial term plus two 1-year extensions.
6. **Create and attach a deviation / assumption / departure register.** If any requirement cannot be met exactly as stated, record the requirement ID, binding value, proposed value, rationale, mitigation and acceptance request.
7. **Reconcile or replace the cross-check architecture document** so that all customer references are BAC/Brisbane, data-residency commitments are Australia-appropriate, and any "to be agreed" items are either resolved or entered in the deviation register.
8. **Optional PDF:** If used, ensure it is ≤5 pages, contains only supporting information, and is correctly labelled.

---

## Conclusion

The `/compliance-validator` skill runs successfully against this unrelated procurement. It identified that the BAC response sheet is an unfilled template, flagged 23 numeric parity failures, detected the absence of a deviation register, and found cross-check inconsistencies with the supporting architecture document. The proposal is **non-conforming / blocking** until all blank cells are completed, evidence attached and deviations declared.
