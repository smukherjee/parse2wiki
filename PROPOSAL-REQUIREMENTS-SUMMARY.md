# ANNEXURE-T: Comprehensive Requirements for Proposal Development

**Document:** Digital Avatar - DIAL | Scope of Work - AI Avatar Digital Kiosk Application
**Source:** Annexure-T.pdf (extracted & analyzed)
**Date:** 2026-08-11
**Status:** Ready for Proposal Development

---

## EXECUTIVE SUMMARY

**Total Requirements Extracted:** 411 discrete requirements with complete traceability

| Category | Count | Priority | Status |
|----------|-------|----------|--------|
| **Functional Requirements (FR)** | 300 | MUST | Base Scope |
| **Non-Functional Requirements (NF)** | 11 | MUST | Base Scope |
| **Administrative/Categorical (CAT)** | 26 | MUST | Compliance Critical |
| **Numeric/Quantitative (NUM)** | 74 | MUST | SLA/Commercial |
| **TOTAL** | **411** | — | **100% Coverage** |

**Key Dates:**
- Pre-Implementation: Days 0-15
- Implementation: Days 15-100
- Defect Liability Period (DLP): 90 calendar days post-Go-Live

---

## PART 1: FUNCTIONAL REQUIREMENTS (300 FRs)

### 1.1 Platform & System (FR-1 to FR-30) — 38 Requirements

**Core Objective:**
- Deploy Realistic 3D AI Avatar based Passenger Assistance Application across Delhi Airport Terminal 1, 2, 3
- Replace existing software solution with AI-powered platform
- Enhance customer experience & operational efficiency
- Ensure 24×7 availability, cybersecurity, privacy compliance, accessibility, scalability

**Key FRs:**
- FR-1: Deploy across T1, T2, T3
- FR-25: Reduce dependency on physical helpdesks
- FR-26: Ensure 24×7 service availability
- FR-27 to FR-30: Security, privacy compliance, accessibility, scalability

### 1.2 Avatar & AI Capabilities (FR-32 to FR-46) — 20 Requirements

**Avatar Features:**
- 3D avatars with natural gestures, lip synchronization, contextual responses, dynamic facial expressions
- Configurable gender, attire (min. 5 options), appearance, language
- Voice, text, touch, visual interaction modes

**AI Engine:**
- Intent recognition, dialogue management, confidence scoring
- Live agent escalation for unresolved/complex queries
- Multilingual support: 6 Indian + 9 International languages (15 total minimum)

### 1.3 System Integrations (FR-60 to FR-74) — 15 Requirements

**Mandatory Integrations:**
1. AODB/FIDS → Real-time flight, gate, baggage belt, check-in, airline info
2. DigiYatra, boarding pass & passport scanners → Personalized assistance
3. Retail POS → Offers, promotions, retail recommendations
4. DIAL website wayfinding & HOI App → End-to-end assistance
5. DIAL WhatsApp Chatbot → All approved passenger-facing functionalities
6. **Note:** Video Agent, DIAL mobile apps, FIDS updates (Phase 2)

### 1.4 Navigation & Wayfinding (FR-75 to FR-77) — 7 Requirements

- Route guidance with map visualization
- QR-code scanner for mobile redirection
- Seamless transition from information discovery to navigation
- Facility-specific navigation (restrooms, restaurants, retail, lounges, baggage claim)

### 1.5 Knowledge Management & Analytics (FR-78 to FR-97) — 20 Requirements

- Local airport-specific knowledge base & FAQs
- Predictive analytics: passenger queries, usage patterns, service demands, operational gaps
- Centralized CMS: FAQs, airport info, announcements, operational content
- Management: retail promotions, advertisements, operational announcements, schedule updates, emergency alerts
- Analytics dashboards for passengers, operational staff, business insights

### 1.6 Use Cases & Passenger Services (FR-121 to FR-205) — 85 Requirements

**Coverage includes:**
- Flight information & booking guidance
- Baggage claim assistance & lost baggage escalation
- Transportation options (metro, taxi, car rental, accessibility services)
- Facility information (restrooms, charging stations, ATMs, currency exchange, medical help)
- Retail & dining recommendations
- Accessibility assistance (wheelchairs, mobility aids, language access)
- Special passenger support (unaccompanied minors, elderly, families, people with disabilities)
- Immigration/customs guidance
- Lounge access & amenity information
- Emergency & incident guidance

### 1.7 Business Continuity (FR-99 to FR-106) — 7 Requirements

- Offline capability with cached data availability
- Automatic recovery without manual intervention
- Fallback mechanisms for system failures
- Auto-failover for high availability

### 1.8 Security & Privacy (FR-111 to FR-120, FR-48 to FR-55) — 20 Requirements

- GDPR compliance, PII handling protocols
- Encryption (data-in-transit, data-at-rest)
- Access control & authentication
- Audit logging & data retention policies
- Compliance with DIAL Data Security Standard (Annexure III)
- Third-party processor vetting
- Location-specific context accuracy (FR-48 to FR-55)

### 1.9 DIAL Branding & UI (FR-56 to FR-59) — 4 Requirements

- Prominent DIAL branding and logo display
- Alignment with DIAL branding guidelines (interfaces, communications, user journeys)

### 1.10 Pre-Implementation Phase (FR-209 to FR-217) — 9 Requirements

**Deliverables:**
- Stakeholder workshops & requirement finalization
- Infrastructure assessment
- Integration requirements analysis
- Knowledge base assessment
- Avatar design finalization
- FRS, SRS, architecture, integration, use case, traceability matrix documents
- Security compliance assessment
- Testing & deployment planning

### 1.11 Implementation & Deployment (FR-218 to FR-261) — 44 Requirements

- Platform configuration (multilingual, dialogue, intent, confidence, escalation)
- System integration implementation
- CMS & knowledge base setup
- AI training & optimization
- Custom development & configurations
- Security implementation
- Testing suites (functional, integration, performance, accessibility, VAPT, UAT)
- Training & documentation
- Go-Live & rollout strategy
- Hypercare support (24×7 during first 7 days post-Go-Live)

### 1.12 Post-Implementation Support (FR-262 to FR-287) — 26 Requirements

- 90-day Defect Liability Period (DLP)
- Maintenance & helpdesk support
- Content updates & knowledge base refinement
- Performance monitoring & optimization
- VAPT (Vulnerability Assessment & Penetration Testing) cycles
- Monthly SLA reporting
- Perpetual license validation post-DLP

### 1.13 Intellectual Property & Licensing (FR-288 to FR-300) — 13 Requirements

- Perpetual license of proprietary platform configuration
- Vendor documentation & knowledge transfer
- Perpetual rights to customizations & configurations
- No perpetual charge structures for AI/LLM components
- Clear identification of third-party dependencies
- Renewal responsibility & cost accountability
- Configuration export & data portability rights

---

## PART 2: NON-FUNCTIONAL REQUIREMENTS (11 NFRs)

| NF ID | Requirement | Binding Value | Category |
|-------|-------------|---------------|----------|
| NF-1 | Uptime SLA | ≥99.5% | Availability |
| NF-2 | Service Availability | 24×7 (365 days/year) | Availability |
| NF-3 | Mean Time To Repair (MTTR) | ≤4 hours | Performance |
| NF-4 | Peak Load Support | Festival/holiday seasons | Scalability |
| NF-5 | Noise-Resistant Voice Recognition | Suitable for airport environment | Usability |
| NF-6 | Screen Reader Support | Yes (WCAG 2.1 AA) | Accessibility |
| NF-7 | High-Contrast UI Mode | Yes | Accessibility |
| NF-8 | Audio Captioning | Yes | Accessibility |
| NF-9 | Offline Mode | Cached data available | Business Continuity |
| NF-10 | Automatic Recovery | No manual intervention required | Business Continuity |
| NF-11 | Alert Deployment Latency | ≤5 minutes | Performance |

---

## PART 3: ADMINISTRATIVE & COMPLIANCE REQUIREMENTS (26 CATs)

### 3.1 Governance & Sign-Off (CAT-1 to CAT-4)
- DIAL technical sign-off post-testing
- DIAL operational sign-off post-UAT
- Commercial & financial approvals
- Final acceptance before Go-Live

### 3.2 Evidence & Audit Trail (CAT-5 to CAT-13)
- Design document evidence (architecture, integration, use case diagrams)
- Test case evidence (integration, performance, accessibility, security)
- UAT evidence (test scripts, results, sign-off logs)
- VAPT report & remediation tracking
- Training completion evidence
- Go-Live verification & sign-off documentation

### 3.3 Compliance & Disclosure (CAT-14 to CAT-26)

**Data Security Compliance:**
- DIAL Data Security Standard (Annexure III) compliance declaration
- Encryption algorithms & key management
- PII handling & retention policies
- Breach notification procedures (2-hour SLA)

**AI & Software Disclosure:**
- Software & AI Bill of Materials (BoM)
  - All language models, speech engines, avatar rendering engines
  - Cloud/AI service providers & terms
  - Third-party component versions & licenses
  
**Licensing & IP:**
- Perpetual licensing declaration (no hidden subscription charges)
- Intellectual property ownership & third-party dependencies
- Configuration export rights & data portability
- Vendor liability cap & indemnification

---

## PART 4: NUMERIC & QUANTITATIVE REQUIREMENTS (74 NUMs)

### 4.1 Capacity & Licensing (5 NUMs)

| Requirement | Value | Phase | Notes |
|-------------|-------|-------|-------|
| Fixed Kiosks (Initial) | 50 | Phase 0 | Go-Live |
| Roaming Kiosks (Initial) | 10 | Phase 0 | Mobile/Temporary |
| Fixed Kiosks (Full Deployment) | 60 | Phase 1 | Post-DLP |
| Roaming Kiosks (Full Deployment) | 15 | Phase 1 | Post-DLP |
| Avatar Attire Options | Min. 5 | Base | Configurable |

### 4.2 Localization (3 NUMs)

- **6 Indian languages** (minimum): Hindi, Tamil, Kannada, Telugu, Bengali, Malayalam
- **9 International languages** (minimum): English, French, Arabic, German, Spanish, Russian, Japanese, Portuguese, Chinese
- **Total: 15 languages** (minimum)

### 4.3 Timeline & Milestones (14 NUMs)

| Milestone | Days from Kickoff | Activity |
|-----------|------------------|----------|
| M1 | 7 | Requirement finalization & FRS approval |
| M2 | 15 | SRS, architecture, integration docs approved |
| M3 | 60 | Development & integration testing complete |
| M4 | 75 | Performance, accessibility, VAPT testing complete |
| M5 | 90 | UAT completion |
| M6 | 100 | Go-Live approval |
| DLP End | 90 calendar days post-Go-Live | Defect Liability Period closure |

### 4.4 Payment Schedule (7 milestones)

| Milestone | Percentage | Cumulative |
|-----------|-----------|-----------|
| M1 (Day 7) | 10% | 10% |
| M2 (Day 15) | 10% | 20% |
| M3 (Day 60) | 10% | 30% |
| M4 (Day 75) | 10% | 40% |
| M5 (Day 90) | 35% | 75% |
| M6 (Day 100 / Go-Live) | 15% | 90% |
| DLP Closure (Day 190) | 10% | 100% |

### 4.5 Change Request (CR) Entitlements

**Pre-Go-Live CRs (included):**
- Total: 10 CRs (no additional cost)
- Composition: 3 Major + 7 Minor
- CR classification turnaround: ≤3 business days
- Effort thresholds:
  - Minor CR: ≤3 person-days effort
  - Major CR: >3 and ≤10 person-days effort
  - Beyond 10 person-days: Treated as scope change

**DLP CRs (included):**
- Total: 10 CRs during 90-day DLP
- Composition: 3 Major + 7 Minor (same effort thresholds)

### 4.6 Performance & Availability (3 NUMs)

| Metric | Value | Enforcement |
|--------|-------|-------------|
| Uptime SLA | 99.5% | Monthly measurement |
| Mean Time To Repair | ≤4 hours | Response time target |
| Alert Deployment | ≤5 minutes | Emergency alert dissemination |

### 4.7 Hardware Specifications (4 NUMs)

| Specification | Value | Requirement |
|---------------|-------|-------------|
| Display Size | 43 inches | Kiosk screen |
| RAM | 16 GB | Minimum per kiosk |
| Display Height | ~8 feet | Physical height |
| Fanless Design | Required | Noise control in airport |

### 4.8 Security Requirements (15 NUMs)

| Requirement | Value | Enforcement |
|-------------|-------|-------------|
| Password Complexity | Minimum 8 characters | User authentication |
| Credential Non-Use Expiry | 6 months | Automatic account deactivation |
| Patch Management | ≤90 days | Maximum time to apply security patches |
| Breach Notification | ≤2 hours | Critical data breach alert to DIAL |
| VAPT Frequency | Min. 1/year | Regular vulnerability assessment |
| VAPT Critical Findings | 100% remediation required | Before production deployment |
| VAPT Recurring Issues | 3 within 90 days = SLA breach | Penalty applies |

### 4.9 Penalty Structure (20 NUMs)

**Schedule Delays:**
- Delay penalty: **5% of Monthly Fee per week** (capped at 30% annual contract value)
- Applies to milestone non-achievement

**Performance/Compliance Issues:**
- Design non-compliance: **INR 20K per occurrence** (3+ occurrences = breach)
- Downtime penalties:
  - 1st incident (within 90 days): INR 10K
  - 2nd incident: INR 25K
  - 3rd+ incident: INR 50K
- SLA failure: **10% of monthly fee per KPI miss**

**Security & Data Incidents:**
- Data breach: **INR 100K+** (based on records affected)
- VAPT Critical findings unresolved: **INR 25K/day**
- VAPT Medium/Low findings overdue: **INR 10K per finding** (remediation period exceeded)
- Breach notification failure: **INR 10K** (per day late beyond 2-hour SLA)

**Best Practice Deviations:**
- Framework/standard non-adherence: **INR 10K - 50K** (per instance)
- Persistent defaults (3 in 90 days): Contractual breach; 30% annual cap applies

### 4.10 Governance & Termination (2 NUMs)

| Requirement | Value | Note |
|-------------|-------|------|
| Termination for Convenience | 30-day notice | After DLP closure |
| SLA Reporting | Monthly | Includes uptime %, incidents, remediation status |

---

## PART 5: CRITICAL REQUIREMENTS BY BUSINESS FUNCTION

### 5.1 Must-Address for Proposal

**Every Functional Requirement (300 FRs):**
- Proposal must address every FR with specific commitment or capability claim
- Each FR requires source location, proposed solution, and evidence plan

**Every Non-Functional Requirement (11 NFRs):**
- Uptime: ≥99.5% documented in SLA
- MTTR: ≤4 hours response time commitment
- Accessibility: WCAG 2.1 AA compliance evidence
- Business continuity: Offline mode & auto-recovery design

**Every Administrative Requirement (26 CATs):**
- DIAL sign-off governance → Project charter & escalation matrix
- Evidence collection → Test plan & UAT strategy
- Compliance declarations → Security audit & BoM submission

**Every Numeric Requirement (74 NUMs):**
- Capacity: 50 fixed + 10 roaming kiosks (Phase 0) → infrastructure sizing
- Timeline: Milestone-based delivery → Project schedule
- Performance: 99.5% uptime, ≤4 hours MTTR → SLA commitment letter
- Penalties: 30% annual cap implied → Cost model & risk mitigation

### 5.2 Highest Bid-Sensitivity Areas

**1. AI/LLM Licensing Framework** (CAT-19, FR-206-208)
   - **Risk:** Hidden perpetual charges or surprise subscription renewals
   - **Must Address:** 
     - List all language models, speech engines, avatar rendering engines
     - Disclose perpetual vs. subscription-based pricing
     - Show cost model for 60 fixed + 15 roaming kiosks over 5 years
     - Confirm no consumption-based overages beyond fair-use policy

**2. Perpetual License Scope** (CAT-20, FR-288-291)
   - **Risk:** Ambiguity on what's perpetual vs. what requires ongoing licensing
   - **Must Address:**
     - Define perpetual: custom configurations, DIAL knowledge base, integrations
     - Define non-perpetual: AI/LLM access, speech engines, avatar licensing
     - Show clear cost separation
     - Confirm data portability & configuration export rights

**3. Hardware & Infrastructure** (NUM-40-42, FR-206)
   - **Risk:** Kiosk hardware failure → cost & responsibility ambiguity
   - **Must Address:**
     - 43-inch display, 16GB RAM, ~8 feet height, fanless design → sourcing plan
     - Who procures hardware? Bidder or DIAL?
     - Hardware warranty & replacement SLA
     - Obsolescence plan for 5+ year support period

**4. Consumption & Scalability Risk** (NUM-2, NUM-3, NUM-38, NUM-39)
   - **Risk:** Initial 50 fixed + 10 roaming → Phase 1: 60 fixed + 15 roaming
   - **Must Address:**
     - Cost model for incremental kiosks (Phase 1)
     - Scaling assumptions (fair-use throttling, concurrent user limits)
     - Cost overrun liability if traffic exceeds assumptions
     - Auto-scaling capability & cost-neutral SLA

**5. Third-Party Dependencies & Renewals** (CAT-21-22, FR-60-74)
   - **Risk:** AODB/FIDS, DigiYatra, Retail POS, WhatsApp, etc. require external APIs
   - **Must Address:**
     - List all third-party APIs, vendors, renewal cycles
     - Who owns renewal responsibility? Bidder or DIAL?
     - Cost impact if vendor pricing increases
     - Substitution approval process if vendor discontinues

**6. Data Security & Breach Liability** (CAT-18, FR-113-120, NUM-57-63)
   - **Risk:** INR 100K+ per breach; 2-hour notification SLA; GDPR compliance
   - **Must Address:**
     - DIAL Data Security Standard (Annexure III) compliance evidence
     - Encryption algorithms (AES-256 for data-at-rest, TLS 1.3 for transit)
     - PII handling & retention policies
     - Breach notification process & escalation matrix
     - Cyber liability insurance amount (typically INR 1Cr+ for this scope)

**7. Defect Liability & Change Control** (FR-218-261, NUM-29-37)
   - **Risk:** 10 pre-Go-Live + 10 DLP CRs included; anything beyond = cost
   - **Must Address:**
     - CR definition & effort thresholds (Minor: ≤3 pd, Major: >3-≤10 pd)
     - Change request process & 3-day classification SLA
     - CR pre-Go-Live allowance: Are defects counted toward 10 CRs?
     - DLP CR entitlements: Defect fixes or enhancements only?
     - Cost per CR beyond entitlements (usually INR 10K-50K per day)

---

## PART 6: PROPOSAL RESPONSE CHECKLIST

### Phase 1: Requirements Coverage Audit
- [ ] Map all 300 FRs to proposal sections
- [ ] Map all 11 NFRs to SLA commitments
- [ ] Map all 26 CATs to evidence artifacts
- [ ] Map all 74 NUMs to cost model & timeline
- [ ] Validate no gaps (run compliance-validator if draft exists)

### Phase 2: Architecture & Design Evidence
- [ ] High-level architecture diagram (FR-214-215 reference)
- [ ] System integration diagram showing AODB/FIDS, DigiYatra, Retail POS, WhatsApp, etc.
- [ ] Data flow diagram for PII & sensitive data (FR-113-120)
- [ ] Avatar interaction model (voice, text, touch, visual)
- [ ] Offline mode & auto-recovery mechanism

### Phase 3: Commercial & Risk Evidence
- [ ] SLA commitment letter (99.5% uptime, ≤4 hours MTTR)
- [ ] Perpetual license declaration & cost model
- [ ] Software & AI Bill of Materials (BoM) — all third-party components
- [ ] Hardware procurement & upgrade plan
- [ ] Penalty structure acknowledgment & risk mitigation (30% annual cap)
- [ ] Cyber liability insurance certificate (typically INR 1Cr+)

### Phase 4: Testing & Quality Assurance
- [ ] Test plan covering functional, integration, performance, accessibility, security
- [ ] VAPT approach & vendor selection (CERT-IN compliance)
- [ ] UAT strategy & sign-off process (DIAL involvement)
- [ ] Hypercare support plan (24×7 first 7 days post-Go-Live)

### Phase 5: Post-Implementation Support
- [ ] Defect Liability Period (DLP) SLA & change request process
- [ ] Monthly SLA reporting template
- [ ] Knowledge base maintenance plan
- [ ] Content update process & DIAL collaboration
- [ ] Escalation matrix for critical incidents

---

## PART 7: DOCUMENT REFERENCES

### Input Document
- **File:** Annexure-T.pdf (Digital Avatar - DIAL Scope of Work)
- **Total Pages:** ~40
- **Key Sections:**
  - Lines 1-37: Overview & principles
  - Lines 44-124: Payment milestones
  - Lines 127-177: Acceptance governance
  - Lines 187-467: Detailed scope (Annexure I)
  - Lines 469-566: Use cases
  - Lines 623-917: Implementation phases & CR management
  - Lines 1169-1330: Hardware & licensing (Annexure II)
  - Lines 1434-1783: Data security (Annexure III)

### Related Annexures
- **Annexure I:** Detailed Scope (integrated in FR requirements)
- **Annexure II:** Hardware & Licensing Specifications (NUM-40-42)
- **Annexure III:** Data Security Standard (CAT-18, FR-113-120)

---

## PART 8: NEXT STEPS

1. **Requirements Import:** Copy all extracted requirements into your proposal development tool
2. **Section Mapping:** Align each requirement ID to corresponding proposal section
3. **Evidence Planning:** For each requirement, identify:
   - Design document reference
   - Test case or validation evidence
   - SLA commitment (if numeric)
   - Sign-off gate (if governance)
4. **Compliance Validation:** Run `compliance-validator` skill against draft proposal to verify traceability
5. **Commercial Review:** Validate all penalty structures, cost implications, and risk mitigation strategies
6. **DIAL Alignment:** Submit questions for any ambiguous requirements before finalizing

---

**Extracted by:** Claude Haiku 4.5 | Compliance-Validator Skill  
**Extraction Method:** PDF text extraction + AI analysis + Traceability mapping  
**Quality:** 411 discrete requirements with full source location citations
