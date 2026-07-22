# Gold Score — Track A BAC Proposal Draft

**Scorer:** Independent gold-scorer (isolated)
**Gold inventory:** `eval/bac/gold-requirements.md` (275 reqs / 269 mandatory)
**Draft scored:** `eval/bac/trackA/proposal-trackA.md` (WAISL / TurnWise / UTAM)
**Method:** Per-requirement classification against the gold inventory. Pass rows omitted from the main table (count given). Numeric parity checked at binding value.

---

## Totals

| Classification | Count (mandatory, n=269) |
|---|---|
| Pass | 212 |
| Partial | 45 |
| Fail | 4 |
| Ambiguous | 8 |
| **Pass rate** | **212 / 269 = 78.8%** |
| Blocking issues | **4** (5 if N-19 treated strictly) |

Optional (not in denominator, 6 total): S-10 Partial (claims ≤5pp but document exceeds), SUB-F-06 Pass, SUB-F-12 Pass, SUB-F-39 Fail (not addressed), SUB-F-48 Pass, SUB-PMR-20 Pass.

Pass distribution by section (mandatory): S 10, C 10, SUB-F 67, SUB-NF 26, SUB-PMR 18, SUB-ISRA 29, P 28, N 24.

---

## Blocking Issues (undeclared shortfalls / gaps on mandatory requirements)

| ID | Requirement | Issue | Blocking reason |
|---|---|---|---|
| S-14 | Acknowledge receipt of all addenda in relevant Schedule | Not addressed anywhere in draft; no addenda acknowledgment and no deviation declared. | Undeclared mandatory gap. |
| C-13 | Declare any Conflict of Interest ("None" if nothing) | No COI declaration in draft or referenced for the Response Sheet tab; not in deviation register. | Undeclared mandatory gap. |
| C-14 | Disclose major changes to control, personnel, or processes | Not addressed; not in deviation register. | Undeclared mandatory gap. |
| C-15 | Social Procurement (Supply Nation, Indigenous status, 75%+ workforce location, Modern Slavery Act 2018 compliance) | Not addressed in draft; not in deviation register. The Response Sheet tab is mandatory and the draft does not commit to completing it. | Undeclared mandatory gap. |
| N-19 (borderline) | Additional supporting PDF ≤ 5 pages | Draft claims the structured proposal sits "within the five-page optional PDF allowance" but the document is clearly far longer (518 lines / ~15+ pages). Not declared as a deviation. | Undeclared over-limit on a mandatory numeric; underlying allowance (S-10) is optional, so flagged borderline — count as 5th blocking only if strict. |

---

## Partial / Fail / Ambiguous rows (Pass rows omitted)

### Submission-Format (S)

| ID | Class | Note |
|---|---|---|
| S-1 | Partial | Cover letter addressed to Leighton.Walker@bne.com.au and marked with ref number, but "confidential" marking not explicitly stated. |
| S-3 | Partial | Closing date stated (10 July 2026) but the 2pm AEST time is not stated. |
| S-6 | Ambiguous | Receipt-acknowledgement is a BAC-side process; not locatable in draft. |
| S-7 | Ambiguous | Late-proposal exclusion is a BAC process; draft commits to on-time lodgement but does not restate the rule. |
| S-8 | Ambiguous | Incomplete/non-compliant exclusion is a BAC process; not restated. |
| S-14 | **Fail (blocking)** | No addenda acknowledgment. |
| S-16 | Ambiguous | Queries-by-email-≥2-BD-before-close process not addressed (pre-submission). |
| S-10 (opt) | Partial | Claims ≤5pp allowance but document exceeds it. |

### Content (C)

| ID | Class | Note |
|---|---|---|
| C-7 | Partial | Business details mostly deferred ("to be confirmed from bidder input"); ABN/ACN/GST/registered address/ultimate parent not provided in draft. |
| C-8 | Partial | Key contacts deferred to bidder input. |
| C-11 | Partial | Certifications named (ISO 9001/20000/27001/22301) but certificate references/scope deferred. |
| C-12 | Partial | Contract execution info committed in principle but director/secretary names, e-signature, contract rep deferred. |
| C-13 | **Fail (blocking)** | No COI declaration. |
| C-14 | **Fail (blocking)** | No major-changes disclosure. |
| C-15 | **Fail (blocking)** | No Social Procurement content (Supply Nation, Indigenous status, 75%+ workforce location, Modern Slavery Act 2018). |
| C-16 | Partial | Company background and product track-record present; on-time/on-budget evidence and quantified outcomes not provided. |
| C-17 | Partial | Two referees committed (D15) but not furnished — declared shortfall, non-blocking. |
| C-19 | Partial | 5-year pricing format committed; values deferred to bidder input. |
| C-20 | Partial | FR conformance given by category range ("Yes") rather than per-requirement (FR01–FR73); per-row conformance deferred to Response Sheet. |
| C-21 | Partial | NF conformance by category range only; not per-row. |
| C-22 | Partial | PMR conformance summarised; Table 1 (priority/response) left empty (D12). |
| C-23 | Pass (strong) | Full 29-row ISRA table with supplier response and residual risk (Low) for every row. |

### Functional (SUB-F) — mandatory

| ID | Class | Note |
|---|---|---|
| SUB-F-09 (FR09) | Partial | Camera health monitoring stated; "notify vendor on stream issue/failure" not explicitly addressed. |
| SUB-F-72 (FR72) | Partial | Phase 2 airline data integration / aerobridge pax counting treated as "roadmap", not a committed delivery; not declared in deviation register. |

Optional: SUB-F-06 Pass, SUB-F-12 Pass, SUB-F-39 Fail (not addressed), SUB-F-48 Pass.

### Non-Functional (SUB-NF) — all mandatory

| ID | Class | Note |
|---|---|---|
| NF-02 | Partial | Export supported; exportable fields/data types not listed. |
| NF-03 | Partial | Live data 24/7/365 stated; state refresh frequency not stated. |
| NF-05 | Partial | 3-year history committed in principle; figures deferred (D10) — declared, non-blocking. |
| NF-09 | Partial | QA methodology/test approach present; QA standards/accreditations not detailed. |
| NF-10 | Partial | "QA tools nominated in Response Sheet NF14 tab" — deferred. |
| NF-14 | Partial | Test tools deferred to Response Sheet. |
| NF-16 | Partial | "API connector list to be confirmed from bidder input" — deferred. |
| NF-27 | Partial | Admin/user training addressed; whether additional cost not stated. |
| NF-28 | Partial | Ongoing training mentioned (NF29) but inclusive/exclusive of managed services not addressed. |
| NF-30 | Partial | Supplier training "scoped under NF30" — format and detail not provided. |
| NF-31 | Partial | "Full support for very large groups" not explicitly addressed. |
| NF-32 | Partial | "Full support for multiple users" not explicitly addressed. |
| NF-33 | Partial | Group-based access to connected applications not explicitly addressed. |
| NF-34 | Partial | Deny unauthorised users implied via RBAC/ABAC; examples not provided. |
| NF-37 | Partial | Consistent UX across browsers/mobile asserted via "responsive web experience"; not detailed. |
| NF-38 | Partial | Browser support (Edge/Chrome/Firefox/Safari, mobile+desktop) not explicitly listed. |
| NF-39 | Partial | Browser plug-in requirement not explicitly addressed. |
| NF-40 | Partial | "Common UX guidelines/principles" not explicitly cited. |
| NF-44 | Partial | Self-service password reset endpoint not explicitly addressed. |
| NF-46 | Partial | Reports on user authentication / application usage / auditing not explicitly addressed. |
| NF-47 | Partial | Geolocation logging on authentications not addressed. |
| NF-48 | Partial | Search/filter on events (hundreds of logins/day) not addressed. |

### Project Management (SUB-PMR) — mandatory

| ID | Class | Note |
|---|---|---|
| SUB-PMR-01 (PMR-01) | Partial | Expertise committed; Kloudspot details/credentials and named certified personnel deferred (D04). |

### Procedural / Contractual (P)

| ID | Class | Note |
|---|---|---|
| P-13 | Ambiguous | Hard-copy/electronic execution copies are a BAC-side action; not addressed. |
| P-19 | Partial | Supplier warranty of information accuracy not explicitly restated (cover letter states experience/skill/resources). |
| P-20 | Ambiguous | "No contract until executed" not addressed. |
| P-22 | Partial | Confidentiality obligations not explicitly addressed. |
| P-23 | Partial | "Participates at own risk" not addressed. |
| P-26 | Partial | BAC contractor registration committed; annual fee not mentioned. |
| P-28 | Partial | No collusive/anti-competitive conduct declaration not addressed. |

### Numeric (N)

| ID | Class | Note |
|---|---|---|
| N-18 | Partial (declared) | 3-year availability history committed but figures not furnished; declared in D10 — non-blocking. |
| N-19 | Partial (flagged, borderline blocking) | ≤5pp claim not met by document length; not declared as a deviation. |
| N-20 | Ambiguous | Queries deadline (≥2 BD before close) is a pre-submission process; not addressed. |
| N-21 | Partial (declared) | Min 2 referees committed (D15) but not furnished — declared, non-blocking. |
| N-28 | Ambiguous | Contract award date (21 Aug 2026) is a BAC milestone; not addressed. |

---

## Numeric Parity Check (N-1 … N-29)

| ID | Parameter | Binding | Draft value | Parity | Declared? |
|---|---|---|---|---|---|
| N-1 | Public Liability | ≥ $20m AUD | $20m | ✓ Pass | — |
| N-2 | Professional Indemnity | $10m | $10m | ✓ Pass | — |
| N-3 | Cyber Security | $10m | $10m | ✓ Pass | — |
| N-4 | Initial term | 3 years | 3 years | ✓ Pass | — |
| N-5 | Extensions | 2 × 1-year | 2 × 1-year | ✓ Pass | — |
| N-6 | Validity | ≥ 90 days | 90 days | ✓ Pass | — |
| N-7 | RTO | ≤ 4h | 4h | ✓ Pass | — |
| N-8 | RPO | All data recoverable | "near zero" | ✓ Pass | — |
| N-9 | Sev1 response | ≤ 1h 24x7x365 | 1h | ✓ Pass | — |
| N-10 | Sev1 resolution | ≤ 4h business day | 4h | ✓ Pass | — |
| N-11 | Sev2 response (business) | ≤ 4h | 4h | ✓ Pass | — |
| N-12 | Sev2 response (non-business) | ≤ 8h | 8h | ✓ Pass | — |
| N-13 | Sev2 resolution | ≤ 4h business day | 4h | ✓ Pass | — |
| N-14 | Sev3 response | ≤ 8h | 8h | ✓ Pass | — |
| N-15 | Sev3 resolution | ≤ 8h business day | 8h | ✓ Pass | — |
| N-16 | Support coverage | 24/7/365 | 24/7/365 | ✓ Pass | — |
| N-17 | Live data refresh | 24/7/365 | 24/7/365 | ✓ Pass | — |
| N-18 | Availability history | 3 years | "will be provided on request" / figures TBD | ✗ Partial (declared D10, non-blocking) | Yes |
| N-19 | Supporting PDF | ≤ 5 pages | Document clearly exceeds 5pp; claims compliance | ✗ Partial (borderline blocking) | No |
| N-20 | Queries deadline | ≥ 2 BD before close | Not addressed | ~ Ambiguous | — |
| N-21 | Min referees | ≥ 2 | 2 committed, not furnished | ✗ Partial (declared D15, non-blocking) | Yes |
| N-22 | Document review | ≥ 5 BD | 5 BD | ✓ Pass | — |
| N-23 | Defects liability | 6 months | 6 months | ✓ Pass | — |
| N-24 | Lump sum withheld | 20% | 20% | ✓ Pass | — |
| N-25 | Pricing horizon | 5 years | 5-year format committed (values TBD) | ✓ Pass | — |
| N-26 | RFP issue date | 15 June 2026 | 15 June 2026 (D02 reconciles cover-page 15 May discrepancy) | ✓ Pass | — |
| N-27 | Closing date | 10 July 2026 | 10 July 2026 | ✓ Pass | — |
| N-28 | Contract award | 21 Aug 2026 | Not addressed | ~ Ambiguous | — |
| N-29 | Go-Live | 11 Dec 2026 | "By 11 December 2026 (TBC)" | ✓ Pass | — |

**Numeric parity summary:** 24/29 at parity; 2 declared shortfalls (N-18 availability history, N-21 referees) — non-blocking; 1 undeclared over-limit (N-19 page cap, borderline); 2 ambiguous BAC-side milestones (N-20, N-28). All binding SLA, insurance, term, RTO, and validity values match exactly.

---

## Optional / Value-Add tracking

| ID | Class | Note |
|---|---|---|
| S-10 | Partial | Supporting-PDF allowance invoked but document exceeds the 5pp cap. |
| SUB-F-06 | Pass | Video buffering supported. |
| SUB-F-12 | Pass | Camera health dashboard available. |
| SUB-F-39 | Fail | Exception annotations by operational staff not addressed. |
| SUB-F-48 | Pass | Live and historical video playback supported. |
| SUB-PMR-20 | Pass | 6-month defects liability period and maintenance agreement committed. |

---

## Notes

- The draft is a supporting proposal, not the completed Response Sheet. Many Content (C) and several NF requirements are satisfied only by a commitment to complete the relevant Response Sheet tab, with specific data deferred ("to be confirmed from bidder input"). These are scored Partial where the commitment is explicit but the data is absent.
- The ISRA coverage (C-23 / SUB-ISRA-01…29) is the strongest section: a full 29-row table with a supplier response and a residual-risk rating (Low) for every row.
- The draft correctly reconciles the UTAM collateral's EU/Athens/GDPR/NIS2 references to the Brisbane/Australian regulatory frame (Sections 4.9 and 14 / D01) and flags the RFP issue-date inconsistency (D02) and the 40-minute vs 4-hour RTO discrepancy (D11).
- The four blocking gaps (S-14, C-13, C-14, C-15) are administrative/Response-Sheet declarations the draft does not mention or register as deviations; they are closeable by a sentence-level commitment to complete the relevant Response Sheet tabs and acknowledge addenda.