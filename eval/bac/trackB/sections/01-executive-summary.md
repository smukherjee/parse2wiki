# 01 — Executive Summary

## BAC's problem, in BAC's words

Brisbane Airport Corporation (BAC) is procuring an enterprise-grade underwing analytics solution that "automatically detect[s], classif[ies], timestamp[s], sequence[s], and analyse[s] underwing activities" using "fixed camera infrastructure, advanced video analytics, and artificial intelligence" (RFP §3.2). The objective is to replace manual timestamping and subjective reporting with "objective, auditable, and defensible operational data aligned with BAC's airport systems" — a single source of truth for Terminal Operations and Airside Operations across BNE's apron. [GROUNDED: BAC-T-26-505 RFP §3.2/§3.3]

The scope is broad and compliance-heavy: 73 functional requirements (69 Must-Have), 48 non-functional, 20 project-management, and 29 ISRA rows in Tab.F, plus insurance bars of $20M public liability, $10M professional indemnity, and $10M cyber. Twenty per cent of the lump sum is withheld until practical completion (PMR-09), signalling that BAC protects itself on delivery. [GROUNDED: RFP §4.4, Response Sheet Tab.F]

## What WAISL proposes

WAISL, operating through its Australia office and alongside its delivery partner, proposes a Turnwise/UTAM-based underwing analytics platform delivered as a managed service for BNE. The platform already performs real-time aircraft/stand/turnaround tracking, CDM milestone monitoring, GSE and vehicle tracking, configurable alerts, dashboards, KPI and SLA reporting, playback, geofenced zone monitoring, and AODB/ADS-B/telematics/weather/RVR integration — capabilities that directly address the operational-visibility and integration backbone of the RFP. [GROUNDED: Turnwise Product Document 1; UTAM Solution Architecture v1]

The solution is parameterised over code, deployable in AWS cloud or BAC private cloud, secured under a zero-trust architecture with ISO 27001-certified ISMS controls, and delivered against RTO ≤40 minutes and RPO near-zero. [GROUNDED: UTAM Solution Architecture v1 — deployment agnosticism, ISO 27001, HA/DR table]

## Where we are strong and where we are honest

We are directly grounded against approximately 44% of Tab.F (turnaround timeline, CDM milestones, dashboards, alerts, AODB/REST APIs, RBAC/ABAC, SSO/MFA, HA/DR, audit, ISO 27001, escrow, change management). A further 38% is assertable from the platform's configurable architecture. [GROUNDED: coverage-matrix.md summary]

We will not overstate. Five areas require explicit treatment in this proposal:

1. **Camera-AI detection of the full GSE-type list (FR17) and personnel presence in apron zones (FR20).** Our current GSE evidence is telematics/GPS-based, not camera-classified against every enumerated type, and personnel presence via camera is not yet evidenced in our collateral. We address these honestly in Section 03 and 13, with a delivery roadmap, computer-vision model commitments, and acceptance criteria — not fabricated claims. [GAP: FR17, FR20 — see gap-report.md §1]
2. **Support SLA matrix (NF19).** Collateral does not state a tiered response matrix. We commit to a Sev-1 ≤1-hour 24×7×365 response matrix, backed by WAISL's follow-the-sun UK/India/UAE/Kuwait/Australia/Singapore footprint, and price it in Schedule E. [GAP: NF19 — addressed via committed matrix]
3. **Data sovereignty and hosting address (ISRA-19, ISRA-25).** Our reusable architecture artefact was written for a European customer and framed around GDPR/EU residency. For BAC we commit to Australian hosting — AWS Sydney (`ap-southeast-2`) or BAC private cloud — and we rewrite every residency, privacy, and ownership narrative to the Australian Privacy Act 1988 / APPs and ASD Essential 8 framing. [GAP: ISRA-19, ISRA-25 — reconciled via Australian re-host commitment]

## Why WAISL

WAISL is an airport-operations software house with a multi-region presence including Australia, ISO 9001/20000/27001/22301 certifications, and a productised Turnwise/UTAM platform already in airport use. [GROUNDED: UTAM cover page — certifications and office footprint; Turnwise Product Document 1] We offer BAC a parameterised, configurable, extensible platform rather than a bespoke build, and we commit to the controlled, phased, auditable delivery lifecycle Tab.F PMR demands.

> The technical solution that delivers these benefits is described in Section 03; the scope coverage and deliverables in Section 04.