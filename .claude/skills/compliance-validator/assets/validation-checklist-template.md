# Compliance Validation Report

This report validates a proposal / RTM against the source requirements documents. It is domain-agnostic: all field values (`applies_to`, `category`, `domain_hint`, etc.) are free-form and derived from the engagement's source documents. No fixed taxonomy of subsystems or quality attributes is assumed.

## Pre-Flight Status

**Status:** [READY FOR ASSEMBLY / BLOCKING ISSUES EXIST / REVIEW REQUIRED]

**Blocking Issues:** [Count — base-scope FRs / NFRs / categorical requirements that are not met or only addressed by capability claim where commitment is required]
**Warnings:** [Count — partial compliance, ambiguous requirements, scored deductions]

### Blocking Issues (if any)

| # | Requirement ID | Requirement | RFP Reference | Why Blocking | Required Action |
|---|---------------|-------------|---------------|--------------|-----------------|
| | | | | | |

---

## Coverage Summary Scoreboard

A single-page scoreboard so the human reviewer can act on the report in 30 seconds without re-reading the detail.

### Functional Requirements (FR)

| Scope Tier | Total in Source | Pass | Partial (commitment) | Partial (capability claim) | Fail (undeclared) | Fail (declared deviation) | Out of Scope / Phase 2 | Not in Source |
|---|---|---|---|---|---|---|---|---|
| Base | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Optional | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Phase 2 | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| **Total** | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |

### Non-Functional Requirements (NFR)

| Scope Tier | Total in Source | Pass | Partial (commitment) | Partial (capability claim) | Fail (undeclared) | Fail (declared deviation) | Out of Scope / Phase 2 | Not in Source |
|---|---|---|---|---|---|---|---|---|
| Base | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Optional | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| Phase 2 | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |
| **Total** | [N] | [N] | [N] | [N] | [N] | [N] | [N] | [N] |

### Categorical Requirements (Format / Content / Substantive / Procedural)

| Category | Total | Pass | Fail | Partial | Ambiguous | N/A |
|---|---|---|---|---|---|---|
| Submission Format | [N] | [N] | [N] | [N] | [N] | [N] |
| Content | [N] | [N] | [N] | [N] | [N] | [N] |
| Substantive | [N] | [N] | [N] | [N] | [N] | [N] |
| Procedural | [N] | [N] | [N] | [N] | [N] | [N] |

### Weighted Score Impact

Sum of `score_weight` of all `Fail` and `Partial` items where the requirement is scored.

| Requirement Class | Total Score at Risk | Realised Deductions | Net After Mitigation |
|---|---|---|---|
| FR (scored) | [N] | [N] | [N] |
| NFR (scored) | [N] | [N] | [N] |
| Categorical (scored) | [N] | [N] | [N] |
| **Total** | [N] | [N] | [N] |

---

## Functional Requirements (FR)

One row per FR. Free-form `applies_to` and `category` are derived from the source.

| # | Req ID | Requirement (short) | Category | Applies To | Modal | Scope | Source | Proposal Section | Proposal Value | Covered By | Verdict | Deviation ID | Notes |
|---|--------|---------------------|----------|------------|-------|-------|--------|------------------|----------------|------------|---------|--------------|-------|
| FR-001 | | | functional | | | | | | | | | | |
| FR-002 | | | functional | | | | | | | | | | |
| FR-003 | | | functional | | | | | | | | | | |

## Non-Functional Requirements (NFR)

One row per NFR. The `category` column is the free-form NFR sub-category (performance, security, usability, availability, etc.) — derived from the source.

| # | Req ID | Requirement (short) | Category (NFR sub) | Applies To | Modal | Scope | Source | Proposal Section | Proposal Value | Covered By | Verdict | Deviation ID | Notes |
|---|--------|---------------------|--------------------|------------|-------|-------|--------|------------------|----------------|------------|---------|--------------|-------|
| NF-001 | | | | | | | | | | | | | |
| NF-002 | | | | | | | | | | | | | |
| NF-003 | | | | | | | | | | | | | |

## Scope-Coverage Completeness (FRs/NFRs)

Build the set of all `base`-scope FRs and NFRs from the source. Confirm that every item is either addressed in the proposal with `covered_by = commitment` or `capability_claim`, or explicitly listed in the deviation register. Items that are `not_addressed` AND `not in the deviation register` are **Fail**.

| # | Req ID | Requirement (short) | Class | Expected Section | Verdict | Deviation ID | Severity | Remediation |
|---|--------|---------------------|-------|------------------|---------|--------------|----------|-------------|
| | | | FR / NFR | | Pass / Partial / Fail | | blocking / scored / informational | |

### Scope-Drift Findings (Proposal claims binding language for an out-of-scope or phase-2 item)

| # | Req ID | Requirement (short) | Class | Scope Tier | What the Proposal Claims | Why this is drift |
|---|--------|---------------------|-------|------------|-------------------------|-------------------|
| | | | | | | |

---

## Numeric / Quantitative Requirements

| # | Req ID | Parameter | Binding | Operator | Applies To | Source | Proposal Value | Ratio / Delta | Verdict | Deviation ID | Notes |
|---|--------|-----------|---------|----------|------------|--------|----------------|---------------|---------|--------------|-------|
| N-001 | | | | | | | | | | | |
| N-002 | | | | | | | | | | | |

---

## Submission Format Requirements

| # | Requirement | RFP Reference | Mandatory | Status | Evidence / Location | Remediation |
|---|-------------|---------------|-----------|--------|--------------------| ------------|
| F-001 | Page limit: [X] pages for [section] | §X.X, p.Y | Yes / No | Pass / Fail / Partial | [Where in proposal this is met] | [What to fix, if needed] |
| F-002 | Font: [requirement] | | | | | |
| F-003 | Margins: [requirement] | | | | | |
| F-004 | File format: [requirement] | | | | | |
| F-005 | Volume / file structure: [requirement] | | | | | |
| F-006 | Cover page: [requirement] | | | | | |
| F-007 | Table of contents: [requirement] | | | | | |

## Content Requirements

| # | Requirement | RFP Reference | Mandatory | Status | Evidence / Location | Remediation |
|---|-------------|---------------|-----------|--------|--------------------| ------------|
| C-001 | Section: [required section name] | | | | [Which file addresses this] | |
| C-002 | Appendix: [required appendix] | | | | | |
| C-003 | Form: [required form] | | | | | |
| C-004 | Executive summary | | | | | |
| C-005 | Contact information | | | | | |

## Substantive Requirements

| # | Requirement | RFP Reference | Mandatory | Status | Evidence / Location | Remediation |
|---|-------------|---------------|-----------|--------|--------------------| ------------|
| S-001 | Certification: [required cert] | | | | [Where in proposal this is claimed] | |
| S-002 | Experience: [minimum threshold] | | | | | |
| S-003 | Personnel qualification: [requirement] | | | | | |
| S-004 | Pricing structure: [required format] | | | | | |
| S-005 | Small business utilization: [target] | | | | | |

## Procedural Requirements

| # | Requirement | RFP Reference | Mandatory | Status | Evidence / Location | Remediation |
|---|-------------|---------------|-----------|--------|--------------------| ------------|
| P-001 | Submission deadline: [date / time / TZ] | | Yes | | | |
| P-002 | Submission method: [method] | | Yes | | | |
| P-003 | Amendment acknowledgment | | | | | |
| P-004 | Conflict of interest disclosure | | | | | |

## "Addressed Within Narrative" Requirements

| # | Requirement | RFP Reference | Found In Section | Prominence | Sufficient Depth | Notes |
|---|-------------|---------------|-----------------|------------|-----------------|-------|
| N-001 | [Embedded requirement] | | [Section file] | [Prominent / Buried] | [Yes / No] | |

## Modal-Verb and Carve-Out Findings

| # | Req ID | Source Language | What the Proposal Says | Modal | Verdict | Notes |
|---|--------|----------------|------------------------|-------|---------|-------|
| | | | | shall / should / may | | |

## Over-Claim Findings

| # | Req ID | What the Proposal Claims | Why this is an over-claim | Verdict |
|---|--------|--------------------------|--------------------------|---------|
| | | | | |

---

## Deviation Register Completeness

| # | Req ID | Requirement | Binding Value | Proposal Value | Declared? | Deviation ID | Rationale (from register) | Buyer Acceptance Required? |
|---|--------|-------------|---------------|----------------|-----------|--------------|---------------------------|----------------------------|
| | | | | | Yes / No | | | Yes / No |

---

## Page Count Assessment

| Section | Estimated Pages | RFP Limit | Status | Notes |
|---------|----------------|-----------|--------|-------|
| [Section name] | [count] | [limit or "None"] | Within / At Risk / Over | |
| **Total** | [count] | [limit or "None"] | | |

---

## Cross-Reference Consistency

| Check | Status | Notes |
|-------|--------|-------|
| Appendix references resolve to actual appendices | Pass / Fail | [Details] |
| Case study metrics consistent across sections | Pass / Fail | |
| Team member names / roles consistent | Pass / Fail | |
| Pricing narrative consistent with pricing tables | Pass / Fail | |
| Client name spelled consistently | Pass / Fail | |
| RFP reference number cited correctly | Pass / Fail | |
| FR / NFR IDs consistent between proposal and RTM | Pass / Fail | |

---

## Remediation Summary

[Ordered list of all required fixes before the proposal can be assembled]

1. **[BLOCKING]** [Requirement] — [What must be done]
2. **[BLOCKING]** [Requirement] — [What must be done]
3. [Requirement] — [What should be done]
4. [Requirement] — [What should be done]
