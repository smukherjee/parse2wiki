# CTG Video Analytics Platform — Comprehensive Case Study
## Strategic Business Proposal & Technical Architecture for Cartagena International Airport

**Prepared for:** CTG Leadership (CEO, CTO, VP Operations) & Technical Teams
**Prepared by:** Waisl Digital
**Date:** July 2026
**Timeline to Presentation:** August 25, 2026
**Project Duration:** Q1 2027 – Q4 2027

---

## PART I: EXECUTIVE BRIEF FOR C-LEVEL LEADERSHIP

### The Strategic Opportunity

**Situation:**
Cartagena International Airport (CTG) is undergoing a transformative USD 500M expansion—growing from 7M to 11M annual passengers and expanding terminal capacity from 25,000 m² to 44,000 m² by December 2027. This expansion represents a critical inflection point for operational excellence and competitive positioning in Latin America's aviation hub market.

**The Problem:**
CTG currently operates with **zero real-time visibility** into passenger experience and operational efficiency. There are no objective flow metrics, no queue analytics, no predictive saturation warnings, and no quantified link between operational decisions and passenger satisfaction. During peak hours (which occur multiple times daily and will intensify during construction periods), the airport routinely experiences:
- Check-in bottlenecks (extended waits during peak hours)
- Security queue collapses (SHA capacity exceeded)
- Gate utilization inefficiency (suboptimal turnaround times)
- Staffing mismatches (either over- or under-deployed)
- No baseline for measuring satisfaction improvement post-expansion

This operational blindness exposes CTG to:
- **Regulatory risk:** The Colombian Government (through the OINAC concessionaire agreement) mandates measurable passenger experience improvements as a condition of the concession
- **Commercial risk:** Competing hubs are investing in similar analytics; CTG risks being positioned as a lower-tier experience
- **Operational risk:** Peak-hour collapses during peak construction periods (2027) threaten revenue (gate closures, delays, passenger dissatisfaction)
- **Benchmarking gap:** No ASQ (Airports Council International) baseline prevents demonstrating transformation to stakeholders (airlines, investors, passengers)

---

### The Waisl Solution: Three-Layer Value Proposition

#### **Layer 1: Real-Time Operational Intelligence**
**What:** Deploy a data warehouse + BI platform that ingests video analytics (passenger flow), sensor data (queues, occupancy), and Collins AODB/RMS/FIDS data (flight operations) into a unified dashboard.

**Outcome:**
- CTG management sees passenger processing in real time: queue lengths at check-in, security throughput, gate utilization
- Predictive alerts (10–15 min foresight) for impending congestion allow proactive staffing adjustments
- Reduces peak-hour wait times through dynamic resource allocation

**Business Impact:**
- Prevents peak-hour service collapses during construction
- Measurable operational improvement by Q2 2027

#### **Layer 2: Passenger Experience Benchmarking**
**What:** Integrate objective operational metrics (flow, queue, wait times) with subjective satisfaction data via ACI Airport Service Quality (ASQ) standard surveys.

**Outcome:**
- Establish baseline CTG satisfaction scores (today: blind)
- Correlate operational metrics to satisfaction drivers (e.g., which queue-time reduction drives greatest satisfaction gain?)
- Position CTG as a leading Latin American airport in data-driven passenger experience management

**Business Impact:**
- **Competitive differentiation:** ASQ benchmark becomes an asset for airline partnerships
- **Evidence of transformation:** Quantified passenger satisfaction improvement post-expansion (critical for concessionaire reputation)
- **Stakeholder credibility:** Transparent, industry-standard metrics for airlines, government, passengers

#### **Layer 3: Strategic Asset Ownership**
**What:** CTG owns the data warehouse, analytics models, and engagement data. Waisl provides platform, integration, and L1 support.

**Outcome:**
- Data residency and control remains with CTG (regulatory compliance, no personal data exposure)
- CTG builds internal analytics capability; can extend to revenue optimization (retail, F&B) and facility planning post-pilot
- Modular architecture allows future integrations (baggage handling, airline systems, DCS integration)

**Business Impact:**
- **Compliance:** Anonymized tracking (hashed device IDs, aggregated counts) mitigates data protection risk
- **Future-proofing:** Platform extensible to revenue-focused use cases (loyalty, retail analytics, dynamic pricing)

---

### Financial Impact: 12-Month Value Estimate [ILLUSTRATIVE]

The figures below are **illustrative estimates** built from industry benchmarks and CTG-specific assumptions. They should be validated against CTG's actual baseline data during the pilot before being used as committed targets.

#### **Value Creation Waterfall [ILLUSTRATIVE]**

| Value Driver | Metric | Assumptions [ILLUSTRATIVE] | Estimated Benefit [ILLUSTRATIVE] | Confidence |
|---|---|---|---|---|
| **Queue Wait Time Reduction** | Reduction in peak-hour wait times via dynamic staffing | Real-time visibility enables faster counter/lane reallocation during peaks | Improved throughput, fewer missed flights | Medium |
| **Staffing Efficiency** | Reduced peak-hour over-staffing | Typical airports over-staff peaks by a wide margin; data-driven allocation tightens the buffer | Labor cost savings | Medium |
| **On-Time Performance (OTP) Improvement** | Fewer ground delays from terminal congestion | Faster gate turnaround, reduced check-in delays | Operational revenue protection | Medium |
| **Passenger Satisfaction Uplift** | ASQ score improvement from an unmeasured baseline | Industry pattern: satisfaction gains correlate with repeat-passenger behavior | Incremental loyalty/commercial value | Low-Medium |
| **Network Resilience During Construction** | Avoided peak-hour service collapses (Q2–Q3 2027) | Construction constrains capacity; predictive analytics reduces failure risk | Avoided concessionaire/regulatory exposure | Medium |
| **Operational Data Asset** | Foundation for future revenue analytics (retail, baggage, loyalty) | Platform extensibility beyond passenger experience | Option value for future initiatives | Low |

**Important:** No hard financial totals are presented here. CTG's actual baseline (current wait times, staffing costs, OTP, delay costs) is not yet known — the pilot's first output should be establishing this baseline so value can be quantified with real numbers rather than assumptions.

**Investment vs. Value:** The pilot is designed to be self-funding relative to the ~USD 1.2M budget CTG has indicated, with a full financial business case delivered at the Week 20 go/no-go gate using pilot-observed data rather than industry proxies.

**Important scope note on the ~USD 1.2M figure:** Camera hardware and on-prem image storage are **CTG's direct capital purchases**, not part of Waisl's quote (Waisl specifies cameras for CTG to buy, and integrates against CTG-owned storage, to keep Waisl outside DPA exposure). Waisl's commercial quote will therefore be a subset of the 1.2M envelope — this should be clarified with CTG early so budget expectations and the quoted price aren't seen as mismatched.

---

### Strategic Recommendation: Phased Deployment Model

**Phase 1: Pilot Deployment (Q1–Q2 2027)** — 2-Zone Proof of Concept
- Scope: Check-in + Security areas (pilot zones only)
- Duration: ~28 weeks deployment + operational validation
- Deliverable: 14 core KPIs operational; 39-KPI roadmap validated
- Go/No-Go Gate: Before full deployment commitment; decision by CTO/leadership on value realization

**Phase 2: Full Terminal Deployment (Q2–Q3 2027)** — Expand to Gates, Baggage, Airside
- Scope: All terminal zones + airside (150–200 cameras, full KPI suite)
- Duration: ~16 weeks (phased by zone, coordinated with construction)
- Delivery: All 39 Mandatory KPIs + 15 Maturity KPIs operational by Q3 2027

**Phase 3: Optimization & Scale (Q4 2027 Onward)** — Fine-Tuning + Advanced Features
- Scope: ML model calibration, ASQ integration, revenue-focused analytics (optional)
- Duration: Continuous improvement

**Why This Approach Works:**
1. **De-risks the program:** Pilot proves value before full investment; allows course correction
2. **Aligns with construction timeline:** Phasing coordinates with terminal expansion completion (Q4 2027)
3. **Mitigates execution risk:** Early validation of camera placement, network capacity, analytics accuracy
4. **Builds organizational capability:** Teams learn during pilot; full deployment scales faster

---

### Key Decision Criteria for CEO/CTO

| Criterion | Requirement | Waisl Commitment |
|---|---|---|
| **Data Ownership** | CTG owns data warehouse; Waisl provides platform as service | Waisl provides analytics platform; CTG infrastructure/storage in-house |
| **Privacy/Compliance** | Anonymized tracking; no personally identifiable data retained | Hashed device IDs, aggregated counts; Waisl has no access to raw video or personal data |
| **Vendor Lock-In** | Avoid proprietary dependencies; ONVIF-standard cameras, open APIs | Open architecture; cameras/sensors ONVIF-compliant; APIs via REST/MQTT; data exports in standard formats |
| **Scalability** | Platform scales from 11M to future passenger growth | Modular design; federated analytics servers; pattern validated at larger-scale airport deployments |
| **ROI Timeline** | Clear payback horizon | Pilot establishes CTG-specific baseline; full business case at Week 20 gate uses real data, not assumptions |
| **Support & Continuity** | Local L1 team; no dependency on offshore support | Waisl provides L1 local team + remote L2 support |

---

### Leadership Recommendation

**PROCEED with Phase 1 Pilot** under the following conditions:
1. **Signed MSA with Waisl** to allow an 8-week pre-deployment site survey and planning period
2. **Phase 1 budget approved** within the indicated ~USD 1.2M total project envelope (pilot is the smaller first tranche — see Part II cost detail)
3. **Phase 1 success criteria defined:** Achieve 12 of 14 pilot KPIs with ≥95% data availability and ≤5% people-counting error
4. **Go/No-Go decision point at Week 20:** Assess KPI performance, real-time value realization, and team readiness before committing to full deployment spend

**What the Pilot Delivers by Week 20:**
- CTG's first-ever real-time operational baseline (queue times, throughput, staffing utilization)
- A validated, CTG-specific financial business case (replacing the illustrative estimates above with actual numbers)
- Proof of Collins integration and ONVIF-camera analytics accuracy
- A trained CTG operations team capable of running the dashboard

---

---

## PART II: TECHNICAL ARCHITECTURE FOR IT PROJECT MANAGEMENT

### Overview: System Architecture & Integration Framework

The CTG Video Analytics Platform operates as a federated, real-time data processing system integrating three primary data streams:

1. **Video Analytics Stream** (CCTV cameras + Xovis/LiDAR sensors) → passenger flow, queue, occupancy
2. **Collins Integration Stream** (AODB/RMS/FIDS) → flight operations, aircraft movements, gate assignments
3. **Operational Systems Stream** (CUPPS check-in, CUSS airline kiosks, Veripax PTS, WiFi sensors) → transaction-level passenger tracking

All streams converge into a **Data Lake** (CTG-owned data warehouse) where they are processed via the **Waisl AIOP Platform** (analytics engine) and visualized via a **BI Dashboard** (KPI reporting + real-time alerts).

```
                    VIDEO ANALYTICS STREAM
                    ┌──────────────────────┐
                    │  CCTV Cameras        │
                    │  Xovis (4–6 units)   │
                    │  LiDAR (2–3 units)   │
                    │  Thermal (2–4 units) │
                    └────────┬─────────────┘
                             │ (RTSP/ONVIF)
                             ▼
        ┌──────────────────────────────────────────┐
        │    Video Analytics Server (GPU-enabled)  │
        │    ├─ People-counting model              │
        │    ├─ Queue detection                    │
        │    ├─ Occupancy heatmaps                 │
        │    └─ Metadata extraction (KPI streams)  │
        └────────┬─────────────────────────────────┘
                 │ (Queue len, count, throughput)
                 │
                 │     COLLINS STREAM           OPERATIONAL SYSTEMS
                 │     ┌──────────────┐         ┌───────────────────┐
                 │     │ AODB (iFIMS) │         │  CUPPS Check-in   │
                 │     │ RMS (iFIMS)  │         │  CUSS Kiosks      │
                 │     │ FIDS (iFIMS) │         │  Veripax PTS      │
                 │     │              │         │  WiFi Sensors     │
                 │     └──────┬───────┘         └────────┬──────────┘
                 │            │ (API calls)               │ (API calls)
                 │            │                           │
                 ▼            ▼                           ▼
        ┌────────────────────────────────────────────────────────┐
        │          Data Lake (CTG Data Warehouse)                 │
        │  ├─ Raw event streams (queue events, pax counts, etc)  │
        │  ├─ Aggregated KPI metrics (hourly, daily)             │
        │  ├─ Historical baseline (rolling 90-day retention)      │
        │  └─ Audit logs (access, changes)                       │
        └────────────────────┬─────────────────────────────────┘
                             │
        ┌────────────────────▼─────────────────────┐
        │   Waisl AIOP Platform (Analytics Engine) │
        │  ├─ KPI calculation engine               │
        │  ├─ Predictive congestion models         │
        │  ├─ ASQ correlation analysis             │
        │  ├─ Real-time alerting logic             │
        │  └─ Historical reporting                 │
        └────────────────────┬─────────────────────┘
                             │
        ┌────────────────────▼─────────────────────┐
        │      BI Dashboard (CTG Operations)        │
        │  ├─ Real-time KPI boards (1-min refresh) │
        │  ├─ Alert dashboard (red/yellow/green)   │
        │  ├─ Historical reporting (daily/monthly) │
        │  └─ Staff allocation recommendations     │
        └─────────────────────────────────────────┘
```

---

### Component 1: Video Analytics Infrastructure

> **Scope Boundary (per Carlos's 22 Jul 2026 email):** *"The cameras are not part of the project. We just need to tell them the type of cameras they need to buy for the expansion, as well as any current HW that needs to be replaced."* Camera hardware — new and replacement — is **CTG's capital purchase**, not a Waisl line item. Waisl's role is to (1) audit existing cameras and recommend what to retain vs. replace, (2) specify the standard for CTG's procurement, and (3) integrate the resulting camera feeds (CTG-owned, ONVIF-compliant) into the analytics pipeline. The same applies to image storage: per the same email, CTG hosts image storage/backups on its own on-prem infrastructure to keep Waisl outside Colombia's data protection authority (DPA) exposure. Waisl configures and integrates against that storage; it does not own or cost it.

#### **Camera Deployment Strategy: Existing vs. New**

CTG currently operates **IP cameras from Vivotek (Taiwan) and Mobotix (Germany)** distributed across the terminal. Age mix ranges from ~2–6 years old, per Waisl's internal correspondence with the airport manager. **This age/count breakdown has not been field-verified — it is carried over from a debrief conversation, not a site survey.** The deployment strategy below leverages existing infrastructure where viable, upgrades where necessary, but every number in this section must be confirmed during the Week 1–2 site survey before it is used for procurement.

##### **1a. Existing Camera Audit & Reuse Strategy**

**Current State (per informal debrief — pending site verification):**
- Cameras deployed across the terminal, primarily for security, not analytics
- Multiple age cohorts referenced: ~6-year-old cameras (likely limited analytics capability), ~2-year-old cameras (possible partial ONVIF support), some newer units (likely full ONVIF)
- Exact resolution, count, and model breakdown: **unknown — first deliverable of site survey**
- Usage: Security surveillance only; not connected to operational systems

**Reuse Assessment Framework (to be populated with real data during site survey):**

| Camera Generation | Resolution (assumed) | ONVIF Compliance (assumed) | Analytics Capable | Reuse Strategy | Reuse % (indicative) |
|---|---|---|---|---|---|
| Oldest cohort | Likely ≤2MP | Uncertain/partial | Likely limited | Migrate to general surveillance; retire from analytics use | ~0% |
| Mid-age cohort | Possibly 3MP | Likely yes | Partial | Repurpose for gate/corridor coverage pending firmware check | ~40–50% |
| Newest cohort | Possibly 4MP | Likely full | Yes, if confirmed | Integrate directly into analytics pipeline | ~100% |

**Recommended Action:**
- **Site survey Week 1–2 must produce:** exact camera count, model, firmware version, resolution, and ONVIF compliance for every existing unit — this is a Waisl deliverable to CTG, not a procurement Waisl executes
- **Waisl's output:** a written recommendation (retain / replace / reposition) per existing camera, plus a specification for any new units CTG should purchase for coverage gaps
- **CTG's action:** procures and installs the recommended new/replacement cameras; Waisl does not hold camera hardware cost, lead time, or installation risk

**Cost Implication:** Camera hardware is **excluded from Waisl's commercial quote**. It will appear in CTG's own capital plan, sized against Waisl's specification. Waisl's Week 1–2 deliverable should include an indicative CTG-side budget estimate (for CTG's planning purposes only) alongside the formal Waisl quote.

---

##### **1b. Recommended Camera Specification (For CTG's Procurement)**

This is **Waisl's recommended specification** for CTG to procure directly — not a Waisl-supplied item — for zones where analytics accuracy is critical and existing coverage is confirmed insufficient:

**Primary: 4MP IP Cameras (e.g., Hikvision DS-2CD2643G2-IZS or equivalent ONVIF-compliant model)**

| Spec | Requirement | Rationale |
|---|---|---|
| **Resolution** | 4MP (2688×1520) minimum | Sufficient for people-counting (3–4m x 3–4m per pixel) |
| **Sensor** | Progressive-scan CMOS | Eliminates motion blur in crowded check-in/security areas |
| **Lens** | 2.8mm (wide) / 4mm (medium) / 6mm (zoom) | Wide for overviews; medium/zoom for counter-level detail |
| **Frame Rate** | 30 FPS @ 4MP | Smooth tracking; adequate for queue detection |
| **Codec** | H.265 (HEVC) with H.264 fallback | H.265 reduces storage 40–50% vs H.264; broad NVR support |
| **Bitrate** | 4–6 Mbps (H.265) | Bandwidth-optimized for Gigabit network infrastructure |
| **PoE+** | 95W support | Powers camera + IR illumination via single cable |
| **IR Range** | ≤0.1 lux with IR | 24/7 operations; critical for airside/apron work |
| **ONVIF** | Profile S + T | Ensures third-party analytics compatibility (platform-agnostic) |
| **WDR** | Digital + Mechanical | Baggage hall lighting variation requires WDR for consistent accuracy |

**Indicative Deployment in Pilot (Check-in + Security Zones):**
- Check-in area: ~6–8 cameras (overview + counter detail + queue lanes), mix of reused + new depending on survey outcome
- Security area: ~8–10 cameras (lanes, pre-security, throughput), mix of reused + new
- **Exact new-camera count to be confirmed post-survey**

---

#### **1c. Specialized Sensors for Queue & Occupancy Analytics**

**Xovis People Counting System (Essential for Pilot)**

Xovis is a thermal, overhead-mounted people counter delivering real-time headcount and flow analytics. It is among the most accurate technologies available for queue-length detection at airports and is not currently deployed at CTG — this is a new procurement in all scenarios.

| Component | Specification | Use Case |
|---|---|---|
| **Sensor Type** | 3D thermal imaging | Detects body heat; counts people even in dark/crowded conditions |
| **Accuracy** | High accuracy for people-counting in normal lighting (vendor-rated ≥99%; to be validated on-site) | Queue-length detection at check-in and security |
| **Range** | Configurable, typically 5–20m optimal | Check-in queue lanes; security lanes |
| **Output** | REST API + MQTT; real-time headcount, flow direction, dwell time | Integrates directly into Waisl AIOP via API |
| **Mounting** | Overhead-optimal (5–6m height); wall-mount alternative | Overhead mounting above queue lanes gives best accuracy |
| **Integration** | ONVIF, MQTT, cloud APIs; webhook support | Native support in Waisl platform |
| **Power/Network** | PoE; Gigabit Ethernet | Standard infrastructure; no auxiliary power needed |

**Pilot Deployment:**
- Check-in area: 1–2 Xovis units (overhead above counter array)
- Security checkpoint: 1–2 Xovis units per lane cluster
- **Total for pilot: ~4–6 Xovis units** (100% new procurement)

**Why Xovis Justifies the Premium vs. Standard CCTV People-Counting:**
- Thermal signature is materially more robust to lighting changes, occlusion, and clothing color than RGB-camera ML counting
- Lower latency enables faster staffing responses than CCTV-derived counts
- Reduces false-positive queue alerts that would otherwise erode operator trust in the dashboard

---

#### **1d. Network Infrastructure for Video Analytics**

The existing airport network backbone likely supports operational systems (AODB, FIDS, WiFi) but its capacity for concurrent video analytics traffic is **unverified** and must be confirmed in the site survey. The project requires a **dedicated CCTV VLAN** isolated from operational traffic regardless of existing headroom, to protect airline-critical systems from video bandwidth spikes.

**Network Architecture:**

```
        ┌─────────────────────────────────────────┐
        │      Core Switch (existing)              │
        │      (Airport LAN + CCTV uplink)         │
        └─────────────────────┬───────────────────┘
                              │ (Dedicated CCTV VLAN)
        ┌─────────────────────▼───────────────────┐
        │  CCTV Core Switch                        │
        │  ├─ VLAN 100: CCTV Stream (cameras)     │
        │  ├─ VLAN 101: Analytics (Waisl servers) │
        │  └─ VLAN 102: NVR Storage               │
        └─────────────────────┬───────────────────┘
                    ┌─────────┼─────────┐
                    │         │         │
         ┌──────────▼──┐ ┌───▼────┐ ┌──▼──────────┐
         │  Zone: PoE  │ │ Zone:  │ │  Zone:      │
         │ Check-in    │ │Security│ │  Gates/     │
         │ (pilot)     │ │(pilot) │ │  Baggage    │
         │             │ │        │ │  (Phase 2)  │
         └─────────────┘ └────────┘ └─────────────┘
                    │         │         │
         ┌──────────▼─────────▼─────────▼──────────┐
         │  NVR Pool (Central Recording)            │
         │  RAID 5; rolling retention window        │
         └─────────────────────┬────────────────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
        ┌─────▼──────────┐          ┌──────────▼────┐
        │ Analytics      │          │  BI Dashboard │
        │ Server Cluster │          │  (CTG Ops)    │
        └────────────────┘          └────────────────┘
```

**Key Design Decisions:**

1. **Dedicated CCTV VLAN:** Isolates video traffic from operational systems (AODB, FIDS); prevents video streams from congesting airline systems during peak hours
2. **Zone-Based PoE Switches:** Each major zone (check-in, security, gates, baggage, airside) has a dedicated PoE switch stack; enables independent scaling and fault isolation
3. **Centralized NVR with RAID 5:** Single point of recording (reduces management complexity); RAID protects against drive failure; retention window supports ASQ analysis + forensic review (exact retention policy to be agreed with CTG Legal — data minimization principle applies)
4. **Redundant Analytics Servers:** Real-time KPI processing with failover to protect dashboard availability
5. **Fiber Uplinks Between Zones:** Reduces latency and EMI susceptibility (particularly relevant for airside cabling near aircraft)

**Bandwidth Estimate (Pilot Phase, indicative):**

| Zone | Est. Cameras | Bitrate (H.265) | Est. Total Mbps |
|---|---|---|---|
| Check-in | ~8 cameras + 2 Xovis | ~4 Mbps each | ~32 Mbps |
| Security | ~10 cameras + 2 Xovis | ~4 Mbps each | ~40 Mbps |
| Support (NVR, analytics, monitoring) | — | — | ~20 Mbps |
| **Pilot Estimate** | ~24 devices | — | **~90–100 Mbps** |

This is well within standard Gigabit capacity; the design constraint is isolation (VLAN) and PoE power budget, not raw bandwidth, at pilot scale. **Full deployment (150–200 cameras) bandwidth and switch sizing should be modeled only after pilot data confirms per-camera bitrate in real operating conditions** — H.265 compression efficiency varies significantly with scene motion (crowded terminals compress less efficiently than the vendor's lab conditions).

**Network Infrastructure Investment (Pilot, indicative — confirm post-survey):**
- CCTV core switch and zone PoE switches: to be scoped against existing switch inventory
- Cabling + fiber (labor + materials): to be scoped against site survey floor plans
- **A firm quote requires the Week 1–2 site survey output; do not commit budget against the estimate above.**

---

### Component 2: Collins Integration & APOC Alignment

#### **2a. Collins Systems Integration Map**

CTG currently operates **Collins AODB/RMS/FIDS** (the iFIMS platform, per the RFP correspondence). This is the system-of-record for flight operations, gates, and passenger counts. The video analytics platform must integrate with it to enable predictive analytics based on flight schedules.

**Important open item:** The specific API surface, authentication model, and rate limits for CTG's Collins iFIMS instance are **not yet known to Waisl** and must be obtained from Collins/CTG IT before integration design can be finalized. The integration pattern below is Waisl's standard approach from prior Collins integrations (DEL, HYD, DXB) and should be treated as a **starting hypothesis**, not a confirmed spec.

**Integration Points (target state):**

| Collins System | Data Flow | Use Case | Integration Method (to be confirmed) |
|---|---|---|---|
| **AODB (iFIMS)** | Pull: Flight schedule, passengers, delays, aircraft type | Predict check-in/security congestion based on flight wave | API (REST or SOAP — confirm with Collins) |
| **RMS (Resource Management)** | Pull: Gate assignment, turnaround time, SLA targets | Gate utilization KPIs (#19); turnaround efficiency (#25–28) | API (confirm with Collins) |
| **FIDS (Flight Info Display)** | Pull: Display content, gate announcements, real-time OTP | Correlate gate display accuracy to passenger flow (#20); detect gate changes | API (confirm with Collins) |
| **Baggage System (if separate)** | Pull: Belt status, bag count by flight | First/last bag times (#29–30); belt availability (#31) | API if exposed; otherwise CCTV-only fallback |

**Architecture Diagram (target state):**

```
        ┌─────────────────────────────────────┐
        │   Collins iFIMS Cluster              │
        │   ├─ AODB (Flight Operations DB)    │
        │   ├─ RMS (Resource Management)      │
        │   └─ FIDS (Flight Info Display)     │
        └─────────────────┬───────────────────┘
                          │ (API — spec TBD with Collins)
        ┌─────────────────▼───────────────────┐
        │   Waisl Integration Adapter          │
        │   ├─ Collins API client              │
        │   ├─ Data transformation             │
        │   ├─ Caching layer                   │
        │   └─ Error handling + retry logic   │
        └─────────────────┬───────────────────┘
                          │
        ┌─────────────────▼───────────────────┐
        │   Data Lake (CTG Warehouse)          │
        └─────────────────┬───────────────────┘
                          │
        ┌─────────────────▼───────────────────┐
        │   Analytics Engine (Waisl AIOP)      │
        └─────────────────┬───────────────────┘
                          │
                ┌─────────┴─────────┐
        ┌───────▼─────┐      ┌──────▼────────┐
        │ BI Dashboard│      │ Alert Engine  │
        └─────────────┘      └───────────────┘
```

#### **2b. Data Exchange — What We Need From Collins Before Design Freeze**

Rather than presenting a fabricated API contract, the honest technical starting point is a **request list** for CTG's IT/Collins administrator:

1. Does iFIMS expose a REST or SOAP API for flight schedule, gate, and passenger-count queries? Documentation reference?
2. What authentication method is supported (API key, OAuth 2.0, mutual TLS, VPN-only access)?
3. What is the polling rate limit, and is a push/webhook model available instead of polling?
4. Is there a sandbox/test environment, or must integration be developed against production?
5. Who is the technical point of contact for API access provisioning and change control?

**Waisl's standard integration pattern (used at DEL/HYD/DXB), pending confirmation against CTG's actual API:**
- Poll for upcoming flights on a short interval (e.g., every 5 minutes) for a 2–4 hour lookahead window
- Transform flight data into predictive features (passenger count + historical flow pattern → predicted congestion)
- Push threshold-breach alerts to the dashboard
- Log all queries for audit and data governance

**Data Retention in CTG Lake (subject to CTG Legal sign-off):**
- Real-time: Flight data cached with short TTL
- Historical: Flight schedule + actual pax + performance metrics retained for a defined window (recommend starting at 90 days, revisit after legal review)

---

#### **2c. Predictive Queue Models (Powered by Collins Data)**

The integration is intended to enable models that predict congestion ahead of time. **These models do not exist yet and cannot be pre-validated without CTG operational data** — the description below is the design approach, not a delivered capability.

**Model 1: Check-in Congestion Forecast — Design Approach**

Inputs: upcoming flights (from Collins), passengers per flight, historical check-in time per passenger (to be measured during pilot, not assumed), current queue length (from Xovis), current staff headcount.

Logic sketch:
```
predicted_wait_time = (upcoming_pax_count × observed_time_per_pax) / num_open_counters
if predicted_wait_time > SLA_threshold:
  → alert with staffing recommendation
```

The **SLA threshold and time-per-pax figures must come from CTG's own operational data**, gathered in the first 4–6 weeks of pilot operation, not from generic industry assumptions.

**Model 2: Security Throughput Forecast — Design Approach**

Same structure, applied to security lanes: predicted throughput vs. SHA SLA, triggering a lane-opening recommendation if a breach is forecast.

**Model Accuracy — Honest Expectation:**
- **Pilot phase:** Accuracy will start low and improve as the model is trained on CTG-specific data (4–6 weeks minimum before the prediction is trustworthy enough to act on operationally)
- **No accuracy percentage should be promised to CTG leadership until pilot data exists to measure it against**

---

### Component 3: Existing Operational Systems Integration

#### **3a. CUPPS (Check-In System) Integration**

**Current State:** CUPPS (Common User Processing System) is referenced as the airline check-in platform used at CTG's check-in counters. Its exact vendor, version, and whether it exposes an API are **not yet confirmed** — this needs to be part of the site survey / IT discovery, not assumed.

**Integration Opportunity (if API access is available):**

| Data Point | Potential Use | KPI Impact |
|---|---|---|
| Counter open/close events | Reconcile with CCTV desk-manning detection | Validate desk-manning alerts (#22) |
| Boarding pass issue times | Calculate actual service time per pax vs. CCTV-derived queue length | Validate check-in throughput (#1–2) |
| Flight-to-passenger mapping | Link video-based counts to specific flights | Enable flight-level resource planning (#15) |

**Fallback if no API access:** The platform can operate on CCTV + Xovis + Collins data alone; CUPPS integration is a validation/accuracy enhancement, not a hard dependency for the pilot's core KPIs.

---

#### **3b. Wi-Fi / BLE Sensor Integration**

**Current State:** Airport WiFi coverage exists for passengers (per email thread); BLE deployment is not currently in place at CTG.

| Sensor Type | Current State | Pilot Role | Full Deployment |
|---|---|---|---|
| **WiFi Triangulation** | Existing (operational, exact coverage TBD) | Optional: anonymized device-density proxy for validation | Optional cross-check against CCTV occupancy |
| **BLE Beacons** | Not deployed | **Out of scope for Pilot** | Contractual requirement — defer to Phase 2 decision point |

**Recommendation for Pilot:**
- Defer BLE beacon deployment out of the pilot scope; it adds cost and complexity without being required for the pilot's core zone-level KPIs (queue time, throughput, occupancy)
- Flag to CTG explicitly that BLE is a stated contractual requirement in the source RFP document and that Waisl's position is it can be met via an alternative (camera analytics + DCS/e-boarding data, per Vinay's email) — **this substitution needs CTG's explicit sign-off before the Gate B presentation**, since the RFP frames it as a requirement, not a suggestion

**Deferral Rationale:** BLE provides end-to-end journey tracking (entry → check-in → security → gate); pilot KPIs are zone-level. Journey tracking has value in Phase 2 for advanced flow analytics but is not required to prove the pilot's core business case.

---

### Component 4: Data Architecture & KPI Calculation

#### **4a. Data Lake Schema (CTG-Owned) — Design Proposal**

The following is a proposed schema structure, not an implemented system. It illustrates how raw and aggregated data would be organized in the CTG-owned data warehouse.

```sql
-- Raw Event Streams (real-time ingestion)
events.video_analytics_stream {
  timestamp,
  zone_id,
  event_type,             -- 'person_count', 'queue_length', 'dwell_time'
  value,
  confidence,
  source_camera_id,
  source_sensor_type      -- 'CCTV', 'Xovis', 'LiDAR', 'WiFi'
}

events.collins_stream {
  timestamp,
  event_type,              -- 'flight_created', 'gate_assigned', 'on_block', 'off_block'
  flight_id,
  flight_number,
  aircraft_type,
  passengers,
  gate_id,
  scheduled_time,
  actual_time
}

events.cupps_stream {
  timestamp,
  event_type,              -- 'checkin_complete', 'counter_open', 'counter_close'
  counter_id,
  flight_id,
  service_time_seconds,
  pax_count
}

-- Aggregated KPI Tables (calculated via Waisl AIOP)
kpi.queues_hourly {
  hour, zone, avg_queue_length_m, max_queue_length_m,
  avg_wait_time_min, p95_wait_time_min,
  throughput_pax_per_hour, confidence_score
}

kpi.occupancy_hourly {
  hour, zone, avg_occupancy_pct, peak_occupancy_pct, dwell_hotspots
}

kpi.gate_utilization_hourly {
  hour, gate_id, gate_type, utilization_pct, turnaround_time_min
}

kpi.asq_baseline {
  survey_date, dimension, satisfaction_score, correlated_kpi, p_value
}
```

**Data Retention Policy (proposed, pending CTG Legal review):**
- Raw event streams: short rolling window (real-time ingestion only)
- Hourly KPI aggregates: 90-day rolling (enables ASQ analysis, anomaly detection)
- Historical baseline: 12-month yearly (seasonal trend analysis)

---

#### **4b. KPI Calculation Pipeline — Illustrative Pseudocode**

The following pseudocode illustrates the calculation *logic*, not production code. Actual thresholds (SLA minutes, throughput baselines) are placeholders pending CTG's real operational data.

**KPI #1: Check-in Average Queue Time (per hour)**

```python
# Illustrative logic only — thresholds are placeholders pending CTG baseline data
for hour in hourly_windows:
    queue_samples = video_analytics_stream.filter(
        zone='check_in', event_type='queue_length', time_window=hour)
    avg_queue_length = mean(queue_samples.value)
    # throughput_per_counter must be measured on-site, not assumed
    estimated_wait_time = avg_queue_length / (num_open_counters * throughput_per_counter)
    kpi['checkin_avg_wait'] = estimated_wait_time
```

**KPI #5: Security Throughput (per lane, per hour)**

```python
for hour in hourly_windows:
    pax_exited = xovis.count_out.filter(zone='security', hour=hour)
    num_open_lanes = cctv.lane_status.filter(zone='security', hour=hour).sum(is_open)
    throughput_per_lane = pax_exited / max(num_open_lanes, 1)
    kpi['security_throughput'] = throughput_per_lane
```

**KPI #10: Predictive Check-in Congestion (design pattern)**

```python
# Runs periodically; model trained on CTG pilot data, not pre-trained
upcoming_flights = collins_api.get_flights(next_2_hours)
upcoming_pax = sum(f.passengers for f in upcoming_flights)
predicted_wait = trained_model.predict(
    pax_count=upcoming_pax, hour_of_day=current_hour,
    queue_length_current=xovis_current_queue)
if predicted_wait > sla_threshold:  # SLA to be set with CTG, not assumed
    push_alert(...)
```

**KPI Update Frequency (target design, to be tuned during pilot):**
- Real-time metrics: near-real-time refresh (target ~1 min, subject to sensor latency)
- Predictive metrics: refreshed on each Collins poll cycle
- Hourly/daily aggregates: published on schedule for management reporting

---

#### **4c. Data Quality & Validation Framework**

**Validation Checks (design intent):**

| Check | Trigger | Action |
|---|---|---|
| **Camera Offline Detection** | No frames received beyond threshold | Alert to ops; flag affected KPIs as unreliable; escalate to IT |
| **People Count Anomaly** | Count deviates sharply from recent baseline | Review ML model; check for camera occlusion or lighting change |
| **Collins API Failure** | No data received beyond threshold | Fall back to CCTV-only predictions; escalate to Collins support |
| **Queue Time Validation** | Calculated wait time outside plausible bounds | Data quality alert; investigate source sensor malfunction |
| **Throughput Sanity Check** | Throughput implausibly exceeds physical lane capacity | Anomaly alert; investigate data source |

**Confidence Scoring (design pattern):**

Each KPI should be tagged with a confidence indicator combining camera availability, model accuracy (once measurable), data freshness, and validation-check pass rate. Exact weighting and thresholds should be calibrated during the pilot rather than fixed in advance — presenting a precise formula now would imply false precision.

---

### Component 5: Phased Deployment Timeline & Existing Infrastructure Coordination

#### **5a. Pilot Phase Roadmap (Q1–Q2 2027) — Indicative, ~28 Weeks**

```
Week 1–2: Pre-Deployment Assessment
├─ Site survey (terminal architecture, existing camera audit — count/model/firmware/ONVIF)
├─ Network assessment (bandwidth, PoE availability, cabling routes)
├─ Collins IT discovery (API availability, auth model, sandbox access)
├─ CUPPS IT discovery (API availability)
├─ Stakeholder kickoff (CTG ops, Collins admin, IT)
└─ Finalize camera placement design (2D floor plans + FOV overlays)

Week 3–6: Network Infrastructure Build
├─ Deploy CCTV VLAN (separate from operational LAN)
├─ Install/confirm PoE switches in check-in + security zones
├─ Lay cabling (new runs + fiber where needed)
├─ Validate network throughput under realistic load
└─ Network acceptance test (IT sign-off)

Week 7–10: Camera & Sensor Deployment
├─ CTG procures/installs new & replacement cameras per Waisl's Week 1–2 spec
├─ Waisl installs and configures Xovis overhead sensors (Waisl-supplied)
├─ Waisl configures ONVIF streams from CTG's cameras into the analytics pipeline
├─ Field-test all cameras (frame rate, bitrate, image quality)
└─ Achieve full camera connectivity for pilot zones
   (Camera hardware = CTG procurement; Xovis + integration = Waisl scope)

Week 11–14: Image Storage Integration
├─ CTG deploys/hosts NVR + storage on its own on-prem infrastructure (CTG-owned, per DPA-avoidance agreement)
├─ Waisl configures retention/access per agreed data policy
├─ Waisl integrates storage system with analytics platform
├─ Load-test recording of pilot camera count
└─ Storage integration acceptance test

Week 15–18: Analytics Platform Setup
├─ Deploy analytics servers (primary + hot-standby)
├─ Configure Collins AODB/RMS API connectivity (pending Week 1–2 discovery)
├─ Load historical Collins data where available
├─ Build KPI calculation pipelines (14 pilot KPIs)
├─ Begin training people-counting/predictive models on live field data
└─ Analytics system acceptance test

Week 19–22: Dashboard & Operations Training
├─ Deploy dashboard (KPI boards, alert pages)
├─ Configure real-time alerts (dashboard, and SMS/email if required)
├─ Train CTG ops team
├─ Establish local L1 support team
├─ Shadowing period (Waisl + CTG teams co-manage dashboard)
└─ Sign-off on readiness (CTO + Ops Manager)

Week 23–28: Pilot Operations + Validation
├─ Continuous system operation
├─ Monitor KPI accuracy vs. manual counts (regular validation runs)
├─ Refine models as historical data accumulates
├─ Collect ops team feedback (dashboard UX, alert tuning)
├─ Weekly steering committee review
└─ Assess pilot success criteria

**Pilot Success Criteria (Gate to Full Deployment):**
- 14 core KPIs operational with ≥95% data availability
- People-counting accuracy validated against manual audit counts (target ≤5% error, to be confirmed as achievable during pilot)
- Queue detection accuracy validated against manual observation
- Real-time dashboard uptime meets an agreed operational target
- Ops team trained and confident (structured feedback survey)
- Demonstrated real-time operational value (documented staffing interventions driven by alerts)
- No data privacy incidents or compliance violations
```

**Timeline Summary (Pilot, indicative):** ~28 weeks total, targeting completion by end of Q2 2027. **This is a planning estimate; the real critical path depends on procurement lead times and Collins/CUPPS API access, both unknowns until Week 1–2 discovery is complete.**

---

#### **5b. Full Deployment Phase (Q2–Q3 2027, contingent on pilot go/no-go)**

```
Week 1–4: Expansion Design & Procurement
├─ Design camera placement for gates, baggage, airside
├─ Procure additional cameras and Xovis units (quantities set by pilot learnings)
├─ Order PoE switches for expanded zones
└─ Finalize procurement + delivery schedule (confirm lead times with vendors)

Week 5–8+: Phased Zone Deployment
├─ Gates, baggage claim, airside, immigration — deployed in parallel where construction allows
└─ Coordinate deployment windows with CTG construction schedule

Week 9–12: Full Analytics Integration
├─ Scale analytics platform (federated servers per zone)
├─ Integrate all 39 mandatory KPIs + 15 maturity KPIs
├─ Integrate ASQ survey data pipeline
├─ Full terminal training (expanded staff)
└─ Full system acceptance test

Week 13–16: Full Operations + Optimization
├─ Continuous full-terminal operation
├─ Model fine-tuning
├─ Address blind spots identified during pilot
└─ Publish first full-terminal ASQ correlation report
```

**Coordination with CTG Construction:** Terminal expansion completes Q4 2027 per the RFP brief; the deployment plan targets full video analytics operational status roughly one quarter ahead, to allow tuning time before new facilities open. This depends on construction-zone access being available on the assumed schedule — should be validated jointly with CTG's construction PMO, not assumed from the email thread alone.

---

#### **5c. Existing Infrastructure Reuse — Framework, Not Final Numbers**

**Do not commit to specific reuse counts or savings figures until the Week 1–2 site survey is complete.** The framework below shows *how* reuse decisions will be made, using placeholder ranges only to illustrate the shape of the analysis.

| Asset Category | Reuse Decision Driver | Illustrative Range (subject to survey) |
|---|---|---|
| Existing IP cameras | ONVIF compliance + resolution ≥ 3MP + physical placement matches pilot zone needs | Reuse rate to be determined |
| PoE network switches | Spare capacity + PoE+ (95W) support | Reuse rate to be determined |
| Fiber/cabling backbone | Physical proximity of existing runs to pilot zones | Reuse rate to be determined |
| CTG internal IT staff | Availability for integration support, reduces Waisl resourcing need | To be scoped with CTG IT lead |

---

#### **5d. Indicative Cost Structure (Order-of-Magnitude, Not a Quote)**

CTG has indicated an approximate budget of USD 1.2M for this scope (per the RFP email thread). The cost categories below are provided to show the *shape* of spend across hardware, software, and labor — **treat every figure as a placeholder for the commercial proposal, not a committed price.** A firm quote requires: (1) site survey camera-reuse confirmation, (2) Collins/CUPPS API access confirmation, (3) vendor pricing at time of procurement, and (4) CTG's final scope decisions (e.g., BLE in/out, LiDAR in/out).

**In Waisl's Quote (Pilot, order of magnitude):**

| Category | Includes | Cost Driver |
|---|---|---|
| Xovis sensors | 4–6 units (100% new, Waisl-supplied) | Fixed by pilot design; premium per-unit cost |
| Analytics servers | Primary + hot-standby, GPU-capable | Fixed architecture requirement |
| Network build-out | New PoE switches, cabling, CCTV VLAN configuration | Depends on existing switch/cable reuse |
| Software licensing | Waisl AIOP platform + dashboard tooling | Annual license model |
| Installation & integration labor | Site work, Collins/CUPPS integration, training | Largest cost component; depends on API access complexity |

**Outside Waisl's Quote (CTG's Direct Capital Spend):**

| Category | Includes | Owner |
|---|---|---|
| New/replacement cameras | Per Waisl's spec (Component 1b); count confirmed post-survey | CTG procurement |
| Image storage / NVR infrastructure | On-prem server + backups, per DPA-avoidance agreement | CTG procurement, Waisl integrates |

**Full Deployment Cost Categories (order of magnitude, Phase 2):**

| Category | Includes | Owner |
|---|---|---|
| Additional cameras | Gates, baggage, airside coverage | CTG procurement (Waisl-specified) |
| Additional Xovis / LiDAR / thermal | Full-terminal sensor coverage per KPI requirements | Waisl quote |
| Additional storage capacity | Zones 3–6 | CTG procurement, Waisl integrates |
| Expanded network infrastructure | Additional PoE switches, fiber runs | Waisl quote |
| Expanded integration & training | Broader KPI set, larger ops team | Waisl quote |

**Why this split matters for the ~USD 1.2M figure Carlos referenced:** that number describes CTG's *total* budget envelope for the initiative, not Waisl's addressable quote. Since cameras and image storage are excluded from Waisl's scope, Waisl's actual commercial quote should be a **subset** of the 1.2M, with the remainder covering CTG's direct camera/storage capital spend. This should be made explicit to CTG leadership to avoid a mismatch between "budget available" and "price quoted."

**Recommendation to CTG:** Request that Waisl's commercial team deliver a firm, itemized quote **after** the Week 1–2 site survey and Collins/CUPPS IT discovery — not before. Presenting precise unit-cost totals today, before camera reuse and API access are confirmed, would create false confidence in a number that is likely to move.

---

### Component 6: Existing vs. New Infrastructure Matrix

This matrix shows the *decision framework* for what stays, what's new, and what's integrated. Quantities are marked "TBD — site survey" where CTG-specific data is required before commitment.

```
┌────────────────────────────────────────────────────────────────┐
│                  INFRASTRUCTURE REUSE MATRIX                    │
├────────────────────────────────────────────────────────────────┤
│ Component              │ Existing        │ New          │ Decision Basis        │
├─────────────────────────┼─────────────────┼──────────────┼────────────────────────┤
│ CAMERAS  — OUT OF WAISL SCOPE (CTG procures; Waisl specifies + integrates only) │
│ Newer IP Cameras        │ TBD — survey    │ CTG buys per │ ONVIF + resolution     │
│                        │                 │ Waisl spec   │ check                  │
│ Older IP Cameras        │ TBD — survey    │ 0            │ Repurpose to general   │
│                        │                 │              │ security if non-       │
│                        │                 │              │ compliant (CTG action) │
├─────────────────────────┼─────────────────┼──────────────┼────────────────────────┤
│ SENSORS                                                                          │
│ Xovis Queue Counter     │ 0 units         │ 4–6 units    │ NEW: Not currently      │
│                        │                 │              │ deployed at CTG         │
│ LiDAR Occupancy         │ 0 units         │ Phase 2 only │ NEW: Deferred past     │
│                        │                 │              │ pilot                  │
│ Thermal (FOD)           │ 0 units         │ Phase 2 only │ NEW: Airside, full     │
│                        │                 │              │ deployment only        │
├─────────────────────────┼─────────────────┼──────────────┼────────────────────────┤
│ NETWORK                                                                          │
│ Airport Core Switch     │ Existing        │ —            │ REUSE: Uplink for      │
│                        │                 │              │ CCTV VLAN, if capacity │
│                        │                 │              │ confirmed              │
│ PoE Switches            │ TBD — survey    │ TBD          │ Mixed, per spare       │
│                        │                 │              │ capacity + PoE+ rating │
│ Fiber Cabling           │ TBD — survey    │ TBD          │ Reuse where proximate  │
├─────────────────────────┼─────────────────┼──────────────┼────────────────────────┤
│ STORAGE — OUT OF WAISL SCOPE (CTG owns/hosts on-prem; Waisl integrates only)     │
│ NVR / Image Storage     │ 0 units (likely)│ CTG procures │ CTG hosts on-prem +    │
│                        │                 │ + hosts      │ backups, per DPA-      │
│                        │                 │              │ avoidance agreement    │
├─────────────────────────┼─────────────────┼──────────────┼────────────────────────┤
│ ANALYTICS                                                                        │
│ Video Analytics Server  │ 0 units         │ New (2)      │ NEW: GPU-enabled,      │
│                        │                 │              │ primary + backup       │
│ Data Warehouse          │ TBD — CTG IT    │ Possibly new │ REUSE if CTG has       │
│                        │                 │              │ enterprise DB capacity │
├─────────────────────────┼─────────────────┼──────────────┼────────────────────────┤
│ INTEGRATION POINTS                                                               │
│ Collins AODB/RMS/FIDS   │ Existing        │ —            │ INTEGRATE: API spec    │
│                        │ (airport owned) │              │ TBD — Collins IT       │
│                        │                 │              │ discovery required    │
│ CUPPS Check-in System   │ Existing        │ —            │ INTEGRATE IF POSSIBLE: │
│                        │ (airline owned) │              │ API availability TBD  │
│ WiFi Infrastructure     │ Existing        │ —            │ OPTIONAL: validation   │
│                        │                 │              │ cross-check only       │
└────────────────────────────────────────────────────────────────┘
```

---

### Component 7: Risk Register & Mitigation Strategy

| Risk | Impact | Probability | Mitigation | Owner |
|---|---|---|---|---|
| **Collins API access/spec unknown** | Integration design cannot be finalized; timeline risk | High (currently unresolved) | Prioritize Collins IT discovery in Week 1–2; escalate to CTG leadership if access is delayed | Waisl + CTG IT |
| **Existing camera inventory unverified** | Procurement/cost estimates inaccurate until survey done | High (currently unresolved) | Site survey Week 1–2 is a hard prerequisite before any hardware order is placed | Waisl |
| **Camera Network Congestion** | Video bitrate exceeds available capacity; frame drops | Low-Medium | Dedicated VLAN + zone-based switch sizing based on survey data | CTG IT |
| **CCTV Coverage Gaps (Blind Spots)** | Certain KPIs (gate queue, baggage dwell) unreliable | Medium | Pilot includes coverage validation; adjust camera angles before full deployment commitment | Waisl + CTG Ops |
| **ML/Predictive Model Accuracy Below Useful Threshold** | KPI confidence low; ops team doesn't trust alerts | Medium | Continuous retraining during pilot; manual count validation; no accuracy promised pre-pilot | Waisl |
| **Staff Adoption / Training Burden** | Dashboard unused; value not realized | Medium | Structured ops team training + shadowing period built into pilot timeline | CTG HR + Waisl |
| **Data Privacy Compliance Violation** | Regulatory sanction; reputational damage | Low | Anonymize at source (hashed IDs, aggregated counts); retention policy agreed with CTG Legal before go-live | Waisl + CTG Legal |
| **Construction Delays (Terminal Expansion)** | New zones unavailable per deployment plan | Medium | Flexible phasing: pilot (check-in/security) can proceed independently of gate/airside construction status | CTG Project Mgmt |
| **BLE Requirement Not Formally Waived** | RFP compliance gap if camera-based substitution isn't accepted | Medium | Get explicit CTG sign-off on the camera+DCS substitution for BLE before Gate B presentation | Waisl + CTG Procurement |
| **Waisl Resource Availability** | Key personnel unavailable during critical weeks | Low | Staffing plan should include buffer; confirm with Carlos/Vinay's team before committing dates | Waisl HR |
| **Budget Envelope Misread by CTG** | CTG expects the full ~USD 1.2M to cover Waisl's quote; camera/storage capex is separate | Medium | Clarify scope boundary (cameras + storage = CTG capex, not Waisl quote) explicitly in the initial draft presentation, not left implicit | Waisl + Carlos |
| **KPI/SLA Thresholds Not Yet CTG-Validated** | The 39-KPI mandatory set (and its indicative SLA thresholds, e.g. "check-in queue > X min") is distilled from a larger internal Waisl master KPI/TOR template, not from a document CTG itself produced — the RFP email thread contains no numeric KPI thresholds. Presenting these as confirmed CTG requirements risks credibility if challenged | Medium-High | Frame the 39 KPIs to CTG explicitly as "Waisl's proposed starting framework based on industry practice — thresholds open for CTG validation," not as pre-agreed requirements | Waisl |
| **CCTV Consulting Package Budget Conflicts With RFP Scope** | The internal CCTV deployment package (Executive Summary / Deployment Strategy / Site Survey docs) prices a $510K all-in budget that includes camera hardware (~$120K) and NVR/storage (~$100K) as Waisl-costed line items — this directly contradicts Carlos's email that cameras and image storage are CTG's responsibility, not Waisl's quote | High (internal document conflict, must be resolved before Aug 25) | Reconcile the CCTV package's cost model with the RFP scope boundary before pulling any figures from it into the client-facing presentation; do not quote the $510K figure as-is | Waisl (Sujoy + Carlos) |

---

---

## PART III: IMPLEMENTATION ARTIFACTS & APPENDICES

### Appendix A: 39 Mandatory KPIs — Grouped Summary

**Group 1: Passenger Flow & Queue (9 KPIs)**
#1–2: Check-in Queue (avg/peak) · #3–6: Security Queue/Wait/Throughput/SBD · #7: Gate Boarding Queue · #8: Passenger Hourly Flow · #9: Immigration Processing Time

**Group 2: Predictive Saturation (5 KPIs)**
#10–11: Predictive Check-in/Security Congestion · #12: Passenger Dwell Hotspots · #13: Resource vs Demand Mismatch · #14: Passenger Flow Trend

**Group 3: Collins Integration & APOC (6 KPIs)**
#15: Check-in Counter Requirement Per Flight · #16: ATM Variance · #17: On-Time Performance (OTP) · #18: Passenger Numbers (Arr/Dep) · #19: Gate Utilization · #20: Counter Open vs Schedule Adherence

**Group 4: Staff Resource Effectiveness (4 KPIs)**
#21: Desk Utilization · #22: Desk Not Manned (Alert) · #23: Security Lane Availability · #24: Optimal Staff Headcount (Recommendation Engine)

**Group 5: Turnaround & Aircraft Operations (4 KPIs)**
#25–28: On/Off-Block Times, Turnaround Efficiency

**Group 6: Baggage Processing (4 KPIs)**
#29–30: Domestic/International First Bag Time · #31: Belt Availability · #32: Predictive First/Last Bag Breach (Maturity-tier, pilot baseline included)

**Group 7: Security & Safety (3 KPIs)**
#33: Unattended Bag Detection · #34: Unauthorized Access to Restricted Areas · #35: CCTV System Availability

**Group 7b: Airside Safety & Operations (3 KPIs)**
#36: FOD Detection · #37: Vehicle Speed Monitoring · #38: Incident/Accident Detection (all three Partial for pilot — CCTV-only; telemetry integration by full deployment)

**Group 8: Satisfaction & Benchmarking (1 KPI)**
#39: ASQ Baseline & Correlation to Operational Metrics

*(Full KPI specification with SLA, data source, and calculation method is maintained in `CTG-KPI-Proposal-List.md`.)*

---

### Appendix B: Camera Placement by Zone (Indicative — Confirm Against Survey)

| Zone | Est. Cameras | Coverage Intent | Notes |
|---|---|---|---|
| Check-in | ~6–8 cameras + 1–2 Xovis | Queue lanes + counter detail + overview | Pilot zone |
| Security | ~8–10 cameras + 1–2 Xovis | All lanes + X-ray + exit | Pilot zone |
| Gates | ~1–2 cameras per gate (podium + boarding) + 1 corridor camera per 2–3 gates | Podium + boarding area + corridor | Phase 2; **total gate count at CTG is not yet known to Waisl — confirm during site survey before sizing** |
| Baggage Claim | ~6–8 cameras | 3–4 carousels + claim area | Phase 2 |
| Airside | ~8–12 cameras + 1–2 thermal per apron zone | Stands + apron + taxiway | Phase 2 |
| Immigration | ~4–6 cameras | Counters + queue lanes | Phase 2 |

Detailed floor-plan-level FOV diagrams require the actual CTG terminal architectural drawings, which have not yet been shared with Waisl — request as part of pre-deployment package.

---

### Appendix C: Network Topology — See Component 1d Diagram

Detailed as-built network diagrams (VLAN segmentation, switch hierarchy, fiber runs, redundancy paths) will be produced as a deliverable of the Week 1–2 site survey, once existing network topology is documented.

---

### Appendix D: Collins Integration — Information Request Checklist

See Component 2b for the full discovery checklist required before API integration design can be finalized. No endpoint URLs, auth tokens, or rate limits should be published in any external-facing document until confirmed by Collins/CTG IT.

---

### Appendix E: Data Security & Privacy Framework

**Privacy-by-Design Principles (per RFP requirement and Waisl's stated commitment):**
1. Anonymization at source (hashed device IDs, no face recognition, no biometric enrollment by Waisl)
2. No personal data retention — counts and aggregates only, never identities
3. Data encryption in transit and at rest
4. Access controls (role-based access; audit logging for all data access)
5. Periodic privacy audits (cadence to be agreed with CTG Legal)

**Explicit RFP Constraint:** Per the source requirements, CTG — not Waisl — owns the data warehouse and any biometric enrollment solution/hardware. Waisl's storage role should be scoped accordingly to avoid exposure under data protection regulation (per Carlos's internal note on avoiding DPA exposure).

**Compliance approach:** Align to applicable data protection regulation for Colombia; specific certifications (ISO 27001 etc.) should be confirmed against Waisl's actual current certification status before being cited in a client-facing document — not assumed here.

---

### Appendix F: Operations Support Model — Design Proposal

**L1 Support (Local Waisl Team, per the "new requirement" noted by Carlos):**
- Dashboard triage (identify component failures)
- Camera/sensor hardware reset
- Network troubleshooting (first-line)
- Escalation to L2 for deep debugging

**L2 Support (Waisl Remote Team):**
- ML model debugging
- Collins API troubleshooting
- Escalation path for vendor-level issues

**Escalation structure and response-time SLAs:** to be defined jointly with CTG during the pilot planning phase, not unilaterally set by Waisl in this document.

---

### Appendix G: Success Metrics Framework (Structure, Not Pre-Set Targets)

| Metric Category | Baseline (Today) | Year 1 Target | How Target Will Be Set |
|---|---|---|---|
| Peak-hour check-in wait time | Unmeasured | To be set from pilot baseline | Measured in pilot Weeks 23–28, then targeted |
| Security throughput utilization | Unmeasured | To be set from pilot baseline | Measured in pilot |
| OTP (on-time performance) | Available from Collins AODB (existing metric) | Improvement target set jointly with CTG Ops | Existing data, new correlation analysis |
| Staff cost per passenger processed | Unmeasured | To be set from pilot baseline | Requires CTG staffing cost data |
| ASQ score | No baseline exists (per RFP: "totally blind to passenger experience data") | First-ever baseline established in pilot | ASQ survey program launch |
| System uptime | N/A (new system) | Target set jointly, informed by pilot reliability data | Pilot operations |
| People-counting accuracy | N/A (new system) | Validated against manual audit during pilot | Manual count comparison |

**This table intentionally does not pre-fill target numbers.** Committing to specific percentage improvements before a CTG baseline exists would be a fabricated promise. The pilot's primary deliverable, from a measurement standpoint, is *establishing the baseline this table is currently missing.*

---

---

## CONCLUSION & RECOMMENDATION

This case study outlines a phased video analytics deployment for CTG, structured around a **~28-week pilot** (check-in + security zones) that establishes CTG's first-ever operational baseline, validates Collins integration and camera-analytics accuracy, and produces a CTG-specific financial business case — before committing to full-terminal investment.

### Key Differentiators:

1. **Honest phasing:** No investment commitment beyond the pilot until real CTG data exists to justify it
2. **Existing infrastructure respected:** Camera reuse strategy is survey-driven, not assumed
3. **Open architecture:** ONVIF-standard hardware, REST APIs, CTG data ownership (per RFP requirement)
4. **Local support:** L1 team based locally, per the client's stated new requirement
5. **Regulatory alignment:** Anonymization-first design matches the RFP's explicit no-PII mandate

### What Must Happen Before August 25 Presentation:

1. **Site survey scheduling** — Carlos's planned August visit should gather the existing-camera inventory data this document flags as unverified
2. **Collins/CUPPS IT discovery** — request API documentation and sandbox access ahead of the visit if possible
3. **BLE substitution sign-off** — confirm with CTG whether camera+DCS tracking is an acceptable substitute for the RFP's stated BLE requirement
4. **Commercial team engagement** — a firm, itemized quote should be prepared in parallel, clearly separating "known" costs (Xovis, analytics servers — 100% new regardless of survey outcome) from "survey-dependent" costs (network build-out), and explicitly excluding camera hardware and image storage (CTG capex, per Carlos's email)

### Open Items Requiring CTG Input (Not Waisl Assumptions):

- Confirmed existing camera count, age, model, and ONVIF compliance
- Total gate count at CTG (needed to size gate-zone camera deployment — not stated in any source document reviewed)
- Collins iFIMS API access and documentation
- CUPPS API availability
- CTG's data retention policy preference (legal/compliance-driven)
- CTG's position on the BLE requirement substitution
- CTG's internal data warehouse infrastructure (reuse vs. new build)
- **ADS-B receiver availability** — On-Block/Off-Block Variance KPIs (#25–28) depend on VDGS/A-VDGS timing data; full accuracy additionally requires an ADS-B receiver, which is not confirmed as existing CTG infrastructure. Treat as a possible new hardware dependency, not yet priced into any quote
- Sign-off that the 39-KPI mandatory set and its indicative SLA thresholds — drawn from Waisl's internal master KPI template rather than a CTG-issued document — are an acceptable starting point for discussion, not a pre-agreed requirement set

---

**Prepared by:** Waisl Digital Solutions
**Reviewed by:** Sujoy Mukherjee, Solution Architect
**Date:** July 2026
**Classification:** Confidential — For CTG Leadership Discussion
