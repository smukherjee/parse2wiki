# Numeric / Quantitative Requirements Inventory Template

Use this template to record every comparable numeric requirement extracted from the authoritative requirements documents (CR/BRD/ABR/Addendum/RFP, in hierarchy order). This inventory is the input to the parity / delta evaluation step.

The template is **domain-agnostic**. All field values — including `applies_to` and `domain_hint` — are free-form and must be derived from the engagement's source documents. Do not impose a fixed taxonomy of subsystems, layers, or quality attributes. The example rows below use generic placeholders (`Subsystem A`, etc.) rather than any case-study-specific subsystem names. Replace the placeholders with values that match the engagement being validated.

## Column definitions

| Column | Description |
|---|---|
| `requirement_id` | Unique ID for this numeric requirement. Use the buyer's ID verbatim when present (e.g., `FR17`, `NF38`); otherwise generate a stable ID (e.g., `N-001`). |
| `domain_hint` | Free-form grouping label that helps the reviewer cluster findings. Examples: `survey`, `ai`, `sla`, `security`, `platform`, `integration`, `commercial`, `legal`, `operations`. Any label is acceptable as long as it groups related requirements. |
| `parameter` | Human-readable name of the parameter. |
| `binding_value` | The strictest value from the authoritative source documents. |
| `operator` | The comparison operator: `≤`, `≥`, `<`, `>`, `=`, `minimum`, `maximum`. |
| `unit` | Unit of measurement: cm, s, min, h, d, %, count, years, etc. |
| `source_document` | Exact filename of the source document, including any typos in the repository name. |
| `source_location` | Section, page, and/or line number in the markdown extraction. |
| `applies_to` | Free-form text naming the subsystem, module, layer, surface, role, deliverable, or any other entity the value applies to. Do not limit to a fixed taxonomy. |
| `modal_verb` | `shall`, `must`, `should`, `may`, `will`, or `none`. Drives verdict logic. |
| `scope_tier` | `base`, `optional`, `phase_2`, `out_of_scope_by_source`, or `reserved_for_human`. |
| `proposal_value` | The corresponding value or status found in the proposal / target artefact. |
| `target_location` | Line / section in the target artefact where the value was found. |
| `covered_by` | `commitment`, `capability_claim`, `not_addressed`, or `out_of_scope`. |
| `declared_in_deviation_register` | `Yes` / `No` / `n/a`. |
| `deviation_register_id` | If yes, the ID of the deviation / exemption / assumption entry. |
| `ratio_or_delta` | Optional: how the proposal value compares to the binding value (e.g., "6.7× worse", "2× coarser"). |
| `verdict` | `Pass` / `Partial` / `Fail` / `Ambiguous` / `N/A`. |
| `notes` | Rationale, severity, remediation pointer, or carve-out wording. |

## Example rows (generic placeholders)

The rows below are **placeholder examples**. They are intentionally generic; replace the `Subsystem A`, `Service B`, etc. labels with values that match the engagement's source documents. The `domain_hint` values are also examples — any free-form label is acceptable.

| requirement_id | domain_hint | parameter | binding_value | operator | unit | source_document | source_location | applies_to | modal_verb | scope_tier | proposal_value | target_location | covered_by | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-001 | survey | Subsystem A point density (boundary) | 20 | ≥ | count / unit area | <source-document-filename>.md | §X.X, line NN | Subsystem A | shall | base | ≥20 count / unit area | Proposal DRAFT line NN | commitment | n/a | n/a | 1.0× | Pass | Matches source. |
| N-002 | survey | Subsystem A vertical accuracy | 3 | ≤ | cm | <source-document-filename>.md | §X.X, line NN | Subsystem A | shall | base | ≤20 cm | Proposal DRAFT line NN | commitment | Yes | Deviation 1 | 6.7× worse | Partial | Declared deviation; needs buyer acceptance. |
| N-003 | survey | Subsystem A grid resolution | 10 | = | cm | <source-document-filename>.md | §X.X, line NN | Subsystem A | shall | base | 50 cm | Proposal DRAFT line NN | not_addressed | No | — | 5× coarser | Fail | Undeclared shortfall. |
| N-004 | ai | Service B agent count (mandatory) | 8 | = | count | <source-document-filename>.md | §X.X, lines NN–NN | Service B agent estate | shall | base | 3 itemised | Proposal DRAFT lines NN–NN | commitment | n/a | n/a | 37.5% | Fail | Five mandatory agents missing from proposal technical narrative. |
| N-005 | ai | Service C alert latency | 5 | ≤ | s | <source-document-filename>.md | §X.X, line NN | Service C | shall | base | not stated | — | not_addressed | n/a | n/a | — | Fail | Service C not itemised; no SLA target offered. |
| N-006 | sla | Critical incident response time | 10 | ≤ | min | <source-document-filename>.md | §X.X, line NN | Incident response | shall | base | ≤30 min | Proposal DRAFT line NN | commitment | Yes | Deviation 2 | 3× slower | Partial | Declared deviation; needs buyer acceptance. |
| N-007 | sla | Data latency | 5 | ≤ | s | <source-document-filename>.md | §X.X, line NN | Data pipeline | shall | base | ≤5 s "measured at platform boundary" | Proposal DRAFT line NN | commitment | No | — | scope narrowed | Partial | Carve-out: source-side latency excluded. |

## Guidance for extraction

1. **Hierarchy matters.** If CR/ABR contradicts the RFP/BRD, use the stricter or more recent value and document both.
2. **Capture implicit thresholds.** Phrases like "minimum 5 years", "at least 99.5%", "no more than 10 minutes" should all become rows.
3. **Capture counts even when not numeric.** "All eight agents", "every BMS point", "the full 40-pump IoT set" are countable requirements.
4. **Capture layer / catalogue / surface requirements.** Enumerated lists of systems, layers, catalogues, basemaps, etc., are comparable coverage requirements.
5. **Do not over-normalise.** Keep each distinct parameter as its own row so the parity check can report exactly where the proposal diverges.
6. **Free-form fields are free-form.** `applies_to` and `domain_hint` must be derived from the source. Do not invent or impose a fixed taxonomy.
7. **Modal verbs and scope tiers drive verdict logic.** A `should` requirement missing from the proposal is a scored deduction, not a blocking failure. A `shall` requirement addressed only by capability claim is `Partial`, not `Pass`. A `phase_2` requirement missing from the proposal is `out_of_scope`, not `Fail`.
