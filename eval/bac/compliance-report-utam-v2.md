# BAC Underwing Analytics — Compliance Report: UTAM Solution Architecture v2

**Skill:** compliance-validator (12-step process)
**Target artefact (non-binding collateral):** `sources/BAC/UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v2.docx.md` (referred to below as "UTAM v2"; line numbers are from this `.md` file)
**Binding sources:** `sources/BAC/BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md` + `sources/BAC/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md` (Tab F governs the actual response; UTAM v2 is collateral that feeds it)
**Requirements denominator (reused):** `eval/bac/gold-requirements.md` — 275 total / **269 mandatory** (Submission 17, Content 23, Functional 69-mandatory, Non-Functional 48, Project-Management 19-mandatory, ISRA 29, Procedural/Contractual 35, Numeric 29). Optional 6 not in denominator.
**v1 for diffing:** `sources/BAC/UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`

**Framing applied throughout:** UTAM v2 is NON-BINDING collateral. It *describes* the solution architecture; the binding response goes in Response Sheet Tab F. Requirements that belong in the response sheet / pricing / commercial submission / declarations (insurance $, 90-day validity, addenda, COI, Social Procurement/Supply Nation/Modern Slavery, pricing structure, page limits, deadline, referees, certificates, bios) are flagged **N/A-collateral** ("Belongs in response sheet, not collateral") and are NOT counted as Fail. The capability-vs-commitment test is applied to every functional/NF/ISRA architectural claim.

---

## 1. Summary

**Mandatory denominator checked: 269** (across 8 categories). Verdict distribution across the 269:

| Verdict | Count | Notes |
|---|---|---|
| **Pass** | 62 | Architecture described AND a measurable commitment given (e.g., RTO ≤4h, RPO <2h, 99.9% availability, RBAC/SSO/SAML/OIDC, connectors, audit/lineage, encryption AES256/TLS1.2) |
| **Partial — capability described, delivery not committed** | 118 | Platform describes the capability in narrative/component form but gives no per-requirement acceptance threshold (the dominant pattern for FR17/20/23/24/25/26/28/34/35/37/38/49-53/68-71 and many NF rows) |
| **Fail (in-scope, mandatory)** | 9 | NF19/NF20 Sev-1/2/3 response+resolution SLA matrix (7 numeric rows) + NF17 24/7/365 phone/email/online support + NF03 live-data refresh frequency |
| **Ambiguous** | 4 | NF05 3-yr availability history (no figure in collateral), NF18 local representative, FR72/FR73 Phase-2 items mentioned only generically |
| **Over-claim** | 6 | Section headers asserting "NF19, NF20 addressed" (line 831) with no SLA matrix; "FR01-FR71 (all applicable)" claim at line 171; "fully compliant with the Data Protection Regulation" (line 1067) while citing wrong (GDPR) framework; "European Union (AP) data centres" (line 1015) |
| **N/A-collateral** | 70 | Belong in response sheet / pricing / commercial / declarations, NOT a solution-architecture document (see §8 sub-table) |

**Pre-flight status: BLOCKING.** 9 mandatory in-scope architectural requirements fail (the entire NF19/NF20 severity-tier SLA set plus NF17 support coverage), plus the document carries residual EU/GDPR/Hellenic/EEA/NIS2 cross-contamination that makes its data-protection/sovereignty framing non-credible for a Brisbane/Australia procurement. The collateral must not be used to substantiate Tab F NF19/NF20/NF17/NF03 or any ISRA data-sovereignty/privacy row until those are fixed.

**Blocking-issue count: 9 mandatory in-scope fails + 1 cross-contamination block (material to ISRA-09/19/21/23/24 and the data-protection narrative).**

---

## 2. Blocking Issues

**BLOCKING — 9 mandatory in-scope requirements not met by UTAM v2:**

1. **NF19 / N-9 — Severity 1 response ≤1 hour, 24x7x365.** UTAM v2 §10 "Operational & Support Commitments" (lines 829-836) only commits that "BAC will be notified within 1 hour of a confirmed security incident" (line 835). That is a *security-incident notification* target, not the Sev-1 support *response* SLA. No Sev-1 response-time commitment is stated. The section header at line 831 asserts "NF19, NF20" are addressed — this is an over-claim.
2. **NF19 / N-10 — Severity 1 resolution/plan ≤4 hours business day.** Not stated. Fail.
3. **NF19 / N-11 — Severity 2 response ≤4h business day.** Not stated. Fail.
4. **NF19 / N-12 — Severity 2 response ≤8h non-business day.** Not stated. Fail.
5. **NF19 / N-13 — Severity 2 resolution/plan ≤4h business day.** Not stated. Fail.
6. **NF19 / N-14 — Severity 3 response ≤8h.** Not stated. Fail.
7. **NF20 / N-15 — Severity 3 resolution/plan ≤8h business day.** Not stated. Fail.
8. **NF17 — 24/7/365 user support via phone, email, online help; update help on new features.** v2 mentions "24×7 operations" only for *availability* (line 758). No 24/7/365 *support channel* commitment (phone/email/online help) appears. Fail.
9. **NF03 — Live data 24/7/365; state refresh frequency.** v2 asserts live operational data but gives no refresh-frequency figure; Partial-to-Fail — treated as Fail on the refresh-frequency limb.

**Cross-contamination block (material to ISRA rows 9, 19, 21, 23, 24 and the whole §12 data-protection narrative):** UTAM v2 frames data protection in EU terms (GDPR Arts. 5-6, 44-49; EEA; NIS2; "Hellenic Data Protection Authority"; "European Union (AP) data centres") that are wrong for a Brisbane/Australia procurement. The correct frame is the Privacy Act 1988 / Australian Privacy Principles (APPs), the Office of the Australian Information Commissioner (OAIC), ASD Essential 8, and Australian/AP data residency. Until this is corrected, the ISRA data-sovereignty / privacy / breach-notification / BCM-geographical-address responses cannot be credibly substantiated from this collateral. See §3.

---

## 3. v2-Specific Cross-Contamination Findings (headline v2 finding)

Scan of the entire v2 document for GDPR / EEA / European Union / Hellenic / NIS2 / AIA / Athens / Eurocontrol. v2 has been edited to add Brisbane-specific sections (§5.8, §8) and to swap "AIA"→"BAC", "EU region"→"AP region" in several places — but the GDPR/EEA/Hellenic/NIS2 framing was *not* removed. In some spots the find-and-replace was applied only partially, producing internally-contradictory edit artefacts. Findings, exact quotes, line numbers, and correct framing:

| # | v2 line | Exact quote (or key fragment) | Defect | Correct Brisbane/Australia framing |
|---|---|---|---|---|
| CC-1 | 1015 | "All BAC data is hosted exclusively within **European Union (AP) data centres**, and no transfer or access outside the AP is permitted" | **Internally contradictory edit artefact.** "European Union" and "AP" (Asia-Pacific) are mutually exclusive. A botched s/EU/AP/ left "European Union" in place. This is the single most damaging contamination line. | "hosted exclusively within Australian (AP) data centres" — Privacy Act 1988 / APPs / OAIC; AWS ap-southeast-2 (Sydney) region |
| CC-2 | 1049 | "No data is transferred or processed outside the **EEA**. All data is hosted and processed exclusively within AP data centers; therefore, **GDPR Articles 44 et seq.** are not applicable" | Contradiction: EEA is the European Economic Area; "AP data centers" are not in the EEA. GDPR Chapter V (Arts 44-49) governs EU cross-border transfers and is irrelevant to an Australian deployment. | "No data is transferred outside Australia. All data is hosted in AWS ap-southeast-2 (Sydney). Australian Privacy Principle 8 / APP 11 cross-border disclosure rules apply." |
| CC-3 | 360 | "AWS AP region deployment is used to satisfy data residency requirements under **GDPR and NIS2**. All data remains within the AP regulatory boundary" | Wrong regulatory frame. GDPR (EU) and NIS2 (EU critical-infrastructure directive) do not apply to a Brisbane Airport procurement. "AP regulatory boundary" is not an EU concept — internally inconsistent. | "AWS ap-southeast-2 deployment satisfies Australian data residency under the Privacy Act 1988 / APPs and BAC data-sovereignty requirements. ASD Essential 8 alignment." |
| CC-4 | 729 | "Supplying any other information requested by BAC or the **Hellenic Data Protection Authority** to complete the DPIA." | Greece's data protection authority is wrong for Brisbane. (Carried unchanged from v1 line 556.) | "…or the Office of the Australian Information Commissioner (OAIC) to complete the DPIA." |
| CC-5 | 1067 | "The proposed TurnWise solution is fully compliant with the **Data Protection Regulation**… in accordance with **GDPR Articles 5 and 6**… full compliance with **GDPR data residency and cross-border transfer restrictions under Articles 44–49**." | "Fully compliant" over-claim against the wrong regulation. GDPR Arts 5/6/44-49 are EU law. | "…compliant with the Privacy Act 1988 and the Australian Privacy Principles (APPs)…" — replace all GDPR article references with APP equivalents. |
| CC-6 | 1025 | "privacy and data protection framework aligned with applicable data protection regulations, including **GDPR**" | Should name the Australian framework first. | "…including the Privacy Act 1988 (Cth) and the Australian Privacy Principles, with GDPR alignment only where EU data is processed." |
| CC-7 | 1043 | "security controls aligned with **GDPR requirements**" | Wrong primary frame for hosting-security controls. | "…aligned with ASD Essential 8, ISO 27001, and the Privacy Act 1988 / APPs." |
| CC-8 | 848 | "personal and regulated data is consistently identified and protected in line with **GDPR expectations**" | Wrong frame. | "…in line with the Australian Privacy Principles (APP 11) and OAIC guidance." |
| CC-9 | 591 | "All processing adheres to privacy regulations (e.g., **GDPR**, HIPAA where applicable)" | GDPR listed as the default privacy regime. | Replace primary citation with Privacy Act 1988 / APPs. |
| CC-10 | 596 | "Cleansing operates under **GDPR‑aligned policies** with minimization, masking, tokenization" | GDPR-aligned. | "APP-aligned policies" (APP 10/11). |
| CC-11 | 600 | "Compliance (e.g., **GDPR**) and security/privacy are embedded end-to-end" | GDPR cited as the exemplar compliance frame. | Cite Privacy Act / APPs / ASD Essential 8. |
| CC-12 | 609 | "**GDPR-ready** controls such as minimization, retention, lawful basis support" | "Lawful basis" is a GDPR concept; APPs use "permitted purpose / APP 6". | "APP-ready controls such as minimisation, retention, and purpose limitation." |
| CC-13 | 631 | "privacy controls (masking/redaction and **GDPR-aligned safeguards**)" | GDPR-aligned. | APP-aligned. |
| CC-14 | 665 | "**GDPR transparency:** Data subject access requests and right-to-erasure processes" | "Data subject" / "right to erasure" are GDPR terms. | "APP 12/13: access and correction requests; APP 11 security; OAIC-aligned." |
| CC-15 | 1061 | "Data Subject Requests are handled through a documented **GDPR compliant procedure**" | GDPR-compliant. | "APP-compliant procedure." |
| CC-16 | 1017 (section title) | "# Security Compliance" | v2 *renamed* this section from v1's "# GDPR Compliance" (v1 line 834) — good direction — **but the body (lines 1021-1067) is still entirely GDPR-framed.** The rename is cosmetic. | Rewrite the section body around the Privacy Act / APPs / OAIC. |

**Net assessment:** v2 made a cosmetic pass at de-EU-ing the document (renamed §12, swapped AIA→BAC, swapped "EU region"→"AP region" in the deployment table) but left the GDPR/EEA/NIS2/Hellenic *substance* in place, and in three places (lines 1015, 1049, 360) produced internally-contradictory text by substituting "AP" next to retained EU terms. This is the highest-priority v2 defect class: an evaluator reading §11.13/§12 would immediately flag a Brisbane/Australia procurement that cites GDPR Articles 44-49, the EEA, and the Hellenic DPA.

---

## 4. What v2 Changed vs v1

### (a) What v2 FIXED (gaps closed / contamination removed / commitments added)

- **AIA → BAC / Brisbane renaming.** "Should AIA prefer" → "Should BAC prefer" (v1 line 143 → v2 line 155); "AIA selects" → "BAC selects" (v1 line 526 → v2 line 695/801); "Athens International Airport (AIA)" → "Brisbane International Airport (BAC)" (v1 line 832 → v2 line 1015); "Athens Airport needs" → "Brisbane Airport needs" (v1 line 194 → v2 line 220); "AIA's data centre" → "BAC's data centre" (v1 line 526 → v2 line 695); "AIA's security team" → "BAC's security team" (v1 line 527 → v2 line 696/802); "AIA's INFOSEC" → "BAC's INFOSEC" (v1 line 544 → v2 line 717).
- **Eurocontrol NM removed.** v1's "NM Message Service… Eurocontrol NM… CTOT, ATFM regulations, TOBT, TSAT" (v1 lines 176, 920) is gone; v2 replaces it with a generic "Network Manager Messaging Services" (v2 line 213) that no longer asserts Eurocontrol NM compliance. Good — that contamination is removed.
- **Section rename §12 "GDPR Compliance" → "Security Compliance"** (v1 line 834 → v2 line 1017). Cosmetic but directionally correct.
- **New Brisbane-specific sections added:** §5.8 "Penetration Testing Alignment with Brisbane Plan" (v2 line 699-705), §8 "Brisbane IT&T Enterprise Architecture Standards" (v2 line 805), §5.10 "Brisbane INFOSEC Policies & Right to Pen Test" (v2 line 713-718). These add genuinely Brisbane-framed commitments (predelivery pen test, retest-until-closure, BAC right-to-pen-test).
- **RPO made concrete.** v1 "< Near zero" (v1 line 587) → v2 "< 2 hours" (v2 line 760). A measurable commitment was added. (Note RTO relaxed from "≤40 mins" to "≤4 hours" — see (c).)
- **Connectors / data-architecture expanded.** v2 adds a full connectors table (v2 lines 374-382) and per-connector detail (lines 385-481) that v1 left as empty headings (v1 lines 321-325). This substantiates FR54/FR55/NF15/NF16.
- **Data Quality / Governance / Modelling / Exchange sections expanded** (v2 lines 571-639) — adds substantive architecture for FR57/FR58/NF02/NF45/NF46.
- **Mermaid architecture diagram added** (v2 lines 1076-1135) — v1 had a diagram block too (v1 lines 890-957) but v2's is cleaner.
- **"Sustainability & General Information" section removed** (v1 lines 870-880 had a sustainability section referencing "AIA's environmental commitments"; gone in v2). Reasonable removal for a focused architecture doc.
- **TETRA radio / Voice notification removed** (v1 line 264 "TETRA radio network"; v1 line 264 "Voice") → v2 line 311 "SMS, Email". TETRA is an EU/airport-emergency frame; removing it is fine.

### (b) What v2 did NOT fix (residual issues carried from v1)

- **GDPR framing throughout the data-protection narrative.** v1 had GDPR throughout (v1 lines 431, 435, 444, 466, 507-508, 838, 850, 854, 868); v2 retains it (v2 lines 591, 596, 600, 609, 631, 665, 848, 1025, 1043, 1049, 1061, 1067). The rename of §12's title did not propagate to the body.
- **Hellenic Data Protection Authority** (v1 line 556 → v2 line 729). Carried verbatim.
- **EEA reference** (v1 line 854 → v2 line 1049). Carried — and made contradictory by the AP swap.
- **NIS2 reference** (v1 line 313 → v2 line 360). Carried — and made contradictory by the AP swap.
- **NF19/NF20 Sev-1/2/3 SLA matrix not committed.** v1 also only had "AIA will be notified within 1 hour of a confirmed security incident" (v1 line 656). v2 carries the same single line (v2 line 835) and still claims NF19/NF20 in the section header. Not fixed.
- **No per-class precision/recall for FR17 GSE classification or FR20 personnel detection.** v1 had none; v2 still has none (only generic "object detection" at v2 line 175-176, 450-453). Not fixed.
- **No deviation register** (neither v1 nor v2 has one). Not fixed.
- **RPO/RTO still reference "AIA's business continuity requirements" in v1 line 582** — v2 line 755 fixes to "BAC's", good. But see (c).

### (c) What v2 made WORSE or newly introduced

- **Line 1015 "European Union (AP) data centres"** — NEW internally-contradictory artefact. v1 line 832 cleanly said "European Union (EU) data centres" (wrong but self-consistent). v2 changed "EU"→"AP" inside the sentence but left "European Union", producing the nonsensical "European Union (AP)". This is the most damaging line in the document because it is simultaneously the data-sovereignty commitment AND internally inconsistent.
- **Line 1049 "outside the EEA… within AP data centers"** — NEW contradiction. v1 line 854 said "outside the EEA… within EU data centers" (self-consistent, wrong). v2 swapped "EU"→"AP" but left "EEA", so the sentence now asserts data is both "not outside the EEA" and "within AP" — impossible.
- **Line 360 "GDPR and NIS2… within the AP regulatory boundary"** — NEW contradiction. v1 line 313 said "GDPR and NIS2… within the EU regulatory boundary" (self-consistent, wrong). v2 swapped "EU"→"AP" but left "GDPR and NIS2", so the sentence invokes EU directives to justify an AP-boundary claim.
- **RTO relaxed.** v1 "<= 40 mins" (v1 line 586) → v2 "<= 4 hours" (v2 line 759). This still meets the binding ≤4h (N-7), so it is not a compliance fail, but v2 is *less* ambitious than v1 on RTO. Worth noting because the edit moves v2 from over-delivery to exactly-the-binding.
- **"Edge Layer - Airport Systems and Pre-processing" line 171 over-claim:** v2 line 171 states "Requirements addressed in this section: FR01-FR71 (all applicable), NF01-NF48". This is a broader, less credible over-claim than v1's component-level TRQ tags — v2 now claims *every* FR and *every* NF is addressed by the Edge Layer, which is self-evidently false (the Edge Layer does not address FR60-67 admin/RBAC or NF19 SLA matrix). This is a new over-claim class.

---

## 5. Numeric Requirements Inventory + Parity Table

29 numerics from `gold-requirements.md` §8. "Commercial" = belongs in response sheet/pricing/declarations (N/A-collateral). "Architectural" = in scope for a solution-architecture document.

| ID | Parameter | Binding value | Op | UTAM v2 value | v2 line | Verdict | Delta / note |
|---|---|---|---|---|---|---|---|
| N-1 | Public Liability insurance | $20,000,000 AUD | ≥ | — | — | **N/A-collateral** | Commercial; response sheet C-10 / P-2 |
| N-2 | Professional Indemnity | $10,000,000 AUD | ≥ | — | — | **N/A-collateral** | Commercial; P-3 |
| N-3 | Cyber Security insurance | $10,000,000 AUD | ≥ | — | — | **N/A-collateral** | Commercial; P-4 |
| N-4 | Initial contract term | 3 years | = | — | — | **N/A-collateral** | Commercial; P-7 |
| N-5 | Extensions | 2 × 1-year | = | — | — | **N/A-collateral** | Commercial; P-8 |
| N-6 | Proposal validity | 90 calendar days | ≥ | — | — | **N/A-collateral** | Commercial; P-15 / S-15 |
| N-7 | RTO | 4 hours | ≤ | <= 4 hours | 759 | **Pass** | Meets binding exactly (relaxed from v1's 40 min). |
| N-8 | RPO | All data incl. transactions recoverable | — | < 2 hours | 760 | **Pass** | Concrete numeric commitment; exceeds qualitative binding. |
| N-9 | Sev-1 response | 1 hour, 24x7x365 | ≤ | not stated (only "1h security-incident notification", line 835) | 835 | **Fail** | Security-incident notification ≠ Sev-1 support response. Undeclared shortfall. |
| N-10 | Sev-1 resolution/plan | 4 hours business day | ≤ | not stated | — | **Fail** | Undeclared shortfall. |
| N-11 | Sev-2 response (business) | 4 hours | ≤ | not stated | — | **Fail** | Undeclared shortfall. |
| N-12 | Sev-2 response (non-business) | 8 hours | ≤ | not stated | — | **Fail** | Undeclared shortfall. |
| N-13 | Sev-2 resolution/plan | 4 hours business day | ≤ | not stated | — | **Fail** | Undeclared shortfall. |
| N-14 | Sev-3 response | 8 hours | ≤ | not stated | — | **Fail** | Undeclared shortfall. |
| N-15 | Sev-3 resolution/plan | 8 hours business day | ≤ | not stated | — | **Fail** | Undeclared shortfall. |
| N-16 | Support coverage | 24/7/365 | = | "24×7 operations" (availability only, line 758); no 24/7/365 phone/email/online-help support commitment | 758, 829-836 | **Partial→Fail** | Availability 24×7 ≠ support 24/7/365. NF17 not met. |
| N-17 | Live data refresh | 24/7/365 | = | live operational data asserted; no refresh-frequency figure | 758 | **Partial** | 24/7 asserted; refresh frequency not quantified. |
| N-18 | Availability history | 3 years | = | not furnished | — | **N/A-collateral** | NF05 deliverable belongs in response sheet, not collateral. |
| N-19 | Additional supporting PDF | ≤5 pages | ≤ | — | — | **N/A-collateral** | Submission format; S-10. |
| N-20 | Queries deadline | 2 business days before close | ≥ | — | — | **N/A-collateral** | Procedural; S-16. |
| N-21 | Referees | ≥2 | ≥ | — | — | **N/A-collateral** | Response sheet C-17. |
| N-22 | Document review period | ≥5 business days | ≥ | — | — | **N/A-collateral** | PMR-06 process; response sheet/methodology. |
| N-23 | Defects liability | 6 months | = | not stated | — | **N/A-collateral** | PMR-10 (optional); belongs in response sheet. |
| N-24 | Lump-sum withheld until PC | 20% | = | — | — | **N/A-collateral** | PMR-09 commercial; response sheet. |
| N-25 | Pricing horizon | 5 years | = | — | — | **N/A-collateral** | Pricing schedule. |
| N-26 | RFP issue date | 15 June 2026 | = | — | — | **N/A-collateral** | Procedural. |
| N-27 | Closing date | 10 July 2026 | = | — | — | **N/A-collateral** | Procedural. |
| N-28 | Award date | 21 August 2026 | = | — | — | **N/A-collateral** | Procedural. |
| N-29 | Go-Live | 11 December 2026 | = | — | — | **N/A-collateral** | Procedural. |

**Architectural numeric score: 2 Pass (N-7, N-8), 1 Partial (N-17), 8 Fail (N-9…N-15 + N-16), 18 N/A-collateral.** The 8 architectural fails are all on the NF19/NF20/NF17/NF03 support-and-availability limb and are the blocking issues.

---

## 6. Capability-vs-Commitment / Over-Claim Findings

Applied to every functional/NF claim in v2. Headline items where the document *describes* a capability but does not *commit* to delivery with a measurable threshold, or asserts "Compliant"/"addressed" without substantiation:

| # | Req | v2 location | Descriptive text (quote) | Missing measurable commitment | Verdict |
|---|---|---|---|---|---|
| OC-1 | NF19/NF20 (Sev-1/2/3 SLA) | line 831 header; line 835 body | "Operational & Support Commitments… NF19, NF20"; "BAC will be notified within 1 hour of a confirmed security incident" | No Sev-1/2/3 response or resolution time matrix; "1h incident notification" is not the Sev-1 response SLA | **Over-claim + Fail** — header claims NF19/NF20 addressed; body delivers only incident notification |
| OC-2 | FR17 (GSE classification) | line 175-176, 450-453 | "computer vision models to extract structured metadata… object detection… Vehicle Detected" | No per-class precision/recall for the 11 GSE classes (baggage loaders, tugs, water, waste, stairs, catering, refuelling, GPUs/ACUs, tow bars/pushback, general support) | **Partial — capability described, delivery not committed** |
| OC-3 | FR18 (GSE arrival/departure timestamps) | line 175 | "Edge Vision Controller… Publishes events to the platform" | No timestamp-accuracy bound (e.g., ±N seconds) | Partial |
| OC-4 | FR20 (personnel presence) | line 450-453 | "Person Detected… Restricted Area Breach" | No detection-accuracy / false-positive-rate commitment | Partial |
| OC-5 | FR23 (PPE detection) | line 135 lists FR23; no dedicated body | Listed in "Requirements addressed" header only | No PPE-detection accuracy; gold notes "where camera quality allows" carve-out — not even acknowledged | Partial / Over-claim (header claim with no body) |
| OC-6 | FR24 (auto-detect start/end of 10 activities) | line 277 | "Turnaround activity monitoring — chocks-in/out, pushback tracking, timestamp logging" | Only 3 of 10 activities named (choking, aerobridge, GPU, baggage, catering, refuelling, pushback, stairs, cabin cleaning); no per-activity detection-accuracy | Partial |
| OC-7 | FR26 (confidence scores) | line 143 | "confidence scoring" mentioned | No confidence-threshold definition or minimum | Partial |
| OC-8 | FR28 / FR71 (continual improvement/learning) | line 145, 198, 777 | "continuous model improvement", "ML Ops platform is responsible for managing, improving" | No improvement-rate metric (e.g., accuracy lift per quarter) | Partial |
| OC-9 | FR69 (detection accuracy per model) | line 199 | "Versioned AI Models" | No per-model accuracy tracking metric stated | Partial |
| OC-10 | FR72/FR73 (Phase-2) | — | Not substantively addressed | Phase-2 airline integration / aerobridge pax counting / mobile+tablet remote access not described | Ambiguous/Partial |
| OC-11 | "FR01-FR71 (all applicable), NF01-NF48" | line 171 | Edge Layer claims to address all FRs and all NFs | Self-evidently false (Edge Layer does not address FR60-67 admin/RBAC or NF19 SLA matrix) | **Over-claim** |
| OC-12 | "fully compliant with the Data Protection Regulation" | line 1067 | "fully compliant… GDPR Articles 5 and 6… Articles 44–49" | Compliant with the *wrong* regulation; no APP mapping | **Over-claim** (see §3 CC-5) |
| OC-13 | "European Union (AP) data centres" | line 1015 | "hosted exclusively within European Union (AP) data centres" | Internally contradictory; no real sovereignty commitment | **Over-claim** (see §3 CC-1) |
| OC-14 | 99.9% availability | line 758 | "≥99.9% (24×7 operations)" | Measurable — Pass, but no measurement-window or exclusions stated | Pass (commit) — note "subject to" carve-outs absent, which is good |
| OC-15 | RTO/RPO | lines 759-760 | "<= 4 hours" / "< 2 hours" | Concrete numeric commitments | Pass (commit) |

---

## 7. Deviation-Register Completeness

**UTAM v2 contains no formal deviation register / departures document / assumptions-and-exclusions register.** This is expected (it is collateral, not the response), but it means **every below-binding architectural shortfall in v2 is an undeclared deviation** with respect to the collateral. The binding response-sheet departures obligation falls under S-13 / P-11 (suppliers must send a departures document with the response); that obligation itself is N/A-collateral and belongs in the response sheet.

**Undeclared architectural shortfalls found in v2 (must either be committed in the response-sheet Tab F with a deviation flag, or fixed in v3 of the collateral):**

1. N-9 Sev-1 response ≤1h — undeclared shortfall (only incident-notification 1h offered).
2. N-10 Sev-1 resolution ≤4h business day — undeclared shortfall.
3. N-11 Sev-2 response ≤4h business day — undeclared shortfall.
4. N-12 Sev-2 response ≤8h non-business day — undeclared shortfall.
5. N-13 Sev-2 resolution ≤4h business day — undeclared shortfall.
6. N-14 Sev-3 response ≤8h — undeclared shortfall.
7. N-15 Sev-3 resolution ≤8h business day — undeclared shortfall.
8. N-16/NF17 24/7/365 support channel — undeclared shortfall.
9. N-17/NF03 live-data refresh frequency — undeclared shortfall (no figure).
10. FR17 GSE per-class accuracy — undeclared (described only).
11. FR20 personnel detection accuracy — undeclared.
12. FR23 PPE detection — claimed in header, no body, no accuracy.
13. FR24 10-activity auto-detection — 3 of 10 named, no accuracy.
14. Cross-contamination: data-sovereignty / privacy framework cited against GDPR/EEA/Hellenic instead of Privacy Act/OAIC — material misfit that would undermine ISRA rows 9, 19, 21, 23, 24 if not corrected before Tab F is populated from this collateral.

---

## 8. Per-Requirement Validation Table

### 8a. In-scope architectural requirements (Functional / Non-Functional / ISRA / Project-Management-architectural)

Verdict legend: **Pass** = capability described + measurable commitment; **Partial-desc** = capability described, delivery not committed; **Fail** = in-scope mandatory, not met; **Over-claim** = asserts conformance without substantiation; **Amb** = ambiguous; **N/A-coll** = belongs in response sheet, not collateral (excluded from mandatory count).

#### Functional (FR01–FR73) — 69 mandatory + 4 optional

| ID | FR | Verdict | v2 evidence (line) | Note / remediation |
|---|---|---|---|---|
| SUB-F-01 | FR01 camera onboarding | Partial-desc | 171-178 edge layer | "vendor-agnostic onboarding" described; no BAC-supported-model list |
| SUB-F-02 | FR02 camera grouping | Partial-desc | 220 | "adapt the platform to Brisbane Airport needs (Location, Asset…)" |
| SUB-F-03 | FR03 FOV / parking zones | Partial-desc | 209 geo-fencing | Multi-level geo-fencing described; no FOV config detail |
| SUB-F-04 | FR04 geofenced operational zones | Pass | 209, 521-528 | Multi-level geo-fencing + role views |
| SUB-F-05 | FR05 live video ingest | Pass | 175, 379 | Vision Analytics Connector RTSP/ONVIF |
| SUB-F-06 | FR06 video buffering *(opt)* | Pass | 175 "buffering and retry mechanisms" | Optional; addressed |
| SUB-F-07 | FR07 configurable frame rates | Partial-desc | 175 | "lightweight pre-processing"; no frame-rate config |
| SUB-F-08 | FR08 timestamped frames | Partial-desc | 175 | "schema normalization"; no synchronised-airport-time-source detail |
| SUB-F-09 | FR09 monitor camera availability | Pass | 145, 175 | "tracking camera availability, video quality" |
| SUB-F-10 | FR10 occlusion/glare detection | Partial-desc | 145 | "video quality" generic; no occlusion/glare specific |
| SUB-F-11 | FR11 alerts for AI-accuracy degradation | Partial-desc | 145 | "AI model performance, confidence levels"; no threshold |
| SUB-F-12 | FR12 camera health dashboard *(opt)* | Partial-desc | 145 | Optional; implied via "system diagnostics" |
| SUB-F-13 | FR13 aircraft arrival / on-block | Pass | 137, 406-421 | ADS-B + AODB connectors |
| SUB-F-14 | FR14 aircraft departure / off-block | Pass | 137, 406-421 | ADS-B connector |
| SUB-F-15 | FR15 AIDX aircraft identity | Partial-desc | 376 AODB connector | AIDX not named; AODB only |
| SUB-F-16 | FR16 correlate with AODB flight info | Pass | 376, 391-399 | AODB connector |
| SUB-F-17 | FR17 GSE classification | **Partial-desc / Over-claim** | 175-176, 450-453 | Object detection described; **no per-class precision/recall for the 11 GSE classes** (OC-2) |
| SUB-F-18 | FR18 GSE timestamps | Partial-desc | 175 | No timestamp-accuracy bound (OC-3) |
| SUB-F-19 | FR19 track equipment presence | Pass | 277, 423-438 | Telematics connector |
| SUB-F-20 | FR20 personnel presence | **Partial-desc** | 450-453 | "Person Detected"; no accuracy/FP-rate (OC-4) |
| SUB-F-21 | FR21 restricted-zone entry | Pass | 451-453 | "Restricted Area Breach" |
| SUB-F-22 | FR22 unsafe dwell times (Pax) | Partial-desc | 176 | "dwell time" mentioned; no Pax-dwell threshold |
| SUB-F-23 | FR23 PPE detection | **Partial / Over-claim** | 135 header only | Listed in header; no body, no accuracy, no "where camera quality allows" carve-out (OC-5) |
| SUB-F-24 | FR24 auto-detect 10 activities | **Partial-desc** | 277 | Only chocks-in/out + pushback named (3 of 10); no per-activity accuracy (OC-6) |
| SUB-F-25 | FR25 single turnaround timeline | Pass | 137, 143 | "aircraft turnaround timelines" |
| SUB-F-26 | FR26 confidence scores | Partial-desc | 143 | "confidence scoring"; no threshold (OC-7) |
| SUB-F-27 | FR27 manual validation/correction | Partial-desc | 143 | Implied; no UI detail |
| SUB-F-28 | FR28 learn from corrections | Partial-desc | 145, 198, 777 | "continuous model improvement"; no metric (OC-8) |
| SUB-F-29 | FR29 airline-specific workflows | Pass | 146, 497-509 | Configurable workflows |
| SUB-F-30 | FR30 aircraft-type sequences | Partial-desc | 146 | Implied via parameterisation |
| SUB-F-31 | FR31 mandatory vs optional activities | Pass | 146 | "mandatory and optional milestones" |
| SUB-F-32 | FR32 dependencies/precedence | Partial-desc | 146 | "configurable business rules"; no precedence detail |
| SUB-F-33 | FR33 ingest planned times from AODB | Pass | 376, 393 | AODB Flight Schedule |
| SUB-F-34 | FR34 planned vs actual timestamps | Partial-desc | 143 | "planned versus actual performance analysis" |
| SUB-F-35 | FR35 delay attribution | Pass | 143 | "turnaround delay attribution" |
| SUB-F-36 | FR36 configurable tolerance thresholds | Pass | 507 | "threshold breaches… configurable" |
| SUB-F-37 | FR37 detect workflow deviations | Pass | 505-508 | Rules engine |
| SUB-F-38 | FR38 root-cause for missed SLAs | Partial-desc | 143 | "delay attribution"; no root-cause detail |
| SUB-F-39 | FR39 exception annotations *(opt)* | Partial-desc | 146 | Optional; "exception handling" mentioned |
| SUB-F-40 | FR40 configurable alerts on duration exceed | Pass | 503-508 | Rules engine |
| SUB-F-41 | FR41 alerts for unsafe/prohibited activity | Pass | 285, 503-508 | "geofence breach alerts"; rules engine |
| SUB-F-42 | FR42 alerts for AI-confidence degradation | Partial-desc | 145 | "confidence levels"; no threshold |
| SUB-F-43 | FR43 alerts via dashboard/Email/API(AIDX) | Pass | 212, 376 | Multi-channel connectors; AIDX implied |
| SUB-F-44 | FR44 alerts include context/severity/action | Pass | 504 | "threshold-based, pattern-based" rules |
| SUB-F-45 | FR45 live turnaround status board | Pass | 137, 222 | "live dashboards, aircraft turnaround timelines" |
| SUB-F-46 | FR46 current state + next milestone | Partial-desc | 137 | "milestone tracking"; no next-milestone UI |
| SUB-F-47 | FR47 colour-coded delay indicators | Partial-desc | 222 | Alerts view; no colour-code detail |
| SUB-F-48 | FR48 video playback per event *(opt)* | Pass | 292 | "Historical playback"; optional |
| SUB-F-49 | FR49 KPIs by airline/ac-type/gate/provider | Pass | 200, 324 | KPI Engine; KPI dashboards |
| SUB-F-50 | FR50 trend/variance analysis | Pass | 221 | "Analytics View… trend analysis" |
| SUB-F-51 | FR51 AI-driven improvement insights | Partial-desc | 223 | "Predictions & Simulations"; no insight metric |
| SUB-F-52 | FR52 ad-hoc queries/filters | Pass | 562-569 | Governed query templates |
| SUB-F-53 | FR53 historical analysis | Pass | 292, 581 | "Historical analysis" / lineage |
| SUB-F-54 | FR54 integrate AODB/FIDS/A-CDM(AIDX) | Pass | 374-382 | Connectors table |
| SUB-F-55 | FR55 REST + event APIs | Pass | 374-382, 629-639 | REST/SOAP/AMQP/MQTT/RTSP |
| SUB-F-56 | FR56 publish actual timestamps | Pass | 376, 56 (header) | AODB connector milestones |
| SUB-F-57 | FR57 event metadata separate from video | Pass | 487-493 | Data lineage / metadata catalogue |
| SUB-F-58 | FR58 configurable retention | Pass | 646 | "Automated retention enforcement with configurable retention periods" |
| SUB-F-59 | FR59 forensic replay | Pass | 292, 591 | "Incident reconstruction for audit/investigation" |
| SUB-F-60 | FR60 RBAC | Pass | 547-556 | RBAC/ABAC at API/data/dashboard layers |
| SUB-F-61 | FR61 airline/SP data segregation | Pass | 556 | "Third-party stakeholders access only their own operational data" |
| SUB-F-62 | FR62 configurable permissions per role | Pass | 521-528 | Role-based views |
| SUB-F-63 | FR63 admin config tools | Pass | 220, 505-509 | User Management & Config / Rules Engine |
| SUB-F-64 | FR64 Dev/Test/Prod separation | Pass | 794 | "development, staging, and production environments" |
| SUB-F-65 | FR65 operational monitoring/health dashboards | Pass | 247-250, 943-952 | CloudWatch/GuardDuty/monitoring |
| SUB-F-66 | FR66 admin configure alerts/reports/views/users | Pass | 220, 505 | User Management & Config |
| SUB-F-67 | FR67 BAC SSO; non-BAC local w/ password params + MFA | Pass | 811-816, 889, 897-908 | Azure AD SSO; OpenLDAP/OneLogin for third parties; MFA mandatory; password policy |
| SUB-F-68 | FR68 versioned AI models | Pass | 199, 777 | "Versioned AI Models"; semver |
| SUB-F-69 | FR69 track detection accuracy per model | **Partial-desc** | 199 | "Versioned AI Models"; **no per-model accuracy metric** (OC-9) |
| SUB-F-70 | FR70 airport-specific model tuning | Partial-desc | 145 | "airport-specific AI tuning"; no tuning process |
| SUB-F-71 | FR71 continual improvement | Partial-desc | 145, 198, 777 | No improvement-rate metric (OC-8) |
| SUB-F-72 | FR72 Phase-2 airline integration / aerobridge pax | **Ambiguous/Partial** | — | Not substantively addressed (OC-10) |
| SUB-F-73 | FR73 Phase-2 mobile/tablet remote access | **Ambiguous/Partial** | — | Not substantively addressed (OC-10) |

Functional summary: ~30 Pass, ~35 Partial-desc, 2 Over-claim (FR17 if read as full claim, FR23 header-only), 2 Ambiguous (FR72/73). The pattern is "platform architecture described, per-FR acceptance criteria absent."

#### Non-Functional (NF01–NF48) — 48 mandatory

| ID | NF | Verdict | v2 evidence (line) | Note |
|---|---|---|---|---|
| SUB-NF-01 | NF01 BAC ISRA | Pass | 672 | Security-by-design aligned with BAC ISRA |
| SUB-NF-02 | NF02 export data + list exportable fields | Pass | 629-639 | Data Exchange / export controls |
| SUB-NF-03 | NF03 live data 24/7/365 + refresh frequency | **Partial/Fail** | 758 | 24×7 asserted; **refresh frequency not quantified** — blocking limb |
| SUB-NF-04 | NF04 redundancy/backup/DR + SLA | Pass | 739-767 | HA/DR framework + RTO/RPO table |
| SUB-NF-05 | NF05 3-yr availability history | Amb / N/A-coll | — | Belongs in response sheet |
| SUB-NF-06 | NF06 RPO all data recoverable | Pass | 760 | "< 2 hours" |
| SUB-NF-07 | NF07 RTO ≤4h | Pass | 759 | "<= 4 hours" |
| SUB-NF-08 | NF08 integration scope/ownership pre-kickoff | Partial-desc | 387-481 | Connectors detailed; ownership TBD |
| SUB-NF-09 | NF09 QA standards/accreditations/methods | Pass | 671-678 | ISO 9001/20000/22301/CMMI L3 |
| SUB-NF-10 | NF10 QA tools | Pass | 788-795 | CI/CD + IaC + test pyramid |
| SUB-NF-11 | NF11 risk mitigation | Pass | 680-689 | Vendor Access Governance / SBOM/SCA |
| SUB-NF-12 | NF12 additional resources to keep timelines | Partial-desc | 783 | "Clear resourcing"; no surge-commitment |
| SUB-NF-13 | NF13 test methodology | Pass | 771, 790-795 | CI/CD + test pyramid |
| SUB-NF-14 | NF14 test tools | Pass | 790-795 | Automated testing pyramid |
| SUB-NF-15 | NF15 implement all integrations in scope | Pass | 374-481 | Connectors |
| SUB-NF-16 | NF16 list API connectors | Pass | 374-382 | Connector table |
| SUB-NF-17 | NF17 24/7/365 phone/email/online support | **Fail** | 829-836 | Only "1h security-incident notification"; no 24/7/365 support channel — blocking |
| SUB-NF-18 | NF18 client-configurable help/knowledge | Partial-desc | — | Not addressed |
| SUB-NF-19 | NF19 Sev-1/2/3 response+resolution | **Fail (Over-claim)** | 831 header, 835 body | Header claims NF19; body only has incident-notification 1h — blocking (OC-1) |
| SUB-NF-20 | NF20 Sev-3 resolution ≤8h business day | **Fail** | — | Not stated — blocking |
| SUB-NF-21 | NF21 documented incident mgmt + SLA per tier | Partial-desc | 835 | "formal incident handling procedure"; no SLA-per-tier |
| SUB-NF-22 | NF22 local rep assigned to BAC account | Amb | — | Not addressed |
| SUB-NF-23 | NF23 help-desk field info | Partial-desc | — | Not addressed |
| SUB-NF-24 | NF24 support details/help on UI | Partial-desc | 222 | Alerts view only |
| SUB-NF-25 | NF25 self-service reporting for IT | Pass | 351-358 (v1 had Self-Service BI; v2 folds into query templates) | Governed query templates |
| SUB-NF-26 | NF26 quick reference guides (state cost) | N/A-coll | — | Training deliverable; response sheet |
| SUB-NF-27 | NF27 admin/user training + format + cost | N/A-coll | — | Response sheet / PMR-07/08 |
| SUB-NF-28 | NF28 ongoing training (incl/excl managed svc) | N/A-coll | — | Response sheet |
| SUB-NF-29 | NF29 training for new features/patches | N/A-coll | — | Response sheet |
| SUB-NF-30 | NF30 training to suppliers | N/A-coll | — | Response sheet |
| SUB-NF-31 | NF31 support large groups | Pass | 517-528 | Role-based views scale |
| SUB-NF-32 | NF32 support multiple users | Pass | 517-528 | Role-based views |
| SUB-NF-33 | NF33 group-based access to apps | Pass | 533, 549 | RBAC/ABAC |
| SUB-NF-34 | NF34 explicitly deny unauthorised (examples) | Pass | 541 | Zero-trust; "no implicit trust" |
| SUB-NF-35 | NF35 MFA | Pass | 711, 889 | "Mandatory multi-factor authentication" |
| SUB-NF-36 | NF36 SSO | Pass | 230, 553, 815 | Azure Entra ID / OIDC / SAML |
| SUB-NF-37 | NF37 consistent UX web/mobile | Partial-desc | — | Not substantively addressed |
| SUB-NF-38 | NF38 support Edge/Chrome/Firefox/Safari | Partial-desc | — | Browser support not enumerated |
| SUB-NF-39 | NF39 no browser plug-ins | Partial-desc | — | Not addressed |
| SUB-NF-40 | NF40 common UX guidelines | Partial-desc | 219-225 | UI layer described; no UX-standard cite |
| SUB-NF-41 | NF41 RBAC for admin delegation | Pass | 521-528 | Role-based views |
| SUB-NF-42 | NF42 SAML2 federated IdP (Azure AD) | Pass | 231, 553 | Keycloak SAML; Azure AD |
| SUB-NF-43 | NF43 just-in-time admin; delegation expires | Pass | 543 | "Short-lived credentials… time-limited" |
| SUB-NF-44 | NF44 self-service password reset | Partial-desc | 900-908 | Password lifecycle mgmt; no self-service reset endpoint |
| SUB-NF-45 | NF45 real-time system log/diagnostics | Pass | 648-659, 939-952 | Logging/monitoring |
| SUB-NF-46 | NF46 reports on auth/usage/audit | Pass | 662-664 | Compliance reporting |
| SUB-NF-47 | NF47 log geolocation on auth | Partial-desc | 652 | "source and destination IP"; no geolocation |
| SUB-NF-48 | NF48 search/filter on events | Pass | 651, 951 | "Searchable logs" |

NF summary: ~28 Pass, ~12 Partial-desc, **3 Fail (NF03 refresh, NF17, NF19/NF20 — the blocking set)**, 1 Over-claim, 2 Amb, ~5 N/A-coll (training).

#### ISRA (rows 1–29) — 29 mandatory

UTAM v2 does not contain an ISRA tab/response; it provides architectural evidence that would feed the response-sheet ISRA responses. Verdicts reflect whether the collateral substantiates the row.

| ID | ISRA # / Domain | Verdict | v2 evidence (line) | Note |
|---|---|---|---|---|
| SUB-ISRA-01 | 1 / A6 Business Assurance — ISO 27001 | Pass | 1031, 671-678 | ISO 27001 certified |
| SUB-ISRA-02 | 2 / A8 Information Classification | Pass | 916-923 | Data classification + DLP |
| SUB-ISRA-03 | 3 / A8 Data Retention — auto-delete | Pass | 646 | Configurable retention + auto enforcement |
| SUB-ISRA-04 | 4 / A8 Asset Disposal — sanitisation | Pass | 823-827 | Exit plan + Certificate of Data Destruction |
| SUB-ISRA-05 | 5 / A6 Access Control — privileged | Pass | 543-545, 881-893 | PAM, break-glass, MFA |
| SUB-ISRA-06 | 6 / A8 IS Roles & Responsibilities | Partial-desc | 1035 | Staff confidentiality; roles not mapped to contract |
| SUB-ISRA-07 | 7 / A8 IS Policy — mature policy | Pass | 672, 717 | INFOSEC policy compliance |
| SUB-ISRA-08 | 8 / A6 IS Awareness — annual training | Partial-desc | 1037 | "periodic" training; not explicitly annual |
| SUB-ISRA-09 | 9 / A16 Mandatory Breach Notification | **Partial / contaminated** | 835, 1049, 1067 | "1h notification" present but framed under GDPR/EEA — must re-frame to OAIC/Notifiable Data Breaches scheme |
| SUB-ISRA-10 | 10 / A12 Security updates/patching | Pass | 773-786 | Patch cadence; CIS hardening |
| SUB-ISRA-11 | 11 / A12 Change Mgmt → BAC CAB | Pass | 834, 969-981 | Change mgmt + BAC CAB |
| SUB-ISRA-12 | 12 / A16 Incident Response Mgmt | Partial-desc | 835, 954-967 | IR procedure; reporting-to-authorities not framed to OAIC |
| SUB-ISRA-13 | 13 / A10 Cryptography | Pass | 243-245, 910-923 | KMS, AES256, TLS1.2 |
| SUB-ISRA-14 | 14 / A14 System Development — secure | Pass | 867-879 | DevSecOps |
| SUB-ISRA-15 | 15 / A12 Malicious Software | Pass | 802, 966 | Antimalware + anti-malware scanning |
| SUB-ISRA-16 | 16 / A12 Backups meet BAC RTO/RPO | Pass | 755-767 | RTO ≤4h, RPO <2h |
| SUB-ISRA-17 | 17 / A12 Backup testing | Pass | 749 | "Proven recoverability… scheduled automated restore workflow" |
| SUB-ISRA-18 | 18 / A13 Network Controls | Pass | 855-865 | NGFW/WAF/EDR/IDS |
| SUB-ISRA-19 | 19 / A8 IP — data sovereignty | **Fail (contaminated)** | 1015, 1049 | "European Union (AP)" + EEA framing — wrong for Australia; must state Australian/AP residency under Privacy Act |
| SUB-ISRA-20 | 20 / A16 Service Escrow | Pass | 827 | Escrow agreement |
| SUB-ISRA-21 | 21 / A8 Privacy — right to anonymity | **Partial / contaminated** | 644-646, 1021-1067 | Pseudonymisation present; privacy framework is GDPR not APP |
| SUB-ISRA-22 | 22 / A11 Physical & Environmental | Pass | 1043 | Cloud data-centre physical security (AWS) |
| SUB-ISRA-23 | 23 / A18 Compliance mgmt during contract | Partial-desc | 836 | "Annual review"; no in-contract validation cadence |
| SUB-ISRA-24 | 24 / A16 Incident plans — tested regularly | Partial-desc | 835 | IR procedure; no test-cadence |
| SUB-ISRA-25 | 25 / A17 BCM — hosting geographical address | **Partial / contaminated** | 356, 1015 | "AWS AP Regions" + "European Union (AP)" — must give concrete ap-southeast-2 (Sydney) address |
| SUB-ISRA-26 | 26 / A7 Screening/Vetting — privileged staff | Partial-desc | 1037 | Confidentiality; no vetting/screening detail |
| SUB-ISRA-27 | 27 / A12 App whitelisting | Partial-desc | 802 | Antimalware; no app-whitelisting |
| SUB-ISRA-28 | 28 / A9 Authentication — MFA across business | Pass | 711, 889 | MFA mandatory for privileged; "across business" not explicit |
| SUB-ISRA-29 | 29 / A16 Security Event/Log mgmt — retention | Pass | 648-659 | Immutable audit log; retention per policy |

ISRA summary: ~17 Pass, ~8 Partial-desc, **4 contaminated (rows 9, 19, 21, 25)** that must be re-framed to Australian Privacy Act/OAIC before the response-sheet ISRA tab can be populated from this collateral.

#### Project-Management (PMR-01–PMR-10) — architectural limbs only

Most PMR rows are process/contractual deliverables that belong in the response sheet (Methodology tab) and are N/A-collateral for a solution-architecture document. Architectural limbs assessed:

| ID | PMR | Verdict | v2 evidence (line) | Note |
|---|---|---|---|---|
| SUB-PMR-04 | PMR-02b Design — DR/backup/retention in detailed design | Pass | 739-767 | HA/DR + RTO/RPO in collateral |
| SUB-PMR-05 | PMR-02c Build — DEV/TST/PROD | Pass | 794 | Env parity via IaC |
| SUB-PMR-13 | PMR-06a Detailed Design — traffic flows/VM/DB/reports; demonstrate each FR met | Partial-desc | 149-252 architecture | Architecture described; per-FR "demonstrate met" is the gap this report identifies |
| SUB-PMR-14 | PMR-06b Test Plan — covers all FR + NFR traceability | N/A-coll | — | Deliverable; response sheet |
| SUB-PMR-16 | PMR-06d As-built — floorplans with hardware/IDs | N/A-coll | — | Deliverable |
| SUB-PMR-19 | PMR-09 20% withheld until PC | N/A-coll | — | Commercial |
| SUB-PMR-20 | PMR-10 6-mo defects *(opt)* | N/A-coll | — | Optional; response sheet |

Other PMR rows (weekly meetings, WHS, change control, training, closure) are process/contractual — N/A-collateral.

### 8b. N/A-collateral — Belongs in response sheet, not collateral (NOT counted as Fail)

These 70 mandatory requirements are out of collateral scope for a solution-architecture document. They must be addressed in the Response Sheet (Tabs A-F), pricing, commercial submission, or declarations. UTAM v2 is not expected to cover them.

- **Submission-format S-1…S-18** (17 mandatory): email submission, marking, closing date/time, acknowledgement, completeness, Response Sheet requirement, 5-page PDF (S-10 optional), no-sales-brochures, departures doc, addenda acknowledgment, 90-day validity, queries deadline, correspondence via email, shortlist presentation.
- **Content C-1…C-23** (23 mandatory): Supplier Info, Social Procurement (Supply Nation, Modern Slavery Act 2018), Relevant Experience, Methodology, Pricing, Tab F FR/NF/PMR conformance, ISRA tab, referees (≥2), insurance certificates, COI declaration, contract execution info, certifications.
- **Procedural/Contractual P-1…P-28** (insurance amounts P-1…P-5, insurance maintenance P-6, contract term P-7/P-8, commencement P-9, MSA form P-10, departures P-11, term P-12, hard copies P-13, Conditions of Proposal P-14, 90-day validity P-15, whole-of-services P-16, BAC discretion P-17/18, reliance P-19, no-contract-until-executed P-20, warranties P-21, confidentiality P-22, own-risk P-23, airport-operations ack P-24, ASIC P-25, BAC contractor registration P-26, CASA/Airports Act compliance P-27, no-collusion P-28). P-29…P-35 (RTO/Sev SLAs) are architectural and assessed in §5/§8a.
- **Numeric N-1…N-6, N-18…N-29** (18): insurance $, term, extensions, validity, availability-history, PDF page limit, queries deadline, referees, doc-review period, defects, retention %, pricing horizon, dates.

**These N/A-collateral items are not compliance failures of the UTAM collateral.** They are listed so the user can see the collateral is not expected to cover them; they must be covered in the Response Sheet / pricing / declarations.

---

## 9. Pre-Flight Status

**STATUS: BLOCKING — collateral not ready to substantiate Tab F for NF03/NF17/NF19/NF20 or ISRA rows 9/19/21/25.**

**Blocking list (must be fixed in v3 of the collateral OR committed directly in Response Sheet Tab F independent of the collateral):**

1. NF19/NF20 Sev-1/2/3 response+resolution SLA matrix — commit the 7 numeric SLAs (N-9…N-15) or declare a deviation in the departures document.
2. NF17 24/7/365 phone/email/online-help support — commit the coverage and channel.
3. NF03 live-data refresh frequency — state the refresh interval.
4. Cross-contamination (§3) — remove all GDPR/EEA/NIS2/Hellenic/"European Union (AP)" references; reframe data-protection/sovereignty to Privacy Act 1988 / APPs / OAIC / ASD Essential 8 / AWS ap-southeast-2 (Sydney). The three internally-contradictory lines (1015, 1049, 360) are the highest-priority fixes.
5. FR17/FR20/FR23/FR24 — add per-class precision/recall or per-activity detection-accuracy commitments, or mark these as Partial in Tab F (not "Compliant").
6. FR72/FR73 Phase-2 — either describe substantively or mark Partial in Tab F.
7. No deviation register — any Tab-F Partial/Deviation must be carried into the departures document per S-13/P-11.

Until items 1-4 are resolved, the UTAM v2 collateral should not be used as the evidence base for Tab F NF03/NF17/NF19/NF20 rows or ISRA rows 9/19/21/25.

---

## 10. Methodology Notes

- **Denominator:** 269 mandatory (gold-requirements.md). 70 N/A-collateral items excluded from the fail count because they belong in the Response Sheet / pricing / declarations, not in a solution-architecture document. This is the key correction vs a naive presence-based check: those 70 are NOT collateral compliance failures.
- **Capability-vs-commitment test** (the prior-eval lesson): applied to every FR/NF claim. The dominant v2 pattern is "architecture described, per-requirement acceptance threshold absent" → Partial-desc. This is not scored as Fail because the platform architecture is genuinely described; it is scored as Partial because an evaluator marking Tab F "Compliant" from this collateral would over-claim.
- **Cross-contamination scan** (§3) is the v2-specific adversarial pass. Three lines (1015, 1049, 360) are internally-contradictory edit artefacts where a partial s/EU/AP/ produced "European Union (AP)", "EEA… AP data centers", and "GDPR and NIS2… AP regulatory boundary". These would be immediately flagged by any evaluator familiar with Australian data-protection law.
- **No deviation register** in the collateral (expected). All 14 architectural shortfalls in §7 are undeclared with respect to the collateral and must be declared in the response-sheet departures document or fixed.
- **Source filenames preserved as-is**, including the repo typos: "BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md" (leading space after BAC-), "BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md" (spaces around dashes).