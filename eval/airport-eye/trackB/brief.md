# Collateral Brief — Airport Eye APOC Phase 2 (Track B)

**Eval context**: Stage 1 of a 6-stage automated pipeline (collateral-analyzer → requirements-mapper → section-drafter → empathy-reviewer → proposal-assembler → external compliance scoring). This brief and its companion gap report are the foundation every downstream stage reads. Confidence levels below are reported honestly, including where evidence is thin, stale, or contradictory — inflating them would only surface as failures later in the pipeline.

**Files explicitly excluded from this analysis per task instruction** (reserved as a separate human-drafted eval baseline, not read or referenced anywhere below): `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`, `AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`.

---

## Client Summary

**Client Name:** Delhi International Airport Limited (DIAL), operating Indira Gandhi International Airport (IGIA)
**Industry/Sector:** Airport operations / aviation infrastructure — Operational Technology (OT), Building Management Systems (BMS), and AI/digital-twin platform procurement
**Organization Size:** Large international hub airport — three terminals (T1, T2, T3; T3 interior alone ~588,000 m²), an Aerocity precinct, ~5,000+ acre campus, 4 runways / 180+ stands. Multi-vendor OT estate spanning 19+ distinct legacy systems (Honeywell, JCI/TKE, ABB, Schneider, Safegate, Edwards, GE, Vanderlande, and others) across at least 10 named internal system owners.
**Key Stakeholders:** No named DIAL business stakeholders appear in the requirements documents themselves. The Consolidated FINAL proposal's cover letter is addressed to **DIAL's CIO**, and references a **CIO scope review dated 13-July-2026**, indicating the CIO's office is the active point of contact for this cycle. On the OT/engineering side, `PE_OT System_09.06.pptx.md` names 10 individual system owners (e.g., Ishan Verma, Manish Singh, Sumit Vaish, Bikash Parida, Priyaranjan Ray, Naveen Saini, Anil Kumar Madineni, Atul Kumar Singh, Isaac Clive, Anand, Nitesh Rajkondawar) — useful for understanding whose sign-off individual OT integrations may need, but these are not evaluation/procurement contacts.

The incumbent IT-services **Concessionaire is WAISL Limited**, operating under a **Concession Agreement (CA) dated 30-September-2019**, with GEOKNO as its geospatial/LiDAR/BIM delivery partner. The current cycle (CR/BRD v1.5, dated 05-June-2026) is explicitly framed as a **Change Request against that existing Concession Agreement**, not a fresh open procurement — see the "Collateral Conflict" flag under Stated Priorities below; this is the single most consequential structural ambiguity in the collateral and should be resolved before drafting proceeds.

---

## Problem Statement

DIAL's OT/BMS estate is fragmented and largely unintegrated: the PE_OT system inventory shows the recurring remark **"Not integrated with T3 ITBMS"** across nearly every one of 19 listed OT systems (HVAC, FDAS, VHT, ECMS, LCMS, PBB, VDGS, WTP/STP, MRSS, BHS, ATRS, GPU/PCA, AGL CMS), spanning 10+ different OEMs and integrators. Operations today are reactive: incidents, equipment failures, and safety/security events are discovered after the fact rather than predicted or pre-empted.

**Root Cause Signals:** Growth and modernization strategy, not a specific failure event — the CR/BRD's Section 1.2 background frames this as an evolution of the existing Concession Agreement toward "a global benchmark for intelligent, data-driven airport operations," with the digital-twin/agentic-AI concept positioned as the mechanism to unify a genuinely heterogeneous, multi-vendor OT landscape (confirmed independently by the PE_OT inventory's system-by-system evidence of non-integration).

**Desired Outcome (CR/BRD v1.5 §2.1, verbatim):** "The overarching vision is to create a living, dynamic, and spatially accurate digital replica of the entire airport ecosystem, including the Aerocity precinct. At the core of the Airport Eye concept is a network of federated AI-driven agents with spatial intelligence, operating continuously (24/7), that act as the 'digital eye' of the airport." Success = "transition airport operations from reactive management to predictive and autonomous intelligence, enhancing efficiency, safety, resilience, and passenger experience."

---

## Stated Priorities

Ranked by weight of evidence across binding sources (CR/BRD v1.5 and ABR override the base RFP per task-defined priority; PE_OT is the final/authoritative OT-systems list):

1. **Federated, governed AI-agent monitoring layer (8 mandatory agents)** — Evidence: CR/BRD §3.5.1–3.5.5 states this is "the most technologically advanced and operationally transformative component," with an explicit 8-agent table, per-agent precision/recall/latency/prediction-horizon targets for 7 of the 8 agents, and a dedicated governance subsection (explainability, auditability, feedback loop, DIAL model ownership). — Confidence: **High** that this is DIAL's top technical priority; **Medium** on the exact agent roster, because the base RFP v5 is internally inconsistent (its own agent list varies from 5 to 7 depending on section) and the requirements registers list 17 `AI-*` line items that only partially map onto the BRD's clean 8-agent table (11 are functional agents, 6 are platform/governance items, and one — an NL Query Agent — isn't in the BRD's named list at all).

2. **Survey-grade geospatial/BIM foundation as prerequisite infrastructure** — Evidence: CR/BRD Objective 1 and §3.1 (airborne LiDAR ≥20 pts/m² core / 8 pts/m² buffer, ≤5cm horizontal / ≤3cm vertical RMSE, LOD 200–350 BIM per asset category, ISO 19650 compliance) is the largest single section of the BRD by page count and deliverable count (D-01 through D-10). — Confidence: **High**.

3. **Trustworthy, auditable OT/IT integration with heavy compliance/governance framing** — Evidence: IEC 62443 compliance, network segmentation, penetration testing, SOC/SIEM, India-only data sovereignty (BRD §9.10, an explicit "shall not transfer/store/process data outside India without prior written approval" clause with material-breach consequences), 12-hour breach notification (§9.11), DIAL ownership of AI model weights/training data (§3.5.5). This governance emphasis, repeated across Objectives, §3.4.5, §9.x, and Appendix E, signals DIAL wants innovation *bounded by* rigorous compliance rather than novelty for its own sake. — Confidence: **High** on the requirement; **Medium-Low** on our own evidenced capability (see Evidence Map).

**Collateral conflict — flagged, not resolved:** The base RFP v5 frames this as a **competitively scored procurement** — three-stage evaluation panel, a weighted scoring table (Technical Approach 30% / Experience 25% / AI Capability 20% / Commercial 15% / Implementation 10%), a 7-volume submission structure with page limits, and gating pre-qualification criteria (≥5 years' experience, ≥2 comparable deployments, ISO 9001/27001 certification, a still-unfilled minimum-turnover figure). The CR/BRD v1.5, however, frames the exercise as a **Change Request to the existing Concessionaire (WAISL) under the 2019 Concession Agreement** (§1.2: "the Concessionaire is requested to submit its quotation in accordance with the provisions of the Concession Agreement") — i.e., a negotiated variation with an incumbent, not a scored competitive bid. **This is not resolved anywhere in the collateral.** It materially affects everything downstream: whether page-limit/volume compliance matters at all, whether the 30/25/20/15/10 evaluation weights are still operative, and whether pre-qualification criteria (which an incumbent already under contract would presumably already satisfy) are even in play. See Open Questions.

---

## Evaluation Signals

**Scoring Method:** Ambiguous — see Collateral Conflict above. Base RFP v5 states a formal weighted/panel-scored method; CR/BRD v1.5 reads as direct negotiation with the incumbent Concessionaire.

**Evaluation Factors (per base RFP v5, status uncertain — may be superseded):**
| Factor | Weight |
|---|---|
| Technical Approach and Solution Architecture | 30% |
| Relevant Experience and Track Record | 25% |
| AI and Analytics Capability | 20% |
| Commercial Proposal | 15% |
| Implementation Methodology and Timeline | 10% |

**Oral Presentations:** Unknown — not mentioned in any source document.
**Past Performance Weight:** 25% per RFP v5 table above (status uncertain given the sole-source framing question).

**Reading Between the Lines:** Both the CR/BRD and RFP v5 devote disproportionate detail — including the only granular, numeric, per-item performance tables in the entire corpus — to the AI Agent section (§3.5/§6 respectively), more than to the procedurally larger geospatial/BIM sections. Cybersecurity/data-governance language is repeated across at least four separate sections in each document. Both signals point the same direction: DIAL's real evaluation emphasis (whatever the formal mechanism turns out to be) is AI-agent credibility plus governance/compliance trustworthiness, not price — commercial is weighted lowest (15%) in the one document that gives explicit weights.

---

## Vocabulary & Tone Notes

**Client's Key Terms:**
- **"Airport Eye" / "digital eye of the airport"** — the platform's brand name and central metaphor; must be used, not translated to generic "monitoring platform" language.
- **"Federated AI-driven agents with spatial intelligence"** / **"agentic AI"** — DIAL's specific framing for the AI layer; do not substitute generic "AI/ML" phrasing.
- **"Survey-grade"** — recurring qualifier for geospatial accuracy; signals DIAL wants precision language, not marketing superlatives.
- **"Demised premises / additional demised premises / excluded premises / carved-out assets"**, **"MCD and DCB area bifurcation"** — legal/facilities-management terms specific to DIAL's land-management context (Phase 3); must be mirrored exactly if addressing facilities scope.
- **"Concessionaire"** — DIAL's term for the vendor/bidder (i.e., WAISL); reinforces the incumbent/CA framing.
- **"IGIA"**, **"Aerocity"** — site-specific location names.
- **"POD"** and **"DEC"** — appear in RACI tables and body text but are never defined in the BRD's own glossary (DEC likely "Design/Engineering Consultant" but unconfirmed) — flag rather than guess if drafting must reference these roles.

**Tone Profile:** Aspirational, innovation-flavored front matter ("digital eye," "agentic AI," "predictive and autonomous intelligence") paired with dense, one-sided, liability-shifting contractual back-half language ("Any failure of integration, regardless of originating system, shall be considered a Vendor's responsibility unless explicitly excluded in writing by DIAL"; broad indemnification clause; material-default language tied to SLA breaches, data-clause breaches, and negligent security incidents). Net read: **risk-averse and compliance-driven**, not experimental — the innovation vocabulary describes the desired outcome, but the enforceable mechanics are conservative and vendor-unfavorable. Drafting should lead with concrete, auditable, governed capability rather than innovation-for-its-own-sake framing.

**Language to Avoid:** Generic vendor superlatives ("cutting-edge," "world-class," "industry-leading") without an attached number — the BRD's own KPI/SLA tables are extremely precise (percentages, seconds, cm, days), and DIAL's tone rewards matching that precision. Also avoid asserting agent counts, accuracy figures, or timelines without checking them against the BRD table first — the corpus itself is inconsistent in several places (see Confidence Map and Gap Report), so unattributed claims risk contradicting the very source they're meant to reflect.

---

## Collateral Inventory

| # | File | Type | Summary | Depth of Analysis |
|---|------|------|---------|-------------------|
| 1 | `Change Request Aiport Eye - APOC Phase 2.pdf.md` | RFP/RFI — **binding, highest priority** | CR/BRD v1.5 (DIAL-AE-BRD-001), 05-Jun-2026, issued to Concessionaire WAISL under the 2019 CA; vision, 6 objectives, 7 KPIs, 5-phase scope, 8-agent AI architecture, cybersecurity/data-sovereignty clauses, commercial costing framework, payment milestones | Deep |
| 2 | `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` | RFP/RFI — supplementary, overrides base RFP on conflict | ABR memo consolidating departmental asks (P&E, S&V, Commercial Aero, Operations, SPG); dominated by a large SPG "what-if" simulation/digital-twin decision-engine ask (24 use cases across Commercial/Operational/Engineering); numerically thin — only one "must" statement, no attached targets | Deep |
| 3 | `PE_OT System_09.06.pptx.md` | RFP/RFI — final/authoritative OT-systems inventory | 19-system OT inventory across HVAC/FDAS/VHT/ECMS/LCMS/PBB/VDGS/WTP/STP/MRSS/BHS/ATRS/GPU-PCA/AGL-CMS with owners, OEMs, and integration status; nearly every row flagged "Not integrated with T3 ITBMS" | Deep |
| 4 | `Airport_Eye_RFP_v5.docx.md` | RFP/RFI — base document, superseded on conflict | Full competitive-RFP structure: weighted evaluation criteria, 7-volume submission format with page limits, pre-qualification gates, KPI/SLA tables, 6-component scope, AI-agent section (internally inconsistent — 3 different agent-count enumerations), 3 unfilled numeric placeholders | Deep |
| 5 | `AirportEye_Requirements_Register_v5.xlsx.md` | RFP/RFI — granular requirements register | ~1,167-line register ("Final Requirements" tab): Geokno LiDAR/BIM/Geo-DT scope, per-terminal OT integration point counts, 17 `AI-*` rows (11 functional + 6 platform/governance), NFR/SLA table, plus a "Geokno_Timeline" Gantt sheet | Deep |
| 6 | `Final requirements.xlsx.md` | RFP/RFI — granular requirements register (partial/trimmed variant) | Same "Final Requirements" sheet lineage as #5 — ~80% word-for-word identical (including all 17 AI-agent rows and all NFR/SLA figures), but missing most LiDAR-scanning and Geo-DT-functionality detail rows present in #5, and systematically diverges from #5 on BIM-modeling delivery months/phases for nearly every shared row | Deep |
| 7 | `AirportEye_Solution_Proposal_v9.docx.md` | Prior proposal (our collateral) — **stale** | WAISL/GEOKNO proposal, v3.0, May-2025; RGIA (Hyderabad) proof point (18+ months, 40+ systems, 100+ KPIs); commits to only **7** AI agents and **10 pts/m²** LiDAR density — both materially below current BRD requirements (8 agents, ≥20 pts/m²); no data-sovereignty statement | Deep |
| 8 | `DIAL APOC Phase II Proposal 1.pdf.md` | Prior proposal (our collateral) — **different, narrower engagement** | WAISL + KloudSpot proposal, 21-Apr-2025, for a KPI-dashboard/video-analytics/AODB integration project (no digital twin, no LiDAR, no AI agents in the current sense); own P1–P4 SLA ladder unrelated to current Severity-1 ≤10-min requirement; proposes AWS Singapore-region DR hosting — in tension with the BRD's India-only data-sovereignty clause | Deep |
| 9 | `Airport_Eye_Consolidated_Proposal_FINAL.docx.md` | Prior proposal (our collateral) — **current, best-aligned** | Cover letter dated 14-Jul-2026 to DIAL's CIO, explicitly reconciled against BRD v1.5 / ABR / a 13-Jul-2026 CIO scope review; correctly commits to 8 agents, ≥20 pts/m² LiDAR, Severity-1 ≤10-min response, India-only data residency, 12-hr breach notification, 6-month exit support; self-flags several agent-performance rows and cost figures as unverified/placeholder; only 1 of 3 required case studies (RGIA) is fully evidenced | Deep |
| 10 | `Airport Eye - Scope v5.png.md` | Prior proposal / org diagram (our collateral) | One-page architecture infographic, explicitly reconciled to the **v9** proposal (not the current Consolidated FINAL) — 3-layer diagram (Airport Eye twin / 8 IT-OT system families / Data-Pipeline-AI layer); the "8 systems" shown are IT/OT system families, not the 8 AI agents — a coincidental-number risk if skimmed quickly | Skimmed (no numeric content) |

*(Not analyzed, per explicit task exclusion: `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`, `AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`.)*

---

## Evidence Map

### Technical Capability
**Available Evidence:** Consolidated FINAL proposal (file #9) gives a fully current, BRD-aligned technical narrative: two-layer Geo Digital Twin + Operational Digital Twin/AIOP architecture, RGIA-proven integration fabric ("hub-and-spoke," 40+ systems, 18+ months live), full 8-agent performance table, survey/BIM figures matching the BRD. WAISL certifications (ISO 9001, 20000, 27001, 22301, CMMI ML3) support general delivery-maturity claims.
**Gaps:** No IEC 62443-specific certification or evidence found anywhere in our collateral (the BRD requires it explicitly for OT/IT integration components). Several of the Consolidated FINAL's own agent-performance rows are self-annotated "(attributed to BRD Section 3.5.4 — verify)" — meaning even our newest document isn't fully confident in its own numbers yet. No evidence anywhere of the SPG "what-if" simulation/decision-engine capability described in the ABR (24 use cases) being built or piloted.

### Past Performance / Case Studies
**Available Evidence:** RGIA (Rajiv Gandhi International Airport, Hyderabad) is a strong, specific, quantified reference: 18+ months live operation, 40+ integrated systems, 100+ KPIs tracked. WAISL's own footprint (India, UAE, US, UK, Singapore, Greece, Kuwait) is asserted but not tied to specific comparable digital-twin/BIM/AI-agent deployments.
**Gaps:** RFP v5 Appendix E requires a minimum of 2 comparable deployments and the submission structure (Volume 6) requires a minimum of 3 case studies — the Consolidated FINAL proposal itself explicitly marks two of its three case-study slots as **"[Placeholder — bidder input]"**. Only 1 of 2 (pre-qualification) and 1 of 3 (submission) required comparable references is currently evidenced.

### Team & Staffing
**Available Evidence:** PE_OT lists 10 named DIAL-side OT system owners (useful for understanding client contacts per system, not for our own staffing).
**Gaps:** No named personnel, CVs, role-specific qualifications, or staffing plan for our own delivery team appear in any of the four org-collateral/prior-proposal documents. This entire area is unaddressed.

### Security & Compliance
**Available Evidence:** WAISL holds ISO 9001, ISO 20000, ISO 27001, ISO 22301, CMMI ML3 (from Consolidated FINAL and v9). The Consolidated FINAL correctly commits to India-only data residency, DPDP Act 2023 compliance, and 12-hour breach notification, matching the BRD.
**Gaps:** No IEC 62443 evidence (explicitly required). No SOC/SIEM-specific track record cited. One of our own prior proposals (`DIAL APOC Phase II Proposal 1.pdf.md`) proposes AWS Singapore-region DR hosting — directly in tension with the India-only data-sovereignty clause — and should not be reused without correction if any of its infrastructure language is repurposed.

### Pricing & Commercial
**Available Evidence:** Both the BRD and RFP v5 provide detailed costing table structures (LiDAR, BIM-by-LOD, legacy migration, BIM-BMS integration, digital-twin viewer, AI agentic framework, infrastructure, 5-year O&M) and a 6-milestone payment schedule (15/10/20/25/20/10%). `DIAL APOC Phase II Proposal 1.pdf.md` contains real commercial figures (₹9.02cr / ₹11.08cr for its two phases) but for a materially different, narrower engagement — not directly reusable.
**Gaps:** The Consolidated FINAL proposal explicitly flags its own O&M cost figures and penalty-formula numbers as **"placeholder pending bidder finalisation"** — meaning no fully committed current pricing exists yet in any of our collateral. The BRD's own Table 6 (AI-agent costing) prices only 5 of the 8 mandatory agent types, an unresolved internal inconsistency. The RFP v5's Appendix E annual-turnover pre-qualification figure is an unfilled `[X] crore` placeholder.

---

## Confidence Map

| RFP Section / Evaluation Area | Confidence | Rationale |
|---|---|---|
| Vision, objectives, and KPI targets | High | Stated clearly and consistently in CR/BRD v1.5 §2.1–2.3, cross-confirmed by RFP v5 and both requirements registers |
| Geospatial/LiDAR/BIM scope and accuracy figures | High | Consistent point-density (≥20/8 pts/m²), RMSE (≤5cm/≤3cm), and LOD figures across BRD, RFP v5, and the Consolidated FINAL proposal; registers confirm acreage/scope but do not carry accuracy numbers themselves |
| AI agent roster (exact count and names) | Medium | BRD's 8-agent table is authoritative, but RFP v5 is internally inconsistent (5/6/7-agent variants across its own sections) and the requirements registers' 17 `AI-*` rows don't cleanly map onto the BRD's 8 — reconciliation is needed before requirements-mapper stage |
| AI agent performance SLAs (precision/recall/latency) | Medium | 7 of 8 BRD agents have explicit targets (Water & Drainage has none); Consolidated FINAL proposal largely mirrors these but self-flags several rows as unverified |
| Incident response / SLA times | Medium-High | Current requirement is clear and consistent (BRD §2.3 and registers: ≤10 min critical) and the Consolidated FINAL proposal matches it — but two of our three older prior-proposal documents commit to materially different, incompatible figures (≤1 hr; a 30/60/90-min P1–P4 ladder) that must not be reused |
| Cybersecurity requirements (IEC 62443, SOC, encryption, RBAC) | High (requirement) / Low (our evidenced compliance) | Requirement language is explicit and detailed in the BRD; no IEC 62443 certification or SOC/SIEM track record found anywhere in our own collateral |
| Data sovereignty / retention | High (requirement) / Medium (our commitment) | BRD §9.10 is unambiguous (India-only, DPDP Act 2023); Consolidated FINAL correctly commits to this, but one of our own older proposals (APOC Phase II) proposes Singapore-region hosting — a live risk if that language were ever reused |
| Evaluation method / scoring weights | Low | Only the base RFP v5 states formal weights, and the CR/BRD's own framing (direct negotiation with the incumbent Concessionaire under an existing CA) casts doubt on whether that competitive-scoring structure still applies — unresolved contradiction, not just a gap |
| Submission mechanics (volumes, page limits, format) | Low | Same unresolved contradiction as above — RFP v5's 7-volume/page-limit structure may or may not be operative under a CR/direct-negotiation model; BRD gives only a 10-day submission window with no restated format requirements |
| Past performance / case studies | Medium | One strong, fully evidenced reference (RGIA); pre-qualification and submission minimums (2 and 3 references respectively) are not yet met — 2 of 3 case-study slots are explicit placeholders |
| Team & staffing | Missing | No named personnel, CVs, or staffing plan found in any reviewed document |
| Pricing & commercial | Low | Costing table structures and milestone percentages are clear; no committed final figures exist — Consolidated FINAL explicitly labels its own cost lines as placeholders pending finalization |
| Geokno LiDAR/BIM delivery schedule (registers) | Low | The two requirements registers systematically disagree with each other on delivery month/phase for nearly every shared BIM-modeling line item; do not treat either register's schedule as settled without reconciliation |

---

## Open Questions

- [ ] **Is this a competitively scored RFP (per RFP v5's evaluation weights and 7-volume submission structure) or a negotiated Change Request to the existing Concessionaire under the 2019 CA (per CR/BRD v1.5's own framing)?** — Affects: evaluation strategy, submission format/page limits, whether pre-qualification gates apply — Priority: **High** (this is the single highest-priority question; it changes how every downstream stage should operate)
- [ ] What is the authoritative, final AI-agent roster and count — the BRD's clean 8-agent table, or some reconciliation with the requirements registers' 17 `AI-*` line items (11 functional + 6 platform/governance, including an NL Query Agent not named in the BRD)? — Affects: AI/Analytics section drafting, compliance mapping — Priority: High
- [ ] What are the missing performance targets (precision/recall/latency) for the Water & Drainage Monitoring Agent, absent from the BRD's §3.5.4 table? — Affects: AI agent SLA commitments — Priority: Medium
- [ ] Which of the two requirements registers' conflicting BIM-modeling delivery-month/phase assignments is correct, or has this been reconciled in a version neither register reflects? — Affects: implementation timeline / phasing section — Priority: Medium
- [ ] Does the Consolidated FINAL proposal's stated "9-month delivery (Mo1–Mo9), re-baselined to March 2027" reconcile with the BRD's own ~15-month (5 phases × ~3 months) programme structure, or are these two different things (e.g., a T2 fast-track subset vs. full programme)? — Affects: implementation methodology/timeline section, and the 10% evaluation weight tied to it — Priority: High
- [ ] Can Appendices A, B, and D of the CR/BRD (Schedule of Buildings/Areas, BIM Execution Plan Requirements, Existing System Inventory) — all currently marked "[To be completed by DIAL]" — be obtained before drafting, since Appendix A underlies all area-based BIM/LiDAR costing? — Affects: commercial costing accuracy, BIM scope precision — Priority: High
- [ ] What is DIAL's minimum annual-turnover pre-qualification threshold (RFP v5 Appendix E currently shows an unfilled `[X] crore` placeholder)? — Affects: pre-qualification compliance response — Priority: Medium
- [ ] Can a second comparable past-performance deployment (beyond RGIA) be identified/evidenced to meet the ≥2-comparable-deployment pre-qualification gate and the ≥3-case-study submission requirement? — Affects: Past Performance section — Priority: Medium
- [ ] Should buffer-zone LiDAR density be confirmed at 8 pts/m² (proposed in the Consolidated FINAL, "pending DIAL confirmation") — is this actually settled in the BRD, or still open? — Affects: geospatial commercial costing — Priority: Low-Medium
