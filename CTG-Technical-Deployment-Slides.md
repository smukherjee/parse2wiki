---
marp: true
theme: default
paginate: true
size: 16:9
---

<!-- _class: lead -->

# CTG Video Analytics Platform
## Technical Deployment Briefing

**Audience:** IT Managers, Airport / Terminal Operations Managers, Facilities
**Prepared by:** Waisl Digital — Solution Architecture & Consulting Team
**Date:** July 2026 | Following CxO approval to proceed

---

## Agenda

1. Solution architecture overview
2. Hardware specifications (cameras, sensors)
3. Zone-by-zone deployment plan
4. Network & bandwidth design
5. Storage & backend infrastructure
6. Systems integration (Collins, CUPPS, BHS, VDGS)
7. KPI measurement framework
8. Deployment methodology & site survey
9. Timeline, budget & procurement responsibility
10. Ownership & RACI — who does what
11. Risks & open items requiring your input

---

## 1. Solution Architecture Overview

```
[Cameras + Xovis + LiDAR + Thermal]  (CTG-procured, Waisl-specified)
              │  RTSP / ONVIF
              ▼
   [CTG On-Prem NVR + Image Storage]  ◄── CTG-owned, avoids DPA exposure
              │
              ▼
      [Waisl Analytics Server]  ── ML models, people-counting, queue detection
              │
              ▼
   [KPI Dashboard]  ◄──►  [Collins AODB/RMS/FIDS · CUPPS · BHS · VDGS]
              │
              ▼
        [CTG Data Warehouse]  ── CTG-owned; ASQ correlation & reporting
```

Anonymization at source: hashed device IDs, aggregated counts only — no PII in the pipeline.

---

## 2. Hardware Specifications — IP Cameras

| Spec | Requirement | Rationale |
|---|---|---|
| Resolution | 4MP (2688×1520) minimum, 5–8MP preferred | Adequate pixel density for people-counting |
| Sensor | Progressive scan CMOS | Eliminates motion blur for accurate tracking |
| Lens | 2.8mm (wide) – 6mm (detail zones) | Matched to zone: wide overview vs. desk-level detail |
| Frame rate | 30 FPS @ full resolution | Smooth tracking without excess bandwidth |
| Codec | H.265 (HEVC) | ~40–50% bandwidth/storage reduction vs H.264 |
| Low light | ≤0.1 lux w/ IR; WDR support | 24×7 airport operations |
| Power | High PoE (95W+) | Single-cable power + IR illumination |
| Compliance | ONVIF Profile S/T | Interoperability with analytics platform |

**Indicative models (consultant reference, not a mandated vendor list):** Hikvision DS-2CD2143G2-I/DS-2CD2643G2-IZS, Axis P1445-LE, Uniview IPC322SR-DVS28

---

## 2. Xovis Is Non-Negotiable; LiDAR Should Wait Until 2027 Q4

| Sensor | Purpose | Accuracy | Deployment Note |
|---|---|---|---|
| **Xovis (thermal overhead people counter)** | Queue length, throughput, dwell time | ≥99% | Non-negotiable for queue-critical KPIs (check-in, security) |
| **LiDAR** | 3D occupancy, dwell hotspot mapping | ±5cm | Optional — recommend deferring to maturity phase (Q4 2027+) |
| **Thermal cameras** | FOD detection, vehicle hot-spot monitoring (airside) | ±2°C, ≥300m range | Required for airside safety KPIs (#36–38) |

**Open question for CTG/Waisl to align on:** whether Xovis/LiDAR/thermal are treated as part of Waisl's analytics platform scope, or fall under the same CTG-procurement model as standard security cameras (see Slide — Budget & Procurement Responsibility).

---

## 3. CTG Infrastructure Baseline (Public-Source Estimates, Pending Site-Survey Confirmation)

| Element | Count | Confidence |
|---|---|---|
| Runways | 1 | Confirmed — public airport data |
| Contact stands | 7 | Confirmed — public airport data |
| Gates | 15 (Domestic 1–8, International 9–15) | Confirmed — public airport data |
| Arrival belts | 6 (3 domestic, 3 international) | Confirmed — public airport data |
| Security lanes | ~6 (3 domestic + 3 international, inferred from terminal map) | **Estimated only** — not officially disclosed; confirm on-site |
| Check-in counters | ~72 | **Unconfirmed** — single public source; verify during survey |
| Avg. daily passengers | ~20–21K, peaking at ~22–25K/day (Dec–Jan) | Confirmed — CTG's published airport statistics, 2024–2026 |
| Avg. daily flight movements | ~75–80 | Confirmed — CTG's published airport statistics, 2024–2026 |

These figures refine — but do not replace — the site survey. The zone camera counts below use them where confirmed, and flag them where still estimated.

---

## 3. Zone-by-Zone Deployment Plan (1/2)

| Zone | Camera Approach | KPIs Covered |
|---|---|---|
| **Check-in** | ~6–8 wide-angle overview cameras + 1–2 Xovis overhead, covering ~72 reported counters — verify per-counter resolution is adequate for desk-manning KPIs during survey | #1–2, #10, #21, #22, #24 |
| **Security** | ~8–10 cameras + 1–2 Xovis, sized against ~6 estimated lanes (3 domestic + 3 international) — lane count not officially disclosed, confirm on-site | #3–6, #11, #23 |
| **Gates** | 15 gates confirmed (Domestic 1–8, International 9–15) → ~15–30 podium/boarding cameras + ~6 corridor cameras (1 per 2–3 gates) ≈ **21–36 cameras total** | #7, #19, #20 |
| **Baggage Claim** | 6 arrival belts confirmed (3 domestic + 3 international) → ~6–8 cameras (1 per belt + claim-area overview) | #29–32 |

*Pilot zones: Check-in + Security. All other zones are Phase 2 (Full Deployment).*

---

## 3. Zone-by-Zone Deployment Plan (2/2)

| Zone | Camera Approach | KPIs Covered |
|---|---|---|
| **Airside (apron/stands)** | 7 contact stands confirmed → ~8–12 cameras + 1–2 thermal per apron zone + taxiway coverage | #25–28, #36–38 |
| **Immigration** | ~4–6 cameras | #9 |

> **Resolved:** Gate count confirmed at 15 (public source) — gate-zone camera sizing is now an absolute total, not just a ratio.
> **Still open:** Security lane count (~6, estimated from terminal map) and check-in counter count (~72, single public source) are not yet CTG-confirmed — validate both during site survey before finalizing the camera BOM.

---

## 4. Pilot Bandwidth Fits Existing Gigabit Capacity; Full Deployment May Need 10GbE

| Scenario | Bitrate | Infrastructure |
|---|---|---|
| Pilot (~80–100 cameras, H.265) | ~320 Mbps | Dedicated CCTV VLAN + Gigabit uplink |
| Full deployment (~150–200 cameras) | ~600 Mbps | Dual redundant Gigabit + optional 10GbE analytics tier |
| Peak/emergency recording | ~1.2 Gbps | 10GbE core + Gigabit edge |

**Design principles:**
- Isolate CCTV traffic on a **dedicated VLAN**, separate from airport operational LAN
- PoE+ switches (802.3bt, 95W+) per zone
- Fiber backbone between zones — reduces latency and EMI exposure (critical airside)
- Dual-path redundancy to NVR for high availability

*These figures are consultant estimates based on typical airport deployments — require validation against CTG's actual network topology during site survey.*

---

## 5. Storage Is CTG-Owned to Avoid DPA Exposure; Full-Scale NVR Capacity Is Still TBD

**Important scope note:** Per CTG's direction, **image storage is hosted on CTG's own on-premise infrastructure** — this avoids exposing Waisl to Data Protection Act (DPA) liability for stored passenger imagery. The specifications below are Waisl's technical guidance for CTG's storage design, not a Waisl-hosted service.

| Component | Guidance |
|---|---|
| **NVR retention** | 60–90 day rolling retention, RAID 5 minimum, dual NVR failover |
| **NVR capacity (pilot, indicative)** | ~150TB single-unit NVR (e.g., Hikvision DS-96128NI-I16 class, 150+ camera capacity) sized for the 2-zone pilot; full-deployment capacity (150–200 cameras) must be re-sized post-survey against confirmed camera count and final retention window |
| **Architecture** | Distributed NVR by zone (check-in / security / gates / baggage) to reduce latency |
| **Analytics server** (Waisl-operated) | 16+ core CPU, optional GPU (NVIDIA A100/RTX 4090) for ML acceleration, 64GB RAM, primary + backup for redundancy |
| **Data warehouse** | CTG-owned; Waisl integrates but does not host |

---

## 6. Systems Integration — What We Need From Your Teams

| System | Integration Need | Status |
|---|---|---|
| **Collins AODB (iFIMS)** | Flight schedule, delays, passenger loads — API/SOA | Requires access + sandbox environment |
| **Collins RMS / FIDS (iFIMS)** | Resource & flight info data | Requires access |
| **CUPPS** | Counter status, pax processed, queue data | Requires API/data export confirmation |
| **BHS (Baggage)** | First/last-bag timestamps — SCADA/OPC-UA | Requires planning; drives KPIs #29–32 |
| **VDGS / A-VDGS** | On-block/off-block docking signal | Preferred source for turnaround timing accuracy |
| **ADS-B receiver** | On/Off-Block Variance KPIs (#27–28) | **Not confirmed as existing infrastructure — potential new hardware dependency, unpriced** |

**Critical path risk:** Collins integration is a prerequisite for turnaround and baggage KPIs — commitment needed in the pilot phase to avoid derailing KPIs #25–32.

---

## 7. KPI Measurement Framework — Structure

**39 Mandatory KPIs** (pilot + full deployment baseline), organized into 9 groups:

| Group | KPIs | Focus |
|---|---|---|
| A. Passenger Flow & Queue Mgmt | 9 (#1–9) | Check-in, security, gates, immigration |
| B. Predictive Saturation | 5 (#10–14) | Congestion forecasting |
| C. Collins/APOC Alignment | 6 (#15–20) | Flight ops linkage |
| D. Staff Resource Effectiveness | 4 (#21–24) | Desk/lane manning, headcount |
| E. Turnaround & Aircraft Ops | 4 (#25–28) | On/off-block timing |
| F. Baggage Processing | 4 (#29–32) | First/last bag, belt availability |
| G. Security & Safety | 3 (#33–35) | Unattended bags, access, CCTV uptime |
| H. Airside Safety & Operations | 3 (#36–38) | FOD, vehicle speed, incidents |
| I. ASQ Standard & Satisfaction | 1 (#39) | Benchmark reporting |

Plus **15 Maturity KPIs** (Q2–Q4 2027) and **8 Good-to-Have KPIs** (2028+).

---

## 7. KPI Framework — Important Context

> **This 39-KPI framework is Waisl's proposed industry-practice starting point** — distilled from Waisl's internal master KPI/TOR template used across airport engagements, not derived from a CTG-issued requirements document. The RFP correspondence from CTG does not specify numeric SLA thresholds.

**Recommendation for this discussion:** treat the indicative SLA thresholds (e.g., "check-in queue ≥10 min") as a **draft for CTG operational teams to validate**, not a pre-agreed requirement set.

Several KPIs are marked **Partial** for pilot readiness — they require either a hardware dependency not yet confirmed (ADS-B, #27–28) or a post-pilot model training period (#10–11, #13, #24, #32).

---

## 8. Deployment Methodology — 8 Steps

1. **Pre-site assessment** (Wk 1–2) — terminal architecture, existing CCTV audit, network topology
2. **KPI-driven coverage analysis** (Wk 3–4) — map every KPI to required camera coverage
3. **Hardware selection & specification** (Wk 5–6)
4. **Detailed site survey** (Wk 7–8) — 100+ question questionnaire across 8 sections (A–H)
5. **Coverage design & placement validation** (Wk 9–10) — FOV maps, blind-spot mitigation
6. **Pilot deployment & validation** (Q1–Q3 2027, ~28 weeks) — check-in + security
7. **Full terminal deployment** (Q3–Q4 2027, ~16 weeks) — phased with construction schedule
8. **Optimization & tuning** (Q4 2027 onward) — recalibration, false-alert reduction

---

## 8. Site Survey — What We'll Need From CTG Teams

- **Facilities:** floor plans (CAD/PDF w/ dimensions), ceiling heights, structural obstacles, environmental conditions (coastal salt air, EMI zones)
- **IT:** network topology, current bandwidth capacity, PoE switch inventory, VLAN segmentation options, power/UPS availability
- **Operations:** existing CCTV inventory (Vivotek/Mobotix — age, count, capability), peak-hour queue/throughput baselines, top 3 operational pain points
- **Security:** restricted-area camera placement constraints, DPA/privacy regulatory requirements
- 3-day on-site survey; escorted access to restricted/airside areas required

---

## 9. Deployment Timeline (Consultant Draft — Subject to CTG Confirmation)

| Phase | Duration | Key Milestones |
|---|---|---|
| **Pilot** | ~28 weeks (Q1–Q3 2027) | Site survey → network build → camera/sensor deployment → storage integration → analytics setup → dashboard/training → operations & validation |
| **Full Deployment** | ~16 weeks (Q3–Q4 2027) | Gates/baggage/airside install → network scaling → ASQ baseline established |
| **Optimization** | Q4 2027 onward (continuous) | Blind-spot remediation, false-alert tuning, maturity KPIs activated |

**Pilot success criteria:** 95% uptime, <5% false alerts, ±10% queue-count accuracy, stakeholder sign-off ≥80%

*Note: this is the consultant's proposed methodology timeline — align with your own construction and procurement lead times before treating as committed. Pilot duration corrected to the detailed week-by-week roadmap in the CTG Video Analytics Case Study (Component 5a) — supersedes an earlier 12-week planning figure that undercounted the full site-survey-through-validation scope, and the earlier "Q1–Q2 2027" label, which was too narrow for a 28-week effort.*

---

## 9. Budget & Procurement Responsibility Matrix

Consultant draft estimate — **presented here with corrected ownership**, per the scope boundary CTG confirmed (cameras and image storage are not Waisl-costed items):

| Component | Est. Cost (Consultant Draft) | Owner |
|---|---|---|
| Camera hardware (IP cameras) | ~$120K | **CTG procures**, per Waisl spec |
| NVR + on-prem storage | ~$100K | **CTG procures & hosts** |
| Analytics server | ~$45K | Waisl-scope |
| Network infrastructure | ~$50K | Waisl-specified; CTG/shared procurement TBD |
| Installation & integration | ~$90K | To be allocated — TBD |
| Site survey & design | ~$10K | Waisl-scope |
| ASQ surveys & reporting | ~$40K | Waisl-scope |

**⚠ Do not treat the $510K "all-in" total from the original consultant estimate as a Waisl quotation** — it bundles CTG capital items. Final Waisl pricing to be issued after reconciliation and site survey.

---

## 10. Ownership & RACI — Who Does What

This consolidates the ownership notes scattered across the sensor, budget, and risk slides into a single reference.

| Workstream | Waisl | CTG-IT | CTG-Ops | CTG-Facilities | CTG-Security |
|---|---|---|---|---|---|
| Site survey | R/A | C | C | R | C |
| Camera procurement & install | C (spec only) | I | C | R/A | I |
| Xovis / LiDAR / thermal procurement & install | R/A | I | C | C | I |
| Storage hosting (NVR + backups) | C (integrates) | R/A | I | C | C |
| Network provisioning (VLAN, PoE, cabling) | C (specifies) | R/A | I | C | I |
| Collins AODB/RMS/FIDS access | C | R/A | C | I | I |
| ASQ survey design & fielding | R/A | I | C | I | I |
| Analytics platform & dashboard | R/A | C | C | I | I |
| L1 local support | R/A | C | C | I | I |

**R** = Responsible · **A** = Accountable · **C** = Consulted · **I** = Informed

---

## 11. Technical Risks & Open Items

| Risk / Open Item | Why It Matters | Needs |
|---|---|---|
| **ADS-B receiver availability** | Required for KPIs #27–28; not confirmed as existing infrastructure | CTG to confirm / budget as new hardware |
| **Security lane & check-in counter counts unconfirmed** | ~6 security lanes and ~72 check-in counters are public-source estimates, not CTG-confirmed — camera BOM for these zones could shift materially | Confirm exact counts during site survey |
| **Collins API/sandbox access** | Prerequisite for turnaround & baggage KPIs | CTG + Collins coordination, early commitment |
| **Xovis budget allocation** (~$30–40K) | Non-negotiable for accurate queue KPIs (40% of mandatory KPI set) | Confirm inclusion in approved scope |
| **Network bandwidth sharing** | 600 Mbps–1.2 Gbps needed; congestion risk if shared with airport LAN | Dedicated VLAN commitment from CTG IT |
| **Privacy/DPA compliance** | CCTV + tracking + on-prem storage = regulatory exposure | Privacy Impact Assessment before pilot |
| **KPI/SLA thresholds unvalidated by CTG** | Framework is Waisl's proposed starting point, not CTG-issued | Sign-off session with CTG ops stakeholders |
| **Full deployment window overlaps the Jul–Aug traffic peak** | ~75–80 flights/day and 22K+ pax/day during install could make physical camera/network work operationally disruptive | Sequence installation around peak days; confirm windows with CTG Ops during site survey |

---

<!-- _class: lead -->

# Next Steps

1. Confirm site survey dates and team availability (facilities / IT / ops / security)
2. Align on procurement responsibility for network infrastructure and installation
3. Confirm ADS-B and Collins integration decisions
4. Schedule KPI/SLA threshold validation session

Questions & Discussion
