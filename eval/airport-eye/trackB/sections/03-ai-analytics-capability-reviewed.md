# Volume 3 — AI and Analytics Capability

## Understanding of the Problem

DIAL's CR/BRD v1.5 §3.5 calls the federated AI-agent monitoring layer "the most technologically advanced and operationally transformative component" of Airport Eye — and backs that emphasis with the only granular, numeric, per-item performance tables in the entire corpus (§3.5.4 precision/recall/latency/prediction-horizon targets for 7 of the 8 named agents). [GROUNDED: CR/BRD v1.5 §3.5; brief.md Stated Priorities #1] Both the BRD and RFP v5 devote disproportionate detail to this section; cybersecurity/data-governance language is repeated across at least four separate sections in each document. [GROUNDED: brief.md — Reading Between the Lines] The signal is unambiguous: DIAL's real evaluation emphasis is AI-agent credibility plus governance/compliance trustworthiness, not price (Commercial is weighted lowest at 15% in the one document that gives explicit weights). [GROUNDED: RFP v5 §9.2 evaluation table, status uncertain per R-001]

## Roster Ambiguity — Flagged, Not Silently Resolved

We adopt the **BRD §3.5.3 eight-agent table as the authoritative working roster** per the binding-priority order. We flag explicitly that this is not the only enumeration in the corpus:

- **RFP v5 §6.3** describes only 6 of the 8 (no subsection for Passenger Flow or Structural Integrity — confirmed by direct re-read: §6.3.1, .2, .4, .5, .6, .7 exist; §6.3.3 is a numbering gap with no corresponding text). [GROUNDED: coverage-matrix R-065 roster note — direct re-read]
- **RFP v5 §6.5 performance table** scores 7 agents (adds Passenger Flow and Structural Integrity, but — like the BRD — omits Water & Drainage entirely). [GROUNDED: coverage-matrix R-065, R-087]
- **BRD/RFP v5 commercial Table 6** prices only 5 of the 8 named types as a single lump sum ("Generic and Configurable AI Agent — Mechanical & HVAC, Electrical, Fire Safety, Security and Perimeter, Water and Drainage"), leaving Energy Management, Passenger Flow, and Structural Integrity unpriced. [GAP: R-124 — internal inconsistency in the source document itself; we seek DIAL clarification on whether the 3 unpriced agents fold into the lump sum or require separate line items]
- **The requirements registers carry 17 `AI-*` rows** (AI-01–AI-17): 6 are platform/governance items, 11 are agent-functional rows that collapse onto the BRD's 8 named agents **except AI-10, a Natural-Language Query Agent with no named counterpart in the BRD's 8-agent table** — though a narrower "GIS Data Viewer... with Natural Language Query Capabilities" line item does appear as a priced deliverable in BRD/RFP v5 Table 1 / Section 1. [GROUNDED: coverage-matrix R-065 roster note, R-074]
- **One stale prior proposal (v9, May-2025) committed to only 7 agents** and is not reused. [GROUNDED: brief.md Collateral Inventory #7 — v9 stale, below current BRD requirements]

We do not average, blend, or silently pick a different count. [ASSERTION: per task instruction and coverage-matrix R-065 — explicit flagging rather than silent normalization]

## The Eight Federated AI-Driven Agents (BRD §3.5.3)

### 1. Mechanical & HVAC Monitoring Agent (R-066)
**Scope:** AHUs, chillers, cooling towers, BAS. Register AI-06/07/08/09 give a staged go-live scope: load forecasting → waste/fault anomaly detection → degradation trending/RUL → advisory optimisation. [GROUNDED: CR/BRD §3.5.3; register AI-06/07/08/09; Consolidated FINAL 8-agent table]
**Performance (R-080):** ≥ 82% precision, ≥ 78% recall, up to 72hr prediction horizon, ≤ 30s alert latency. [GROUNDED: CR/BRD §3.5.4 / RFP v5 §6.5, identical — Consolidated FINAL reproduces this figure but self-annotates several rows "(attributed to BRD Section 3.5.4 — verify)"; we recommend a verification pass before final citation]

### 2. Electrical Systems Monitoring Agent (R-067)
**Scope:** transformers, UPS, switchgear. Register AI-11 notes DGA/insulation-failure prediction is deferred until the MRSS server upgrade completes. [GROUNDED: CR/BRD §3.5.3; register AI-11; Consolidated FINAL] The MRSS upgrade is a DIAL-side prerequisite, not a vendor gap.
**Performance (R-081):** ≥ 80% precision, ≥ 75% recall, up to 48hr, ≤ 30s. [GROUNDED: BRD §3.5.4, with same verify-flag caveat]

### 3. Fire Safety & Life Safety Monitoring Agent (R-068)
**Scope:** multi-sensor correlation, suppression monitoring, evacuation modelling. Register AI-14 clarifies this is **advisory analytics layered over, never replacing, the certified fire system**. [GROUNDED: CR/BRD §3.5.3; register AI-14; Consolidated FINAL] We preserve this "advisory, never replacing" framing throughout. [REVIEW: MISSING-EMPATHY (minor) — The "advisory, never replacing" framing is correct and is DIAL's own language from register AI-14, but the paragraph stops at restating it. DIAL's life-safety stakeholders (the named OT owners for FDAS in PE_OT) will read this nervously given the ~65,000-point T3 FDAS estate. Suggested addition: "Given the ~65,000-point T3 FDAS estate and the life-safety criticality reflected in this agent's tightest-in-table targets (≥95% precision/recall, ≤5s latency), WAISL treats the certified fire system as the authoritative safety layer and positions this agent strictly as a decision-support overlay; all advisories route through, and do not bypass, the existing FDAS command path." Demonstrates understanding of the FDAS scale and stakeholder concern, not just the framing.]

**Performance (R-084):** ≥ 95% precision, ≥ 95% recall, real-time, ≤ 5s — the tightest targets in the table, consistent with life-safety criticality. [GROUNDED: BRD §3.5.4, with verify-flag caveat]

### 4. Water & Drainage Monitoring Agent (R-069, R-087)
**Scope:** potable/chilled/grey water, stormwater. Register AI-12 gives go-live scope: roof alerts, pump health, leak indication, stormwater forecasting benchmarked against the Walter P Moore hydrology study. [GROUNDED: CR/BRD §3.5.3; register AI-12; Consolidated FINAL; Walter P Moore cross-reference per ABR §3.1 — R-105]
**Performance target:** **No numeric target exists for this agent anywhere in the requirement corpus.** Confirmed by direct re-read: absent from BRD §3.5.4 **and** independently absent from RFP v5 §6.5 — a genuine gap in the source documents themselves, not an extraction error. [GAP: R-087 — Manageable severity. We draft this as "target to be finalized in consultation with DIAL, consistent with the rigor applied to the other 7 agents." We do not invent a number.]

### 5. Energy Management & Sustainability Agent (R-070)
**Scope:** EUI by zone, waste detection, carbon tracking. [GROUNDED: CR/BRD §3.5.3; register AI-06; Consolidated FINAL]
**Performance (R-085):** ≥ 80% precision, ≥ 75% recall, up to 24hr, ≤ 60s. [GROUNDED: BRD §3.5.4, with verify-flag caveat] Note: this agent is one of the 3 unpriced in BRD Table 6 — see R-124 gap above.

### 6. Passenger Flow Monitoring Agent (R-071)
**Scope:** congestion prediction, ATRS/DFMD monitoring. Register AI-13 adds XOVIS/Kloudspot counter data sources, 45-min forecast horizon. [GROUNDED: CR/BRD §3.5.3; register AI-13; Consolidated FINAL] Directly relevant to the ABR Operations department's queue-management asks (R-116).
**Performance (R-082):** ≥ 85% precision, ≥ 80% recall, up to 45min, ≤ 15s. [GROUNDED: BRD §3.5.4, with verify-flag caveat] Also unpriced in BRD Table 6 — see R-124.

### 7. Structural Integrity Monitoring Agent (R-072, R-083)
**Scope:** settlement/movement analysis. Register AI-16 flags **"CONDITIONAL SCOPE: cannot start until DIAL procures and installs the SHM sensor network,"** needing a further 6–12 month baseline. [GROUNDED: CR/BRD §3.5.3; register AI-16; Consolidated FINAL covers the agent generically]
**Deliverability caveat:** roster inclusion is [GROUNDED: Consolidated FINAL]; actual deliverability is [ASSERTION with explicit dependency — cannot commit to a start date until DIAL's SHM sensor network exists and a 6–12 month baseline is collected — per R-072].
**Performance (R-083):** ≥ 90% precision, ≥ 85% recall, up to 7 days, ≤ 60s. [GROUNDED: BRD §3.5.4, with verify-flag caveat and SHM dependency note — the target only becomes measurable once the SHM network is in place]

### 8. Security & Perimeter Monitoring Agent (R-073)
**Scope:** PSIM/access control/CCTV correlation, crowd density. Register AI-15 flags **"all scope subject to CISF approval before build starts."** [GROUNDED: CR/BRD §3.5.3; register AI-15; Consolidated FINAL] CISF approval is an external dependency we flag explicitly.
**Performance (R-086):** ≥ 88% precision, ≥ 82% recall, real-time/15min, ≤ 10s. [GROUNDED: BRD §3.5.4, with verify-flag caveat]

## AI Platform & Orchestration Layer

### AI Orchestration Engine (R-075)
Data routing, alert aggregation, priority scoring, cross-agent correlation, zero-downtime agent versioning. [GROUNDED: CR/BRD §3.5.2; register AI-03; Consolidated FINAL AIOP/orchestration architecture description]

### Shared AI Platform (R-077)
Common ingestion, historian, feature store, model registry, explainability service, alert pipeline, CMMS/AMMS connector — built once. [GROUNDED: register AI-02; substantially the same claim as R-075/orchestration architecture]

### Data Readiness Gate (R-076)
Per-domain data audit before any agent build; publish a Data Readiness Report; agree realistic day-1 benchmarks with DIAL. [ASSERTION: standard data-quality-audit practice for a competent AI vendor; not independently evidenced as a named process — register AI-01 only, no BRD counterpart]

### MLOps Lifecycle (R-078)
Monthly drift monitoring, quarterly retraining, DIAL approval before release, rolling 90-day KPI window. [ASSERTION: standard MLOps practice; no named evidence of this specific cadence — register AI-05]

### Per-Agent Acceptance (R-079)
Per-agent acceptance against individual §6.5 performance rows on a rolling 90-day window, tied to Milestone M5 / Deliverable D-10. [ASSERTION: standard acceptance-testing practice — register AI-17]

## AI Model Governance & Transparency (BRD §3.5.5)

DIAL's governance emphasis — repeated across §3.5.5, RFP v5 §6.4, and §9.x — signals that DIAL wants innovation bounded by auditable, explainable, DIAL-owned AI. [GROUNDED: brief.md Stated Priorities #3]

| Governance requirement | Our commitment | Marker |
|---|---|---|
| Explainability: plain-language explanation + confidence score (%) on every alert (R-088) | Match | [GROUNDED: CR/BRD §3.5.5 / RFP v5 §6.4; Consolidated FINAL commits] |
| Auditability: complete audit log (input data, model version, timestamp, operator response), minimum 5-year retention (R-089) | Match — distinct from the 2-year user-activity log and the 5-year BMS-historical log (three separate logs) | [GROUNDED: CR/BRD §3.5.5; Consolidated FINAL commits] |
| Feedback loop: operator feedback on alert accuracy feeds retraining (R-090) | Match | [GROUNDED: CR/BRD §3.5.5; Consolidated FINAL commits] |
| Model version control; rollback to prior version within 4 hours (R-091) | Match | [GROUNDED: CR/BRD §3.5.5; Consolidated FINAL commits] |
| DIAL owns all AI model weights and training data generated under contract (R-092) | Match | [GROUNDED: CR/BRD §3.5.5 / RFP v5 §9.3; Consolidated FINAL commits] |
| "No Black Box": deep-learning models must use SHAP/LIME/attention-visualisation interpretability techniques (R-093) | Commit to general explainability per R-088; the specific technique mandate (SHAP/LIME/attention) appears in RFP v5 §6.4 only, not with this specificity in the binding BRD §3.5.5 (which speaks more generally of "contributing factors") | [ASSERTION: general explainability commitment is Grounded (R-088); the technique-level prescriptiveness is a version-difference-between sources — flagged for confirmation against the binding BRD rather than silently adopted] |

## NL Query Agent — Scope-Boundary Flag (R-074)

The requirements registers' AI-10 describes a Natural-Language Query Agent with no counterpart in the BRD's 8-agent table. [GROUNDED: coverage-matrix R-074] A narrower "NL query for GIS data retrieval" line item does appear separately as a priced deliverable in BRD/RFP v5 Table 1 / §3.4.6, which we commit to delivering. [GROUNDED: BRD/RFP v5 Table 1 priced line item] We **flag the broader platform-wide NL-query-over-full-platform-data interpretation (assets, telemetry, alerts, CMMS, docs) as an open scope-boundary question**, not a silent scope addition or a silent scope drop. [GAP: R-074 broader interpretation — no evidence of this capability in our collateral; we seek DIAL clarification on whether AI-10 is the priced GIS-NL-query line item or additional scope]

## SPG "What-If" Simulation / Decision-Engine Scope (ABR §4)

The ABR (2-July-2026) devotes its largest section to a dynamic digital twin decision-support / "what-if" simulation engine spanning Commercial/Operational/Engineering domains (24 use cases), with a 4-part architecture (DT for simulation, scenario-control UI, decision engine, visualisation UI). [GROUNDED: ABR §4.1 — R-100] We track this as **its own distinct scope item**, not folded into the 8 AI agents, per coverage-matrix guidance.

**Adjacent precedent:** the Consolidated FINAL proposal references an "IROPs/Disruption Decision Engine," cross-referencing prior Solution Proposal v9 §5.2 — real, if partial and unresolved, adjacent evidence. [ASSERTION: Consolidated FINAL references the IROPs/Disruption Decision Engine; no evidence the full 24-use-case capability is built or piloted — R-100]

**Use-case clusters:**

- **10 Commercial use cases (R-101)** — store-mix optimisation, shelf merchandising, dwell-time monetisation, queue-vs-revenue trade-off, gate allocation, etc. [GAP: R-101 — no evidence any of these are built; framed as "possible examples" in the ABR, not obligations. We propose a phased roadmap rather than committing to all 10.]
- **8 Operational use cases (R-102)** — passenger flow optimisation, queue management, check-in/security capacity planning, disruption management, workforce deployment, baggage flow, curbside management. [GAP: R-102 — partially adjacent. The Passenger Flow Monitoring Agent (R-071) is a real adjacent capability for some of these; no evidence of the simulation/decision-engine layer itself.]
- **5 Engineering use cases (R-103)** — thermal load simulation, HVAC demand modelling, power infrastructure stress testing. [GAP: R-103 — no evidence of any simulation capability at this level; the Mechanical & HVAC and Energy Management agents monitor, not simulate.]

## Additional ABR Departmental Asks Mapped to the AI Platform

| ABR ask | Agent / capability | Marker |
|---|---|---|
| Borewell recharge monitoring via IoT (P&E, R-104) | General IoT-ingestion capability (R-046) | [ASSERTION: adjacent — R-104] |
| Storm water analysis with Walter P Moore (P&E, R-105) | Water & Drainage Agent register AI-12 names "benchmarked against the Walter P Moore hydrology study" | [GROUNDED: register AI-12 linkage — R-105] |
| Reverse-entry detection in restricted zones (S&V, R-106) | Security & Perimeter Agent access-pattern analytics (R-073) | [ASSERTION: adjacent — R-106] |
| Unattended baggage detection via video analytics (S&V, R-107) | General video-analytics/AI framing | [ASSERTION: adjacent, no specific named evidence — R-107] |
| Behaviour analytics for threat detection (S&V, R-108) | Security & Perimeter Agent (R-073) | [ASSERTION: adjacent — R-108] |
| Predictive security monitoring (S&V, R-109) | Security & Perimeter Monitoring Agent (R-073) | [GROUNDED: directly overlaps with the already-Grounded Security & Perimeter Agent — R-109] |
| Security asset mapping (S&V, R-110) | Adjacent GIS capability | [ASSERTION: R-110] |
| Google Maps / satellite integration for landside monitoring (Commercial Aero, R-111) | BRD §3.1.2 Landside Coverage explicitly specifies "aircraft and satellite scans" | [GROUNDED: BRD §3.1.2 — R-111] |
| Identification of space-allocation changes (Commercial Aero, R-112) | Depends on the land/space-management capability already flagged as a gap (R-039) | [GAP: R-112 — same remediation as R-039] |
| GIS-based analytics for planning and utilisation (Commercial Aero, R-113) | Core GIS platform capability | [GROUNDED: R-113] |
| Surface navigation in low-visibility/fog (Operations, R-114) | No evidence of this specific capability anywhere else in the corpus | [GAP: R-114 — niche ABR-only ask; no "must" language attached] |
| What-if scenario analytics (Operations, R-115) | Same IROPs/Disruption Decision Engine precedent as R-100 | [ASSERTION: same treatment as R-100 — R-115] |
| Monitoring/alerting of DigiYatra, E-Gates, CUSS, CUPPS (Operations, R-116) | These named systems do not appear in PE_OT's 19-system inventory or the BRD's scope at all | [GAP: R-116 — possible scope addition; we seek DIAL clarification on whether these are in scope for Airport Eye or a separate IT workstream] |
| Live operations monitoring dashboard (Operations, R-117) | Core APOC/CCC dashboard capability (R-050) | [GROUNDED: R-117] |
| Identification of overstaying/unidentified passengers (Operations, R-118) | Passenger Flow Agent (R-071) + general video-analytics framing | [ASSERTION: adjacent — R-118] |

## Scalability & Performance

Our RGIA proof point — 40+ integrated systems, 100+ KPIs tracked, 18+ months live operation — is the strongest available evidence that a federated, governed AI-agent layer of this scope has been operated at airport scale. [GROUNDED: RGIA case study] [REVIEW: VENDOR-CENTRIC (mild) — "Our RGIA proof point … is the strongest available evidence that a federated, governed AI-agent layer of this scope has been operated at airport scale" frames RGIA around the vendor's evidence strength. Given DIAL just devoted the most granular numeric tables in the corpus to this agent layer, the client-centric version ties RGIA directly to those targets: "A federated, governed AI-agent layer of this scope has been operated at airport scale at RGIA — 40+ integrated systems, 100+ KPIs tracked, 18+ months live — which is why WAISL commits to the BRD §2.3 KPI-4 floor (≥80% precision / ≥75% recall) for the Airport Eye agent layer as a whole below." Leads with the capability claim DIAL cares about, then cites RGIA as the basis.] We commit to the BRD's platform-wide predictive accuracy KPI (≥ 80% precision / ≥ 75% recall, BRD §2.3 KPI-4) as the floor for the agent layer as a whole. [GROUNDED: CR/BRD §2.3 KPI-4, cross-confirmed by register AI-05]

---

**Bridge.** The AI architecture above is delivered through the 5-phase implementation methodology and 15-deliverable plan detailed in Volume 4.