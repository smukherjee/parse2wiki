# CTG Passenger Experience Platform — Internal Readiness Checklist

**Purpose:** Everything Waisl needs to sort out internally before the CxO pitch deck and technical deck are ready to present externally (target: Aug 24–26, 2026 meeting, Cartagena). Owners split by function. Use this to drive an internal alignment discussion — not for client circulation.

**Status legend:** 🔴 blocks the meeting if unresolved | 🟡 should resolve before meeting | 🟢 can resolve during/after pilot survey

---

## BD — Carlos (relationship, contracting, commercial positioning)

- 🔴 **Fix the stakeholder sequencing problem.** We are negotiating scope and price with CCNC (construction consortium), but OINAC (the actual Concesionario) carries the 15+ year regulatory obligation. Get OINAC formally into the solution sign-off loop — not just as a data source for items 5–9 — before CCNC is allowed to finalize commercial terms. Push for OINAC technical/security reps to attend Aug 24–26, not just CCNC.
- 🔴 **Resolve the cost-bucket ownership dispute before it becomes one.** Jorge's email is already steering camera-hardware costs toward OINAC's domain ("our requirement doesn't necessarily need to include this infrastructure"). Get explicit, written agreement on which entity — CCNC, OINAC, or CTG Ops — owns each cost bucket (camera hardware, storage, integration, ongoing support) before presenting the ~US$1.2M figure.
- 🔴 **Independently engage OINAC on the outstanding data request.** CCNC redirected the camera inventory/CAD/PoC-photo ask to OINAC on Jul 28; as of today we have not heard from OINAC directly. Don't wait for CCNC to relay it — open a direct line to Christian Carrazana / Abdon Ramirez (OINAC, cc'd on the original thread).
- 🟡 **Get clarity on the granting authority and compliance mechanism.** Confirm who actually holds/audits the Concession Agreement (ANI, Aerocivil, or other) and whether Intervención 8's "nueva normalidad" language has been formally reinterpreted via an Otrosí to accept a modern ASQ/analytics framing — or whether that's an assumption we're making on the client's behalf. If it's assumption-only, flag it as a compliance risk rather than presenting it as settled.
- 🟡 **Find out if Intervención 8 compliance gates terminal certification.** Determine whether this technology deliverable is a precondition for the expanded terminal's operating certification (RAC 139) or opening date. If yes, the "go/no-go pilot gate" framing in the deck understates the real stakes and needs to be rewritten — a "no-go" may not be a real option.
- 🟡 **Decide our commercial risk-sharing position.** Flat-fee services vs. a partial outcome/gain-share component tied to ASQ or staffing-efficiency KPIs. Given OINAC funds 100% of CAPEX/OPEX and carries the liability, expect this question from their finance team — have a position ready rather than reacting live.
- 🟡 **Lock down the ballpark-estimate approach and its caveat, in writing, with CCNC.** CCNC has told us explicitly they'll use whatever number we give to build their own economic offer. Confirm with them (ideally in writing) that any figure shared Aug 24–26 is non-binding and not to be used in a formal offer/budget submission until the site survey completes.
- 🟡 **Secure multi-year support commitment from OINAC, not just CCNC.** CCNC's contractual interest ends at construction handover; OINAC operates the concession for years afterward. Get OINAC to co-sign or independently commit to the long-term support/SLA/IP-documentation-escrow terms — this is what Item 9 ("L1 local support model") in the deck is quietly gesturing at; make it explicit.
- 🟢 Confirm final attendee list and roles for the Aug 24–26 meeting (Waisl side and client side) once the above stakeholder issues are resolved.

---

## Solution Architecture — Sujoy (technical scope, regulatory, data governance)

- 🔴 **Build the Intervención 8 compliance crosswalk.** Line-by-line table: each of the six sub-objectives in the scope document → platform capability. Explicitly name the two gaps:
  - (ii) API integration with the airport passenger app — currently absent from both decks.
  - (iv)/(v) individual, point-to-point passenger journey tracking via beacon/app identification — currently in tension with the platform's "anonymized, aggregate-only, no PII retained" architecture.
  Propose a resolution for each (e.g., phase-2 app/API scope, or a documented reinterpretation to put in front of the client) rather than leaving the gap implicit.
- 🔴 **Resolve the anonymized-aggregate vs. identified-individual architecture conflict.** Decide whether the platform needs an opt-in identity layer (app login or beacon-to-device binding) to support personalized, point-to-point guidance as scoped in the contract, and how that coexists with the current privacy positioning. This is a design decision, not a wording fix.
- 🔴 **Scope the security-restricted-area (SRA) regulatory workstream.** Determine whether any proposed camera repositioning or BLE/Wi-Fi beacon placement touches checkpoint sightlines or sterile-area boundaries. If so, this likely requires a formal Aerocivil-approved Security Program (PSA) amendment — a separate approval track with its own lead time, distinct from the general site survey. Get this scoped and timed before it becomes a surprise on the critical path.
- 🟡 **Do not assume the existing camera inventory is a usable baseline.** Existing cameras were placed for surveillance/security purposes, not passenger-flow analytics (per Carlos's own point to Jorge). Define a coverage-gap-analysis methodology to run during the site survey rather than presenting current inventory as a known-good starting point.
- 🟡 **Define the data governance model under Colombian law.** Clarify data controller (CTG) vs. processor (Waisl) roles for raw video capture under Ley 1581/2012 (Habeas Data) — raw footage is personal data at capture regardless of downstream anonymization. Determine whether a data processing agreement and a passenger notice distinct from standard security-CCTV signage are needed for behavioral/analytics use.
- 🟡 **Firm up the BLE/beacon technology recommendation.** The deck currently defers this to "Waisl will recommend the best-fit option" (Item 8, closing slide). Have an actual recommendation ready to present, not an open question, given the meeting is meant to present "the solution."
- 🟡 **Confirm integration/API access terms with Collins (AODB/RMS/FIDS), CUPPS, CUSS, Veripax.** Already flagged in the technical deck as a risk (sandbox access dependency) — get a realistic timeline and named point of contact, since this gates turnaround/baggage KPIs.
- 🟡 **Draft IP/documentation/escrow terms** needed to protect OINAC against the CCNC-handover cliff — technical documentation completeness and transition requirements, to hand to BD for contracting.
- 🟢 **Pressure-test the phased timeline** (pilot Q1–Q3 2027, full deployment Q3–Q4 2027) against construction handover dependencies and any regulatory certification deadline surfaced by BD's item above.
- 🟢 **Validate the proposed pilot zones (check-in + security)** technically once photos/CAD are available — confirm they have sufficient existing infrastructure and sightlines for a viable 28-week PoC before committing to that scope in writing.

---

## Product Team (KPIs, hardware sizing, mobile app)

- 🔴 **Own the mobile app / API integration scope.** Neither deck currently addresses Intervención 8 objective (ii) — API into the airport's passenger app. Scope whether Waisl builds/integrates this, what personalized-notification features are required, and produce an incremental cost/timeline estimate so it can be added to the offer if confirmed in scope.
- 🔴 **Own hardware sizing with a defensible bottom-up model.** Camera count/type/position per zone (pilot and full-terminal), Xovis/LiDAR/thermal sizing — build this independently rather than anchoring only to CTG's stated ~US$1.2M budget figure. The budget number should be a cross-check, not the source of the estimate.
- 🟡 **Define the KPI/metric measurement methodology.** Queue time, congestion incidents, ASQ alignment — the current deck labels the 4.1–4.3 ASQ figure as "illustrative, not committed." Define exactly how CTG's own baseline will be measured (instrumentation, survey cadence, data sources) so this isn't just a slide claim.
- 🟡 **Design the identity/opt-in flow for app-linked passenger journeys** (paired with Solution Architecture's architecture-conflict item above) — what's captured client-side vs. server-side, retention policy, and how it's disclosed to passengers.
- 🟡 **Build a sensitivity model for hardware/cost estimates** (e.g., "+X% if new camera positions are required beyond existing footprint") so the ballpark isn't presented with false precision.
- 🟡 **Design the KPI dashboard spec with three distinct audiences in mind** — CTG Ops (operational, real-time), OINAC (compliance/concession-KPI framing), CCNC (unlikely to need ongoing access post-handover). Different permission levels and views likely needed.
- 🟢 **Get real comparable-deployment data from Delhi, Hyderabad, Dubai** to replace "typical industry result" placeholders, or explicitly re-label them as illustrative-only with sourcing caveats.
- 🟢 **Define auditable KPI definitions** (ASQ delta, staffing cost reduction, queue-time reduction) in case BD pursues an outcome/gain-share commercial model — these need to be contract-grade, not just dashboard metrics.

---

## Joint / Leadership Decisions (needs BD + SA + Product alignment before the meeting)

- Decide whether to proactively raise the regulatory items (PSA/Aerocivil approval, Habeas Data, certification-linkage) with the client before Aug 24–26, or hold them as an internal risk register for now and surface only if asked.
- Align on one internal position for the ballpark estimate and its caveats so BD, Solution Architecture, and Product present consistent numbers and consistent framing in the room.
- Decide how much of the compliance crosswalk (API/app gap, identity-architecture conflict) to expose proactively vs. let the client discover — recommend disclosing it framed as "here's phase 2" rather than waiting to be caught.
