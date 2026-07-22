# 02 — Understanding of Requirements

## What BAC is asking for

BAC's objective, stated in RFP §3.2, is to procure a solution that can "automatically detect, classify, timestamp, sequence, and analyse underwing activities associated with aircraft arrivals and departures, including aircraft movements, ground support equipment (GSE), personnel activity, and key turnaround processes." The solution must "reduce reliance on manual data entry and provide objective, auditable, and defensible operational data aligned with BAC's airport systems." [GROUNDED: BAC-T-26-505 RFP §3.2]

The scope of work (RFP §3.3) enumerates eleven high-level outcomes: secure camera/video ingestion; aircraft identification and positioning via operational flight data fused with visual detection; apron safety via automated personnel detection and zone monitoring; automatic detection, sequencing, and visualisation of all key turnaround activities without manual timestamping; real-time and post-event analysis vs plan; transparent and continuously improving AI; configurable proactive alerts; intuitive operational and analytical visibility; seamless integration across BAC operational, enterprise, and data systems; mission-critical security/resilience/compliance; and a controlled, transparent, auditable project lifecycle with full BAC self-sufficiency. [GROUNDED: RFP §3.3]

## How requirements are organised

BAC has structured the response in the Excel Response Sheet around six schedules: Supplier Information, Social Procurement, Relevant Experience, Methodology, Pricing, and Tab.F Requirements. Tab.F decomposes the requirement set into:

- **Functional Requirements (FR01–FR73)** — 73 rows, 69 Must-Have, covering camera onboarding, aircraft detection, GSE classification, personnel/zone monitoring, turnaround activity detection, sequencing, AI governance, alerts, dashboards, reporting, integration, and administration.
- **Non-Functional Requirements (NF01–NF48)** — 48 rows covering availability/DR, support, training, accessibility, IAM, browser compatibility, and logging.
- **Project Management Requirements (PMR-01..PMR-10, with sub-rows 02a–02f and 06a–06d)** — 20 rows covering phased delivery, weekly meetings, WHS, change control, documentation, training, practical completion with 20% withhold, and six-month defects liability.
- **ISRA (rows 1–29)** — Information Security Risk Assessment rows covering ISO 27001, PII handling, retention, privileged access, breach notification, change management, incident response, cryptographic controls, resilience, data sovereignty, escrow, privacy, physical/environmental security, compliance management, incident testing, vetting, application whitelisting, MFA, and log management. [GROUNDED: Response Sheet Tab.F; coverage-matrix.md reconciliation]

## Our reading of the priorities

The RFP's emphasis is unambiguous. The words "automated", "without manual timestamping", and "objective, auditable, defensible" recur (§3.2, §3.3). Camera-plus-AI detection of the specific underwing activities in FR17 and FR24 is the core differentiator — a re-skinned flight-tracking or CDM dashboard will not satisfy it. The detailed Tab.F (170 rows) and the statement that incomplete or non-compliant proposals "may be excluded" (§6.1) make this a compliance-heavy procurement. [GROUNDED: RFP §6.1; §3.2/§3.3]

The user communities are Terminal Operations and Airside Operations (RFP §3.4 "Who is it for?"). Expected benefits cluster around improved apron safety via automated personnel detection, enhanced operational efficiency via automated turnaround tracking and earlier delay detection, and improved on-time performance via proactive intervention. [GROUNDED: RFP §3.4]

## Constraints and commercial signals

- **Submission is tightly bounded** — the Excel response sheet plus an optional single PDF of no more than 5 pages; "no sales brochures" (§8). This forces concise, evidence-led responses. [GROUNDED: RFP §8]
- **Insurance bars are specific and high** — $20M PL, $10M PI, $10M Cyber (§4.4). Cyber insurance signals security sensitivity. [GROUNDED: RFP §4.4]
- **20% lump-sum withhold until practical completion** (PMR-09) — BAC protects itself on delivery. [GROUNDED: Response Sheet Tab.F PMR-09]
- **Term** — 3 years initial, with two by-one-year extensions tied to SLA, sustainability and performance targets (§4.3). [GROUNDED: RFP §4.3]
- **Oral presentations** — shortlisted suppliers present to the Evaluation Team and SMEs (§4.8). Methodology and team credibility will be tested live. [GROUNDED: RFP §4.8]
- **Evaluation criteria** — Relevant experience, Methodology, Pricing, Requirements (mandatory, §4.6). No explicit weights given. [GROUNDED: RFP §4.6]

## Site and regulatory context

BNE operates under a 50-year lease (from 1997, with a 49-year option) and contributes more than $4bn/yr to Queensland's economy. Work is performed on the land of the Turrbal People, and BAC's Reconciliation Action Plan, Modern Slavery Act obligations, and Supply Nation social procurement expectations apply (Schedule B). [GROUNDED: RFP §1.1, §1.2, Response Sheet Schedule B] Aviation security legislation (Aviation Transport Security Act 2004, CASA Manual of Standards Part 139, Airports Act 1996) applies to all on-airport work, and Aviation Security Identification Cards (ASICs) are required for personnel. [GROUNDED: RFP Annexure A §14–§16]

## Where our understanding diverges from collateral reality

We have mapped each of the 170 Tab.F rows to a coverage classification (Grounded / Assertable / Gap) in `coverage-matrix.md`. We do not pretend that our existing collateral satisfies every Must-Have row. In particular, five disqualifying gaps must be resolved before this proposal can be considered compliant: FR17 (camera-based GSE type classification), FR20 (personnel presence in apron zones), NF19 (tiered support SLA), ISRA-19 (data sovereignty), and ISRA-25 (hosting geographical address). Each is addressed explicitly in Sections 03, 08, 10, and 13. [GROUNDED: coverage-matrix.md — Disqualifying Gaps; gap-report.md §1–§3]

> Our technical response to these requirements is set out in Section 03.