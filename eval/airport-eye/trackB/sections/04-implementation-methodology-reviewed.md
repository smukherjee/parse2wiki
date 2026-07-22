# Volume 4 — Implementation Methodology and Timeline

## Understanding of the Problem

DIAL's BRD prescribes a structured, phase-gated delivery: 5 phases of approximately 3 months each (~15 months total), 15 numbered deliverables D-01 through D-15, and a 14-calendar-day DIAL review/sign-off period per deliverable. [GROUNDED: CR/BRD §4.1, §4.2; RFP v5 §5.1, §5.2 — identical structure confirmed by direct re-read] The programme is not a greenfield build — it is an evolution of an existing Concession Agreement toward a digital-twin/agentic-AI capability, layered onto a live, multi-vendor OT estate that must not be disrupted during integration. [GROUNDED: CR/BRD §1.2; PE_OT inventory of 19 in-production systems]

## Programme Structure — 5 Phases

| Phase | Months | Scope | Key deliverables |
|---|---|---|---|
| Phase 1 — Geospatial & LiDAR Survey | ~3 mo | Airborne + mobile/indoor LiDAR, orthophotography, DTM/DSM, survey-grade foundation | D-01 to D-03 (LiDAR datasets, survey report) |
| Phase 2 — GIS–BIM Integration & Federated BIM | ~3 mo | LOD 200–350 BIM models, CDE, legacy CAD/DWG migration, clash detection | D-04 to D-06 (BIM models, BEP, migration report) |
| Phase 3 — Facilities Maintenance Management | ~3 mo | Land/space digital footprint, CLM integration, unified BMS/LCMS/ECMS/CMS/FDAS/BHS/HBS/VDGS/VHT/ATRS/DFMD/PBB/WTP-STP/AGL-CMS/IoT platform | D-07 (facilities platform) |
| Phase 4 — Digital Twin Platform | ~3 mo | Modular cloud-native platform, 3D GIS+BIM viewer, BMS/IoT ingestion middleware, APOC/CCC integration, access control, audit logging | D-08 to D-10 (DT platform, integration report, API docs) |
| Phase 5 — AI Agents & Agentic Monitoring | ~3 mo | Shared AI platform, orchestration engine, 8 federated agents, governance/explainability, MLOps | D-10/D-11 (AI platform, agent acceptance) |

[ASSERTION: phase-by-deliverable mapping follows the BRD's §4.1/§4.2 structure; specific deliverable numbering per phase is our interpretation, not a verbatim BRD allocation — the BRD lists D-01 through D-15 but does not explicitly map each to a phase — R-119, R-120]

**Authoritative schedule caveat:** we adopt the BRD's 15-month structure as authoritative for compliance purposes. We flag explicitly that the Consolidated FINAL proposal's own stated "9-month delivery (Mo1–Mo9), re-baselined to March 2027" does not obviously reconcile with this 15-month structure — possibly a fast-track T2 subset vs. the full programme. [ASSERTION: open question carried from the brief — R-119; we seek DIAL confirmation before using either number as the contracted delivery date]

## Deliverables D-01 through D-15 (R-120)

The 15 numbered deliverables span: Project Execution Plan / BIM Execution Plan, LiDAR datasets, BIM models, DT platform, BMS/IoT integration report, AI platform, API documentation, cybersecurity report, training materials, as-built documentation, and post-implementation review. [GROUNDED: CR/BRD §4.2 / RFP v5 §5.2 — identical, confirmed by direct re-read] Our RGIA delivery track record supports the process capability to deliver against this deliverable-based structure. [GROUNDED: RGIA case study — 18+ months live, 40+ systems, 100+ KPIs] [REVIEW: VENDOR-CENTRIC (mild) — "Our RGIA delivery track record supports the process capability to deliver against this deliverable-based structure" frames the RGIA evidence around the vendor's process capability. DIAL's §4.2 deliverable-and-14-day-review structure is itself a phase-gated acceptance discipline; the client-centric version: "This deliverable-based structure with a 14-day DIAL review per deliverable is the same phase-gated acceptance discipline WAISL has run at RGIA across 15+ deliverables over 18+ months of live operation." Leads with DIAL's acceptance discipline, then cites RGIA as proof of having operated it.]

## Deliverable Acceptance (R-121)

Each deliverable is subject to a 14-calendar-day DIAL review/sign-off period before it is accepted and milestone payment is released. [ASSERTION: standard commercial-process acceptance commitment per BRD §4.2 — R-121]

## Dependencies and External Prerequisites We Flag

Honest delivery planning requires naming the prerequisites that sit outside our control:

- **Structural Integrity Agent (R-072, R-083):** cannot start until DIAL procures and installs the SHM sensor network, with a further 6–12 month baseline collection period before predictions are meaningful. [GAP-adjacent: register AI-16 — "CONDITIONAL SCOPE: cannot start until DIAL procures and installs the SHM sensor network." We cannot commit to a start date for this agent until that prerequisite is met.]
- **Security & Perimeter Agent (R-073):** all scope subject to CISF approval before build starts. [GROUNDED: register AI-15 — external dependency flagged]
- **Electrical Systems Agent DGA/insulation-failure prediction (R-067):** register AI-11 notes this is deferred until the MRSS server upgrade DIAL is completing. [GROUNDED: register AI-11 — DIAL-side prerequisite]
- **MRSS integration (R-098):** gated on the same GE→Schneider SCADA upgrade. [GROUNDED: register, PE_OT]
- **Appendix A (Schedule of Buildings/Areas, R-032) and Appendix B (BEP, R-038):** both "[To be completed by DIAL]" — underlie area-based BIM/LiDAR costing and the BIM execution plan respectively. [GAP: R-032, R-038 — flagged for DIAL input]
- **T2 OT integration scope (R-097):** register marks OEM and/or point count as "X" / "TBD" for most T2 rows. [GAP: R-097 — flagged to DIAL rather than guessing]
- **IT-side OneAPOC integrations (R-099) and DigiYatra/E-Gates/CUSS/CUPPS (R-116):** scope boundary with the OneAPOC program unclear. [GAP: R-099, R-116 — we seek DIAL clarification]
- **Buffer-zone LiDAR density (R-022):** 8 pts/m² stated in the BRD/RFP but Consolidated FINAL itself annotates "pending DIAL confirmation." [ASSERTION with caveat — flagged as open per R-022]
- **Cross-register BIM-modeling schedule conflict:** the two requirements registers systematically disagree on delivery month/phase for nearly every shared `BIMM-*` line item — in one case by ~4 months. Neither file is a clean superset of the other. [GAP-adjacent: coverage-matrix §13 / gap-report §13 — we treat `AirportEye_Requirements_Register_v5.xlsx.md` as the more complete source but do not assert any specific BIM-modeling delivery month from either register without flagging the conflict.]

## Roles & RACI (R-122)

We commit to a RACI matrix across Planning/Surveys, Platform Development, AI/Analytics, and Operations workstreams, with Vendor (WAISL/GEOKNO) / DIAL / Smart City / DEC roles per BRD §5. [ASSERTION: we can commit to a RACI structure without naming individuals — the team/staffing gap (R-129) is addressed in Volume 7 — R-122]

**Term-definition flag:** the BRD uses the abbreviations **"DEC"** and **"POD"** in its RACI tables and body text but does not define either in its own glossary. "DEC" is likely "Design/Engineering Consultant" but unconfirmed; "POD" is undefined. We flag these rather than guess their meaning and request DIAL confirmation. [GAP-adjacent: R-122 — undefined terms in the binding source]

## Testing & Quality Assurance

Per-agent acceptance testing against the individual BRD §3.5.4 / §6.5 performance rows on a rolling 90-day window, tied to Milestone M5 / Deliverable D-10. [ASSERTION: standard acceptance-testing practice — register AI-17, R-079] Penetration testing of internet-facing components prior to go-live, tied to Deliverable D-12. [ASSERTION: R-058] Full cybersecurity risk assessment prior to deployment, findings submitted for DIAL approval. [ASSERTION: R-060] [REVIEW: PASSIVE-ACCOUNTABILITY — "Penetration testing … is tied to Deliverable D-12" and "Full cybersecurity risk assessment … findings submitted for DIAL approval" do not name the actor who conducts or signs off. DIAL's contractual back half holds the vendor responsible regardless of originating system, so named ownership matters. Suggested: "WAISL's Cybersecurity Lead (Volume 7, to be named) conducts penetration testing prior to go-live with findings submitted for DIAL approval at D-12, and runs the full pre-deployment cybersecurity risk assessment with DIAL sign-off before any production cutover." Same note as Volume 2 §Testing; keep consistent across volumes.]

## O&M and Support (R-127)

5-year O&M plan with 24×7 support, RTO 4hr / RPO 24hr. [GROUNDED: register NFR section, confirmed by direct re-read — note these RTO/RPO figures originate from the register, not the BRD itself; flagged if BRD silence matters] Our RGIA 18+ month live O&M track record supports this commitment. [GROUNDED: RGIA case study] The full O&M support ladder (Sev1 ≤ 30min response / 4hr workaround, Sev2 ≤ 1hr / 8hr, Sev3 ≤ 4 business hrs / 5 business days, Sev4 ≤ 1 business day / 30 days) elaborates on the BRD's ≤ 10-minute Critical/Severity-1 headline KPI without contradicting it. [GROUNDED: Consolidated FINAL O&M ladder; CR/BRD §2.3 KPI-6 for the ≤10-min headline — R-017]

## Exit Management (R-131)

6-month minimum transition support at contract end, no additional cost. [GROUNDED: CR/BRD §9.12; Consolidated FINAL explicitly commits to the 6-month figure matching the BRD]

## Regulatory Approvals (R-134)

WAISL is the incumbent Concessionaire already operating under the necessary BCAS, AAI, and other regulatory approvals at IGIA since the 2019 CA; we obtain and maintain all such approvals at our own cost. [GROUNDED: CR/BRD §9.12 "Applicable Laws and Approvals"; WAISL incumbent status per brief — R-134]

---

**Bridge.** The implementation plan above is costed and milestone-structured in Volume 5.