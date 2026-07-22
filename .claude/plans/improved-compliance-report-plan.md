# Plan: Improved compliance-validation test report for Airport Eye

## Goal
Produce a test compliance report using the improved logic (numeric parity, deviation-register completeness, semantic carve-out detection, multi-artefact reconciliation, adversarial critic pass) and validate whether the three known gap classes from the existing report (§9–§11) surface automatically, plus whether any new issues appear.

## Scope
Validate the **proposal** (`AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`) against the **authoritative requirements** in priority order:
1. `Change Request Aiport Eye - APOC Phase 2.pdf.md` — CR/BRD v1.5 (highest authority)
2. `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` — ABR (additive)
3. `PE_OT System_09.06.pptx.md` — PE_OT (OT systems reconciliation)

Cross-check consistency against the RTM (`AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`) where the proposal claims alignment.

## Methodology (the improved skill logic)

### Step 1: Build the numeric/quantitative requirements inventory
Extract every comparable numeric requirement from CR/BRD + ABR:
- All values with ≤ / ≥ / < / > / minimum / maximum / at least / at most.
- Counts: agents, points, sensors, pumps, roof sensors, roles, years.
- Times: response time, latency, RTO, RPO, alert latency, prediction horizon, breach notification.
- Quality thresholds: RMSE, GSD, DTM/DSM resolution, contour interval, LOD, precision/recall.
- Coverage thresholds: integration coverage, NAVAID layers, system families.

Output: a structured inventory table with `requirement_id`, `parameter`, `binding_value`, `source_document`, `source_location`.

### Step 2: Map proposal commitments
For each inventory item, locate the corresponding value/status in the proposal (or RTM if three-way check requested). Record:
- `proposal_value`
- `status_in_proposal` (Compliant / Deviation / not mentioned)
- `declared_in_deviation_register?` (yes/no)

### Step 3: Parity / delta evaluation
- Proposal meets/exceeds binding value → **Pass**
- Proposal is below binding value but declared as deviation → **Partial** (deviation, needs acceptance)
- Proposal is below binding value and NOT in deviation register → **Fail** (undeclared shortfall)
- Proposal states status word without measurable figure → **Ambiguous**

### Step 4: Deviation-register completeness audit
Build the set of all numeric/categorical shortfalls and carve-outs. Read the proposal’s deviation register. Any shortfall not listed → new **Fail**.

### Step 5: Semantic carve-out detection
For every row marked **Compliant** in the proposal, read the commitment text. If it contains parenthetical weakening ("subject to", "and Excluded Events", "measured at the platform boundary", "subject to baseline confirmation"), downgrade to **Partial / Ambiguous**.

### Step 6: Multi-artefact reconciliation
Where the proposal references the RTM (e.g., agent inventory, per-agent targets), check whether the proposal matches the RTM. Flag internal inconsistencies.

### Step 7: Adversarial critic pass
Prompt a second pass asking: "What did the first pass miss? Are there any binding numeric specs treated as Pass/Compliant that are actually weaker? Are there deviations missing from the register?"

### Step 8: Produce the report
Write `improved-compliance-report-test.md` with:
- Pre-flight status and counts
- Numeric inventory + parity table (the core new artifact)
- Deviation-register completeness table
- Carve-out / over-claim findings
- Blocking issues
- Remediation instructions
- Validation note: which known §9–§11 findings surfaced automatically vs which needed the new logic

## Expected output
A new markdown file: `/Users/sujoymukherjee/code/doc2md/parse2wiki/improved-compliance-report-test.md`

## Validation criteria
After generating the report, compare it against the existing `compliance-report.md` §9–§11:
- Does the numeric parity step catch the agent count gap (3 vs 8), survey accuracy gaps (≤20 cm vs ≤3 cm, 50 cm vs 10 cm, ≤10 cm vs ≤5 cm), and SLA gaps (≤30 min vs ≤10 min)?
- Does the deviation-register audit flag the undeclared DTM/DSM, orthophoto GSD, contour, indoor RMSE, DGPS/GNSS/12D, and NAVAID-layer shortfalls?
- Does the semantic carve-out detection catch KPI 1/2/7 carve-outs and KPI 4 over-claim?
- Does anything new surface that the manual §9–§11 passes missed?

## Files to read (already inspected; will be used)
- `sources/Airport Eye/Change Request Aiport Eye - APOC Phase 2.pdf.md`
- `sources/Airport Eye/Airport Eye Additional Busines Requirements- 2-July-2026.docx.md`
- `sources/Airport Eye/AIRPORT EYE (APOC Phase 2)_Proposal_DRAFT.docx.md`
- `sources/Airport Eye/AIRPORT EYE (APOC Phase 2)_RTM_DRAFT.docx.md`
- `sources/Airport Eye/PE_OT System_09.06.pptx.md` (for OT-system reconciliation)
- Existing `compliance-report.md` (to baseline known findings)

## What will NOT be changed
No source files will be edited. This is a read-only analysis that produces one new report artifact.
