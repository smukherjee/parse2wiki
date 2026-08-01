# CTG Passenger Experience Platform — Rough Block Diagram (RBD) for Budgetary Quote

**Audience:** Product team (hardware sizing, KPI definition, mobile app scoping)
**Purpose:** Give Product enough of a rough scope — zones, sensor types, minimum KPI set, on-prem sizing inputs, Collins integration, and the mobile app/wayfinding workstream — to produce a budgetary (ROM) quote for CTG. This is deliberately *rough*: real counts depend on the site survey (CAD, zone dimensions, existing camera inventory) and on one still-open scope decision on wayfinding footprint (see Section 3a/7). Every figure below is a placeholder assumption to size against, not a spec.
**Constraint:** All infrastructure is on-premise at CTG. No cloud components in the architecture — size compute/storage/network accordingly (one narrow, unavoidable exception for mobile push notifications — see Section 5).
**Scope update:** Mobile app + wayfinding is now **confirmed Phase 1 in-scope** — it's an existing Waisl product being deployed/configured for CTG, not a ground-up build. This changes the BLE default (Section 4) and the app effort profile (Section 7) from earlier drafts of this document.

---

## 1. How to use this document

1. Apply the rough device-count assumptions in Section 4 to the zone list in Section 3.
2. Cross-check against the minimum KPI set in Section 2 — don't size a sensor type that no KPI in scope actually needs.
3. Run the on-prem sizing formulas in Section 5 to size compute/storage/network.
4. Size the Collins integration (Section 6) as a separate services line, and the mobile app/wayfinding workstream (Section 7) as a Phase 1 deployment/configuration line — both real Phase 1 costs, and both broken out separately from the sensor budget for transparency.
5. Package the output as a Bill of Quantities (Section 8) split into CTG-CAPEX vs. Waisl-solution buckets, with a ROM contingency band (±30–40%, standard for pre-survey budgetary stage).
6. Flag anything you can't size without the open inputs in Section 9 — don't guess past that list; escalate instead.

---

## 2. Minimum KPI Set (defines what hardware is actually needed)

Keep this lean. Every sensor type in Section 4 exists because a KPI here needs it — don't size beyond this list without a reason.

| KPI | Definition | Sensor needed | Notes |
|---|---|---|---|
| Queue wait time | Time from joining to being served, per checkpoint (check-in cluster, security lane) | Camera + queue-analytics | Core pilot KPI |
| Queue length | Number of people in queue at a point in time | Camera + queue-analytics | Same camera as above, no extra hardware |
| Zone occupancy / density | People per m² in an open area (congestion indicator) | Camera + people-counting analytics | Overhead/angled general-area cameras, distinct from queue-lane cameras |
| Flow rate / throughput | Passengers processed per hour at a checkpoint | Camera + queue-analytics | Same camera as queue KPIs |
| Dwell time in zone | Time spent in a given area (e.g., domestic lounge) | BLE/Wi-Fi sensing (hashed/anonymized) | Cameras alone can't track dwell across a large open zone economically |
| End-to-end transit time | Time between two strategic points (e.g., check-in → gate) | BLE/Wi-Fi sensing (hashed/anonymized) | Only needs sensing at zone boundaries, not continuous coverage |
| Flight-linked turnaround/baggage KPIs | KPIs tied to a specific flight/passenger load (e.g., stand turnaround, baggage-to-belt time) | Collins AODB/RMS/FIDS data feed | Not a physical sensor — requires the Collins integration in Section 6 |
| Wayfinding / in-app positioning | Passenger navigates to gate/amenity via app with real-time indoor position | BLE Option B (dense grid) + mobile app | **Now Phase 1 in-scope** — drives BLE default to Option B (Section 4) and may require expanding the pilot footprint beyond check-in+security (Section 3a) |

**Explicitly out of the minimum set (don't size hardware for these unless confirmed in scope):**
- ASQ satisfaction score — survey-based, not sensor-driven. No hardware implication.

---

## 3. Zone Scope

### 3a. Phase 1 Pilot (concrete — size this first)
Per the CxO deck's proposed pilot: **check-in + security**, existing infrastructure where reusable.

| Zone | Journey stage | KPIs applicable |
|---|---|---|
| Check-in hall (counters + kiosks) | Departure | Queue wait, queue length, flow rate, occupancy |
| Security screening (SSCP) | Departure | Queue wait, queue length, flow rate, occupancy |
| Check-in → Security transit | Departure | Dwell, end-to-end transit (if BLE/Wi-Fi Option A deployed) |

*Zone dimensions and existing camera coverage are unconfirmed — this is exactly what's blocked pending CCNC/OINAC's CAD files and photos (see Section 9). Lane/counter counts, however, are not fully blind — see the known-inputs table below.*

**Known airport infrastructure inputs (from CxO deck / technical deployment slides — use these now, don't treat as equally "pending survey" as CAD/dimensions):**

| Input | Value | Status |
|---|---|---|
| Runways | 1 | Confirmed — public airport data |
| Gates | 15 (Domestic 1–8, International 9–15) | Confirmed — public airport data |
| Security lanes | ~6 (3 domestic + 3 international, inferred from terminal map) | Estimated only — not officially disclosed; confirm on-site |
| Check-in counters | ~72 | Unconfirmed — single public source; verify during survey |
| Avg. daily passengers | ~20–21K, peaking at ~22–25K/day (Dec–Jan) | Confirmed — CTG's published airport statistics, 2024–2026 |
| Avg. daily flight movements | ~75–80 | Confirmed — CTG's published airport statistics, 2024–2026 |

These refine — but do not replace — the site survey. Use them as the actual denominators for the check-in/security ratios in Section 4 rather than sizing against an unknown lane count. **Peak-vs-average:** the Dec–Jan and daily-bank peaks (not the ~20–21K average) should drive BLE/Wi-Fi device density, compute headroom, and bandwidth sizing in Section 5 — sizing off the average will under-provision for the congestion moments the platform exists to catch.

**Scope tension to resolve:** wayfinding is most useful exactly where the current 2-zone pilot (check-in + security) doesn't reach — the post-security concourse, gates, and amenities. Confirm with BD/client whether Phase 1's physical footprint expands beyond check-in+security to make wayfinding meaningful, or whether Phase 1 wayfinding stays scoped to only the existing 2 zones (limited practical value for passengers, but validates the tech), with full-terminal wayfinding rolling out at full deployment (Q3–Q4 2027). This changes the BLE Option B device count and cost materially — do not size Option B against only the 2-zone footprint without this confirmation.

### 3b. Full-Terminal Placeholder (for the all-in ~US$1.2M cross-check — size later, scale from pilot unit costs)

| Zone | Journey stage | Notes |
|---|---|---|
| Curbside / departures forecourt | Arrival at airport | Outdoor cameras, different environmental spec |
| Immigration / emigration (if international) | Departure | May already have govt-mandated systems — check for overlap before sizing new hardware |
| Domestic & international boarding gates/lounges | Departure | Largest open-area occupancy zones |
| Arrivals immigration/customs + baggage claim | Arrival | Out of scope for Phase 1; contract language centers on the departure ("point-to-point... to boarding") journey — confirm with BD whether arrivals is in scope at all |

Do not size Section 3b in detail yet — use it only to sanity-check that the full ~$1.2M figure scales plausibly from the Phase 1 per-zone unit cost. Detailed sizing should wait for pilot results and the survey.

---

## 4. Rough Device-Count Assumptions (illustrative — validate against survey)

**Cameras**
- Queue/lane monitoring: ~1 camera per 4–6 lane cluster (wide-angle, overhead or steep angle) — narrower FOV cameras may need 1 per 2 lanes. [ILLUSTRATIVE ratio]
- General open-area occupancy/density: ~1 camera per 150–250 m² of open floor, adjusted for ceiling height and camera FOV. [ILLUSTRATIVE ratio]
- Confirm existing camera reuse potential only after the coverage-gap analysis (Solution Architecture workstream) — do not assume current security cameras are usable as-is.

**Applying the ratios against the known-inputs table (Section 3a) — pilot zones only:**

| Zone | Camera approach | Basis |
|---|---|---|
| Check-in | ~6–8 wide-angle overview cameras + 1–2 Xovis overhead, covering ~72 reported counters | Counter count unconfirmed (single public source) — verify per-counter resolution during survey |
| Security | ~8–10 cameras + 1–2 Xovis, sized against ~6 estimated lanes (3 domestic + 3 international) | Lane count not officially disclosed — confirm on-site before finalizing BOM |

This turns the Section 4 ratios into a working camera-count range for the pilot BOQ (Section 8) instead of leaving Product with a formula and no denominator. Both counts remain **estimates pending survey confirmation** — don't present them to CTG as final.

**BLE / Wi-Fi — two design options, pick based on confirmed scope, not by default:**

| | Option A: Sparse chokepoint gateways | Option B: Dense indoor-positioning grid |
|---|---|---|
| What it enables | Anonymized dwell time + zone-to-zone transit time only | Same, plus continuous indoor positioning for personalized app-linked wayfinding |
| Device density | 1 BLE/Wi-Fi gateway per zone entry/exit chokepoint | 1 beacon per ~20–30m spacing across the zone |
| Cost | Low | Significantly higher — driven by device count, not just coverage |
| Required for | Minimum KPI set only | Wayfinding (Section 7) — now confirmed Phase 1 scope |

**Default to Option B for the pilot budgetary quote.** Wayfinding is confirmed Phase 1 scope, so the dense indoor-positioning grid is required, not optional. The open question is no longer *whether* Option B is needed — it's **what footprint** it needs to cover. See the scope tension flagged in Section 3a before finalizing device counts.

**Wi-Fi passive sensing:** check whether CTG's existing Wi-Fi infrastructure (via CUPPS/IT) can expose passive probe-request data before pricing dedicated Wi-Fi sensors — could reduce hardware count materially.

**Optional/premium tier (not in minimum scope):** LiDAR or thermal sensors for high-precision counting in low-light or camera-constrained lanes. Price only if requested — not a baseline assumption.

---

## 5. On-Prem Infrastructure Sizing (formulas, not fixed numbers — all on-prem, no cloud)

**Storage (video retention):**
`Storage (TB) ≈ (bitrate_Mbps × 3600 × 24 × retention_days × camera_count) / (8 × 1,000,000)`
Plug in actual bitrate once camera resolution/codec (e.g., H.265, 1080p) is selected — don't assume a fixed bitrate.

**Compute (video analytics processing):**
Vendor-dependent — typical GPU/edge-appliance benchmarks range ~8–32 camera streams per unit depending on algorithm complexity (simple counting vs. queue/behavior analytics). [ILLUSTRATIVE — confirm with the analytics engine actually selected.] Note: if Xovis-type sensors are used for queue analytics, on-board processing may reduce central GPU server needs — check vendor spec before sizing a separate analytics server tier.

**Network:**
- PoE budget: ~15–30W per standard IP camera (higher for PTZ) — drives switch/UPS sizing.
- Bandwidth: per-camera stream bitrate × camera count for backbone sizing; BLE/Wi-Fi gateways are low-bandwidth and negligible by comparison.

**Server stack (all on-prem):**
- Video management/recording (NVR/VMS) — sized by concurrent streams + retention.
- Analytics processing (queue/occupancy/counting engines).
- Data warehouse / BI (KPI aggregation, trends) — modest sizing, scales with KPI data volume, not raw video.
- Application/dashboard server — lightweight.
- Integration middleware — see Section 6 for Collins-specific sizing.
- Mobile app backend/API — hosted on-prem per the no-cloud constraint. **Exception:** push notification delivery (wayfinding alerts, queue-time updates) mechanically routes through Apple APNs / Google FCM — unavoidable for any iOS/Android app and a standard, narrow exception to the on-prem rule. Only notification payloads transit through it, not passenger data or the underlying platform. Flag this exception explicitly to CTG rather than presenting the app as 100% on-prem without qualification.
- Redundancy: flag N+1 for recording/analytics as an explicit scope/cost decision (24/7 airport criticality) — don't assume it by default; price it as an option.
- Environment: reserve placeholder rack space (assume 1–2 racks for pilot) — confirm actual power/cooling/rack availability with CTG facilities during survey.

---

## 6. Collins AODB/RMS/FIDS Integration Scope

This is a **services/effort line item, not a hardware line item** — size and price it separately from the sensor BoQ.

**What it delivers:** flight schedule, delays, and passenger-load data (via API/SOA per the technical deck) needed for turnaround and baggage-linked KPIs — this data cannot come from cameras or BLE/Wi-Fi.

**Effort categories to estimate (person-days, not fixed hardware units):**
- API/sandbox access setup and credential provisioning (dependent on CTG + Collins coordination — see blocker below).
- Data mapping/normalization from Collins' schema into the platform's data warehouse.
- Integration build and testing (including handling of delayed/missing flight data gracefully).
- Ongoing maintenance/support for schema or API-version changes over the concession's life — this is a recurring cost, not a one-time build, and should be priced into the multi-year support line rather than only the pilot.

**Known blocker:** Collins API/sandbox access is a **prerequisite**, not a nice-to-have — it's already flagged in the CxO deck's ask list (Item 7, "Collins AODB/RMS/FIDS data access commitment") as unconfirmed. Price this with a **wide contingency band** until access is actually granted and the real API surface is inspected — don't assume the technical deck's description of the interface is final. If access slips, the pilot's core KPIs (queue/occupancy) can still run on video/sensor data alone, but turnaround/baggage KPIs should be shown as "at risk" in the quote, not silently dropped.

---

## 7. Mobile App & Wayfinding Scope (Phase 1 — existing Waisl product, deployment/configuration effort)

Intervención 8's contractual scope explicitly requires (ii) an API into the airport's passenger app and (iv)/(v) individual, point-to-point passenger identification for personalized guidance. **This is now confirmed Phase 1 in-scope** — mobile app + wayfinding is an existing Waisl product capability, not a ground-up build. That changes the effort profile from software development to **deployment, content creation, and integration** — but it's still a real cost and timeline line item. Don't treat "existing product" as "free" or "instant."

**Effort categories to estimate (deployment/configuration, not ground-up build):**
- Indoor map / POI data creation for the CTG terminal (check-in, security, gates, amenities, restrooms, etc.) — a data/content-creation effort requiring a terminal walkthrough/survey, with its own lead time distinct from software work.
- App branding/configuration/white-labeling for CTG, or integration into CTG's existing app if one exists and is confirmed as the target — still an open input (Section 9).
- Identity/opt-in consent flow configuration — depends on Solution Architecture's resolution of the identity-architecture question and Colombian Habeas Data requirements.
- Positioning accuracy tuning against the BLE Option B grid once deployed — real-world calibration in a live airport environment, not a one-time setup step.
- Integration with the passenger-experience analytics backend (shared KPI/data layer with the sensor platform).
- **Ongoing content operations**: gate changes, store/amenity changes, and terminal-layout updates (especially significant during the terminal expansion) require someone to maintain the map/POI data over time. This is an operational responsibility question, not a one-time deployment cost — tie it explicitly to the L1 local-support/handover discussion already flagged as an open risk (who maintains this after CCNC's construction scope closes: Waisl, OINAC, or CTG Ops?).

**Compliance upside:** folding this into Phase 1 directly closes the Intervención 8 objective (ii)/(iv) gap flagged in the earlier compliance crosswalk — worth stating explicitly in the client-facing deck once Product firms up cost/timeline, since it turns a known gap into a differentiator.

**Still open (see Section 9):** existing-vs-new CTG app target, and the Phase 1 wayfinding footprint (Section 3a) — both materially affect cost and must be resolved before final sizing, even though the app itself no longer needs to be built.

---

## 8. Expected Output from Product Team

A Bill of Quantities with:
- Device counts and unit costs by zone and type (camera, BLE/Wi-Fi gateway or beacon, optional LiDAR/thermal).
- On-prem server/storage/network bill, sized per Section 5 formulas.
- **Collins integration** as a separate services-effort line (Section 6), with contingency band pending API access.
- **Mobile app/wayfinding workstream** as a Phase 1 deployment/configuration line (Section 7) — priced as content-creation and integration effort (existing product), not ground-up development, but still broken out separately from the core sensor BoQ for transparency.
- Split into **CTG CAPEX** (camera hardware, on-prem storage — per the ownership model) vs. **Waisl solution & services** (analytics platform, sensors, integration, professional services) buckets.
- A ROM contingency band (±30–40%) with an explicit sensitivity line: cost delta if new camera positions are required beyond current inventory reuse (per the coverage-gap risk flagged separately).
- Clearly labeled as **budgetary/ROM, not a quotation** — precise figures require survey.

---

## 9. Open Inputs Still Needed (don't guess past these — escalate instead)

- Confirmed zone **dimensions** (CAD files — requested from CCNC/OINAC, outstanding). Lane/counter counts are no longer fully blind — see the known-inputs table in Section 3a — but both remain estimates (~6 security lanes, ~72 check-in counters) pending on-site confirmation.
- Existing camera inventory (make/model/age/ONVIF compliance, NVR config) — outstanding, redirected to OINAC.
- Photos of existing camera coverage in proposed pilot zones — outstanding.
- Existing Wi-Fi AP density and whether CTG/IT can expose passive sensing data.
- BLE Option B footprint — the technology choice is now settled (wayfinding is in scope), but the physical coverage area (2-zone pilot only vs. extending to concourse/gates) is still open — see Section 3a.
- Rack space, power, and cooling availability at CTG for on-prem servers.
- Collins API/sandbox access — outstanding (CxO deck Item 7), gates the effort/cost estimate for Section 6.
- Whether the mobile app targets CTG's existing app or a new Waisl-branded app — gates Section 7's branding/integration effort estimate.
- Who owns ongoing wayfinding map/content maintenance post-handover (Waisl, OINAC, or CTG Ops) — ties to the L1 local-support risk already flagged in the readiness checklist.
