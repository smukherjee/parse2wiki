---
marp: true
theme: default
paginate: true
size: 16:9
---

<!-- _class: lead -->

# CTG Passenger Experience & Video Analytics Platform
## Executive Briefing — Strategic Overview

**Prepared for:** CTG Leadership (CEO / CTO)
**Prepared by:** Waisl Digital
**Date:** July 2026 | Confidential — For Discussion Purposes

---

## Why This, Why Now

- CTG is undertaking a **US$500M terminal expansion**: 25,000 m² → 44,000 m² by end of 2027
- Passenger volume growing **7M → 11M annually** by December 2027
- Today's scale is already significant: **~20–21K passengers/day** on average (peaking at ~22–25K/day in December–January), across **~75–80 flight movements/day**, through 1 runway, 15 gates, and a reported 72 check-in counters
- Today, **CTG has no objective visibility into any of this** — no data on queue times, congestion, or satisfaction drivers
- The Colombian Government / OINAC concession requires a technology solution for **"Passenger Experience in the New Normal"**
- Growth without visibility means growth without control — this is the moment to fix that, before the new terminal opens

---

## CTG Operates With Zero Passenger-Experience Visibility Today

**From blind operations to data-driven passenger experience management**

| Today | With the Platform |
|---|---|
| No visibility into queues, wait times, or crowding | Real-time flow and wait-time data across every touchpoint |
| Reactive staffing, based on instinct | Predictive congestion alerts, proactive staffing |
| No benchmark for passenger satisfaction | ACI ASQ-aligned satisfaction benchmarking vs 200+ global airports |
| Expansion investment with no way to prove ROI | Demonstrable, benchmarked transformation story for stakeholders and airlines |

---

## We're Proposing a Passenger Experience Intelligence Platform — Not a Camera System

- Combines **objective flow data** (video analytics, Xovis, Wi-Fi/BLE, LiDAR) with **subjective satisfaction data** (ACI ASQ surveys)
- Built on a **standard data warehouse + BI layer** — owned by CTG
- Integrates with your existing systems: **Collins AODB/RMS/FIDS, CUPPS, CUSS, Veripax (PTS)**
- Delivers a live **management/KPI dashboard** for operations and executive teams
- Modular and phased — deployed incrementally as your terminal expansion progresses

---

## How It Works — Simple View

```
 Sensors (cameras, Xovis, Wi-Fi/BLE, LiDAR)
              │
              ▼
   Waisl Analytics & AI Platform  ◄──►  Collins AODB/RMS/FIDS
              │
              ▼
    KPI Dashboard + ASQ Benchmarking
              │
              ▼
  Data-driven staffing & operational decisions
```

Anonymized at source — hashed identifiers, aggregated counts only. **No personally identifiable data collected or retained by Waisl.**

---

## CTG Retains Full Ownership of All Passenger Data and Infrastructure

We believe in a clean, low-risk ownership model from day one:

| Item | Owner |
|---|---|
| Cameras (hardware) | **CTG procures**, per Waisl's technical specification |
| Image storage & backups | **CTG-hosted, on-premise** |
| Data warehouse & analytics platform | **CTG-owned infrastructure**; Waisl-delivered software |
| Analytics, KPIs, dashboards, integration | **Waisl-delivered** |

**Why this matters to you:** CTG retains full control and ownership of sensitive passenger imagery and data — no third-party data protection exposure, full sovereignty over your own infrastructure.

---

## A Phased, Low-Risk Path

| Phase | Timing | What Happens |
|---|---|---|
| **1. Pilot** | Q1–Q3 2027 (~28 wks) | 2-zone proof of concept (check-in + security), existing infrastructure |
| **2. Full Deployment** | Q3–Q4 2027 | All zones live, aligned to construction completion |
| **3. Maturity** | Q1–Q2 2028 | Predictive analytics, root-cause intelligence |
| **4. Strategic Enhancement** | 2028+ | Digital twin, scenario simulation, advanced capability |

We do not ask CTG to commit to full-terminal deployment on day one — the pilot validates value before scaling.

*Timeline reconciled to the detailed 28-week pilot roadmap in the technical case study — supersedes earlier quarter-only estimates.*

---

## We've Deployed and Operate Similar Platforms at Delhi, Hyderabad, and Dubai

- Deployed and operating similar platforms at **Delhi (DEL), Hyderabad (HYD), Dubai (DXB)**
- **Dubai digital-twin** reference implementation available for CTG to review
- Entry-to-boarding passenger tracking proof-of-concept delivered in Dubai using camera + LiDAR fusion
- 15+ years of airport-specific video analytics deployment experience across the consulting team

---

## Addressing the Two Questions You're Likely Asking

**"Why Waisl, and not Collins — they already won a contract here and run our AODB/RMS/FIDS?"**
Collins' award covers airport systems of record (AODB/RMS/FIDS) — not passenger-experience analytics, video/sensor fusion, or ASQ benchmarking. Waisl's platform is designed to integrate *with* Collins, not replace it — CTG gets both systems working together rather than one vendor covering both jobs.

**"What could go wrong?"**

| Risk | Mitigation |
|---|---|
| Collins integration access delayed | Data access commitment requested today (see next slide); pilot's core KPIs can run on video/sensor data alone if Collins access slips |
| Pilot scope proves narrower than expected | Go/no-go gate before full-deployment spend — no commitment beyond the pilot until value is proven |
| Timeline compresses against the Dec-2027 construction deadline | Full deployment phased to shadow construction zone-by-zone, not a big-bang cutover |
| Full deployment window (Q3–Q4 2027) overlaps the July–August traffic peak | Sequence physical installation around peak days; confirm windows with CTG Ops during site survey |

---

## Comparable Airports See 4.1–4.3 ASQ Within 12 Months of Deployment

*Illustrative — based on comparable industry deployments, not a committed guarantee. To be validated against CTG's own baseline during the pilot.*

| Dimension | Typical Industry Result |
|---|---|
| ASQ overall satisfaction | Movement toward 4.1–4.3 / 5.0 (global peer average) |
| Peak-hour congestion incidents | Meaningful reduction through predictive staffing |
| Queue time | Reduction through proactive counter/lane management |
| Staff allocation | Shift from manual/reactive to data-driven |

CTG's own baseline will be established during the pilot phase via ASQ survey + operational data — real targets follow real measurement, not assumptions.

---

## ~US$1.2M All-In; Waisl's Quote Is a Subset, Confirmed After Site Survey

- We understand CTG's informal budget guidance is in the range of **~US$1.2M** for this initiative — **to be confirmed**, not a committed figure
- Investment splits into two distinct buckets:
  - **CTG capital expenditure:** camera hardware, on-prem image storage — sized and specified by Waisl, procured by CTG
  - **Waisl solution & services:** analytics platform, sensors (Xovis/LiDAR/thermal as needed), integration, professional services
- **Precise figures require a site survey** — current numbers are draft consultant estimates, not a quotation
- ROI case: reduced congestion incidents, improved staff efficiency, and a benchmarked ASQ story that supports airline partnerships and investor confidence in the expansion

---

## The Decision We Need Today: Approve the Site Survey

**What we're asking for:**
1. **Approval to proceed** to detailed technical design and on-site survey
2. **Confirmed budget envelope** for the Waisl solution & services scope
3. **Collins AODB/RMS/FIDS data access** commitment — this is a prerequisite for turnaround/baggage KPIs
4. **Decision support** on BLE approach — Waisl will recommend the best-fit option
5. **Confirmation of L1 local support model** (newly scoped requirement)
6. **Site visit access** — target: 2nd–3rd week of August 2026

**What happens next:**
- **Site visit:** Mid-to-late August 2026
- **Detailed technical proposal & pricing:** Following site survey
- **Pilot kickoff:** Q1 2027 (~28-week pilot, running through Q3 2027)
- **Full deployment complete:** Q4 2027, aligned with terminal construction completion

---

<!-- _class: lead -->

# Let's Build CTG's Passenger Experience Transformation Together

**Next step:** Confirm approval to proceed to technical design and site survey.

Questions & Discussion
