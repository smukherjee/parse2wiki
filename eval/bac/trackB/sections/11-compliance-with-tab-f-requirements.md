# 11 — Compliance with Tab.F Requirements

## Compliance posture summary

Tab.F contains 170 requirement rows (73 FR + 48 NF + 20 PMR + 29 ISRA). Our coverage-matrix classifies them as:

- **Grounded (74, 44%)** — directly supported by Turnwise/UTAM collateral.
- **Assertable (65, 38%)** — reasonable from the platform's configurable architecture.
- **Gap (31, 18%)** — not evidenced; acknowledged and committed for delivery or accepted as contractual terms.

[GROUNDED: coverage-matrix.md — Re-tallied coverage]

This section provides the per-domain compliance declaration that will drive the Tab.F response-sheet entries. The detailed Yes/No/Partial + detail per row will be entered in the Excel Response Sheet; this narrative summarises the posture and the disqualifying-gap handling.

## Functional Requirements (FR01–FR73)

**Grounded (directly evidenced):** FR04, FR05, FR06, FR16, FR19, FR25, FR33, FR34, FR35, FR36, FR37, FR40, FR41, FR45, FR46, FR47, FR49, FR52, FR53, FR55, FR58, FR59, FR60, FR61, FR62, FR63, FR64, FR65, FR66, FR67. [GROUNDED: coverage-matrix FR rows]

**Assertable (architecturally reasonable):** FR01, FR02, FR03, FR08, FR09, FR11, FR12, FR13, FR14, FR15, FR18, FR22, FR24, FR28, FR29, FR30, FR31, FR32, FR38, FR42, FR43, FR44, FR48, FR50, FR51, FR54, FR56, FR57, FR68, FR70, FR71, FR73. [ASSERTION: coverage-matrix FR rows — assertable with caveat]

**Gap (acknowledged / committed for delivery):**

- **FR07** — configurable frame rates/resolutions per camera. [GAP — coverage-matrix FR07; committed]
- **FR10** — detect camera occlusion/lens obstruction/glare. [GAP — coverage-matrix FR10; committed]
- **FR17** — camera-based GSE type classification (disqualifying). [GAP — see Sections 03/13; committed CV delivery with acceptance criteria]
- **FR20** — personnel presence in apron zones (disqualifying). [GAP — see Sections 03/13; committed CV delivery]
- **FR21** — personnel entering restricted zones. [GAP — coverage-matrix FR21; depends on FR20]
- **FR23** — PPE detection. [GAP — coverage-matrix FR23; committed CV delivery]
- **FR26** — per-event confidence scores. [GAP — coverage-matrix FR26; committed]
- **FR27** — manual validation/correction. [GAP — coverage-matrix FR27; committed]
- **FR39** — exception annotations. [GAP — coverage-matrix FR39; addressable]
- **FR69** — per-model accuracy tracking. [GAP — coverage-matrix FR69; committed]
- **FR72** — Phase-2 aerobridge pax counting / airline data integration. [GAP — coverage-matrix FR72; roadmap]

## Non-Functional Requirements (NF01–NF48)

**Grounded:** NF02, NF04, NF06, NF07, NF15, NF16, NF25, NF32, NF33, NF34, NF35, NF36, NF39, NF41, NF42, NF43, NF45, NF46. [GROUNDED: coverage-matrix NF rows]

**Assertable:** NF01, NF03, NF08, NF11, NF12, NF13, NF14, NF21, NF22, NF24, NF27, NF28, NF29, NF30, NF31, NF37, NF38, NF40, NF44, NF48. [ASSERTION: coverage-matrix NF rows — assertable with caveat]

**Gap (acknowledged / committed):**

- **NF05** — 3-year availability history. [GAP — coverage-matrix NF05; commit to SLA reporting going forward]
- **NF09** — QA standards/accreditations/methodologies. [GAP — coverage-matrix NF09; addressable, to be supplied]
- **NF10** — QA tools & technology. [GAP — coverage-matrix NF10; addressable, to be supplied]
- **NF17** — 24/7/365 phone/email/online. [GAP — coverage-matrix NF17; committed via follow-the-sun]
- **NF18** — client-configurable help & knowledge artefacts. [GAP — coverage-matrix NF18; committed]
- **NF19** — severity response scenarios (disqualifying). [GAP — see Sections 10/13; committed matrix meeting/exceeding thresholds]
- **NF20** — Sev-3 resolution within 8 business hrs. [GAP — coverage-matrix NF20; committed]
- **NF23** — help-desk field-level info. [GAP — coverage-matrix NF23; addressable]
- **NF26** — customised quick-reference guides. [GAP — coverage-matrix NF26; committed, cost in Schedule E]
- **NF47** — geolocation on authentications. [GAP — coverage-matrix NF47; committed, low-cost]

## Project Management Requirements (PMR-01..PMR-10)

**Grounded:** PMR-02c, PMR-02e, PMR-05, PMR-06c. [GROUNDED: coverage-matrix PMR rows — UTAM IaC, blue/green, change management, implementation plan]

**Assertable:** PMR-01, PMR-02, PMR-02a, PMR-02b, PMR-02d, PMR-02f, PMR-03, PMR-04, PMR-06, PMR-06a, PMR-06b, PMR-06d, PMR-07, PMR-08, PMR-09. [ASSERTION: coverage-matrix PMR rows — standard delivery with UTAM support]

**Gap:**

- **PMR-10** — 6-month defects liability + maintenance agreement. [GAP — coverage-matrix PMR-10; accepted contractual term]

## ISRA (rows 1–29)

**Grounded:** ISRA-01, 03, 04, 05, 07, 08, 09, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 28, 29. [GROUNDED: coverage-matrix ISRA rows]

**Assertable:** ISRA-02, 06, 10, 21, 24, 26. [ASSERTION: coverage-matrix ISRA rows — assertable with caveat; ISRA-21 reframed to Australian Privacy Act]

**Gap:**

- **ISRA-19** — data sovereignty (disqualifying). [GAP — see Sections 08/13; reconciled via Australian hosting commitment — AWS Sydney or BAC private cloud]
- **ISRA-25** — hosting geographical address (disqualifying). [GAP — see Sections 08/13; reconciled via Australian address commitment]
- **ISRA-27** — application whitelisting. [GAP — coverage-matrix ISRA-27; committed in ISRA response]

## Disqualifying-gap handling summary

| Req | Gap | Handling | Where addressed |
|-----|-----|----------|-----------------|
| FR17 | Camera-based GSE type classification | Committed CV classifier delivery with per-class acceptance criteria; 20% withhold protects BAC | Sections 03, 04 (D12), 13 |
| FR20 | Personnel presence in apron zones | Committed CV model delivery with acceptance criteria; prerequisite for FR21/FR23 | Sections 03, 04 (D13), 13 |
| NF19 | Sev-1 ≤1h 24×7×365 SLA | Committed support matrix meeting/exceeding thresholds; follow-the-sun via multi-region offices; priced in Schedule E | Sections 10, 04 (D15), 13 |
| ISRA-19 | Data sovereignty | Australian hosting commitment (AWS Sydney ap-southeast-2 or BAC private cloud); rewrite all residency/privacy/ownership to Australian frame | Sections 08, 04 (D16), 13 |
| ISRA-25 | Hosting geographical address | Australian data-centre address supplied in completed ISRA tab once hosting target confirmed | Sections 08, 04 (D16), 13 |

[GROUNDED: gap-report.md §1–§3; coverage-matrix Disqualifying Gaps]

> Commercial and insurance responses are in Section 12.