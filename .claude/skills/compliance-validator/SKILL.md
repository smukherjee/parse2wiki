---
name: compliance-validator
description: >
  Validates every reviewed section and the consolidated proposal against the
  RFP/BRD/ABR/CR's explicit requirements. Produces a pass/fail compliance report
  with numeric parity checks, deviation-register completeness, semantic carve-out
  detection, multi-artefact reconciliation, functional and non-functional
  requirement coverage, modal-verb and scope-tier classification, and remediation
  notes. Runs after the empathy reviewer because tone fixes can inadvertently
  remove compliance-critical language.
  Trigger when the user says "check compliance," "validate the sections," "are we
  compliant," "run the compliance check," or after the empathy reviewer has produced
  sections/*-reviewed.md files.
---

## Inputs

- **`sections/[section-name]-reviewed.md`** — reviewed sections from the empathy-reviewer
- **RFP/BRD/ABR/CR document(s)** — the authoritative requirements sources, in hierarchy order
- *(Optional)* **`buyer-response-sheet.md`** — the buyer's own compliance matrix / response sheet, when one is supplied. This is the most direct and complete source of FRs/NFRs because the buyer has already enumerated them.
- *(Optional)* **`stakeholder-deltas.md`** — post-issuance meeting minutes, review actions, clarification logs, or addenda communicated outside the formal document trail (e.g., by email). When supplied, ranks above the base RFP/BRD in the binding hierarchy (most-recent-buyer-communication wins) but below any formal CR/ABR that supersedes it. Purely additive: absence does not change any other step's behavior.
- *(Optional)* **`proposal-artefact.md`** — the consolidated proposal or RTM to validate directly
- *(Optional)* **`cross-check-artefact.md`** — a second artefact to reconcile (e.g., RTM vs proposal)
- **`brief.md`** — collateral brief, specifically the submission mechanics captured during collateral analysis
- **`coverage-matrix.md`** — to cross-reference whether mandatory requirements are addressed

## Outputs

- **`compliance-report.md`** — per-requirement validation table with remediation instructions for failures
- *(Optional)* **`compliance-report-numeric-inventory.md`** — structured numeric requirements inventory used during the check
- *(Optional)* **`compliance-report-fr-nfr-inventory.md`** — structured functional and non-functional requirements inventory used during the check

---

## Purpose

Compliance is binary in procurement. A non-compliant proposal may be eliminated from evaluation regardless of technical quality. This skill catches compliance gaps after all drafting and review passes are complete — because every upstream edit is an opportunity to introduce a gap.

The original version of this skill checked **presence**: is the topic there? Is the section present? This version adds **parity**: does the proposal's stated value meet or exceed the binding requirement value? It also checks **deviation-register completeness**, **semantic carve-outs**, **functional and non-functional requirement coverage**, **modal-verb and scope-tier classification**, and **covered-by** discipline — the classes of shortfall most likely to slip past a presence-based check.

The skill is domain-agnostic. It works for any procurement (aviation, defence, IT, infrastructure, professional services, or any other domain). All field names — `applies_to`, `domain_hint`, `category`, and the IDs — are free-form and must be derived from the engagement's source documents. The skill does not bake in a fixed taxonomy of subsystems, layers, or quality attributes.

---

## Provenance and Blindness Discipline

Every finding in the compliance report must cite a clause in a document listed under **Inputs** for this run. A finding that cites a reviewer's feedback, a client's own gap list, a prior eval's answer key, or any other document not declared as an input for this run is invalid — remove it or re-derive it from a declared source before including it in the report.

If a stakeholder-delta input is supplied, findings may cite it, and it must be listed in Inputs for that run.

If this skill is run as the subject of an evaluation against a gold/reference gap list, that gold/reference document must be excluded from the declared Inputs for the run and listed explicitly under an "Excluded sources" note in the resulting report. Findings that reference the excluded document, directly or by paraphrase, invalidate the blind-run claim — re-run without exposure to that document before scoring recall/precision against it.

---

## Process

### Step 1: Extract Compliance Requirements

Re-read the requirements documents in binding hierarchy order (CR + ABR > stakeholder-deltas, if supplied, most-recent-communication wins > Addendum > RFP/BRD). If a buyer response sheet is supplied, treat it as the most direct and complete source of FRs/NFRs — extract from it first, then enrich from the main RFP/BRD body. Extract every explicit compliance requirement. These fall into categories:

**Functional Requirements (FR):**
- What the system, service, or deliverable must *do*. Expressed as a verb-on-object statement.
- May be numbered (e.g., `FR17`) or unnumbered in prose.
- May appear in a dedicated "Functional Requirements" section, a buyer response sheet, or scattered through scope descriptions.
- Capture every one. Do not summarise.

**Non-Functional Requirements (NFR):**
- Cross-cutting quality attributes: performance, scalability, availability, reliability, security, maintainability, usability, accessibility, compliance, auditability, interoperability, data integrity, latency, throughput, and similar.
- Same enumeration discipline as FRs.

**Submission Format Requirements:**
- Page limits (per section and total)
- Font size, margin, and spacing requirements
- File format requirements (PDF, Word, specific naming conventions)
- Number of copies (physical/digital)
- Required file/volume structure
- Cover page requirements

**Content Requirements:**
- Required sections or topics that must be addressed
- Required appendices (resumes, certifications, financial statements, representations)
- Required forms (signature pages, certifications, representations and certifications)
- Required contact information placement
- Executive summary requirements (if mandated)

**Substantive Requirements:**
- Mandatory certifications or clearances
- Mandatory experience thresholds
- Mandatory team qualifications
- Mandatory pricing structure
- Small business utilization targets

**Procedural Requirements:**
- Submission deadline (date and time, time zone)
- Submission method
- Q&A or amendment acknowledgment requirements
- Conflict of interest disclosures
- Lobbying certifications

For every requirement, FR, and NFR, record:

- `requirement_id` — use the buyer's ID verbatim when present (`FR17`, `NF38`, `S-001`); otherwise generate a stable ID (`F-NN`, `NF-NN`).
- `requirement_text` — verbatim or close-paraphrase from the source.
- `category` — one of the categories above. For FRs and NFRs, also record an NFR sub-category (performance, security, usability, etc.) using free-form text — no fixed taxonomy.
- `modal_verb` — `shall`, `must`, `should`, `may`, `will`, or `none`. This drives verdict logic in Step 3.
- `mandatory_or_scored` — `M` for mandatory/pass-fail, `S` for scored (with weight), `I` for informational.
- `scope_tier` — `base`, `optional`, `phase_2`, `out_of_scope_by_source`, or `reserved_for_human`. See Step 2a.
- `domain_hint` — free-form grouping label (e.g., `survey`, `ai`, `sla`, `security`, `platform`, `integration`, `commercial`, `legal`, `operations`, or any other label that helps the reviewer group findings).
- `applies_to` — free-form text naming the subsystem, module, layer, surface, role, deliverable, or other entity the requirement attaches to. Do not limit to a fixed taxonomy.
- `source_document`, `source_location` — exact filename (preserving any repository typos), section, page, and line.
- `exact_language` — quote the source language verbatim when it carries legal, commercial, security, compliance, or acceptance weight.

### Step 2: Build the Numeric/Quantitative Requirements Inventory

Extract every comparable numeric requirement from the authoritative requirements sources. This is now a first-class requirement set, not an afterthought. Capture:

- Values with `≤`, `≥`, `<`, `>`, `=`, `minimum`, `maximum`, `at least`, `at most`, `no more than`, `no less than`.
- Counts: number of agents, sensors, points, gateways, servers, roles, years, deliveries, milestones.
- Time-boxes: response time, resolution time, delivery time, RTO, RPO, alert latency, prediction horizon, breach notification, data retention.
- Quality thresholds: accuracy, error tolerance, resolution, granularity, precision / recall, confidence, completeness, freshness, fidelity.
- Coverage thresholds: system families, integration coverage percentages, layer / catalogue / basemap / surface coverage requirements.

Use the template in `assets/numeric-inventory-template.md` as the output format. Each row must contain:
- `requirement_id`
- `parameter`
- `binding_value`
- `operator` (≤, ≥, =, etc.)
- `source_document`
- `source_location`
- `applies_to` (free-form; what the value applies to)

### Step 2a: Classify Scope Tier

For every requirement, FR, and NFR, classify by scope tier. The proposal's coverage is judged against base-scope items only — optional / phase 2 / out-of-scope items must not be treated as failures if they are absent from the proposal.

- **`base`** — explicitly required in the current engagement's base scope. Must be addressed in the proposal.
- **`optional`** — buyer offers an option or alternative the bidder may take or leave.
- **`phase_2`** — explicitly deferred to a later phase, extension, or option year. May be addressed, but absence is not a failure.
- **`out_of_scope_by_source`** — not in the RFP at all (used to filter "ghost" requirements that appear in the proposal but are not in the source documents; also used to record items the proposal claims to address that have no binding basis).
- **`reserved_for_human`** — explicitly carved out by the buyer (e.g., "buyer reserves the right to amend", "to be confirmed by procurement authority").

Record `scope_tier` in the per-requirement output of Step 1, and use it as a filter in Step 3 (out-of-scope items should not be counted as failures but should be flagged as "scope drift" if the proposal claims to address them with binding language).

### Step 2b: Extract Functional and Non-Functional Requirements Inventory

In addition to the numeric inventory, produce a second first-class inventory: the **FR/NFR inventory**. Use the template in `assets/fr-nfr-inventory-template.md`. Each row must contain:

- `requirement_id` (using the buyer's ID verbatim: `FR17`, `NF38`; otherwise generated as `F-NN`, `NF-NN`)
- `requirement_text` (verbatim or close-paraphrase)
- `category` (`functional` for FR; for NFR, a free-form sub-category such as `performance`, `security`, `usability`, `availability`, `reliability`, `maintainability`, `scalability`, `compliance`, `auditability`, `interoperability`, `data_integrity`, `accessibility`, `latency`, `throughput`, or any other attribute the source uses)
- `modal_verb` (`shall`, `must`, `should`, `may`, `will`, or `none`)
- `mandatory_or_scored` (`M` for mandatory/pass-fail, `S` for scored with weight, `I` for informational)
- `scope_tier` (from Step 2a)
- `domain_hint` (free-form grouping label)
- `applies_to` (free-form; subsystem, module, layer, surface, role, deliverable)
- `source_document`, `source_location`
- `proposal_section` (which section of the proposal addresses it — to be filled in Step 3)
- `proposal_value` (the value or commitment the proposal offers — to be filled in Step 3)
- `covered_by` (`commitment`, `capability_claim`, `not_addressed`, `out_of_scope` — to be filled in Step 3)
- `notes` (rationale, carve-out, deviation pointer)

The FR/NFR inventory is the input to the FR/NFR coverage check in Step 3 and the scope-coverage completeness check in Step 6.

### Step 3: Validate Categorical, Functional, and Non-Functional Requirements

For each requirement (categorical, FR, or NFR) from Step 1, check the target artefact. The verdict set is the same for all three; the difference is what `covered_by` records.

**Pass** — the requirement is clearly addressed. The evidence is in the section and is specific enough that an evaluator would check this box. For FRs/NFRs, also record `proposal_section` and `proposal_value`.

**Fail** — the requirement is not addressed, or is addressed incompletely. Specify exactly what is missing and where it should appear. For base-scope FRs/NFRs not addressed, this is a blocking finding.

**Partial** — the requirement is partially addressed. Some elements are present, others are missing. Specify what is present and what is not. For FRs/NFRs, also record which elements are present and which are missing.

**Ambiguous** — the requirement is unclear, and whether the proposal meets it depends on interpretation. State the ambiguity, the interpretation used, and the risk. Mark as "Assumed compliant — [rationale]."

**Not Applicable** — the requirement does not apply to this response. State why. For FRs/NFRs, this is only valid when the buyer's response sheet or RFP body explicitly excludes it from the engagement (e.g., a different lot, a different phase, a different buyer entity).

**Modal-verb-driven verdict logic (FRs/NFRs only):**

- `shall` / `must` / `will` (in binding context) → **binding**. A `Fail` is a blocking finding.
- `should` → **scored**. A `Fail` is a deduction-grade finding (severity depends on score weight).
- `may` → **optional**. Addressed well, it earns points; not addressed, no points lost.
- `none` → **ambiguous**. Treat as binding unless context overrides; record the assumption.

**Covered-by discriminator (FRs/NFRs only):** for every FR/NFR that is at least Partial, record one of:

- `commitment` — the proposal makes a binding, measurable commitment ("we will deliver X by date Y at value Z"). This is the strongest form of coverage.
- `capability_claim` — the proposal asserts it *can* do X but does not commit to X in this contract ("our platform supports X; available on request"). This is weaker than a commitment and should be flagged for the human reviewer, because the buyer may not accept a capability claim as evidence.
- `not_addressed` — the proposal does not mention or address the requirement at all. Combined with `scope_tier = base`, this is a `Fail`.
- `out_of_scope` — the requirement is `optional`, `phase_2`, `out_of_scope_by_source`, or `reserved_for_human`. Absence is not a failure; if the proposal claims to address it with binding language, flag as `scope_drift` in the report.

**Advisory (expectation risk)** is a sixth, non-blocking verdict class reserved exclusively for the architecture-completeness heuristics in Step 6a. It flags a structural expectation gap without asserting the source explicitly requires it, and never counts toward Fail totals or blocking status.

### Step 4: Validate Numeric Requirements (Parity / Delta Evaluation)

For each row in the numeric inventory from Step 2, locate the corresponding figure in the target artefact (and in the cross-check artefact, if supplied). Then:

- **Pass** — target value meets or exceeds binding value.
- **Partial** — target value is below binding value, but is explicitly declared as a deviation/exemption. Note: deviation still requires customer acceptance.
- **Partial (superseded-value risk)** — the target value meets an older or lower-tier source's binding value, but a newer or higher-tier source (per the hierarchy order established in Step 1) demands a stricter value that the target does not meet. Do not mark this Pass merely because it matches the source the proposal author consulted — name both source values and locations so the gap is traceable.
- **Fail** — target value is below binding value and is **not** declared in the deviation register. This is an undeclared shortfall.
- **Ambiguous** — target uses a status word ("Compliant", "Meets", "Exceeds") without a measurable figure, or the corresponding value cannot be found.

Compute and record the ratio or delta where useful (e.g., "proposal vertical RMSE is 6.7× worse than BRD"). This makes the severity of the gap immediately visible.

When two authoritative sources at different hierarchy tiers state different binding values for the same parameter, compare the target artefact against the **strictest applicable value**, not merely the first one located.

### Step 5: Semantic Carve-Out and Over-Claim Detection

For every row in the target artefact that is marked **Compliant** (or equivalent status word), read the commitment text carefully. Downgrade the verdict if the commitment contains parenthetical weakening:

- "subject to"
- "and Excluded Events"
- "measured at the [system/platform] boundary"
- "subject to baseline confirmation"
- "to be confirmed"
- "as available"
- "where feasible"
- "on terms agreed at renewal"

Also flag over-claims:
- "Compliant" applied to a set where only a subset is substantiated (e.g., "per-agent standards, each at or above BRD threshold" when only 2 of 7 agents have targets).
- "100% coverage" with a mechanism that materially narrows the covered set.
- "Compliant" applied to an FR that the proposal only addresses by capability claim, not commitment.

For FRs/NFRs specifically, also detect these carve-out patterns:

- "available as a Phase 2 option" — when the requirement is in `base` scope.
- "where regulatory approval is granted" — when the requirement is unconditional.
- "subject to interface availability from [third party]" — when no third-party dependency is named in the source documents.
- "to be confirmed at design" — when the requirement is explicit and binding.
- "via upgrade" or "in a future release" — when the requirement is in the current contract.
- "during scheduled maintenance windows" — when the requirement is for live operation.

Quote the weakening phrase in the report and downgrade to **Partial** or **Ambiguous**. If the weakening phrase contradicts a `shall` requirement, downgrade to **Fail** and flag as undeclared deviation (Step 9).

### Step 6: Check "Addressed Within Narrative" Requirements and Scope-Coverage Completeness

Many complex procurements include requirements that must be "addressed within the narrative" rather than in a dedicated section. For these, check:
- Is the topic addressed somewhere in the proposal?
- Is it addressed with sufficient depth, or merely mentioned in passing?
- Would an evaluator searching for this topic find it?

If the requirement is addressed but buried, note the location and assess whether it is prominent enough.

**Scope-coverage completeness check (FRs/NFRs specifically):** using the FR/NFR inventory from Step 2b, build the set of all `base`-scope FRs and NFRs from the buyer's response sheet (or RFP). Confirm that every item in the set is either:
- addressed in the proposal with `covered_by = commitment` or `capability_claim`, or
- explicitly listed in the deviation register with a unique ID, rationale, and mitigation.

Items that are `not_addressed` AND `not in the deviation register` are **Fail** (undeclared deviation). This is the check that catches the "N mandatory FRs, only M addressed" type of gap, where M < N. For each failure, record:
- `requirement_id`
- `requirement_text` (short)
- `proposal_section` where it was supposed to be (if a target section is named in the response sheet)
- severity (`blocking` if mandatory and base-scope; `scored` if scored with non-trivial weight; `informational` if optional)

### Step 6a: Architecture-Completeness Heuristics (Advisory)

When the source documents mandate a federated, multi-system, or platform-of-platforms architecture (several distinct systems, registries, or data sources that must be integrated, unified, or cross-referenced), run a set of generic structural probes regardless of whether the source explicitly names each probe. These heuristics surface a class of "expectation gap" that experienced evaluators look for even when the RFP itself doesn't spell it out — but because the source does not explicitly demand them, findings here use a distinct, non-blocking verdict class rather than Fail/Partial.

For each named integration point across the federated system, check whether the proposal addresses:
- **Identifier / cross-reference mapping** — how records or entities in one system are matched to their counterparts in another.
- **Lifecycle / version governance** — how changes to a shared object are tracked, versioned, or approved over time.
- **Relationship / structural model** — how the parts of the federated system relate to each other (hierarchy, dependency, composition), not just that they exist.
- **Long-term ownership** — who is accountable for a shared asset or dataset after handover, and how that ownership transfers.
- **End-to-end lineage** — whether a value or record can be traced from its origin through every system it passes through to its final consumer.

Record each finding as:
- `probe` — which of the five heuristics.
- `applies_to` — the specific systems/entities the probe was run against (free-form, from the source).
- verdict — **Advisory (expectation risk)** if the proposal is silent, or **Advisory (addressed)** if the proposal covers it. If the source's own explicit language also binds this probe (caught in Step 1/3), the finding belongs there as a Fail/Partial, not here.

This step is generic across domains — it is not specific to any one industry's federated architecture. Skip entirely when the source does not describe a multi-system or federated architecture.

### Step 7: Estimate Page/Word Count

For each section, estimate the page count based on word count, standard formatting, tables, diagrams, and white space. Compare against page limits. Flag sections within 10% of the limit as "at risk."

### Step 8: Check Cross-References and Multi-Artefact Consistency

Verify that:
- Sections reference the correct appendices (and those appendices exist or are noted as pending).
- Case studies reference the correct client names and metrics consistently across sections.
- Team member names and roles are consistent.
- Pricing references match the pricing approach described in the technical narrative.

If a cross-check artefact (e.g., RTM, final proposal, costing table) was supplied, perform three-way reconciliation:
- BRD target ↔ proposal commitment ↔ cross-check artefact row.
- Flag any internal inconsistency between tables in the target or between the target and the cross-check artefact.

**Naming discipline:** use the exact source filenames in all references, including any repository typos. Do not attribute a table from one document to another document.

**RACI-direction check (when a RACI matrix is present in the target or cross-check artefact):** for each row, compare the assigned Accountable (A) and Responsible (R) parties against the accountability intent stated in the source documents (e.g., who the buyer names as approver, owner, or final decision-maker for that activity). Flag any row where the proposal's RACI reverses or contradicts the source's stated intent (e.g., proposal assigns the vendor as Accountable for an activity the source reserves for the buyer, or vice versa). This is a directional check, not a completeness check — a RACI row can be present and still assign the wrong party.

### Step 9: Deviation-Register Completeness Audit

Build the set of all numeric and categorical requirements that are not met at the binding value or that carry carve-outs. Read the target artefact's deviation/exemption/assumption register. For each shortfall:

- If it appears in the register with a unique ID, rationale, and mitigation/acceptance requirement → note it as a declared deviation. Record `deviation_acceptance_status` as one of: `accepted` (buyer has explicitly signed off), `rejected` (buyer has explicitly declined), or `pending` (declared but no buyer decision recorded — the default when the register is silent on acceptance). A `pending` status does not clear the deviation; flag it for human follow-up before the proposal is finalized.
- If it does **not** appear in the register → create a new **Fail** finding: "Undeclared deviation — [requirement] requires [binding value]; proposal offers [proposal value]; not listed in deviation register."

This step is what catches the silent gaps: spec values looser than the source, optional deliverables treated as out-of-scope, missing methods, missing layers, missing subsystems, carve-outs that never made it into the register.

### Step 10: Adversarial Critic Pass

Before finalizing the report, run a second pass over the numeric inventory and the target artefact. Ask:
- "What binding numeric specs were treated as Pass/Compliant in Step 4 but are actually weaker in the target?"
- "Are there shortfalls missing from the deviation register?"
- "Are there internal inconsistencies between tables in the target?"
- "Are there status-word over-claims that Step 5 missed?"

Append any new findings. Loop until one full pass returns nothing new, or until diminishing returns are reached.

### Step 11: Produce the Compliance Report

Write `compliance-report.md` with:
- **Coverage summary scoreboard** (top of report):
  - Total FRs in source / FRs addressed (commitment) / FRs addressed (capability claim) / FRs partial / FRs not addressed / FRs out of scope.
  - Total NFRs in source / NFRs addressed (commitment) / NFRs addressed (capability claim) / NFRs partial / NFRs not addressed / NFRs out of scope.
  - Total categorical requirements in source / Pass / Fail / Partial / Ambiguous / N/A.
  - Weighted score impact (sum of score weights of all `Fail` and `Partial` items where the requirement is `scored`).
- Numeric requirements inventory + parity table.
- FR/NFR inventory + coverage table (per FR/NFR: id, text, category, modal verb, scope tier, proposal_section, proposal_value, covered_by, verdict, deviation register id if any).
- Deviation-register completeness table.
- Carve-out / over-claim findings.
- Per-requirement validation table.
- Remediation instructions for every failure and partial.
- Page count assessment.
- Cross-reference consistency notes.
- Scope-drift findings (proposal claims binding language for an `out_of_scope_by_source` or `phase_2` requirement).
- Pre-flight status: whether the proposal is ready for assembly or has blocking issues.

### Step 12: Surface Blocking Issues

If any mandatory requirement fails compliance:
- Mark the compliance report prominently: "BLOCKING: [count] mandatory requirements not met"
- List blocking issues at the top of the report before the detailed table
- The proposal assembler should not proceed until blocking issues are resolved

---

## Graceful Degradation

**Empathy-reviewed sections not available (only raw drafts):**
- Validate the raw section drafts. Note that compliance is being checked against pre-review content and should be re-checked after tone review.

**Buyer response sheet not supplied:**
- Fall back to extracting FRs/NFRs from the RFP/BRD body. Be aware that FRs/NFRs may be scattered through scope descriptions; enumerate carefully. Note in the report that without a buyer response sheet, the FR/NFR coverage check is run from inferred IDs and may be incomplete.

**RFP has vague compliance requirements:**
- Validate what is explicit. For vague requirements, mark as "Ambiguous — assumed compliant" with the interpretation used.
- Note in the report that compliance certainty is reduced due to vague source language.

**Sections are missing for some RFP requirements:**
- Mark as Fail. Do not assume the missing section will be written later — surface it now.

**No page limits specified:**
- Skip page count validation. Note "No page limits specified" in the report.

**Coverage matrix not available:**
- Validate compliance from the RFP/BRD directly. Note reduced cross-reference capability.

**Numeric values are missing from the source document:**
- Skip parity check for that item. Mark as "Ambiguous — no comparable value in source."

**Deviation register not present in the proposal:**
- Treat every below-binding shortfall as a Fail (undeclared deviation). Note in the report that absence of a deviation register increases compliance risk.

**Modal verb is missing or ambiguous in the source:**
- Treat as binding (`shall`-equivalent) unless context overrides. Record the assumption in `notes`.

**Scope tier is not stated in the source:**
- Default to `base` for explicit requirements. If the requirement is in a clearly-marked "optional" or "future" section, classify as `optional` or `phase_2`. Record the assumption.

**Applies_to / domain_hint is genuinely free-form:**
- These fields are intentionally free-form. Do not invent or impose a fixed taxonomy. If the source documents do not name a subsystem, record `applies_to` as `unspecified` and `domain_hint` based on the most relevant topic area in the source.

**Stakeholder-delta document not supplied:**
- Proceed using only the formal RFP/BRD/ABR/CR documents. Note in the report that no post-issuance buyer-communication log was available, so requirements changed verbally or via informal channels after issuance may not be captured.

---

## Integration with Other Skills

- **`rfp-analysis-and-response`** is the upstream skill for understanding the buyer documents and drafting the response. Its compliance review is high-level and strategic.
- **Enhanced `compliance-validator`** is the downstream final quality gate. It runs after drafting and empathy review and before assembly. It performs the rigorous numeric parity, deviation-register completeness, semantic carve-out, and multi-artefact reconciliation checks that the upstream analysis does not.
- **Both skills are needed.** Do not treat `rfp-analysis-and-response` as the final compliance gate, especially when the RFP/BRD contains measurable thresholds.
- **Proposal Assembler** reads `compliance-report.md` before assembling — if critical failures exist, assembly should stop.
- **Compliance report** serves as the final quality gate; it is read by the assembler and by the human reviewer.
- This skill does not modify sections — it reports. Fixes are applied by the team or by re-running upstream skills.

---

## Lessons learned and anti-patterns to avoid

Lessons distilled from prior compliance exercises:

1. **Presence is not parity.** A proposal can address every topic and still be non-compliant if the stated value is weaker than the binding requirement.
2. **Single-artefact validation misses three-way gaps.** Validating only the RTM misses cases where the proposal diverges from both the BRD and the RTM.
3. **Deviation registers are often under-populated.** A declared deviation does not excuse undeclared shortfalls. Audit every BRD numeric spec against the register.
4. **"Compliant" is not evidence.** Status words with parenthetical carve-outs or incomplete substantiation must be downgraded.
5. **Document attribution matters.** Do not attribute a table from one source to another; always verify which file the line number points to.
6. **Modal verbs are binding.** "Should" is not "shall". A `should` requirement that is missing is a scored deduction, not a blocking failure — and a `shall` requirement addressed only by capability claim is a `Partial`, not a `Pass`.
7. **Scope tiers separate ghost requirements from real ones.** When the proposal claims to address something the RFP never asked for, that is scope drift — flag it. When the RFP asks for something the proposal does not address, that is undeclared deviation — fail it. Conflating the two masks both.
8. **The buyer's response sheet is the most direct source of FRs/NFRs.** When supplied, extract from it first; do not re-derive IDs by reading the RFP body.
9. **Coverage summary tells the story before the detail.** A single scoreboard (FRs / NFRs / categorical / weighted score) at the top of the report is the difference between a report a human can act on in 30 seconds and a report that requires re-reading to interpret.
10. **Matching a stale source is not compliance.** When two authoritative sources disagree on a threshold, matching the looser, superseded one is a `Partial (superseded-value risk)`, not a `Pass` — always compare to the strictest applicable value.
11. **RACI completeness is not RACI correctness.** A RACI row can list every activity and still assign accountability to the wrong party — check direction, not just presence.
12. **Advisory findings must stay advisory.** Architecture-completeness heuristics surface expectations an experienced evaluator would probe for, but they must never be counted as Fail/Partial or contribute to blocking status unless the source's own explicit language (caught in Step 1/3) confirms the requirement.
13. **Provenance discipline prevents false confidence.** A finding that cites an undeclared source (e.g., a gold/reference gap list during a "blind" eval run) inflates apparent recall. Verify every citation resolves to a declared input before trusting eval metrics.
