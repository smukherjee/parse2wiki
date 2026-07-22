# Numeric / Quantitative Requirements Inventory Template

Use this template to record every comparable numeric requirement extracted from the authoritative requirements documents (CR/BRD/ABR/Addendum/RFP, in hierarchy order). This inventory is the input to the parity/delta evaluation step.

## Column definitions

| Column | Description |
|---|---|
| `requirement_id` | Unique ID for this numeric requirement (e.g., N-AIR-01, N-AI-03, N-SLA-02). |
| `domain` | Domain group: `survey`, `ai`, `sla`, `security`, `platform`, `integration`, `abr`, etc. |
| `parameter` | Human-readable name of the parameter. |
| `binding_value` | The strictest value from the authoritative source documents. |
| `operator` | The comparison operator: `≤`, `≥`, `<`, `>`, `=`, `minimum`, `maximum`. |
| `unit` | Unit of measurement: cm, s, min, h, d, %, pts/m², years, count, etc. |
| `source_document` | Exact filename of the source document, including any typos in the repository name. |
| `source_location` | Section, page, and/or line number in the markdown extraction. |
| `applies_to` | What the requirement applies to (e.g., "Airborne LiDAR", "AI agents", "BMS/IoT integration"). |
| `proposal_value` | The corresponding value/status found in the proposal/target artefact. |
| `target_location` | Line/section in the target artefact where the value was found. |
| `declared_in_deviation_register` | `Yes` / `No` / `n/a`. |
| `deviation_register_id` | If yes, the ID of the deviation/exemption/assumption entry. |
| `ratio_or_delta` | Optional: how the proposal value compares to the binding value (e.g., "6.7× worse", "2× coarser"). |
| `verdict` | `Pass` / `Partial` / `Fail` / `Ambiguous` / `N/A`. |
| `notes` | Rationale, severity, remediation pointer, or carve-out wording. |

## Example rows

| requirement_id | domain | parameter | binding_value | operator | unit | source_document | source_location | applies_to | proposal_value | target_location | declared_in_deviation_register | deviation_register_id | ratio_or_delta | verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N-AIR-01 | survey | Airborne LiDAR point density (boundary) | 20 | ≥ | pts/m² | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 230 | Airborne LiDAR | ≥20 pts/m² | Proposal DRAFT line 147 | n/a | n/a | 1.0× | Pass | Matches BRD. |
| N-AIR-04 | survey | Vertical RMSE | 3 | ≤ | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1 / KPI 5, lines 232, 211 | Geospatial accuracy | ≤20 cm | Proposal DRAFT line 151 | Yes | Deviation 1 | 6.7× worse | Partial | Declared deviation, still blocking until DIAL accepts. |
| N-AIR-06 | survey | DTM/DSM grid resolution | 10 | = | cm | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.1.1, line 235 | DTM/DSM | 50 cm | Proposal DRAFT line 149 | No | — | 5× coarser | Fail | Undeclared shortfall. |
| N-AI-01 | ai | Mandatory domain AI agents | 8 | = | count | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.3, lines 441–448 | AI agent estate | 3 itemised | Proposal DRAFT lines 500–503 | n/a | n/a | 37.5% | Fail | Six mandatory agents missing from proposal technical narrative. |
| N-AI-16 | ai | Fire Safety alert latency | 5 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §3.5.4, line 458 | Fire Safety agent | not stated | — | n/a | n/a | — | Fail | Agent not itemised; no SLA target offered. |
| N-SLA-04 | sla | Critical incident response time | 10 | ≤ | min | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 6, line 212 | Incident response | ≤30 min | Proposal DRAFT line 990 | Yes | Deviation 2 | 3× slower | Partial | Declared deviation; needs DIAL acceptance. |
| N-SLA-02 | sla | Data latency | 5 | ≤ | s | Change Request Aiport Eye - APOC Phase 2.pdf.md | §2.3 KPI 2, line 208 | Data pipeline | ≤5 s "measured at platform boundary" | Proposal DRAFT line 985 | No | — | scope narrowed | Partial | Carve-out: source-side latency excluded. |

## Guidance for extraction

1. **Hierarchy matters.** If CR/ABR contradicts the RFP/BRD, use the stricter or more recent value and document both.
2. **Capture implicit thresholds.** Phrases like "minimum 5 years", "at least 99.5%", "no more than 10 minutes" should all become rows.
3. **Capture counts even when not numeric.** "All eight agents", "every BMS point", "the full 40-pump IoT set" are countable requirements.
4. **Capture layer/catalogue requirements.** Enumerated lists of systems, layers, NAVAIDs, basemap layers, etc., are comparable coverage requirements.
5. **Do not over-normalise.** Keep each distinct parameter as its own row so the parity check can report exactly where the proposal diverges.
