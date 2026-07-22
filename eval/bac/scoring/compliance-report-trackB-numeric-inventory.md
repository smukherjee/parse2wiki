# Numeric / Quantitative Requirements Inventory — Track B

**Proposal under validation:** `eval/bac/trackB/proposal-trackB.md`
**Authoritative RFP:** `sources/BAC/BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md`
**Response sheet:** `sources/BAC/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md`
**Cross-check collateral:** `sources/BAC/Turnwise Product Document 1.pdf.md`, `sources/BAC/UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`
**Validation date:** 2026-07-17

Binding hierarchy: RFP §4 (commercial/insurance) + Response Sheet Tab.F (FR/NF/PMR/ISRA) govern. UTAM/Turnwise collateral is non-binding evidence, not a requirements source. Where UTAM's Athens/AIA/EU/GDPR framing conflicts with the RFP's Australian context, the RFP governs and the proposal must rewrite, not propagate.

## Column definitions

| Column | Description |
|---|---|
| `requirement_id` | Unique ID for this numeric requirement. |
| `domain` | `insurance`, `term`, `submission`, `sla`, `dr`, `pm`, `fr`, `nf`, `isra` |
| `parameter` | Human-readable parameter name. |
| `binding_value` | Strictest value from the authoritative source documents. |
| `operator` | `≤`, `≥`, `=`, `minimum` |
| `unit` | Unit of measurement. |
| `source_document` | Exact filename of the source document. |
| `source_location` | Section / row in the source. |
| `applies_to` | What the requirement applies to. |
| `proposal_value` | Corresponding value found in the proposal. |
| `target_location` | Line/section in the proposal. |
| `declared_in_deviation_register` | `Yes` / `No` / `n/a` |
| `deviation_register_id` | Deviation/assumption entry ID. |
| `ratio_or_delta` | How the proposal value compares to binding. |
| `verdict` | `Pass` / `Partial` / `Fail` / `Ambiguous` / `N/A` |
| `notes` | Rationale, severity, carve-out wording, remediation. |

## Inventory

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-INS-01 | insurance | Public Liability | 20 | ≥ | $M | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | RFP §4.4 / Insurance tab | Public Liability cover | $20M | §12 table, line 895 | n/a | n/a | 1.0× | Pass | Meets binding minimum. Certificates of currency to be supplied (Schedule A). |
| N-INS-02 | insurance | Professional Indemnity | 10 | ≥ | $M | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | RFP §4.4 / Insurance tab | Professional Indemnity cover | $10M | §12 table, line 896 | n/a | n/a | 1.0× | Pass | Meets binding minimum. |
| N-INS-03 | insurance | Cyber Security Insurance | 10 | ≥ | $M | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | RFP §4.4 / Insurance tab | Cyber cover | $10M | §12 table, line 897 | n/a | n/a | 1.0× | Pass | Meets binding minimum. |
| N-INS-04 | insurance | Workers Compensation | per Act 2003 (Qld) | = | statute | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | RFP §4.4 | Workers Comp | Committed per Act | §12 table, line 893 | n/a | n/a | n/a | Pass | Accepted statutory term. |
| N-TERM-01 | term | Initial contract term | 3 | = | years | BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md | §4.3 | Contract initial term | 3 years | Cover page, line 89 | n/a | n/a | 1.0× | Pass | Matches RFP. |
| N-TERM-02 | term | Contract extensions | 2 | = | ×1-year | BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md | §4.3 | Extension options | Two by-one-year | Cover page, line 89 | n/a | n/a | 1.0× | Pass | Matches RFP; tied to SLA/sustainability/performance. |
| N-VALID-01 | submission | Proposal validity | 90 | ≥ | calendar days | BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md | §4.2; Annexure A §1 | Proposal validity | 90 calendar days | Cover page, line 91; §12 line 929 | n/a | n/a | 1.0× | Pass | Matches RFP. |
| N-SUB-01 | submission | Optional PDF max pages | 5 | ≤ | pages | BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md | §8 | Optional PDF | 5 pages (committed); internal draft ~10,086 words | Pre-flight, line 46 | n/a | n/a | 1.0× (target) | Pass | Submission-format limit acknowledged; internal draft is working content to be compressed. Not yet formatted. |
| N-SUB-02 | submission | Closing date/time | 2026-07-10 14:00 AEST | = | datetime | BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md | §4.2; §6.1 | Submission deadline | Draft dated 2026-07-17 (post-close); for review only | Pre-flight, line 1-4 | n/a | n/a | n/a | Ambiguous | This is an internal review draft, not the live submission. Pre-flight lists deadline confirmation as unresolved. Must be confirmed before submission. |
| N-PM-01 | pm | Lump-sum withhold until practical completion | 20 | = | % | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | PMR-09 | Practical-completion withhold | 20% accepted | §06 lines 499-501; §12 line 909 | n/a | n/a | 1.0× | Pass | Accepted contractual term; protects BAC on gap-row delivery. |
| N-PM-02 | pm | Defects liability period | 6 | = | months | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | PMR-10 | Defects liability | 6 months accepted | §05 line 434; §10 line 788 | Yes | DEV-19 | 1.0× | Pass | Accepted; maintenance agreement aligned to support tiers. |
| N-PM-03 | pm | Document review period | 5 | ≥ | business days | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | PMR-06 | Document review | Not stated | — | No | — | — | Ambiguous | PMR-06 minimum 5-business-day review period not explicitly addressed in proposal narrative. Assumed compliant via PMR-06 commitment; not evidenced. |
| N-RTO-01 | dr | Recovery Time Objective | 4 | ≤ | hours | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF07 / ISRA-16 | RTO | ≤40 minutes | §08 HA/DR table, line 644 | n/a | n/a | 6× better | Pass | Proposal commits 40 min, well within the 4-hour RFP ceiling. |
| N-RPO-01 | dr | Recovery Point Objective | recoverable | = | all data | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF06 / ISRA-16 | RPO | near-zero | §08 HA/DR table, line 645 | n/a | n/a | meets | Pass | "Near-zero" satisfies "all data recoverable". |
| N-AVL-01 | dr | Target availability | agreed service levels | = | SLA | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF04 | Availability SLA | ≥99.9% (24×7) | §08 HA/DR table, line 643 | n/a | n/a | exceeds | Pass | Proposal commits 99.9%; RFP leaves the level to agreement, so 99.9% is a stronger commitment. |
| N-AVLHIST-01 | nf | 3-year availability history | 3 | = | years | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF05 | Availability history | Not provided; committed SLA reporting going forward | §10 lines 779-780 | Yes | DEV-14 | absent | Fail | Historical 3-year history not evidenced in collateral; declared deviation. Still a Must-Have gap until supplied. Blocking. |
| N-SLA-01 | sla | Sev-1 response | 1 | ≤ | hour 24×7×365 | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF19 item 1 | Sev-1 response | ≤1 hour, 24×7×365 | §10 SLA matrix, line 744 | Yes | DEV-03 | 1.0× | Pass | Meets NF19 item 1. |
| N-SLA-02 | sla | Sev-1 resolution | 4 | ≤ | hours business day | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF19 item 2 | Sev-1 resolution | "Best-effort continuous until restored" (no time bound) | §10 SLA matrix, line 744 | No | — | unbounded | Fail | Carve-out: "best-effort" is not a time-bounded commitment. RFP requires ≤4h business day. Not declared in DEV-03 (DEV-03 only cites response times). Undeclared shortfall. Blocking. |
| N-SLA-03 | sla | Sev-2 response | 4 | ≤ | hours business day; 8 non-business | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF19 item 3 | Sev-2 response | ≤4 hrs business-day; ≤8 hrs non-business | §10 SLA matrix, line 745 | Yes | DEV-03 | 1.0× | Pass | Meets NF19 item 3. |
| N-SLA-04 | sla | Sev-2 resolution | 4 | ≤ | hours business day | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF19 item 4 | Sev-2 resolution | "Within 1 business day" (~8h) | §10 SLA matrix, line 745 | No | — | 2× slower | Fail | 1 business day ≈ 8h vs RFP 4h. Not declared in DEV-03. Undeclared shortfall. Blocking. |
| N-SLA-05 | sla | Sev-3 response | 8 | ≤ | hours business AND non-business | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF19 item 5 | Sev-3 response | "≤8 business hrs" (non-business day not stated) | §10 SLA matrix, line 746 | No | — | partial | Partial | Non-business-day Sev-3 response not committed. Not declared in DEV-03. Blocking. |
| N-SLA-06 | sla | Sev-3 resolution | 8 | ≤ | business hours | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF20 | Sev-3 resolution | Matrix says "Within 3 business days"; parenthetical says "NF20: Sev-3 resolution within 8 business hrs committed" | §10 SLA matrix, line 746 | No | — | internal contradiction | Ambiguous | Row value (3 business days) contradicts parenthetical (8 business hrs). Internal inconsistency. Not declared in DEV-03. Blocking until clarified. |
| N-SLA-07 | nf | 24/7/365 live data | 24/7/365 | = | coverage | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF03 | Live data | Asserted | §07, §08 | Yes | DEV-16 | n/a | Ambiguous | Asserted from platform; refresh cadence not stated. Assumed compliant. |
| N-SLA-08 | nf | 24/7/365 user support | 24/7/365 | = | coverage | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF17 | Support coverage | Committed via follow-the-sun (UK/India/UAE/Kuwait/Australia/Singapore) | §10 line 753 | Yes | DEV-16 | n/a | Pass | Committed; not evidenced in collateral but declared. |
| N-INC-01 | isra | Security incident notification | 1 | ≤ | hour | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | ISRA-09 / NF21 | Breach notification | 1 hour | §08 line 609; §10 line 759 | n/a | n/a | 1.0× | Pass | Meets. |
| N-EXIT-01 | isra | Exit data return | 15 | ≤ | working days | UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md | §Contractual & Exit Provisions | Exit data return | 15 working days | §08 line 669; §12 line 912 | n/a | n/a | 1.0× | Pass | Meets. |
| N-RET-01 | isra | Operational backup retention | 30 | = | days | UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md | Server hardware commitment / Backup schedule | Backup retention | 30 days operational; longer archival | §08 line 654 | n/a | n/a | 1.0× | Pass | Meets; aligned to configurable retention policy. |
| N-PEN-01 | isra | Penetration-test retest notice | 30 | = | days | UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md | Penetration Testing Alignment | Additional pen-test notice | 30 days' notice | §08 line 665 | n/a | n/a | 1.0× | Pass | Meets. |
| N-FR-01 | fr | Functional requirements total | 73 | = | count | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Tab.F FR | FR coverage | 73 addressed (74 grounded+assertable+gap across FR set) | §11 lines 808-826 | n/a | n/a | n/a | Partial | All 73 rows addressed in narrative; 11 are gaps (10 Must-Have + 1 Should-Have). 5 disqualifying (FR17/FR20). |
| N-FR-MH-01 | fr | Must-Have functional requirements | 69 | = | count | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Tab.F FR MoSCoW | Must-Have FR coverage | 69 addressed; 10 Must-Have gaps (FR07, FR10, FR17, FR20, FR21, FR23, FR26, FR27, FR69, FR72) | §11 lines 814-826 | Yes | DEV-01..DEV-13 | 59/69 = 85.5% | Partial | 10 of 69 Must-Have FRs are gaps with committed delivery. 2 disqualifying (FR17, FR20). |
| N-NF-01 | nf | Non-functional requirements total | 48 | = | count | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Tab.F NF | NF coverage | 48 addressed; 10 gaps | §11 lines 830-845 | Yes | DEV-14..DEV-18 | 38/48 = 79% | Partial | 10 of 48 NFs are gaps; all Must-Have. NF19 disqualifying. |
| N-PMR-01 | pm | PM requirements total | 20 | = | count | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Tab.F PMR | PMR coverage | 20 addressed; 1 gap (PMR-10) | §11 lines 848-855 | Yes | DEV-19 | 19/20 = 95% | Partial | PMR-10 (defects liability + maintenance) is a "Should Have" sub-row; main PMR-10 Must-Have accepted. |
| N-ISRA-01 | isra | ISRA rows total | 29 | = | count | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Tab.F ISRA | ISRA coverage | 29 addressed; 3 gaps (ISRA-19, ISRA-25, ISRA-27) | §11 lines 858-867 | Yes | DEV-04, DEV-05, DEV-22 | 26/29 = 89.7% | Partial | 2 disqualifying (ISRA-19, ISRA-25). |
| N-REF-01 | submission | Referees required | 2 | = | count | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Relevant Experience §2 | Referees supplied | 0 (placeholder) | §14 lines 1042-1046 | n/a | n/a | 0/2 | Fail | Not supplied; committed before submission. Blocking. |
| N-REF-02 | submission | 5-year pricing breakdown | 5 | = | years | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Pricing Schedule E | Pricing supplied | 0 (placeholder) | §12 lines 903-905 | n/a | n/a | 0/5 | Fail | Not supplied; committed in Schedule E before submission. Blocking. |
| N-REF-03 | submission | Key personnel/resumes | named | = | set | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Schedule C | Personnel supplied | 0 (placeholder) | §14 lines 1030-1031, 1043 | n/a | n/a | absent | Fail | Not supplied; committed before submission. Blocking. |
| N-REF-04 | submission | ISO/insurance certificates | current | = | set | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | Schedule A | Certificates supplied | 0 (placeholder) | Pre-flight line 32; §14 line 1044 | n/a | n/a | absent | Fail | Not supplied; committed before submission. Blocking. |
| N-REF-05 | submission | QA standards/tools documentation | supplied | = | set | BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md | NF09/NF10 | QA docs supplied | 0 (not in collateral) | §09 line 685; §11 line 837 | Yes | DEV-15 | absent | Fail | Not supplied; committed from WAISL internal QA docs. Blocking. |

## Summary

- **Total numeric requirements checked:** 38
- **Pass:** 18
- **Partial:** 9
- **Fail:** 8
- **Ambiguous:** 3
- **Blocking (subset of Fail/Partial that are Must-Have and not met):** 11

### Numeric parity summary

| Domain | Binding | Proposal | Delta | Verdict |
|---|---|---|---|---|
| Public Liability | $20M | $20M | 1.0× | Pass |
| Professional Indemnity | $10M | $10M | 1.0× | Pass |
| Cyber Insurance | $10M | $10M | 1.0× | Pass |
| RTO | ≤4h | ≤40min | 6× better | Pass |
| RPO | recoverable | near-zero | meets | Pass |
| Availability | agreed | ≥99.9% | exceeds | Pass |
| Sev-1 response | ≤1h 24×7×365 | ≤1h 24×7×365 | 1.0× | Pass |
| Sev-1 resolution | ≤4h business day | best-effort (unbounded) | carve-out | **Fail** |
| Sev-2 response | ≤4h bus / ≤8h non-bus | ≤4h bus / ≤8h non-bus | 1.0× | Pass |
| Sev-2 resolution | ≤4h business day | ~1 business day (~8h) | 2× slower | **Fail** |
| Sev-3 response | ≤8h bus AND non-bus | ≤8h business (non-bus missing) | partial | **Partial** |
| Sev-3 resolution (NF20) | ≤8h business | 3 business days vs 8h (contradiction) | ambiguous | **Ambiguous** |
| 3-yr availability history | 3 years | absent | absent | **Fail** |
| 20% withhold | 20% | 20% | 1.0× | Pass |
| 6-mo defects liability | 6 months | 6 months | 1.0× | Pass |
| Proposal validity | 90 days | 90 days | 1.0× | Pass |
| Initial term | 3 years | 3 years | 1.0× | Pass |
| Extensions | 2×1-year | 2×1-year | 1.0× | Pass |
| Incident notification | ≤1h | ≤1h | 1.0× | Pass |
| Exit data return | ≤15 working days | 15 working days | 1.0× | Pass |

### Key numeric gaps

1. **N-SLA-02 (Sev-1 resolution):** RFP requires ≤4h business day; proposal offers "best-effort continuous until restored" — an unbounded carve-out, not a time-bounded commitment. Not declared in DEV-03. **Blocking.**
2. **N-SLA-04 (Sev-2 resolution):** RFP requires ≤4h business day; proposal offers "within 1 business day" (~8h) — 2× slower. Not declared in DEV-03. **Blocking.**
3. **N-SLA-05 (Sev-3 response non-business):** RFP requires ≤8h on both business and non-business days; proposal commits only business-day ≤8h. Not declared. **Blocking.**
4. **N-SLA-06 (Sev-3 resolution / NF20):** Internal contradiction — matrix row says "3 business days", parenthetical says "8 business hrs committed". Not declared. **Blocking until clarified.**
5. **N-AVLHIST-01 (3-year availability history):** Not provided. Declared (DEV-14) but still a Must-Have gap. **Blocking.**
6. **N-REF-01..05 (submission components):** Referees, pricing, personnel, certificates, QA docs all absent. **Blocking.**