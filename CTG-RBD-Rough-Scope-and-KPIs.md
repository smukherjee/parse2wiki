# CTG Passenger Experience Platform — Sizing Inputs for Product

**Audience:** Product team (hardware/server sizing, storage, cameras, integrations, wayfinding)
**Purpose:** This document is an **input package, not a sizing output.** It gives Product everything currently known — KPIs in scope, zones, confirmed/estimated airport infrastructure figures, sizing methodologies, and effort drivers — so Product can independently size: (1) hardware/server sizing, (2) storage, (3) cameras needed, (4) integrations, (5) wayfinding needed, and roll all five into an internal **cost/budget sheet**. That sheet is for internal use to drive the discussion with CTG during the Aug 24–26 workshop — it is not a client-facing quotation. Real counts still depend on the site survey (CAD, zone dimensions, existing camera inventory) and on one open scope decision on wayfinding footprint (Section 8). Every ratio/formula below is a methodology to apply, not a pre-computed answer — Product owns running the numbers.
**Constraint:** All infrastructure is on-premise at CTG. No cloud components in the architecture — size compute/storage/network accordingly (one narrow, unavoidable exception for mobile push notifications — see Section 5).
**Scope update:** Mobile app + wayfinding is now **confirmed Phase 1 in-scope** — it's an existing Waisl product being deployed/configured for CTG, not a ground-up build. This changes the BLE default (Section 8) and the app effort profile (Section 8) from earlier drafts of this document.

---

## 0. How to use this document

1. Read Section 1 (KPIs) and Section 2 (zones) to know what's in scope — don't size a sensor type or server component that no in-scope KPI actually needs.
2. Pull the confirmed/estimated figures in Section 3 — use these as real denominators wherever they apply, rather than treating everything as blocked on the survey.
3. Work through Sections 4–8 in order (cameras → hardware/compute → storage → integrations → wayfinding). Camera count feeds hardware/compute and storage sizing, so size cameras first.
4. Assemble the outputs into the cost/budget sheet described in Section 9, split CTG-CAPEX vs. Waisl-solution, with a ROM contingency band.
5. Anything you can't size without an item in Section 10's open-inputs list — don't guess past it; escalate instead.

---

## 1. Minimum KPI Set (defines what needs sizing — don't size beyond this without a reason)

| KPI | Definition | Sensor/system needed | Notes |
|---|---|---|---|
| Queue wait time | Time from joining to being served, per checkpoint (check-in cluster, security lane) | Camera + queue-analytics | Core pilot KPI |
| Queue length | Number of people in queue at a point in time | Camera + queue-analytics | Same camera as above, no extra hardware |
| Zone occupancy / density | People per m² in an open area (congestion indicator) | Camera + people-counting analytics | Overhead/angled general-area cameras, distinct from queue-lane cameras |
| Flow rate / throughput | Passengers processed per hour at a checkpoint | Camera + queue-analytics | Same camera as queue KPIs |
| Dwell time in zone | Time spent in a given area (e.g., domestic lounge) | BLE/Wi-Fi sensing (hashed/anonymized) | Cameras alone can't track dwell across a large open zone economically |
| End-to-end transit time | Time between two strategic points (e.g., check-in → gate) | BLE/Wi-Fi sensing (hashed/anonymized) | Only needs sensing at zone boundaries, not continuous coverage |
| Flight-linked turnaround/baggage KPIs | KPIs tied to a specific flight/passenger load (e.g., stand turnaround, baggage-to-belt time) | Collins AODB/RMS/FIDS data feed | Not a physical sensor — requires the integration in Section 7 |
| Wayfinding / in-app positioning | Passenger navigates to gate/amenity via app with real-time indoor position | BLE Option B (dense grid) + mobile app | **Now Phase 1 in-scope** — drives BLE default (Section 8) and may require expanding the pilot footprint beyond check-in+security (Section 2a) |

**Explicitly out of the minimum set (don't size hardware for these unless confirmed in scope):**
- ASQ satisfaction score — survey-based, not sensor-driven. No hardware implication.

---

## 2. Zone Scope (defines *where* sizing applies)

### 2a. Phase 1 Pilot (concrete — size this first)
Per the CxO deck's proposed pilot: **check-in + security**, existing infrastructure where reusable.

| Zone | Journey stage | KPIs applicable |
|---|---|---|
| Check-in hall (counters + kiosks) | Departure | Queue wait, queue length, flow rate, occupancy |
| Security screening (SSCP) | Departure | Queue wait, queue length, flow rate, occupancy |
| Check-in → Security transit | Departure | Dwell, end-to-end transit (if BLE/Wi-Fi Option A deployed) |

*Zone dimensions and existing camera coverage are unconfirmed — blocked pending CCNC/OINAC's CAD files and photos (Section 10). Lane/counter counts are not fully blind, though — see Section 3.*

**Scope tension to resolve:** wayfinding is most useful exactly where the current 2-zone pilot (check-in + security) doesn't reach — the post-security concourse, gates, and amenities. Confirm with BD/client whether Phase 1's physical footprint expands beyond check-in+security to make wayfinding meaningful, or whether Phase 1 wayfinding stays scoped to only the existing 2 zones (limited practical value for passengers, but validates the tech), with full-terminal wayfinding rolling out at full deployment (Q3–Q4 2027). This changes the BLE Option B device count and cost materially — see Section 8.

### 2b. Full-Terminal Placeholder (for the all-in ~US$1.2M cross-check — size later, scale from pilot unit costs)

| Zone | Journey stage | Notes |
|---|---|---|
| Curbside / departures forecourt | Arrival at airport | Outdoor cameras, different environmental spec |
| Immigration / emigration (if international) | Departure | May already have govt-mandated systems — check for overlap before sizing new hardware |
| Domestic & international boarding gates/lounges | Departure | Largest open-area occupancy zones |
| Arrivals immigration/customs + baggage claim | Arrival | Out of scope for Phase 1; contract language centers on the departure ("point-to-point... to boarding") journey — confirm with BD whether arrivals is in scope at all |

Do not size Section 2b in detail yet — use it only to sanity-check that the full ~$1.2M figure scales plausibly from the Phase 1 per-zone unit cost. Detailed sizing should wait for pilot results and the survey.

---

## 3. Known Airport Infrastructure Inputs (use these across every category below)

These figures already exist (CxO deck / published airport data) — treat them as real inputs, not as equally "pending survey" alongside CAD/dimensions.

| Input | Value | Status |
|---|---|---|
| Runways | 1 | Confirmed — public airport data |
| Gates | 15 (Domestic 1–8, International 9–15) | Confirmed — public airport data |
| Security lanes | ~6 (3 domestic + 3 international, inferred from terminal map) | Estimated only — not officially disclosed; confirm on-site |
| Check-in counters | ~72 | Unconfirmed — single public source; verify during survey |
| Avg. daily passengers | ~20–21K, peaking at ~22–25K/day (Dec–Jan) | Confirmed — OINAC concession manager (Patricia Mejía) stated >20K/day directly for June 2026 (El Universal, 27 Jul 2026), consistent with CTG's published 2024–2026 range |
| Annual passenger volume | 7.7M (2025 actual); >8M projected 2026 (record year); H1 2026 = 3.9M, +4% YoY | Confirmed for 2025/2026 (OINAC reporting via El Universal, Jul 2026); 2027 growth target from CxO deck expansion narrative — treat that longer-range figure as unconfirmed |
| Avg. daily flight movements | ~75–80 | Confirmed — CTG's published airport statistics, 2024–2026. **Data-quality flag:** June 2026 press reporting cites 4,667 total "operations" for the month (~156/day) — roughly 2x the ~75–80 figure. Likely a terminology mismatch (aircraft turnarounds/"flights" vs. arrivals+departures counted separately as "operations"), but unreconciled — confirm definition during the survey before using either number for capacity sizing. |

**Peak-vs-average:** the Dec–Jan and daily-bank peaks — not the ~20–21K average — should drive BLE/Wi-Fi device density, compute headroom, and bandwidth sizing (Sections 4–6). Sizing off the average will under-provision for the congestion moments the platform exists to catch.

---

## 4. Inputs for Camera Sizing

**KPIs driving this:** queue wait/length, flow rate, occupancy (Section 1).

**Known denominators to size against (Section 3):** ~72 check-in counters, ~6 security lanes.

**Sizing methodology to apply [ILLUSTRATIVE — validate against survey]:**
- Queue/lane monitoring: ~1 camera per 4–6 lane cluster (wide-angle, overhead or steep angle); narrower FOV cameras may need 1 per 2 lanes.
- General open-area occupancy/density: ~1 camera per 150–250 m² of open floor, adjusted for ceiling height and camera FOV.

**Other inputs:**
- Existing camera reuse potential — do not assume current security cameras are usable as-is; existing cameras were placed for surveillance, not passenger-flow analytics. Confirm only after the Solution Architecture coverage-gap analysis.
- Optional/premium tier (not minimum scope): LiDAR or thermal sensors for high-precision counting in low-light or camera-constrained lanes — price only if requested.

**Open inputs blocking a firm count (Section 10):** zone dimensions/CAD, existing camera inventory + ONVIF/reuse potential, photos of existing coverage, confirmation of the ~6 lane / ~72 counter estimates.

---

## 5. Inputs for Hardware / Compute (Server) Sizing

**Drivers:**
- Camera count (output of Section 4) — the primary sizing input for NVR/VMS and analytics compute.
- Analytics complexity: simple people-counting vs. behavior/queue analytics changes GPU/edge load materially.
- Xovis-type sensors do on-board processing — check vendor spec, since this may reduce central GPU server needs.

**Benchmark to apply [ILLUSTRATIVE — confirm with the analytics engine actually selected]:** ~8–32 camera streams per GPU/edge-appliance unit, depending on algorithm complexity.

**Server stack to size (all on-prem):**
- Video management/recording (NVR/VMS) — sized by concurrent streams + retention.
- Analytics processing (queue/occupancy/counting engines).
- Data warehouse / BI (KPI aggregation, trends) — modest sizing, scales with KPI data volume, not raw video.
- Application/dashboard server — lightweight.
- Integration middleware — see Section 7 for Collins-specific sizing.
- Mobile app backend/API — hosted on-prem per the no-cloud constraint. **Exception:** push notification delivery (wayfinding alerts, queue-time updates) mechanically routes through Apple APNs / Google FCM — unavoidable for any iOS/Android app. Only notification payloads transit through it, not passenger data or the underlying platform. Flag this exception explicitly to CTG rather than presenting the app as 100% on-prem without qualification.

**Network inputs:**
- PoE budget: ~15–30W per standard IP camera (higher for PTZ) — drives switch/UPS sizing.
- Bandwidth: per-camera stream bitrate × camera count for backbone sizing; BLE/Wi-Fi gateways are low-bandwidth and negligible by comparison.

**Decisions still needed from CTG/internal:**
- Redundancy: N+1 for recording/analytics (24/7 airport criticality) — price as an explicit option, don't assume it by default.
- Environment: reserve placeholder rack space (assume 1–2 racks for pilot) — confirm actual power/cooling/rack availability with CTG facilities during survey.

**Open inputs (Section 10):** camera count (depends on Section 4), analytics engine selection, redundancy decision, rack/power/cooling confirmation.

---

## 6. Inputs for Storage Sizing

**Formula to apply (methodology, not an answer — plug in real inputs once known):**
`Storage (TB) ≈ (bitrate_Mbps × 3600 × 24 × retention_days × camera_count) / (8 × 1,000,000)`

**Inputs still needed to run the formula:**
- Camera resolution/codec decision (e.g., H.265, 1080p) — don't assume a fixed bitrate.
- Retention policy (days) — not yet confirmed by CTG.
- Camera count — output of Section 4.

**Architecture note:** distributed NVR by zone (check-in / security / gates / baggage) reduces latency vs. one central unit — factor this into the server stack (Section 5), not just the storage total.

**Open inputs (Section 10):** retention-policy confirmation from CTG, codec/resolution decision, camera count.

---

## 7. Inputs for Collins AODB/RMS/FIDS Integration Sizing

This is a **services/effort line item, not a hardware line item** — size and price separately from the sensor cost sheet.

**What it delivers:** flight schedule, delays, and passenger-load data (via API/SOA per the technical deck) needed for turnaround and baggage-linked KPIs — this data cannot come from cameras or BLE/Wi-Fi.

**Effort categories to estimate (person-days, not hardware units):**
- API/sandbox access setup and credential provisioning (dependent on CTG + Collins coordination — see blocker below).
- Data mapping/normalization from Collins' schema into the platform's data warehouse.
- Integration build and testing (including handling of delayed/missing flight data gracefully).
- Ongoing maintenance/support for schema or API-version changes over the concession's life — a recurring cost, price into the multi-year support line rather than only the pilot.

**Known blocker:** Collins API/sandbox access is a **prerequisite**, not a nice-to-have — already flagged in the CxO deck's ask list (Item 7) as unconfirmed. Price with a **wide contingency band** until access is actually granted and the real API surface is inspected. If access slips, the pilot's core KPIs (queue/occupancy) can still run on video/sensor data alone, but turnaround/baggage KPIs should be shown as "at risk," not silently dropped.

**Open inputs (Section 10):** Collins API/sandbox access commitment, real API surface once inspected.

---

## 8. Inputs for Wayfinding / Mobile App Sizing

Intervención 8's contractual scope requires (ii) an API into the airport's passenger app and (iv)/(v) individual, point-to-point passenger identification for personalized guidance. **This is now confirmed Phase 1 in-scope** — mobile app + wayfinding is an existing Waisl product capability, not a ground-up build. That shifts the effort profile from software development to **deployment, content creation, and integration** — still a real cost/timeline line item, not free or instant.

**BLE/Wi-Fi design options — the technology choice, needed as an input to device-count sizing:**

| | Option A: Sparse chokepoint gateways | Option B: Dense indoor-positioning grid |
|---|---|---|
| What it enables | Anonymized dwell time + zone-to-zone transit time only | Same, plus continuous indoor positioning for personalized app-linked wayfinding |
| Device density | 1 gateway per zone entry/exit chokepoint | 1 beacon per ~20–30m spacing across the zone |
| Cost | Low | Significantly higher — driven by device count, not just coverage |
| Required for | Minimum KPI set only | Wayfinding — now confirmed Phase 1 scope |

**Option B is the default for the pilot cost sheet** — wayfinding is confirmed Phase 1 scope, so the dense grid is required, not optional. The open question is no longer *whether* Option B is needed but **what footprint** it needs to cover (see the 2a scope tension) — this materially changes the device count Product should size against.

**Wi-Fi passive sensing:** check whether CTG's existing Wi-Fi infrastructure (via CUPPS/IT) can expose passive probe-request data before pricing dedicated Wi-Fi sensors — could reduce hardware count materially.

**Effort categories to estimate (deployment/configuration, not ground-up build):**
- Indoor map / POI data creation for the CTG terminal (check-in, security, gates, amenities, restrooms, etc.) — a data/content-creation effort requiring a terminal walkthrough/survey, with its own lead time.
- App branding/configuration/white-labeling for CTG, or integration into CTG's existing app if one exists and is confirmed as the target.
- Identity/opt-in consent flow configuration — depends on Solution Architecture's resolution of the identity-architecture question and Colombian Habeas Data requirements.
- Positioning accuracy tuning against the BLE Option B grid once deployed — real-world calibration, not a one-time setup step.
- Integration with the passenger-experience analytics backend (shared KPI/data layer with the sensor platform).
- **Ongoing content operations**: gate changes, store/amenity changes, and terminal-layout updates (especially during the terminal expansion) require someone to maintain the map/POI data over time — an operational responsibility question tied to the L1 local-support/handover discussion (who maintains this after CCNC's construction scope closes: Waisl, OINAC, or CTG Ops?).

**Compliance upside to note in the cost sheet narrative:** folding this into Phase 1 directly closes the Intervención 8 objective (ii)/(iv) gap — worth stating explicitly once cost/timeline are firm, since it turns a known gap into a differentiator.

**Open inputs (Section 10):** Phase 1 wayfinding footprint decision (2-zone vs. extended), existing-vs-new CTG app target, content-maintenance ownership.

---

## 9. Expected Output: Cost / Budget Sheet (internal, for the Aug 24–26 workshop)

Assemble the five sized categories above into a single internal cost/budget sheet:

- **Cameras (Section 4):** device counts and unit costs by zone.
- **Hardware/compute + storage (Sections 5–6):** on-prem server/storage/network bill, sized per the formulas above.
- **Integrations (Section 7):** Collins integration as a separate services-effort line, with a wide contingency band pending API access.
- **Wayfinding (Section 8):** mobile app/wayfinding as a Phase 1 deployment/configuration line — priced as content-creation and integration effort (existing product), broken out separately from the sensor cost for transparency.
- **BLE/Wi-Fi devices:** priced under whichever option (Section 8) is selected, tied to the resolved footprint.

**Formatting requirements:**
- Split into **CTG CAPEX** (camera hardware, on-prem storage — per the ownership model) vs. **Waisl solution & services** (analytics platform, sensors, integration, professional services) buckets.
- A ROM contingency band (±30–40%, standard for pre-survey budgetary stage), with an explicit sensitivity line: cost delta if new camera positions are required beyond current inventory reuse.
- Clearly labeled **budgetary/ROM, internal discussion draft — not a client quotation.**
- Purpose: this sheet is the internal basis for driving the cost/scope conversation with CTG in the workshop — it is not to be shared with CTG in this form; a client-facing figure follows BD's ballpark-estimate framing (see readiness checklist) only after internal alignment.

---

## 10. Master Open-Inputs List (don't guess past these — escalate instead)

- Confirmed zone **dimensions** (CAD files — requested from CCNC/OINAC, outstanding).
- Existing camera inventory (make/model/age/ONVIF compliance, NVR config) — outstanding, redirected to OINAC.
- Photos of existing camera coverage in proposed pilot zones — outstanding.
- Confirmation of the ~6 security lanes / ~72 check-in counters estimates (Section 3) — currently public-source estimates only.
- Existing Wi-Fi AP density and whether CTG/IT can expose passive sensing data.
- BLE Option B footprint — technology choice is settled (wayfinding in scope), but physical coverage area (2-zone pilot only vs. extending to concourse/gates) is still open (Section 8).
- Camera resolution/codec decision and video retention policy (Section 6).
- Analytics engine selection and redundancy (N+1) decision (Section 5).
- Rack space, power, and cooling availability at CTG for on-prem servers.
- Collins API/sandbox access (Section 7) — outstanding (CxO deck Item 7).
- Whether the mobile app targets CTG's existing app or a new Waisl-branded app (Section 8).
- Who owns ongoing wayfinding map/content maintenance post-handover (Waisl, OINAC, or CTG Ops) — ties to the L1 local-support risk in the readiness checklist.
