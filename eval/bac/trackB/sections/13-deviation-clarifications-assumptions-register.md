# 13 — Deviation, Clarifications, and Assumptions Register

## Purpose

This register consolidates every deviation, clarification, and assumption in the proposal so that BAC can evaluate them transparently. It is the honest companion to Section 11's compliance posture: where we cannot ground a requirement, we say so here and state the mitigation.

## Disqualifying-gap deviations

| ID | Req | Deviation / Gap | Mitigation | Disposition |
|----|-----|-----------------|------------|-------------|
| DEV-01 | FR17 | Collateral evidences telematics-based GSE tracking, not camera-based classification of the full enumerated GSE-type list (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, tractors, golf carts). | Committed CV classifier delivery in Phase 1, with per-class precision/recall acceptance criteria agreed in Detailed Design; telematics identity fused with CV classification; 20% practical-completion withhold (PMR-09) protects BAC financially; named CV delivery partner in Detailed Design. | Gap acknowledged; delivery commitment; Tab.F row marked Partial pending Test-phase acceptance. [GAP — coverage-matrix FR17; gap-report.md §1] |
| DEV-02 | FR20 | No personnel-detection capability via camera is evidenced in collateral. | Committed personnel-presence CV model on the Edge Vision Controller, scoped to apron zones (excluding passenger terminal zones), with acceptance criteria; prerequisite for FR21 and FR23. | Gap acknowledged; delivery commitment; Tab.F row marked Partial pending Test-phase acceptance. [GAP — coverage-matrix FR20; gap-report.md §1] |
| DEV-03 | NF19 | No tiered support SLA matrix in collateral. | Committed Sev-1 ≤1h 24×7×365, Sev-2 ≤4h business / ≤8h non-business, Sev-3 ≤8 business hrs matrix (Section 10); follow-the-sun via WAISL UK/India/UAE/Kuwait/Australia/Singapore offices; priced in Schedule E. | Gap acknowledged; committed matrix meeting/exceeding NF19 thresholds. [GAP — coverage-matrix NF19; gap-report.md §3] |
| DEV-04 | ISRA-19 | UTAM artefact frames data sovereignty as EU residency under GDPR/NIS2 — conflicts with BAC/Australia. | Australian hosting commitment (AWS Sydney ap-southeast-2 or BAC private cloud); all residency/privacy/ownership narrative rewritten to Australian Privacy Act 1988 / APPs / ASD Essential 8 framing; BAC is the exclusive data owner. | Gap reconciled via commitment; subject to BAC confirming hosting target at Initiation. [GAP — coverage-matrix ISRA-19; gap-report.md §2; brief.md Source Conflicts] |
| DEV-05 | ISRA-25 | UTAM cites EU/Athens data-centre addresses. | Australian data-centre address (AWS Sydney ap-southeast-2 default, or BAC private-cloud address) supplied in the completed ISRA tab once hosting target confirmed. | Gap reconciled via commitment. [GAP — coverage-matrix ISRA-25; gap-report.md §2] |

## Manageable-gap deviations

| ID | Req | Deviation / Gap | Mitigation |
|----|-----|-----------------|------------|
| DEV-06 | FR07 | Per-camera frame-rate/resolution configuration not evidenced. | Committed Edge configuration pack in Detailed Design. [GAP — coverage-matrix FR07] |
| DEV-07 | FR10 | Camera occlusion/glare detection not evidenced. | Committed CV pre-processing feature with acceptance criteria. [GAP — coverage-matrix FR10] |
| DEV-08 | FR21 | Restricted-zone monitoring shown for vehicles/GSE, not personnel. | Reuses geofence + personnel CV model (depends on FR20). [GAP — coverage-matrix FR21] |
| DEV-09 | FR23 | PPE detection not evidenced. | Committed CV model where camera quality allows; acceptance criteria tied to camera-quality survey. [GAP — coverage-matrix FR23] |
| DEV-10 | FR26/27/69 | Per-event confidence scores, manual validation/correction UI, per-model accuracy tracking not evidenced. | Committed AI-governance pack (Deliverable D14) in Phase 1. [GAP — coverage-matrix FR26/27/69] |
| DEV-11 | FR39 | Exception annotations by operational staff not shown. | Committed in Detailed Design; Partial in Tab.F. [GAP — coverage-matrix FR39] |
| DEV-12 | FR48 | Raw video playback per event not confirmed (Turnwise Playback replays movement on map). | Committed in Detailed Design; Partial in Tab.F. [ASSERTION — coverage-matrix FR48] |
| DEV-13 | FR72 | Phase-2 aerobridge pax counting / airline data integration. | Roadmap commitment for Phase 2. [GAP — coverage-matrix FR72] |
| DEV-14 | NF05 | 3-year availability history not provided. | Commit to SLA reporting going forward; publish historical metrics from existing deployments if available. [GAP — coverage-matrix NF05] |
| DEV-15 | NF09/NF10 | QA standards/tools/methodology not in collateral. | To be supplied from WAISL internal QA documentation before submission. [GAP — coverage-matrix NF09/NF10; addressable] |
| DEV-16 | NF17 | 24/7/365 phone/email/online not explicitly stated. | Committed via follow-the-sun multi-region model. [GAP — coverage-matrix NF17] |
| DEV-17 | NF18/NF23/NF26 | Help/knowledge artefacts, field-level help, quick-reference guides not evidenced. | Committed in PMR-07/PMR-08; cost in Schedule E if additional. [GAP — coverage-matrix NF18/NF23/NF26] |
| DEV-18 | NF47 | Geolocation on authentications not evidenced. | Committed; low-cost feature. [GAP — coverage-matrix NF47] |
| DEV-19 | PMR-10 | 6-month defects liability + maintenance agreement not in collateral. | Accepted contractual term. [GAP — coverage-matrix PMR-10] |
| DEV-20 | ISRA-21 | UTAM frames privacy via GDPR; BAC needs Australian Privacy Act / APPs. | Reframed to Australian Privacy Act 1988 / APPs with pseudonymisation/anonymisation. [ASSERTION — coverage-matrix ISRA-21] |
| DEV-21 | ISRA-24 | Incident plans exist; regular testing not evidenced. | Committed test cadence. [ASSERTION — coverage-matrix ISRA-24] |
| DEV-22 | ISRA-27 | Application whitelisting not evidenced. | Committed in ISRA response. [GAP — coverage-matrix ISRA-27] |

## Source-conflict-driven deviations (rewrite, not propagate)

The UTAM architecture document is a repurposed Athens International Airport (AIA) artefact with EU/GDPR/Hellenic-DPA framing. The following passages are **excluded** from BAC proposal text and replaced with Australian-framed equivalents:

- "adapt the platform to Athens Airport needs" → rewritten for BNE.
- "exclusive property of Athens International Airport (AIA)" → BAC is the exclusive data owner.
- "hosted exclusively within European Union (EU) data centres" → committed to Australian hosting.
- "AWS EU region deployment ... GDPR and NIS2" → AWS Sydney ap-southeast-2 or BAC private cloud; Australian Privacy Act / APPs / ASD Essential 8.
- "the Hellenic Data Protection Authority" → removed; Australian Privacy Act / OAIC framework.
- "developed and implemented by Brisbaine Airport" (factually incorrect) → WAISL developed UTAM; BAC is the customer.
- Entire GDPR Compliance section (§12) → replaced with Australian Privacy Act compliance narrative.

[GROUNDED: brief.md Source Conflicts; gap-report.md §Source-Conflict-Driven Gaps]

## Clarifications requested from BAC

1. Hosting target — AWS Sydney (ap-southeast-2) or BAC private cloud? (affects ISRA-19, ISRA-25, NF04, all residency claims) [GAP — brief.md Open Questions]
2. Are camera-based auto-detection of all FR24 sub-activities in scope for Phase 1, or can some be delivered as CDM/telematics-sourced timestamps? (affects FR13/14, FR17/18, FR24–28 classification) [GAP — brief.md Open Questions]
3. Does BAC have a preferred camera model list ("BAC supported camera models", FR01)? [GAP — brief.md Open Questions]
4. Expected 5-year pricing envelope / target ROI? [GAP — brief.md Open Questions]
5. Does BAC require ASD Essential 8 / IRAP alignment explicitly, or is ISO 27001 sufficient? (affects ISRA-01, ISRA-14, NF01) [GAP — brief.md Open Questions]
6. Are Phase-2 items (FR72 aerobridge pax counting, FR73 mobile/tablet) truly Must-Have in this contract or deferred? [GAP — brief.md Open Questions]
7. Civil/hardware install costs — borne by BAC or supplier? [GAP — brief.md Open Questions; Response Sheet Start tab]

## Assumptions

- A1: BAC will provide AODB, FIDS, A-CDM/AIDX, and camera infrastructure access in the Test and Prod environments per the integration scope agreed at Initiation (NF08). [ASSERTION: standard — coverage-matrix NF08]
- A2: BAC will confirm the Australian hosting target (AWS Sydney or BAC private cloud) at Initiation. [ASSERTION: gating decision — brief.md Open Questions]
- A3: BAC will provide named referees and Schedule C content directly or via WAISL's reference-gathering process. [GAP: Schedule C referees not in collateral — brief.md Evidence Map]
- A4: The 5-page optional PDF will be used to present the disqualifying-gap mitigations and the FR17/FR20 CV delivery roadmap in summary form. [ASSERTION: submission strategy — RFP §8]
- A5: WAISL's Australia office provides the local account-representative escalation point (NF22) and local support presence. [ASSERTION: WAISL Australia office listed — UTAM cover page; coverage-matrix NF22]

## What we will not fabricate

We will not invent team bios, referees, case studies, pricing values, or certifications. Each of these is marked `[GAP] / placeholder` in this draft and must be supplied before submission. [GAP: brief.md Evidence Map — Past Performance, Team & Staffing, Pricing & Commercial]

> Relevant experience (and the limits of our collateral) is addressed in Section 14.