# 08 — Security, ISRA, and Compliance

## The problem this section must solve

Tab.F ISRA rows 1–29 and NF01 require a completed BAC Information Security Risk Assessment, grounded in Australian regulatory framing. Our reusable UTAM architecture artefact was written for a European customer and frames compliance around GDPR/NIS2/Hellenic DPA with EU residency. **We do not propagate that framing.** We rewrite every residency, privacy, and ownership narrative for Brisbane/Australia. This section directly addresses the two disqualifying sovereignty gaps (ISRA-19, ISRA-25). [GROUNDED: gap-report.md §2; brief.md Source Conflicts]

## Disqualifying gap 3, ISRA-19: Data sovereignty management

**Requirement (ISRA-19, Must-Have):** data sovereignty management, with data hosted in Australia under Australian law.

**Evidence position:** UTAM asserts "All data is hosted exclusively within European Union (EU) data centres" and "AWS EU region deployment is used to satisfy data residency requirements under GDPR and NIS2." This conflicts with BAC's Australian context. [GAP: ISRA-19 — gap-report.md §2; coverage-matrix ISRA-19]

**Resolution:** WAISL commits to Australian hosting for all BAC data, in AWS Sydney region (`ap-southeast-2`) or BAC private cloud at BAC's election. The platform's stated deployment agnosticism and private-cloud option make this reconcilable without architectural change. [ASSERTION: UTAM already claims "deployment agnosticism" and a private-cloud option — UTAM Deployment Architecture note — coverage-matrix ISRA-19 action] All residency, compliance, privacy, and data-ownership narrative is rewritten to the Australian regulatory frame: **Australian Privacy Act 1988 / Australian Privacy Principles (APPs)**, **ASD Essential 8 / IRAP alignment**, and **BAC as the exclusive data owner**. [ASSERTION: reframe from GDPR/EU to Australian Privacy Act/APPs/ASD Essential 8 — brief.md Source Conflicts resolution] Every AIA/Athens/Hellenic-DPA/GDPR reference in the source artefact is excluded from BAC proposal text.

With this commitment, ISRA-19 moves from Disqualifying Gap to Addressable, subject to BAC confirming the preferred hosting target (AWS Sydney vs BAC private cloud). That open question will be closed at Initiation. [GAP: open question — brief.md Open Questions — hosting target]

## Disqualifying gap 4, ISRA-25: Hosting geographical address

**Requirement (ISRA-25, Must-Have):** hosting location, as a geographical address.

**Evidence position:** UTAM cites EU/Athens addresses. [GAP: ISRA-25 — gap-report.md §2; coverage-matrix ISRA-25]

**Resolution:** WAISL commits to an Australian data-centre address. Proposed default: **AWS Sydney region (`ap-southeast-2`)**, with the specific AWS data-centre address supplied in the completed ISRA tab once BAC confirms the hosting target. If BAC elects private cloud, the address will be the BAC data-centre address. [ASSERTION: AWS Sydney ap-southeast-2 as the default Australian region — standard AWS region designation; coverage-matrix ISRA-25 action]

## Security architecture, grounded

UTAM operates under a zero-trust security model: verify explicitly, enforce least privilege, assume breach, applied across every layer, not just the perimeter. [GROUNDED: UTAM Zero-Trust Security Architecture]

- **Identity-centric**: every request (users, services, automated processes) authenticated and authorised independently. [GROUNDED: UTAM Zero-Trust — identity-centric]
- **mTLS for service-to-service**: no plaintext internal communication. [GROUNDED: UTAM Zero-Trust — mTLS]
- **Short-lived credentials**: access tokens rotated automatically; no long-lived static credentials. [GROUNDED: UTAM Zero-Trust — short-lived credentials]
- **PAM for privileged access**: break-glass access requires PAM approval, is time-limited, and is fully audit-logged (ISRA-05). [GROUNDED: UTAM Zero-Trust — PAM; coverage-matrix ISRA-05]
- **Micro-segmentation**: lateral movement restricted by policy. [GROUNDED: UTAM Zero-Trust — micro-segmentation]

## ISRA row-by-row mapping (summary)

- **ISRA-01 ISO/IEC 27001** — UTAM states ISO 27001 certified; WAISL cover page lists 9001/20000/27001/22301. [GROUNDED: UTAM Certifications; UTAM cover page — coverage-matrix ISRA-01]
- **ISRA-02 sensitive info collected** — apron video analytics may capture images of personnel; PII handling to be confirmed with BAC in the ISRA. [ASSERTION: apron video analytics; PII handling to be confirmed with BAC — coverage-matrix ISRA-02]
- **ISRA-03 auto-delete when no business requirement** — UTAM retention policies with automated enforcement. [GROUNDED: UTAM retention policies — coverage-matrix ISRA-03]
- **ISRA-04 asset disposal sanitisation** — UTAM secure erasure + Certificate of Destruction. [GROUNDED: UTAM exit provisions — coverage-matrix ISRA-04]
- **ISRA-05 privileged access management** — UTAM PAM + break-glass. [GROUNDED: coverage-matrix ISRA-05]
- **ISRA-06 infosec roles in contract** — standard contractual clauses to be included. [ASSERTION: standard contractual clauses — coverage-matrix ISRA-06]
- **ISRA-07 mature information security policy** — UTAM ISO 27001 ISMS. [GROUNDED: coverage-matrix ISRA-07]
- **ISRA-08 annual security awareness training** — UTAM staff awareness training. [GROUNDED: coverage-matrix ISRA-08]
- **ISRA-09 breach notification process** — UTAM incident handling, 1-hour notification. [GROUNDED: UTAM Operational & Support Commitments — incident handling — coverage-matrix ISRA-09]
- **ISRA-10 security updates & patching** — UTAM release train/patch cadence. [ASSERTION: UTAM release train/patch cadence — coverage-matrix ISRA-10]
- **ISRA-11 change management feeding BAC CAB** — UTAM change management. [GROUNDED: coverage-matrix ISRA-11]
- **ISRA-12 incident response management** — UTAM incident response (classification, escalation, containment, eradication, recovery, post-incident review), aligned to ISO 27001. [GROUNDED: UTAM Operational & Support Commitments — coverage-matrix ISRA-12]
- **ISRA-13 cryptographic controls** — UTAM AES256 at rest, TLS 1.2 in transit, KMS-managed keys. [GROUNDED: UTAM Data Protection & Encryption — coverage-matrix ISRA-13]
- **ISRA-14 system secure & resilient against cyber attack** — UTAM zero-trust, WAF, GuardDuty, Inspector, hardening (CIS/STIG). [GROUNDED: UTAM Secure Connectivity; UTAM Certifications table — coverage-matrix ISRA-14]
- **ISRA-15 protection against malicious software** — UTAM Defender for Server / antimalware. [GROUNDED: UTAM Server hardware commitment — coverage-matrix ISRA-15]
- **ISRA-16 meet BAC availability incl. RTO & RPO** — UTAM RTO ≤40 min, RPO near-zero. [GROUNDED: UTAM HA/DR table — coverage-matrix ISRA-16]
- **ISRA-17 backup testing to ensure RTO/RPO** — UTAM scheduled restore tests. [GROUNDED: UTAM Backup & Recovery Framework — coverage-matrix ISRA-17]
- **ISRA-18 network management** — UTAM NGFW, WAF, mTLS, segmentation. [GROUNDED: UTAM Secure Connectivity — coverage-matrix ISRA-18]
- **ISRA-19 data sovereignty** — see resolution above. [GAP reconciled via Australian hosting commitment — coverage-matrix ISRA-19]
- **ISRA-20 service escrow** — UTAM source-code escrow agreement with a recognised third-party agent, updated with each major release. [GROUNDED: UTAM Contractual & Exit Provisions — coverage-matrix ISRA-20]
- **ISRA-21 privacy & right to anonymity** — UTAM frames privacy via GDPR/pseudonymisation; for BAC we reframe to the Australian Privacy Act 1988 / APPs, with pseudonymisation/anonymisation for analytics workloads and data minimisation. [ASSERTION: reframe from GDPR to Australian Privacy Act/APPs — coverage-matrix ISRA-21]
- **ISRA-22 physical & environmental security** — AWS data-centre physical controls (theft, fire, heat, power). [GROUNDED: UTAM ISRA-22 — coverage-matrix]
- **ISRA-23 compliance management & validation during contract** — UTAM continuous validation + annual review. [GROUNDED: UTAM Operational & Support Commitments — annual review — coverage-matrix ISRA-23]
- **ISRA-24 formal incident plans, tested regularly** — UTAM incident response plan exists; regular testing not yet evidenced. [ASSERTION: UTAM incident response plan; regular testing to be committed — coverage-matrix ISRA-24]
- **ISRA-25 hosting geographical address** — see resolution above. [GAP reconciled via Australian address commitment — coverage-matrix ISRA-25]
- **ISRA-26 vetting of staff with privileged access** — standard vetting; not explicitly described in collateral. [ASSERTION: standard; to be confirmed with WAISL security/legal — coverage-matrix ISRA-26]
- **ISRA-27 application whitelisting** — not evidenced. [GAP — coverage-matrix ISRA-27; committed in ISRA response]
- **ISRA-28 MFA across service provider's business** — UTAM MFA across privileged/admin. [GROUNDED: UTAM IAM — coverage-matrix ISRA-28]
- **ISRA-29 security event/log management; retention duration** — UTAM CloudTrail/CloudWatch + retention policies. [GROUNDED: UTAM Logging, Monitoring & Auditability — coverage-matrix ISRA-29]

## IAM and access (FR60–FR67, NF32–NF46)

RBAC and ABAC are enforced at the API, dashboard, and data layers, where row-level and column-level access controls ensure even authenticated users see only authorised data. [GROUNDED: UTAM RBAC/ABAC — coverage-matrix FR60–FR62, NF33/NF34] External parties (airlines, ground handlers) access only their own operational data through role-restricted views with full audit logging (FR61). [GROUNDED: UTAM RBAC/ABAC — external party access — coverage-matrix FR61]

SSO via Azure Entra ID / Azure AD for BAC users (Windows integrated authentication, with no re-authentication after desktop login), with OpenLDAP and OneLogin SSO for third-party stakeholders (FR67, NF36, NF42). [GROUNDED: UTAM Authentication & Identity Management — coverage-matrix FR67/NF36/NF42] Mandatory MFA for all administrative and privileged access (NF35, ISRA-28). [GROUNDED: UTAM IAM — coverage-matrix NF35/ISRA-28] Just-in-time admin delegation with short-lived credentials (NF43). [GROUNDED: UTAM Zero-Trust — short-lived credentials — coverage-matrix NF43] No browser plug-ins required (NF39). [GROUNDED: UTAM Self-Service BI — "no client-side software installation" — coverage-matrix NF39]

Real-time system logs and technical diagnostics (NF45), user auth/app usage/audit reports (NF46), and centralised searchable logs for high-volume event search (NF48) are grounded in CloudTrail/CloudWatch. [GROUNDED: UTAM Logging, Monitoring & Auditability — coverage-matrix NF45/NF46/NF48] Geolocation on authentications (NF47) is not evidenced and is committed as a low-cost feature. [GAP: NF47 — coverage-matrix NF47; committed]

## Availability, DR, and resilience (NF04–NF07, ISRA-16/17)

| HA/DR Parameter | Specification |
|----------------|---------------|
| Target Availability | ≥99.9% (24×7) |
| RTO | ≤40 minutes |
| RPO | near-zero |
| Deployment | Multi-AZ for all production workloads |
| Database HA | Multi-instance with automated failover and point-in-time recovery |
| Message Queue | Fully replicated across AZs |
| Auto-healing | Kubernetes self-healing with HPA |
| Backup | Automated DB backups + continuous replication + versioned object storage |

[GROUNDED: UTAM HA/DR table — coverage-matrix NF04/NF06/NF07/ISRA-16/17]

Daily backups with 30-day retention for operational data (and longer for archival per the agreed retention policy); full backups stored in a separate region for DR. [GROUNDED: UTAM Server hardware commitment — backup schedule]

## Certifications and standards

WAISL holds ISO 9001, 20000, 27001, and 22301 certifications (cover page). [GROUNDED: UTAM cover page] The solution is delivered on an ISO 27001-certified cloud foundation, with a SOC-2 Type II roadmap. [GROUNDED: UTAM Certifications & Standards Alignment table] For BAC, we will additionally align to **ASD Essential 8** and **IRAP** framing on request, recognising that BAC's environment is Australian-regulated. [ASSERTION: reframe to ASD Essential 8/IRAP — brief.md Open Questions]

## Penetration testing

- Predelivery penetration test by an accredited third party before Provisional Acceptance, covering all application and infrastructure components. [GROUNDED: UTAM Penetration Testing Alignment]
- Retest until no exploitable critical/high/medium vulnerabilities remain; only then is the system accepted into production. [GROUNDED: UTAM Penetration Testing Alignment]
- Alignment with BAC's annual penetration testing plan; additional tests on 30 days' notice. [GROUNDED: UTAM Penetration Testing Alignment — rewritten for BAC]
- BAC's right to perform penetration tests against the platform with prior notice is acknowledged. [GROUNDED: UTAM INFOSEC Policies & Right to Pen Test — rewritten for BAC]

## Escrow and exit

Source-code escrow agreement with a recognised third-party agent, updated with each major release (ISRA-20). [GROUNDED: UTAM Contractual & Exit Provisions] Exit plan: return of all BAC data in machine-readable format (CSV/JSON/API) within 15 working days; secure erasure of all copies with Certificate of Data Destruction; handover of credentials, documentation, and (if applicable) escrowed source. [GROUNDED: UTAM Contractual & Exit Provisions — rewritten for BAC as data owner]

## Data ownership

All data generated, processed, or stored within the platform is the exclusive property of **Brisbane Airport Corporation**, not WAISL and not a European customer. [ASSERTION: rewritten from UTAM's AIA ownership clause — brief.md Source Conflicts; coverage-matrix ISRA-19/25 action]

> Testing, acceptance, and handover are described in Section 09.