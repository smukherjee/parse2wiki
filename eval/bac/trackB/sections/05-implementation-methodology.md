# 05 — Implementation Methodology

## What BAC requires

RFP §3.3 requires delivery "through a controlled, transparent, and auditable project lifecycle." Tab.F PMR-02 mandates defined phases: Initiation, Design, Build, Test, Implementation, Closure. PMR-06 requires project documentation (PM plan, schedule, status reports, design, test plans, as-built). PMR-09 ties practical completion to cutover + tests + docs + training, with 20% withheld. PMR-10 requires a six-month defects-liability plus maintenance agreement. [GROUNDED: Response Sheet Tab.F PMR-02..PMR-10; RFP §3.3]

## Methodology — phased delivery

WAISL proposes a phased delivery aligned to PMR-02 sub-rows, governed by weekly project meetings (PMR-03) and BAC change control (PMR-05).

### Phase 1 — Initiation (PMR-02a)

Produce a Project Management Plan covering stakeholders, risk analysis, and schedule; confirm integration scope and ownership with BAC pre-kickoff (NF08); agree the ISRA approach (NF01) and the Australian hosting target (ISRA-19, ISRA-25). [ASSERTION: standard PM initiation — coverage-matrix PMR-02a, NF08, NF01]

### Phase 2 — Design (PMR-02b, PMR-06a)

Workshops with Terminal Operations, Airside Operations, and BAC IT&T to produce a Detailed Design Document documenting the full solution with FR traceability. This is where the FR17 GSE-type CV classifier, the FR20 personnel-presence model, and the FR26/27/28/69 AI-governance pack are specified with acceptance criteria. The Hardening Checklist and DPIA inputs (where applicable) are delivered here. [ASSERTION: UTAM detailed-design approach — coverage-matrix PMR-02b/06a] [GAP: FR17/FR20/FR23/FR26/FR27/FR69 are committed in design, not pre-evidenced — see Section 03]

### Phase 3 — Build (PMR-02c)

Configure the platform per design across DEV/TST/PROD using Infrastructure as Code, with environment parity. [GROUNDED: UTAM IaC env parity — coverage-matrix PMR-02c] Build the Edge Vision Controller CV models for FR17/FR20, the AIDX connector (FR15/FR43/FR54), and the AI-governance pack. [ASSERTION: UTAM low-code configuration over code — coverage-matrix FR15/FR43/FR54]

### Phase 4 — Test (PMR-02d, PMR-06b)

Install in the Test environment, execute a Comprehensive Test Plan with requirement traceability, and support UAT. Automated testing pyramid (unit, contract/integration, end-to-end, performance) is asserted. [ASSERTION: UTAM automated testing pyramid; methodology doc not provided — coverage-matrix PMR-02d/06b, NF13/NF14] [GAP: NF09/NF10 — QA standards, tools, methodology not yet evidenced — coverage-matrix NF09/NF10] The FR17 and FR20 CV models must pass per-class and per-scenario acceptance criteria in this phase before the corresponding Tab.F rows are marked conformant. [ASSERTION: phased acceptance tied to the 20% withhold — coverage-matrix FR17 action; PMR-09]

### Phase 5 — Implementation (PMR-02e, PMR-06c)

Production cutover in an agreed BAC change window, with rollback (blue/green, DB migration revert) and a post-cutover debrief. [GROUNDED: UTAM blue/green + rollback + DB migration revert — coverage-matrix PMR-02e/06c] All changes feed BAC's Change Approval Board (PMR-05, ISRA-11). [GROUNDED: UTAM change management process — coverage-matrix PMR-05, ISRA-11]

### Phase 6 — Closure (PMR-02f, PMR-06d, PMR-09)

Defect inspection and rectification, as-built documentation reflecting the final solution, end-user and technical training (PMR-07, PMR-08), and practical completion with the 20% withhold released on BAC acceptance. [ASSERTION: standard closure — coverage-matrix PMR-02f/06d/09] [ASSERTION: UTAM training commitment generic — coverage-matrix PMR-07/08]

### Phase 7 — Defects liability (PMR-10)

Six-month defects liability plus maintenance agreement aligned to the support tiers in Section 10. [GAP: PMR-10 — not in collateral — coverage-matrix PMR-10; accepted as a contractual term]

## Change control and risk management

All production changes follow a documented change-management process with impact assessment, BAC CAB approval, and scheduled implementation in agreed maintenance windows (PMR-05, ISRA-11). [GROUNDED: UTAM change management process — coverage-matrix PMR-05/ISRA-11] The platform continuously monitors for configuration drift. [GROUNDED: UTAM Change Management & Operational Security]

Risk mitigation strategy (NF11) is asserted from the UTAM risk framework. [ASSERTION: UTAM risk framework implied — coverage-matrix NF11] WAISL's multi-region footprint (UK | India | UAE | Kuwait | Australia | Singapore) enables additional resources to be drawn on to keep timelines (NF12). [ASSERTION: WAISL multi-region footprint — coverage-matrix NF12]

## WHS and contractor status (PMR-04)

WAISL operates an Australia office and will comply with BAC's Work Health and Safety requirements, Safe Work Method Statements, and the BAC contractor management system registration (including the annual fee). Personnel requiring airside access will obtain Aviation Security Identification Cards (ASICs). [ASSERTION: WAISL operates in Australia; WHS process not yet evidenced — coverage-matrix PMR-04; RFP Annexure A §14–§16]

## Non-disruptive upgrades and release train

The platform ships on the current GA/LTS release and follows a predictable release train — monthly maintenance, quarterly feature releases, annual LTS — with blue/green and canary deployments, pre-flight checks, automated DB migrations with rollback, and verified backup/restore tests. [GROUNDED: UTAM Non-disruptive Upgrades] API backward compatibility is maintained via semantic versioning. [GROUNDED: UTAM Non-disruptive Upgrades]

> The project management and governance overlay is described in Section 06.