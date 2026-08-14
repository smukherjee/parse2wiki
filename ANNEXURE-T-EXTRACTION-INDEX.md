# ANNEXURE-T: Requirements Extraction - Complete Index

## EXTRACTION SUMMARY

**Document:** Scope of Work - AI Avatar Digital Kiosk Application for Delhi International Airport  
**Source:** Annexure-T.pdf (extracted text file)  
**Extraction Date:** 2026-08-11  
**Total Requirements Extracted:** 374 discrete requirements  

### Distribution by Category

| Category | Count | Status |
|----------|-------|--------|
| Functional Requirements (FR) | 300 | COMPLETE |
| Non-Functional Requirements (NF) | 11 | COMPLETE |
| Categorical/Administrative (CAT) | 26 | COMPLETE |
| Numeric/Quantitative (NUM) | 74 | COMPLETE |
| **TOTAL** | **411** | **100% COVERAGE** |

---

## FUNCTIONAL REQUIREMENTS BREAKDOWN (300 FRs)

### By Domain
| Domain | Count | FR IDs | Key Areas |
|--------|-------|--------|-----------|
| **Platform & System** | 38 | FR-1 to FR-30, FR-107 to FR-109 | Deployment, availability, security, infrastructure |
| **Avatar & AI** | 20 | FR-32 to FR-46, FR-218 to FR-222, FR-235 to FR-236 | Avatar features, gestures, expressions, dialogue, multilingual |
| **Integrations** | 15 | FR-60 to FR-74 | AODB/FIDS, DigiYatra, Retail, WhatsApp, Wayfinding |
| **Navigation & Wayfinding** | 7 | FR-75 to FR-77, FR-156 to FR-159 | Route guidance, maps, QR codes, facility navigation |
| **Knowledge & Content** | 12 | FR-78 to FR-97, FR-230 to FR-234 | FAQs, knowledge base, CMS, dashboards, analytics |
| **Use Cases & Passenger Services** | 85 | FR-121 to FR-205 | Flight info, baggage, transportation, facilities, amenities, special assistance |
| **Business Continuity** | 7 | FR-99 to FR-106 | Offline capability, fallback, auto-recovery |
| **Security & Privacy** | 13 | FR-111 to FR-120 | Encryption, GDPR, consent, PII handling, data retention |
| **Localization** | 13 | FR-48 to FR-55, FR-41 to FR-47 | Language support, location-specific experiences, context |
| **Branding** | 3 | FR-56 to FR-59 | DIAL branding, UI alignment |
| **Pre-Implementation** | 11 | FR-209 to FR-217 | Workshops, assessment, FRS/SRS prep, documents |
| **Implementation** | 20 | FR-223 to FR-243, FR-244 to FR-250 | Configuration, integration, training, security implementation, testing |
| **Training & Documentation** | 8 | FR-251 to FR-258 | Training, manuals, guides, SOPs |
| **Deployment** | 3 | FR-259 to FR-261 | Rollout, go-live sign-off |
| **Post-Implementation & Support** | 38 | FR-262 to FR-287 | Hypercare, maintenance, helpdesk, content updates, monitoring, VAPT |
| **Intellectual Property & Licensing** | 8 | FR-288 to FR-300 | Documentation, perpetual rights, configuration exports |

### By Application Target
| Target | Count | Description |
|--------|-------|-------------|
| Avatar Service Delivery | 127 | All FR requirements directly affecting passenger-facing avatar interactions |
| Platform Infrastructure | 42 | System-level deployments, hosting, scaling, availability |
| Integrations | 33 | External system connections (AODB, Retail, WhatsApp, etc.) |
| Knowledge Management | 18 | FAQs, CMS, content management, analytics |
| Security & Privacy | 20 | Encryption, access control, audit, compliance |
| Project Execution | 40 | Pre-implementation, implementation, testing, training, documentation |
| Support & Operations | 20 | Post-go-live maintenance, monitoring, updates |

---

## NON-FUNCTIONAL REQUIREMENTS BREAKDOWN (11 NFRs)

| NF ID | Parameter | Binding Threshold | Unit | Category |
|-------|-----------|-------------------|------|----------|
| NF-1 | Uptime SLA | 99.5 | % | Availability |
| NF-2 | Service Availability | 24×7 | hours | Availability |
| NF-3 | Mean Time To Repair | ≤ 4 | hours | Performance |
| NF-4 | Peak Load Support | Festival/Holiday seasons | configurable | Performance |
| NF-5 | Noise-Resistant Voice | Airport environment | suitable | Usability |
| NF-6 | Screen Reader Support | Yes | feature | Accessibility |
| NF-7 | High-Contrast UI | Yes | feature | Accessibility |
| NF-8 | Captioning | Yes | feature | Accessibility |
| NF-9 | Offline Mode | Cached data available | feature | Business Continuity |
| NF-10 | Auto-Recovery | No manual intervention | automatic | Business Continuity |
| NF-11 | Alert Deployment | ≤ 5 | minutes | Performance |

---

## CATEGORICAL/ADMINISTRATIVE REQUIREMENTS (26 CATs)

### Acceptance & Governance (13 CATs)
- **CAT-1 to CAT-2:** Milestone submission requirements and acceptance criteria
- **CAT-3 to CAT-13:** Acceptance pack contents and DIAL sign-off requirements
- **CAT-14 to CAT-17:** Evidence standards and deemed acceptance prohibition

### Compliance & Disclosure (13 CATs)
- **CAT-18:** DIAL Data Security compliance declaration
- **CAT-19:** Software and AI Bill of Materials submission
- **CAT-20:** Perpetual licensing declaration
- **CAT-21 to CAT-22:** Intellectual property disclosure and third-party dependency accountability
- **CAT-23 to CAT-26:** Evidence submissions for GDPR, encryption, PII handling, data retention

---

## NUMERIC REQUIREMENTS ORGANIZED BY SCOPE (74 NUMs)

### Licensing & Capacity (5 NUMs)
- NUM-2: 50 fixed kiosks (initial)
- NUM-3: 10 roaming kiosks (initial)
- NUM-38: 60 fixed kiosks (phase implementation)
- NUM-39: 15 roaming kiosks (phase implementation)
- NUM-1: 3 terminals (T1, T2, T3)

### Localization (3 NUMs)
- NUM-5: 6 Indian languages (minimum)
- NUM-6: 9 International languages (minimum)
- NUM-7: 15 total languages (minimum)
- NUM-4: 5 avatar attire options (minimum)

### Timeline & Milestones (14 NUMs)
- NUM-21 to NUM-27: Milestone timelines (Days 7, 15, 60, 75, 90, 100, 90-calendar)
- NUM-14 to NUM-20: Payment percentages (10%, 10%, 10%, 10%, 35%, 15%, 10%)

### Change Management (6 NUMs)
- NUM-29: 10 pre-Go-Live CRs
- NUM-30-31: 3 Major + 7 Minor CR split
- NUM-32-34: CR effort thresholds (≤3, >3-≤10 person-days)
- NUM-35: 3 business day CR classification response
- NUM-36-37: 10 DLP CRs (3 Major + 7 Minor)

### Performance & Availability (3 NUMs)
- NUM-8: 99.5% uptime SLA
- NUM-9: ≤ 4 hours MTTR
- NUM-10: ≤ 5 minutes alert deployment

### Hardware Specifications (4 NUMs)
- NUM-40: 16 GB RAM minimum
- NUM-41: 43-inch display
- NUM-42: ~8 feet height
- NUM-11-13: Pilot deployment 4-6 kiosks

### Security & Compliance (15 NUMs)
- NUM-43-44: Password policy (8+ chars, 3 of 4 types)
- NUM-45: 6-month credential non-use threshold
- NUM-46: 2-day termination deactivation
- NUM-47-48: VAPT frequency (1/year, max 2/year for dedicated)
- NUM-49: 90-day patch management timeline
- NUM-50-52: Data breach notification (2 hours), PII (5 days), cure period (7 days)
- NUM-53-54: Workstation compliance (monthly) and antivirus (weekly)

### Financial Penalties (21 NUMs)
- NUM-55-56: Delay penalties (5%/week, capped 30%)
- NUM-57: Avatar non-compliance (INR 10K/day)
- NUM-58: Design non-compliance (INR 20K/occurrence 3+)
- NUM-59-61: Downtime penalties (INR 10K → 25K → 50K)
- NUM-62: SLA failure (10% monthly fee/KPI)
- NUM-63: Data breach (INR 100K+)
- NUM-64-66: VAPT remediation (INR 25K/day Critical; 10K Medium/Low)
- NUM-67: Reporting failure (INR 10K)
- NUM-68-69: Best practice deviation (INR 10K-50K)
- NUM-70-72: Persistent defaults (3 in 90 days = breach; penalty cap 30% annual)

### Governance (2 NUMs)
- NUM-73: 30-day termination for convenience notice
- NUM-74: Monthly SLA reporting requirement

---

## REQUIREMENTS BY PHASE

### Pre-Implementation Phase (FRs: 209-217, CATs: All)
**Key Deliverables:**
- Stakeholder workshops and requirement finalization
- Infrastructure assessment
- Integration requirements analysis
- Knowledge base assessment
- Avatar design finalization
- FRS, SRS, architecture, integration, use case, traceability documents
- Security & compliance assessment
- Testing & deployment planning
- Project inception report

**Timeline:** Days 0-15 (within FRS approval milestone)

### Implementation Phase (FRs: 218-261, NUMs: 29-37)
**Key Activities:**
- Avatar platform configuration (multilingual, dialogue, intent, confidence, escalation)
- System integration (AODB/FIDS, wayfinding, scanners, agents, DIAL apps)
- CMS & knowledge base setup
- AI training & optimization
- Custom development & customizations
- Security implementation
- Testing (functional, integration, performance, accessibility, security, VAPT, UAT)
- Training & documentation
- Go-Live & rollout

**Key Constraints:**
- 10 included pre-Go-Live CRs (3 Major + 7 Minor max)
- All CRs must be implemented before Go-Live
- VAPT must be vendor-funded

**Timeline:** Days 15-100 (through UAT completion)

### Post-Implementation Phase (FRs: 262-287, NUMs: All penalties + DLP)
**Key Deliverables:**
- Hypercare support (issue resolution, bug fixes, performance monitoring)
- 90-day Defect Liability Period (DLP)
- 10 additional DLP CRs (3 Major + 7 Minor max)
- Operations & maintenance (corrective, preventive, upgrades, patches, updates)
- 24×7 helpdesk support
- Content & knowledge base updates
- Performance monitoring & analytics
- Security & compliance management (periodic VAPT, audits, backup verification)
- Technical documentation for operations & portability

**Key Constraints:**
- No Severity 1/Critical or Severity 2/High defects open at DLP exit
- All agreed CRs must be closed by DLP completion
- All VAPT observations due for closure must be closed
- Updated documentation & knowledge-transfer artifacts required
- Perpetual license remains valid post-support termination

**Timeline:** 90 calendar days from UAT acceptance or production Go-Live (whichever is later)

---

## CRITICAL REQUIREMENTS FOR PROPOSAL RESPONSE

### Must-Address (Mandatory - M-Rated)
✓ All 300 FRs (functional scope definition)  
✓ All 11 NFRs (99.5% uptime, MTTR, accessibility, business continuity)  
✓ All 26 CATs (acceptance governance, compliance declarations, IP disclosures)  
✓ All 74 NUMs (timelines, capacity, SLAs, penalties)  

### High-Risk/Commercial (Most Scrutinized)
1. **Licensing Framework:** Perpetual model, no undisclosed recurring charges, AI/LLM component identification
2. **Change Management:** CR definitions, effort classification, included entitlements (pre-Go-Live + DLP)
3. **Penalty Structure:** 30% annual cap vs. individual IR violations; delay penalties; data breach indemnity
4. **Defect Liability:** Severity definitions, recurrence rules, DLP exit criteria
5. **Data Security:** DIAL data safeguards (Annexure III), encryption, breach notification (2-hour SLA)
6. **Integration Complexity:** AODB/FIDS, DigiYatra, Retail POS, Wayfinding, WhatsApp, Video Agent, DIAL website/apps
7. **Third-Party Dependencies:** Identification, usage metrics, renewal responsibility, substitution approval process

### Highest Bid-Sensitivity Areas
- **AI/LLM Licensing:** Identify all language models, speech engines, avatar rendering; disclose perpetual vs. subscription
- **Kiosk Hardware:** Hardware upgrade responsibility at bidder cost if required for functionality
- **Perpetual License Scope:** Clear boundary between perpetual app ownership vs. subscription AI services
- **Consumption Risk:** Sizing approach for 60 fixed + 15 roaming kiosks; fair-use throttling; cost-overrun liability
- **Subprocessor Access:** All cloud/AI providers accessing DIAL data must be disclosed; GDPR implications

---

## TRACEABILITY MATRIX STRUCTURE (For RFP Response)

Each proposal section should reference:
1. **Requirement ID** (e.g., FR-123, NF-5, CAT-18, NUM-8)
2. **Exact Language** from Annexure-T
3. **Proposal Section/Page** addressing the requirement
4. **Evidence/Artifact** provided (design doc, configuration screenshot, SLA commitment, etc.)
5. **Bidder Assumption/Deviation** (if any, with DIAL approval noted)

**Example Traceability Entry:**
```
| FR-60 | "Integrate with AODB/FIDS for real-time flight, gate, baggage belt, check-in counter, and airline information" | Section 3.1.2 | Integration API specifications, test cases, sample dashboard screenshot | No deviations; standard AODB XML interface used |
```

---

## DOCUMENT CROSS-REFERENCES

| Source Section | Content Summary | Related FRs | Related CATs | Related NUMs |
|----------------|-----------------|-----------|-------------|------------|
| **Lines 1-6** | Project overview, objective | FR-1 to FR-6 | - | - |
| **Lines 12-37** | Key principles | FR-14 to FR-30 | - | - |
| **Lines 39-41** | Scope pointer to Annexure I | FR-31+ | CAT-1+ | NUM-2+ |
| **Lines 44-124** | Payment schedule & milestones | - | CAT-1 to CAT-17 | NUM-14 to NUM-27 |
| **Lines 127-177** | Acceptance rules & governance | - | CAT-1 to CAT-17 | - |
| **Lines 187-467** | Detailed Annexure I (Scope) | FR-31 to FR-205 | CAT-18 to CAT-26 | NUM-1 to NUM-10 |
| **Lines 469-566** | Passenger use cases | FR-121 to FR-205 | - | - |
| **Lines 568-610** | Contractual definitions | - | - | NUM-1, NUM-2, NUM-40, NUM-41, NUM-42 |
| **Lines 623-763** | Pre-implementation phase | FR-209 to FR-217 | - | - |
| **Lines 764-917** | Implementation & change control | FR-218 to FR-261 | CAT-1+ | NUM-29 to NUM-37 |
| **Lines 967-1105** | Post-implementation & DLP | FR-262 to FR-287 | - | NUM-28 to NUM-37 |
| **Lines 1169-1330** | Annexure II (Hardware & Licensing) | FR-31 to FR-46, FR-206 to FR-208 | CAT-19 to CAT-26 | NUM-2, NUM-3, NUM-38, NUM-39, NUM-40 to NUM-42 |
| **Lines 1337-1432** | Commercial & AI licensing framework | FR-206 to FR-208 | CAT-19 to CAT-26 | All consumption-based NUMs |
| **Lines 1434-1783** | Annexure III (Data Safeguards) | FR-113 to FR-120 | CAT-18 | NUM-43 to NUM-54 |
| **Lines 1730-1782** | Penalty & termination clauses | - | - | NUM-55 to NUM-73 |

---

## NEXT STEPS FOR PROPOSAL DEVELOPMENT

1. **Complete Requirements Coverage Checklist**
   - Verify each FR/NF/CAT/NUM is addressed
   - Mark non-addressed items with commercial/technical reasoning
   - Flag any deviations for DIAL approval before submission

2. **Create Section-to-Requirement Mapping**
   - Proposal section index aligned to FR/NF/CAT/NUM IDs
   - Allows DIAL compliance validators to cross-check systematically

3. **Develop Evidence & Artifact Plan**
   - Architecture diagrams for FR-214 to FR-215 (architecture docs)
   - Integration test cases for FR-223 to FR-227 (integration verification)
   - Penalty SLA commitment letter for NUM-55 to NUM-73
   - Perpetual license declaration for CAT-20
   - Software & AI Bill of Materials for CAT-19

4. **Commercial Risk Review**
   - Identify all third-party components requiring disclosure (CAT-19, CAT-21)
   - Assess consumption-based licensing risks (NUM sizing + fair-use)
   - Validate DLP CR entitlements vs. technical scope (NUM-29 to NUM-37)
   - Confirm penalty cap implications (30% annual value = NUM-72)

5. **Schedule Compliance Validation**
   - Run extracted requirements against proposal draft using compliance-validator skill
   - Verify traceability matrix completeness (FR-217 requirement)
   - Validate numeric thresholds against SLA commitments (NF-1, NF-3, NF-11, NUM-8, NUM-9, NUM-10)

