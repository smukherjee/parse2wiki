# DXB 3D Digital Twin RFP — Compliance Mapping Matrix

**Purpose:** Proposal team reference guide mapping every RFP requirement to its location, binding strength, and required proposal response format.

**How to Use:** For each requirement row, proposal writers should:
1. Confirm the RFP source (verify the exact language)
2. Determine scope tier (base/optional/phase_2)
3. Draft proposal response in the recommended format
4. Mark completion status in "Proposal Status" column

**Document:** `/Users/sujoymukherjee/code/doc2md/parse2wiki/DXB-COMPLIANCE-MAPPING-MATRIX.md`  
**Last Updated:** 2026-08-10  
**Total Requirements:** 91 unique items across RFP body + 7 annexures

---

## QUICK REFERENCE: Coverage Targets

| Category | Count | Binding | Addressed | Gap | Proposal Must Cover |
|---|---|---|---|---|---|
| **RFP Body FRs/NFRs** | 80 | 100% shall | 67 (84%) | 13 | All 13 gaps |
| **Annexure III (Buyer Questions)** | 43 | 80% shall, 20% should | 15 (35%) | 28 | All 28 questions |
| **Annexure IV (Use Cases)** | 8 | 100% shall | 5.5 (69%) | 2.5 | All 8 use cases |
| **Annexure V (Integrations)** | 17 | 100% shall | 15 (88%) | 2 | All 17 integrations |
| **Annexure VII (Capabilities)** | 23 | 100% shall | 20 (87%) | 3 | All 23 capabilities |
| **TOTAL** | **91** | **—** | **55.5 (61%)** | **35.5** | **All 91 items** |

---

## HOW TO READ THIS MATRIX

Each row contains:

| Column | Meaning | Example |
|---|---|---|
| **Req ID** | Unique requirement ID | FR-001, BU-003, CAP-14 |
| **Requirement** | What the RFP mandates | "Platform shall store all data in UAE datacentre" |
| **RFP Source** | Exact location in source document | Section 4, Paragraph 2.1 OR Annexure III, BU1 |
| **Binding Strength** | Modal verb classification | 🔴 shall (mandatory) / 🟡 should (scored) / 🟢 may (optional) |
| **Scope Tier** | When required | base (now) / optional (bidder choice) / phase_2 (later) |
| **Numeric Value** | If applicable | RTO ≤ 4 hrs, ≥ 99.9% uptime |
| **Proposal Response Format** | How proposal must answer | Commitment / Capability Claim / Deviation Entry / Narrative |
| **Proposal Section** | Where answer should appear | Section 3 "Architecture", Appendix A, etc. |
| **Proposal Status** | Team tracking | ☐ Not Started / ◐ In Progress / ✓ Complete |

---

## MASTER COMPLIANCE MATRIX

### SECTION A: RFP BODY SECTIONS 4–6 (80 FRs/NFRs)

#### Addressed Items (67 requirements) — ✓ COVERED IN PROPOSAL

These 67 items are already addressed in existing proposal materials. Proposal team should **verify** these sections exist and are accurate.

| Req ID | Requirement | RFP Source | Binding | Scope | Proposal Section | Status |
|---|---|---|---|---|---|---|
| FR-001 | Real-time passenger location tracking (curb to gate) | Section 4, "Tracking Requirements" | 🔴 shall | base | Section 3.1 Journey Tracking | ✓ |
| FR-002 | Queue detection & wait-time estimation (±10% accuracy) | Section 4, "Queue Monitoring" | 🔴 shall | base | Section 3.2 Queue Analytics | ✓ |
| FR-003 | Predictive congestion alerts (10–15 min foresight) | Section 4, "Predictive Analytics" | 🔴 shall | base | Section 3.3 Predictive Algorithms | ✓ |
| FR-004 | IoT integration (HVAC, doors, fire alarms, UPS, escalators) | Section 6, "Engineering Use Cases" | 🔴 shall | base | Section 3.8 IoT Integration | ✓ |
| FR-005 | Multi-stakeholder role-based dashboards | Section 4, "Stakeholder Use Cases" | 🔴 shall | base | Section 3.6 Dashboard Framework | ✓ |
| (continues for all 67 addressed items... see archived documents for full list) |

---

#### MISSING Items (13 requirements) — 🔴 PROPOSAL MUST ADD

These 13 items are in the RFP but not yet addressed in proposal materials. **Proposal team must add responses for each.**

| Req ID | Requirement | RFP Source | Binding | Scope | Response Format | Proposal Section TBD | Status |
|---|---|---|---|---|---|---|---|
| FR-006 | Multi-channel passenger notification delivery (real-time push) | Section 4, Paragraph 3.2 | 🔴 shall | base | **Commitment:** "Platform shall deliver [X% within Y seconds]; SLA: [availability ≥Z%]" | Section 3.4 Notification Architecture | ☐ |
| FR-012 | Automated staff rostering/shift optimization based on predicted demand | Section 5, "Predictive Staffing" | 🔴 shall | base | **Commitment:** "Solution shall provide rostering engine with [algorithm type], constraints: [manual override, accuracy targets]" | Section 3.7 Staff Optimization | ☐ |
| FR-023 | Predictive maintenance alerts for airport infrastructure | Section 6, "Engineering Use Cases" | 🔴 shall | base | **Commitment:** "Maintenance prediction models for [HVAC/doors/escalators]; alert thresholds: [trigger conditions]" | Section 3.8 Predictive Maintenance | ☐ |
| FR-028 | Passenger satisfaction measurement (in-situ surveys, post-journey feedback) | Section 4, "KPI Framework" (Item #39) | 🟡 should | optional | **Commitment or Capability Claim:** "Survey mechanism: [embedded surveys / QR-code / post-flight]; response target: [X% adoption]" | Section 3.9 Satisfaction Measurement | ☐ |
| NFR-009 | **Data latency from sensor ≤ [X seconds] end-to-end** | Section 4, "Real-Time Requirements" | 🔴 shall | base | **Commitment:** "Platform shall guarantee end-to-end latency ≤ [N seconds] (p95); measured from [sensor trigger] to [dashboard update]" | Section 4.2 Performance SLAs | ☐ |
| NFR-013 | **System uptime during non-maintenance hours ≥ 99.9%** | Section 5, "Tier 1 Service Definition" | 🔴 shall | base | **Commitment:** "Tier 1 service uptime guarantee: ≥ 99.9% (excluding [maintenance windows, defined herein])" | Section 4.1 Availability SLA | ☐ |
| NFR-015 | **Concurrent transactions per second: ≥ [N]** | Section 5, "Performance SLAs" | 🔴 shall | base | **Commitment:** "Platform shall support minimum [N transactions/sec]; scaling mechanism: [horizontal/vertical]; tested to [peak load scenario]" | Section 4.3 Throughput Capacity | ☐ |
| NFR-020 | **RTO (Recovery Time Objective) ≤ [N hours]** | Section 5, "Business Continuity Requirements" | 🔴 shall | base | **Commitment:** "DR capability: RTO ≤ [4 hours] / RPO ≤ [1 hour]; DR provider: [name], location: [UAE/regional]; tested frequency: [annually]" | Section 5.1 Disaster Recovery | ☐ |
| NFR-021 | **RPO (Recovery Point Objective) ≤ [N minutes]** | Section 5, "Business Continuity Requirements" | 🔴 shall | base | **Commitment:** (Same as NFR-020; include both RTO and RPO numeric values) | Section 5.1 Disaster Recovery | ☐ |
| NFR-026 | **Data residency: UAE datacenter mandate** | Section 4, Glossary "Data Residency" + Annexure III BU1 | 🔴 shall | base | **Commitment:** "All Dubai Airports production data shall reside exclusively in UAE datacentre(s); specific location(s): [Dubai/Abu Dhabi]; backup location: [within UAE / approved external]; no off-shore copies except for [DR only, if approved]" | Section 5.2 Data Residency & Sovereignty | ☐ |
| CAT-005 | Technical architecture documentation (HLD + LLD) | Section 8, "Proposal Deliverables" | 🔴 shall | base | **Deliverable:** "Appendix B: Technical Architecture Diagrams (HLD showing systems/data flows; LLD showing component details)" | Appendix B | ☐ |
| CAT-012 | Disaster recovery plan with RTO/RPO SLAs | Section 8, "Mandatory Attachments" | 🔴 shall | base | **Deliverable:** "Appendix C: Disaster Recovery Plan (DR trigger conditions, failover procedures, RTO/RPO testing schedule, DR provider certification)" | Appendix C | ☐ |
| CAT-014 | Support model + training documentation | Section 8, "Support & Training Requirements" | 🔴 shall | base | **Deliverable:** "Appendix D: Support & Training Plan (support levels L1/L2/L3, SLA response times, training curriculum, knowledge transfer schedule)" | Appendix D | ☐ |

---

### SECTION B: ANNEXURE III — NON-FUNCTIONAL COMPLIANCE QUESTIONNAIRE (43 Questions)

**Coverage:** 15/43 answered (35%) | **Gap:** 28 questions need proposal responses

The buyer has provided a structured questionnaire in Annexure III. Proposal must answer **every question** or list as deviation.

#### Solution Architecture (SA1–SA5): 2/5 Covered

| Q ID | Question | RFP Source | Binding | Scope | Response Required | Proposal Section | Status |
|---|---|---|---|---|---|---|---|
| SA1 | Provide technical setup diagram (logical + integration architecture) | Annexure III, SA1 | 🟡 should | base | **Proposal Narrative + Diagrams:** "Provide [logical architecture diagram showing system tiers]; [integration points with CCTV, AODB, Collins, etc.]" | Appendix B Technical Architecture | ☐ |
| SA2 | Subcontractor/multi-supplier elements; end-to-end solution integrity | Annexure III, SA2 | 🟡 should | base | **Proposal Narrative:** "Solution composition: [Waisl core modules: X, Y, Z]; [third-party integrations: Genetec, Xovis, etc.]; [RACI for each component]" | Section 2 Solution Overview | ☐ |
| SA3 | Provide 36-month roadmap | Annexure III, SA3 | 🟢 may | optional | **Capability Claim or Roadmap:** "Available: [phased feature roadmap]; [post-implementation enhancements]" | Appendix E Product Roadmap | ◐ |
| SA4 | Configurable solution elements | Annexure III, SA4 | 🔴 shall | base | **Commitment:** "Platform supports low-code configuration of [business rules, workflows, dashboards, KPI calculations]; no custom coding required for [standard use cases]" | Section 3.5 Business Rules Engine | ✓ |
| SA5 | Demonstrate multi-org data/rule isolation | Annexure III, SA5 | 🟡 should | base | **Commitment + Narrative:** "Multi-org support: [separate data schemas / application-level RBAC]; org-level business rules isolated via [mechanism]; proven at [X deployments]" | Section 5.4 Multi-Tenancy Isolation | ☐ |

**ACTION:** Answer SA1, SA2, SA3, SA5; verify SA4 existing content.

---

#### Scalability (SC1–SC5): 1/5 Covered

| Q ID | Question | RFP Source | Binding | Scope | Response Required | Proposal Section | Status |
|---|---|---|---|---|---|---|---|
| SC1 | Horizontal scalability to meet DA's growing needs | Annexure III, SC1 | 🟡 should | base | **Capability Claim:** "Architecture: [cloud-native / Kubernetes / horizontal scaling]; proven scaling: [X→Y throughput increase without redesign]" | Section 4.3 Scalability Architecture | ✓ |
| SC2 | Max database size; scalability mechanisms; capacity cost structure | Annexure III, SC2 | 🟡 should | base | **Commitment + Numeric:** "Max database size supported: [≥ X TB]; scaling approach: [vertical + horizontal]; cost per additional capacity: [Y per TB/month]" | Section 5.5 Capacity Planning | ☐ |
| SC3 | Multi-tenancy elasticity; peak-load protection mechanisms | Annexure III, SC3 | 🟡 should | base | **Commitment:** "Peak-load handling: [auto-scaling triggers], [SLA during peak hours ≥99%]; elasticity tested to [X concurrent users]" | Section 4.1 Availability SLA | ☐ |
| SC4 | Resilience options; trade-offs analysis; UX continuity during failure | Annexure III, SC4 | 🟡 should | base | **Proposal Narrative:** "Resilience options: [Option A: active-active, RTO 0; Option B: active-passive, RTO 4 hrs]; tradeoffs: [cost, complexity, latency]" | Section 5.1 Disaster Recovery | ☐ |
| SC5 | Dynamic subscription changes; cost structure; minimum increments | Annexure III, SC5 | 🟡 should | base | **Commitment + Pricing:** "Subscription flexibility: [mid-contract user changes allowed]; cost model: [per-user or per-transaction]; minimum increment: [≥1 user]; pricing effective date: [within 30 days]" | Section 7 Commercial Terms | ☐ |

**ACTION:** Answer SC2, SC3, SC4, SC5; verify SC1 existing content.

---

#### Hosting/Data/Backup/Recovery (BU1–BU20): 3/20 Covered

**⚠️ CRITICAL SECTION — Most gaps concentrated here**

| Q ID | Question | RFP Source | Binding | Scope | Response Required | Proposal Section | Status |
|---|---|---|---|---|---|---|---|
| BU1 | **UAE datacentre residency (GOVERNMENT MANDATE)** | Annexure III, BU1 | 🔴 shall | base | **CRITICAL Commitment:** "✓ Confirmed: All Dubai Airports production data shall reside in UAE datacentre(s). Specific DC location(s): [List]; Backup DC: [UAE / regional]; no off-shore data copies except [DR location if approved by buyer]." | Section 5.2 Data Residency | ☐ |
| BU2 | Backup schedule; frequency (daily/weekly/monthly) | Annexure III, BU2 | 🔴 shall | base | **CRITICAL Commitment:** "Backup frequency: [incremental daily, full weekly]; retention: [X days]; backup location: [same DC / different region]" | Section 5.1 Backup SLAs | ☐ |
| BU3 | Backup & restore capabilities; time periods for recovery | Annexure III, BU3 | 🔴 shall | base | **CRITICAL Commitment:** "Backup restoration SLA: [restore time ≤ Y hours]; tested frequency: [annually]; restore procedure: [documented, practiced]" | Section 5.1 Backup SLAs | ☐ |
| BU4 | Full system restore capability; timeline | Annexure III, BU4 | 🔴 shall | base | **CRITICAL Commitment:** "Full system restore: [supported from all backup points]; timeline: [≤ Z hours from backup trigger]; data validation: [post-restore verification]" | Section 5.1 Backup SLAs | ☐ |
| BU5 | Disaster recovery approach; geographic separation | Annexure III, BU5 | 🔴 shall | base | **CRITICAL Commitment:** "DR approach: [active-active / active-passive]; geographic separation: [DR DC location—name it]; RTO: [≤ N hours]; RPO: [≤ M minutes]" | Section 5.1 Disaster Recovery | ☐ |
| BU6 | Referential integrity enforcement mechanism | Annexure III, BU6 | 🟡 should | base | **Commitment:** "Data integrity: [database-level foreign keys / application-level referential integrity]; validation: [frequency of consistency checks]" | Section 5.3 Data Quality | ☐ |
| BU7 | Data/API rate-limiting; threshold notifications | Annexure III, BU7 | 🟡 should | base | **Commitment:** "Rate limiting: [per-API limits: X calls/sec]; alerting: [when threshold at Y% utilization]; escalation: [buyer notification at Z%]" | Section 4.4 API Limits & Quotas | ☐ |
| BU8–BU10 | Data archiving, purging, permanent deletion governance | Annexure III, BU8–BU10 | 🟡 should | base | **Proposal Narrative:** "Data lifecycle: [archive after X months]; deletion: [hard-delete after Y months]; retention compliance: [GDPR / UAE data protection law]" | Section 5.6 Data Lifecycle | ☐ |
| BU11 | Data version control; asset restoration | Annexure III, BU11 | 🟡 should | base | **Capability Claim:** "Version history: [available for [configuration / reference data]]; full data versioning: [not part of base offering; Phase 2 option]" | Section 3.5 Business Rules Engine | ◐ |
| BU12 | Physical backup DC location(s) | Annexure III, BU12 | 🟡 should | base | **Commitment:** "Backup datacentre location(s): [name specific facility / geography]; distance from primary DC: [≥ X km]" | Section 5.1 Backup SLAs | ☐ |
| BU13–BU15 | Infrastructure subcontractors; encryption; key management; change control | Annexure III, BU13–BU15 | 🟡 should | base | **Proposal Narrative:** "Subcontractors: [list]; encryption approach: [AES-256 at-rest, TLS in-transit]; key management: [HSM / AWS KMS / internal]; change control: [documented, audited]" | Section 5.7 Security & Encryption | ☐ |
| BU16 | **DR provider + location + RTO/RPO certifications** | Annexure III, BU16 | 🔴 shall | base | **CRITICAL Commitment + Disclosure:** "Disaster Recovery Provider: [Name]; Location: [City, Country]; Certified RTO: [N hours]; Certified RPO: [M minutes]; audit frequency: [annual]" | Section 5.1 Disaster Recovery | ☐ |
| BU17 | Data retention after contract termination; cost | Annexure III, BU17 | 🟡 should | base | **Commitment:** "Post-termination data handling: [deleted within X days / archived for Y months / returned to buyer]; cost: [included in termination / additional fee]" | Section 7 Commercial Terms | ☐ |
| BU18 | Data format: proprietary vs. open sources | Annexure III, BU18 | 🟡 should | base | **Commitment:** "Data storage format: [X% proprietary, Y% open-source]; export capability: [standard formats: CSV, JSON, Parquet]" | Section 5.8 Data Portability | ☐ |
| BU19–BU20 | Regular audit access & data accessibility testing; test frequency | Annexure III, BU19–BU20 | 🟡 should | base | **Commitment:** "Audit access: [buyer can request data export]; testing: [annual accessibility audit]; compliance certification: [SOC 2 Type II / ISO 27001]" | Section 5.8 Audit & Compliance | ☐ |

**ACTION:** Answer ALL 17 BU questions; BU1, BU5, BU16 are CRITICAL BLOCKING items.

---

#### System Integration (IN1–IN8): 4/8 Covered

| Q ID | Question | RFP Source | Binding | Scope | Response Required | Proposal Section | Status |
|---|---|---|---|---|---|---|---|
| IN1 | Integration with Tableau, Splunk, Kofax, Box | Annexure III, IN1 | 🟡 should | optional | **Capability Claim or Roadmap:** "Third-party integrations: [Tableau: available in Phase 1 / Phase 2]; [Splunk: via syslog export]; [Kofax: scheduled Q3 2027]; [Box: available on request]" | Section 3.10 Third-Party Integrations | ☐ |
| IN2–IN3 | Data migration/export mechanisms | Annexure III, IN2–IN3 | 🟡 should | base | **Commitment:** "Data export: [batch export to CSV/JSON]; migration tools: [documented ETL for legacy systems]; time to export: [≤ X hours for Y GB]" | Section 5.8 Data Portability | ✓ |
| IN4 | **Per-interface fees; API call limits; bandwidth overage costs** | Annexure III, IN4 | 🟡 should | base | **CRITICAL Pricing Transparency:** "API pricing: [per-interface fee: $X/month]; API call limits: [Y calls/second, Z calls/day]; overage: [$A per 1M calls]; bandwidth: [$B per GB over Q GB/month]" | Section 7 Commercial Terms | ☐ |
| IN5–IN6 | Data sharing with other DA organizations (holding co., subsidiaries) | Annexure III, IN5–IN6 | 🟡 should | base | **Commitment or Capability Claim:** "Multi-org data sharing: [API-based data federation]; governance: [shared reference data / separate operational data]; approval: [buyer-controlled access lists]" | Section 5.4 Multi-Tenancy | ◐ |
| IN7 | Developer APIs; integration services | Annexure III, IN7 | 🔴 shall | base | **Commitment:** "RESTful APIs: [publicly documented]; integration services: [standard middleware]; sandbox environment: [available for testing]" | Section 3.10 APIs & Integration | ✓ |
| IN8 | Typical integration architecture; cost per interface | Annexure III, IN8 | 🟡 should | base | **Proposal Narrative:** "Integration architecture: [ESB / point-to-point / hybrid]; typical cost per interface: [labor + licensing]; timeline: [X weeks per integration]" | Section 3.10 Integration Approach | ☐ |

**ACTION:** Answer IN1, IN4, IN8; verify IN2–IN3, IN7; clarify IN5–IN6.

---

#### Performance/Availability (PF1–PF7): 1/7 Covered

| Q ID | Question | RFP Source | Binding | Scope | Response Required | Proposal Section | Status |
|---|---|---|---|---|---|---|---|
| PF1 | Software release process; availability impact during patching | Annexure III, PF1 | 🟡 should | base | **Proposal Narrative:** "Release cadence: [monthly / quarterly]; patching windows: [X hours per release]; availability during patching: [zero-downtime / planned maintenance window: date/time]" | Section 6 Change Management | ☐ |
| PF2 | **Concurrent user capacity limits** | Annexure III, PF2 | 🟡 should | base | **Commitment:** "Concurrent user baseline: [≥ 500 simultaneous users guaranteed]; scaling: [additional licenses available]; peak testing: [tested to X concurrent users]" | Section 4.3 Throughput Capacity | ☐ |
| PF3 | Performance monitoring dashboard; user visibility; SLA dashboards | Annexure III, PF3 | 🟡 should | base | **Commitment:** "SLA compliance dashboard: [real-time visibility]; available to: [AOCC team]; metrics: [uptime %, API latency, response times]; refresh: [every X minutes]" | Section 3.6 Monitoring Dashboards | ☐ |
| PF4 | SLA compliance across geographies + network edge | Annexure III, PF4 | 🟡 should | base | **Commitment or Capability Claim:** "Geographic SLAs: [guaranteed at [datacentre location]]; edge network: [CDN partner / local caching]; latency at edge: [≤ Y ms]" | Section 4.2 Performance SLAs | ✓ |
| PF5 | Performance tuning measures; responsibility; cost | Annexure III, PF5 | 🟡 should | optional | **Proposal Narrative:** "Performance tuning: [included in support / additional service]; cost model: [fixed annual / hourly consulting]; responsibility: [Waisl / buyer / shared]" | Section 7 Commercial Terms | ☐ |
| PF6 | Analytical tools available to users | Annexure III, PF6 | 🟡 should | base | **Capability Claim:** "User-facing tools: [embedded dashboards, reporting, what-if simulation]; export: [CSV, PowerPoint, PDF]; data access: [self-service / through AOCC admin]" | Section 3.6 Dashboards & Reports | ◐ |
| PF7 | **Standard SLA offers** | Annexure III, PF7 | 🔴 shall | base | **Commitment + Numeric:** "Standard SLA tiers: [Tier 1: ≥99.9% uptime + RTO ≤4hrs]; [Tier 2: ≥99.5% uptime + RTO ≤8hrs]; SLA credit: [automatic 1% discount per 0.1% variance below target]" | Section 4.1 Availability SLAs | ☐ |

**ACTION:** Answer PF1, PF2, PF3, PF5, PF7; verify PF4, PF6.

---

#### Usability/Compatibility (UC1–UC12): 1/12 Covered

| Q ID | Question | RFP Source | Binding | Scope | Response Required | Proposal Section | Status |
|---|---|---|---|---|---|---|---|
| UC1–UC2 | Browser + mobile OS support matrix | Annexure III, UC1–UC2 | 🟡 should | base | **Commitment:** "Browser support: [Chrome, Firefox, Safari, Edge — latest 2 versions]; mobile: [iOS Safari, Android Chrome]; tested platforms: [list specific versions]" | Section 3.6 UI/Compatibility | ☐ |
| UC3 | Concurrent edit conflict resolution (2 users editing same data) | Annexure III, UC3 | 🟡 should | base | **Commitment:** "Conflict handling: [last-write-wins / optimistic locking / manual resolution]; user notification: [conflict alert sent within X minutes]" | Section 3.6 Data Consistency | ☐ |
| UC4 | Required plugins (Flash, etc.); version support | Annexure III, UC4 | 🟢 may | optional | **Capability Claim:** "Browser plugins required: [none; 100% web-based]; legacy support: [available via [deprecated feature]]" | Section 3.6 UI Technology | ◐ |
| UC5 | Device usage limitations (iPhone/iPad/desktop licensing) | Annexure III, UC5 | 🟡 should | optional | **Proposal Narrative:** "Licensing model: [per-user / per-device]; device limits: [user can access via X devices]; restriction: [none / [location-based / concurrent-session limit]]" | Section 7 Commercial Terms | ☐ |
| UC6 | Mobile device data deletion policy | Annexure III, UC6 | 🟡 should | base | **Commitment:** "Mobile data deletion: [auto-delete cached data after X days / on logout]; buyer control: [MDM integration available]; encryption: [data encrypted at rest on device]" | Section 5.7 Security | ☐ |
| UC7 | **Accessibility compliance (WCAG)** | Annexure III, UC7 | 🟡 should | base | **Commitment:** "Accessibility compliance: [WCAG 2.1 Level AA / AAA]; audit: [annual third-party accessibility audit]; assistive tech: [screen reader support, keyboard navigation tested]" | Section 3.6 Accessibility | ☐ |
| UC8 | Training/admin support levels; service desk scope | Annexure III, UC8 | 🟡 should | base | **Commitment:** "Training: [initial training: X hours]; admin support: [L1/L2/L3 support tiers]; response times: [critical: X hours, normal: Y hours]" | Section 6 Support & Training | ☐ |
| UC9–UC11 | **Multi-language support (English + Arabic); RTL support** | Annexure III, UC9–UC11 | 🟡 should | base | **Commitment:** "Languages: [English, Arabic supported]; RTL rendering: [✓ native RTL support for Arabic]; date formats: [localized per language]; tested: [both LTR and RTL end-to-end]" | Section 3.6 Internationalization | ☐ |
| UC12 | User personalization (profile settings, preferences) | Annexure III, UC12 | 🟢 may | optional | **Capability Claim:** "Personalization: [user preferences for dashboard layout, theme, language]; saved profiles: [per user]" | Section 3.6 User Preferences | ◐ |

**ACTION:** Answer UC1–UC3, UC5–UC9; verify UC4, UC12; UC7 is HIGH-RISK.

---

#### Ownership & Security (OS1–OS17): 2/17 Covered

| Q ID | Question | RFP Source | Binding | Scope | Response Required | Proposal Section | Status |
|---|---|---|---|---|---|---|---|
| OS1 | Data ownership; customer retains all rights | Annexure III, OS1 | 🔴 shall | base | **Commitment:** "✓ Confirmed: All data collected by platform is owned exclusively by Dubai Airports. Waisl has [no ownership rights / read-only access for support purposes only]. Data use: [only for contracted services]." | Section 5.2 Data Ownership | ☐ |
| OS2–OS3 | **Multi-tenant data isolation; RBAC granularity** | Annexure III, OS2–OS3 | 🟡 should | base | **Commitment:** "Data isolation: [database-level schema separation / row-level security]; RBAC: [role hierarchy levels: X]; testing: [cross-tenant audit testing performed annually]" | Section 5.4 Multi-Tenancy | ☐ |
| OS4–OS5 | Cloud security model; audit capabilities | Annexure III, OS4–OS5 | 🟡 should | base | **Commitment:** "Security model: [shared responsibility model defined]; audit scope: [application-level / infrastructure-level / both]; audit trails: [queryable by buyer]" | Section 5.7 Security | ✓ |
| OS6 | Audit data contribution to user allowance/quota | Annexure III, OS6 | 🟡 should | optional | **Proposal Narrative:** "Quota model: [audit logs count against / separate from user data quota]; pricing: [included in base / additional charge]" | Section 7 Commercial Terms | ☐ |
| OS7–OS8 | **Audit trail visibility; retention periods** | Annexure III, OS7–OS8 | 🟡 should | base | **Commitment:** "Audit logging: [who/what/when/where/why captured]; retention: [X months for operational, Y months for compliance audit]; searchability: [by user/timestamp/entity/action]" | Section 5.7 Audit Trails | ☐ |
| OS9–OS10 | Collaboration data retention; data-allowance composition | Annexure III, OS9–OS10 | 🟡 should | optional | **Proposal Narrative:** "Data quota: [calculation: user data + shared data / user data only]; retention after deletion: [purged immediately / X-day soft-delete window]" | Section 7 Commercial Terms | ☐ |
| OS11 | **Geographic data location choice** | Annexure III, OS11 | 🟡 should | base | **Commitment:** (Same as BU1 — tie to UAE DC residency mandate) "Data geography: [UAE only] / [buyer choice of [UAE/regional/hybrid]]" | Section 5.2 Data Residency | ☐ |
| OS12–OS17 | **SSO/MFA; IDP/LDAP; Okta integration** | Annexure III, OS12–OS17 | 🟡 should | base | **Commitment:** "Authentication: [SSO support via [SAML/OpenID]]; MFA: [✓ supported]; directory integration: [LDAP/Active Directory/Okta]; provisioning: [Just-In-Time / pre-provisioned]" | Section 5.7 Identity Management | ☐ |

**ACTION:** Answer OS1, OS2–OS3, OS6–OS12; verify OS4–OS5; OS1 and OS11 are CRITICAL for sovereignty.

---

### SECTION C: ANNEXURE IV — USE CASE COMPLIANCE MATRIX (8 Use Cases)

**Coverage:** 5.5/8 addressed (69%) | **Gap:** 2.5 use cases need deeper detail

Proposal must score each use case as: **Comply / Partially Comply / Do Not Comply**

| Use Case ID | Use Case Title | RFP Stakeholders | Success Criteria | Proposal Must Include | Proposal Status |
|---|---|---|---|---|---|
| **A1** | End-to-end passenger tracking (curb→gate) | AOCC, GDRFA, Terminal Ops | Journey visibility, queue detection, congestion alerts | ✓ How platform tracks passengers through each stage; accuracy targets (≥99%); integration points (AODB, video, Wi-Fi) | ✓ COVERED |
| **A2** | Passenger identity + baggage linkage | AOCC, GDRFA, Customs | Transfer visibility, baggage tracking, boarding readiness | ⚠ Add: Specific identity correlation method; baggage tracking accuracy; transfer scenario detail (e.g., connecting pax vs. originating) | ◐ PARTIAL |
| **A3** | Security monitoring + intrusion detection | Police, GDRFA, Security | Anomaly detection, unattended baggage, false-positive rates | ⚠ Add: False-positive SLA (target false-positive rate ≤ X%); evidence retention (video clip retention for security); escalation workflow timing | ◐ PARTIAL |
| **A4** | Disruption management + resource optimization | AOCC, Airlines, dnata | Unified operational view, predictive bottlenecks, recovery coordination | ✓ How platform predicts disruption (algorithms); resource recommendations (staffing, gates); recovery SLA | ✓ COVERED |
| **A5** | Stakeholder-specific use cases + KPI framework | All stakeholders | Role-based dashboards, measurable outcomes, adoption | ⚠ Add: KPI calculation logic for each stakeholder; how outcomes are measured (automated vs. manual); adoption targets | ◐ PARTIAL |
| **A6** | Commercial analytics + concession intelligence | Commercial, DDF | Footfall analytics, dwell tracking, conversion attribution | ⚠ Add: Attribution model for conversion tracking (e.g., how platform links passenger visit to retail purchase); accuracy targets; privacy considerations | ◐ PARTIAL |
| **A7** | Engineering + asset health monitoring | Engineering, AOCC, Facilities | Asset condition monitoring, predictive maintenance, incident response | ⚠ Add: Predictive maintenance thresholds (e.g., temperature alert levels); asset types covered (HVAC, doors, escalators, etc.); incident detection latency SLA | ◐ PARTIAL |
| **A8** | Scalability + extensibility | Dubai Airports enterprise | Low-effort onboarding of new systems, rules, dashboards | ⚠ Add: Effort estimate for onboarding new data source (hours/days); configuration complexity (low-code vs. custom dev); time-to-live for new KPI | ◐ PARTIAL |

**ACTION:** Deepen A2, A3, A5, A6, A7, A8 responses; verify A1, A4.

---

### SECTION D: ANNEXURE V — SYSTEM INTEGRATION REGISTER (17 Integrations)

**Coverage:** 15/17 addressed (88%) | **Gap:** 2 critical systems (Kayvan, RealTimeDXB)

Proposal must describe integration approach for each system.

| Integration ID | System/Source | Binding | Integration Type | Current Status | Proposal Must Address | Proposal Status |
|---|---|---|---|---|---|---|
| INT-01 | CCTV / Camera Feeds | 🔴 shall | Video ingest | ✓ Video analytics via IP cameras | Confirm feed formats (RTSP/ONVIF), latency target, camera resolution requirements | ✓ |
| INT-02 | **Kayvan Airside Maps** | 🔴 shall | Airside visualization data | 🔴 **GAP** | **CRITICAL:** How will airside passenger tracking be visualized? Native Kayvan integration or fallback to 2D/3D-only? Timeline for integration? | ☐ BLOCKED |
| INT-03 | Platform Outbound Data Exchange | 🔴 shall | Data export/API | ✓ ESB, APIs, file export | Confirm export formats (CSV, JSON, Parquet), refresh intervals, data lineage | ✓ |
| INT-04 | Genetec SDK (video management) | 🔴 shall | Video archive/evidence | ✓ Genetec integration | Confirm video archive access, evidence chain of custody, retention SLAs | ✓ |
| INT-05 | LiDAR sensors | 🔴 shall | People counting | ✓ LiDAR data ingest | Confirm sensor types supported, accuracy thresholds, latency | ✓ |
| INT-06 | Xovis overhead thermal sensors | 🔴 shall | Queue/occupancy monitoring | ✓ Xovis integration | Confirm coverage areas, accuracy targets, escalation triggers | ✓ |
| INT-07 | AODB (Airport Operational Database) | 🔴 shall | Flight data source | ✓ AODB via Collins APIs | Confirm data refresh rate, fields captured (TTOT, CTOT, gate assignment), SLA for data accuracy | ✓ |
| INT-08 | Quintiq / QRMS (resource management) | 🔴 shall | Staff scheduling | ✓ QRMS integration | Confirm data exchange (crew, gate agents, baggage handlers), real-time sync capability | ✓ |
| INT-09 | Passenger Flow Model (predictive) | 🔴 shall | Flow prediction engine | ✓ Internal analytics module | Confirm prediction horizon (10–15 min), accuracy targets, continuous learning | ✓ |
| INT-10 | Assaia AI (baggage/gate intelligence) | 🔴 shall | Baggage & gate insights | ✓ Assaia APIs | Confirm data types (baggage handling time, boarding times), accuracy SLAs | ✓ |
| INT-11 | **RealTimeDXB / A-CDM / ATFM** | 🔴 shall | Existing SSOV platform | 🔴 **CONFLICT** | **CRITICAL ARCHITECTURAL DECISION:** Will Digital Twin subsume RealTimeDXB data, operate in parallel, or consume it as a data source? How will users transition? Timeline? | ☐ BLOCKED |
| INT-12 | FIDS / Community App / Communication | 🔴 shall | Passenger information display | ✓ FIDS data + mobile app integration | Confirm message delivery SLA, multi-language support (Arabic), real-time updates | ✓ |
| INT-13 | Biometric / BioHub / GDRFA | 🔴 shall | Identity & border control | ✓ Biometric data integration | Confirm privacy compliance, data retention, facial recognition policy (if used) | ✓ |
| INT-14 | BHS / BRS / Airline Operations | 🔴 shall | Baggage handling systems | ✓ Baggage system integration | Confirm baggage sortation data, claim accuracy, handoff timing | ✓ |
| INT-15 | BMS / IoT / HVAC Systems | 🔴 shall | Facility monitoring | ✓ IoT sensor integration | Confirm sensor types, alert thresholds, escalation protocols | ✓ |
| INT-16 | MS Teams / Communication Tools | 🔴 shall | Stakeholder alerts | ✓ Teams integration | Confirm message routing, escalation levels, notification SLAs | ✓ |
| INT-17 | ESB / APIs (internal/external) | 🔴 shall | Data sharing backbone | ✓ RESTful APIs | Confirm API rate limits, latency SLAs, documentation completeness | ✓ |

**ACTION:** Resolve INT-02 (Kayvan) and INT-11 (RealTimeDXB) conflicts before proposal finalization; these are BLOCKING.

---

### SECTION E: ANNEXURE VII — TECHNICAL CAPABILITY MATRIX (23 Capabilities)

**Coverage:** 20/23 addressed (87%) | **Gap:** 3 new capabilities (Sustainability, Case Mgmt, Maturity Roadmap)

Proposal must confirm capability availability for each item.

| Cap ID | Capability | Binding | Availability | Proposal Must Address | Proposal Status |
|---|---|---|---|---|---|
| CAP-01–CAP-13 | Visualization, Integration, Monitoring, Playback, Simulation, Data Stitching, Biometric Integration, Assaia AI, Canonical Data Model, Spatial Management, Data Quality, Explainability, Business Rules Config | 🔴 shall | Base (Phase 1) | ✓ All confirmed in existing architecture | ✓ COVERED |
| CAP-14 | **Sustainability Analytics** | 🔴 shall | ⚠ **NEW REQUIREMENT** | **Add:** How platform correlates energy/utilities/assets with passenger flow; carbon reporting metrics; environmental KPI calculation logic | ☐ |
| CAP-15 | **Case Management Workflow** | 🔴 shall | ⚠ **NEW REQUIREMENT** | **Add:** Alert→case creation automation; ownership assignment; escalation routing; closure tracking; after-action review capabilities | ☐ |
| CAP-16 | Planning-Mode Scenarios (what-if simulation) | 🟡 should | Base (Phase 1) | ✓ Confirmed in predictive analytics section | ✓ COVERED |
| CAP-17 | **Digital Twin Domain Maturity Roadmap** | 🟡 should | ⚠ **NEW REQUIREMENT** | **Add:** Phased capability progression roadmap showing: visibility → prediction → optimization → automation across domains; timeline for each phase | ☐ |
| CAP-18 | Business Rules Configuration (low-code) | 🔴 shall | Base (Phase 1) | ✓ Confirmed in platform capabilities | ✓ COVERED |
| CAP-19 | Alerting + Simulation + Prediction | 🔴 shall | Base (Phase 1) | ✓ Core analytics confirmed | ✓ COVERED |
| CAP-20 | **Data Archival & Reporting SLAs** | 🔴 shall | ⚠ **NEW REQUIREMENT** | **Add:** Archive retention policy; reporting availability for archived data; SLA for archive retrieval; cost model for long-term retention | ☐ |
| CAP-21 | Security & Deployment (ISR, multi-deployment) | 🔴 shall | Base (Phase 1) | ✓ Confirmed in security & deployment section | ✓ COVERED |
| CAP-22 | Multi-Channel Information Sharing (video walls, mobile) | 🔴 shall | Base (Phase 1) | ✓ Confirmed in distribution channels | ✓ COVERED |
| CAP-23 | Communication Tool Integration (Teams, SMS, Slack) | 🔴 shall | Base (Phase 1) | ✓ Confirmed in stakeholder notification | ✓ COVERED |

**ACTION:** Add CAP-14, CAP-15, CAP-17, CAP-20 to proposal; verify all others.

---

## SUMMARY: PROPOSAL CHECKLIST

**Use this checklist to ensure all 91 requirements are addressed:**

### RFP Body Sections (80 items)
- [ ] 67 addressed items → verify content accurate & complete
- [ ] 13 missing items → add proposals per table in Section A

### Annexure III (43 questions)
- [ ] **Solution Architecture (SA):** 5 questions answered
- [ ] **Scalability (SC):** 5 questions answered
- [ ] **Hosting/Data/Backup/Recovery (BU):** 20 questions answered ← **PRIORITY: 7 CRITICAL items**
- [ ] **System Integration (IN):** 8 questions answered
- [ ] **Performance/Availability (PF):** 7 questions answered
- [ ] **Usability/Compatibility (UC):** 12 questions answered ← **PRIORITY: UC7 (WCAG) & UC9–UC11 (Arabic/RTL)**
- [ ] **Ownership & Security (OS):** 17 questions answered ← **PRIORITY: OS1 (data ownership) & OS11 (data location)**

### Annexure IV (8 use cases)
- [ ] All 8 use cases compliance scored (Comply / Partially Comply / Do Not Comply)
- [ ] 2.5 use cases with gaps (A2, A3, A5, A6, A7, A8) deepened

### Annexure V (17 integrations)
- [ ] All 17 integrations described
- [ ] **INT-02 (Kayvan):** resolved or noted as deviation
- [ ] **INT-11 (RealTimeDXB):** architectural decision documented

### Annexure VII (23 capabilities)
- [ ] All 23 capabilities confirmed
- [ ] CAP-14, CAP-15, CAP-17, CAP-20 added (new capabilities)

---

## BLOCKING ISSUES (Must Resolve Before Proposal Submission)

| Issue | RFP Source | Impact | Resolution Required |
|---|---|---|---|---|
| **UAE Data Residency** | BU1, OS11, NFR-026 | CRITICAL — Government mandate | Explicit commitment: all production data in UAE DC |
| **RTO/RPO Numeric Targets** | BU3, BU5, NFR-020/021 | CRITICAL — Tier 1 SLA | Specify RTO ≤ 4 hrs, RPO ≤ 1 hr (or propose alternative) |
| **DR Provider Disclosure** | BU16 | CRITICAL — Vendor lock-in risk | Name DR provider, location, certified RTO/RPO |
| **Kayvan Airside Integration** | INT-02 | HIGH — Phase 1 airside capability | Confirm integration approach or document as Phase 2 |
| **RealTimeDXB Coexistence** | INT-11 | CRITICAL — Architectural conflict | Clarify subsumption/parallel/data-source strategy |
| **WCAG Accessibility** | UC7 | MEDIUM — User adoption | Commit to WCAG 2.1 Level AA/AAA |
| **Arabic + RTL Support** | UC9–UC11 | MEDIUM — Regional compliance | Confirm native Arabic + RTL support |
| **API/Bandwidth Pricing** | IN4 | MEDIUM — TCO transparency | Itemize per-API fees, bandwidth overages |

---

**Document Version:** 2026-08-10  
**Next Step:** Proposal team uses this matrix to fill gaps and create comprehensive Section-by-Section responses  
**Final Validation:** Run compliance-validator Step 3 (proposal artefact validation) once proposal draft is complete

