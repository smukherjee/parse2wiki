# DDF CTO Meeting — Talking Notes
**Based on:** GAL Duty Free Digital Transformation & Retail Analytics Technical Proposal (V5), submitted by WAISL
**Audience:** GAL Technology & Digital Initiatives (Mr. Himanshu Sharma and team) — IT integration, security and architecture approvals
**Purpose:** Walk the CTO/technology counterpart through the proposed solution architecture, integration approach, security/compliance posture and delivery model, and surface the decisions/dependencies that need their input.

---

## 1. Opening framing

- We're proposing the **Duty Free Intelligence Platform (DFIP)** — a unified, cloud-hosted analytics platform across Delhi (IGI) and Hyderabad, delivered in 3 phases over 9 months, followed by managed services (Y2–Y5).
- Design stance: **outcome-first, asset-leveraging, privacy-by-design, modular.** We integrate existing GAL/DIAL investments (Xovis lidar, camera estate, POS/ERP, current BI) rather than replace them.
- Scale context: ~295 lac passengers, ~INR 3,273 Cr duty-free sales, ~39 lac transactions/year across both airports (FY27 projection, Annexure-1) — worth stating up front so the CTO calibrates performance/throughput expectations.

## 2. System architecture — the core technical narrative

DFIP is a **layered, cloud-native architecture**: Edge → Integration/Ingestion → Data Platform → Analytics/Intelligence → Experience, with security/governance/observability cross-cutting every layer, converging into a single Command Centre.

Walk through layer-by-layer if asked for depth:
- **Edge** — connectors/edge agents for POS, AODB/FIDS, Xovis lidar + CCTV/VMS, RFID readers, ESL access points, payment-gateway MPR files. CV inference runs at/near edge where bandwidth/latency requires it.
- **Integration & Ingestion** — API gateway + event-streaming backbone, CDC for non-intrusive POS/ERP replication, scheduled ETL/ELT, file ingestion for MPR. All interfaces catalogued, versioned, monitored.
- **Data Platform** — governed data lake (raw/curated/consumption zones), analytical warehouse, feature store, master/reference data. Data contracts and quality checks enforced at zone boundaries.
- **Analytics & Intelligence** — descriptive, predictive, prescriptive models, CV pipeline, Phase-3 AI agents, all under an MLOps lifecycle.
- **Experience** — role-specific Power BI dashboards, NLQ/LLM conversational analytics, alerting, controlled write-back to ESL/POS.
- **Cross-cutting** — IAM/RBAC, encryption in transit/at rest, consent management, immutable audit logging, data lineage, full-stack observability.

**Key technical principle to emphasize:** integration is **API-first, non-intrusive, read-optimised** (CDC taps, replica reads) — we do not touch live transaction processing on POS/ERP.

## 3. Hosting, residency & resilience — items still open, flag explicitly

- Cloud-first, hosted in **Indian data-centre regions** to satisfy DPDPA residency (RFP 9.3) — primary region + separate DR region.
- **Not yet finalised, needs GAL IT input during Discovery:** final cloud platform, specific regions, and RTO/RPO/availability targets — these will be confirmed against GAL's own standards and the SLA framework, and stated in the Infrastructure Proposal/Commercial Volume.
- No personal data crosses borders without GAL's explicit written approval — worth confirming GAL's expectation here directly with the CTO.

## 4. Integration approach — what we need from GAL's technology org

Table of source systems and patterns (good to have ready if CTO probes specifics):

| Source | Pattern | Notes |
|---|---|---|
| POS (Delhi & Hyderabad) | CDC/replica + API | Non-intrusive, protects live transactions |
| ERP/inventory | CDC/API + batch | GRN, stock movements |
| Flight systems (AODB/FIDS) | API/message feed | Schedule, gate, status |
| Xovis lidar + CCTV/VMS | Sensor API/RTSP + edge CV | Footfall, flow, dwell |
| RFID infrastructure | Reader middleware/API | Inventory, self-checkout |
| ESL network | ESL server API | Price/content sync |
| Payment gateways | MPR file ingestion/API | Settlement mapping |
| Existing GAL/DIAL BI | Connector/dataset reuse | Avoid duplication |

**Explicit ask for the CTO:** WAISL owns coordination and query-resolution for third-party access, but **GAL needs to facilitate introductions and access approvals** — airport-authority and IT-concessionaire sign-off is a named dependency (not assumed, tracked in the risk register). This is the single biggest schedule risk we should discuss face-to-face — get a sense of realistic lead times for POS/Xovis/flight-system access approvals.

## 5. Security, privacy & compliance — lead with this for a CTO audience

- **DPDPA 2023:** GAL = Data Fiduciary, WAISL = Data Processor. DPA to be executed before processing; PII (travel profiles, boarding-pass data, transactions, video/biometric) identified/classified before processing.
- **Consent framework** designed as a Discovery deliverable — purpose limitation, opt-in/opt-out, auditable consent log.
- **ISO 27001-aligned controls:** encryption in transit/at rest, RBAC, MFA for privileged access, annual pen-testing, documented breach response, **72-hour breach notification**.
- **Retention:** documented schedule; on termination, all data returned and securely deleted within 30 days with written certification.
- **Certifications held:** CMMI Level 3, ISO 27001 (satisfies RFP Compliance PQ 2(B)(v)).
- Video-analytics privacy posture: only derived events/aggregates persisted, **not raw video** — worth stating explicitly since CTOs often probe this.

## 6. Engineering practice & delivery methodology

- **Hybrid delivery:** waterfall phase-gate spine (for the RFP's payment-milestone model) wrapping agile 2-week sprints within each phase.
- **DevSecOps/CI-CD** with security scanning embedded; infra-as-code.
- **MLOps:** versioned datasets/features/models, automated bias/accuracy checks before promotion, drift monitoring, full lineage — supports the independent operations-domain validation the RFP permits.
- Separate **DEV/UAT/Production** environments with controlled promotion.
- Capability-based go-live: each module's SLA clock starts at its own go-live date, not a single big-bang cutover.

## 7. Phased technical scope — quick orientation (not the full sales pitch)

| Phase | Go-live | Theme |
|---|---|---|
| Discovery | M1 | Locked scope, KPI framework, integration architecture, signed Implementation Plan |
| Phase 1 | M4 | Foundational analytics, video-analytics + RFID foundations, Xovis AMC takeover |
| Phase 2 | M6 | Forecasting, cohort intelligence, passenger-flow prediction, ESL integration |
| Phase 3 | M9 | AI-led automation, intelligent agents, AI reconciliation, revenue-leakage detection, full command centre |

Useful CTO-level framing: Phase 1 = "see clearly," Phase 2 = "anticipate & advise," Phase 3 = "act autonomously" — and Phase 3 automation is explicitly **guardrailed and re-uses validated Phase 1–2 signals**, not speculative day-one automation.

## 8. Risks/dependencies to raise proactively

- Third-party airport-system access delays (POS/flight/Xovis approvals) — **High/High**, WAISL-owned coordination but GAL access-facilitation is the critical dependency.
- RFID/ESL hardware procurement & commissioning lead-times — early BoM lock-in needed; site survey for power/network/mounting.
- Xovis AMC handover — inventory/value to be confirmed in Discovery/pre-bid; structured takeover plan.
- Data quality/completeness gaps in source feeds — addressed via Discovery data audit + zone-boundary quality gates.

## 9. Open items / explicit asks for GAL's CTO in this meeting

- Confirm cloud platform/region preference and RTO/RPO/availability targets against GAL's own IT standards.
- Confirm scope boundary on ESL infrastructure supply (raised as a pre-bid clarification).
- Confirm the fast-lane/bypass-suppression regulatory threshold definition and the airside passenger-count data source.
- Realistic timelines for third-party system access approvals (POS, Xovis, AODB/FIDS) — this drives the Discovery schedule.
- GAL's position on CCTV/lidar coverage gaps — new camera/lidar procurement is explicitly **out of scope for WAISL** (Assumption 5–6); confirm GAL's plan to close any gaps.
- Confirm access to space/power/internet at both airports for RFID self-checkout and ESL infrastructure (Assumption 8).

## 10. Anticipated CTO questions — quick answers

- **"Why not vendor-lock into a single hyperscaler now?"** — Final cloud platform/region is a Discovery decision made jointly against GAL's own standards, not pre-committed.
- **"How do you avoid impacting live POS/ERP performance?"** — CDC/replica-read patterns only; no direct writes to operational systems except controlled, agreed write-back paths (ESL price sync, POS flight-context).
- **"What happens if a model is inaccurate?"** — Rolling-origin backtesting, human-in-the-loop guardrails through Phase 2, and Phase 3 automation stays within commercial-leadership-agreed guardrails with full action logging.
- **"Who owns the data after contract end?"** — GAL; full return and certified deletion within 30 days of termination.
