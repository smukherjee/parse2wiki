# 09 — Testing, Acceptance, and Handover

## Testing methodology (NF13, NF14, PMR-02d, PMR-06b)

WAISL will deliver a Comprehensive Test Plan with requirement traceability to Tab.F (PMR-06b). The UTAM platform supports an automated testing pyramid — unit, contract/integration, end-to-end, performance testing — through CI/CD pipelines with policy gates for security, performance, and compliance. [GROUNDED: UTAM DevOps & CI/CD Framework — coverage-matrix PMR-02d/06b, NF13]

We acknowledge that the specific QA standards/accreditations/methodologies (NF09) and QA tools/technology (NF10) are not evidenced in our collateral and will be supplied from WAISL's internal QA process documentation before submission. [GAP: NF09/NF10 — coverage-matrix NF09/NF10; addressable]

## Test phases

- **Unit & contract testing** — automated in CI/CD per build. [ASSERTION: UTAM automated testing pyramid — coverage-matrix NF13/NF14]
- **Integration testing** — connectors (AODB, ADS-B, telematics, vision, weather, RVR, AIDX, FIDS) tested against BAC test endpoints. [GROUNDED: UTAM connectors — coverage-matrix NF15/NF16]
- **System & performance testing** — end-to-end turnaround detection, alerts, dashboards, reporting under load; scalability for very large groups (NF31). [ASSERTION: UTAM scalable microservices — coverage-matrix NF31]
- **UAT** — BAC Terminal Operations and Airside Operations users exercise the platform in the Test environment against agreed acceptance criteria (PMR-02d). [ASSERTION: UTAM automated testing supports UAT — coverage-matrix PMR-02d]
- **Security testing** — predelivery penetration test by an accredited third party, with retest until closure (see Section 08). [GROUNDED: UTAM Penetration Testing Alignment]
- **CV model acceptance (FR17, FR20, FR23)** — per-class and per-scenario acceptance criteria for the GSE-type classifier and personnel-presence model, agreed in Detailed Design and executed before the corresponding Tab.F rows are marked conformant. [ASSERTION: phased acceptance tied to PMR-09 withhold — coverage-matrix FR17/FR20/FR23 action]

## Requirement traceability

The Test Plan maps every Tab.F row (FR01–FR73, NF01–NF48, PMR-01..PMR-10, ISRA 1–29) to a test case or to a committed-delivery acceptance criterion (for gap rows), providing the traceability PMR-06b requires. [ASSERTION: standard traceability practice — coverage-matrix PMR-06b]

## Acceptance criteria

Each deliverable in Section 04 has acceptance criteria:

- Detailed Design accepted by BAC before Build (PMR-02b). [ASSERTION: standard — coverage-matrix PMR-02b]
- Build configured across DEV/TST/PROD per design (PMR-02c). [GROUNDED: UTAM IaC env parity — coverage-matrix PMR-02c]
- Test plan executed, UAT signed off (PMR-02d). [ASSERTION: standard — coverage-matrix PMR-02d]
- Production cutover in change window with rollback verified (PMR-02e, PMR-06c). [GROUNDED: UTAM blue/green + rollback — coverage-matrix PMR-02e/06c]
- As-built documentation reflects the final solution (PMR-06d). [ASSERTION: standard — coverage-matrix PMR-06d]
- Training delivered (PMR-07, PMR-08). [ASSERTION: UTAM training commitment generic — coverage-matrix PMR-07/08]
- Practical completion signed by BAC; 20% withhold released (PMR-09). [ASSERTION: contractual — coverage-matrix PMR-09]

## Handover

Handover includes:

- As-built documentation (PMR-06d). [ASSERTION: standard — coverage-matrix PMR-06d]
- Operational runbooks (backup/restore, incident response, change management). [ASSERTION: UTAM operations runbook referenced in HA/DR section — coverage-matrix]
- Admin and end-user training materials plus customised quick-reference guides (NF26). [GAP: NF26 — coverage-matrix NF26; committed, cost stated in Schedule E]
- Credentials, documentation, and (if applicable) escrow confirmation (ISRA-20). [GROUNDED: UTAM Contractual & Exit Provisions]
- Daily availability and transaction-performance reporting (via API or automated email). [GROUNDED: UTAM Operational & Support Commitments]

## Defects liability (PMR-10)

Six-month defects liability period from practical completion, with a maintenance agreement aligned to the support tiers in Section 10. [GAP: PMR-10 — not in collateral — coverage-matrix PMR-10; accepted contractual term]

> Ongoing support, SLA, and maintenance are in Section 10.