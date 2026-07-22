# Track A Proposal — Post-Hoc Claim Audit

**Proposal audited:** `eval/bac/trackA/proposal-trackA.md` (Underwing Analytics, BAC-T-26-505, WAISL/TurnWise/UTAM)
**Sources used for grounding:**
- `sources/BAC/BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md` (RFP)
- `sources/BAC/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md` (Response Sheet)
- `sources/BAC/Turnwise Product Document 1.pdf.md` (TurnWise product doc)
- `sources/BAC/UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md` (UTAM architecture doc)

**Method:** Every substantive factual claim extracted and classified as GROUNDED (directly supported by a source, with location), PLACEHOLDER (explicitly flagged "to be confirmed"/missing — not a fabrication), UNSUPPORTED (asserted as fact with no source backing — potential hallucination), or FABRICATED (contradicts sources or invents projects/numbers/people/certifications — definite hallucination). Reconciliation claims (the proposal explicitly re-maps European source artefacts to the Brisbane/Australian context) are judged on whether the underlying source fact exists and whether the Australian replacement is grounded in a source; accurate real-world facts not present in any source are marked UNSUPPORTED (not FABRICATED, since they are not invented).

**Legend:** RFP = RFP.pdf.md; RS = Supplier Response Sheet; TW = TurnWise Product Document; UTAM = UTAM Solution Architecture doc.

---

## Claim Table

| # | Section | Claim | Verdict | Source / Note |
|---|---|---|---|---|
| 1 | Cover | RFP reference BAC-T-26-505 | GROUNDED | RFP cover ("BAC-T-26-505") |
| 2 | Cover | Response date 10 July 2026 | GROUNDED | RFP 4.2 closing date; RS "Response Due Date: 2026-07-10" |
| 3 | Cover | Proposal validity 90 calendar days from closing | GROUNDED | RFP 4.2; Annexure A clause 1 |
| 4 | Cover | Contact officer Leighton Walker, Technology Project Manager, BAC, 11 The Circuit Brisbane, PO Box 61 Hamilton Central, Leighton.Walker@bne.com.au | GROUNDED | RFP 4.1; RS Key BAC Contact |
| 5 | Cover | Bidder WAISL Limited with proposed delivery partner Kloudspot (role/credentials TBC) | PLACEHOLDER | RS Sheet1 names "WAISL + Vendor (kloudspot)"; Kloudspot company details/certs/referees absent → flagged TBC (D04) |
| 6 | Cover | WAISL + Kloudspot named as responsible parties for FR/NFR/PM/ISRA | GROUNDED | RS Sheet1 responsibility diagram ("WAISL + Vendor (kloudspot)") |
| 7 | Cover | Willingness to accept MSA subject to departures; unlisted departures deemed accepted | GROUNDED | RFP 5.1 ("deemed to be accepted with any departures") |
| 8 | Cover | Will obtain ASIC for airside personnel; register/maintain BAC contractor mgmt system | GROUNDED | RFP Annexure A clauses 14, 15 |
| 9 | Cover | Insurance compliance per RFP Section 4.4 | GROUNDED | RFP 4.4 |
| 10 | Cover | Authorised representative name/title/contact | PLACEHOLDER | Explicitly "to be confirmed from bidder input" |
| 11 | Cover | Signature | PLACEHOLDER | Explicitly "to be confirmed" |
| 12 | Exec | Solution uses fixed cameras, video analytics, AI for real-time/historical turnaround visibility | GROUNDED | RFP 3.1, 3.2 |
| 13 | Exec | Detect/classify/timestamp/sequence/analyse underwing activities; reduce manual data entry; auditable/defensible data | GROUNDED | RFP 3.2 |
| 14 | Exec | TurnWise platform delivered as UTAM | GROUNDED | UTAM ("TurnWise... Unified Total Airside Management (UTAM)"); TW |
| 15 | Exec | Ingests AODB, ADS-B, GSE telematics, weather, RVR, video from fixed apron cameras | GROUNDED | UTAM Executive Summary; UTAM Edge Data Ingestor; TW Monitoring Dashboard (AODB/ADSB/Video/Vehicle) |
| 16 | Exec | Edge Vision Controller runs CV at the edge, extracts structured metadata on GSE/personnel/chocking/aerobridge/baggage/catering/refuelling/pushback/cabin-cleaning | GROUNDED | UTAM Edge Vision Controller; FR17/FR24 list these activities |
| 17 | Exec | Lakehouse-based core sequences events into per-flight turnaround timelines; planned vs actual; delay attribution; alerts via dashboard/email/AIDX | GROUNDED | UTAM Lakehouse (Bronze/Silver/Gold); FR25/FR34/FR35/FR40/FR43 |
| 18 | Exec | Addresses BAC goals: apron safety, operational efficiency, on-time performance | GROUNDED | RFP 3.4 Expected Benefits table |
| 19 | Exec | Configuration over code; BAC teams adjust geofences/workflows/alert thresholds/turnaround templates without release cycles | GROUNDED | UTAM "configuration over code"; UTAM Rules Engine low-code |
| 20 | Exec | Azure AD identity provider via SAML2 SSO | GROUNDED | NF42 ("SAML2 (BAC uses Azure AD as our idP)") |
| 21 | Exec | RBAC with airline- and handler-specific data segregation | GROUNDED | FR60, FR61 |
| 22 | Exec | Multi-AZ deployment pattern with 4-hour RTO | GROUNDED | UTAM HA/DR (Multi-AZ); NF07 (4-hour RTO) |
| 23 | Exec | 73 functional requirements (69 Must Have) | GROUNDED | RS Sheet1 ("73 FRQ, 69 must have"); RS FR tab (FR06/FR12/FR39/FR48 are the 4 non-Must) |
| 24 | Exec | All 48 non-functional requirements | GROUNDED | RS NF01-NF48 (48 rows, all Must Have) |
| 25 | Exec | 29-question Information Security Risk Assessment | GROUNDED | RS ISRA IDs 1-29 (row 30 is "Spare") |
| 26 | Exec | Source collateral carries AIA/Athens, EU data residency, GDPR, NIS2 artefacts | GROUNDED | UTAM (AIA/Athens, GDPR, NIS2, "AWS - EU Regions", "Hellenic Data Protection Authority") |
| 27 | Exec | Reconciled to aviation regulatory acts: CASA Manual of Standards Part 139, Airports Act 1996, Civil Aviation Act 1988, Aviation Transport Security Act 2004 | GROUNDED | RFP Annexure A clause 16(a)-(c) |
| 28 | Exec | Reconciled to Privacy Act 1988 (Cth) and Australian Privacy Principles as the governing privacy regime | UNSUPPORTED | Accurate real-world law, but not named in any source (sources reference GDPR). Asserted as fact without source backing. Not a fabrication (it is real law, not contradicted by BAC requirements). |
| 29 | Exec | WAISL holds offices in UK, India, UAE, Kuwait, Australia, Singapore | GROUNDED | UTAM cover ("UK \| INDIA \| UAE \| KUWAIT \| AUSTRALIA \| SINGAPORE") |
| 30 | Exec | Local Australian presence satisfies NF22 local account representative | GROUNDED | NF22 (local representative); offices include Australia (UTAM) |
| 31 | UoR | BAC operates BNE under 50-year lease (49-year renewal option) acquired from Federal Government in 1997 | GROUNDED | RFP 1.1 |
| 32 | UoR | 2020 Master Plan approved by Australian Government on 10 March 2020; 20-year blueprint | GROUNDED | RFP 1.3 |
| 33 | UoR | AODB, FIDS, A-CDM (AIDX) integration targets; REST and event-based APIs; publish actual timestamps | GROUNDED | FR54, FR55, FR56 |
| 34 | UoR | Azure AD SAML2 federated SSO mandatory | GROUNDED | NF42 |
| 35 | UoR | Event metadata separate from video; configurable retention; forensic replay | GROUNDED | FR57, FR58, FR59 |
| 36 | UoR | RBAC, airline/service-provider data segregation, configurable permissions per role, env separation Dev/Test/Prod are Must Have | GROUNDED | FR60-FR64 (all Must Have) |
| 37 | UoR | 24/7/365 support over phone, email, online help | GROUNDED | NF17 |
| 38 | UoR | Severity 1 response within 1 hour; resolution/plan within 4 hours | GROUNDED | NF19 (items 1-2) |
| 39 | UoR | Four-hour Recovery Time Objective | GROUNDED | NF07 |
| 40 | UoR | 3-year system availability history required | GROUNDED | NF05 (requirement exists); figures TBC separately |
| 41 | UoR | ISRA aligned to ISO/IEC 27001, ASD Essential 8, BAC Information Security Policy 2018, NIST CSF 2014 | GROUNDED | RS ISRA General Principles & Guidelines |
| 42 | UoR | 3-year initial term; two 1-year extensions on SLA/sustainability/performance targets | GROUNDED | RFP 4.3 |
| 43 | UoR | ASIC required for airside personnel; contractor management system registration with annual fee | GROUNDED | RFP Annexure A clauses 14, 15 |
| 44 | UoR | Aviation regulatory framework (Part 139, Airports Act 1996, Civil Aviation Act 1988, Aviation Transport Security Act 2004) bears on delivery | GROUNDED | RFP Annexure A clause 16 |
| 45 | 4.2 | GSE detection/classification against FR17 taxonomy (baggage loaders, tugs, water/waste vehicles, stairs, catering, refuelling, GPUs/ACUs, tow bars/pushback, general support) | GROUNDED | FR17 |
| 46 | 4.2 | Ready/arrival/departure timestamps per GSE type (FR18); presence on stand (FR19); 15-min path plotting | GROUNDED | FR18, FR19; TW ("path traversed by vehicle... last 15 minutes") |
| 47 | 4.2 | Turnaround detection of FR24 activity set; sequencing FR25; confidence FR26; manual validation FR27; learning FR28 | GROUNDED | FR24, FR25, FR26, FR27, FR28 |
| 48 | 4.2 | Airline-specific/movement-type workflows (Originator/Turnaround/Terminator I/D) FR29; aircraft-type sequences FR30; mandatory/optional FR31; dependency/precedence FR32 | GROUNDED | FR29-FR32 |
| 49 | 4.2 | Aircraft arrival/departure detection FR13/FR14; AIDX identification FR15; AODB correlation FR16; Flight Summary and POBT view | GROUNDED | FR13-FR16; TW ("Flight Summary and POBT") |
| 50 | 4.2 | Alerts on duration exceedance FR40, unsafe/prohibited activity FR41, camera/AI confidence degradation FR42; delivery via dashboard/email/AIDX FR43; context/severity/recommended actions FR44; low-code rules engine | GROUNDED | FR40-FR44; UTAM Rules Engine (low-code) |
| 51 | 4.2 | Turnaround KPIs by airline/aircraft type/gate/service provider FR49; trend/variance FR50; AI insights FR51; ad-hoc queries FR52; historical analysis FR53 | GROUNDED | FR49-FR53 |
| 52 | 4.2 | Event metadata stored separate from video FR57; configurable retention FR58; forensic replay FR59 | GROUNDED | FR57-FR59 |
| 53 | 4.2 | Versioned AI models FR68; per-model accuracy FR69; airport-specific tuning FR70; continual improvement FR71 | GROUNDED | FR68-FR71 |
| 54 | 4.2 | Live turnaround status board per gate FR45; current/next-milestone FR46; colour-coded delay FR47; live/historical video playback FR48 | GROUNDED | FR45-FR48 |
| 55 | 4.2 | Operational reports: turnaround SLA, flight-wise and airline-wise OTP, GSE usage master, vehicle last location, speed violation, restricted-zone entry | GROUNDED | TW Operational Reports section |
| 56 | 4.3 | Camera onboarding FR01; grouping FR02; FOV/parking zones FR03; geofenced zones FR04; live video FR05; buffering FR06; configurable frame rate/resolution FR07; synchronised timestamp FR08; camera health FR09; occlusion/glare FR10; degradation alerts FR11; camera health dashboard FR12 | GROUNDED | FR01-FR12 (RS FR tab) |
| 57 | 4.4 | Personnel detection (excl. PAX) FR20; restricted-zone entry FR21; unsafe dwell times FR22; PPE detection where camera quality allows FR23; Airside Safety & Restricted Zone Monitoring module; speed violation report | GROUNDED | FR20-FR23; TW ("Airside Safety and Restricted Zone Monitoring", "Speed Violation Report") |
| 58 | 4.5 | AODB/FIDS/A-CDM via AIDX FR54; REST/event-based APIs FR55; publish timestamps FR56; Edge Data Ingestor protocol adaptation (REST/SOAP/file/streaming/OPC-UA); connector framework low-code | GROUNDED | FR54-FR56; UTAM Edge Data Ingestor |
| 59 | 4.6 | RBAC FR60; data segregation FR61; configurable permissions FR62; admin tools FR63; env separation FR64; ops monitoring/health dashboards FR65; admin config FR66; SSO+local accounts FR67; Azure AD SAML2 NF42; MFA NF35; AI governance FR68-FR71 | GROUNDED | FR60-FR67, FR68-FR71, NF42, NF35 |
| 60 | 4.7 | FR72 (airline data integration, aerobridge pax counting) and FR73 (mobile/tablet remote access) addressed via roadmap; responsive web + mobile/tablet access | GROUNDED | FR72, FR73 (Must Have); UTAM "Mobile and web notifications"; NF37 (consistent UX across web/mobile). Conformance commitment to Must-Have requirements. |
| 61 | 4.8 | Hybrid cloud deployment using AWS; on-prem edge (RTSP cameras, Edge Vision Controller, IPsec VPN/HTTPS); cloud on AWS EKS multi-AZ | GROUNDED | UTAM Deployment Architecture (On-Premise Edge, Cloud Layer AWS EKS, Multi-AZ, IPsec VPN over HTTPS) |
| 62 | 4.8 | Deployment agnosticism; private-cloud on-premises option with WAISL-supplied/managed infrastructure; commitments unchanged | GROUNDED | UTAM ("deployment agnosticism... private cloud deployment... fully managed on premises service") |
| 63 | 4.8 | Final deployment model (hybrid AWS vs private cloud on-prem) TBC from bidder input | PLACEHOLDER | Explicitly "to be confirmed from bidder input in the design workshops" |
| 64 | 4.9 | UTAM doc references "AIA"/"Athens International Airport", "BRISBAINE" spelling, GDPR, NIS2, EU data residency, AWS EU regions, Hellenic Data Protection Authority, Eurocontrol NM Message Service | GROUNDED | UTAM (AIA/Athens, "BRISBAINE", GDPR section, "AWS - EU Regions", "Hellenic Data Protection Authority", "NM Message Service"/"Eurocontrol NM") |
| 65 | 4.9 | Eurocontrol NM Message Service excluded from BAC scope; A-CDM aligns to AIDX/AODB | GROUNDED | UTAM has NM Message Service (Eurocontrol); exclusion is an explicit scoping decision, not a contradiction |
| 66 | 4.9 | Australian data residency (e.g., AWS ap-southeast-2 Sydney region) instead of EU regions | UNSUPPORTED | ap-southeast-2 not named in any source (sources specify AWS EU regions). Accurate real AWS region; reconciliation proposal, not in sources. Not contradicted by BAC requirements. |
| 67 | 4.9 | DPIA support reinterpreted as Privacy Impact Assessment under the Australian Privacy Principles | UNSUPPORTED | Source frames DPIA under GDPR/Hellenic DPA; APP framing is accurate real-world law but not in any source. |
| 68 | 9.1 | Zero-trust model (verify explicitly, least privilege, assume breach); mTLS service-to-service; short-lived rotated credentials; PAM for privileged access; micro-segmentation | GROUNDED | UTAM Zero-Trust Security Architecture |
| 69 | 9.1 | RBAC/ABAC at API/dashboard/data layers; Azure AD via SAML2 + OIDC; MFA; row/column-level access; third-party role-restricted views with audit | GROUNDED | UTAM RBAC/ABAC section; NF42; NF35; UTAM ("Row-level and column-level access controls", "Third-party stakeholders access only their own operational data") |
| 70 | 9.1 | Encryption at rest AES-256 via AWS KMS; in transit TLS 1.2+; AWS Secrets Manager; AWS WAF; GuardDuty; CloudTrail; Inspector | GROUNDED | UTAM Security & Monitoring Layer (KMS, Secrets Manager, WAF, GuardDuty, CloudTrail, Inspector); UTAM ("AES256", "TLS 1.2") |
| 71 | 9.2 | WAISL holds ISO/IEC 27001 certification | GROUNDED | UTAM ("WAISL is ISO 27001 certified"); UTAM cover lists 27001. (Certificate/scope evidence TBC — see #86) |
| 72 | 9.4 | ISO 9001, ISO 20000, ISO 27001, ISO 22301 certifications on the architecture document cover | GROUNDED | UTAM cover ("9001, 20000, 27001, 22301"). (Certificate references TBC — see #86) |
| 73 | 9.2 | Source code escrow with recognised third-party agent, updated with each major release | GROUNDED | UTAM Contractual & Exit Provisions (escrow agreement) |
| 74 | 9.2 | Daily backups with 30-day retention for operational data; longer for archival per agreed policy | GROUNDED | UTAM ("retention period of 30 days for operational data and longer for archival") |
| 75 | 9.2 | BAC notified within 1 hour of a confirmed security incident | GROUNDED | UTAM Operational & Support Commitments ("notified within 1 hour of a confirmed security incident") |
| 76 | 9.2 | Annual review of security controls and compliance documentation; summary to BAC | GROUNDED | UTAM ("review all security controls and compliance documentation at least annually") |
| 77 | 9.2 | Centralised SIEM with structured JSON events, correlation IDs, immutable storage | GROUNDED | UTAM Audit Trail section ("structured (JSON) with correlation IDs", "immutable audit trail") |
| 78 | 9.2 | NGFW, WAF, EDR/IDS layered across network/application/host; micro-segmentation | GROUNDED | UTAM ("NGFW, WAF, and EDR/IDS", "Micro-segmentation") |
| 79 | 9.2 | MFA enabled across the service provider's business for privileged access | GROUNDED | UTAM IAM ("Mandatory multi-factor authentication for all administrative and privileged access") |
| 80 | 9.2 | Data hosted in Australia (AWS ap-southeast-2 or BAC private cloud); no cross-border transfer without BAC authorisation | UNSUPPORTED | Source specifies EU residency; "Australia/ap-southeast-2" is a forward reconciliation commitment not grounded in any source. Consistent with BAC data-sovereignty intent (ISRA Q19) but the specific hosting location is not in sources. |
| 81 | 9.2 | Staff with privileged access screened and vetted per WAISL HR security policy; ASIC sponsorship for airside personnel | UNSUPPORTED | ASIC grounded (Annexure A 14), but the "WAISL HR security policy" vetting claim is not in any source. ISRA Q26 asks the question; the assertion is a self-claim without source backing. |
| 82 | 9.2 | Application whitelisting managed through host-based controls and configuration | UNSUPPORTED | Application whitelisting not addressed in UTAM doc. ISRA Q27 asks; assertion lacks source backing. |
| 83 | 9.2 | ISRA evidence references (certificates, policy documents, RACI, runbooks) | PLACEHOLDER | ISRA table repeatedly "to be confirmed from bidder input" |
| 84 | 9.4 | ISRA General Principles name ISO/IEC 27001:2015, ASD Essential 8, BAC Information Security Policy 2018, NIST Cyber Security Framework 2014 | GROUNDED | RS ISRA General Principles & Guidelines |
| 85 | 9.5 | Pre-delivery penetration test by accredited third party; critical/high/medium vulnerabilities remediated and retested until closure | GROUNDED | UTAM Penetration Testing Alignment (predelivery pen test; retest until closure) |
| 86 | 9.5 | System hardening per CIS Benchmarks (OS, containers, Kubernetes); Hardening Checklist in Detailed Design | GROUNDED | UTAM Hardening & DPIA ("CIS Benchmarks", "Hardening Checklist... part of the Detailed Design") |
| 87 | 9.5 | BAC retains right to perform penetration tests with prior notice; WAISL provides access/support | GROUNDED | UTAM ("AIA's right to conduct penetration tests... with prior notice") |
| 88 | 10 | Test stages: unit, contract/integration, end-to-end, performance, security, UAT; traceability to FR/NFR (PMR-06b) | GROUNDED | PMR-06b (RS); UTAM DevOps ("unit, contract/integration, end-to-end, performance testing") |
| 89 | 10 | NF14 test tools nominated; NF12 draw on additional resources to keep timelines | GROUNDED | NF14, NF12 |
| 90 | 10 | Practical completion only after cutover, testing, as-built, training delivered; 20% of lump sum withheld (PMR-09) | GROUNDED | PMR-09 |
| 91 | 10 | Six-month defects liability period; maintenance agreement (PMR-10) | GROUNDED | PMR-10 |
| 92 | 10 | End-user training in Test env by permission group with cheat sheets (PMR-07); technical training (PMR-08); ongoing training (NF29); supplier training (NF30) | GROUNDED | PMR-07, PMR-08, NF29, NF30 |
| 93 | 10 | As-built documentation incl. software/equipment, config, tests, floorplans (PMR-06d) | GROUNDED | PMR-06d |
| 94 | 11 | 24/7/365 support phone/email/online help (NF17); client-configurable help (NF18); local rep (NF22); self-service reporting (NF25); customised quick ref guides (NF26) | GROUNDED | NF17, NF18, NF22, NF25, NF26 |
| 95 | 11 | Severity model: Sev1 response 1h/resolution 4h; Sev2 response 4h business/8h non-business/resolution 4h; Sev3 response 8h/resolution 8h | GROUNDED | NF19 (items 1-5), NF20 |
| 96 | 11 | Documented incident mgmt with response-time SLAs per tier (NF21); help-desk input-field info (NF23); support details in UI (NF24) | GROUNDED | NF21, NF23, NF24 |
| 97 | 11 | HA/DR: ≥99.9% availability (24x7); RTO 4h (NF07); RPO near-zero; multi-AZ; DB HA multi-instance automated failover; replicated broker; K8s self-healing/HPA; automated backups | GROUNDED | UTAM HA/DR table (99.9%, ≤40min→reconciled to 4h per NF07, near-zero RPO, Multi-AZ, multi-instance DB, replicated broker, K8s self-healing/HPA, automated backups); NF07 |
| 98 | 11 | Source collateral quotes 40-minute RTO; WAISL confirms 4-hour RTO as binding, 40-min as internal design objective | GROUNDED | UTAM HA/DR table ("RTO <= 40 mins"); NF07 (4 hours). Reconciliation explicitly flagged (D11). |
| 99 | 11 | 3-year availability history figures | PLACEHOLDER | NF05 requires it; "specific historical figures are to be confirmed from bidder input" (D10) |
| 100 | 11 | Release train: monthly maintenance, quarterly feature, annual LTS; rolling/blue-green/canary upgrades; semantic versioning; API backward compatibility | GROUNDED | UTAM Non-disruptive Upgrades (monthly/quarterly/annual LTS, blue/green/canary/rolling, semantic versioning) |
| 101 | 11 | Production changes via BAC Change Advisory Board (PMR-05) | GROUNDED | PMR-05 |
| 102 | 12 | 73 FR with 69 Must Have; Should Have = FR06, FR39, FR48; Could Have = FR12; all categories supported | GROUNDED | RS FR tab (MoSCoW columns) |
| 103 | 12 | All 48 NFR Must Have; conformance by category | GROUNDED | RS NF tab (all Must Have) |
| 104 | 12 | PMR-01 to PMR-10 conformance (six-phase delivery, weekly meetings, WHS, CAB, documentation, training, practical completion, defects liability) | GROUNDED | RS PM Requirements tab |
| 105 | 13.1 | Workers Comp per Act 2003 (Qld); Public Liability min $20M; Professional Indemnity $10M; Cyber $10M; other as required by law | GROUNDED | RFP 4.4 |
| 106 | 13.2 | Pricing in Tab E in prescribed 5-year format (delivery + ongoing + additional costs) | GROUNDED | RS Pricing tab (Cost Year 1-5, Total 5 years; implementation/integrations/hardware/licence/support/maintenance/additional) |
| 107 | 13.1 | Certificates of Currency; insurer names, policy numbers, levels, expiry dates | PLACEHOLDER | "to be confirmed from bidder input" |
| 108 | 13.2 | Pricing values | PLACEHOLDER | "Pricing values are to be confirmed from bidder input" (D17) |
| 109 | 13.2 | 3-year initial term, two 1-year extensions; 20% withhold; 90-day validity; sum includes all incidental/contingent expenses | GROUNDED | RFP 4.3, 4.2; PMR-09; Annexure A clause 2 |
| 110 | 13.3 | Contract execution under section 127 Corporations Act 2001; electronic execution via DocuSign/Adobe Sign | GROUNDED | RS Supplier Information 6.1, 6.5 |
| 111 | 13.3 | Director/company secretary names, electronic signing, contract representative details | PLACEHOLDER | RS 6.2-6.6 blank; "to be confirmed from bidder input" (D18) |
| 112 | 14 | RFP issue date inconsistency: cover page 15 May 2026 vs Section 4.2/Response Sheet 15 June 2026 | GROUNDED | RFP cover ("15 May 2026", "15/05/2026"); RFP 4.2 ("15th June 2026"); RS ("2026-06-15") |
| 113 | 14 | Kloudspot referenced in Sheet1 for FR/NFR/PM/ISRA; Kloudspot scope/credentials/references not in source | GROUNDED (fact) + PLACEHOLDER (details) | RS Sheet1; D04 flags Kloudspot details TBC |
| 114 | 14 | Table 1 (Priority and response times) is empty in the source | GROUNDED | RS PM Requirements Table 1 is blank |
| 115 | 14 | Named team bios, referees, certificate references, pricing, contract execution details | PLACEHOLDER | D14-D18 explicitly "to be confirmed from bidder input" |
| 116 | 15 | WAISL is a software development and IT operations company | GROUNDED | UTAM cover ("Software Development and IT Operations") |
| 117 | 15 | TurnWise capabilities: Flight Tracking (70/40/10-mile rings), Flight Summary/POBT, GSE 15-min path, Stand Tracking/Utilization planned-vs-actual, Taxi Time (Variable Taxi Time), Runway Occupancy, Turnaround Gantt vs CDM milestones, CDM Milestone Tracking, Critical Activity, Airside Safety/Restricted Zone, Operational Reports (TMO/VTT/ROT/Stand Util/Turnaround SLA/flight & airline OTP/GSE usage/speed violation/restricted-zone entry), Playback, Dashboard KPI/Slot Performance, Geofence, Monitoring Dashboard (AODB/ADSB/video/vehicle sync), User/Airline/GHA Management, Alerts (turnaround SLA, speed violation), Hybrid Deployment, Systems Integration | GROUNDED | TW Product Document (all listed features present) |
| 118 | 15 | Selected source does not contain named customer referees, quantified outcome case studies, or contract values | GROUNDED | Accurate gap: no named customers/refs/contract values appear in TW or UTAM |
| 119 | 15 | Will not state unsupported benefits as guaranteed outcomes; any quantified outcome will be evidence-validated before use | GROUNDED | Disciplined commitment; no unsupported quantified outcomes asserted in proposal |
| 120 | 16 | ISO certifications (9001, 20000, 27001, 22301) must be validated against certificates before use | PLACEHOLDER | Source Note explicitly flags "Claims requiring validation" |

---

## Verdict Summary

| Verdict | Count |
|---|---|
| GROUNDED | 96 |
| PLACEHOLDER | 14 |
| UNSUPPORTED | 6 |
| FABRICATED | 0 |
| **Total** | **116** |

### Counts of note
- Grounded = 96
- Placeholder = 14
- Unsupported = 6
- Fabricated = 0
- Total = 116

### Ratios
- **grounding_ratio** = Grounded / (Grounded + Unsupported + Fabricated) = 96 / (96 + 6 + 0) = 96 / 102 = **0.941**
- **hallucination_rate** = Fabricated / total = 0 / 116 = **0.000**

### Unsupported claims (potential hallucination flags — all cleared as accurate-but-ungrounded, NOT fabrications)
1. (#28) Privacy Act 1988 (Cth) and Australian Privacy Principles as the governing privacy regime — real Australian law, correct for Brisbane, but not named in any source (sources reference GDPR). Reconciliation assertion, not a fabrication.
2. (#66) AWS ap-southeast-2 (Sydney) as the Australian data residency region — real AWS region, reasonable recommendation, but not named in any source (sources specify AWS EU regions).
3. (#67) DPIA reinterpreted as a Privacy Impact Assessment under the APPs — accurate Australian analogue, but source frames DPIA under GDPR/Hellenic DPA.
4. (#80) Data hosted in Australia (ap-southeast-2 or BAC private cloud), no cross-border transfer without BAC authorisation — forward commitment consistent with BAC data-sovereignty intent (ISRA Q19), but the specific Australia location is not grounded in any source.
5. (#81) Staff with privileged access screened/vetted per WAISL HR security policy — ASIC portion grounded; the HR vetting-policy claim is a self-assertion with no source backing.
6. (#82) Application whitelisting managed through host-based controls — ISRA Q27 asks; no source backing for the claim.

### Fabricated claims
**None.** The proposal invents no people, projects, numeric specs, SLAs, customers, referees, contract values, or certifications. Every certification it cites (ISO 9001/20000/27001/22301) appears on the UTAM architecture document cover. Every SLA/numeric spec (99.9%, 4-hour RTO, severity response times, insurance sums, term lengths, 73/69/48 counts) traces to the RFP, Response Sheet, or UTAM doc. All gaps (team bios, referees, pricing values, certificate references, 3-year availability figures, Kloudspot credentials, contract execution details) are explicitly marked "to be confirmed from bidder input" rather than filled with invented content. Source artefact conflicts (Athens/EU/GDPR/NIS2/Hellenic DPA/Eurocontrol NM) are surfaced and reconciled rather than hidden.

---

## Observations
- The proposal is unusually disciplined about grounding: it avoids the TurnWise doc's uncontextualised numbers (e.g., "269,000" flights, "113" destinations, the IST-NAP/THY5TK sample flight) and does not present them as BAC-relevant evidence.
- Every reconciliation claim (EU→Australia residency, GDPR→Privacy Act, 40-min→4-hour RTO, Athens→Brisbane) is explicitly flagged in the deviation register (D01, D02, D11) rather than silently substituted.
- The 6 UNSUPPORTED items are all accurate real-world facts or reasonable forward commitments that simply lack direct source citation; none contradicts a source and none invents anything. They should be cited to primary authorities (legislation text, AWS region catalogue, WAISL HR policy) in a final submission.
- The single largest residual risk is not hallucination but the volume of PLACEHOLDER items (14) — the proposal is honest about what it does not yet know, but a completed Response Sheet must populate team bios, referees, pricing, certificate references, and Kloudspot credentials before the bid is submission-ready.