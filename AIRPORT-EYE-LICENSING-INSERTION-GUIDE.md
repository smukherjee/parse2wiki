# Airport Eye Licensing Section — Insertion Guide

## QUICK REFERENCE

**File Location:** `/Users/sujoymukherjee/code/doc2md/parse2wiki/AIRPORT-EYE-LICENSING-SECTION.md`

**Insertion Point:** After Section 5.4 (Milestone Payment Schedule), before Section 5.5 (Pricing Principles)

**New Numbering:** Section **5.5a** (Licensing & Intellectual Property Framework)

---

## VISUAL STRUCTURE

### Current Proposal Structure (Section 5)
```
5. Commercial Proposal                               [Page 45]
  ├─ 5.1 Pricing principles                          [Page 45]
  ├─ 5.2 Commercial Tables                           [Page 45]
  │   ├─ Table 1: Geospatial & Survey
  │   ├─ Table 2: BIM Modelling & Asset Attribution
  │   ├─ Table 3: Platform & Digital Twin
  │   ├─ Table 4: System Integration
  │   ├─ Table 5: Infrastructure (pass-through)
  │   ├─ Table 6: AI Agents & Simulation Engine
  │   └─ Table 7: 5-year Operations, Support & Maintenance
  ├─ 5.3 Grand total summary                         [Page 59]
  ├─ 5.4 Milestone payment schedule                  [Page 60]
  ├─ 5.5 Pricing assumptions                         [Page 60]
  └─ 5.6 Deviations and contractual notes            [Page 61]
```

### PROPOSED New Structure (Section 5 with Licensing)
```
5. Commercial Proposal                               [Page 45]
  ├─ 5.1 Pricing principles                          [Page 45]
  ├─ 5.2 Commercial Tables                           [Page 45]
  │   ├─ Table 1: Geospatial & Survey
  │   ├─ Table 2: BIM Modelling & Asset Attribution
  │   ├─ Table 3: Platform & Digital Twin
  │   ├─ Table 4: System Integration
  │   ├─ Table 5: Infrastructure (pass-through)
  │   ├─ Table 6: AI Agents & Simulation Engine
  │   └─ Table 7: 5-year Operations, Support & Maintenance
  ├─ 5.3 Grand total summary                         [Page 59]
  ├─ 5.4 Milestone payment schedule                  [Page 60]
  ├─ 5.5a LICENSING & INTELLECTUAL PROPERTY ★       [NEW: ~10–15 pages]
  │   ├─ 5.5a.1 AIOP Platform Code IP Ownership
  │   ├─ 5.5a.2 Geospatial Digital Twin IP
  │   ├─ 5.5a.3 AI Models, Training Data & Knowledge Assets
  │   ├─ 5.5a.4 Custom Configurations & Integrations
  │   ├─ 5.5a.5 Third-Party & Open-Source Components
  │   ├─ 5.5a.6 Source Code Escrow & Business Continuity
  │   ├─ 5.5a.7 Branding, Attribution & Trademark
  │   ├─ 5.5a.8 License Perpetuity & Survival
  │   ├─ 5.5a.9 Compliance & Remedies
  │   ├─ 5.5a.10 Transition & Knowledge Transfer
  │   └─ Summary Table: IP Ownership & Usage Rights
  ├─ 5.5b Pricing assumptions (renumbered)           [Page 70]
  └─ 5.6 Deviations and contractual notes            [Page 72]
```

---

## EDITING CHECKLIST FOR AIRPORT_EYE_CONSOLIDATED_PROPOSAL_FINAL.docx.md

### Step 1: Update Table of Contents (Page 5-6)

**Find & Update:**
```
5. Commercial proposal	45

5.1 Pricing principles	45

5.2 Commercial Tables	45

5.2.1 Table 1 - geospatial & survey (Section 2.2)	45
... [tables 2-7]

5.3 Grand total summary	59

5.4 Milestone payment schedule	60

5.5 Pricing assumptions	60

5.6 Deviations contractual notes (commercial)	61

6. Qualifications & references	63
```

**To:**
```
5. Commercial proposal	45

5.1 Pricing principles	45

5.2 Commercial Tables	45

5.2.1 Table 1 - geospatial & survey (Section 2.2)	45
... [tables 2-7]

5.3 Grand total summary	59

5.4 Milestone payment schedule	60

5.5a Licensing & Intellectual Property Framework	61

5.5b Pricing assumptions	71

5.6 Deviations contractual notes (commercial)	72

6. Qualifications & references	83
```

---

### Step 2: Insert Licensing Section After Milestone Payment Schedule

**Find Line:** `## Milestone payment schedule` (around line 1380)

**Add After All Milestone Payment Content (after the payment schedule table):**
```markdown

## Licensing & Intellectual Property Framework

### Scope

[INSERT FULL SECTION 5.5a CONTENT FROM AIRPORT-EYE-LICENSING-SECTION.md]

[... continues through Section 5.5a.10 ...]

[Include Summary Table: IP Ownership & Usage Rights]

```

---

### Step 3: Renumber Remaining Sections

**Find:** Current Section 5.5 heading `## Pricing assumptions`

**Change to:** `## Pricing assumptions (5.5b)` or restructure as `### 5.5b Pricing assumptions`

**Find:** Current Section 5.6 heading `## Deviations contractual notes (commercial)`

**Change to:** `### 5.6 Deviations contractual notes (commercial)`

---

### Step 4: Update Cross-References in Existing Sections

#### In Section 3.4 (AI Governance)

**Current Text (around line 754):**
```
**DIAL ownership:** DIAL owns all AI model weights training data generated under contract (BRD Section 3.5.5). 
The bidder does not use DIAL data train or improve external AI models.
```

**Update To:**
```
**DIAL ownership:** DIAL owns all AI model weights and training data generated under this contract (BRD Section 3.5.5). 
The bidder does not use DIAL data to train or improve external AI models. For comprehensive IP ownership terms and 
licensing restrictions, see Section 5.5a (Licensing & Intellectual Property Framework).
```

#### In Section 5.6 (Deviations)

**Add New Deviation Entry (in the deviations table):**
```markdown
| CC-09 | AIOP platform IP ownership: perpetual licence, no unbundling of components | BRD Section 9.13 (if present) / Commercial Framework | Bidder proposes WAISL perpetual ownership of AIOP platform source code and proprietary algorithms, with DIAL receiving a perpetual, royalty-free, irrevocable licence for exclusive use at IGI Airport. DIAL retains absolute ownership of AI model weights and training data. No unbundling of AIOP components for use in competing systems is permitted. Details in Section 5.5a (Licensing & Intellectual Property Framework). |
```

---

## UPDATED APPENDICES INDEX

### Add to Appendices List (end of proposal):

**Existing:**
```
Annexure K: Compliance & Mandatory Forms, CVs, sub-contractor declarations, ISO certs, SBOM, Clarification Log, Acronyms, Deviation List
```

**Add:**
```
Annexure L: Licensing & Intellectual Property Framework (detailed terms and conditions) [OPTIONAL: if separate volume preferred]

Annexure M: Source Code Escrow Agreement (formal escrow terms, agent details, release triggers, obligations)
```

---

## CONTENT MAPPING: Section 5.5a Subsections

| Subsection | Key Topics | Length | Cross-Reference |
|------------|-----------|--------|-----------------|
| 5.5a.1 | AIOP Platform IP ownership, DIAL's perpetual licence, restrictions, exclusivity | ~800 words | Relates to Section 2.6 (Operational DT), 3.4 (AI governance) |
| 5.5a.2 | Geospatial DT (GEOKNO + ESRI) ownership, DIAL's rights, ESRI renewal responsibility | ~500 words | Relates to Section 2.2–2.4 (Geo DT delivery) |
| 5.5a.3 | DIAL's absolute ownership of AI models, training data, knowledge assets; bidder restrictions | ~700 words | Relates to Section 3.4 (AI governance), BRD 3.5.5 |
| 5.5a.4 | Custom code & integrations ownership model, maintenance obligations | ~600 words | Relates to Section 2.5 (Integrations), 4.1 (implementation) |
| 5.5a.5 | Third-party components, open-source governance, SBOM, ESRI licensing, no GPL copyleft | ~800 words | Relates to Annexure K.6 (SBOM), Section 4.3 (infrastructure) |
| 5.5a.6 | Source code escrow terms, triggers, deliverables, escrow agent, post-release obligations | ~700 words | Annexure M (Escrow Agreement) |
| 5.5a.7 | Branding, attribution, trademark restrictions | ~300 words | Relates to DIAL marketing/comms standards |
| 5.5a.8 | Perpetual grant, term clarity, post-contract support, infrastructure responsibility | ~600 words | Relates to BRD Section 9.12 (exit/transition) |
| 5.5a.9 | Breach remedies, indemnification, insurance, liability cap | ~400 words | Relates to commercial risk framework |
| 5.5a.10 | End-of-contract deliverables, knowledge transfer, transition support, post-contract responsibility | ~500 words | Relates to Section 4.1.4 (transition plan) |
| Summary Table | IP Ownership & Usage Rights matrix (8 components × 6 dimensions) | ~300 words | Summary reference |
| **Total** | | **~6,200 words (~15–18 pages)** | |

---

## INTEGRATION WORKFLOW

### Stage 1: Content Preparation (1–2 hours)
- [ ] Copy Section 5.5a content from `AIRPORT-EYE-LICENSING-SECTION.md`
- [ ] Customize references to match Airport Eye specific terminology (e.g., confirm AIOP/DIAL/WAISL naming)
- [ ] Verify all subsection hyperlinks/cross-references are accurate
- [ ] Review summary table for accuracy

### Stage 2: Structural Edits (1–2 hours)
- [ ] Insert Section 5.5a into Airport Eye proposal after Section 5.4
- [ ] Update Table of Contents numbering
- [ ] Renumber Sections 5.5 → 5.5b and 5.6 onwards
- [ ] Add Annexure L (Licensing Framework) and Annexure M (Escrow Agreement) to appendices index

### Stage 3: Cross-Reference Updates (30–45 minutes)
- [ ] Update AI Governance section (3.4) with reference to Section 5.5a
- [ ] Add CC-09 deviation entry to Section 5.6 deviations table
- [ ] Add Annexure references (L, M) to appendices index
- [ ] Verify all internal hyperlinks resolve correctly

### Stage 4: Legal/Technical Review (2–3 hours)
- [ ] WAISL Legal: Review perpetual licence commitments, escrow terms, data-use restrictions
- [ ] GEOKNO Alignment: Confirm Geospatial DT ownership & licensing language is accurate
- [ ] DIAL Procurement: Review DIAL rights, AI model ownership, third-party renewal responsibility
- [ ] BDDA/Legal: Final legal review for compliance and enforceability

### Stage 5: Formatting & Finalization (30–45 minutes)
- [ ] Ensure consistent markdown formatting (headers, tables, bullet points)
- [ ] Verify page breaks and section flow
- [ ] Proofread for typos and inconsistencies
- [ ] Generate final PDF/DOCX from markdown
- [ ] Add updated page numbers to Table of Contents

**Total Estimated Time: 5–8 hours (including legal reviews)**

---

## KEY STAKEHOLDER ALIGNMENT ITEMS

### For WAISL Internal Sign-Off:

1. ✅ **Perpetual Licence Commitment** (Sections 5.5a.1 & 5.5a.8)
   - Confirms WAISL retains ownership; DIAL receives perpetual, royalty-free usage rights
   - No future monetisation expected post-contract expiry

2. ✅ **Escrow Obligation** (Section 5.5a.6)
   - WAISL commits to source code escrow upon triggering events
   - Confirm board approval and cost allocation

3. ✅ **Data Usage Restriction** (Section 5.5a.3)
   - WAISL restricted from using DIAL data for external AI model training
   - Confirm does not conflict with other WAISL client engagements

4. ✅ **Third-Party Components** (Section 5.5a.5)
   - SBOM audit required to confirm no GPL copyleft exposure in core AIOP
   - Confirm ESRI ArcGIS licensing is valid and current

---

### For DIAL Procurement Sign-Off:

1. ✅ **Perpetual Usage Rights** (Sections 5.5a.1 & 5.5a.8)
   - DIAL retains perpetual licence without additional fees post-Year 5
   - Confirms no surprise licensing costs in Years 6+

2. ✅ **AI Model Ownership** (Section 5.5a.3)
   - DIAL owns all AI models, training data, knowledge assets in perpetuity
   - Aligns with data-sovereignty and AI governance policies (Annexure III)

3. ✅ **Source Code Escrow** (Section 5.5a.6)
   - Formal Escrow Agreement (Annexure M) to be negotiated pre-contract
   - DIAL engagement: select escrow agent, define triggers, cost allocation

4. ✅ **Third-Party Renewal Responsibility** (Section 5.5a.5)
   - ESRI ArcGIS renewal: WAISL during contract, DIAL post-contract
   - Budget provision required for Years 6+ ESRI maintenance

---

## QUICK-REFERENCE LICENSING SUMMARY

### IP Ownership at a Glance

| Who Owns What? | Owner | DIAL's Rights | Perpetual? |
|---|---|---|---|
| **AIOP Platform Code** | WAISL | Exclusive, royalty-free licence for IGI Airport, no resale | ✅ Yes |
| **Geospatial DT Code** | GEOKNO + ESRI | Exclusive, royalty-free licence, expandable to other DIAL properties | ✅ Yes* |
| **AI Model Weights** | DIAL | Absolute ownership, export & retrain freely | ✅ Yes |
| **Training Data** | DIAL | Absolute ownership, use for retraining & analytics | ✅ Yes |
| **Custom Code & Integrations** | WAISL + DIAL licence | WAISL code licensed to DIAL perpetually, no resale without consent | ✅ Yes |

**\*** DIAL responsible for ESRI ArcGIS renewal post-contract.

---

## NEXT STEPS

1. **Copy full Section 5.5a** from `AIRPORT-EYE-LICENSING-SECTION.md` into proposal after Section 5.4
2. **Update Table of Contents** to reflect new section numbering
3. **Add cross-references** in Sections 3.4 and 5.6
4. **Schedule legal review** with WAISL, GEOKNO, and DIAL legal teams
5. **Prepare Annexure M (Escrow Agreement)** for negotiation with DIAL
6. **Finalize SBOM** (Annexure K.6) and confirm GPL compliance
7. **Generate final proposal** with updated page numbers and hyperlinks

---

**Licensing Section Status:** ✅ Ready for Integration  
**File Path:** `/Users/sujoymukherjee/code/doc2md/parse2wiki/AIRPORT-EYE-LICENSING-SECTION.md`  
**Total Content:** ~6,200 words (~15–18 pages)  
**Estimated Integration Time:** 5–8 hours (including reviews)
