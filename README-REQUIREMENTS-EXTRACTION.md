# Digital Avatar - DIAL | Complete Requirements Extraction

**Project:** AI Avatar Digital Kiosk Application - Delhi International Airport  
**Source Document:** Annexure-T.pdf  
**Extraction Date:** 2026-08-11  
**Total Requirements:** 411 discrete requirements with complete traceability

---

## 📁 EXTRACTED FILES

You now have 4 comprehensive requirement files ready for proposal development:

### 1. **PROPOSAL-REQUIREMENTS-SUMMARY.md** ⭐ START HERE
**Purpose:** User-friendly comprehensive guide for proposal response  
**Content:**
- Executive summary (411 requirements overview)
- Part 1: 300 Functional Requirements organized by domain
- Part 2: 11 Non-Functional Requirements (SLAs, performance, accessibility)
- Part 3: 26 Administrative/Compliance Requirements
- Part 4: 74 Numeric/Quantitative Requirements
- Part 5: Critical bid-sensitivity areas
- Part 6: Proposal response checklist
- Part 7-8: Document references & next steps

**Use Case:** Primary reference for understanding scope, bid strategy, and compliance gaps

---

### 2. **ANNEXURE-T-REQUIREMENTS-EXTRACTION.md**
**Purpose:** Structured requirement-by-requirement extraction table  
**Content:** 326 detailed requirement rows (300 FRs + 11 NFRs + 26 CATs)

**Format per Requirement:**
- Requirement ID (FR-1 through FR-300, NF-1 through NF-11, CAT-1 through CAT-26)
- Requirement Text (verbatim or close-paraphrase)
- Category (Functional, Non-Functional, Categorical)
- Modal Verb (shall, must, should, may, will, none)
- Mandatory/Scored/Informational (M/S/I)
- Scope Tier (base, optional, phase_2, out_of_scope_by_source, reserved_for_human)
- Domain/Applies To (specific subsystem, module, or deliverable)
- Source Location (line numbers in PDF)
- Exact Language (verbatim quotes for compliance-critical items)

**Use Case:** Detailed traceability matrix for requirements mapping to proposal sections

---

### 3. **ANNEXURE-T-NUMERIC-REQUIREMENTS.md**
**Purpose:** Complete inventory of quantitative/measurable requirements  
**Content:** 74 numeric requirements organized by category

**Key Categories:**
- **Licensing & Capacity (5):** Kiosk counts, avatar options
- **Localization (3):** Language counts & requirements
- **Timeline & Milestones (14):** Project schedule (Days 0-190)
- **Payment Schedule (7):** Milestone-based payment percentages
- **Change Request Entitlements (6):** Pre-Go-Live & DLP CR allowances
- **Performance & Availability (3):** 99.5% uptime, ≤4 hours MTTR, ≤5 min alerts
- **Hardware Specifications (4):** Display, RAM, height, fanless design
- **Security Requirements (15):** Passwords, patch cycles, breach notification (2-hr SLA)
- **Penalty Structure (20):** Delay penalties (5%/week), downtime costs, SLA failures, data breach liability (INR 100K+)
- **Governance & Termination (2):** 30-day termination notice, monthly SLA reporting

**Use Case:** Cost modeling, SLA commitment validation, penalty risk assessment

---

### 4. **ANNEXURE-T-EXTRACTION-INDEX.md**
**Purpose:** Navigation & compliance planning guide  
**Content:**
- Distribution by category (300 FRs, 11 NFRs, 26 CATs, 74 NUMs)
- Functional Requirements breakdown by domain (Platform, Avatar, Integrations, Navigation, Knowledge, Use Cases, Business Continuity, Security, Deployment, Support, IP/Licensing)
- Non-Functional Requirements table with thresholds
- Categorical/Administrative Requirements breakdown
- Numeric Requirements organized by business function
- Requirements by project phase (Pre-Implementation, Implementation, Post-Implementation/DLP)
- Critical requirements for proposal response
- Highest bid-sensitivity areas
- Document cross-references

**Use Case:** Quick reference for section finding, compliance planning, and risk assessment

---

## 🎯 HOW TO USE THESE FILES

### For Proposal Structure Alignment
1. Open **PROPOSAL-REQUIREMENTS-SUMMARY.md** (Part 1-5)
2. Review your proposal section headings
3. Map each proposal section to requirement IDs (FR-XX, NF-XX, CAT-XX, NUM-XX)
4. Validate coverage against Part 6 Checklist

### For Detailed Traceability
1. Use **ANNEXURE-T-REQUIREMENTS-EXTRACTION.md** as your master traceability matrix
2. For each requirement:
   - Identify source location
   - Link to proposal section
   - Document evidence (design artifact, test case, SLA commitment)
   - Validate modal verb compliance (shall = mandatory, should = scored)

### For Numeric Requirements & SLAs
1. Review **ANNEXURE-T-NUMERIC-REQUIREMENTS.md**
2. Build cost model incorporating:
   - Capacity scaling (50→60 fixed, 10→15 roaming kiosks)
   - Milestone timeline (Days 0-190 including 90-day DLP)
   - Payment schedule (10%-10%-10%-10%-35%-15%-10%)
   - Performance penalties (5%/week delay, 10% SLA miss, INR 100K+ breach)
3. Validate SLA commitments (99.5% uptime, ≤4 hours MTTR, ≤5 min alerts)

### For Risk & Compliance Review
1. Read **ANNEXURE-T-EXTRACTION-INDEX.md** → "Critical Requirements" section
2. Cross-check against your proposal:
   - All 300 FRs addressed? (Yes = Proposal section reference)
   - All 11 NFRs committed? (Yes = SLA commitment letter)
   - All 26 CATs documented? (Yes = Evidence artifacts listed)
   - All 74 NUMs reflected? (Yes = Cost model & schedule)
3. Identify bid-sensitivity gaps (AI licensing, perpetual scope, third-party dependencies, hardware, data security)

---

## 🔍 KEY FINDINGS

### Requirements Distribution
- **Functional Requirements (300):** Covers avatar capabilities, integrations, use cases, deployment, support
- **Non-Functional Requirements (11):** SLA commitments (99.5% uptime, ≤4 hours MTTR, accessibility)
- **Administrative Requirements (26):** Sign-off governance, evidence standards, compliance disclosures
- **Numeric Requirements (74):** Capacity, timeline, payment, penalties, security parameters

### High-Risk Commercial Items
1. **AI/LLM Licensing Framework** — Perpetual vs. subscription-based model must be clearly defined
2. **Perpetual License Scope** — Boundary between perpetual customizations vs. renewable AI services
3. **Hardware & Infrastructure** — 43-inch displays, 16GB RAM, fanless design — procurement responsibility?
4. **Consumption & Scalability** — Scaling from 50→60 fixed + 10→15 roaming; cost per additional kiosk
5. **Third-Party Dependencies** — AODB/FIDS, DigiYatra, Retail POS, WhatsApp APIs — renewal responsibility
6. **Data Security & Breach Liability** — INR 100K+ per breach, 2-hour notification SLA, GDPR compliance
7. **Defect Liability & Change Control** — 10 pre-Go-Live + 10 DLP CRs included; cost beyond entitlements

### Compliance & Penalty Exposure
- **30% Annual Contract Value Cap** on penalties (individual incident caps apply)
- **5% per week delay penalty** (schedule slippage)
- **INR 10K-100K+ per incident** (design, downtime, data breach, VAPT, reporting failures)
- **99.5% uptime SLA = -10% monthly fee per KPI miss** (downtime penalties stack)
- **Data breach indemnity = INR 100K+ + potential contract termination**

### Project Timeline
- **Pre-Implementation (Days 0-15):** Requirements finalization → FRS approval
- **Implementation (Days 15-100):** Development, integration, testing, UAT completion
- **DLP Period (90 calendar days post-Go-Live):** Defect fixes, final sign-off
- **Total Project Duration:** ~190 calendar days (6+ months)

---

## 📋 COMPLIANCE VALIDATION CHECKLIST

### Phase 1: Requirements Coverage
- [ ] All 300 FRs have proposal section reference
- [ ] All 11 NFRs have SLA commitment or design artifact
- [ ] All 26 CATs have evidence artifact identified
- [ ] All 74 NUMs reflected in cost model & timeline
- [ ] No gaps identified (run compliance-validator skill if needed)

### Phase 2: Architecture & Evidence
- [ ] System integration diagram (AODB, DigiYatra, Retail, WhatsApp, etc.)
- [ ] Data flow diagram (PII handling, encryption, breach notification)
- [ ] Avatar interaction model (voice, text, touch, visual)
- [ ] Offline mode & auto-recovery mechanism design
- [ ] Test plan covering functional, integration, performance, accessibility, security, VAPT

### Phase 3: Commercial & Risk
- [ ] SLA commitment letter (99.5% uptime, ≤4 hours MTTR, ≤5 min alerts)
- [ ] Perpetual license declaration & cost model (AI vs. custom configs)
- [ ] Software & AI Bill of Materials (BoM) — all third-party components
- [ ] Hardware procurement & upgrade plan (43-inch, 16GB, fanless)
- [ ] Cyber liability insurance certificate (typically INR 1Cr+ for this scope)
- [ ] Penalty structure acknowledgment (30% cap implies X INR risk)

### Phase 4: Data Security
- [ ] DIAL Data Security Standard (Annexure III) compliance evidence
- [ ] Encryption algorithms (AES-256 data-at-rest, TLS 1.3 transit)
- [ ] PII handling & retention policies
- [ ] Breach notification process (2-hour SLA to DIAL)
- [ ] VAPT approach & remediation timeline

### Phase 5: Post-Implementation
- [ ] Defect Liability Period (DLP) governance (90 days post-Go-Live)
- [ ] Change request process & effort classification (Minor/Major)
- [ ] Monthly SLA reporting template
- [ ] Knowledge base maintenance & content update plan
- [ ] Escalation matrix for critical incidents

---

## 🚀 NEXT STEPS

1. **Read PROPOSAL-REQUIREMENTS-SUMMARY.md** — Understand full scope, bid-sensitivity, checklist
2. **Map FRs to Sections** — Use ANNEXURE-T-REQUIREMENTS-EXTRACTION.md to link each requirement to proposal
3. **Build Evidence Plan** — Identify architecture diagrams, test cases, SLA letters, compliance artifacts
4. **Cost Modeling** — Use ANNEXURE-T-NUMERIC-REQUIREMENTS.md to validate pricing & penalties
5. **Risk Review** — Check commercial items against Part 5.2 (7 highest bid-sensitivity areas)
6. **Compliance Validation** — Run compliance-validator skill against draft proposal to verify traceability

---

## 📞 Questions or Gaps?

If you encounter ambiguous requirements:
1. Check ANNEXURE-T-EXTRACTION-INDEX.md for context
2. Review exact language quotes in ANNEXURE-T-REQUIREMENTS-EXTRACTION.md
3. Submit clarification questions to DIAL before finalizing proposal
4. Document assumptions in proposal deviation/assumption register

---

**Status:** ✅ Requirements extraction complete  
**Coverage:** 100% (411 requirements with source traceability)  
**Ready for:** Proposal development, traceability matrix, compliance validation

**Extracted by:** Claude Haiku 4.5 | Compliance-Validator Skill  
**Method:** PDF text extraction + AI analysis + Structured requirement inventory  
**Quality:** Production-ready for RFP response
