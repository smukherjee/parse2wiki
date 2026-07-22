# Gold Score — Track B (BAC Underwing Analytics)

**Scorer:** Independent gold-scorer (isolated from Track A).
**Gold inventory:** `eval/bac/gold-requirements.md` — 275 requirements, 269 mandatory, 6 optional.
**Draft scored:** `eval/bac/trackB/proposal-trackB.md` (narrative technical draft; Excel Response Sheet entries stated as derived/not yet completed).

**Method:** Each gold requirement classified Pass / Partial / Fail / Ambiguous.
- Grounded + correct = **Pass**.
- Assertable (architecturally reasonable, claimed but not evidenced, no deviation declared) = **Partial** (per gold scorer-note: Partial conformance on a Must-Have is non-compliant unless the detail closes the gap; an un-evidenced assertion does not).
- Declared gap/shortfall (in §13 deviation register) = **Fail (not blocking)**.
- Undeclared numeric shortfall or wrong value = **Fail (blocking)**.
- Response absent and not locatable in the draft = **Ambiguous**.
- ISRA rows require BOTH a supplier response AND a residual-risk rating (gold C-23); the draft provides responses (§08) but **no residual-risk ratings** → every ISRA row is at best Partial.

---

## Totals (mandatory denominator = 269)

| Class | Count | Share |
|---|---|---|
| **Pass** | 93 | 34.6% |
| **Partial** | 116 | 43.1% |
| **Fail** | 31 | 11.5% |
| **Ambiguous** | 29 | 10.8% |
| **TOTAL** | 269 | 100% |

**Pass rate: 93 / 269 = 34.6%**
**Blocking count: 2 unique blocking issues** (Sev-1 resolution ≤4h not committed; Sev-2 resolution ≤4h not met — undeclared). These surface as 4 row-level Fails (N-10/P-32 and N-13/P-34, which the gold treats as the same requirement restated in P and N).

**Optional (6, excluded from denominator):** S-10 Pass, SUB-F-06 (FR06) Pass, SUB-F-12 (FR12) Partial, SUB-F-39 (FR39) Fail-declared, SUB-F-48 (FR48) Partial, SUB-PMR-20 (PMR-10) Pass (accepted/committed — value-add).

**Pass rows omitted from the main table (93):** S-2, S-8, S-12, S-13, S-15, S-18; C-9; FR04,05,16,19,25,33,34,35,36,37,40,41,45,46,47,49,52,53,55,58,59,60,61,62,63,64,65,66,67 (29); NF02,04,06,07,15,16,25,32,33,34,35,36,39,41,42,43,45,46 (18); PMR-02c,02e,05,06c (4); P-1..P-8, P-10, P-11, P-12, P-15, P-25, P-26, P-27, P-29, P-30, P-31, P-33 (19); N-1..N-9, N-11, N-12, N-14, N-16, N-19, N-23, N-24 (16).

---

## Main table — Partial / Fail / Ambiguous rows

### Submission-Format (S)

| ID | Class | Note |
|---|---|---|
| S-1 | Partial | Contact Officer "Leighton Walker" named; binding email `Leighton.Walker@bne.com.au` and "marked confidential" not stated. |
| S-3 | Ambiguous | Closing time 2pm AEST not stated. |
| S-4 | Ambiguous | Closing date 10 July 2026 not stated (§4.2 referenced generically). |
| S-5 | Partial | "Submission method confirmed" but not the return-email-by-closing mechanism. |
| S-6 | Ambiguous | Acknowledgement-of-receipt via return email not addressed. |
| S-7 | Ambiguous | Late-proposal exclusion not addressed. |
| S-9 | Partial | Excel Response Sheet completion committed/derived but not done. |
| S-11 | Ambiguous | "No additional info unless requested" not addressed. |
| S-14 | Ambiguous | Addenda acknowledgment not addressed. |
| S-16 | Ambiguous | Queries-via-email / 2-BD-deadline not addressed. |
| S-17 | Ambiguous | Day-to-day email correspondence not addressed. |

### Content (C)

| ID | Class | Note |
|---|---|---|
| C-1 | Partial | Schedule A insurance/cert content committed; certificates are placeholders. |
| C-2 | Partial | Social procurement obligations acknowledged (§02) but Schedule B not completed. |
| C-3 | Partial | Relevant Experience addressed (§14) but sub-contractor identification is placeholder. |
| C-4 | Partial | Methodology narrative present (§05) but Tab D entry not completed. |
| C-5 | Fail* | "Pricing is not in scope of this draft." Declared. |
| C-6 | Partial | Tab F conformance summarised (§11) but per-row Yes/No/Partial+detail not entered. |
| C-7 | Partial | Business details partial on cover; most fields placeholder. |
| C-8 | Fail* | Key contacts: explicit placeholder ("to be supplied"). Declared. |
| C-10 | Partial | Insurance committed (§12); Certificates of Currency not appended. |
| C-11 | Partial | ISO certs listed; certificate evidence placeholder. |
| C-12 | Ambiguous | Contract-execution info (Corps Act s.127, directors/authority) not addressed. |
| C-13 | Ambiguous | Conflict-of-Interest declaration not addressed. |
| C-14 | Ambiguous | Major-changes disclosure not addressed. |
| C-15 | Partial | Social procurement fields acknowledged but not completed (75%+ workforce location, Indigenous status, Modern Slavery statement). |
| C-16 | Partial | Company background/products/years partial (§14); on-time/on-budget evidence absent. |
| C-17 | Fail* | Two referees explicitly not provided; declared placeholder. |
| C-18 | Partial | Methodology 5 questions partially answered (risks/assumptions in §13); not in Response Sheet format. |
| C-19 | Fail* | 5-year pricing plan not in scope; declared. |
| C-20 | Partial | FR conformance summarised, not entered per row. |
| C-21 | Partial | NF conformance summarised, not entered per row. |
| C-22 | Partial | PMR conformance summarised, not entered per row. |
| C-23 | Partial | ISRA responses provided (§08); **residual-risk ratings absent for all 29 rows**. |

\* Declared gap → Fail, not blocking.

### Substantive — Functional (SUB-F), mandatory gaps/partials

Assertable (claimed, not evidenced, no deviation) = Partial. Grounded = Pass (omitted).

| ID | Class | Note |
|---|---|---|
| FR01,02,03,08,09,11,13,14,15,18,22,24,28,29,30,31,32,38,42,43,44,50,51,54,56,57,68,70,71,73 | Partial (30) | Assertable — architecturally reasonable, not evidenced; no per-row deviation declared. |
| FR07 | Fail* | Per-camera frame-rate/resolution; DEV-06. |
| FR10 | Fail* | Occlusion/glare; DEV-07. |
| FR17 | Fail* | Camera GSE-type classification; disqualifying; DEV-01. |
| FR20 | Fail* | Personnel presence in apron zones; disqualifying; DEV-02. |
| FR21 | Fail* | Personnel in restricted zones; DEV-08. |
| FR23 | Fail* | PPE detection; DEV-09. |
| FR26 | Fail* | Per-event confidence scores; DEV-10. |
| FR27 | Fail* | Manual validation/correction; DEV-10. |
| FR39 | Fail* | Exception annotations (optional; DEV-11). |
| FR69 | Fail* | Per-model accuracy tracking; DEV-10. |
| FR72 | Fail* | Phase-2 aerobridge pax counting / airline data integration; DEV-13. |

\* All declared → Fail, not blocking. FR39 is optional (excluded from denominator).

### Substantive — Non-Functional (SUB-NF)

Assertable = Partial.

| ID | Class | Note |
|---|---|---|
| NF01,03,08,11,12,13,14,21,22,24,27,28,29,30,31,37,38,40,44,48 | Partial (20) | Assertable, not evidenced. |
| NF19 | Partial | SLA matrix provided + DEV-03 declared, but matrix contains undeclared sub-shortfalls (Sev-1/Sev-2 resolution — see N-10/N-13). |
| NF20 | Partial | Sev-3 resolution table shows "3 business days" but a parenthetical commits to 8 business hrs — internally contradictory; no dedicated deviation entry. |
| NF05 | Fail* | 3-year availability history; DEV-14. |
| NF09 | Fail* | QA standards/methodologies; DEV-15. |
| NF10 | Fail* | QA tools; DEV-15. |
| NF17 | Fail* | 24/7/365 support; DEV-16. |
| NF18 | Fail* | Client-configurable help; DEV-17. |
| NF23 | Fail* | Field-level help; DEV-17. |
| NF26 | Fail* | Quick-reference guides; DEV-17. |
| NF47 | Fail* | Geolocation on auth; DEV-18. |

\* Declared → Fail, not blocking.

### Substantive — Project Management (SUB-PMR)

| ID | Class | Note |
|---|---|---|
| PMR-01,02,02a,02b,02d,02f,03,04,06,06a,06b,06d,07,08,09 | Partial (15) | Assertable, not evidenced. |

(PMR-10 optional: Pass — draft accepts the 6-month defects-liability term in §05/§06/§09/§12 and DEV-19; value-add.)

### Substantive — ISRA (29)

**Systemic: no residual-risk rating is provided for any ISRA row (gold C-23 requires both a response AND a residual-risk rating).**

| ID | Class | Note |
|---|---|---|
| ISRA-01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,28,29 | Partial (26) | Supplier response provided (§08); residual-risk rating missing. |
| ISRA-19 | Fail* | Data sovereignty; disqualifying; DEV-04 (Australian hosting committed). |
| ISRA-25 | Fail* | Hosting geographical address; disqualifying; DEV-05. |
| ISRA-27 | Fail* | Application whitelisting; DEV-22. |

\* Declared → Fail, not blocking.

### Procedural / Contractual (P)

| ID | Class | Note |
|---|---|---|
| P-9 | Ambiguous | Contract commencement 7 Sep 2026 not stated. |
| P-13 | Ambiguous | Two hard copies + electronic on award not addressed. |
| P-14 | Ambiguous | Acceptance of Conditions of Proposal (Annexure A) not addressed. |
| P-16 | Ambiguous | Whole-of-services / incidentals inclusion not addressed. |
| P-17 | Ambiguous | BAC discretion rights not addressed. |
| P-18 | Ambiguous | BAC accept/reject discretion not addressed. |
| P-19 | Ambiguous | Reliance-on-information warranty not addressed. |
| P-20 | Ambiguous | No-contract-until-executed not addressed. |
| P-21 | Ambiguous | Accuracy/skill/resources warranty not addressed. |
| P-22 | Ambiguous | Confidentiality obligations not addressed. |
| P-23 | Ambiguous | Participates-at-own-risk not addressed. |
| P-24 | Partial | Airside/safety acknowledged (§02/§05, ASICs); not a full Annexure A §13 acknowledgement. |
| P-28 | Ambiguous | No-collusive-conduct declaration not addressed. |
| P-32 | **Fail (blocking)** | Sev-1 resolution/plan ≤4h business day not committed — matrix says "Best-effort continuous until restored." Undeclared shortfall. (= N-10.) |
| P-34 | **Fail (blocking)** | Sev-2 resolution/plan ≤4h business day not met — matrix says "Within 1 business day" (8h > 4h). Undeclared shortfall. (= N-13.) |
| P-35 | Partial | Sev-3 response ≤8h committed (Pass); Sev-3 resolution contradictory (table 3 business days vs note 8 business hrs). |

### Numeric / Quantitative (N) — full parity table

| ID | Parameter | Binding | Draft value | Parity | Class | Note |
|---|---|---|---|---|---|---|
| N-1 | Public Liability | ≥$20M | $20M | ✓ | Pass | §12. |
| N-2 | Professional Indemnity | $10M | $10M | ✓ | Pass | §12. |
| N-3 | Cyber Security | $10M | $10M | ✓ | Pass | §12. |
| N-4 | Initial term | 3 yrs | 3 yrs | ✓ | Pass | §01/§12. |
| N-5 | Extensions | 2×1-yr | 2×1-yr | ✓ | Pass | §01/§12. |
| N-6 | Validity | ≥90 days | 90 days | ✓ | Pass | cover/§12. |
| N-7 | RTO | ≤4h | ≤40 min | ✓ | Pass | §08 (better than binding). |
| N-8 | RPO | all data recoverable | near-zero | ✓ | Pass | §08. |
| N-9 | Sev-1 response | ≤1h 24×7×365 | ≤1h 24×7×365 | ✓ | Pass | §10. |
| N-10 | Sev-1 resolution/plan | ≤4h business day | "Best-effort continuous" | ✗ | **Fail (blocking)** | No ≤4h commitment; undeclared. |
| N-11 | Sev-2 response (business) | ≤4h | ≤4h business-day | ✓ | Pass | §10. |
| N-12 | Sev-2 response (non-business) | ≤8h | ≤8h non-business | ✓ | Pass | §10. |
| N-13 | Sev-2 resolution/plan | ≤4h business day | "Within 1 business day" | ✗ | **Fail (blocking)** | 1 business day > 4h; undeclared. |
| N-14 | Sev-3 response | ≤8h | ≤8 business hrs | ✓ | Pass | §10. |
| N-15 | Sev-3 resolution/plan | ≤8h business day | table "3 business days" / note "8 business hrs" | ✗/✓ | Partial | Contradictory; 8h committed only in a parenthetical, table shows 3 days. Flag. |
| N-16 | Support coverage | 24/7/365 | 24/7/365 | ✓ | Pass | §10. |
| N-17 | Live data refresh | 24/7/365 | asserted real-time | ? | Partial | Asserted (NF03 assertable); refresh rate not specified. |
| N-18 | Availability history | 3 yrs | not provided | ✗ | Fail* | DEV-14; declared. |
| N-19 | Additional PDF | ≤5 pages | 5 pages | ✓ | Pass | Pre-Flight. |
| N-20 | Queries deadline | ≥2 BD before close | not stated | ? | Ambiguous | Not addressed. |
| N-21 | Minimum referees | ≥2 | "two referees" (placeholder) | ✗ | Fail* | §14 declares placeholders to be supplied. |
| N-22 | Doc review period | ≥5 business days | not locatable | ? | Ambiguous | 5-BD review period not stated in §06. |
| N-23 | Defects liability | 6 months | 6 months | ✓ | Pass | §05/§06/§09/§12. |
| N-24 | Lump sum withheld | 20% | 20% | ✓ | Pass | §01/§06/§12. |
| N-25 | Pricing horizon | 5 yrs | 5-yr acknowledged, no data | ✗ | Partial | Horizon acknowledged (§12); pricing data declared not in scope. |
| N-26 | RFP issue date | 15 Jun 2026 | not stated | ? | Ambiguous | |
| N-27 | Proposal closing date | 10 Jul 2026 | not stated | ? | Ambiguous | |
| N-28 | Contract award (est.) | 21 Aug 2026 | not stated | ? | Ambiguous | |
| N-29 | Project Go-Live | 11 Dec 2026 | not stated | ? | Ambiguous | |

\* Declared → Fail, not blocking.

**Numeric parity summary:** 16 of 29 numeric requirements meet parity (Pass). 2 are blocking Fails (N-10, N-13 — Sev-1/Sev-2 resolution times). 3 Partial (N-15 contradictory, N-17 asserted not evidenced, N-25 data absent). 2 declared non-blocking Fails (N-18, N-21). 6 Ambiguous (dates/deadlines not stated).

---

## Blocking issues

1. **N-10 / P-32 — Sev-1 resolution/plan ≤4 hours business day.** The §10 support matrix states Sev-1 resolution = "Best-effort continuous until restored" with no ≤4h commitment. This is a numeric shortfall against the binding N-10/P-32 and is NOT declared in the §13 deviation register (DEV-03 covers only response times, not Sev-1 resolution). **Undeclared shortfall → blocking.**

2. **N-13 / P-34 — Sev-2 resolution/plan ≤4 hours business day.** The §10 matrix states Sev-2 resolution = "Within 1 business day" (~8h), which is worse than the ≤4h binding. NOT declared in the deviation register (DEV-03 covers Sev-2 response, not resolution). **Undeclared shortfall → blocking.**

Note: both blocking issues are visible in the §10 matrix (not hidden), but they are not flagged as deviations/shortfalls, so per the scoring rule they count as undeclared. They could be rendered non-blocking by either (a) tightening the matrix to ≤4h for Sev-1/Sev-2 resolution, or (b) declaring them in the deviation register.

---

## Systemic / cross-cutting findings

- **ISRA residual-risk ratings absent (29 rows).** Gold C-23 and SUB-ISRA-01..29 require both a supplier response AND a residual-risk rating per row. The draft supplies responses (§08) but no residual-risk ratings for any of the 29 rows. This depresses every ISRA row to Partial at best and should be the single highest-priority fix.
- **Assertable claims dominate (116 Partial).** ~38% of Tab.F is claimed as "architecturally reasonable" but not evidenced, with no per-row deviation declared. Under the gold's mandatory scoring these count as non-Pass. Many could convert to Pass only with evidence or with explicit deviation entries.
- **Response Sheet not completed.** The draft is a narrative; the Excel Response Sheet entries (Schedules A–F, ISRA tab) are placeholders/derived-not-done. Pricing, referees, key contacts, insurance certificates, and sub-contractor identification are all declared placeholders.
- **SLA matrix internal contradiction.** Sev-3 resolution shows "3 business days" in the table but "8 business hrs committed" in a parenthetical (N-15 / NF20). The table value should be corrected to ≤8 business hrs to match the binding and the parenthetical.
- **Dates/deadlines not restated.** Closing date (10 Jul 2026), closing time (2pm AEST), issue date, award date, Go-Live, commencement date, and queries deadline (2 BD) are not stated in the draft (only generic §4.2 references). These are Ambiguous rather than wrong; they should be restated with the binding values.
- **Source-conflict handling is strong.** The UTAM/AIA/EU/GDPR reframing to Australian hosting (AWS Sydney ap-southeast-2 / BAC private cloud), Australian Privacy Act / APPs / ASD Essential 8, and BAC-as-data-owner is explicit and well-documented (§08, §13). ISRA-19/ISRA-25 are declared deviations with committed resolution paths (Fail, not blocking).
- **No fabricated content.** The draft explicitly refuses to invent referees, bios, pricing, or certifications and marks them as placeholders — an integrity positive, though it leaves many C/N rows as declared Fails.