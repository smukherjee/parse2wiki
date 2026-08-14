# Airport Eye Licensing & Intellectual Property Framework

## PROPOSED SECTION PLACEMENT

**Location:** Section 5 (Commercial Proposal)  
**Sequence:** Insert as **Section 5.5a** (before existing 5.5 Pricing Assumptions)  
**Numbering:** Renumber existing 5.5 onwards as 5.5b, 5.6 onwards as 5.7, etc.

**Alternative:** Can also be placed as **Annexure L (Licensing & IP Framework)** if a separate exhibits volume is preferred.

---

## SECTION 5.5a: LICENSING & INTELLECTUAL PROPERTY FRAMEWORK

### Scope

This section defines intellectual property ownership, licensing rights, attribution, and usage restrictions across the Airport Eye Integrated Digital Twin programme, covering:

- **Operational Digital Twin (AIOP Platform)** — WAISL proprietary platform
- **Geospatial Digital Twin** — GEOKNO proprietary geospatial engine + ESRI ArcGIS integration
- **AI Models, Training Data, and Knowledge Assets** — DIAL-owned per BRD Section 3.5.5
- **Custom Configurations, Integrations, and Adaptations** — Shared ownership model
- **Third-Party Components and Dependencies** — Licensed to DIAL per subsection 5.5a.8

### 5.5a.1 Operational Digital Twin (AIOP) — Platform Code & IP Ownership

#### IP Ownership

**WAISL retains perpetual, exclusive ownership** of the Operational Digital Twin (AIOP) platform's:

- Source code (Unity/Unreal engine rendering, 3D viewer components, WebGL streaming architecture)
- Architecture and technical design patterns
- Proprietary algorithms for digital twin synchronisation, real-time data fusion, and scene-graph optimisation
- User interface components and design system
- Platform SDKs and APIs (public-facing and internal)

**DIAL receives a perpetual, royalty-free licence** to deploy, operate, and maintain the AIOP platform **for the duration of the project and in perpetuity thereafter** at the Airport Eye installation (Indira Gandhi International Airport, Delhi, Terminals 1, 2, 3).

**Scope of Licence:**

- Right to install and operate AIOP on DIAL's infrastructure (on-premises or cloud, per Section 4.3 deployment model)
- Right to integrate AIOP with DIAL's systems, data sources, and operational workflows
- Right to configure AIOP for Airport Eye use cases (operational intelligence, simulation, visualisation)
- Right to grant access to DIAL staff, contractors, and authorised third parties for operational use
- **No right to sublicense, redistribute, resell, or create derivative platforms based on AIOP**
- **No right to reverse engineer, disassemble, or extract components for use in competing platforms**

#### Limitations & Restrictions

1. **Restricted to Airport Eye Scope:** Licence applies exclusively to digital-twin operations at IGI Airport. Use for other DIAL properties, external consulting, or re-sale is prohibited without written consent from WAISL.

2. **No Unbundling:** DIAL may not separate AIOP components (e.g., 3D viewer, data synchronisation engine, simulation framework) for use in other systems without WAISL's express permission.

3. **Confidentiality:** DIAL agrees to protect WAISL's proprietary algorithms and source-code architecture from unauthorised disclosure, consistent with industry-standard NDA practices.

4. **No Concurrent Licensing:** WAISL confirms this is an **exclusive deployment licence** for IGI Airport; WAISL will not license competing platforms (e.g., ArcGIS, Autodesk, Bentley) for the same operational scope at IGI during the contract term + 5-year O&M period.

### 5.5a.2 Geospatial Digital Twin — GEOKNO Platform IP

#### IP Ownership

**GEOKNO retains perpetual, exclusive ownership** of the Geospatial Digital Twin's:

- Geospatial data processing and fusion algorithms
- BIM federation and federated CDE (Common Data Environment) architecture
- Asset tagging, spatial indexing, and query optimisation logic
- GIS/BIM-to-IoT-OT mapping and semantic bindings
- ESRI ArcGIS integration layer and customisations

**DIAL receives a perpetual, royalty-free licence** to use the Geospatial Digital Twin for:

- Spatial planning, facilities management, and asset lifecycle management
- Coordination with the Operational Digital Twin (real-time data updates from AIOP → Geo DT)
- Public/stakeholder visualisation and reporting (WebGIS, mobile, desktop)
- Future expansion to other DIAL properties (with licensing escalation determined per CR process)

#### Scope & Limitations

1. **Perpetual Usage:** DIAL's rights persist beyond the 5-year O&M phase and the contract term, provided DIAL continues to maintain ESRI ArcGIS licences (DIAL responsibility per Section 4.3.2).

2. **Third-Party Component:** Geospatial Digital Twin is built on ESRI ArcGIS; DIAL's usage is subject to ESRI's separate licensing terms (maintained by WAISL/GEOKNO on DIAL's behalf per Section 5.5a.8).

3. **No Resale:** DIAL may not resell Geospatial Digital Twin services to third parties or use it for external consulting without GEOKNO's written consent.

### 5.5a.3 AI Models, Training Data, and Knowledge Assets — DIAL Ownership

#### DIAL-Owned IP

**DIAL owns, in perpetuity, all intellectual property generated during the contract term:**

- **AI Model Weights:** All trained neural networks, decision trees, ensemble models, and other ML artefacts trained on DIAL data
- **Training Datasets:** All historical operational data, labelled datasets, and synthetic data used to train models
- **Operational Baselines:** All baseline thresholds, normal-case profiles, and anomaly definitions derived from DIAL operations
- **Knowledge Assets:** Airport-specific domain knowledge, SOP integrations, use-case mappings, and operational heuristics captured in the models

#### DIAL's Rights & Responsibilities

1. **Perpetual Ownership:** DIAL owns these assets beyond contract termination and can:
   - Use models for internal operations indefinitely
   - Retrain/update models with future data without additional licence fees
   - Migrate models to new platforms/vendors (with WAISL's cooperation during transition support)
   - Archive models for compliance and audit purposes

2. **No Vendor Lock-In:** DIAL retains model export rights; models can be exported in standard formats (ONNX, SavedModel, H5, PMML) to facilitate vendor migration.

3. **Bidder Restriction:** WAISL **does not** use DIAL data to:
   - Train or improve external AI models, language models, or MLaaS platforms
   - Build general-purpose aviation or airport-operations models for resale to other clients
   - Create competitive intelligence or benchmarking products

#### Model Governance & Versioning

- All model versions are tagged, documented, and retained for 5+ years (BRD Section 3.5.5)
- Rollback to previous versions is achievable within 4 hours (Section 3.4)
- DIAL SME sign-off is required for threshold and SOP changes baked into models
- Audit trail records every model deployment, retraining, and operational outcome

### 5.5a.4 Custom Configurations, Integrations & Adaptations — Shared Ownership

#### Scope

Custom configurations, integrations, and adaptations developed during implementation include:

- System integration connectors (AODB/FIDS adapters, BMS gateways, OT data normalisation)
- Domain-specific use-case logic (operational rules engines, alert SOP mappings, passenger-flow decision criteria)
- Custom UI customisations and airport-specific branding
- Data mappings, ETL logic, and schema transformations
- Testing scripts, UAT harnesses, and operational runbooks

#### Ownership & Rights

**Ownership Structure:**

1. **WAISL Ownership (with DIAL Licence):**
   - All custom code is WAISL-owned, subject to a **perpetual, royalty-free, irrevocable licence to DIAL**
   - DIAL may use, modify, and maintain custom code for the duration of the contract and indefinitely thereafter
   - DIAL may not resell or relicense custom code without WAISL consent

2. **DIAL Ownership (Limited Scope):**
   - DIAL's own operational rules, SOP documentation, and decision logic (as distinct from platform code) remain DIAL-owned
   - DIAL's data models, schema extensions, and domain-specific knowledge assets are DIAL-owned

#### Maintenance & Support

- **Pre-Contract Expiry:** WAISL maintains and updates all custom code per the 9-month delivery + warranty/AMC schedule
- **During 5-Year O&M:** WAISL provides bug fixes, patch management, and compatibility updates; DIAL may submit enhancement requests via formal change control
- **Post-Contract Expiry:** DIAL may request source-code escrow release (see Section 5.5a.6); DIAL becomes responsible for future maintenance

### 5.5a.5 Third-Party & Open-Source Components — Licensing Model

#### Third-Party Software

The AIOP platform and supporting infrastructure incorporate third-party software components licensed under various models:

**Proprietary Commercial Licenses:**
- ESRI ArcGIS (Geospatial Digital Twin foundation)
- Unity/Unreal Engine (3D rendering, as selected in Mo1 workshop per Section 3.5.1)
- Commercial cloud services (e.g., Azure, AWS, Google Cloud as applicable per Section 4.3)

**Open-Source Licenses:**
- Libraries and frameworks licensed under OSI-approved licences (MIT, Apache 2.0, BSD, LGPL, GPL, etc.)
- Full inventory and compliance audit in Software Bill of Materials (SBOM), Annexure K.6

#### DIAL's Rights & Compliance

1. **Scope of Rights:** DIAL's licence to AIOP includes the right to use all embedded third-party components in the scope of the Digital Twin licence (Section 5.5a.1).

2. **No Additional Fees:** All third-party component licensing fees are included in Tables 1-6 pricing. No additional per-seat or consumption-based fees accrue to DIAL.

3. **Compliance & Audit:**
   - WAISL provides an SBOM (Software Bill of Materials) in Annexure K.6 listing all third-party components and their licences
   - WAISL warrants compliance with all open-source licence obligations (source-code disclosure, attribution, etc.)
   - DIAL may conduct periodic compliance audits; WAISL provides cooperation and documentation

4. **Commercial Licence Renewals:**
   - ESRI ArcGIS maintenance and upgrades: WAISL manages on DIAL's behalf during contract term; DIAL assumes renewal responsibility post-contract (unless extended O&M is agreed)
   - Cloud service infrastructure: Cost escalation provisions per Section 5.5 (Pricing Assumptions)

#### Open-Source Governance

- **No GPL Copyleft Exposure:** WAISL warrants that no GPL-licensed code is used in AIOP core (only in optional tooling/utilities, clearly documented in SBOM). AIOP source code is not subject to GPL copyleft obligations.
- **Attribution & Credits:** All open-source components are attributed in AIOP's About/Credits interface and in the SBOM; DIAL may request custom attribution as per open-source licence terms.

### 5.5a.6 Source Code Escrow & Business Continuity

#### Escrow Arrangement

To protect DIAL's operational continuity in the event of WAISL business disruption, the following escrow terms apply:

**Trigger Events for Release:**
- WAISL files for bankruptcy or is acquired by a competitor (per DIAL's reasonable assessment)
- WAISL is unable to provide critical support for ≥30 consecutive days (support-response SLA breach escalated)
- Mutual agreement between DIAL and WAISL to transition to a successor vendor

**Escrowed Materials:**
- AIOP platform source code (Unity/Unreal implementation, C#/C++ core, rendering algorithms)
- Geospatial Digital Twin core algorithms and integration code (GEOKNO code within the federated CDE)
- Custom integration code and configuration scripts developed during implementation
- Detailed technical documentation, architecture diagrams, and deployment playbooks

**Escrow Agent:**
- A neutral third-party escrow agent (e.g., Iron Mountain, Escrow Tech, or equivalent) holds encrypted copies
- DIAL and WAISL jointly designate the escrow agent and define release conditions in a formal Escrow Agreement (Annexure M)
- Cost: WAISL funds initial deposit and annual maintenance; DIAL reimburses 50% of renewal fees post-contract expiry (negotiable)

**Post-Release Obligations:**
- Upon release, DIAL receives unencrypted source code, build instructions, and technical documentation
- DIAL may maintain, debug, and operate the released code without further royalty or licence fees
- DIAL is not entitled to resell or redistribute escrow-released code to third parties
- WAISL is released from ongoing support obligations once escrow code is released

### 5.5a.7 Branding, Attribution & Trademark

#### DIAL Branding

All Airport Eye deliverables prominently display DIAL branding:

1. **System Interfaces:** All user-facing screens (Operational DT viewer, scenario engine, mobile apps) display DIAL logo and attribution (e.g., "Airport Eye — Powered by WAISL").

2. **Documentation:** All technical documentation, user manuals, and training materials include DIAL and WAISL attribution.

3. **Signage & Collateral:** System signage (helpdesk, public screens) and marketing collateral are co-branded per DIAL's guidelines.

#### WAISL & GEOKNO Attribution

- WAISL and GEOKNO are named as technology partners in public announcements and case studies (with DIAL pre-approval of messaging)
- Case studies and reference installations may cite Airport Eye as a reference (with DIAL's written consent)
- No competitive use: WAISL may not use Airport Eye or DIAL branding to pitch competing airport-operations platforms without DIAL consent

#### Trademark Restrictions

- DIAL owns or maintains all trademarks related to "Airport Eye" and derivative marks
- WAISL may use "Airport Eye" solely in the context of this project and historic case-study references (post-project)
- Neither party may register sub-trademarks or domain names incorporating "Airport Eye" without the other's consent

### 5.5a.8 License Perpetuity & Survival

#### Perpetual Grant

DIAL's licence to the AIOP platform, Geospatial Digital Twin, and custom code **survives contract termination in perpetuity**:

1. **Term Clarity:** "For the duration of the project and in perpetuity thereafter" means:
   - During the 9-month delivery + 12-month warranty/AMC + 5-year O&M: Full support and updates per SLA
   - Post-contract expiry (Year 6 onwards): DIAL retains perpetual usage rights with no additional licence fees

2. **Limitation on Support:** Post-contract expiry, WAISL is not obligated to provide:
   - Bug fixes or security patches (unless extended O&M is separately contracted)
   - Technical support or helpdesk services
   - Platform upgrades or new feature releases
   - However, DIAL may engage WAISL on a time-and-materials basis for support services

3. **Infrastructure Continuity:** DIAL is responsible for infrastructure maintenance, security patching (OS, cloud platform), and third-party licence renewal (e.g., ESRI) post-contract expiry.

#### Intellectual Property Survival

- All IP rights and restrictions outlined in Sections 5.5a.1–5.5a.7 survive contract termination indefinitely
- DIAL's ownership of AI models, training data, and knowledge assets is absolute and irrevocable
- WAISL's restrictions on unbundling, resale, and competitive use continue in perpetuity

### 5.5a.9 Compliance & Remedies

#### Breach of IP Terms

If either party breaches the licence terms in this Section:

1. **Breach by DIAL:** (e.g., unauthorised resale, reverse engineering, use outside Airport Eye scope)
   - WAISL may seek injunctive relief and damages
   - DIAL's licence may be suspended pending remediation
   - Remediation period: 30 days notice + 30 days cure

2. **Breach by WAISL:** (e.g., use of DIAL data for external AI model training, unauthorised sublicensing)
   - DIAL may seek damages and immediate injunctive relief
   - DIAL may terminate the contract and transition to alternative vendor (escrow code released per Section 5.5a.6)
   - Remediation period: 15 days notice + 15 days cure

#### Indemnification

- **WAISL Indemnification:** WAISL indemnifies DIAL against third-party IP infringement claims arising from AIOP or Geospatial DT (e.g., alleged patent infringement). WAISL's obligation is capped at 12 months of average monthly fees (or 2x the relevant component fee, whichever is higher).

- **DIAL Indemnification:** DIAL indemnifies WAISL against third-party claims arising from DIAL's use of AIOP outside the Airport Eye scope or in violation of licence restrictions.

#### Insurance & Liability Cap

- WAISL maintains IP indemnity insurance (per professional-services norms, typically INR 50 Lakh–1 Crore per project)
- Liability for IP claims is capped at the contract grand total (Section 5.3)
- Claims must be notified within 12 months of discovery; claims notified after 12 months are waived

### 5.5a.10 Transition & Knowledge Transfer

#### End-of-Contract Deliverables

At contract conclusion (Mo9 + 12-month warranty + 5-year O&M), WAISL delivers:

1. **Source Code & Documentation Package:**
   - AIOP source code (if escrow-released or if extended O&M is not agreed)
   - Custom integration code, scripts, and configuration
   - Technical architecture documentation, API reference, and deployment playbooks
   - AI model export (in portable formats: ONNX, SavedModel, PMML)
   - Training data inventory and data dictionary

2. **Knowledge Transfer:**
   - 6-month transition-support window (included in 5-year O&M exit scope per BRD Section 9.12)
   - Knowledge-transfer sessions for DIAL operations and engineering teams
   - Handover of on-premises infrastructure, cloud configurations, and security keys

3. **Operational Handoff:**
   - All runbooks, troubleshooting guides, and escalation procedures
   - Fully trained DIAL operations team (per training plan in Section 4.5)
   - System in production-ready state, all defects resolved, all VAPT findings remediated

#### Post-Contract Responsibility

After contract expiry:

- **DIAL Operations:** DIAL assumes full responsibility for platform operations, maintenance, and data management
- **Optional Extended Support:** DIAL may contract with WAISL (or another vendor) for continued support on a separate time-and-materials basis
- **Alternative Vendor Migration:** DIAL may migrate to a competing platform using escrow-released source code and exported data/models (no contractual restriction)

---

## SUMMARY TABLE: IP OWNERSHIP & USAGE RIGHTS

| Component | IP Ownership | DIAL Usage Rights | Perpetual? | Resale Allowed? | Vendoring Flexibility |
|-----------|--------------|-------------------|-----------|-----------------|----------------------|
| **AIOP Platform Code** | WAISL | Perpetual, royalty-free, exclusive to IGI Airport, no unbundling | Yes | No | High (escrow source code available) |
| **Geospatial DT** | GEOKNO + ESRI | Perpetual, royalty-free, expandable to other DIAL properties with escalation | Yes (DIAL responsible for ESRI renewal) | No | Moderate (ESRI-dependent) |
| **AI Models & Weights** | DIAL | Perpetual, absolute, export & retrain without restriction | Yes | Permitted internally only | Very High (portable formats) |
| **Training Data** | DIAL | Perpetual, absolute, use for model retraining & analytics | Yes | Permitted internally only | Very High (portable formats) |
| **Custom Code & Integrations** | WAISL (with DIAL licence) | Perpetual, royalty-free, modifiable, no resale without consent | Yes | No | High (escrow available) |
| **Third-Party Components** | Respective vendors | Included in AIOP licence scope; SBOM provided; no additional fees | Yes (per vendor terms) | No (governed by respective vendor licences) | Moderate (per vendor agreements) |
| **Operational Documentation** | Shared | DIAL ownership of operational/domain content; WAISL ownership of technical architecture | Yes | Permitted internally only | High (fully transferable) |
| **Branding & Trademarks** | DIAL | DIAL exclusive ownership of "Airport Eye" marks; WAISL attribution in perpetuity | Yes | WAISL reference rights post-contract | N/A |

---

## INCORPORATION INTO PROPOSAL

### Document Structure Recommendation

**Option 1: Integrated into Commercial Section (Preferred)**
- Insert as Section 5.5a, immediately after Section 5.4 (Milestone Payment Schedule)
- Renumber existing Section 5.5 as Section 5.5b, and subsequent sections accordingly
- Creates a logical flow: Payment (5.4) → Licensing/IP (5.5a) → Pricing Assumptions (5.5b) → Deviations (5.6)

**Option 2: Separate Annexure**
- Create Annexure L (Licensing & Intellectual Property Framework)
- Reference Section 5.5a in the main text: "For detailed licensing terms, see Annexure L"
- Useful if this section grows or requires separate legal review/sign-off

### Cross-References to Update

If Section 5.5a is added, update these cross-references:

1. **Table of Contents (Page 5–6):**
   - Current: "5.5 Pricing principles", "5.6 Deviations"
   - Update to: "5.5a Licensing & Intellectual Property Framework", "5.5b Pricing principles", "5.6 Deviations"

2. **AI Governance Section (3.4):**
   - Add reference: "For detailed IP ownership and usage restrictions, see Section 5.5a (Licensing & Intellectual Property Framework)"

3. **Deviations Table (5.6):**
   - Add entry:
     ```
     | CC-09 | AIOP platform IP ownership (perpetual licence, no unbundling) | BRD Section 9.13 (if present) / RFP / Commercial Framework | Bidder proposes WAISL perpetual ownership with DIAL perpetual, royalty-free, exclusive-use licence; details in Section 5.5a |
     ```

4. **Appendices Index:**
   - Add: "Annexure M: Source Code Escrow Agreement (referenced in Section 5.5a.6)"
   - Update: "Annexure K.6: Software Bill of Materials (SBOM) – referenced in Section 5.5a.5"

---

## LEGAL REVIEW NOTES

### For WAISL Internal Review:

1. **Perpetual Licence Commitment:** Section 5.5a.1 & 5.5a.8 commit to perpetual usage rights post-contract expiry. Confirm this aligns with WAISL's long-term business model (no future monetisation expected on this deployment).

2. **Source Code Escrow:** Section 5.5a.6 commits to escrow. Confirm WAISL board/legal approval and cost allocation.

3. **DIAL Data Usage:** Section 5.5a.3 restricts use of DIAL data for external AI model training. Confirm this does not conflict with WAISL's other clients or research initiatives.

4. **Third-Party Components:** Section 5.5a.5 warrants compliance with open-source licences. Conduct SBOM audit before finalising.

### For DIAL Review:

1. **Perpetual Licence Clarity:** Section 5.5a.1 & 5.5a.8 confirm DIAL retains perpetual usage rights without additional licensing fees post-Year 5. Confirm this meets DIAL's operational continuity requirements.

2. **Escrow Terms:** Section 5.5a.6 references a formal Escrow Agreement (Annexure M) to be negotiated. DIAL should engage legal/procurement to finalise escrow terms, agent selection, and cost allocation.

3. **AI Model Ownership:** Section 5.5a.3 confirms DIAL's absolute ownership of AI models and training data. Confirm this aligns with DIAL's data-sovereignty and AI governance policies (Annexure III, Data Safeguards).

4. **Third-Party Renewals:** Section 5.5a.5 clarifies ESRI ArcGIS renewal responsibility (WAISL during contract, DIAL post-contract). Confirm DIAL budget provisions for Year 6+ ESRI maintenance.

---

## DRAFTING NOTES FOR BDDA / LEGAL TEAM

### Suggested Refinements Post-Stakeholder Review:

1. **Exclusivity Duration:** Consider if WAISL's commitment to not license competing platforms (Section 5.5a.1, item 4) should extend beyond the 5-year O&M phase. Current language: "during the contract term + 5-year O&M period." Could tighten to perpetuity or relax to Year 3 depending on DIAL's competitive positioning.

2. **Third-Party Component Risk:** If DIAL's risk appetite for GPL-licensed components is low, tighten Section 5.5a.5 to **exclude GPL entirely** (not just GPL copyleft exposure to AIOP core). Current language allows GPL in "optional tooling/utilities"—confirm this is acceptable.

3. **Escrow Trigger Precision:** Section 5.5a.6 lists business-disruption triggers but does not quantify "critical support" (e.g., severity-1 SLA breaches). Consider defining triggers in the formal Escrow Agreement (Annexure M) to avoid post-contract disputes.

4. **IP Breach Remediation Timeline:** Section 5.5a.9 gives DIAL 30 days cure time for IP breaches; WAISL gets 15 days. Consider if asymmetry is intentional or should be balanced (e.g., both 15 days, or escalation timeline tied to impact severity).

5. **Post-Contract Support Pricing:** Section 5.5a.10 allows DIAL to engage WAISL on time-and-materials basis post-contract. Consider pre-defining a "legacy support" rate card (e.g., INR X per person-day for bug fixes; INR Y per day for architecture consultation) to reduce post-contract negotiation friction.

---

**Status:** Ready for integration into Airport Eye proposal  
**Review Level:** Requires WAISL legal, GEOKNO alignment, and DIAL procurement sign-off  
**Estimated Editing Time:** 2–3 hours to adapt, cross-reference, and integrate into final proposal
