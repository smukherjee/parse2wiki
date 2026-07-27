# Functional and Non-Functional Requirements Inventory Template

Use this template to record every functional requirement (FR) and non-functional requirement (NFR) extracted from the authoritative requirements documents (CR/BRD/ABR/Addendum/RFP, in hierarchy order). This inventory is the input to the FR/NFR coverage check (Step 6 of the skill) and the per-FR/NFR verdict (Step 3).

The template is **domain-agnostic**. All field values — including `category`, `domain_hint`, `applies_to`, and the requirement text — are free-form and must be derived from the engagement's source documents. Do not impose a fixed taxonomy. The example rows below use generic placeholders so the template can be reused for any procurement.

## When to use this template

Use this template whenever the source documents enumerate explicit functional or non-functional requirements. Common shapes:

- The RFP / BRD has a numbered "Functional Requirements" section (e.g., `FR01`, `FR02`, …).
- The RFP / BRD has a numbered "Non-Functional Requirements" section (e.g., `NF01`, `NF02`, …).
- The buyer has supplied a response sheet / compliance matrix that lists the FRs and NFRs by ID.
- The RFP / BRD uses `shall` statements scattered through the scope description; in this case, generate stable IDs (`F-NN`, `NF-NN`) and capture each one.

If a buyer's response sheet is supplied, extract from it first. It is the most direct and complete source.

## Column definitions

| Column | Description |
|---|---|
| `requirement_id` | Unique ID. Use the buyer's ID verbatim when present (e.g., `FR17`, `NF38`); otherwise generate a stable ID (`F-NN`, `NF-NN`). |
| `requirement_text` | Verbatim or close-paraphrase of the requirement from the source. |
| `category` | For FR: `functional`. For NFR: a free-form sub-category such as `performance`, `security`, `usability`, `availability`, `reliability`, `maintainability`, `scalability`, `compliance`, `auditability`, `interoperability`, `data_integrity`, `accessibility`, `latency`, `throughput`, or any other attribute the source uses. No fixed taxonomy. |
| `domain_hint` | Free-form grouping label that helps the reviewer cluster findings. Any label is acceptable. |
| `applies_to` | Free-form text naming the subsystem, module, layer, surface, role, or deliverable the requirement attaches to. No fixed taxonomy. |
| `modal_verb` | `shall`, `must`, `should`, `may`, `will`, or `none`. Drives verdict logic. |
| `mandatory_or_scored` | `M` for mandatory / pass-fail, `S` for scored (with weight recorded in `score_weight`), `I` for informational. |
| `score_weight` | If `mandatory_or_scored = S`, the numeric weight (points or %). If not scored, leave blank or write `n/a`. |
| `scope_tier` | `base`, `optional`, `phase_2`, `out_of_scope_by_source`, or `reserved_for_human`. |
| `source_document` | Exact filename of the source document, including any repository typos. |
| `source_location` | Section, page, and/or line number in the markdown extraction. |
| `proposal_section` | Which section of the proposal addresses this requirement. Filled in during Step 3. |
| `proposal_value` | The value, commitment, or claim the proposal offers. Filled in during Step 3. |
| `covered_by` | `commitment`, `capability_claim`, `not_addressed`, or `out_of_scope`. Filled in during Step 3. |
| `verdict` | `Pass` / `Partial` / `Fail` / `Ambiguous` / `N/A`. Filled in during Step 3. |
| `declared_in_deviation_register` | `Yes` / `No` / `n/a`. |
| `deviation_register_id` | If yes, the ID of the deviation / exemption / assumption entry. |
| `notes` | Rationale, carve-out wording, severity, remediation pointer, scope-drift flag. |

## Verdict logic (from skill Step 3)

- `shall` / `must` / `will` (binding) → **binding**. A `Fail` is a blocking finding.
- `should` → **scored**. A `Fail` is a deduction-grade finding (severity depends on `score_weight`).
- `may` → **optional**. Addressed well, it earns points; not addressed, no points lost.
- `none` → **ambiguous**. Treat as binding unless context overrides; record the assumption in `notes`.

`covered_by`:

- `commitment` — the proposal makes a binding, measurable commitment. Strongest form of coverage.
- `capability_claim` — the proposal asserts it can do X but does not commit. Weaker than a commitment.
- `not_addressed` — the proposal does not mention the requirement. Combined with `scope_tier = base`, this is a `Fail`.
- `out_of_scope` — the requirement is `optional`, `phase_2`, `out_of_scope_by_source`, or `reserved_for_human`.

## Example rows (generic placeholders)

The rows below are **placeholder examples**. They are intentionally generic; replace `FR-EXAMPLE-01`, `NF-EXAMPLE-01`, and the `Subsystem A` / `Service B` labels with values that match the engagement's source documents. The `category`, `domain_hint`, and `applies_to` values are also examples — any free-form label is acceptable.

### Functional requirements

| requirement_id | requirement_text | category | domain_hint | applies_to | modal_verb | mandatory_or_scored | score_weight | scope_tier | source_document | source_location | proposal_section | proposal_value | covered_by | verdict | declared_in_deviation_register | deviation_register_id | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR-EXAMPLE-01 | The system shall detect and classify Service A types within the monitored area. | functional | detection | Service A | shall | M | n/a | base | <source-document-filename>.md | §X.X, line NN | §3.1 | "Detects 8 Service A types with ≥95% precision / ≥90% recall." | commitment | Pass | n/a | n/a | FR matches proposal; figures meet source. |
| FR-EXAMPLE-02 | The system shall record arrival and departure timestamps for each Service A instance per source. | functional | detection | Service A | shall | M | n/a | base | <source-document-filename>.md | §X.X, line NN | §3.1 | "Logs arrival / departure at the source boundary." | commitment | Pass | n/a | n/a | FR matches; source boundary wording is acceptable because source uses inclusive language. |
| FR-EXAMPLE-03 | The system shall track Service A presence on the stand area. | functional | detection | Service A | shall | M | n/a | base | <source-document-filename>.md | §X.X, line NN | (none) | — | not_addressed | Fail | No | — | **Blocking.** FR not addressed. |
| FR-EXAMPLE-04 | The system should provide a public-facing dashboard. | functional | ux | Dashboard | should | S | 5 | base | <source-document-filename>.md | §X.X, line NN | §5 | "Dashboard available to all stakeholders." | capability_claim | Partial | No | — | Capability claim, not commitment; deduct up to 5 points. |
| FR-EXAMPLE-05 | The system may integrate with Service C. | functional | integration | Service C | may | I | n/a | optional | <source-document-filename>.md | §X.X, line NN | (none) | — | out_of_scope | N/A | n/a | n/a | Optional; absence is not a failure. |
| FR-EXAMPLE-06 | The system shall support Service D activation via upgrade. | functional | integration | Service D | shall | M | n/a | base | <source-document-filename>.md | §X.X, line NN | §3.2 | "Service D support is planned for a future release." | capability_claim | Partial | No | — | **Carve-out:** "via upgrade" weakens a `shall` requirement. Downgrade to Partial; flag as undeclared deviation. |

### Non-functional requirements

| requirement_id | requirement_text | category | domain_hint | applies_to | modal_verb | mandatory_or_scored | score_weight | scope_tier | source_document | source_location | proposal_section | proposal_value | covered_by | verdict | declared_in_deviation_register | deviation_register_id | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NF-EXAMPLE-01 | Detection latency shall not exceed 5 seconds end-to-end. | performance | latency | Service A pipeline | shall | M | n/a | base | <source-document-filename>.md | §X.X, line NN | §3.1 | "≤5 s end-to-end, measured at the platform boundary." | commitment | Partial | No | — | **Carve-out:** "measured at the platform boundary" excludes source-side latency. Downgrade to Partial; flag as undeclared deviation. |
| NF-EXAMPLE-02 | The system shall be available 99.5% of the time, excluding scheduled maintenance. | availability | availability | Platform | shall | M | n/a | base | <source-document-filename>.md | §X.X, line NN | §6 | "99.5% availability." | commitment | Pass | n/a | n/a | NFR met. |
| NF-EXAMPLE-03 | The system should support concurrent users. | scalability | scalability | Platform | should | S | 3 | base | <source-document-filename>.md | §X.X, line NN | (none) | — | not_addressed | Fail | No | — | NFR not addressed; deduct up to 3 points. |
| NF-EXAMPLE-04 | The system shall comply with [standard / framework] [version]. | compliance | security | Platform | shall | M | n/a | base | <source-document-filename>.md | §X.X, line NN | §7 | "Compliant with [version]." | commitment | Pass | n/a | n/a | Version match verified. |
| NF-EXAMPLE-05 | The system should be operable by users with no technical background. | usability | ux | UI | should | S | 4 | base | <source-document-filename>.md | §X.X, line NN | §5 | "Designed for non-technical operators." | capability_claim | Partial | No | — | Capability claim; deduct up to 4 points. |

## Guidance for extraction

1. **Buyer response sheet first.** If supplied, it is the most direct and complete source. Extract every row.
2. **Hierarchy matters.** If CR/ABR contradicts the RFP/BRD, use the stricter or more recent value and document both.
3. **Capture implicit `shall` statements.** Even when an RFP does not label a paragraph as "FR-XX", any `shall` statement of a binding capability is a functional requirement and should be captured.
4. **NFR sub-categories are free-form.** Performance, security, usability, availability, reliability, maintainability, scalability, compliance, auditability, interoperability, data integrity, accessibility, latency, throughput are common — but the source may use any label. Use what the source uses.
5. **Modal verbs drive severity.** A `should` requirement that is missing is a scored deduction, not a blocking failure. A `shall` requirement that is missing is blocking.
6. **Scope tier separates ghost requirements from real ones.** A `phase_2` requirement missing from the proposal is not a failure. A `base` requirement missing is a failure.
7. **Covered-by is not optional.** Every FR/NFR must end up with one of `commitment`, `capability_claim`, `not_addressed`, or `out_of_scope`. Without this, the coverage summary cannot be produced.
8. **Do not over-normalise.** Keep each distinct requirement as its own row so the coverage check can report exactly where the proposal diverges.
