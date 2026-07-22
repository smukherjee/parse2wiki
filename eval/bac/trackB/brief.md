# Collateral Brief — BAC Underwing Analytics (BAC-T-26-505)

## Client Summary

**Client Name:** Brisbane Airport Corporation Pty Limited (BAC)
**Industry/Sector:** Airport operator — Brisbane Airport (BNE), Australia
**Organization Size:** Operator of Brisbane Airport under a 50-year lease (from 1997, +49-yr option); contributes >$4bn/yr to Queensland economy; thousands of employees.
**Key Stakeholders:** Leighton Walker, Technology Project Manager (Contact Officer); Terminal Operations and Airside Operations are the stated user communities ("Who is it for?").

BAC is the operator of Brisbane Airport and is procuring an enterprise-grade underwing analytics solution that uses fixed-camera infrastructure, video analytics and AI to give objective, real-time and historical visibility of aircraft turnaround operations at BNE.

## Problem Statement

> "The objective of this RFP is to procure a solution that can automatically detect, classify, timestamp, sequence, and analyse underwing activities associated with aircraft arrivals and departures, including aircraft movements, ground support equipment (GSE), personnel activity, and key turnaround processes. The solution must reduce reliance on manual data entry and provide objective, auditable, and defensible operational data aligned with BAC's airport systems." (RFP §3.2)

**Root Cause Signals:** Today turnaround visibility depends on manual timestamping and subjective reporting; growth in traffic is increasing apron complexity and safety risk; BAC wants a single source of truth for underwing operations aligned with A-CDM/AIDX and AODB.

**Desired Outcome:** Automated, camera/AI-driven detection of all turnaround activities; real-time and post-event analysis vs plan; proactive alerts; enterprise-grade security/resilience; extensible architecture; full BAC self-sufficiency through training and documentation.

## Stated Priorities

1. **Automated underwing activity detection & sequencing** — RFP §3.2/3.3 + Tab.F FR17-FR25, FR33-FR38 — Confidence: High
2. **Apron safety & personnel/zone monitoring** — RFP §3.3 + FR20-FR23, FR41 — Confidence: High
3. **Integration with BAC operational systems (AODB, FIDS, A-CDM/AIDX, REST/event APIs)** — FR15, FR33, FR54-FR56 — Confidence: High
4. **Real-time alerts & operational dashboards** — FR40-FR47 — Confidence: High
5. **AI governance: confidence scores, continuous improvement, model tuning** — FR26-FR28, FR68-FR71 — Confidence: High
6. **Security, resilience, compliance (ISRA, ISO 27001, RTO/RPO, MFA/SSO)** — NF01, NF04-NF07, ISRA 1-29 — Confidence: High
7. **Controlled project lifecycle (phased delivery, test plan, as-built, training, defects liability)** — PMR-01..PMR-10 — Confidence: High
8. **Pricing / value for money** — RFP §4.6 Evaluation Criteria; Schedule E — Confidence: High

## Evaluation Signals

**Scoring Method:** Trade-off / best-value. Standard criteria: compliance with requirements, ability to meet timeframes, cost and value for money (RFP §4.6). "Mandatory" evaluation criteria: Relevant experience, Methodology, Pricing, Requirements.
**Evaluation Factors:** Relevant experience; Methodology; Pricing; Requirements (no explicit weights given).
**Oral Presentations:** Yes — shortlisted suppliers invited to present to the Evaluation Team and SMEs (§4.8).
**Past Performance Weight:** Not explicitly weighted; "Relevant Experience" (Schedule C) and two referees required.

**Reading Between the Lines:**
- RFP repeatedly emphasises "automated", "without manual timestamping", "objective, auditable, defensible" — camera+AI detection is the differentiator, not a re-skinned flight-tracking/CDM dashboard.
- Detailed Tab.F with 73 FRs (69 Must-Have), 48 NFs, 16 PMRs, 29 ISRA rows — compliance-heavy; non-compliant or incomplete proposals may be excluded (§6.1).
- Submission is tightly bounded: Excel response sheet + optional single 5-page PDF only. No "sales brochures" (§8). This forces concise, evidence-led responses.
- Insurance bars are specific and high ($20M PL, $10M PI, $10M Cyber) — cyber insurance signals security sensitivity.
- 20% lump-sum withheld until practical completion (PMR-09) — BAC protects itself on delivery.
- Shortlisted presentations + Q&A — methodology and team credibility will be tested live.

## Vocabulary & Tone Notes

**Client's Key Terms:**
- Underwing analytics / aircraft turnaround / apron
- GSE (Ground Support Equipment), GPU/ACU, aerobridge, chocking, pushback, boarding
- AIDX, AODB, FIDS, A-CDM, CDM milestones
- Stand / gate / terminal; Airside / Terminal Operations
- MoSCoW (Must/Should/Could Have) — Tab.F uses this framing
- ISRA (Information Security Risk Assessment), ASD Essential 8, ISO/IEC 27001, NIST CSF
- "Single source of truth", "auditable, defensible"
- Turrbal People, Reconciliation Action Plan, Modern Slavery Act, Supply Nation (social procurement vocabulary)

**Tone Profile:** Formal, procurement-mechanical, risk-averse, safety- and compliance-oriented; mixes technical depth with airport-operations pragmatism. Australian English.

**Language to Avoid:** Generic "smart airport" marketing language; EU/GDPR framing (BAC is Australian — see Source Conflicts); references to Athens/AIA; "sales brochures" are explicitly disallowed.

## Collateral Inventory

| # | File / Source | Type | Summary | Depth of Analysis |
|---|--------------|------|---------|-------------------|
| 1 | `BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md` | RFP | Authoritative solicitation: scope, evaluation criteria, dates, insurances, submission mechanics, conditions, Tab.F pointers. | Deep |
| 2 | `BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md` | RFP response template | Schedules A-F: Supplier Info, Social Procurement, Relevant Experience, Methodology, Pricing, and Tab.F (FR01-FR73, NF01-NF48, PMR-01..10, ISRA 1-29). Core requirement set. Pre-tagged with "WAISL" ownership notes. | Deep |
| 3 | `Turnwise Product Document 1.pdf.md` | Org / Product collateral | WAISL Turnwise product overview: flight tracking, GSE/vehicle tracking, stand tracking, turnaround monitoring, CDM milestones, alerts, playback, dashboards, user/airline/GHA management, hybrid deployment, system integrations. | Deep |
| 4 | `UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md` | Solution architecture (prior-proposal reuse) | WAISL UTAM technical architecture: edge ingestor, vision controller, lakehouse, rules/workflow engines, RBAC/ABAC, Azure Entra SSO, MFA, HA/DR, ISO 27001, GDPR/EU residency. **Written for Athens International Airport (AIA) — mis-attributed to Brisbane.** | Deep |

## Evidence Map

### Technical Capability (underwing camera/AI analytics)
**Available Evidence:** Turnwise shows turnaround activity monitoring, Gantt, CDM milestones, GSE tracking, stand tracking, playback. UTAM describes an "Edge Vision Controller" processing CCTV/edge cameras via CV models for queue length, dwell time, wait times, processing times, security incidents; AODB/ADS-B/telematics/weather/RVR/video integration; lakehouse; rules engine; APIs.
**Gaps:** Neither doc explicitly demonstrates camera-AI auto-detection of the specific underwing activities the RFP lists (chocking, aerobridge dock/undock, stair position/removal, GPU connect/disconnect, baggage load/unload, catering, refuelling on bay, pushback readiness, cabin cleaning). No PPE detection. No personnel detection in apron zones (excluding passengers). No confidence-score-per-event or manual-validation/correction UI shown. No camera occlusion/glare detection. No explicit AIDX integration (A-CDM/AODB yes; AIDX named only via RFP).

### Past Performance / Case Studies
**Available Evidence:** None quantified. Turnwise infographic references "Flights 2024 Destinations 269,000" and an example route IST–NAP (Istanbul–Naples), implying deployment at non-Australian airports. WAISL office footprint stated as UK | India | UAE | Kuwait | Australia | Singapore.
**Gaps:** No named client engagements, no metrics for underwing-analytics deployments, no Australian airport references, no case studies. Referees (Schedule C) not provided in collateral.

### Team & Staffing
**Available Evidence:** WAISL regional offices (incl. Australia). ISO/ISMS scope implied.
**Gaps:** No named personnel, resumes, certifications of key staff, or local-support commitments for BAC. No evidence of "established relationships with required equipment suppliers" (PMR-01).

### Security & Compliance
**Available Evidence:** UTAM describes zero-trust, RBAC/ABAC, Azure Entra SSO, MFA, KMS/TLS encryption, WAF, GuardDuty, CloudTrail, immutable audit logs, ISO 27001 certification (stated), SOC-2 roadmap, RTO ≤40 min / RPO near-zero, daily backups + cross-region replication, pen-testing regime, escrow, incident handling aligned to ISO 27001.
**Gaps:** ISRA must be completed (NF01). All security narrative is framed against GDPR/EU/NIS2 and AIA/Hellenic DPA — not Australian frameworks (ASD Essential 8, Australian Privacy Act, IRAP). No evidence of 3-year availability history (NF05). No application whitelisting evidence (ISRA-27). No geolocation-on-auth evidence (NF47).

### Pricing & Commercial
**Available Evidence:** Schedule E template defines 5-year cost breakdown (Implementation, Integrations, Hardware, License, Support, Maintenance, Additional).
**Gaps:** No pricing data, no rate card, no commercial model in collateral. Civil-cost responsibility unclear (noted in response sheet).

## Confidence Map

| RFP Section / Evaluation Area | Confidence | Rationale |
|-------------------------------|------------|-----------|
| Scope & Goals (§3) | High | Clearly stated in RFP. |
| Functional Requirements (FR01-FR73) | Low-Medium | Turnwise/UTAM cover ~40-50% directly; core camera-AI underwing detection and several AI-governance FRs un evidenced. |
| Non-Functional Requirements (NF01-NF48) | Medium | Architecture addresses security/DR/IAM broadly; support SLAs, 3-yr availability, training/quick-ref-guides and several operational NFs unaddressed. |
| Project Management (PMR-01..10) | Low-Medium | Phased delivery implied but no project plan, test methodology, defects-liability, or 20%-withhold acceptance narrative in collateral. |
| ISRA (1-29) | Medium (with conflict) | Strong security architecture but framed for EU/Athens — must be re-grounded in Australian residency/standards. |
| Relevant Experience | Low | No named references, referees, or quantified case studies in collateral. |
| Methodology | Low | No delivery methodology narrative provided. |
| Pricing | Missing | No pricing collateral. |
| Submission Mechanics | High | Clearly specified (Excel + 5-page PDF; email to Contact Officer). |
| Insurance / Commercial | Medium | Stated in RFP; no evidence of supplier's current coverage. |

## Source Conflicts

**CONFLICT 1 (major): UTAM architecture is a repurposed Athens International Airport (AIA) proposal, not a Brisbane artefact.**
The UTAM Solution Architecture document repeatedly names the client as Athens International Airport / AIA and frames all compliance around the EU/GDPR/NIS2/Hellenic DPA, while the cover and some headings say "BRISBAINE" (misspelled). Manifestations:
- "to adapt the platform to Athens Airport needs (Location, Asset, etc.)"
- "All data generated, processed, or stored within the AIOP Platform remains the exclusive property of Athens International Airport (AIA)."
- "All AIA data is hosted exclusively within European Union (EU) data centres"
- "AWS EU region deployment is used to satisfy data residency requirements under GDPR and NIS2"
- "Data Hosting and Security Controls ... hosted in EU based data centers"
- DPIA references "the Hellenic Data Protection Authority"
- "developed and implemented by Brisbaine Airport" (factually wrong — WAISL developed UTAM; Athens is a customer)
- GDPR Compliance section (§12) in full, irrelevant for an Australian procuring authority
- Server-hardware/pen-test clauses addressed to "AIA"
Resolution required before drafting: rewrite all residency/compliance/ownership narrative for Australian hosting (AWS Sydney or equivalent), Australian Privacy Act 1988 / APPs, ASD Essential 8 / IRAP, and BAC as the data owner. Treat the UTAM doc as reusable technical architecture only, not as proposal text.

**CONFLICT 2 (minor): Turnwise infographic example uses Istanbul–Naples (IST–NAP) route and non-Australian aircraft reg (TCLPO / A21N).** Not a conflict per se, but signals collateral is generic/global, not Brisbane-specific. Reframe for BNE before submission.

**CONFLICT 3 (note): Response-sheet "Start" tab pre-populates ownership cells as "WAISL (PQ)", "WAISL + Vendor (kloudspot)" etc.** This indicates the response sheet is being authored from the WAISL bid perspective (with kloudspot as a vendor partner). Ensure final response does not leak internal assignment notes.

## Open Questions

- [ ] Where will BAC data be hosted (AWS Sydney region? on-prem at BAC? hybrid)? — Affects: ISRA-19, ISRA-25, NF04, all residency claims — Priority: High
- [ ] Is camera-based auto-detection of all FR24 sub-activities in scope for Phase 1, or can some be delivered as CDM/telematics-sourced timestamps? — Affects: FR13-FR14, FR17-FR18, FR24-FR28 coverage classification — Priority: High
- [ ] Does BAC have a preferred camera model list ("BAC supported camera models", FR01)? — Affects: FR01-FR04 onboarding evidence — Priority: Medium
- [ ] What is the expected 5-year pricing envelope / target ROI? — Affects: Pricing schedule — Priority: High
- [ ] Who are the named referees WAISL will offer (Schedule C requires 2)? — Affects: Relevant Experience — Priority: High
- [ ] Does BAC require ASD Essential 8 / IRAP alignment explicitly, or is ISO 27001 sufficient? — Affects: ISRA-01, ISRA-14, NF01 — Priority: Medium
- [ ] Are Phase-2 items (FR72 aerobridge pax counting, FR73 mobile/tablet) truly Must-Have in this contract or deferred? — Affects: FR72-FR73 severity — Priority: Medium
- [ ] Civil/hardware install costs — borne by BAC or supplier? — Affects: Pricing (Schedule E note) — Priority: Medium