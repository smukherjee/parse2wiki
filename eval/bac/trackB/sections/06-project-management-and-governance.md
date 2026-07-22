# 06 — Project Management and Governance

## Governance structure

WAISL will establish a project governance structure aligned to PMR-01..PMR-10:

- **Project Sponsor (WAISL)** — accountable for delivery, commercial, and security commitments.
- **Project Manager (WAISL)** — single point of contact for BAC's Contact Officer (Leighton Walker, Technology Project Manager), running weekly project meetings (PMR-03). [GROUNDED: RFP §4.1 Contact Officer; Response Sheet PMR-03]
- **BAC Steering Group** — Terminal Operations, Airside Operations, BAC IT&T, and BAC Information Security, meeting at phase gates.
- **Change Advisory Board (BAC)** — receives all production change requests per PMR-05/ISRA-11. [GROUNDED: UTAM change management process — coverage-matrix PMR-05/ISRA-11]
- **WAISL Australia local representative** — account escalation point for BAC (NF22). [ASSERTION: WAISL Australia office listed — coverage-matrix NF22]

## RACI summary

| Activity | WAISL PM | WAISL Sponsor | BAC Contact Officer | BAC IT&T | BAC InfoSec | BAC CAB |
|----------|----------|---------------|---------------------|----------|-------------|---------|
| PM plan & schedule | A/R | C | C | I | I | I |
| Detailed design | A/R | C | C | C | C | I |
| Build & configure | A/R | I | I | C | I | I |
| Test & UAT | A/R | I | C | C | C | I |
| Production cutover | A/R | C | C | C | C | A |
| Training | A/R | I | C | C | I | I |
| Practical completion | A/R | C | A | C | C | I |
| Defects liability | A/R | I | C | C | C | I |
| Change requests | A/R | I | C | C | C | A |
| ISRA completion | A/R | C | C | C | A | I |

[ASSERTION: standard RACI pattern for a managed-service airport delivery — coverage-matrix PMR-01..10]

## Status reporting

Weekly status reports against the PM plan, schedule, risk register, and issue log (PMR-06). Daily availability and transaction-performance data is available via API or automated email (UTAM operational commitment). [GROUNDED: UTAM Operational & Support Commitments — daily availability and transaction performance data]

## Risk and issue management

A live risk register maintained from Initiation, with likelihood/impact/mitigation/owner per NF11. Risks are reviewed at each phase gate and at weekly meetings. [ASSERTION: UTAM risk framework implied — coverage-matrix NF11] The five disqualifying gaps (FR17, FR20, NF19, ISRA-19, ISRA-25) are entered as top delivery risks with explicit mitigations (see Sections 03, 08, 10, 13).

## Personnel and contractor management

WAISL commits to certified personnel and established equipment-supplier relationships (PMR-01). [ASSERTION: WAISL Australia office + ISO certs; no named relationships/certs of personnel yet — coverage-matrix PMR-01] [GAP: named personnel, resumes, and certifications to be supplied in Schedule A/C — brief.md Evidence Map] All airside personnel will hold ASICs and be registered on the BAC contractor management system (annual fee). [GROUNDED: RFP Annexure A §14–§16]

## Documentation deliverables

The documentation set is governed by PMR-06 and its sub-rows (PMR-06a detailed design, PMR-06b test plan, PMR-06c implementation/migration plan, PMR-06d as-built), each version-controlled and accepted at phase gates before progression. [ASSERTION: standard documentation lifecycle — coverage-matrix PMR-06a–d]

## Practical completion and 20% withhold

Practical completion (PMR-09) requires cutover, successful tests, documentation, and training. Twenty per cent of the lump sum is withheld until BAC accepts practical completion. WAISL accepts this contractual term. [ASSERTION: contractual; not in collateral — coverage-matrix PMR-09] This withhold protects BAC on the delivery of the committed-but-not-yet-evidenced CV models (FR17, FR20) and the AI-governance pack (FR26/27/28/69).

## Defects liability

Six-month defects liability plus a maintenance agreement aligned to the support tiers (PMR-10), priced in Schedule E. [GAP: not in collateral — coverage-matrix PMR-10; accepted contractual term]

> Integration, data, and technical approach details are in Section 07.