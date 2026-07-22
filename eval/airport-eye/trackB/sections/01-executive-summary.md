# Volume 1 — Executive Summary

## Procurement Framing and Structural Assumption

This submission is prepared by **WAISL Limited**, the incumbent Concessionaire under the Concession Agreement (CA) dated 30-September-2019, with GEOKNO as geospatial/LiDAR/BIM delivery partner. The binding Change Request / Business Requirements Document (CR/BRD v1.5, DIAL-AE-BRD-001, 05-June-2026) frames this cycle as a Change Request against that existing Concession Agreement, stating in §1.2 that "the Concessionaire is requested to submit its quotation in accordance with the provisions of the Concession Agreement." [GROUNDED: CR/BRD v1.5 §1.2]

A structural ambiguity must be flagged honestly at the outset: the base RFP v5 carries a full competitively-scored apparatus (3-stage evaluation panel, weighted scoring, 7-volume submission structure, pre-qualification gates), and no document in the corpus explicitly states whether that apparatus remains operative under the CR framing or has been superseded. [GAP: R-001 — unresolved contradiction between binding sources; neither document states the other is superseded on this point.] **We draft this submission against the more complete RFP v5 structure as a conservative default** — a formal 7-volume response is a strict superset that can be trimmed to a CA-referenced quotation letter if DIAL confirms the negotiated-CR framing, whereas a quotation letter cannot retroactively acquire evaluation-compliant structure. We request DIAL confirmation on this point and will reformat accordingly.

## DIAL's Problem, In DIAL's Words

IGIA's OT/BMS estate is fragmented and largely unintegrated. The authoritative PE_OT system inventory lists 19 distinct OT systems (HVAC, FDAS, VHT, ECMS, LCMS, PBB, VDGS, WTP/STP, MRSS, BHS, ATRS, GPU/PCA, AGL CMS, and others) across 10+ OEMs and integrators, with the remark **"Not integrated with T3 ITBMS"** recurring across nearly every row. [GROUNDED: PE_OT System_09.06.pptx.md — 19-system inventory, confirmed by direct re-read of all 19 rows] Operations today are reactive: incidents, equipment failures, and safety/security events are discovered after the fact rather than predicted or pre-empted. [GROUNDED: CR/BRD v1.5 §1.2 background — evolution toward "a global benchmark for intelligent, data-driven airport operations"]

DIAL's desired outcome, stated verbatim in the binding BRD §2.1, is "a living, dynamic, and spatially accurate digital replica of the entire airport ecosystem, including the Aerocity precinct... a network of federated AI-driven agents with spatial intelligence, operating continuously (24/7), that act as the 'digital eye' of the airport" — transitioning operations "from reactive management to predictive and autonomous intelligence." [GROUNDED: CR/BRD v1.5 §2.1]

## Our Response, In Summary

As the incumbent Concessionaire operating under these approvals at IGIA since 2019, WAISL with GEOKNO offers a two-layer architecture directly aligned to DIAL's vision: a **Geo Digital Twin** (survey-grade geospatial/BIM foundation) underlying an **Operational Digital Twin / AIOP layer** hosting the eight federated AI-driven agents the BRD §3.5.3 names as mandatory. [GROUNDED: Airport_Eye_Consolidated_Proposal_FINAL.docx.md — two-layer architecture, 8-agent table, BRD-aligned figures]

Our strongest evidenced proof point is the **Rajiv Gandhi International Airport (RGIA), Hyderabad** deployment: 18+ months live operation, 40+ integrated systems, 100+ KPIs tracked — a direct operational analog for the multi-system unification DIAL requires. [GROUNDED: RGIA case study, per Consolidated FINAL and v9 proposal]

## Headline Commitments (Binding KPIs)

| KPI | BRD Target | Our Commitment | Source |
|---|---|---|---|
| Platform Uptime | ≥ 99.5% (excl. planned maintenance) | Match | [GROUNDED: CR/BRD §2.3 KPI-1] |
| Real-time data latency | ≤ 5 seconds sensor-to-dashboard | Match | [GROUNDED: CR/BRD §2.3 KPI-2] |
| BIM LOD compliance | 100% of specified assets | Match | [GROUNDED: CR/BRD §2.3 KPI-3] |
| Predictive alert accuracy | ≥ 80% precision / ≥ 75% recall | Match | [GROUNDED: CR/BRD §2.3 KPI-4] |
| Geospatial accuracy | ≤ 5cm H RMSE / ≤ 3cm V RMSE | Match | [GROUNDED: CR/BRD §2.3 KPI-5] |
| Critical incident response | ≤ 10 minutes from notification | Match | [GROUNDED: CR/BRD §2.3 KPI-6, triple-confirmed] |
| System integration coverage | 100% of agreed BMS/IoT points within 3 months of go-live | Match | [GROUNDED: CR/BRD §2.3 KPI-7] |

We note explicitly that RFP v5's own KPI table states a materially different ≤ 1 hour Critical Incident Response figure for the same metric; per the binding-priority order we adopt the BRD's ≤ 10 minute figure and treat the RFP v5 ≤ 1 hour figure as superseded. [GROUNDED: coverage-matrix R-017 — direct re-read confirmed the discrepancy; BRD governs per binding priority]

## Honest Gaps We Flag Rather Than Disguise

Four gaps must be named plainly, because an evaluator reading alongside competitors can distinguish a vendor who has done this from one improvising:

1. **Procurement mechanism ambiguity (R-001)** — flagged above; this submission's structural assumption is labelled, not silently chosen.
2. **Comparable deployments / case studies (R-007, R-128)** — RFP v5 Appendix E requires ≥ 2 comparable deployments for pre-qualification and Volume 6 requires ≥ 3 case studies. Only **RGIA (Hyderabad)** is fully evidenced in our current collateral; two of three case-study slots are explicit placeholders pending bidder input. [GAP: R-007, R-128 — only 1 of 2–3 required references currently evidenced]
3. **Team & staffing (R-129)** — no named personnel, CVs, or staffing plan exist in any reviewed collateral. We do not fabricate bios. [GAP: R-129 — complete blank; Volume 7 drafted as an honest placeholder with a staffing-plan skeleton, pending capture-team input]
4. **IEC 62443 OT cybersecurity certification (R-056) and SOC/SIEM track record (R-059)** — not held or evidenced in our collateral; addressed via a compliance roadmap and named-partner mitigation rather than a false assertion of certification in hand. [GAP: R-056, R-059]

One additional self-inflicted risk is worth naming: one of our own prior proposals (`DIAL APOC Phase II Proposal 1.pdf.md`) proposed AWS Singapore-region DR hosting, which directly contradicts the BRD's binding India-only data-sovereignty clause (§9.10). We explicitly exclude that hosting language from this submission and commit to India-only data residency throughout. [GROUNDED: coverage-matrix R-061 — direct contradiction identified and excluded]

## Where This Submission Goes Next

Volume 2 details our technical approach and solution architecture. Volume 3 addresses the AI and analytics capability that DIAL's own evaluation emphasis (the most granular numeric tables in the corpus) marks as the technologically transformative core. Volume 4 covers implementation methodology and timeline. Volume 5 presents the commercial structure. Volume 6 presents qualifications and the available case study. Volume 7 addresses team & staffing honestly. Appendices carry the requirements traceability matrix.