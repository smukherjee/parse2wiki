# Compliance Report — Track B

**Proposal under validation:** `eval/bac/trackB/proposal-trackB.md`
**Authoritative RFP:** `sources/BAC/BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md`
**Response sheet (required-response structure):** `sources/BAC/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md`
**Cross-check collateral:**
- `sources/BAC/Turnwise Product Document 1.pdf.md`
- `sources/BAC/UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`

**Validation date:** 2026-07-17
**Validator:** `compliance-validator` skill, 12-step process

---

## BLOCKING: 11 mandatory requirements not met

The proposal is a draft that honestly declares its gaps and commits to resolution paths. That honesty is noted and valued. However, compliance is binary at submission: the following mandatory items are not met in the current artefact and must be closed (or formally accepted by BAC) before this proposal can be considered submission-ready.

### Disqualifying capability gaps (no current evidence; committed for delivery)

1. **FR17 — Camera-based GSE type classification (Must-Have).** Collateral evidences telematics/GPS GSE tracking only, not camera classification of the full enumerated GSE-type list. Committed CV classifier with per-class acceptance criteria (DEV-01). Blocking until Test-phase acceptance.
2. **FR20 — Personnel presence in apron zones, excluding passengers (Must-Have).** No personnel-detection capability evidenced in Turnwise or UTAM. Committed CV model (DEV-02). Blocking until Test-phase acceptance.
3. **NF19 — Severity response scenarios (Must-Have, partially met).** The committed SLA matrix meets the response-time thresholds but does NOT meet the resolution-time thresholds (see blocking items 7-9 below). The matrix is a commitment, not evidence.
4. **ISRA-19 — Data sovereignty, hosted in Australia (Must-Have).** Committed to AWS Sydney (`ap-southeast-2`) or BAC private cloud; all residency/privacy narrative rewritten to Australian framing. Reconciled at commitment level but not yet delivered; subject to BAC confirming hosting target at Initiation (DEV-04).
5. **ISRA-25 — Hosting geographical address (Must-Have).** Committed to supply Australian data-centre address in the completed ISRA tab once BAC confirms hosting target. Not yet supplied (DEV-05).

### SLA resolution-time shortfalls (NF19/NF20 — Must-Have, not declared)

6. **Sev-1 resolution ≤4 hours business day (NF19 item 2).** Proposal offers "Best-effort continuous until restored" — an unbounded carve-out, not the required ≤4h commitment. **Not listed in DEV-03.** Undeclared shortfall.
7. **Sev-2 resolution ≤4 hours business day (NF19 item 4).** Proposal offers "Within 1 business day" (~8h) — 2× slower than binding. **Not listed in DEV-03.** Undeclared shortfall.
8. **Sev-3 response on non-business days ≤8h (NF19 item 5).** Proposal commits only "≤8 business hrs"; non-business-day response not stated. **Not listed in DEV-03.** Undeclared shortfall.
9. **Sev-3 resolution ≤8 business hours (NF20).** Internal contradiction: SLA matrix row says "Within 3 business days" while a parenthetical says "NF20: Sev-3 resolution within 8 business hrs committed". Which is the commitment? **Not listed in DEV-03.** Ambiguous; blocking until clarified.

### Submission-component gaps (mandatory, placeholders not yet filled)

10. **Schedule C referees (2 required) + named key personnel/resumes.** Not supplied; placeholders. Blocking.
11. **Schedule E 5-year pricing breakdown + Schedule A insurance/ISO certificates + NF09/NF10 QA documentation.** Not supplied; placeholders. Blocking.

---

## Summary counts

| Verdict | Tab.F (170 rows) | RFP body / submission (18 reqs) | Total |
|---|---|---|---|
| **Pass** | 74 | 7 | **81** |
| **Partial** | 31 | 1 | **32** |
| **Ambiguous** | 65 | 3 | **69** |
| **Fail** | 0 | 7 | **7** |
| **Blocking** (subset) | 5 | 6 | **11** |
| **Total checked** | 170 | 18 | **188** |

- **Tab.F Pass (74):** directly evidenced in Turnwise/UTAM collateral (the "Grounded" set).
- **Tab.F Ambiguous (65):** the "Assertable" set — architecturally reasonable from the configurable platform but not directly evidenced. Marked "Assumed compliant — architecturally reasonable, not yet evidenced." These become Pass only when Test-phase acceptance is signed.
- **Tab.F Partial (31):** the "Gap" set — declared in the deviation register (DEV-01..DEV-22) with committed resolution paths. 5 are blocking (disqualifying); the remaining 26 are Must-Have/Should-Have gaps with delivery commitments.
- **Tab.F Fail (0):** every gap is declared in the deviation register, so there are no undeclared capability shortfalls at the row-presence level. The undeclared shortfalls are within NF19/NF20 resolution times (see numeric inventory) — these are captured as Fail in the numeric inventory and as blocking items above.

**Numeric requirements checked:** 38. **Numeric parity:** 18 Pass, 9 Partial, 8 Fail, 3 Ambiguous. See `compliance-report-trackB-numeric-inventory.md`.

---

## Binding-hierarchy reconciliation (RFP governs; UTAM does not)

The RFP and Response Sheet are the binding requirements source. The UTAM Solution Architecture document (`UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`) is a reusable architecture artefact originally written for an Athens International Airport (AIA) engagement and framed around GDPR / NIS2 / Hellenic DPA / EU residency. Its AIA/Athens/EU references are **non-binding** for BAC and must be reconciled to Brisbane/Australia.

### Was the UTAM Athens/EU framing properly reconciled?

**Largely yes, with two residual items.** The draft explicitly:

- Flags the conflict in Section 08: "Our reusable UTAM architecture artefact was written for a European customer and frames compliance around GDPR/NIS2/Hellenic DPA with EU residency. **We do not propagate that framing.**"
- Commits to Australian hosting: AWS Sydney (`ap-southeast-2`) or BAC private cloud at BAC's election.
- Rewrites the regulatory frame to **Australian Privacy Act 1988 / Australian Privacy Principles (APPs)**, **ASD Essential 8 / IRAP**, and **BAC as exclusive data owner**.
- Lists, in the Section 13 "Source-conflict-driven deviations" table, every Athens/EU passage being excluded and its Australian replacement: "adapt the platform to Athens Airport needs" → BNE; "exclusive property of Athens International Airport (AIA)" → BAC; "hosted exclusively within European Union (EU) data centres" → Australian hosting; "AWS EU region... GDPR and NIS2" → AWS Sydney / Australian Privacy Act / ASD Essential 8; "the Hellenic Data Protection Authority" → removed; "developed and implemented by Brisbaine Airport" (factually incorrect) → WAISL developed UTAM, BAC is the customer; entire GDPR Compliance section (UTAM §12) → replaced with Australian Privacy Act narrative.

**Residual items not fully reconciled:**

1. **NM Message Service / Eurocontrol reference (Section 07).** The proposal states "UTAM's NM Message Service handles A-CDM milestones (TOBT, TSAT, A-CDM milestones) and is adaptable to BNE's A-CDM context." The NM Message Service is a Eurocontrol Network Manager construct. The "adaptable" caveat is a soft carve-out; the proposal does not explain how a Eurocontrol-NM-specific service applies at BNE (which is not in the Eurocontrol network). This is a minor reconciliation gap — flag for Detailed Design.
2. **Turnwise IST-NAP route example (Section 14).** The proposal acknowledges the Turnwise infographic uses an Istanbul–Naples (IST–NAP) example route and non-Australian aircraft registration (TCLPO/A21N), and commits to "reframe examples for BNE before submission." The reframe is **not yet done** in this draft. Declared, not propagated, but pending.

**Verdict:** The Athens/EU/GDPR framing is properly excluded from the proposal's commitments and replaced with Australian framing. The reconciliation is sound at the commitment level. The two residual items are acknowledged and tracked, not silently propagated. This is the correct handling per the binding hierarchy.

---

## Semantic carve-out and over-claim detection (Step 5)

| Location | Committed text | Weakening / carve-out | Downgrade |
|---|---|---|---|
| §10 SLA matrix, Sev-1 resolution | "Best-effort continuous until restored" | "best-effort" — unbounded, not the ≤4h binding commitment | **Fail** (was implicitly "Compliant") |
| §10 SLA matrix, Sev-2 resolution | "Within 1 business day" | ~8h vs RFP 4h — 2× slower presented as if it meets NF19 | **Fail** |
| §10 SLA matrix, Sev-3 resolution | "Within 3 business days" (parenthetical: "NF20: 8 business hrs committed") | Internal contradiction — the parenthetical walks back the row value | **Ambiguous** |
| §03, FR24 | "Whether each listed activity's start/end is camera-AI derived or telematics/CDM derived is to be confirmed in detailed design" | "to be confirmed" — the camera-AI origin of FR24 sub-activities is uncommitted | **Partial** |
| §03, FR48 | "Turnwise Playback replays movement on the map; raw video playback per event is to be confirmed" | "to be confirmed" — raw video playback per event uncommitted | **Partial** (DEV-12) |
| §07, A-CDM | "UTAM's NM Message Service handles A-CDM milestones... adaptable to BNE's A-CDM context" | "adaptable" — Eurocontrol NM service applied to a non-Eurocontrol airport | **Ambiguous** |
| §08, ISRA-19 | "subject to BAC confirming the preferred hosting target" | "subject to" — the sovereignty commitment is conditional on BAC election | **Partial** (acceptable; BAC-held open question) |
| §11 coverage | "Assertable (65, 38%) — reasonable from the platform's configurable architecture" | "Assertable" is itself a status word without measurable substantiation | **Ambiguous** (65 rows) |

**Over-claim check:** The proposal does not claim "100% coverage" or "Compliant" across the gap set. It is explicit that 31 rows are gaps. The one area of over-claim risk is the SLA matrix, where "Resolution target" values are presented alongside the response commitments as if the whole matrix meets NF19 — but the resolution targets do not meet NF19 items 2, 4, 5 or NF20. This is the most serious over-claim in the draft.

---

## Deviation-register completeness audit (Step 9)

The proposal includes a consolidated deviation register (Section 13) with 22 entries (DEV-01..DEV-22). Audit results:

| Shortfall | In register? | Register ID | Verdict |
|---|---|---|---|
| FR17 GSE camera classification | Yes | DEV-01 | Declared |
| FR20 personnel presence | Yes | DEV-02 | Declared |
| NF19 response matrix (response times) | Yes | DEV-03 | Declared — but DEV-03 cites only response times, not resolution times |
| **NF19 item 2 — Sev-1 resolution ≤4h** | **No** | — | **Undeclared shortfall** |
| **NF19 item 4 — Sev-2 resolution ≤4h** | **No** | — | **Undeclared shortfall** |
| **NF19 item 5 — Sev-3 response non-business day** | **No** | — | **Undeclared shortfall** |
| **NF20 — Sev-3 resolution ≤8h** | **No** | — | **Undeclared shortfall** |
| ISRA-19 data sovereignty | Yes | DEV-04 | Declared |
| ISRA-25 hosting address | Yes | DEV-05 | Declared |
| FR07 frame-rate/resolution config | Yes | DEV-06 | Declared |
| FR10 occlusion/glare detection | Yes | DEV-07 | Declared |
| FR21 restricted-zone personnel | Yes | DEV-08 | Declared |
| FR23 PPE detection | Yes | DEV-09 | Declared |
| FR26/27/69 AI governance | Yes | DEV-10 | Declared |
| FR39 exception annotations | Yes | DEV-11 | Declared |
| FR48 raw video playback | Yes | DEV-12 | Declared |
| FR72 Phase-2 aerobridge/pax | Yes | DEV-13 | Declared |
| NF05 3-year availability history | Yes | DEV-14 | Declared |
| NF09/NF10 QA standards/tools | Yes | DEV-15 | Declared |
| NF17 24/7/365 support | Yes | DEV-16 | Declared |
| NF18/NF23/NF26 help artefacts | Yes | DEV-17 | Declared |
| NF47 geolocation | Yes | DEV-18 | Declared |
| PMR-10 defects liability | Yes | DEV-19 | Declared |
| ISRA-21 privacy framing | Yes | DEV-20 | Declared |
| ISRA-24 incident-plan testing | Yes | DEV-21 | Declared |
| ISRA-27 application whitelisting | Yes | DEV-22 | Declared |

**Completeness verdict:** The register is complete for capability gaps but **incomplete for SLA resolution-time shortfalls**. DEV-03 declares the response-time commitments but omits the four resolution-time items where the proposal is below binding (NF19 items 2, 4, 5 and NF20). These four undeclared shortfalls are the most material finding in this report: they are Must-Have, they are below the binding value, and they are not in the deviation register. Per the skill, these are Fail findings ("Undeclared deviation — [requirement] requires [binding value]; proposal offers [proposal value]; not listed in deviation register.").

**Remediation:** Update DEV-03 to explicitly declare each resolution-time shortfall, or — better — revise the SLA matrix so Sev-1 resolution ≤4h, Sev-2 resolution ≤4h, Sev-3 response on non-business days ≤8h, and Sev-3 resolution ≤8h are all committed at binding value, removing the "best-effort" carve-out, the "1 business day" relaxation, and the 3-business-day/8-hour contradiction.

---

## Per-requirement validation (Step 3 + Step 6)

### Submission / RFP body requirements

| # | Requirement | Source | Verdict | Evidence / gap |
|---|---|---|---|---|
| S-01 | Proposal closing date/time (10 Jul 2026, 2pm AEST) | RFP §4.2, §6.1 | Ambiguous | Draft dated 2026-07-17 (post-close); this is a review draft, not the live submission. Pre-flight lists deadline confirmation as unresolved. |
| S-02 | Proposal validity 90 calendar days | RFP §4.2; Ann. A §1 | Pass | Cover page and §12 commit to 90 days. |
| S-03 | Insurance bars ($20M PL / $10M PI / $10M Cyber / Workers Comp) | RFP §4.4 | Pass | §12 table commits at binding; certificates to be supplied in Schedule A. |
| S-04 | Submission method (email to Leighton.Walker@bne.com.au, confidential) | RFP §4.5, §6.1 | Pass | Acknowledged; pre-flight tracks confirmation. |
| S-05 | Submission format (Excel + optional ≤5-page PDF; no sales brochures) | RFP §8 | Pass | Acknowledged; draft will be compressed. |
| S-06 | Contact information (vendor primary contact) | RFP §4.5; Response Sheet §2 | **Fail** | Placeholder — "[PLACEHOLDER — vendor primary contact...]". Blocking. |
| S-07 | Contract vehicle (BAC MSA, Annexure B) | RFP §5.1 | Pass | §12 commits to enter BAC MSA; departures returned with response. |
| S-08 | Two referees | Response Sheet Schedule C §2 | **Fail** | Not supplied; committed before submission. Blocking. |
| S-09 | Named key personnel + resumes | Response Sheet Schedule C | **Fail** | Not supplied; committed before submission. Blocking. |
| S-10 | 5-year pricing breakdown (Schedule E) | RFP §8; Response Sheet Schedule E | **Fail** | Not supplied; placeholders. Blocking. |
| S-11 | ISO 9001/20000/27001/22301 certificate evidence | Response Sheet Schedule A | **Fail** | Not supplied; committed before submission. Blocking. |
| S-12 | Insurance certificates of currency | Response Sheet Schedule A | **Fail** | Not supplied; committed before submission. Blocking. |
| S-13 | Conflict of interest disclosure | Response Sheet §7 | Ambiguous | Not addressed in proposal narrative; Response Sheet §7 to be completed. |
| S-14 | Modern Slavery Act statement | Response Sheet Social Procurement §3.1 | Ambiguous | Not addressed in proposal narrative; Social Procurement tab to be completed. |
| S-15 | Supply Nation membership | Response Sheet Social Procurement §1.1 | Ambiguous | Not addressed in proposal narrative; Social Procurement tab to be completed. |
| S-16 | ASIC requirement for airside personnel | Ann. A §14 | Pass | §05 and §06 acknowledge ASIC requirement. |
| S-17 | BAC contractor management system registration (annual fee) | Ann. A §15 | Pass | §05 and §06 acknowledge registration and fee. |
| S-18 | Addenda acknowledgment | RFP §4.10 | Partial | No addenda mentioned; mechanism acknowledged via deviation register. |

### Tab.F — Functional Requirements (FR01–FR73)

| Classification | Count | Verdict | Notes |
|---|---|---|---|
| Grounded (evidenced) | 30 | Pass | FR04, FR05, FR06, FR16, FR19, FR25, FR33–FR37, FR40, FR41, FR45–FR47, FR49, FR52, FR53, FR55, FR58, FR59, FR60–FR67. |
| Assertable (architecturally reasonable) | 32 | Ambiguous | FR01–FR03, FR08, FR09, FR11–FR15, FR18, FR22, FR24, FR28–FR32, FR38, FR42–FR44, FR48, FR50, FR51, FR54, FR56, FR57, FR68, FR70, FR71, FR73. Assumed compliant pending Test-phase evidence. |
| Gap — Must-Have, disqualifying | 2 | Partial (Blocking) | FR17, FR20. |
| Gap — Must-Have, manageable | 8 | Partial | FR07, FR10, FR21, FR23, FR26, FR27, FR69, FR72. |
| Gap — Should-Have | 1 | Partial | FR39. |

### Tab.F — Non-Functional Requirements (NF01–NF48)

| Classification | Count | Verdict | Notes |
|---|---|---|---|
| Grounded | 18 | Pass | NF02, NF04, NF06, NF07, NF15, NF16, NF25, NF32–NF36, NF39, NF41–NF43, NF45, NF46. |
| Assertable | 20 | Ambiguous | NF01, NF03, NF08, NF11–NF14, NF21, NF22, NF24, NF27–NF31, NF37, NF38, NF40, NF44, NF48. |
| Gap — Must-Have, disqualifying | 1 | Partial (Blocking) | NF19 (response matrix committed; resolution-time shortfalls — see blocking items 6-9). |
| Gap — Must-Have, manageable | 9 | Partial | NF05, NF09, NF10, NF17, NF18, NF20, NF23, NF26, NF47. |

### Tab.F — Project Management Requirements (PMR-01..PMR-10)

| Classification | Count | Verdict | Notes |
|---|---|---|---|
| Grounded | 4 | Pass | PMR-02c, PMR-02e, PMR-05, PMR-06c. |
| Assertable | 15 | Ambiguous | PMR-01, PMR-02, PMR-02a, PMR-02b, PMR-02d, PMR-02f, PMR-03, PMR-04, PMR-06, PMR-06a, PMR-06b, PMR-06d, PMR-07, PMR-08, PMR-09. |
| Gap — Should-Have sub-row | 1 | Partial | PMR-10 Table 1 (priority/response times for defects liability). Main PMR-10 Must-Have accepted. |

### Tab.F — ISRA (rows 1–29)

| Classification | Count | Verdict | Notes |
|---|---|---|---|
| Grounded | 20 | Pass | ISRA-01, 03–05, 07–09, 11–18, 20, 22, 23, 28, 29. |
| Assertable | 6 | Ambiguous | ISRA-02, 06, 10, 21, 24, 26. |
| Gap — Must-Have, disqualifying | 2 | Partial (Blocking) | ISRA-19, ISRA-25. |
| Gap — Must-Have, manageable | 1 | Partial | ISRA-27. |

---

## Cross-reference and multi-artefact consistency (Step 8)

Three-way reconciliation: RFP/Response Sheet (binding) ↔ proposal commitment ↔ UTAM/Turnwise collateral (evidence).

| Check | Result |
|---|---|
| Proposal grounded claims traceable to Turnwise/UTAM? | Yes — the "Grounded" set maps to named Turnwise features (flight tracking, stand tracking, GSE/vehicle tracking, turnaround Gantt, CDM milestones, alerts, playback, dashboards, geofence, monitoring dashboard, user/airline/GHA management, hybrid deployment, integrations). |
| UTAM AIA/Athens references leaked into proposal commitments? | No — Section 13 "Source-conflict-driven deviations" explicitly excludes them. Two residual items (NM Message Service; IST-NAP example) are acknowledged, not propagated. |
| UTAM typo "Brisbaine Airport" propagated? | No — Section 13 flags it as factually incorrect ("WAISL developed UTAM; BAC is the customer"). |
| Internal consistency of SLA matrix vs deviation register? | **Inconsistent** — DEV-03 declares response times only; the matrix's resolution-time shortfalls (Sev-1 best-effort, Sev-2 ~8h, Sev-3 3-day vs 8h contradiction, Sev-3 non-business-day missing) are not declared. |
| Coverage-matrix counts vs Section 11 counts? | Section 11 reports 74 Grounded / 65 Assertable / 31 Gap = 170. The named gap lists in §11 sum to 25 (11 FR + 10 NF + 1 PMR + 3 ISRA). The 6-row difference is in the coverage matrix (not read); the §11 lists are the authoritative in-proposal enumeration. Minor inconsistency to reconcile. |
| Pricing references consistent? | Consistent — pricing is consistently stated as out-of-scope for the draft, with Schedule E placeholders. |
| Team/personnel naming consistent? | Consistent — no named personnel anywhere; all placeholders. |
| Document attribution discipline | Correct — the report attributes Turnwise features to `Turnwise Product Document 1.pdf.md` and architecture to `UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`; no cross-attribution observed. |

---

## Page / word count assessment (Step 7)

The RFP permits the Excel response sheet plus an optional single PDF of no more than 5 pages (§8). The internal draft is ~10,086 words across 14 sections — working technical content to be compressed into the 5-page optional PDF plus Excel entries. The pre-flight checklist acknowledges this. No per-section page limit applies to the internal draft. The submission-format limit (5 PDF pages) is the binding constraint and is not yet met — the compression pass is a pre-submission step. Not blocking for a draft; blocking for submission.

---

## "Addressed within narrative" check (Step 6)

| Topic | Addressed? | Prominence |
|---|---|---|
| WHS / Safe Work Method Statements / contractor status (PMR-04) | Yes | §05 "WHS and contractor status" — adequate prominence. |
| ASIC requirement (Ann. A §14) | Yes | §05, §06 — adequate. |
| Modern Slavery / Supply Nation / social procurement | Mentioned | §02 site/regulatory context mentions RAP and Modern Slavery Act obligations; but the Social Procurement schedule is not filled. Buried; needs explicit treatment in the schedule. |
| Reconciliation Action Plan / Turrbal acknowledgment | Yes | §02 acknowledges Turrbal People and RAP — adequate. |
| Oral presentation readiness (§4.8) | Yes | §02 notes presentations will test methodology and team credibility. |
| Data ownership (BAC exclusive) | Yes | §08 "Data ownership" section — adequate. |
| Escrow (ISRA-20) | Yes | §08 and §12 — adequate. |
| Exit plan | Yes | §08 and §12 — adequate. |

---

## Adversarial critic pass (Step 10)

Findings added on the second pass:

1. **SLA resolution-time shortfalls (already above).** The most material finding. The SLA matrix reads as if it satisfies NF19, but four sub-items (Sev-1 resolution, Sev-2 resolution, Sev-3 non-business response, Sev-3 resolution/NF20) are below binding and not in the deviation register.
2. **"Assertable" is a status word.** 65 rows are marked "Assertable — architecturally reasonable." For a compliance gate, an assertion is not evidence. These are Ambiguous, not Pass. The proposal is honest about this, but the compliance posture should not treat "assertable" as "compliant" until Test-phase acceptance.
3. **FR24 "to be confirmed" carve-out.** Section 03 states "Whether each listed activity's start/end is camera-AI derived or telematics/CDM derived is to be confirmed in detailed design." FR24 is Must-Have and requires auto-detection of start/end. If the detection mechanism is "to be confirmed," FR24 is Partial, not Pass — but the proposal lists FR24 under "Assertable," not "Gap." Consider reclassifying FR24 as a gap with a delivery commitment.
4. **Coverage-matrix count discrepancy.** §11 says 31 gaps; the named lists sum to 25. Reconcile the coverage matrix or the §11 lists before submission so BAC does not find an unexplained 6-row discrepancy.
5. **NM Message Service.** Eurocontrol-specific service cited as an integration asset for BNE (non-Eurocontrol). Flagged above; needs Detailed-Design reconciliation.

---

## Pre-flight status

**NOT READY FOR ASSEMBLY.** 11 blocking issues must be resolved or formally accepted by BAC before this proposal is submission-ready:

1. FR17 camera-based GSE classification — deliver CV classifier and pass Test-phase acceptance.
2. FR20 personnel presence — deliver CV model and pass Test-phase acceptance.
3. NF19/20 SLA matrix — revise to commit Sev-1 resolution ≤4h, Sev-2 resolution ≤4h, Sev-3 response ≤8h on both business and non-business days, and Sev-3 resolution ≤8h; remove "best-effort" carve-out and the 3-day/8-hour contradiction; declare any residual shortfall in DEV-03.
4. ISRA-19 — confirm Australian hosting target with BAC at Initiation; complete ISRA.
5. ISRA-25 — supply Australian data-centre geographical address in the ISRA tab.
6. Supply Schedule C referees (2) and named key personnel/resumes.
7. Supply Schedule E 5-year pricing breakdown.
8. Supply Schedule A insurance certificates of currency and ISO 9001/20000/27001/22301 certificates.
9. Supply NF09/NF10 QA standards/tools/methodology documentation.
10. Supply vendor primary contact details (cover page).
11. Reclassify or substantiate FR24 (auto-detection mechanism "to be confirmed") and reconcile the coverage-matrix gap count (31 vs 25 named).

**Honesty note:** The draft is unusually honest about its gaps. The deviation register is well-populated for capability gaps. The single most important fix is the SLA matrix: it currently over-claims compliance with NF19/NF20 while four resolution-time sub-items are below binding and undeclared. Fix the matrix (preferred) or declare the shortfalls (minimum).

---

## Remediation instructions

| Blocking item | Remediation |
|---|---|
| FR17 | Deliver CV classifier in Phase 1; agree per-class precision/recall in Detailed Design; pass Test-phase acceptance; then mark FR17 conformant. 20% withhold protects BAC meanwhile. |
| FR20 | Deliver personnel-presence CV model in Phase 1; pass Test-phase acceptance; then mark FR20 conformant. |
| NF19/NF20 resolution times | Revise §10 SLA matrix: Sev-1 resolution ≤4h business day; Sev-2 resolution ≤4h business day; Sev-3 response ≤8h business AND non-business; Sev-3 resolution ≤8h business (NF20). Remove "best-effort." Resolve the 3-day vs 8-hour contradiction. Update DEV-03 to declare any residual. |
| ISRA-19/25 | Confirm hosting target (AWS Sydney or BAC private cloud) at Initiation; complete ISRA tab with Australian data-centre address. |
| Submission components | Populate Schedule C (referees, personnel), Schedule E (5-year pricing), Schedule A (certificates), cover page (contact), and supply NF09/NF10 QA docs. |
| FR24 | Reclassify FR24 as a Gap with a delivery commitment for camera-AI-derived start/end detection, or substantiate the detection mechanism in Detailed Design. |
| Coverage-matrix count | Reconcile §11 "31 gaps" with the 25 named gaps; either add the 6 missing rows to the §11 lists or correct the headline count. |

---

## Notes on graceful degradation

- **Coverage matrix not read:** `coverage-matrix.md` is referenced by the proposal but is outside the validated artefact set. Validation is against the RFP/Response Sheet and the in-proposal §11 lists. The 31-vs-25 gap-count discrepancy is flagged for reconciliation.
- **Draft, not submission:** The proposal is explicitly "Ready for Review (draft)." Several Fail verdicts reflect placeholders the proposal commits to fill before submission. These are blocking for submission, not for continued drafting.
- **Vague RFP requirements:** RFP §4.6 gives no explicit evaluation weights. Marked Ambiguous (assumed compliant — standard evaluation criteria apply).