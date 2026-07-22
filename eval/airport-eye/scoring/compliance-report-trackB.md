# Compliance Validation Report — Track B

**Target artefact validated:** `eval/airport-eye/trackB/proposal-trackB.md`
**Scorer:** `compliance-validator` skill, full 12-step process.
**Scoring date:** 17-July-2026
**Role:** Objective scoring agent in a controlled eval. This is a measurement, not advocacy — honesty gaps are scored as Fail/Partial per the skill's rules; no credit is awarded for candour.

**Authoritative requirements sources (binding priority order):**
1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` (CR/BRD v1.5 — binding)
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` (ABR)
3. `PE_OT System_09.06.pptx.md` (PE_OT list — 19 OT systems)
4. `Airport_Eye_RFP_v5.docx.md` (base RFP)
5. `AirportEye_Requirements_Register_v5.xlsx.md`, `Final requirements.xlsx.md`

**Excluded sources (per task constraint, not read):** `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`, `AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`, and `eval/airport-eye/trackA/`.

---

## BLOCKING: 14 mandatory requirements not met

The proposal is **NOT ready for assembly**. It must not proceed to a submission-ready state until the blocking issues below are resolved.

| # | ID | Requirement (short) | Binding source | Finding |
|---|---|---|---|---|
| 1 | N-SUR-07 / R-026b | 10 cm contour datasets | BRD §3.1.1, line 236 | Not addressed anywhere in V2 Component 1; the commitment table lists DTM/DSM, GSD, RMSE, indoor accuracy, LOD — contours omitted entirely. Undeclared shortfall. |
| 2 | R-007 / N-PRE-02 | ≥2 comparable deployments (pre-qualification gate) | RFP v5 App. E, line 817 | Only RGIA (Hyderabad) evidenced (1 of 2). Pre-qualification gate not met. Proposal itself labels this conditional-Disqualifying. |
| 3 | R-020 / N-PLATFORM-01 | Minimum 15-year operational lifecycle | BRD Objective 6, line 202 | No explicit 15-year commitment anywhere in the proposal. RTM R-020 concedes "no explicit 15-year commitment evidenced." Binding BRD objective unmet. |
| 4 | R-039 | Land/space digital footprint with DIAL legal vocabulary | BRD §3.3.1, lines 345–356 | "No land/space-management module evidenced anywhere in our collateral" (proposal's own words). Mandatory BRD Phase-3 scope unmet. |
| 5 | R-040 | CLM tool integration | BRD §3.3.1, line 354 | "No named CLM integration evidence." Mandatory BRD scope unmet. |
| 6 | R-056 | IEC 62443 OT/IT cybersecurity compliance | BRD §3.4.5 / RFP v5 §4.2, line 466 | No certification or compliance evidence; roadmap + unnamed partner only. Mandatory standard not met. |
| 7 | R-059 | SOC & SIEM continuous monitoring | BRD §3.4.5 / RFP v5 §4.2, line 469 | No SOC/SIEM track record; unnamed partner only. Mandatory capability not met. |
| 8 | R-101 | 10 Commercial SPG what-if use cases | ABR §4.2 | Flagged `[GAP]` — "illustrative; phased roadmap proposed." ABR mandatory scope not built. |
| 9 | R-103 | 5 Engineering SPG what-if use cases | ABR §4.2 | Flagged `[GAP]` — "No simulation capability evidenced." ABR mandatory scope not built. |
| 10 | R-112 | Space-allocation change identification | ABR §3.3 | Flagged `[GAP]` — depends on R-039 land/space gap. ABR ask not met. |
| 11 | R-114 | Fog / low-visibility surface navigation | ABR §3.4 | Flagged `[GAP]` — "No evidence of this specific capability." ABR ask not met. |
| 12 | R-128 / N-SUB-01 | ≥3 case studies (submission minimum) | RFP v5 §9.3, line 638 | Only 1 of 3 evidenced (RGIA); 2 explicit `[Placeholder — bidder input]`. Mandatory submission minimum not met. |
| 13 | R-129 / N-SUB-02 | CVs / key personnel | RFP v5 §9.3, line 639 | Complete blank — staffing-plan skeleton only, no named personnel, CVs, or certifications. Mandatory submission content absent. |
| 14 | R-123 / N-COM-06 | 8-table commercial costing (priced) | BRD §6, Tables 1–8 | 8-table structure committed but **every table is unpriced** ("pending bidder cost-modeling input"). Commercial proposal is not evaluable. |

**Pre-flight verdict: BLOCKING — 14 mandatory requirements not met.** The proposal assembler must not proceed.

---

## Summary counts

Two complementary score sets are reported: the **numeric/quantitative inventory** (54 comparable numeric specs) and the **full categorical requirement set** (135 requirements, R-001–R-135).

### Numeric inventory (54 rows — see companion file)

| Verdict | Count |
|---|---|
| Pass | 43 |
| Partial | 4 |
| Fail | 5 |
| Ambiguous | 1 |
| N/A | 1 |
| **Total** | **54** |

### Full categorical requirement set (135 requirements)

| Verdict | Count |
|---|---|
| Pass | 91 |
| Partial | 24 |
| Fail | 12 |
| Ambiguous | 7 |
| N/A | 1 |
| **Total** | **135** |

**Blocking issues:** 14 (listed above).
**Overall pre-flight status:** **BLOCKING — not ready for assembly.**

---

## Step 1 — Compliance requirement extraction (method note)

Requirements were extracted from the binding-priority sources in order. The CR/BRD v1.5 is the strictest and most recent source and governs wherever it contradicts the base RFP (e.g., critical-incident response ≤10 min vs RFP ≤1 hour; TLS 1.3 vs register's TLS 1.2+). The ABR adds the SPG what-if simulation engine and departmental asks. The PE_OT list fixes the OT estate at 19 systems. The base RFP v5 contributes the 7-volume submission structure, pre-qualification gates (App. E), evaluation weights, and the SHAP/LIME/attention "No Black Box" technique mandate (§6.4) that is more specific than the BRD §3.5.5 general explainability language. The two requirements registers contribute the RTO 4hr / RPO 24hr NFRs and per-agent register narratives (AI-01…AI-17).

## Step 2 — Numeric inventory

Written to the companion file `compliance-report-trackB-numeric-inventory.md` (54 rows). Summary verdict counts are repeated above. Key parity findings:

- **All seven BRD §2.3 KPIs met at parity** (uptime, latency, LOD, predictive accuracy, geospatial RMSE H/V, critical incident ≤10min, integration coverage 100%/3mo). No carve-outs on the headline KPI table.
- **All eight BRD §3.5.3 agents itemised** with their §3.5.4 performance targets stated — except Water & Drainage, which has no source target (N/A).
- **Two agent performance commitments carry carve-outs** that downgrade them to Partial: Structural Integrity (delivery contingent on DIAL SHM sensor procurement + 6–12mo baseline) and Security & Perimeter (scope "subject to CISF approval before build starts").
- **One survey deliverable is silently missing:** 10 cm contours (N-SUR-07, Fail).
- **Buffer-zone density (N-SUR-02)** is "Match, pending DIAL confirmation" — a carve-out weakening a binding BRD figure → Partial.
- **15-year lifecycle (N-PLATFORM-01)** is not committed → Fail.
- **Commercial pricing (N-COM-06)** — structure present, every table unpriced → Partial (blocking for evaluation).
- **Pre-qualification gate N-PRE-02** (≥2 comparable deployments) — 1 of 2 → Fail.

## Step 3 — Categorical validation (per-requirement table, R-001–R-135)

| ID | Requirement (short) | Volume / Section | Verdict | Notes |
|---|---|---|---|---|
| R-001 | Procurement mechanism (competitive RFP vs negotiated CR) | V1 §Procurement Framing | Ambiguous | Honestly flagged, not resolved; conservative RFP v5 structure adopted. Unresolved structural ambiguity. |
| R-002 | Evaluation weights 30/25/20/15/10 | V1 §Procurement Framing | Ambiguous | Asserted operative pending R-001 resolution. |
| R-003 | 3-stage evaluation panel | V1 §Procurement Framing | Ambiguous | Same R-001 caveat. |
| R-004 | 7-volume submission structure | V1–V7 | Pass | Followed as structural default. |
| R-005 | Volume 1 page limit 10 pages | V1 | Pass | ~5 pages; within limit. |
| R-006 | ≥5 years digital twin/BIM/geospatial | V6 §Pre-Qualification | Pass | WAISL incumbent since 30-Sep-2019 CA. |
| R-007 | ≥2 comparable deployments | V6 §Pre-Qualification, §Case Studies | **Fail (blocking)** | Only RGIA evidenced (1 of 2). Pre-qualification gate not met. |
| R-008 | ISO 9001:2015 | V6 §Certifications | Pass | Held. |
| R-009 | ISO/IEC 27001:2013 | V6 §Certifications | Pass | Held. |
| R-010 | Annual turnover ≥ INR [X] crore | V6 §Pre-Qualification | Ambiguous | Source placeholder unfilled; cannot confirm. |
| R-011 | 180-day proposal validity | V5 §Proposal Validity | Pass | Committed. |
| R-012 | Uptime ≥99.5% | V1 §Headline Commitments | Pass | Match. |
| R-013 | Latency ≤5s | V1 §Headline Commitments | Pass | Match. |
| R-014 | BIM LOD compliance 100% | V1 §Headline Commitments | Pass | Match. |
| R-015 | Predictive alert ≥80%/≥75% | V1, V3 | Pass | Match. |
| R-016 | Geospatial ≤5cm/≤3cm RMSE | V1, V2 §Component 1 | Pass | Match. |
| R-017 | Critical incident ≤10 min | V1, V4 §O&M | Pass | BRD ≤10min adopted over RFP ≤1hr. |
| R-018 | Integration 100% within 3 months | V1 §Headline Commitments | Pass | Match. |
| R-019 | Six primary objectives | V2 §Proposed Solution | Pass | All six addressed. |
| R-020 | 15-year lifecycle, modular cloud-native | V2 §Component 4 | **Fail (blocking)** | No explicit 15-year commitment; RTM concedes the gap. |
| R-021 | LiDAR core ≥20 pts/m² | V2 §Component 1 | Pass | Match. |
| R-022 | Buffer 8 pts/m² | V2 §Component 1, V5 §Open Items | Partial | "Match, pending DIAL confirmation" — carve-out on a binding figure. |
| R-023 | Horizontal RMSE ≤5cm | V2 §Component 1 | Pass | Match. |
| R-024 | Vertical RMSE ≤3cm | V2 §Component 1 | Pass | Match. |
| R-025 | Orthophoto GSD ≤5cm | V2 §Component 1 | Pass | Match. |
| R-026 | DTM/DSM 10cm grid | V2 §Component 1 | Pass | Match. |
| R-027 | Indoor positional accuracy ≤5cm | V2 §Component 1 | Pass | Match. |
| R-028 | Indoor scanning density [X] pts/m² | V2 §Component 1 | Ambiguous | Unfilled `[X]` placeholder in RFP v5 §3.2.1 — no binding value. |
| R-029 | LOD 200–350, 10-category BIM | V2 §Component 1 | Pass | Match. |
| R-030 | ISO 19650 compliance | V2 §Component 1 | Partial | Committed via GEOKNO partner; no named certification evidenced. |
| R-031 | IFC 4.0 (ISO 16739) | V2 §Component 1 | Partial | Asserted as industry-standard; no specific certification. |
| R-032 | Appendix A Schedule of Buildings/Areas | V2, V5 | Ambiguous | "[To be completed by DIAL]" — DIAL-side prerequisite, not a vendor gap. |
| R-033 | Automated clash detection | V2 §Component 2 | Pass | Asserted standard federated-BIM capability. |
| R-034 | Version control / audit trail | V2 §Component 2 | Pass | Asserted standard. |
| R-035 | RBAC on BIM CDE | V2 §Component 2 | Partial | RBAC evidenced at DT viewer, not specifically at BIM CDE. |
| R-036 | API integration BIM/DT/AI | V2 §Component 2 | Pass | Two-layer architecture. |
| R-037 | Legacy CAD/DWG migration | V2 §Component 2 | Partial | Asserted as adjacent; no specific evidence. |
| R-038 | Appendix B BEP | V2, V5 | Ambiguous | "[To be completed by DIAL]" — DIAL-side prerequisite. |
| R-039 | Land/space digital footprint (DIAL legal vocabulary) | V2 §Component 3 | **Fail (blocking)** | No land/space module evidenced; mandatory BRD §3.3.1 scope. |
| R-040 | CLM integration | V2 §Component 3 | **Fail (blocking)** | No named CLM evidence; mandatory BRD §3.3.1 scope. |
| R-041 | Single platform 13+ system families | V2 §Component 3 | Pass | RGIA 40+ systems hub-and-spoke. |
| R-042 | IoT sensor inventory ingestion | V2 §Component 3 | Pass | Middleware capability; sensor counts DIAL-provided. |
| R-043 | Environmental monitoring | V2 §Component 3 | Partial | Plausible GIS extension; no named evidence of environmental-layer delivery. |
| R-044 | Modular cloud-native platform | V2 §Component 4 | Pass | Two-layer architecture. |
| R-045 | 3D GIS+BIM viewer, AR/VR, offline mobile | V2 §Component 4 | Partial | Core viewer grounded; AR/VR + offline asserted. Text is truncated/incomplete ("core 3D viewer capability is; AR/VR output and full offline-mobile responsiveness are."). |
| R-046 | BMS/IoT middleware protocol list | V2 §Component 4, §Integration | Pass | RGIA proof point; full protocol list matched. |
| R-047 | DTDL semantic data model | V2 §Component 4 | Partial | Committed; no DTDL-specific evidence. |
| R-048 | BMS point → BIM element mapping | V2 §Component 4 | Pass | Core to two-layer DT. |
| R-049 | 5-year BMS historical retention | V2 §Component 4 | Pass | Match. |
| R-050 | APOC/CCC integration REST/GraphQL/WebSocket | V2 §Component 4 | Pass | APOC Phase II adjacent precedent (hosting language excluded). |
| R-051 | MFA + RBAC 5 roles | V2 §Component 4 | Pass | Match. |
| R-052 | SSO SAML 2.0 / OAuth 2.0 | V2 §Component 4 | Pass | Standard capability. |
| R-053 | TLS 1.3 / AES-256 | V2 §Component 4 | Pass | BRD TLS 1.3 governs over register's TLS 1.2+. |
| R-054 | 2-year activity audit log | V2 §Component 4 | Pass | Match. |
| R-055 | Outdoor 3D GIS multi-department layering | V2 §Component 4 | Partial | Adjacent GEOKNO GIS capability asserted. |
| R-056 | IEC 62443 compliance | V2 §Component 5 | **Fail (blocking)** | No certification; roadmap + unnamed partner only. |
| R-057 | Network segmentation | V2 §Component 5 | Pass | Standard OT practice. |
| R-058 | Penetration testing pre-go-live | V2 §Component 5, V4 §Testing | Pass | Standard; tied to D-12. |
| R-059 | SOC/SIEM | V2 §Component 5, V7 | **Fail (blocking)** | No track record; unnamed partner only. |
| R-060 | Cybersecurity risk assessment | V2 §Component 5, V4 | Pass | Standard; tied to D-12. |
| R-061 | India-only data sovereignty | V2 §Component 5 | Pass | Committed; prior Singapore-hosting language excluded. |
| R-062 | DPDP Act 2023 | V2 §Component 5 | Pass | Committed. |
| R-063 | 12-hour breach notification | V2 §Component 5 | Pass | Match. |
| R-064 | Vendor bears breach costs | V2 §Component 5 | Pass | Contract-term acceptance. |
| R-065 | Authoritative AI-agent roster | V3 §Roster Ambiguity | Pass | BRD 8 adopted; divergences flagged. |
| R-066 | Mechanical & HVAC Agent | V3 §Agent 1 | Pass | BRD §3.5.3; register AI-06/07/08/09. |
| R-067 | Electrical Systems Agent | V3 §Agent 2 | Pass | BRD §3.5.3; MRSS dependency flagged. |
| R-068 | Fire Safety Agent (advisory, never replacing) | V3 §Agent 3 | Pass | BRD §3.5.3; register AI-14. |
| R-069 | Water & Drainage Agent (scope) | V3 §Agent 4 | Pass | Scope delivered; no source performance target. |
| R-070 | Energy Management Agent | V3 §Agent 5 | Pass | BRD §3.5.3; unpriced in Table 6 (commercial gap). |
| R-071 | Passenger Flow Agent | V3 §Agent 6 | Pass | BRD §3.5.3; unpriced (commercial gap). |
| R-072 | Structural Integrity Agent (SHM-dependent) | V3 §Agent 7 | Partial | Roster grounded; deliverability contingent on DIAL SHM network + 6–12mo baseline. Truncated commitment text. |
| R-073 | Security & Perimeter Agent (CISF-dependent) | V3 §Agent 8 | Partial | Grounded; "all scope subject to CISF approval before build starts" — carve-out. |
| R-074 | NL Query Agent (AI-10) | V3 §NL Query Agent | Partial | Broader interpretation flagged as open scope-boundary question; narrower GIS-NL line item committed. |
| R-075 | AI Orchestration Engine | V3 §Orchestration | Pass | BRD §3.5.2. |
| R-076 | Data Readiness Gate | V3 §Platform | Pass | Standard practice; register AI-01. |
| R-077 | Shared AI Platform | V3 §Platform | Pass | Register AI-02. |
| R-078 | MLOps lifecycle | V3 §Platform, V4 §Testing | Pass | Standard MLOps. |
| R-079 | Per-agent acceptance | V3 §Platform, V4 §Testing | Pass | Standard; register AI-17. |
| R-080 | Mech&HVAC performance SLAs | V3 §Agent 1 | Pass | BRD §3.5.4 matched. |
| R-081 | Electrical performance SLAs | V3 §Agent 2 | Pass | BRD §3.5.4 matched. |
| R-082 | Passenger Flow performance SLAs | V3 §Agent 6 | Pass | BRD §3.5.4 matched. |
| R-083 | Structural Integrity performance SLAs | V3 §Agent 7 | Partial | Targets matched but deliverability contingent on DIAL SHM procurement. |
| R-084 | Fire Safety performance SLAs | V3 §Agent 3 | Pass | BRD §3.5.4 matched. |
| R-085 | Energy Management performance SLAs | V3 §Agent 5 | Pass | BRD §3.5.4 matched. |
| R-086 | Security performance SLAs | V3 §Agent 8 | Partial | Targets matched but scope subject to CISF approval. |
| R-087 | Water & Drainage performance target | V3 §Agent 4 | N/A | Absent from source documents themselves. |
| R-088 | Explainability + confidence | V3 §Governance | Pass | BRD §3.5.5. |
| R-089 | Auditability 5-year AI-alert log | V3 §Governance | Pass | BRD §3.5.5. |
| R-090 | Feedback loop | V3 §Governance | Pass | BRD §3.5.5. |
| R-091 | Model version control + 4hr rollback | V3 §Governance | Pass | BRD §3.5.5. |
| R-092 | DIAL owns model weights/training data | V3 §Governance | Pass | BRD §3.5.5. |
| R-093 | SHAP/LIME/attention "No Black Box" | V3 §Governance | Partial | Proposal commits general explainability but defers the specific SHAP/LIME/attention technique mandate as "RFP v5-only." RFP v5 §6.4 is an authoritative source and the mandate is not contradicted by the BRD (BRD is more general, not conflicting) — the specific technique commitment is not given. |
| R-094 | 19-system "Not integrated" estate | V2 §Understanding, V3 | Pass | PE_OT inventory — best-evidenced problem-statement fact. |
| R-095 | T1 OT integration | V2 §Integration | Pass | Middleware + RGIA. |
| R-096 | T3 OT integration | V2 §Integration | Pass | Largest scale. |
| R-097 | T2 OT integration | V2 §Integration, V4 | Partial | Register marks TBD/X — flagged to DIAL. |
| R-098 | Common integrations (WTP/STP/MRSS/AGL CMS/ITBMS) | V2 §Integration | Pass | MRSS upgrade dependency flagged. |
| R-099 | IT-side OneAPOC integrations | V2, V4 | Partial | Scope boundary unclear; seek DIAL clarification. |
| R-100 | SPG what-if simulation engine | V3 §SPG | Partial | IROPs/Decision Engine precedent; full 24-use-case engine not built. |
| R-101 | 10 Commercial use cases | V3 §SPG | **Fail (blocking)** | Illustrative only; phased roadmap proposed, not built. |
| R-102 | 8 Operational use cases | V3 §SPG | Partial | Partially adjacent to Passenger Flow Agent; not built as simulation. |
| R-103 | 5 Engineering use cases | V3 §SPG | **Fail (blocking)** | No simulation capability evidenced. |
| R-104 | Borewell recharge IoT | V3 §ABR Mapping | Pass | Adjacent IoT ingestion. |
| R-105 | Storm water + Walter P Moore | V3 §ABR Mapping | Pass | Register AI-12 names Walter P Moore. |
| R-106 | Reverse-entry detection | V3 §ABR Mapping | Pass | Adjacent Security Agent. |
| R-107 | Unattended baggage detection | V3 §ABR Mapping | Pass | Adjacent video analytics. |
| R-108 | Behaviour analytics | V3 §ABR Mapping | Pass | Adjacent Security Agent. |
| R-109 | Predictive security monitoring | V3 §ABR Mapping | Pass | Overlaps Security Agent R-073. |
| R-110 | Security asset mapping | V3 §ABR Mapping | Pass | Adjacent GIS. |
| R-111 | Google Maps/satellite landside | V3 §ABR Mapping | Pass | BRD §3.1.2 "aircraft and satellite scans." |
| R-112 | Space-allocation changes | V3 §ABR Mapping | **Fail (blocking)** | Depends on R-039 land/space gap. |
| R-113 | GIS analytics for planning | V3 §ABR Mapping | Pass | Core GIS capability. |
| R-114 | Fog/low-visibility surface navigation | V3 §ABR Mapping | **Fail (blocking)** | No evidence anywhere in corpus. |
| R-115 | What-if scenario analytics (Ops) | V3 §ABR Mapping | Partial | Same as R-100. |
| R-116 | DigiYatra/E-Gates/CUSS/CUPPS | V3, V4 | Partial | Not in PE_OT or BRD scope; seek clarification. |
| R-117 | Live ops dashboard | V3 §ABR Mapping | Pass | Core APOC/CCC dashboard (R-050). |
| R-118 | Overstaying/unidentified passengers | V3 §ABR Mapping | Pass | Adjacent Passenger Flow Agent. |
| R-119 | 5-phase ~15-month programme | V4 §Programme Structure | Pass | BRD structure adopted. |
| R-120 | 15 deliverables D-01–D-15 | V4 §Deliverables | Pass | BRD §4.2 / RFP §5.2. |
| R-121 | 14-day DIAL review per deliverable | V4 §Deliverable Acceptance | Pass | Standard per BRD §4.2. |
| R-122 | RACI matrix | V4 §RACI, V7 §RACI | Partial | Structure committed; DEC/POD undefined in BRD glossary; no named individuals. |
| R-123 | 8-table costing structure | V5 §Costing Structure | **Partial (blocking)** | Structure present; all pricing blank. Commercial not evaluable. |
| R-124 | AI-agent costing (3 unpriced) | V5 §AI-Agent Costing Gap | Partial | Source-document internal inconsistency (BRD Table 6 prices only 5 of 8); declared but unresolved. |
| R-125 | 6-milestone payment 15/10/20/25/20/10 | V5 §Payment Milestones | Pass | BRD §7 / RFP §9.4. |
| R-126 | 12-month warranty + AMC | V5 §Warranty | Pass | Standard per RFP §9.5. |
| R-127 | 5-year O&M, 24×7, RTO 4hr/RPO 24hr | V4 §O&M, V5 | Pass | Match; RGIA track record. |
| R-128 | ≥3 case studies | V6 §Case Studies | **Fail (blocking)** | 1 of 3; 2 placeholders. |
| R-129 | CVs / key personnel | V7 | **Fail (blocking)** | Complete blank; skeleton only. |
| R-130 | Company profile / org references | V6 §Org Profile | Pass | WAISL footprint asserted. |
| R-131 | 6-month exit support | V4 §Exit Management | Pass | BRD §9.12. |
| R-132 | DIAL exclusive IP on deliverables | V5 §IP | Pass | Standard legal commitment. |
| R-133 | SBOM | V5 §IP | Pass | Standard practice. |
| R-134 | Regulatory approvals at vendor cost | V4 §Regulatory Approvals | Pass | WAISL incumbent under these approvals since 2019. |
| R-135 | Material default 3+ SLA breaches/quarter | V5 §Material Default | Pass | Contractual risk-term acceptance. |

## Step 4 — Numeric parity / delta evaluation

See the companion numeric-inventory file for the full 54-row parity table. Headline result: **43 Pass, 4 Partial, 5 Fail, 1 Ambiguous, 1 N/A.** The BRD's measurable thresholds (survey accuracy, point density, DTM/DSM, GSD, 8-agent precision/recall/latency targets, breach notification, retention periods, RTO/RPO, milestone split, warranty, O&M term, exit support) are almost all matched at parity. The shortfalls are:
- **N-SUR-07 (10 cm contours):** silently missing → Fail.
- **N-PLATFORM-01 (15-year lifecycle):** not committed → Fail.
- **N-PRE-02 (≥2 deployments):** 1 of 2 → Fail.
- **N-SUB-01 / N-SUB-02 (case studies / CVs):** below mandatory minimums → Fail.
- **N-SUR-02 / N-AI-08 / N-AI-09 / N-COM-06:** carve-outs / conditional delivery / unpriced → Partial.

## Step 5 — Semantic carve-out / over-claim detection

Downgrades applied (quoted weakening phrases from the proposal):

1. **Buffer-zone LiDAR density (R-022 / N-SUR-02):** "Match, **pending DIAL confirmation**" — weakens a binding BRD figure (8 pts/m²). Downgraded Pass→Partial.
2. **Structural Integrity Agent (R-072 / N-AI-08):** "**roster inclusion is; actual deliverability is**" — truncated conditional; "cannot start until DIAL procures and installs the SHM sensor network, needing a further 6–12 month baseline." Downgraded Pass→Partial.
3. **Security & Perimeter Agent (R-073 / N-AI-09):** "all scope **subject to CISF approval before build starts**." Downgraded Pass→Partial.
4. **3D viewer AR/VR + offline (R-045):** text literally incomplete — "core 3D viewer capability is; AR/VR output and full offline-mobile responsiveness are." Downgraded to Partial (core grounded, AR/VR + offline not substantiated).
5. **SHAP/LIME/attention "No Black Box" (R-093):** proposal declines to commit to the specific technique mandate, framing it as "RFP v5-only." This is a partial deferral on an authoritative-source requirement. Downgraded to Partial.

Over-claims: none of the "Match" entries on the headline KPI table carry weakening parentheticals, and the 8-agent roster is itemised rather than blanket-claimed. No "100% coverage" over-claims with narrowed mechanisms were detected. The proposal is, if anything, conservative in its claim wording — the failures are genuine gaps, not over-claims.

## Step 6 — "Addressed within narrative" check

Several mandatory topics are addressed only as flagged gaps rather than substantively:
- **Land/space management (R-039):** mentioned in V2 Component 3 only to acknowledge the gap; no capability described. Fail.
- **CLM integration (R-040):** mentioned only to acknowledge absence. Fail.
- **IEC 62443 (R-056) / SOC-SIEM (R-059):** addressed via "compliance roadmap" and "named-partner mitigation" — a roadmap is not compliance. Fail.
- **15-year lifecycle (R-020):** not addressed even in narrative. Fail.
- **10 cm contours:** not addressed at all. Fail.
- **SPG what-if engine (R-100/101/102/103):** addressed with an adjacent precedent (IROPs/Decision Engine) and a phased roadmap, but the 24 use cases are not built. Fail for Commercial/Engineering clusters; Partial for Operational cluster (adjacent to Passenger Flow Agent).

These are buried as honest acknowledgements rather than substantive responses. Per the skill rules, honesty does not convert a gap into compliance.

## Step 7 — Page / word count assessment

| Volume | Estimated pages (proposal's own count) | RFP v5 limit | Status |
|---|---|---|---|
| V1 Executive Summary | ~5 | 10 (max) | OK |
| V2 Technical Approach | ~12 | None stated | OK |
| V3 AI & Analytics | ~10 | None stated | OK |
| V4 Implementation | ~5 | None stated | OK |
| V5 Commercial | ~4 | None stated | OK (content-short: unpriced) |
| V6 Qualifications | ~4 | None stated | At risk (2 of 3 case studies placeholder) |
| V7 Team & Staffing | ~3 | None stated | At risk (skeleton only) |
| Appendices — RTM | ~9 | None stated | OK |
| **Total** | **~52** | only V1 stated | V1 within limit |

No page-limit breaches. V6 and V7 are within limits only because their mandatory content is missing (placeholders/blank), which is a content-compliance failure, not a format failure.

## Step 8 — Cross-reference / multi-artefact consistency

This is a single-artefact validation (the assembled proposal plus its internal RTM appendix). No second cross-check artefact was supplied (the DRAFT RTM was excluded). Findings:

- **Internal inconsistency — incident response:** V1/V4 commit to the BRD's ≤10 min Critical Incident KPI, but V4 §O&M also states a "Sev1 ≤30 min response / 4hr workaround" ladder. The proposal asserts these do not contradict, but does not clearly reconcile "critical incident" vs "Sev1." Flagged Ambiguous. Recommend the final SLA ladder map critical-incident notification to ≤10 min and reserve the ≤30 min figure for non-critical Sev1 workaround commencement.
- **Programme duration:** V4 adopts the BRD's 15-month structure but flags that the Consolidated FINAL proposal's own 9-month figure is unreconciled. The proposal discloses this honestly; not a compliance failure against the BRD, but an unresolved internal inconsistency.
- **AI-agent roster:** V3 resolves the 8-vs-6/7-vs-17 enumeration conflict in favour of the BRD's 8. Consistent with binding priority.
- **TLS version:** V2 adopts BRD TLS 1.3 over the register's TLS 1.2+. Consistent with binding priority.
- **Pricing references:** V5 references the 8-table structure and 6-milestone split consistently with the BRD, but all pricing cells are blank — internally consistent only because everything is unpriced.
- **Naming discipline:** BRD Appendix A/B/D are attributed correctly as "[To be completed by DIAL]" (DIAL-side prerequisites, not vendor gaps). PE_OT's 19-system inventory is attributed correctly.

## Step 9 — Deviation-register completeness audit

**The proposal contains no formal deviation/exemption/assumption register.** It uses `[GAP]` markers in the RTM and an "Unresolved Items" / "Honest Gaps We Flag Rather Than Disguise" section as an informal declaration mechanism. These informal flags lack unique deviation IDs, formal rationale, and mitigation/acceptance requirements.

Per skill graceful-degradation rule: "Deviation register not present in the proposal: Treat every below-binding shortfall as a Fail (undeclared deviation)."

Audit of all below-binding shortfalls against the (absent) register:

| Shortfall | Informally flagged? | Treated as | Deviation-register status |
|---|---|---|---|
| Buffer density "pending DIAL confirmation" | Yes (V2, V5) | Partial (carve-out) | No formal entry |
| Structural Integrity conditional on SHM | Yes (V3, V4) | Partial (carve-out) | No formal entry |
| Security subject to CISF approval | Yes (V3) | Partial (carve-out) | No formal entry |
| IEC 62443 not held | Yes (V2, V6) | Fail (mandatory) | No formal entry |
| SOC/SIEM not evidenced | Yes (V2, V7) | Fail (mandatory) | No formal entry |
| 1 of 2 comparable deployments | Yes (V6) | Fail (gate) | No formal entry |
| 1 of 3 case studies | Yes (V6) | Fail (minimum) | No formal entry |
| CVs/key personnel blank | Yes (V7) | Fail (mandatory) | No formal entry |
| 15-year lifecycle not committed | Yes (RTM R-020) | Fail (binding objective) | No formal entry |
| 10 cm contours omitted | No | Fail (undeclared) | Not flagged at all |
| Land/space module absent | Yes (V2) | Fail (mandatory) | No formal entry |
| CLM integration absent | Yes (V2) | Fail (mandatory) | No formal entry |
| SPG Commercial/Engineering use cases | Yes (V3) | Fail (ABR mandatory) | No formal entry |
| Commercial tables unpriced | Yes (V5) | Partial (blocking) | No formal entry |
| 3 AI agents unpriced in BRD Table 6 | Yes (V5) | Partial (source inconsistency) | No formal entry |

**Finding:** The absence of a formal deviation register is itself a structural compliance gap. Every short fall above is either an undeclared deviation (10 cm contours) or an informally-flagged gap that still fails the underlying mandatory requirement. None are "declared deviations awaiting customer acceptance" in the formal sense the skill requires.

## Step 10 — Adversarial critic pass

A second pass over the numeric inventory and proposal surfaced the following additional findings (none reversed a Pass to a worse verdict; several confirmed Partial/Fail):

1. **10 cm contours (N-SUR-07):** confirmed silently missing — the V2 Component 1 commitment table lists 10 distinct parameters; contours are not among them. This is the clearest undeclared shortfall in the draft.
2. **Sev1 ≤30 min vs ≤10 min critical incident:** potential internal inconsistency not fully reconciled. Flagged in Step 8.
3. **15-year lifecycle:** confirmed absent from every volume; RTM R-020 is the proposal's own concession.
4. **SHAP/LIME/attention (R-093):** the proposal's framing that the technique mandate is "RFP v5-only" is not a valid excuse — RFP v5 is an authoritative source and the BRD does not contradict it (it is more general). Partial stands.
5. **Commercial pricing:** every one of the 8 tables is blank. This is not a Partial that can wait — a commercial proposal with zero prices is not evaluable and is blocking for assembly/submission.
6. **Water & Drainage agent (R-087):** confirmed no source target — N/A is correct; the agent's scope is still delivered, so R-069 is Pass.
7. **Truncated text in V2 Component 4 (R-045) and V3 Agent 7 (R-072):** the assembled document contains incomplete sentences ("core 3D viewer capability is; AR/VR output and full offline-mobile responsiveness are." and "roster inclusion is; actual deliverability is."). These are draft artefacts that also weaken the corresponding commitments. Partial stands.

No further downgrades. One full pass returned nothing new beyond the above.

## Step 11 — Report production

This is the report. The companion numeric inventory is `compliance-report-trackB-numeric-inventory.md`.

## Step 12 — Blocking issues surfaced

**BLOCKING: 14 mandatory requirements not met.** Listed in the table at the top of this report. The proposal is **not ready for assembly**. The proposal assembler must not proceed until:
- 10 cm contours are explicitly committed (N-SUR-07);
- the 15-year lifecycle is committed (R-020);
- IEC 62443 and SOC/SIEM are either evidenced or covered by a formal, customer-accepted deviation with named partners (R-056, R-059);
- ≥2 comparable deployments and ≥3 case studies are evidenced (R-007, R-128);
- Volume 7 CVs / named personnel are provided (R-129);
- land/space management and CLM integration are either delivered or formally deviated (R-039, R-040);
- the SPG what-if Commercial and Engineering use-case clusters are built or formally scoped out of this cycle with DIAL acceptance (R-101, R-103);
- the ABR space-allocation and fog-navigation asks are addressed or formally de-scoped (R-112, R-114);
- the 8 commercial costing tables are priced (R-123);
- a formal deviation register is produced covering every below-binding shortfall.

---

## Remediation summary (every Fail and blocking Partial)

| Finding | Remediation |
|---|---|
| N-SUR-07 10 cm contours | Add an explicit "10 cm contour dataset (SHP/DXF/DWG)" row to V2 Component 1 commitment table; tie to deliverable D-04. |
| R-020 15-year lifecycle | Add an explicit commitment in V2 §Component 4 / V4 that the platform architecture is designed for a minimum 15-year operational lifecycle (BRD Objective 6). |
| R-007 ≥2 deployments | Evidenced a 2nd comparable airport/transport/large-built-environment deployment in V6, or enter a formal deviation with DIAL acceptance. |
| R-039 Land/space module | Deliver or formally deviate the DIAL-legal-vocabulary land/space module; name the product/capability. |
| R-040 CLM integration | Name the CLM tool and integration approach, or formally deviate. |
| R-056 IEC 62443 | Name the IEC 62443 certification roadmap owner and timeline, or formal deviation; "to be named" subcontractor is insufficient for a mandatory standard. |
| R-059 SOC/SIEM | Name the SOC/SIEM service partner and evidence track record, or formal deviation. |
| R-101 / R-103 SPG use cases | Build or formally de-scope (with DIAL acceptance) the 10 Commercial and 5 Engineering what-if use-case clusters. |
| R-112 Space-allocation | Depends on R-039; resolve the land/space gap first. |
| R-114 Fog navigation | Deliver or formally de-scope the low-visibility surface-navigation capability. |
| R-128 ≥3 case studies | Insert evidenced Case Studies 2 and 3. |
| R-129 CVs / key personnel | Populate V7 with named individuals and CVs for all 9 roles listed in the staffing skeleton. |
| R-123 8-table pricing | Price all 8 commercial tables; resolve the 3 unpriced AI agents (R-124) with DIAL. |
| N-SUR-02 / N-AI-08 / N-AI-09 carve-outs | Enter formal deviation-register entries (with IDs, rationale, mitigation) for the buffer-density confirmation, SHM-sensor dependency, and CISF-approval dependency. |
| R-093 SHAP/LIME/attention | Commit explicitly to SHAP/LIME/attention-viz interpretability techniques for deep-learning models (RFP v5 §6.4). |
| R-045 truncated text | Complete the truncated V2 §Component 4 sentences and substantiate AR/VR + offline-mobile. |

---

*End of compliance report — Track B. Companion file: `compliance-report-trackB-numeric-inventory.md`.*