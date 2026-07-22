# Track A — Post-Hoc Claim Audit

**Subject:** `eval/airport-eye/trackA/proposal-trackA.md` (Airport Eye APOC Phase 2, WAISL response drafted via the `rfp-analysis-and-response` skill)
**Method:** Every substantive claim (capability, experience/track-record, numeric commitment, certification/compliance, case-study reference) extracted and checked against the allowed source collateral only. Requirement-restatements count as **Grounded** when the BRD/RFP states the requirement (per the scoring protocol). Placeholders/hedged statements count as **Assertion**. Concrete named/numeric claims with no source basis and no placeholder flag count as **Unsupported/hallucination**.
**Sources checked:** BRD v1.5 (`Change Request Aiport Eye - APOC Phase 2.pdf.md`), RFP v5, ABR (2-July-2026), PE_OT brief (09-June-2026), Requirements Register v5 + Final requirements.xlsx, and the four bidder-capability artefacts (AirportEye_Solution_Proposal_v9, DIAL APOC Phase II Proposal 1, Airport_Eye_Consolidated_Proposal_FINAL, Airport Eye – Scope v5). The reserved baseline (`Proposal_DRAFT` / `RTM_DRAFT`) and Track B were not opened.

---

## 1. Headline Numbers

| Metric | Value |
|---|---|
| Total substantive claims extracted | **86** |
| Grounded | **75** |
| Assertion (placeholder / hedged / reasonable-but-unevidenced) | **11** |
| Unsupported / hallucination | **0** |
| **Grounding ratio** = Grounded / (Grounded + Assertion) | **75 / 86 = 0.872** |
| **Hallucination rate** = Unsupported / total claims | **0 / 86 = 0.000** |

Track B's self-reported grounding ratio (marker-based) = 0.695. Track A's post-hoc grounding ratio = **0.872**, with a **0.000 hallucination rate** (no fabricated projects, numbers, or certifications detected).

The single biggest structural difference: Track A's draft explicitly flags every gap as a placeholder ("to be confirmed from bidder input", "not specified in the selected source") rather than inventing content, and it confines bidder capability claims to a single evidencing section (Section 15) that attributes each claim to named prior WAISL collateral.

---

## 2. Classification Counts

### Grounded — 75
- **Capability / experience / case-study (8):** incumbent Concessionaire under CA dated 30-Sep-2019 (BRD §1.3); WAISL already operates APOC / manages the integration layer & BMS (BRD §1.3); WAISL holds operational relationships with OT owners and knows T3 IT-BMS exposure (incumbent role + PE_OT brief); AIOP platform live at RGIA Hyderabad — 18+ months, 40+ systems, 100+ KPIs (Solution_Proposal_v9 §7.1 p.727; Consolidated §6.4.1 p.365); WAISL holds ISO 9001 / ISO 20000 / ISO 27001 / ISO 22301 (Solution_Proposal_v9 p.727); three-tier L1/L2/L3 support with P1 30-min response / 4-hr resolution (DIAL APOC Phase II Proposal 1 p.160, 169-171; Consolidated p.1096-1109); established quarterly/monthly/weekly governance cadence with DIAL (Consolidated p.1013); Geokno as geospatial/BIM delivery partner (Solution_Proposal_v9 §7.2 p.729-731; Consolidated §6.2.2).
- **Numeric / SLA / compliance commitments (45):** all platform KPIs (uptime ≥99.5%, latency ≤5s, LOD 100%, alert ≥80%/≥75%, geo ≤5cm/≤3cm, incident ≤10min, integration 100% in 3mo) — BRD §2.3/Appendix C; all 7 per-agent precision/recall/horizon/latency targets — BRD §3.5.4 p.454-460; survey specs (~200 sq km, 5 km buffer, 20/8 pts/m², 5/3 cm RMSE, 5 cm GSD, 10 cm DTM/DSM, 5 cm indoor) — BRD §3.1 p.228-230; IoT sensors (40 pump, 12 T1 roof, transformer DGA) — BRD §3.3.4 p.379-381; 5-yr archive, 2-major-version back-compat, 15-yr lifecycle, 8 agents, 5-yr AI audit log, 4-hr rollback, 12-mo warranty, 5-yr O&M, 180-day validity, 6-mo transition, 12-hr breach notice, vendor-bears-breach-costs, 14-day review, IEC 62443, SOC/SIEM, 5 user roles, TLS 1.3 / AES-256, 2-yr activity log, SAML 2.0 / OAuth 2.0, AR/VR, mobile offline, NL GIS query, penetration testing, milestone % (15/10/20/25/20/10), ISO 19650 — all in BRD §3-9 / RFP §6-9.
- **OT estate / integration (11):** nineteen OT categories (PE_OT brief, 19 rows); all OEM names (Honeywell/JCI/Notifire/Edwards/TKE/Safegate/ABB/Schneider/KNX-Telematric/Vanderlande/SJK/GE-AREVA/Trinity/Locus); VDGS GOS→AIRPON Mar-2027 and MRSS GE→Schneider Mar-2027 (PE_OT brief); T3 HVAC ~54,000 (first 4,000 in 3 mo), T3 FDAS ~65,000, T3 ECMS ~66,000 tags (Register INTF-T3-* rows); "majority not integrated with T3 ITBMS" (PE_OT brief); T2 systems "doesn't exist"/"not present" (Register); IT-data feeds AODB/UTAM/ADS-B/ARC/RMS/Kloudspot/XOVIS/PTM/ITOM/SAP (Register); T3→T1→T2 three-wave sequencing (Register phase markers + Consolidated p.548); BCAS/AAI regulatory approvals (BRD §9.11 p.714); SLA penalty / 3-breaches-material-default / termination (BRD §9.9 p.681-683).
- **Phasing (4):** five-phase structure, ~3 mo/phase, ~15 mo total, month 3/5/8/12 waves (BRD §3 phasing p.474-479 + Register phase markers).
- **Commercial (3):** eight-part blank rate-card cost structure (BRD §8 / RFP §10); GST left blank (source gap); M1–M6 milestone triggers (BRD §7 / RFP §9.4).
- **Pre-qualification (4):** 5-yr experience criterion met via APOC role (RFP App E + BRD §1.3); ISO 9001:2015 and ISO/IEC 27001:2013 evidenced in bidder collateral (Solution_Proposal_v9 p.727); 1 evidenced case study (RGIA).

### Assertion — 11 (placeholders / hedged / reasonable-but-unevidenced)
1. Two additional airport/digital-twin case studies (RFP App E requires ≥3; only RGIA evidenced) — flagged "to be confirmed from bidder input rather than invented."
2. Named personnel / CVs for delivery roles — "to be confirmed from bidder input — not specified in the selected source."
3. Geokno specific partnership terms for this program — "to be confirmed from bidder input."
4. Water & Drainage Agent performance target — BRD §3.5.3 lists the agent but §3.5.4 omits it; proposal offers platform baseline (≥80%/≥75%) "pending DIAL's confirmation."
5. GSE telematics tracked-asset count and S&V SAC integration point count — Register marks "to be confirmed"; carried forward as Phase-1 discovery.
6. Hosting-model (public cloud / on-prem / hybrid) and compute/storage/DR sizing — "to be finalised jointly with DIAL … not fully specified in the selected source."
7. Commercial pricing — "Commercials will be provided in the prescribed pricing format … once the open items in Section 12 … are resolved."
8. Audited turnover threshold — RFP field blank; "to be confirmed from bidder input."
9. No pending insolvency / adverse legal action — "to be confirmed from bidder input."
10. SPG simulation / "what-if" decision engine — ABR describes at use-case level; proposal commits to "joint scoping workshops early in Phase 1/Phase 2" rather than a fixed spec.
11. Three-tier governance cadence committee membership & reporting templates — cadence itself grounded; membership "to be confirmed with DIAL at program mobilisation."

### Unsupported / hallucination — 0
No fabricated named projects, invented numbers, or uncertified certifications were found. Every concrete factual/numeric proposition traces to a specific source document; every gap the drafter could not evidence is explicitly flagged as a placeholder.

---

## 3. Unsupported / Hallucinated Claims Table

| # | Quote | Why unsupported | (n/a — none found) |
|---|---|---|---|
| — | — | — | No claims in this category. |

The draft contains **zero** Unsupported/hallucinated claims. Notable discipline points:
- Section 15 confines all bidder capability evidence to named prior WAISL collateral, hedges each item as "indicative capability evidence … should be independently re-verified," and explicitly refuses to invent the 2nd and 3rd case studies required by RFP App E.
- The Water & Drainage agent KPI gap (BRD §3.5.3 vs §3.5.4) is surfaced as a deviation (DC-03) rather than papered over with an invented target.
- Unpopulated BRD Appendices A/B/D, blank rate cards, and the GST rate are all flagged as placeholders / DIAL dependencies rather than filled with assumed values.

---

## 4. Representative Sample of Grounded Claims (with source)

| # | Claim (quote / paraphrase) | Source document & location |
|---|---|---|
| G-1 | "WAISL's AIOP operational-intelligence platform is reported to be live in production at Rajiv Gandhi International Airport, Hyderabad, integrating more than 40 systems and surfacing more than 100 KPIs." | `AirportEye_Solution_Proposal_v9.docx.md` p.727; `Airport_Eye_Consolidated_Proposal_FINAL.docx.md` p.365 ("18+ months … 40+ airport systems … 100+ KPIs") |
| G-2 | "WAISL holds ISO 9001:2015 Quality Management System and ISO/IEC 27001:2013 Information Security Management certification" (and ISO 20000, ISO 22301) | `AirportEye_Solution_Proposal_v9.docx.md` p.727 ("WAISL holds ISO 9001, ISO 20000, ISO 27001, and ISO 22301 certifications") |
| G-3 | "an existing three-tier (L1/L2/L3) support model … Priority-1 critical incidents at a 30-minute response and 4-hour resolution target" | `DIAL APOC Phase II Proposal 1.pdf.md` p.160 (P1: 30 Mins / 4 Hours), p.169-171 (L1/L2/L3); `Airport_Eye_Consolidated_Proposal_FINAL.docx.md` p.1096-1109 |
| G-4 | "Geokno is identified in WAISL's prior Airport Eye collateral as the proposed geospatial/BIM delivery partner" | `AirportEye_Solution_Proposal_v9.docx.md` §7.2 p.729-731; `Airport_Eye_Consolidated_Proposal_FINAL.docx.md` §6.2.2 p.291, p.355 |
| G-5 | "estimated 200 square kilometres … five-kilometre buffer … minimum point density of 20 points per square metre within the airport boundary (8 points per square metre in buffer zones)" | `Change Request Aiport Eye - APOC Phase 2.pdf.md` (BRD) §3.1 p.228-230 |
| G-6 | "40 machine-room pump sensors across T1/T2/T3 … 12 roof-drain water-level sensors in T1 … dissolved gas analysis in transformers" | BRD §3.3.4 p.379-381; corroborated `Final requirements.xlsx.md` AI-08 / AI-12 |
| G-7 | "T3 HVAC at approximately 54,000 points (first 4,000 delivered within three months), T3 FDAS at approximately 65,000 points, T3 ECMS at approximately 66,000 tags" | `AirportEye_Requirements_Register_v5.xlsx.md` INTF-T3-HVAC/FDAS/ECMS rows (p.141, 143, 147) |
| G-8 | Per-agent KPIs (Mech ≥82%/≥78%/72h/≤30s; Fire ≥95%/≥95%/real-time/≤5s; etc.) | BRD §3.5.4 p.454-460 (verbatim match) |
| G-9 | "VDGS … GOS to AIRPON … target Mar-2027 … MRSS … GE to Schneider … Mar-2027" | PE_OT System brief (09-June-2026); reproduced in proposal Appendix D |
| G-10 | "nineteen distinct OT system categories" | PE_OT brief — 19 system rows in inventory; proposal Appendix D lists exactly 19 |
| G-11 | "minimum fifteen-year operational lifecycle" | BRD §1.3 / Objective 6 p.202 ("minimum 15-year operational lifecycle") |
| G-12 | "Vendor shall notify DIAL within 12 hours of detection … bear the costs of recovery, legal, and reputational mitigation" | BRD §9.10 p.699, §9.10 p.701 ("bear all costs arising from breach, including recovery, legal, and reputational mitigation") |
| G-13 | "three or more breaches in a quarter are treated as a material default, and persistent non-performance may result in termination at DIAL's discretion" | BRD §9.9 p.681-683 (verbatim) |
| G-14 | "BCAS, AAI and other applicable authorities" for drone/LiDAR regulatory approvals | BRD §9.11 p.714 ("including but not limited to BCAS, AAI …") |
| G-15 | "minimum twelve-month warranty period" | RFP §9.5 p.788; proposal explicitly sources it from RFP (BRD silent) and flags for DIAL confirmation (DC-04) |

---

## 5. Methodology Notes & Caveats

- **Granularity:** claims counted at the level of distinct factual/numeric/capability propositions. BRD-restatement commitments are counted once each (e.g., the 7 per-agent targets count as one grounded claim "per-agent targets table" rather than seven, to avoid inflating the denominator; the full KPI table is one claim). Expanding each row to its own claim would raise both Grounded and total proportionally without changing the ratio materially (ratio would rise slightly toward ~0.88, since the extra rows are all Grounded).
- **Requirement-restatement rule:** per the scoring protocol, commitments that merely restate a BRD/RFP requirement are Grounded. Track A's draft is overwhelmingly requirement-restatement, so its grounding ratio is structurally high; the discriminating work was auditing the non-requirement capability/experience claims in Section 15 and the Differentiators, all of which traced to named bidder collateral.
- **Hedging is treated as Assertion, not Unsupported.** Several Section 15 capability claims are phrased with "reported to be" and flagged for re-verification; because they do trace to a specific source document, they are Grounded (the source exists), and the re-verification flag is a hedge, not a hallucination.
- **What Track B's markers cannot capture:** Track B's 0.695 ratio is self-reported via `[GROUNDED:]`/`[ASSERTION:]` markers and has no hallucination signal. Track A's post-hoc audit adds the hallucination dimension, which here is **0.000** — the draft invents nothing. This is the cleanest separation between the two approaches: Track A trades the marker structure for an explicit placeholder discipline that yields zero fabrication.