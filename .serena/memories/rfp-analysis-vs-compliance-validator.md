# rfp-analysis-and-response vs. enhanced compliance-validator

These two skills are complementary, not redundant. Use them in sequence, with distinct roles in the proposal pipeline.

## What `rfp-analysis-and-response` does (upstream)

- **Scope:** broad buyer-document analysis and response drafting.
- **Primary outputs:** RFP snapshot, scope/deliverables table, response-format rules, commercial/legal terms review, high-level compliance and traceability review, risks/gaps/clarifications, recommended response structure, optional aviation overlay and evidence mapping.
- **Modes:** generic analysis, aviation overlay, evidence mapping, proposal drafting.
- **Best used early:** when the RFP arrives, to understand it and outline/draft the response.

## What enhanced `compliance-validator` does (downstream)

- **Scope:** final quality gate on a drafted proposal or traceability artefact.
- **Primary outputs:** `compliance-report.md` + `compliance-report-numeric-inventory.md`.
- **Distinctive checks:**
  - numeric/quantitative requirements inventory,
  - parity / delta evaluation (proposal value vs binding value),
  - deviation-register completeness audit,
  - semantic carve-out and over-claim detection,
  - multi-artefact reconciliation (e.g., proposal vs RTM),
  - adversarial critic pass,
  - blocking-issue surfacing.
- **Best used late:** after drafting and empathy review, before `proposal-assembler`.

## Overlap

Both skills:
- extract requirements from buyer documents (RFP/BRD/ABR/CR);
- identify gaps, risks, and missing bidder inputs;
- care about response format and submission mechanics;
- produce structured reports;
- flag items that need legal/security/delivery/finance review.

## Differentiation

| Dimension | `rfp-analysis-and-response` | enhanced `compliance-validator` |
|---|---|---|
| **Timing** | Upfront analysis / drafting | Final pre-assembly validation |
| **Orientation** | Bid strategy and response structure | Compliance / parity verification |
| **Numeric parity** | Mentions measurable requirements; does not systematically compare values | First-class numeric inventory + ratio/delta |
| **Deviation register** | Notes deviations and clarifications | Audits every shortfall against a deviation register; flags undeclared deviations |
| **Carve-out detection** | General risk framing | Explicit downgrade of "Compliant" rows with weakening phrases |
| **Multi-artefact reconciliation** | Evidence mapping across collateral | Three-way reconciliation of BRD ↔ proposal ↔ RTM/cross-check artefact |
| **Blocking gate** | Identifies risks | Declares "NOT READY for assembly" and stops the assembler |

## Best-practice workflow

1. **`rfp-analysis-and-response`** — understand the RFP, extract requirements, build the response outline.
2. **`requirements-mapper`** + **`section-drafter`** — map requirements to sections and draft content.
3. **`empathy-reviewer`** — tone/alignment review.
4. **Enhanced `compliance-validator`** — run numeric parity, deviation-register audit, carve-out detection, and multi-artefact reconciliation. Fix blocking issues.
5. **`proposal-assembler`** — only runs if `compliance-report.md` has no blocking issues.

## Airport Eye learning

The original `compliance-validator` checked presence, not parity. The Airport Eye case showed that a proposal can "address" every topic and still be non-compliant because:
- stated values are weaker than the binding BRD (RMSE, DTM/DSM, orthophoto GSD),
- deviations are declared for some shortfalls but not others,
- "Compliant" status words contain parenthetical carve-outs,
- the proposal diverges from its own RTM.

`rfp-analysis-and-response` would likely surface these as risks or clarifications, but it does not run the rigorous numeric/deviation/carve-out/reconciliation pass that the enhanced `compliance-validator` now performs. Both skills are needed.

## Anti-pattern to avoid

Do not treat `rfp-analysis-and-response` as the final compliance gate. Its compliance review is high-level and strategic. Always run the enhanced `compliance-validator` before assembly, especially when the RFP/BRD contains measurable thresholds (SLAs, accuracy, counts, coverage percentages, retention periods, insurance values).

**Related memories:** [[compliance-validator-enhancement]], [[airport-eye-procurement-context]]
