# Plan: Enhanced compliance-validator skill

## Goal
Update the `compliance-validator` skill so that the gap classes uncovered in the Airport Eye exercise (AI-agent inventory shortfalls, survey/accuracy deviations, SLA carve-outs, over-claims, undeclared deviations) are surfaced automatically on future validation runs, without requiring manual adversarial passes.

## Scope of changes
1. Rewrite `/.claude/skills/compliance-validator/SKILL.md` with the enhanced process.
2. Add a new supporting asset: `/.claude/skills/compliance-validator/assets/numeric-inventory-template.md`.
3. Document the learnings from the Airport Eye test run in project memory.

## What the enhanced skill must do differently

### 1. Build a numeric/quantitative requirements inventory (new Step 1B)
After extracting categorical requirements, extract every comparable numeric value from the authoritative requirements documents in hierarchy order:
- Values with ≤ / ≥ / < / > / minimum / maximum / at least / at most.
- Counts: agents, sensors, pumps, points, roles, years.
- Times: response, latency, RTO, RPO, alert latency, prediction horizon, notification windows.
- Quality thresholds: RMSE, GSD, DTM/DSM resolution, contour interval, LOD, precision/recall.
- Coverage thresholds: integration coverage, system families, NAVAID/layer catalogues.

Output: a structured table with `requirement_id`, `parameter`, `binding_value`, `source_document`, `source_location`.

### 2. Perform parity / delta evaluation (new Step 3B)
For every numeric inventory item:
- Locate the corresponding figure in the target artefact (proposal, RTM, etc.).
- If the target meets or exceeds the binding value → **Pass**.
- If the target is below the binding value but is declared as a deviation → **Partial** (deviation, needs acceptance).
- If the target is below the binding value and NOT declared → **Fail** (undeclared shortfall).
- If the target uses a status word ("Compliant", "Meets", "Exceeds") without a measurable figure → **Ambiguous**.

### 3. Audit the deviation register for completeness (new Step 6B)
- Build the set of all numeric/categorical shortfalls and carve-outs.
- Read the proposal's deviation/exemption/assumption register.
- Require every shortfall to appear in the register with a unique ID, rationale, and mitigation or acceptance requirement.
- Any shortfall not listed → new **Fail**.

### 4. Detect semantic carve-outs and over-claims (new Step 3C)
For every row marked **Compliant** (or equivalent status word) in the proposal:
- Read the commitment text.
- If it contains weakening phrases such as "subject to", "and Excluded Events", "measured at the ... boundary", "subject to baseline confirmation", "to be confirmed", "as available", downgrade to **Partial** or **Ambiguous** and quote the carve-out.
- If the status is "Compliant" but the evidence does not substantiate it for all covered items, flag as **Over-claim / Partial**.

### 5. Support multi-artefact validation (updated Inputs and Step 6)
- Primary target: proposal or section-under-test.
- Requirements source(s): in hierarchy order (CR/ABR > Addendum > RFP/BRD).
- Optional cross-check artefact: RTM or second proposal version.
- When a cross-check artefact is supplied, perform three-way reconciliation: BRD target ↔ proposal commitment ↔ RTM row. Flag internal inconsistencies.

### 6. Add an adversarial critic pass (new Step 7B)
Before finalising the report, run a second pass that asks:
- "What binding numeric specs were treated as Pass/Compliant but are actually weaker in the target?"
- "Are there shortfalls missing from the deviation register?"
- "Are there internal inconsistencies between tables in the target?"
Append new findings.

### 7. Naming and reference discipline
- Use the exact filenames of source documents in the report, including repository typos (`Aiport`, `Busines`, etc.).
- Quote line numbers from the markdown extractions.
- Distinguish clearly between documents: do not attribute a table from the BRD to the proposal.

## Files to change
- `/Users/sujoymukherjee/code/doc2md/parse2wiki/.claude/skills/compliance-validator/SKILL.md` — full rewrite of the process section.
- `/Users/sujoymukherjee/code/doc2md/parse2wiki/.claude/skills/compliance-validator/assets/numeric-inventory-template.md` — new template for the numeric inventory.

## Files NOT to change
- No source documents.
- No existing compliance reports.

## Validation
After updating the skill, the Airport Eye exercise should be reproducible by invoking the skill against the same source set and checking that the output contains:
- Agent count shortfall (3 vs 8).
- Survey accuracy shortfalls (≤20 cm vs ≤3 cm, 50 cm vs 10 cm, ≤10 cm vs ≤5 cm).
- SLA carve-outs (Excluded Events, platform-boundary latency, baseline freeze).
- KPI 4 over-claim.
- Undeclared deviations (DTM/DSM, orthophoto GSD, contours, indoor RMSE, DGPS/GNSS/12D, NAVAID layers).
- 15-year lifecycle / O&M renewal carve-out.

## Next steps after plan approval
1. Write the enhanced `SKILL.md`.
2. Write the `numeric-inventory-template.md` asset.
3. Save project memory summarising the learnings.
4. (Optional) Run the enhanced skill against the Airport Eye DRAFT proposal to verify it produces an equivalent report.
