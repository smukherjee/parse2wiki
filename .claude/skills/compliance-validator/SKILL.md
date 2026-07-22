---
name: compliance-validator
description: >
  Validates every reviewed section and the consolidated proposal against the
  RFP/BRD/ABR/CR's explicit requirements. Produces a pass/fail compliance report
  with numeric parity checks, deviation-register completeness, semantic carve-out
  detection, multi-artefact reconciliation, and remediation notes. Runs after the
  empathy reviewer because tone fixes can inadvertently remove compliance-critical
  language.
  Trigger when the user says "check compliance," "validate the sections," "are we
  compliant," "run the compliance check," or after the empathy reviewer has produced
  sections/*-reviewed.md files.
---

## Inputs

- **`sections/[section-name]-reviewed.md`** — reviewed sections from the empathy-reviewer
- **RFP/BRD/ABR/CR document(s)** — the authoritative requirements sources, in hierarchy order
- *(Optional)* **`proposal-artefact.md`** — the consolidated proposal or RTM to validate directly
- *(Optional)* **`cross-check-artefact.md`** — a second artefact to reconcile (e.g., RTM vs proposal)
- **`brief.md`** — collateral brief, specifically the submission mechanics captured during collateral analysis
- **`coverage-matrix.md`** — to cross-reference whether mandatory requirements are addressed

## Outputs

- **`compliance-report.md`** — per-requirement validation table with remediation instructions for failures
- *(Optional)* **`compliance-report-numeric-inventory.md`** — structured numeric requirements inventory used during the check

---

## Purpose

Compliance is binary in procurement. A non-compliant proposal may be eliminated from evaluation regardless of technical quality. This skill catches compliance gaps after all drafting and review passes are complete — because every upstream edit is an opportunity to introduce a gap.

The original version of this skill checked **presence**: is the topic there? Is the section present? This version adds **parity**: does the proposal's stated value meet or exceed the binding requirement value? It also checks **deviation-register completeness** and **semantic carve-outs**, which are the classes of shortfall most likely to slip past a presence-based check.

---

## Process

### Step 1: Extract Compliance Requirements

Re-read the requirements documents in binding hierarchy order (CR + ABR > Addendum > RFP/BRD). Extract every explicit compliance requirement. These fall into categories:

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

Record each requirement with:
- Exact language from the source document
- Source document and location (section, page, line)
- Whether it is mandatory (disqualifying if missed) or expected (points deducted if missed)

### Step 2: Build the Numeric/Quantitative Requirements Inventory

Extract every comparable numeric requirement from the authoritative requirements sources. This is now a first-class requirement set, not an afterthought. Capture:

- Values with `≤`, `≥`, `<`, `>`, `=`, `minimum`, `maximum`, `at least`, `at most`, `no more than`, `no less than`.
- Counts: number of agents, sensors, pumps, cameras, points, gateways, servers, roles, years.
- Time-boxes: response time, resolution time, delivery time, RTO, RPO, alert latency, prediction horizon, breach notification, data retention.
- Quality thresholds: accuracy, RMSE, GSD, DTM/DSM resolution, contour interval, indoor positioning error, LOD, precision/recall.
- Coverage thresholds: system families, integration coverage percentages, NAVAID/layer catalogues, basemap layers.

Use the template in `assets/numeric-inventory-template.md` as the output format. Each row must contain:
- `requirement_id`
- `parameter`
- `binding_value`
- `operator` (≤, ≥, =, etc.)
- `source_document`
- `source_location`
- `applies_to` (what the value applies to, e.g., "AI agents", "airborne survey")

### Step 3: Validate Categorical Requirements

For each requirement from Step 1, check the target artefact:

**Pass** — the requirement is clearly addressed. The evidence is in the section and is specific enough that an evaluator would check this box.

**Fail** — the requirement is not addressed, or is addressed incompletely. Specify exactly what is missing and where it should appear.

**Partial** — the requirement is partially addressed. Some elements are present, others are missing. Specify what is present and what is not.

**Ambiguous** — the requirement is unclear, and whether the proposal meets it depends on interpretation. State the ambiguity, the interpretation used, and the risk. Mark as "Assumed compliant — [rationale]."

**Not Applicable** — the requirement does not apply to this response. State why.

### Step 4: Validate Numeric Requirements (Parity / Delta Evaluation)

For each row in the numeric inventory from Step 2, locate the corresponding figure in the target artefact (and in the cross-check artefact, if supplied). Then:

- **Pass** — target value meets or exceeds binding value.
- **Partial** — target value is below binding value, but is explicitly declared as a deviation/exemption. Note: deviation still requires customer acceptance.
- **Fail** — target value is below binding value and is **not** declared in the deviation register. This is an undeclared shortfall.
- **Ambiguous** — target uses a status word ("Compliant", "Meets", "Exceeds") without a measurable figure, or the corresponding value cannot be found.

Compute and record the ratio or delta where useful (e.g., "proposal vertical RMSE is 6.7× worse than BRD"). This makes the severity of the gap immediately visible.

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

Quote the weakening phrase in the report and downgrade to **Partial** or **Ambiguous**.

### Step 6: Check "Addressed Within Narrative" Requirements

Many complex procurements include requirements that must be "addressed within the narrative" rather than in a dedicated section. For these, check:
- Is the topic addressed somewhere in the proposal?
- Is it addressed with sufficient depth, or merely mentioned in passing?
- Would an evaluator searching for this topic find it?

If the requirement is addressed but buried, note the location and assess whether it is prominent enough.

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

### Step 9: Deviation-Register Completeness Audit

Build the set of all numeric and categorical requirements that are not met at the binding value or that carry carve-outs. Read the target artefact's deviation/exemption/assumption register. For each shortfall:

- If it appears in the register with a unique ID, rationale, and mitigation/acceptance requirement → note it as a declared deviation.
- If it does **not** appear in the register → create a new **Fail** finding: "Undeclared deviation — [requirement] requires [binding value]; proposal offers [proposal value]; not listed in deviation register."

This step is what catches the silent gaps: DTM/DSM coarser than BRD, orthophoto GSD relaxed, missing contours, missing methods, missing layers, carve-outs that never made it into the register.

### Step 10: Adversarial Critic Pass

Before finalizing the report, run a second pass over the numeric inventory and the target artefact. Ask:
- "What binding numeric specs were treated as Pass/Compliant in Step 4 but are actually weaker in the target?"
- "Are there shortfalls missing from the deviation register?"
- "Are there internal inconsistencies between tables in the target?"
- "Are there status-word over-claims that Step 5 missed?"

Append any new findings. Loop until one full pass returns nothing new, or until diminishing returns are reached.

### Step 11: Produce the Compliance Report

Write `compliance-report.md` with:
- Summary: total requirements checked, pass/fail/partial/ambiguous counts, critical failures.
- Numeric requirements inventory + parity table.
- Deviation-register completeness table.
- Carve-out / over-claim findings.
- Per-requirement validation table.
- Remediation instructions for every failure and partial.
- Page count assessment.
- Cross-reference consistency notes.
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

From the Airport Eye exercise:
1. **Presence is not parity.** A proposal can address every topic and still be non-compliant if the stated value is weaker than the binding requirement.
2. **Single-artefact validation misses three-way gaps.** Validating only the RTM misses cases where the proposal diverges from both the BRD and the RTM.
3. **Deviation registers are often under-populated.** A declared deviation does not excuse undeclared shortfalls. Audit every BRD numeric spec against the register.
4. **"Compliant" is not evidence.** Status words with parenthetical carve-outs or incomplete substantiation must be downgraded.
5. **Document attribution matters.** Do not attribute a table from the BRD to the proposal; always verify which file the line number points to.
