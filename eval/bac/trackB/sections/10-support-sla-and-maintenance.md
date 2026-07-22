# 10 — Support, SLA, and Maintenance

## Disqualifying gap 5 — NF19: Severity response scenarios

**Requirement (NF19, Must-Have):** severity-1 response within 1 hour 24×7×365; Sev-2 within 4 hrs business-day / 8 hrs non-business; Sev-3 within 8 hrs; resolution commitments.

**Evidence position:** neither Turnwise nor UTAM provides a support-tier response matrix or evidence of 24/7/365 capability. [GAP: NF19 — gap-report.md §3; coverage-matrix NF19]

**Resolution:** WAISL commits to the following support matrix meeting or exceeding NF19 thresholds. [ASSERTION: committed support matrix — coverage-matrix NF19 action]

## Committed support SLA matrix

| Severity | Definition | Response | Update cadence | Resolution target |
|----------|------------|----------|----------------|-------------------|
| Sev-1 (Critical) | Production down; data loss; safety-impacting alert failure | ≤1 hour, 24×7×365 | Every 1 hour | Best-effort continuous until restored |
| Sev-2 (High) | Major feature unavailable; significant degradation | ≤4 hrs business-day; ≤8 hrs non-business | Every 4 hours | Within 1 business day |
| Sev-3 (Medium) | Functional issue with workaround | ≤8 business hrs | Daily | Within 3 business days (NF20: Sev-3 resolution within 8 business hrs committed) |
| Sev-4 (Low) | Cosmetic, minor, enhancement | ≤1 business day | As agreed | Next release or per agreement |

[ASSERTION: committed matrix meeting/exceeding NF19/NF20 — coverage-matrix NF19/NF20]

## 24/7/365 capability

WAISL's multi-region footprint — **UK | India | UAE | Kuwait | Australia | Singapore** — enables a follow-the-sun support model providing 24/7/365 phone, email, and online coverage (NF17). [ASSERTION: WAISL multi-region office footprint supports follow-the-sun 24/7 — UTAM cover page; coverage-matrix NF17/NF19] [GAP: NF17 — not explicitly stated in collateral; committed — coverage-matrix NF17]

A local WAISL Australia representative provides BAC account escalation (NF22). [ASSERTION: WAISL Australia office listed — coverage-matrix NF22]

## Incident management

A formal incident-handling procedure aligned to ISO 27001 covers classification, escalation, containment, eradication, recovery, and post-incident review (NF21, ISRA-12). BAC is notified within 1 hour of a confirmed security incident. [GROUNDED: UTAM Operational & Support Commitments — incident handling — coverage-matrix NF21/ISRA-09/ISRA-12] Documented incident management with response SLAs per priority (NF21). [ASSERTION: UTAM ISO 27001 incident handling — coverage-matrix NF21]

## Support channels and help (NF17, NF18, NF23, NF24, NF26)

- 24/7/365 phone, email, online help (NF17). [GAP/ASSERTION: committed; not explicitly in collateral — coverage-matrix NF17]
- Client-configurable help & knowledge artefacts (NF18). [GAP: coverage-matrix NF18; committed]
- Help-desk field-level info (NF23). [GAP: coverage-matrix NF23; addressable — standard help capability]
- Clear support/help options in the UI (NF24). [ASSERTION: Turnwise UI; not explicit — coverage-matrix NF24]
- Customised quick-reference guides, with cost stated in Schedule E if additional (NF26). [GAP: coverage-matrix NF26; committed]

## Training (NF27–NF30)

- Admin/user training (format and cost in Schedule E) (NF27). [ASSERTION: UTAM training commitment generic — coverage-matrix NF27]
- Ongoing training (inclusive/exclusive of managed services; cost) (NF28). [ASSERTION: implied — coverage-matrix NF28]
- Training & materials for new features/patches (NF29). [ASSERTION: UTAM release train — coverage-matrix NF29]
- Training & support to suppliers (airlines, GHAs) (NF30). [ASSERTION: platform multi-stakeholder — coverage-matrix NF30]

End-user training in the Test environment with cheat sheets (PMR-07); technical training for BAC personnel on architecture, fault-finding, and configuration (PMR-08). [ASSERTION: UTAM training commitment generic — coverage-matrix PMR-07/08]

## Availability reporting and history

Daily availability and transaction-performance data provided via API or automated email. [GROUNDED: UTAM Operational & Support Commitments] A 3-year history of system availability, failures, and downtime (NF05) is not evidenced in collateral; we commit to SLA reporting going forward and will publish historical availability metrics from existing deployments if available. [GAP: NF05 — coverage-matrix NF05; commit to SLA reporting going forward]

## Maintenance and upgrades

Non-disruptive upgrades via blue/green, canary, and rolling deployments, coordinated during agreed maintenance windows, with pre-flight checks, automated DB migrations with rollback, and verified backup/restore tests (PMR-05, ISRA-11). [GROUNDED: UTAM Non-disruptive Upgrades; UTAM Change Management & Operational Security] Security and hotfix patches as needed, monthly maintenance, quarterly feature releases, annual LTS. [GROUNDED: UTAM Non-disruptive Upgrades]

## Defects liability and ongoing maintenance (PMR-10)

Six-month defects liability plus a maintenance agreement aligned to the support tiers above. [GAP: PMR-10 — not in collateral — coverage-matrix PMR-10; accepted contractual term]

> Compliance with Tab.F requirements is summarised in Section 11.