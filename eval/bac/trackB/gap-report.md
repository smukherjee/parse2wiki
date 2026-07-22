# Gap Report — BAC Underwing Analytics (BAC-T-26-505)

Companion to `coverage-matrix.md` and `brief.md`. Gaps are grouped by theme and severity. Marker discipline: `[GROUNDED]` / `[ASSERTION]` / `[GAP]`.

## Disqualifying Gaps (bid-critical; resolve before submission)

### 1. Camera-AI underwing detection is the RFP's core ask — and the weakest evidence area
The RFP's central objective (§3.2) is a solution that "automatically detect[s], classif[ies], timestamp[s], sequence[s], and analyse[s] underwing activities" using "fixed camera infrastructure, advanced video analytics, and artificial intelligence." The supplier collateral leans on flight-tracking, CDM milestones, ADS-B and telematics — not camera-AI detection of the specific activities Tab.F lists.

- **FR17 — GSE type classification via camera (loaders, tugs, water, waste, stairs, catering, refuelling, GPU/ACU, tow bars, tractors, golf carts).** `[GAP]` Turnwise tracks GSE via telematics/GPS and shows a "vehicle type" field, but there is no evidence of camera-based classification of the full enumerated list. Mandatory Must-Have. Severity: **Disqualifying**.
- **FR20 — Personnel presence detection in apron zones (excluding passengers).** `[GAP]` No personnel-detection capability is evidenced in either Turnwise or UTAM. UTAM's Edge Vision Controller extracts "queue length, dwell time, wait times, processing times, security incidents" — not personnel presence in defined zones. Mandatory. Severity: **Disqualifying**.
- **FR23 — PPE detection.** `[GAP]` Not mentioned. Mandatory Must-Have. Severity: Manageable (conditional on camera quality) but still a Gap.

**Recommended action:** Escalate immediately. Either (a) produce evidence of prior WAISL/kloudspot deployments that perform camera-AI detection of these classes, (b) partner with a specialist computer-vision vendor and commit to a delivery roadmap with acceptance criteria, or (c) reconsider bid. Drafting cannot credibly proceed without one of these.

### 2. Data sovereignty / hosting location — source conflict vs BAC
The UTAM architecture document asserts, repeatedly, that all data is hosted exclusively in EU data centres to satisfy GDPR/NIS2, and names the client as Athens International Airport (AIA). For a Brisbane Airport Corporation procurement, this is both a source conflict (see `brief.md` §Source Conflicts) and a direct gap against mandatory ISRA rows.

- **ISRA-19 — Data sovereignty management.** `[GAP]` UTAM evidence answers with EU residency. Required answer: Australian sovereignty (and Australian Privacy Act / APPs / ASD Essential 8 framing, not GDPR). Severity: **Disqualifying**.
- **ISRA-25 — Hosting geographical address.** `[GAP]` UTAM cites EU/Athens addresses. Required: an Australian data-centre address (e.g., AWS Sydney `ap-southeast-2`) or BAC on-prem. Severity: **Disqualifying**.

**Recommended action:** Commit in writing to Australian hosting (AWS Sydney region or BAC private cloud — UTAM already claims "deployment agnosticism" and a private-cloud option, so this is reconcilable). Rewrite all residency, compliance, privacy, and data-ownership narrative for the Australian regulatory frame. Remove every AIA/Athens/Hellenic-DPA/GDPR reference from proposal text. Severity drops to Addressable once a concrete Australian address and re-hosting commitment are in the response.

### 3. Support SLA matrix
- **NF19 — Severity-1 response within 1 hour 24×7×365; Sev-2 within 4 hrs business-day / 8 hrs non-business; Sev-3 within 8 hrs; resolution commitments.** `[GAP]` Neither Turnwise nor UTAM provides a support-tier response matrix or evidence of 24/7/365 capability. Mandatory Must-Have. Severity: **Disqualifying**.
- Related: **NF20** (Sev-3 resolution in 8 business hrs) — Gap/Manageable; **NF17** (24/7/365 phone/email/online) — Gap/Manageable.

**Recommended action:** Define a support model with a tier-based response matrix meeting or exceeding NF19 thresholds, and evidence the 24/7/365 capability (follow-the-sun across WAISL's UK/India/UAE/Kuwait/Australia/Singapore offices is a credible answer). Provide cost implications in Schedule E.

## Manageable Gaps (deductible but not eliminating)

| Req IDs | Theme | Gap | Mitigation |
|---------|-------|-----|------------|
| FR07, FR10, FR11, FR12 | Camera configuration & health | Configurable frame-rate/resolution per camera, occlusion/glare detection, AI-accuracy-degradation alerts, camera health dashboard not evidenced | Assert via UTAM Rules Engine + Monitoring Dashboard; commit to FR-by-FR conformance in Tab.F; demo at presentation |
| FR21 | Personnel entering restricted zones | Restricted-zone monitoring shown for vehicles/GSE, not personnel | Reuse geofence + CV personnel model (depends on FR20 resolution) |
| FR26, FR27, FR28, FR69 | AI confidence & validation | Per-event confidence scores, manual validation/correction UI, learning loop, per-model accuracy tracking not evidenced | Assert platform capability; provide mockups; commit in detailed design |
| FR39, FR48 | Annotations & video playback per event | Exception annotations not shown; Turnwise Playback is movement-replay, not raw video per event | Clarify in Tab.F (Partial + detail) and proposal PDF |
| FR43 | Alert channels incl. AIDX API | UTAM covers SMS/voice/email/Teams/TETRA/web; AIDX-specific API alert channel not confirmed | Add AIDX alert publication via API Gateway; assert in Tab.F |
| FR72, FR73 | Phase 2 FRs | Aerobridge pax counting & mobile/tablet remote access not in collateral | Commit to roadmap (FR72) and responsive UI (FR73) |
| NF05 | 3-year availability history | Not provided | If WAISL has operational deployments, publish availability metrics; otherwise assert and commit to SLA reporting going forward |
| NF18, NF23, NF26 | Help/knowledge artefacts, field-level help, quick-ref guides | Not evidenced | Commit to deliverables in PMR-07/PMR-08; price in Schedule E if additional |
| NF47 | Geolocation on authentications | Not evidenced | Assert or commit; low-cost feature |
| PMR-10 | 6-month defects liability + maintenance agreement | Not in collateral | Accept contractual term; commit in Schedule D methodology |
| ISRA-21 | Privacy / right to anonymity | UTAM frames via GDPR; BAC needs Australian Privacy Act / APPs | Reframe narrative |
| ISRA-24 | Incident plans tested regularly | Plan exists; regular testing not evidenced | Commit to test cadence |
| ISRA-27 | Application whitelisting | Not evidenced | Commit in ISRA response |

## Addressable Gaps (evidence likely exists; seek before drafting)

| Req IDs | Theme | Action |
|---------|-------|--------|
| FR01-FR03, FR08, FR13-FR15 | Camera onboarding, FOV/parking-zone config, time-sync, AIDX | Likely deliverable via UTAM Edge layer; confirm with engineering and provide specifics in Tab.F |
| NF09, NF10 | QA standards, tools, methodology | Likely internal to WAISL; obtain QA process doc + tool list |
| NF23 | Help-desk field-level info | Standard help capability; confirm with support team |
| ISRA-02, ISRA-06, ISRA-26 | Sensitive-data scope, contractual infosec roles, staff vetting | Standard; confirm with WAISL security/legal |

## Source-Conflict-Driven Gaps (must rewrite, not just fill)

The UTAM document is, on its face, a redacted Athens International Airport response repurposed for Brisbane without cleaning the body text. Conflicting passages that must not appear in the BAC response:
- "adapt the platform to Athens Airport needs"
- "exclusive property of Athens International Airport (AIA)"
- "hosted exclusively within European Union (EU) data centres"
- "AWS EU region deployment ... GDPR and NIS2"
- "the Hellenic Data Protection Authority"
- "developed and implemented by Brisbaine Airport" (factually incorrect)
- Entire GDPR Compliance section (§12) and EU-residency assurances

Every ISRA row that the UTAM doc answers with EU/GDPR framing must be re-answered for the Australian context. The conflict directly produces the two Disqualifying gaps above (ISRA-19, ISRA-25) and weakens the credibility of ISRA-21 (privacy) and ISRA-23 (compliance management).

## What the Collateral Supports Confidently (Grounded areas, drafter can cite)

- Aircraft/flight tracking, stand occupancy, turnaround timeline & CDM milestones (FR16, FR19, FR25, FR33-FR37, FR45-FR47, FR49, FR53, FR59)
- AODB integration, REST/event APIs, configurable retention, playback (FR33, FR55, FR58, FR59)
- Dashboards, alerts for SLA/speed/restricted-zone, KPI/reporting, self-service BI (FR40-FR41, FR45-FR53, NF25)
- RBAC/ABAC, airline/service-provider data segregation, admin config, Dev/Test/Prod, SSO (Azure Entra), MFA, no browser plug-ins (FR60-FR67, NF32-NF43)
- Security architecture: encryption, KMS, WAF, GuardDuty, CloudTrail, audit, incident handling, ISO 27001, HA/DR (RTO ≤40 min / RPO near-zero), pen-test regime, escrow (ISRA-01, 03-05, 07-09, 11-18, 20, 22-23, 28-29; NF04-NF07, NF15-NF16, NF32-NF46)
- Build/implementation with rollback, change management feeding CAB, IaC env parity (PMR-02c, 02e, 05, 06c)

## Pre-Drafting Action List

1. **Resolve the 5 Disqualifying gaps** (FR17, FR20, NF19, ISRA-19, ISRA-25) — no drafting of the affected Tab.F rows or methodology narrative should proceed without a decision on each.
2. **Rewrite the UTAM/AIA/EU narrative** for Brisbane/Australia — this is a gating edit; the architecture content is reusable, the compliance/residency/ownership text is not.
3. **Gather evidence for Addressable gaps** (QA methodology, field-level help, camera specifics) — low effort, high value.
4. **Prepare Tab.F conformance answers** with explicit Yes/No/Partial + detail per row, using this matrix as the checklist — do not leave Must-Have rows blank or vague.
5. **Confirm Australian hosting address and support SLA matrix** and feed both into the ISRA tab and Schedule D/Pricing.
6. **Line up two referees (Schedule C)** with relevant underwing/airport-analytics deployments — currently no reference evidence exists in collateral.