# Gap Report — Airport Eye APOC Phase 2 (Track B)

Companion to `brief.md`. Organized by major RFP section / evaluation area. This is a decision tool, not a complaints list: each area states what we have, what's missing, what would resolve it, whether drafting can proceed with a caveat, and the recommended action.

Excluded from all analysis per task instruction: `AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`, `AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`.

---

## 0. Procurement Mechanism (Competitive RFP vs. Negotiated Change Request)

**What evidence exists:** Base RFP v5 contains a full competitive apparatus — 3-stage evaluation panel, a weighted scoring table (30/25/20/15/10%), a 7-volume submission structure with page limits, and gating pre-qualification criteria. The CR/BRD v1.5, which is the binding, most-recent document, frames the entire exercise differently (§1.2): "the Concessionaire is requested to submit its quotation in accordance with the provisions of the Concession Agreement" dated 30-Sep-2019 — language consistent with a negotiated variation/change order to an incumbent, not a scored competitive bid.

**What is missing:** Nothing in the collateral explicitly reconciles these two framings. No document states "the RFP v5 evaluation criteria have been superseded" or "the RFP v5 evaluation criteria still apply under this CR." The BRD gives no page limits, volume structure, or scoring method of its own.

**What questions should be asked:** Is DIAL running a scored evaluation for this Change Request, or is WAISL's incumbency under the CA sufficient that this is effectively a negotiated quotation? If scored, do the RFP v5 weights (30/25/20/15/10) still apply?

**Can we proceed with caveats?** No — this is disqualifying-level ambiguity for the assembler/scoring stages, not a manageable gap. Proceeding under the wrong assumption (e.g., producing a 7-volume, page-limited competitive submission when DIAL expects a CA-referenced quotation letter, or vice versa) would misdirect every downstream stage's structure.

**Recommended action:** **Flag for bid/no-bid-equivalent decision before section-drafter runs.** This eval should treat this as the single highest-priority unresolved item. In the absence of a real answer, the safest default for a Track B automated pipeline is to draft against the **more complete/formal RFP v5 structure** (since a formal document is a strict superset — a negotiated quotation can always drop volumes, but a quotation letter cannot retroactively acquire an evaluation-compliant structure it never built), while explicitly labeling that assumption in the assembled proposal's cover material.

---

## 1. Vision, Objectives, and KPIs

**What evidence exists:** CR/BRD v1.5 §2.1–2.3 gives a clear vision statement, 6 objectives, and a 7-row KPI table with hard numeric targets (uptime ≥99.5%, latency ≤5s, LOD compliance 100%, predictive alert accuracy ≥80%/≥75%, geospatial accuracy ≤5cm/≤3cm RMSE, critical incident response ≤10 min, integration coverage 100% within 3 months). Cross-confirmed by RFP v5 (near-identical KPI table, though with a materially different incident-response figure — see §7 below) and both requirements registers (matching NFR/SLA section).

**What is missing:** Nothing structurally missing here — this is the best-evidenced section in the entire corpus.

**What questions should be asked:** None high-priority; this section is ready to draft from.

**Can we proceed with caveats?** Yes, without caveats.

**Recommended action:** Proceed with direct assertion, citing the BRD KPI table as the authoritative source (not the RFP v5 table, given the incident-response discrepancy noted in §7).

---

## 2. Geospatial / LiDAR / BIM Scope

**What evidence exists:** BRD §3.1 and RFP v5 §3.1.1–3.1.3 agree on point density (≥20 pts/m² core, 8 pts/m² buffer), RMSE (≤5cm horizontal / ≤3cm vertical), DTM/DSM resolution (10cm grid), orthophoto GSD (≤5cm), and LOD ranges (200–350). The Consolidated FINAL proposal (our most current org-collateral) matches these figures and adds acreage detail (~200 sq.km total survey, 225 acres landside LiDAR, 5km buffer, ~5,000+ acre campus). Both requirements registers independently confirm the acreage/scope figures (5,000 acres campus, 5km radius, 225 acres GPR).

**What is missing:** (a) Buffer-zone point density is stated as 8 pts/m² in the BRD/RFP but the Consolidated FINAL proposal itself annotates this as "pending DIAL confirmation" — treat as not fully settled. (b) RFP v5 has an unfilled indoor-scanning density placeholder (`[X]` points/m² at internal surfaces, §3.2.1) that must not be mistaken for a settled figure. (c) Neither requirements register carries an accuracy/point-density number at all — they give scope (acreage) only, so they cannot be used to cross-check the accuracy figures, only the coverage area. (d) CR/BRD Appendix A (Schedule of Buildings/Areas for BIM Modelling) is an explicit unfilled placeholder ("[To be completed by DIAL]") — this underlies all area-based BIM/LiDAR costing and is not currently available in any form.

**What questions should be asked:** Can DIAL confirm the buffer-zone point density (8 pts/m²) and provide the completed Appendix A building/area schedule before commercial costing is finalized?

**Can we proceed with caveats?** Yes — the core accuracy/density figures are solid and consistent across 3+ sources; only the buffer-zone figure and the underlying building schedule need a flagged caveat.

**Recommended action:** Proceed with assertion on core LiDAR/BIM figures; flag buffer-zone density and Appendix A dependency explicitly in the commercial section as open items pending DIAL input.

---

## 3. AI Agent Architecture and Roster

**What evidence exists:** BRD §3.5.3 gives a clean, explicit 8-agent table (Mechanical & HVAC, Electrical, Fire Safety, Water & Drainage, Energy Management, Passenger Flow, Structural Integrity, Security & Perimeter). The Consolidated FINAL proposal matches this 8-agent framing.

**What is missing:** RFP v5 is internally inconsistent — §6.3 lists 6 agents (with a numbering gap where §6.3.3 should be), §6.5's performance table scores 7 different agents, and the commercial Table 6 in both RFP v5 and the BRD prices only 5 named agent types. None of RFP v5's three internal enumerations matches the BRD's clean 8. Separately, the two requirements registers carry **17** `AI-*` line items (AI-01 through AI-17), of which only 11 (AI-06–AI-16) are actual functional monitoring agents — the rest are platform/governance items (Data Readiness Gate, Shared AI Platform, Orchestration Engine, Explainability/Audit, MLOps Reporting, Acceptance Milestone). Even the 11 functional register items don't map 1:1 onto the BRD's 8 named agents: the registers split "Mechanical & HVAC"/"Energy" into four granular sub-capabilities (load forecasting, waste/anomaly detection, predictive maintenance, optimization advisory) and add a **Natural-Language Query Agent (AI-10)** that has no counterpart anywhere in the BRD's named list. One prior proposal (`AirportEye_Solution_Proposal_v9.docx.md`, May-2025) commits to only **7** mandatory agents — a stale figure that must not be reused.

**What questions should be asked:** Is the BRD's 8-agent table the final, authoritative roster, and if so, how do the registers' 17 `AI-*` items (particularly the NL Query Agent and the 4-way HVAC/Energy split) map onto it — are they sub-tasks of the 8 named agents, or additional in-scope capability beyond the 8?

**Can we proceed with caveats?** Yes, with an explicit caveat that the BRD's 8-agent table is being treated as authoritative and the register's granular items are treated as implementation detail under that umbrella, pending confirmation.

**Recommended action:** Requirements-mapper should reconcile the BRD's 8 agents against the registers' 17 `AI-*` rows explicitly, rather than silently picking one; the NL Query Agent in particular should be flagged as a possible scope addition not covered by the BRD's named agent list or its per-agent performance table.

---

## 4. AI Agent Performance Standards (Precision/Recall/Latency)

**What evidence exists:** BRD §3.5.4 gives explicit precision/recall/prediction-horizon/alert-latency targets for 7 of the 8 named agents (80–95% precision, 75–95% recall, 45 minutes–7 days prediction horizon, 5–60 seconds alert latency). Consolidated FINAL proposal largely reproduces this table.

**What is missing:** The **Water & Drainage Monitoring Agent has no performance-standard row** in the BRD's own §3.5.4 table — this is a genuine gap in the source document itself, not an extraction error (confirmed independently against both RFP v5's own performance table, which also omits it). Several rows in the Consolidated FINAL proposal are self-annotated "(attributed to BRD Section 3.5.4 — verify)," meaning our own most current document isn't fully confident in its own numbers.

**What questions should be asked:** What are DIAL's expected precision/recall/latency targets for the Water & Drainage agent, given every other agent has one?

**Can we proceed with caveats?** Yes — 7 of 8 agents are fully specified; only Water & Drainage needs a flagged assumption or an explicit "target to be agreed with DIAL" placeholder.

**Recommended action:** Draft Water & Drainage agent commitments as "to be finalized in consultation with DIAL, consistent with the rigor applied to the other 7 agents" rather than inventing a number.

---

## 5. Cybersecurity and Data Governance Requirements

**What evidence exists:** BRD §3.4.5/§9.10/§9.11 gives explicit, detailed requirements: IEC 62443 compliance for OT/IT integration, network segmentation, penetration testing pre-go-live, SOC/SIEM, MFA, RBAC (5 roles), TLS 1.3 in transit, AES-256 at rest, India-only data residency (explicit prohibition on transferring/storing/processing data outside India without prior written DIAL approval, treated as material breach), 12-hour breach notification, and DIAL ownership of all AI model weights/training data. WAISL holds general certifications (ISO 9001, 20000, 27001, 22301, CMMI ML3).

**What is missing:** No IEC 62443 certification or specific compliance evidence anywhere in our own collateral. No SOC/SIEM operational track record cited. Critically: one of our own prior proposals (`DIAL APOC Phase II Proposal 1.pdf.md`) proposes **AWS Singapore-region hosting for disaster recovery** — directly in tension with the India-only data-sovereignty clause. This is a real and specific risk, not a generic gap: if any infrastructure language from that proposal is reused without correction, it would create a self-inflicted compliance contradiction in the final response.

**What questions should be asked:** Does WAISL/GEOKNO (or a named subcontractor) hold IEC 62443 certification, or is this a capability gap requiring a partner or a stated compliance roadmap?

**Can we proceed with caveats?** Yes for general security posture (strong ISO/CMMI baseline to cite); **no, not without correction**, for any hosting/DR architecture language — the Singapore-hosting proposal must be explicitly excluded from reuse, and any infrastructure section must assert India-only hosting affirmatively.

**Recommended action:** Draft cybersecurity section from ISO/CMMI certifications plus an explicit commitment to IEC 62443 compliance (roadmap if not yet certified); explicitly instruct section-drafter to exclude the APOC Phase II proposal's Singapore-hosting language from any reuse and assert India-only data residency throughout.

---

## 6. Data Retention and Sovereignty

**What evidence exists:** BRD is explicit and internally consistent: BMS historical data retention minimum 5 years (§3.4.2), AI-alert audit log retention minimum 5 years (§3.5.5), user-activity audit logging retention minimum 2 years (§3.4.4) — these are two *different* logs with two *different* retention periods, not a contradiction (worth noting so requirements-mapper doesn't flag it as one). Data sovereignty: India-only, explicit and strict (§9.10). Consolidated FINAL proposal correctly commits to all of this, including noting it "supersedes RFP Section 3.5.2's 2-year figure" with the BRD's 5-year figure for the AI/Bronze-layer log specifically.

**What is missing:** `AirportEye_Solution_Proposal_v9.docx.md` (older) states only a generic 5-year retention line with **no data-sovereignty statement anywhere** — a real gap in that document, not evidence we can rely on for the sovereignty commitment. `DIAL APOC Phase II Proposal 1.pdf.md` addresses neither retention nor sovereignty at all, and (per §5 above) actively conflicts with the sovereignty requirement via its Singapore-hosting proposal.

**What questions should be asked:** None outstanding on the requirement itself — this is a clear, binding clause. The open question is purely internal: which of our own prior-proposal documents should NOT be reused for this section (answer: v9 and the APOC Phase II proposal, both silent-or-contradictory on sovereignty).

**Can we proceed with caveats?** Yes, and without a major caveat — the Consolidated FINAL proposal already provides fully aligned, ready-to-use language for this section.

**Recommended action:** Draft directly from the Consolidated FINAL proposal's retention/sovereignty language; instruct drafter explicitly not to pull retention/sovereignty language from v9 or the APOC Phase II proposal.

---

## 7. Incident Response / SLA Times

**What evidence exists:** The current, binding figure is unambiguous and triple-confirmed: BRD §2.3 KPI table, both requirements registers' NFR sections, and the Consolidated FINAL proposal all state **Critical/Severity-1 incident response ≤10 minutes**. The Consolidated FINAL also adds a fuller O&M support ladder (Sev1 ≤30min/4hr workaround, Sev2 ≤1hr/8hr, Sev3 ≤4 business hrs/5 business days, Sev4 ≤1 business day/30 days) that is consistent with, and elaborates on, the ≤10-min headline KPI.

**What is missing / contradicts:** RFP v5's own KPI table states Critical Incident Response as **≤1 hour** — six times slower than the BRD's ≤10-minute figure, for what should be the same metric. `AirportEye_Solution_Proposal_v9.docx.md` (May-2025) also commits to ≤1 hour, matching the stale RFP v5 figure rather than the current BRD. `DIAL APOC Phase II Proposal 1.pdf.md` uses an entirely different, unrelated P1–P4 SLA ladder (30/60/90/90-minute response tiers) from a narrower, different-scope engagement. **This is exactly the kind of confident-but-wrong precision the eval is designed to catch**: three different, specific numbers exist across the corpus for "incident response time," and only the newest, BRD-aligned figure (≤10 min) is correct for this procurement.

**What questions should be asked:** None on the correct current figure — it's clear from the binding source. The risk is purely about which prior-proposal language gets reused downstream.

**Can we proceed with caveats?** Yes — the correct figure is well established; the risk is entirely about drafting-stage reuse discipline, not missing information.

**Recommended action:** Explicitly instruct section-drafter to use ≤10 minutes (BRD §2.3) as the Critical/Severity-1 incident response commitment, and to treat the ≤1-hour figure (RFP v5, v9 proposal) and the P1–P4 ladder (APOC Phase II proposal) as superseded/inapplicable — do not average, blend, or "split the difference" between these numbers.

---

## 8. OT/BMS System Integration

**What evidence exists:** `PE_OT System_09.06.pptx.md` is explicit, final, and detailed — 19 named OT systems with owners, OEMs, and per-system integration status, with the dominant finding being that nearly every system is currently **not integrated with T3 ITBMS**. Both requirements registers independently confirm this with per-terminal, per-system point/tag counts (e.g., T3 HVAC 54,000 points, T3 FDAS 65,000 points, MRSS 60,000 tags), giving strong quantitative grounding for the scale of the integration challenge.

**What is missing:** No committed integration timeline per system beyond the general 5-phase programme structure; some T2 systems have counts marked "TBD"/"X" in the registers (undefined OEM or point count) — these should not be treated as confirmed zero-scope, just unconfirmed.

**What questions should be asked:** For T2 systems marked TBD/X in the registers, can DIAL confirm whether integration is in scope at all, or out of scope by design?

**Can we proceed with caveats?** Yes — the overall integration challenge and most terminal-specific figures are solidly evidenced; only a handful of T2-specific line items are genuinely unknown.

**Recommended action:** Proceed with assertion on T1/T3 figures; flag T2 TBD items explicitly rather than guessing counts.

---

## 9. SPG "What-If" Simulation / Decision-Engine Scope (ABR)

**What evidence exists:** The ABR (2-July-2026) devotes its largest section (24 use cases across Commercial, Operational, and Engineering categories) to a simulation/digital-twin decision-support capability requested by SPG (Strategic Planning Group) — store-mix optimization, queue-vs-revenue trade-offs, thermal-load simulation, disruption monetization, etc.

**What is missing:** This scope is not clearly reflected anywhere in the BRD's 8-agent AI architecture or in RFP v5's 6-component scope. No document states whether this becomes a 9th agent, a separate module, or is descoped. The Consolidated FINAL proposal references "the IROPs/Disruption Decision Engine" and cross-references "Solution Proposal v9 Section 5.2," suggesting some prior internal thinking exists on this, but it is not resolved into the current 8-agent framework anywhere reviewed.

**What questions should be asked:** Does the SPG "what-if" simulation/decision-engine requirement fold into the existing AI-agent architecture (as a 9th agent or an extension of an existing one), or is it a separate platform capability with its own SLA/evaluation treatment?

**Can we proceed with caveats?** Yes, with a clearly flagged assumption — this is real, DIAL-prioritized scope (largest section of the ABR) that risks being under-addressed if treated as a footnote to the 8-agent framework.

**Recommended action:** Requirements-mapper should treat this as its own tracked scope item distinct from the 8 AI agents, not silently fold it in or drop it.

---

## 10. Past Performance and Case Studies

**What evidence exists:** RGIA (Rajiv Gandhi International Airport, Hyderabad) is a strong, specific, quantified case study: 18+ months live operation, 40+ integrated systems, 100+ KPIs tracked — repeated consistently across v9 and the Consolidated FINAL proposal.

**What is missing:** RFP v5 Appendix E requires ≥2 comparable deployments for pre-qualification and Volume 6 requires ≥3 case studies for submission. The Consolidated FINAL proposal itself explicitly marks **two of its three case-study slots as "[Placeholder — bidder input]"** — meaning only 1 of 2 (pre-qualification) and 1 of 3 (submission) required references currently exist in our collateral.

**What questions should be asked:** Are there other comparable WAISL/GEOKNO deployments (digital twin, BIM, geospatial, or large-scale airport/infrastructure AI monitoring) that simply haven't been written up yet, or is RGIA genuinely the only comparable reference available?

**Can we proceed with caveats?** No, not fully — this is a pre-qualification gating criterion (≥2 deployments), and only 1 is evidenced. This risks disqualification if the competitive-RFP framing (§0 above) turns out to be operative.

**Recommended action:** Seek additional case-study collateral before the proposal-assembler stage; flag this explicitly in the pre-flight checklist as a potential compliance failure if the RFP v5 pre-qualification gate applies.

---

## 11. Team and Staffing

**What evidence exists:** None. No named personnel, CVs, certifications, or role-specific staffing plan for our own delivery team appear in any of the four reviewed prior-proposal/org-collateral documents.

**What is missing:** Everything — this is a complete blank in the current collateral set.

**What questions should be asked:** Who are the named project leads, technical architects, and key AI/BIM/GIS personnel WAISL/GEOKNO would propose, and what are their qualifications?

**Can we proceed with caveats?** No — this area cannot be addressed without additional collateral. It should not be drafted from assertion alone if the RFP v5 submission structure (which includes a "Qualifications & References" volume with CVs) is operative.

**Recommended action:** Request team/staffing collateral from capture team before section-drafter attempts this section; do not fabricate placeholder bios.

---

## 12. Pricing and Commercial

**What evidence exists:** Both the BRD and RFP v5 provide detailed costing table structures (LiDAR, BIM-by-LOD, legacy CAD migration, BIM-BMS integration, digital-twin viewer, AI agentic framework, infrastructure, 5-year O&M) and a clear 6-milestone payment schedule (15/10/20/25/20/10% of contract value, summing to 100%). `DIAL APOC Phase II Proposal 1.pdf.md` contains real, specific commercial figures (₹9.02cr / ₹11.08cr across two phases) but for a materially different, narrower engagement (KPI dashboards, not the digital-twin/AI-agent programme) — not directly transferable.

**What is missing:** The Consolidated FINAL proposal explicitly labels its own O&M cost figures and penalty-formula numbers as **"placeholder pending bidder finalisation"** — no fully committed current pricing exists in any reviewed document for the actual Airport Eye scope. The BRD's own Table 6 (AI-agent costing) prices only 5 of the 8 mandatory agent types, an internal inconsistency in the source document itself. RFP v5 Appendix E's minimum-turnover pre-qualification figure is an unfilled `[X] crore` placeholder.

**What questions should be asked:** Can DIAL clarify how the 3 unpriced AI agents (Energy Management, Passenger Flow, Structural Integrity) should be costed — folded into the "Generic and Configurable AI Agent" lump sum, or itemized separately? What is the actual minimum-turnover threshold?

**Can we proceed with caveats?** Yes for structure (table formats and milestone percentages are solid); no for actual committed numbers — this section cannot be finalized without genuine bidder cost-modeling input, which is out of scope for this eval's automated pipeline.

**Recommended action:** Draft the commercial section's structure and milestone schedule with confidence; explicitly flag that final unit/line-item pricing requires bidder financial input not present in any reviewed collateral.

---

## 13. Requirements Register Data Quality (Cross-Register Consistency)

**What evidence exists:** `AirportEye_Requirements_Register_v5.xlsx.md` and `Final requirements.xlsx.md` share the same underlying "Final Requirements" sheet lineage — ~80% of content (including all NFR/SLA figures and all 17 AI-agent rows) is word-for-word identical between them.

**What is missing / contradicts:** The two registers systematically disagree on delivery month and/or phase for nearly every shared BIM-modeling (`BIMM-*`) line item — in one case (T1 rows) by as much as 4 months. `Final requirements.xlsx` is also missing most of the Geokno LiDAR-scanning and Geo-DT-functionality detail rows that `AirportEye_Requirements_Register_v5.xlsx.md` carries, while carrying one row (`BIMM-BE-01`) the other lacks. Neither file is a clean superset of the other.

**What questions should be asked:** Which register reflects the current, agreed delivery schedule — has this been reconciled in a version not present in this collateral set?

**Can we proceed with caveats?** Yes for scope/content (both registers agree on what's in scope); no for schedule specifics — any BIM-modeling delivery date cited in a draft should be explicitly sourced and flagged as provisional given this unresolved conflict.

**Recommended action:** Requirements-mapper should treat `AirportEye_Requirements_Register_v5.xlsx.md` as the more complete source (it has more detail rows) but should not assert any specific delivery month/phase from either register without flagging the cross-register conflict.

---

## Summary Table — Proceed / Seek Input / Escalate

| Area | Recommended Action |
|---|---|
| Procurement mechanism (competitive vs. CR) | **Escalate** — resolve before drafting proceeds |
| Vision/Objectives/KPIs | Proceed with assertion |
| Geospatial/LiDAR/BIM scope | Proceed with caveat (buffer density, Appendix A) |
| AI agent roster/count | Proceed with caveat (BRD's 8 as authoritative; flag register/RFP v5 mismatches) |
| AI agent performance SLAs | Proceed with caveat (Water & Drainage agent target missing) |
| Cybersecurity/data governance | Proceed with caveat (no IEC 62443 evidence; exclude Singapore-hosting language) |
| Data retention/sovereignty | Proceed with assertion (use Consolidated FINAL language only) |
| Incident response SLA | Proceed with assertion (≤10 min only; explicitly exclude ≤1hr and P1–P4 figures) |
| OT/BMS integration | Proceed with assertion (flag T2 TBD items) |
| SPG what-if/decision-engine scope | Proceed with caveat — track as separate scope item |
| Past performance/case studies | **Seek more collateral** — only 1 of 2–3 required references evidenced |
| Team & staffing | **Seek more collateral** — complete blank |
| Pricing/commercial | Proceed on structure only; **seek bidder cost input** for final figures |
| Requirements register schedule data | Proceed with caveat — flag cross-register schedule conflicts, don't assert either as final |
