# Numeric / Quantitative Requirements Inventory — Track A

**Proposal under validation:** `eval/bac/trackA/proposal-trackA.md`
**Authoritative RFP:** `sources/BAC/BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md`
**Response sheet (required-response structure):** `sources/BAC/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md`
**Cross-check collateral (non-binding):** `sources/BAC/Turnwise Product Document 1.pdf.md` and `sources/BAC/UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v1.docx.md`

**Binding hierarchy:** RFP (incl. Annexure A) and Response Sheet Tab F govern. The UTAM Solution Architecture document is product collateral prepared for a prior European airport deployment; its AIA/Athens, EU data-residency, GDPR, NIS2, Hellenic DPA, Eurocontrol NM Message Service, and 40-minute RTO references are non-binding and are reconciled to the Brisbane / Australian regulatory context in the proposal (Section 4.9 and deviation D01/D11). Where the UTAM document quotes a value, it is recorded here with `source_document = UTAM...` and verdict `N/A` (non-binding design target) unless the RFP/Response Sheet also states the value.

## Numeric requirements inventory

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-GEN-01 | submission | Proposal validity period | 90 | = | calendar days | BAC-...RFP.pdf.md | Annexure A clause 1; §4.2 | Proposal validity | 90 calendar days from closing | proposal §1 line 7; §13.2 | n/a | n/a | 1.0x | Pass | Matches RFP. |
| N-GEN-02 | term | Initial contract term | 3 | = | years | BAC-...RFP.pdf.md | §4.3 | Contract term | 3 years | proposal §13.2 | n/a | n/a | 1.0x | Pass | Matches RFP. |
| N-GEN-03 | term | Contract extensions | 2 | = | one-year extensions | BAC-...RFP.pdf.md | §4.3 | Extensions | Two one-year extensions | proposal §13.2 | n/a | n/a | 1.0x | Pass | Matches RFP. |
| N-GEN-04 | insurance | Public Liability cover | 20 | minimum | $ million | BAC-...RFP.pdf.md | §4.4 | Insurance | Minimum $20 million | proposal §13.1 | n/a | n/a | 1.0x | Pass | Matches RFP. |
| N-GEN-05 | insurance | Professional Indemnity cover | 10 | = | $ million | BAC-...RFP.pdf.md | §4.4 | Insurance | $10 million | proposal §13.1 | n/a | n/a | 1.0x | Pass | Matches RFP. |
| N-GEN-06 | insurance | Cyber Security Insurance | 10 | = | $ million | BAC-...RFP.pdf.md | §4.4 | Insurance | $10 million | proposal §13.1 | n/a | n/a | 1.0x | Pass | Matches RFP. |
| N-GEN-07 | submission | Optional supporting PDF length | 5 | ≤ | pages | BAC-...RFP.pdf.md | §8 | Supporting document | Claims "within the five-page optional PDF allowance, extended here as a structured proposal"; document body is ~515 lines / clearly >5 pages | proposal §1 line 24; §16 last para | No | — | exceeds limit | Partial | Over-claim: asserts compliance with the 5-page cap while the body exceeds it. Not in deviation register. Remediate by trimming the PDF to ≤5 pages or relying solely on the Response Sheet. |
| N-FR-01 | functional | Functional requirements addressed | 73 | = | count | BAC- Supplier Response Sheet...xlsx.md | Functional Requirements tab | FR coverage | All 73 FR (FR01-FR73) | proposal §12.1 | n/a | n/a | 1.0x | Pass | Category-level conformance "Yes"; per-requirement wording TBC from bidder input. |
| N-FR-02 | functional | Must-Have functional requirements | 69 | = | count | BAC- Supplier Response Sheet...xlsx.md | Functional Requirements tab; Sheet1 note "73 FRQ, 69 must have" | Must Have FR | 69 Must Have | proposal §12.1 | n/a | n/a | 1.0x | Pass | Matches RFP. |
| N-NF-01 | nonfunctional | Non-functional requirements addressed | 48 | = | count | BAC- Supplier Response Sheet...xlsx.md | NF Requirements tab | NF coverage | All 48 NF (NF01-NF48), all Must Have | proposal §12.2 | n/a | n/a | 1.0x | Pass | Category-level "Yes"; per-requirement TBC. |
| N-ISRA-01 | security | ISRA questions answered | 29 | = | count | BAC- Supplier Response Sheet...xlsx.md | ISRA tab (ID 1-29; ID 30 = Spare) | ISRA response | All 29 questions addressed in §9.2 table | proposal §9.2 | n/a | n/a | 1.0x | Pass | Summary responses present; evidence TBC (see C-SUBS-01). |
| N-PM-01 | pm | Document review period | 5 | minimum | business days | BAC- Supplier Response Sheet...xlsx.md | PMR-06 | Document review | Minimum five business days per document | proposal §7 | n/a | n/a | 1.0x | Pass | Matches PMR-06. |
| N-PM-02 | pm | Lump sum withheld to practical completion | 20 | = | % | BAC- Supplier Response Sheet...xlsx.md | PMR-09 | Payment | Twenty percent withheld until practical completion | proposal §10; §13.2 | n/a | n/a | 1.0x | Pass | Matches PMR-09. |
| N-PM-03 | pm | Defects liability period | 6 | = | months | BAC- Supplier Response Sheet...xlsx.md | PMR-10 | Defects | Six-month defects liability period | proposal §10; §5 | n/a | n/a | 1.0x | Pass | Matches PMR-10. |
| N-REF-01 | experience | Referees supplied | 2 | minimum | count | BAC- Supplier Response Sheet...xlsx.md | Relevant Experience §2 | Referees | "At least two referees" — placeholder, TBC from bidder input | proposal §15; D15 | Yes | D15 | not yet provided | Partial | Declared placeholder. Blocking if unresolved at submission. |
| N-SLA-01 | sla | Severity 1 response time | 1 | ≤ | hour | BAC- Supplier Response Sheet...xlsx.md | NF19 item 1 (24x7x365) | Incident response | Within 1 hour, 24x7x365 | proposal §11 | n/a | n/a | 1.0x | Pass | Matches NF19. |
| N-SLA-02 | sla | Severity 1 resolution / plan | 4 | ≤ | hours | BAC- Supplier Response Sheet...xlsx.md | NF19 item 2 (business day AU) | Incident resolution | Within 4 hours on a business day | proposal §11 | n/a | n/a | 1.0x | Pass | Matches NF19. |
| N-SLA-03 | sla | Severity 2 response (business day) | 4 | ≤ | hours | BAC- Supplier Response Sheet...xlsx.md | NF19 item 3 | Incident response | Within 4 hours on a business day | proposal §11 | n/a | n/a | 1.0x | Pass | Matches NF19. |
| N-SLA-04 | sla | Severity 2 response (non-business day) | 8 | ≤ | hours | BAC- Supplier Response Sheet...xlsx.md | NF19 item 3 (relative to AEDT) | Incident response | Within 8 hours on a non-business day | proposal §11 | n/a | n/a | 1.0x | Pass | Matches NF19. |
| N-SLA-05 | sla | Severity 2 resolution / plan | 4 | ≤ | hours | BAC- Supplier Response Sheet...xlsx.md | NF19 item 4 (business day) | Incident resolution | Within 4 hours on a business day | proposal §11 | n/a | n/a | 1.0x | Pass | Matches NF19. |
| N-SLA-06 | sla | Severity 3 response | 8 | ≤ | hours | BAC- Supplier Response Sheet...xlsx.md | NF19 item 5 / NF20 | Incident response | Within 8 hours (business and non-business day) | proposal §11 | n/a | n/a | 1.0x | Pass | Matches NF19/NF20. |
| N-SLA-07 | sla | Severity 3 resolution / plan | 8 | ≤ | hours | BAC- Supplier Response Sheet...xlsx.md | NF20 (business day) | Incident resolution | Within 8 hours on a business day | proposal §11 | n/a | n/a | 1.0x | Pass | Matches NF20. |
| N-DR-01 | dr | Recovery Time Objective | 4 | ≤ | hours | BAC- Supplier Response Sheet...xlsx.md | NF07 | Disaster recovery | 4 hours (binding commitment); 40 min stated as internal design objective only | proposal §11 HA/DR table; D11 | Yes | D11 | 1.0x (binding met) | Pass | UTAM collateral quotes 40 min (non-binding); proposal correctly commits to 4-hour binding RTO per NF07. Declared in D11. |
| N-DR-02 | dr | Recovery Point Objective | all data recoverable | = | — | BAC- Supplier Response Sheet...xlsx.md | NF06 | Disaster recovery | "Near zero" RPO | proposal §11 HA/DR table | n/a | n/a | meets | Pass | "Near zero" satisfies "all data recoverable." |
| N-DR-03 | availability | 3-year availability history | 3 | = | years | BAC- Supplier Response Sheet...xlsx.md | NF05 | Availability history | Figures TBC from bidder input; will provide available history and explain gaps | proposal §11 note; D10 | Yes | D10 | not yet provided | Partial | Declared in D10. Blocking if unresolved. |
| N-AVAIL-01 | availability | Target availability | 99.9 | ≥ | % | UTAM_Solution_Architecture...docx.md | §7.1 HA/DR table (non-binding) | Availability (design target) | ≥99.9% (24x7) | proposal §11 HA/DR table | n/a | n/a | 1.0x | N/A | Non-binding UTAM design target, not an RFP threshold. Proposed by WAISL; not a binding parity item. |

## Parity summary

- **Total binding numeric rows:** 25 (N-GEN-01 through N-DR-03)
- **Pass:** 21
- **Partial:** 3 (N-GEN-07 supporting-PDF page over-claim; N-REF-01 referees placeholder; N-DR-03 availability-history figures TBC)
- **Fail:** 0
- **Ambiguous:** 0
- **N/A (non-binding collateral):** 1 (N-AVAIL-01; 99.9% availability is a UTAM design target, not an RFP threshold)

## Adversarial critic pass notes

1. **N-DR-01 (RTO):** The UTAM document states `<= 40 mins`; the RFP/Response Sheet binds at 4 hours. The 40-minute figure is *better* than binding, so there is no shortfall. The proposal correctly commits to the 4-hour binding value and offers 40 minutes as an internal design objective (declared in D11). No undeclared deviation.
2. **N-GEN-07 (5-page PDF):** This is the one numeric shortfall that is *not* declared in the deviation register. The proposal asserts it is "within the five-page optional PDF allowance" while the document body is clearly longer. This is an over-claim / undeclared deviation and is carried forward as a blocking item in the main report.
3. **N-DR-03 (availability history):** Declared in D10. No undeclared shortfall, but the substantive value is absent and would block a compliant final submission if not resolved.
4. **No other binding numeric specs were treated as Pass while actually weaker** in the target. Severity model, RTO, RPO, insurance, term, validity, FR/NF/ISRA counts, review period, withhold %, and defects liability all match the RFP/Response Sheet values exactly.