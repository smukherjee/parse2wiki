# Compliance Report — Track A (Underwing Analytics, BAC-T-26-505)

**Proposal under validation:** `eval/bac/trackA/proposal-trackA.md`
**Authoritative RFP:** `sources/BAC/BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md`
**Response sheet (required-response structure):** `sources/BAC/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md`
**Cross-check collateral:** `sources/BAC/Turnwise Product Document 1.pdf.md` and `sources/BAC/UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`

**Validator:** `compliance-validator` skill, full 12-step process.
**Binding hierarchy:** The RFP (including Annexure A Conditions of RFP and Annexure B MSA) and the Response Sheet Tab F (Functional, Non-Functional, PM, ISRA schedules) are the binding artefacts. The TurnWise Product Document and the UTAM Solution Architecture Details document are product/solution collateral and are **non-binding**. In particular, the UTAM document was prepared for a prior European airport deployment and its references to AIA / Athens International Airport, "BRISBAINE" spelling, GDPR, the NIS2 Directive, EU data residency / AWS EU regions, the Hellenic Data Protection Authority, the Eurocontrol NM Message Service, and a 40-minute RTO are **non-binding**; they are reconciled to the Brisbane / Australian regulatory context in the proposal (Section 4.9 and deviation register items D01 and D11). Where the UTAM document quotes a value that the RFP also binds, the RFP value governs.

---

## BLOCKING: 6 mandatory requirements not substantively met

The proposal is structurally complete and well-reconciled, but six mandatory items are not yet substantively satisfied and would prevent a compliant final submission if left unresolved. All bar B06 are declared as placeholders in the deviation register (Section 14); B06 is an undeclared over-claim.

1. **B01 — Pricing values not provided.** Schedule E (Pricing tab) and the pricing envelope are empty; all pricing values are "to be confirmed from bidder input" (D17). The RFP requires the whole-of-services price in a 5-year prescribed format; an empty pricing schedule is a non-conforming proposal. *Numeric link:* C-CON-07.
2. **B02 — Referees not provided.** The Response Sheet Relevant Experience tab requires at least two referees; the proposal states these are TBC from bidder input (D15). *Numeric link:* N-REF-01.
3. **B03 — Certificates of Currency not appended.** Insurance evidence (Public Liability $20M, Professional Indemnity $10M, Cyber $10M, Workers Compensation) is committed in §13.1 but certificates, insurer names, policy numbers, levels and expiry dates are TBC (D14/D18). *Numeric link:* N-GEN-04..06, C-CON-14.
4. **B04 — Named team / bios not provided.** PMR-01 requires the Contractor to demonstrate appropriate expertise, established supplier relationships, local support, proven experience, and suitably trained/certified personnel. Named individuals and bios for all eight project roles are TBC (D14). *Numeric link:* C-CON-01, C-SUBS-04.
5. **B05 — ISO/IEC 27001 certificate not appended.** ISRA question 1 (A6) asks for evidence of ISO/IEC 27001 accreditation. The proposal asserts certification but the certificate and scope are TBC (D16). *Numeric link:* C-SUBS-01.
6. **B06 — Supporting PDF exceeds the 5-page limit (undeclared over-claim).** RFP §8 allows one optional PDF "not more than 5 pages." The proposal asserts it is "within the five-page optional PDF allowance, extended here as a structured proposal for evaluation reading," but the document body is clearly longer. This is an over-claim not listed in the deviation register. Remediate by trimming the PDF to ≤5 pages or relying solely on the Response Sheet. *Numeric link:* N-GEN-07, C-SUB-05.

**Pre-flight status:** NOT READY for assembly as a final submission. The Response Sheet tabs (Pricing, Relevant Experience, Supplier Information, ISRA evidence) must be completed with bidder input and certificates appended before the proposal can be lodged. The supporting PDF must be brought within the 5-page limit or dropped.

---

## Summary counts

| Verdict | Count | Notes |
|---|---|---|
| Pass | 37 | Clearly addressed with evidence at the level available in this draft. |
| Partial | 17 | Structurally addressed but substantive value/evidence is a placeholder ("to be confirmed from bidder input"). |
| Fail | 0 | No requirement is entirely unaddressed. |
| Ambiguous | 3 | COI disclosure, addenda acknowledgment, collusive-conduct certification — all standard/assumed compliant but not explicitly stated. |
| N/A | 1 | N-AVAIL-01 (99.9% availability is a non-binding UTAM design target, not an RFP threshold). |
| **Total** | **59** | 26 numeric rows (25 binding + 1 non-binding) + 33 categorical requirements. |
| **Blocking** | **6** | B01–B06 above. |

Numeric parity (binding rows only, N = 25): **21 Pass, 3 Partial, 0 Fail, 0 Ambiguous.** Full detail in `compliance-report-trackA-numeric-inventory.md`.

---

## 1. Requirement extraction (Step 1)

Compliance requirements were extracted from the RFP (§3–§8, Annexure A clauses 1–17, Annexure B) and the Response Sheet (Sheet1 responsibility diagram, Start checklist, Supplier Information, Social Procurement, Relevant Experience, Methodology, Pricing, Functional Requirements, NF Requirements, PM Requirements, ISRA) in binding hierarchy order. The RFP does not issue a separate BRD or Change Request; the Response Sheet Tab F carries the Functional, Non-Functional, PM and ISRA requirements that §3.5 and §3.6 of the RFP defer to. Requirements fall into four categories:

- **Submission format:** method of submission (email to Contact Officer), closing date/time (10 July 2026, 2pm AEST), marking with Proposal name and reference, completed Response Sheet, optional supporting PDF ≤5 pages, departures document, no additional documents unless requested.
- **Content:** Supplier Information, Social Procurement, Relevant Experience (≥2 referees), Methodology (5 questions), Pricing (5-year), Functional Requirements (73), Non-Functional Requirements (48), PM Requirements (PMR-01–PMR-10), ISRA (29 questions), Conflict of Interest, contract execution under s127 Corporations Act, certificates of currency, certifications/registrations.
- **Substantive:** insurance minimums, ASIC for airside personnel, BAC contractor management registration, local Australian account representative (NF22), SAML2 SSO with Azure AD (NF42), MFA (NF35), ISO/IEC 27001 accreditation, severity-model SLAs, 4-hour RTO, 3-year availability history, 20% withhold, 6-month defects liability, 5-business-day review period.
- **Procedural:** addenda acknowledgment, WHS compliance (PMR-04), compliance with Manual of Standards Part 139 / Airports Act 1996 / Civil Aviation Act 1988 / Aviation Transport Security Act 2004 (Annexure A clause 16), collusive-conduct prohibition (Annexure A clause 17), MSA acceptance or departures lodged with response.

---

## 2. Numeric / quantitative inventory (Step 2)

See the structured inventory in `compliance-report-trackA-numeric-inventory.md`. Twenty-six rows were extracted (25 binding + 1 non-binding UTAM design target), covering submission limits, insurance minimums, FR/NF/ISRA counts, PM thresholds (review period, withhold %, defects liability), referee minimum, the full Severity 1/2/3 response-and-resolution SLA set, RTO, RPO, and the 3-year availability history.

---

## 3. Categorical requirement validation (Step 3)

| ID | Requirement (source) | Mandatory? | Verdict | Evidence / gap |
|---|---|---|---|---|
| C-SUB-01 | Submission via return email to Contact Officer by closing date/time (RFP §4.5, §6.1) | Mandatory | Pass | Cover letter confirms lodging via return email to Contact Officer by closing date and time, marked with Proposal name and reference (§1). |
| C-SUB-02 | Marked with Proposal Name and reference number (RFP §4.5) | Mandatory | Pass | Cover letter confirms marking (§1). |
| C-SUB-03 | Completed Supplier Response Sheet (Excel) returned (RFP §8, §6) | Mandatory | Partial | Proposal confirms Response Sheet accompanies the submission, but all tabs (Supplier Info, Social Procurement, Relevant Experience, Methodology, Pricing, FR, NF, PM, ISRA) carry "to be confirmed from bidder input" placeholders. |
| C-SUB-04 | Closing 2pm AEST 10 July 2026 (RFP §4.2, §6.1) | Mandatory | Pass | Response Date 10 July 2026 stated (§1); time not restated but method committed. |
| C-SUB-05 | Optional supporting PDF ≤5 pages (RFP §8) | Mandatory | Partial | Over-claim: asserts it is within the 5-page allowance while the body exceeds it. See B06. |
| C-SUB-06 | No additional documents unless specifically requested (RFP §8) | Mandatory | Pass | Proposal notes this and excludes prior-deployment artefacts (§16). |
| C-SUB-07 | Departures lodged with response or deemed accepted (RFP §5.1, Annexure A) | Mandatory | Pass | Deviation register at §14; cover letter confirms departures listed there. |
| C-CON-01 | Cover letter with authorised representative (RFP §4.5, Annexure A clause 9) | Mandatory | Partial | Cover letter present; signature, name, title and contact are "to be confirmed from bidder input" (§1). See B04. |
| C-CON-02 | Executive Summary (RFP §3, evaluation criteria) | Expected | Pass | Section 2 present, addresses goals, scope, and solution. |
| C-CON-03 | Supplier Information tab (business details, key contacts, mandatory-criteria dropdown) (Response Sheet) | Mandatory | Partial | Referenced; all fields TBC from bidder input. |
| C-CON-04 | Social Procurement tab (Supply Nation, business size, Modern Slavery statement) (Response Sheet) | Mandatory | Partial | Not addressed in proposal narrative; Response Sheet tab TBC. |
| C-CON-05 | Relevant Experience tab with ≥2 referees (Response Sheet §2) | Mandatory | Partial | Section 15 describes capabilities; referees are a placeholder (D15). See B02. |
| C-CON-06 | Methodology tab — 5 questions (Response Sheet Schedule D) | Mandatory | Pass | Sections 3–11 describe products/services, on-time/on-budget delivery, risks, assumptions, and exclusions. |
| C-CON-07 | Pricing tab — 5-year prescribed format (Response Sheet Schedule E) | Mandatory | Partial | Structure described in §13.2; all values TBC (D17). See B01. |
| C-CON-08 | Functional Requirements tab — 73 FR conformance (Response Sheet Tab F) | Mandatory | Partial | §12.1 records "Yes" at category level; per-requirement conformance wording TBC from bidder input. |
| C-CON-09 | Non-Functional Requirements tab — 48 NF conformance (Response Sheet Tab F) | Mandatory | Partial | §12.2 records "Yes" by category; per-requirement wording TBC. |
| C-CON-10 | PM Requirements tab + completed Table 1 (Response Sheet PM Requirements) | Mandatory | Partial | §12.3 confirms the six-phase model; Table 1 (priority/response times) is empty in source and TBC (D12). |
| C-CON-11 | ISRA tab — 29 questions (Response Sheet ISRA) | Mandatory | Partial | §9.2 provides a 29-row response summary; evidence references and certificate TBC (D16). |
| C-CON-12 | Conflict of Interest disclosure (Response Sheet §7.1) | Mandatory | Ambiguous | Not addressed in proposal narrative; Response Sheet field default "None" assumed. Assumed compliant — standard field to be completed in the tab. |
| C-CON-13 | Contract execution info — s127 Corporations Act, directors, e-signing (Response Sheet §6) | Mandatory | Partial | Committed in §13.3; all details TBC (D18). |
| C-CON-14 | Insurance details + Certificates of Currency (Response Sheet §4; RFP §4.4) | Mandatory | Partial | §13.1 commits to all four insurance types at the required levels; certificates TBC. See B03. |
| C-CON-15 | Certification/registration details (Response Sheet §5) | Mandatory | Partial | ISO 9001/20000/27001/22301 asserted; certificate references TBC (D16). |
| C-SUBS-01 | ISO/IEC 27001 accreditation evidence (ISRA Q1; NF01) | Mandatory | Partial | Asserted in §9.2 and §15; certificate and scope TBC. See B05. |
| C-SUBS-02 | Aviation Security Identification Cards for airside personnel (Annexure A clause 14) | Mandatory | Pass | Cover letter confirms WAISL holds or will obtain ASICs (§1). |
| C-SUBS-03 | BAC contractor management system registration (Annexure A clause 15) | Mandatory | Pass | Cover letter confirms WAISL will register and maintain registration (§1). |
| C-SUBS-04 | Local Australian account representative (NF22) | Mandatory | Pass | BAC Account Executive (Australia) named as local escalation point (§7, §11). |
| C-SUBS-05 | SAML2 federated SSO with Azure AD (NF42) | Mandatory | Pass | Confirmed in §4.6, §9.1. |
| C-SUBS-06 | Multi-factor authentication (NF35) | Mandatory | Pass | Confirmed in §4.6, §9.1, ISRA Q28. |
| C-PROC-01 | Addenda acknowledgment (RFP §4.10) | Mandatory | Ambiguous | No addenda issued; proposal acknowledges the RFP structure and Annexures. Assumed compliant — no addenda to acknowledge at drafting time. |
| C-PROC-02 | WHS compliance (PMR-04) | Mandatory | Pass | §6 and §7 confirm WHS compliance, SWMS, and approved-contractor status. |
| C-PROC-03 | Part 139 / Airports Act 1996 / Civil Aviation Act 1988 / Aviation Transport Security Act 2004 compliance (Annexure A clause 16) | Mandatory | Pass | §3 and §4.9 reconcile all four instruments to the Brisbane context. |
| C-PROC-04 | Collusive-conduct prohibition (Annexure A clause 17) | Mandatory | Ambiguous | Not explicitly addressed. Assumed compliant — standard certification to be confirmed in the Response Sheet. |
| C-PROC-05 | RFP/MSA acceptance or departures lodged with response (RFP §5.1) | Mandatory | Pass | Cover letter and §13.3 confirm acceptance subject to departures in §14. |

---

## 4. Numeric parity / delta evaluation (Step 4)

See `compliance-report-trackA-numeric-inventory.md` for the full table. Headline findings:

- **Pass (21/25 binding):** proposal validity, initial term, extensions, all three insurance minimums, FR/NF/ISRA counts, review period, 20% withhold, 6-month defects liability, all seven Severity 1/2/3 response and resolution SLAs, RTO (4 hours, with the 40-minute UTAM figure correctly subordinated to the binding value via D11), and RPO ("near zero" satisfies "all data recoverable").
- **Partial (3/25):**
  - **N-GEN-07** — supporting PDF ≤5 pages: the proposal claims to be within the allowance while exceeding it (over-claim, undeclared).
  - **N-REF-01** — ≥2 referees: declared placeholder (D15).
  - **N-DR-03** — 3-year availability history: figures TBC (D10).
- **Fail (0), Ambiguous (0).**
- **N/A (1):** N-AVAIL-01 (99.9% availability is a UTAM design target, not an RFP threshold; proposed by WAISL).

---

## 5. Semantic carve-out and over-claim detection (Step 5)

| Location | Carve-out / over-claim wording | Verdict change | Notes |
|---|---|---|---|
| §1 line 24; §16 last para | "within the five-page optional PDF allowance, extended here as a structured proposal for evaluation reading" | → Partial (N-GEN-07 / C-SUB-05) | Over-claim: asserts compliance with the 5-page cap while the document body exceeds it. Not in the deviation register. |
| §4.4 (FR23) | "PPE detection where camera quality allows" | No change | This is the RFP's own wording (FR23), mirrored by the proposal. Not a proposal-introduced carve-out. |
| §9.2 / ISRA evidence column | "to be confirmed from bidder input" (repeated) | → Partial (C-SUBS-01, C-CON-11) | Placeholder, not a carve-out; but it means evidence is absent. |
| §11 note | "the source collateral quotes an RTO of 40 minutes ... WAISL confirms the 4-hour RTO as the binding commitment and offers the 40-minute target as the internal design objective" | No change (declared) | Correctly subordinated to the binding value; declared in D11. |
| §16 last para | "the Response Sheet remains the authoritative response format and the completed tabs take precedence over any narrative summary here in case of conflict" | No change | Reasonable subordination; reinforces that the binding artefact is the Response Sheet. |
| §4.8 / §8 | "to be confirmed from bidder input in the design workshops" (hosting model) | No change (declared) | Declared in D03. |

No "subject to baseline confirmation," "and Excluded Events," "as available," "where feasible," or "on terms agreed at renewal" weakening phrases were found in commitment text. The proposal does not claim "100% coverage" with a narrowing mechanism.

---

## 6. Addressed-within-narrative requirements (Step 6)

The RFP places no dedicated "addressed within the narrative" topics beyond the Response Sheet. The proposal addresses all RFP §3.3 scope-of-work bullets inside the narrative (Sections 2, 3, 4, 5, 8, 9, 10, 11). Integration targets (AODB, FIDS, A-CDM/AIDX, REST/event APIs, timestamp publishing) are covered with depth in §4.5 and §8. ISRA/ISO 27001/ASD Essential 8/NIST CSF/BAC IS Policy 2018 alignment is covered in §9.4. No topic is merely mentioned in passing.

---

## 7. Page / word count estimate (Step 7)

The RFP limits the optional supporting PDF to "not more than 5 pages." The proposal body is approximately 515 lines / ~5,200 words plus numerous tables, which at standard formatting renders to roughly 18–22 pages. This materially exceeds the 5-page allowance. The proposal acknowledges the Response Sheet as the authoritative format, but if the supporting PDF is lodged as written it is non-compliant with RFP §8. Flagged as B06 / N-GEN-07. No per-section page limits are specified by the RFP.

---

## 8. Cross-reference and multi-artefact consistency (Step 8)

Three-way reconciliation: RFP/Response Sheet requirement ↔ proposal commitment ↔ cross-check collateral.

| Check | Result |
|---|---|
| FR coverage (FR01–FR73) vs Response Sheet Tab F | Proposal §4.2–4.7 maps each capability to FR IDs consistently with the Response Sheet. No FR is omitted. |
| NF coverage (NF01–NF48) vs Response Sheet NF tab | §12.2 covers all 48; category mapping matches the Response Sheet grouping. |
| PMR coverage (PMR-01–PMR-10) vs Response Sheet PM tab | §6 and §7 cover all PMRs; Table 1 is correctly flagged as empty-in-source (D12). |
| ISRA (29 questions) vs Response Sheet ISRA tab | §9.2 answers all 29 in the same order; ID 30 (Spare) correctly excluded. |
| Insurance levels vs RFP §4.4 | §13.1 matches all four values exactly. |
| Severity model vs NF19/NF20 | §11 reproduces the binding Severity 1/2/3 response and resolution times exactly. |
| RTO vs NF07 and UTAM §7.1 | Proposal correctly binds 4 hours (NF07) and subordinates the UTAM 40-minute figure (D11). No inconsistency. |
| Data residency vs UTAM §5.3/§12 (EU) | UTAM states EU/AWS-EU/GDPR; proposal reconciles to Australia / Privacy Act 1988 (D01, §4.9). The binding frame for BAC is the Australian one. No inconsistency in the proposal; the UTAM text is the source of the divergence and is correctly flagged. |
| Eurocontrol NM Message Service | UTAM includes it; proposal excludes it as not applicable to BAC (§4.9, D01). Consistent. |
| Pricing references vs §13.2 narrative | Narrative references the Pricing tab; no numeric pricing is stated anywhere, so there is no internal numeric inconsistency, but the Pricing tab is empty (B01). |
| Team names / roles | Consistent across §7 (role list) and §14 (D14 placeholder). No named individuals, so no name-level inconsistency. |
| Case-study / client metrics | The TurnWise product document carries a sample route (IST–NAP) and airport context that is clearly illustrative, not a BAC case study. The proposal does not over-claim named BAC referees (§15 explicitly states none are in the source). |

**Naming discipline:** The UTAM document spells the airport as "BRISBAINE" and refers to "AIA" / "Athens International Airport." These are source-artefact typos carried over from a prior European deployment and are not attributed to the RFP. The proposal records them in D01 and uses the correct "Brisbane Airport Corporation" throughout.

---

## 9. Deviation-register completeness audit (Step 9)

The proposal's deviation register (§14) contains D01–D18. Audit of every below-binding shortfall and carve-out:

| Shortfall / carve-out | Declared? | Register ID | Verdict |
|---|---|---|---|
| UTAM AIA/Athens/GDPR/NIS2/EU-residency/Hellenic DPA/Eurocontrol NM artefact carry-over | Yes | D01 | Declared (source-artefact reconciliation; no deviation from BAC requirements sought). |
| RFP issue-date inconsistency (15 May cover vs 15 June §4.2/Response Sheet) | Yes | D02 | Declared. |
| Hosting model unspecified by RFP | Yes | D03 | Declared (clarification). |
| Kloudspot delivery-partner role and credentials | Yes | D04 | Declared (clarification). |
| Camera infrastructure / interface specs / Azure AD / time source / airside access assumptions | Yes | D05–D09 | Declared (assumptions). |
| 3-year availability history figures (NF05) | Yes | D10 | Declared; Partial (B-adjacent). |
| RTO 40 min vs 4 hour | Yes | D11 | Declared; no deviation sought. |
| PM Table 1 empty in source | Yes | D12 | Declared (clarification). |
| MSA acceptance subject to departures | Yes | D13 | Declared (standard condition). |
| Named team / bios | Yes | D14 | Declared (placeholder). |
| Referees | Yes | D15 | Declared (placeholder). Blocking if unresolved. |
| ISO certifications evidence | Yes | D16 | Declared (placeholder). Blocking if unresolved. |
| Pricing values | Yes | D17 | Declared (placeholder). Blocking if unresolved. |
| Contract execution details | Yes | D18 | Declared (placeholder). |
| **Supporting PDF exceeds 5-page limit** | **No** | — | **Undeclared deviation (B06).** The proposal claims to be within the 5-page allowance while exceeding it. Not listed in the register. |
| Social Procurement tab completion | No | — | Not a numeric shortfall; a Response Sheet tab to be completed. Treated as Partial (C-CON-04), not an undeclared numeric deviation. |
| Conflict of Interest disclosure | No | — | Response Sheet field; not a numeric shortfall. Treated as Ambiguous (C-CON-12). |
| NF16 API connector list TBC | No | — | Proposal states connector list TBC; not in register. Treated as Partial within C-CON-09; not a below-binding numeric shortfall (NF16 has no numeric value). |

**Conclusion:** The deviation register is well-populated for placeholders and source-artefact reconciliation. The single undeclared deviation is the 5-page supporting-PDF over-claim (B06). All placeholder items (D14–D18) are declared but must be resolved before submission (B01–B05).

---

## 10. Adversarial critic pass (Step 10)

1. **Binding numeric specs treated as Pass that are actually weaker?** No. Re-checked RTO (4 h vs UTAM 40 min — the 40 min is better, and the proposal binds at 4 h), all SLAs (exact match), insurance (exact match), counts (exact match). No hidden weakness.
2. **Shortfalls missing from the deviation register?** One: the 5-page PDF over-claim (B06). Added above.
3. **Internal inconsistencies between tables in the target?** None found. The §11 HA/DR table and the §13.1 insurance table are internally consistent and consistent with the RFP/Response Sheet.
4. **Status-word over-claims Step 5 missed?** Re-scanned §12.1/§12.2 conformance tables. The "Yes" entries are category-level and explicitly caveated by "Specific conformance wording per requirement is to be confirmed from bidder input in the completed Response Sheet." This is an honest placeholder, not a per-requirement over-claim. No additional downgrade beyond the Partial already applied to C-CON-08/09 is warranted.
5. **Loop result:** One full re-pass returned no new findings beyond B06. Diminishing returns reached.

---

## 11. Compliance report (Step 11)

This document *is* the compliance report. Remediation instructions for every Partial and Ambiguous item follow.

### Remediation instructions

**Blocking (resolve before submission):**
- **B01 (Pricing):** Complete Response Sheet Pricing tab (Schedule E) with 5-year delivery and ongoing costs plus additional costs and key assumptions; submit the pricing envelope.
- **B02 (Referees):** Provide at least two referees with company name, address, referee name and contact details, and a brief description of the similar goods/services supplied, in the Relevant Experience tab.
- **B03 (Certificates of Currency):** Append insurer name, policy number, level of cover, and expiry date for Workers Compensation, Public Liability ($20M), Professional Indemnity ($10M), and Cyber ($10M) to the Supplier Information tab.
- **B04 (Team / bios):** Provide named individuals and bios for the eight project roles; demonstrate established supplier relationships, local support, proven experience, and certified personnel per PMR-01.
- **B05 (ISO 27001 certificate):** Append the ISO/IEC 27001 certificate and scope (and ISO 9001/20000/22301 certificates) to the Supplier Information tab and reference them in the ISRA tab evidence column.
- **B06 (5-page PDF):** Either trim the supporting PDF to ≤5 pages, or do not lodge a supporting PDF and rely solely on the completed Response Sheet. If a >5-page document is intended, add it to the deviation register and seek BAC's acceptance (not recommended; RFP §8 is explicit).

**Non-blocking (complete the Response Sheet tabs):**
- **C-CON-03/04/08/09/10/11/13/15:** Complete the Supplier Information, Social Procurement, Functional, Non-Functional, PM (incl. Table 1), ISRA, contract-execution, and certification tabs with bidder input.
- **C-CON-12/ C-PROC-01/04:** Confirm Conflict of Interest (None or declare), addenda acknowledgment (none issued), and collusive-conduct certification in the Response Sheet.
- **N-DR-03 (availability history):** Provide the 3-year availability, service-failure, and total-time-not-online figures (D10); explain any gaps honestly.
- **C-CON-01:** Complete the authorised representative signature, name, title, and contact in the cover letter.

### Cross-reference consistency notes
No internal inconsistencies found. Source-artefact divergences (UTAM EU/AIA/GDPR/NIS2/Eurocontrol/40-min RTO) are correctly reconciled and declared. The binding RFP/Response Sheet values govern throughout.

### Page-count assessment
Supporting PDF materially exceeds the 5-page allowance (B06). No other page limits apply.

---

## 12. Blocking issues (Step 12)

**BLOCKING: 6 mandatory requirements not met.** Listed at the top of this report (B01–B06). The proposal assembler should not proceed to final assembly/lodgement until B01–B05 are resolved with bidder input and B06 is resolved by trimming or dropping the supporting PDF.

---

## Binding-hierarchy reconciliation summary

| Artefact | Binding status | Treatment |
|---|---|---|
| RFP (BAC-T-26-505) incl. Annexure A & B | **Binding** | Governs all compliance and numeric parity. |
| Response Sheet Tab F (FR/NF/PM/ISRA) | **Binding** | Carries the functional, non-functional, PM and ISRA requirements the RFP defers to (§3.5/§3.6). |
| TurnWise Product Document 1 | Non-binding product collateral | Used only to corroborate capability claims; no parity obligations. |
| UTAM Solution Architecture (draft v1) | Non-binding solution collateral | Prepared for a prior European deployment. AIA/Athens, GDPR, NIS2, EU data residency, AWS EU regions, Hellenic DPA, Eurocontrol NM Message Service, and 40-minute RTO are **non-binding** and reconciled to the Brisbane/Australian frame (Privacy Act 1988 (Cth) and APPs, CASA MOS Part 139, Airports Act 1996, Civil Aviation Act 1988, Aviation Transport Security Act 2004, AWS ap-southeast-2 / BAC private cloud). The Eurocontrol NM Message Service is excluded from BAC scope. The 4-hour RTO (NF07) governs over the UTAM 40-minute figure. |

*End of compliance report.*