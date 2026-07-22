# Source-System / Input-Feed Coverage Matrix — UTAM Solution Architecture v2

**Target proposal checked:** `sources/BAC/UTAM_Solution_Architecture_Details_Document_WAISL_Draft_v2.docx.md` (the "UTAM v2" / TurnWise proposal)
**Inputs compared against:**
- `sources/BAC/BAC-T-26-505 - Project- Underwing Analytics - RFP.pdf.md` (RFP — binding)
- `sources/BAC/BAC- Supplier Response Sheet - Underwing Analytics.xlsx.md` (Response Sheet — Tab F FR/NF binding)
- `sources/BAC/Turnwise Product Document 1.pdf.md` (Turnwise product collateral)

All line numbers are to the above `.md` extractions.

---

## Coverage Summary

| Metric | Count |
|---|---|
| Distinct source systems / input feeds identified (RFP + Response Sheet + Turnwise + UTAM v2) | 17 |
| **Fully covered in UTAM v2** | 6 |
| **Partially covered in UTAM v2** | 7 |
| **Missing / not covered in UTAM v2** | 0 (all required systems have at least a narrative mention) |
| Required by RFP/Response Sheet | 13 |
| Of those required: fully covered | 4 |
| Of those required: partial | 9 |
| Out-of-scope connectors UTAM v2 adds (not required by RFP/Response Sheet) | 7 (ADS-B, GSE Telematics, Weather, RVR, Stand Mgmt System, RMS, Network Manager Messaging) |

**Headline finding:** UTAM v2's §3.1 Connector table (lines 374-383) and §3.2 Connector Detail (lines 385-481) list only **6 connectors: AODB, ADS-B, Telematics, Vision Analytics, Weather, RVR**. The three RFP-mandated integration targets named in **FR54 (line 454) — FIDS and A-CDM (AIDX)** — appear only in narrative prose and diagrams, NOT as connectors in the §3.1/§3.2 connector tables. **FIDS** is the clearest gap: it is named in FR54 (Must Have), in the System Integration Module (line 304), the Integration Layer list (line 343), the Executive Summary (line 143), and the Mermaid diagram (line 1079), but it has **no row in the §3.1 connector table and no §3.2 connector detail entry** — no protocol, no data type, no data fields. **A-CDM / AIDX** suffer the same table omission; AIDX (required by FR15, FR43, FR54 — all Must Have) is only mentioned parenthetically as "A-CDM ( AIDX)" at line 344.

---

## Coverage Matrix

| # | Source system (normalized) | Where required (doc + line) | Mandatory? | Covered in UTAM v2? | UTAM v2 evidence (line) | Gap note |
|---|---|---|---|---|---|---|
| 1 | **AODB** (Airport Operational Database) | RFP line 177 (operational flight data); Response Sheet FR16 (line 328), FR33 (line 397), FR54 (line 454); Turnwise line 368/372 | Yes — Must Have (FR16, FR33, FR54) | **Yes (full)** | Connector table line 376 (AODB Connector, REST/SOAP/AMQP/MQ); Connector Detail lines 389-405; Edge Data Ingestor line 175; Exec Summary line 143; Deployment line 355; Mermaid line 1079 | None. |
| 2 | **AIDX** (Aircraft Information Exchange standard) | Response Sheet FR15 (line 326 — identify aircraft type/reg/flight no/airline), FR43 (line 422 — API integration via AIDX), FR54 (line 454) | Yes — Must Have (FR15, FR43, FR54) | **Partial** | Only narrative mentions: System Integration Module line 344 "A-CDM ( AIDX)"; Exec Summary line 143 | **No dedicated AIDX connector** in §3.1 table (lines 374-383) or §3.2 Connector Detail (lines 385-481). No protocol, data type, or data fields specified for AIDX ingestion. FR15 (Must Have) depends on AIDX for aircraft identification — how AIDX is ingested is undescribed. |
| 3 | **FIDS** (Flight Information Display System) | Response Sheet FR54 (line 454); Turnwise line 304 ("FIDs"), line 343 ("FIDS") | Yes — Must Have (FR54) | **Partial** | Narrative only: System Integration Module line 304; Integration Layer line 343; Exec Summary line 143; Mermaid line 1079 | **FIDS is absent from the §3.1 connector table (lines 374-383) and §3.2 Connector Detail (lines 385-481).** No connector, protocol, data type, or data fields. Named in prose/diagram only — the known FIDS gap. |
| 4 | **A-CDM** (Airport Collaborative Decision Making) | Response Sheet FR54 (line 454); Turnwise line 305, line 344 | Yes — Must Have (FR54) | **Partial** | Narrative only: System Integration Module line 306; Integration Layer line 344; Exec Summary line 143; Deployment line 355 ("AODB, A-CDM, RMS, ADS-B, Weather,"); Mermaid line 1079 | **A-CDM has no row in the §3.1 connector table and no §3.2 Connector Detail entry.** No protocol or data fields specified. Appears in prose/diagram only. |
| 5 | **Video Analytics / VMS / CCTV / RTSP / ONVIF** | RFP lines 165, 176 (fixed camera, video ingestion, video analytics); Response Sheet FR01-FR12 (cameras/video, esp. FR05 line 302 ingest live video), FR17-FR24 (GSE/personnel/turnaround via video); Turnwise line 376 ("Video Events") | Yes — Must Have (FR01-FR12, FR17-FR24) | **Yes (full)** | Connector table line 379 (Vision Analytics Connector, **RTSP/ONVIF**/REST API); Connector Detail lines 440-453; Edge Vision Controller line 176; Exec Summary line 143 ("Video Management Systems (VMS)") | None. RTSP/ONVIF explicitly listed. |
| 6 | **Airline systems** (planned/estimated times — alternate to AODB) | Response Sheet FR33 (line 397 — "from AODB or airline systems") | Yes — Must Have (FR33, OR-branch) | **Partial** | AODB connector (line 376) satisfies the AODB branch; AIDX (line 344) partially covers airline data exchange | The "airline systems" alternate branch of FR33 is not explicitly named as a connector. AODB path is covered; the OR allows this, but airline-systems ingest is not described. |
| 7 | **Aerobridge camera / pax counting / crew boarding** (Phase 2) | Response Sheet FR72 (line 499 — "Aerobridge camera for pax counting / crew boarding") | Yes — Must Have (FR72, Phase 2) | **Partial** | Edge Vision Controller (line 176) and Vision Analytics Connector (line 379) cover video generally; DPIA line 726 mentions "video analytics, Wi-Fi probe data" | **No explicit mention of "aerobridge camera", "pax counting", or "crew boarding"** anywhere in UTAM v2. FR72 (Phase 2, Must Have) not specifically addressed. |
| 8 | **Airline data integration** (Phase 2) | Response Sheet FR72 (line 499 — "Airline data integration") | Yes — Must Have (FR72, Phase 2) | **Partial** | AIDX mention (line 344) partially overlaps | Phase 2 "airline data integration" not explicitly scoped or detailed. |
| 9 | **Synchronised airport time source (NTP)** | Response Sheet FR08 (line 308 — timestamp video frames using synchronised airport time source) | Yes — Must Have (FR08) | **Yes (full)** | Line 652 "time-synchronized"; line 655 "clock synchronization (NTP)" | None. NTP explicitly named. |
| 10 | **Identity — Azure AD / Entra ID / SSO** | Response Sheet FR67 (line 484 — BAC users SSO), NF36 (line 603 — SSO), NF42 (line 617 — SAML2, "BAC uses Azure AD as our idP") | Yes — Must Have (FR67, NF36, NF42) | **Yes (full)** | Line 230 (SSO/OIDC, "Azure Entra id / Azure B2B"); line 231 (Keycloak SAML); line 553 ("Azure ID … Microsoft Entra ID / Azure Active Directory … via OIDC"); line 815 (Windows integrated auth via Microsoft Entra ID / Azure AD); line 809 (Authentication & Identity Mgmt section) | None. Azure AD/Entra, SSO, SAML2, OIDC all covered. |
| 11 | **Identity — SAML2 federation** | Response Sheet NF42 (line 617 — SAML2, Azure AD idP) | Yes — Must Have (NF42) | **Yes (full)** | Line 231 (Keycloak supporting SAML); line 809-816 section | None. |
| 12 | **Identity — OpenLDAP / OneLogin (third-party/non-BAC users)** | Response Sheet FR67 (line 484 — "Non-BAC users - local accounts") | Yes — Must Have (FR67) | **Yes (full — exceeds)** | Line 816 ("OpenLDAP and OneLogin SSO for non-Brisbane users … configured as additional identity providers in the IAM layer (KeyCloak)") | None. UTAM v2 exceeds the "local accounts" minimum by offering federated OpenLDAP/OneLogin. |
| 13 | **MFA (Multi-Factor Authentication)** | Response Sheet FR67 (line 484 — "MFA"), NF35 (line 601 — "Can offer Multi Factor Authentication") | Yes — Must Have (FR67, NF35) | **Partial** | Line 889 — "Mandatory multi-factor authentication for **all administrative and privileged access**" | UTAM v2 scopes MFA to "administrative and privileged access" only. NF35 asks for MFA capability generally; FR67 asks BAC to "define password parameters (… lockout, MFA)". MFA for all users / configurable MFA policy is not explicitly stated. Minor gap. |
| 14 | **ADS-B** (Automatic Dependent Surveillance – Broadcast) | **Not in RFP or Response Sheet** (FR13/FR14 detect arrival/departure but via video, not ADS-B). Turnwise line 303 ("ADS-B Data Source"), lines 368-377 (Monitoring Dashboard "ADSB Data") | No — product claim only | **Yes (full)** in UTAM v2 | Connector table line 377 (ADS-B Connector, REST/WebSocket/TCP); Connector Detail lines 406-421; Edge Data Ingestor line 175; Deployment line 355 | **Reverse-check: out-of-scope connector.** RFP/Response Sheet never require ADS-B. Gold-plating (reasonable for aircraft movement, but not mandated). |
| 15 | **GSE Telematics / GPS** | **Not in RFP or Response Sheet** (FR17-19 require GSE detection via **video analytics**, not telematics feeds). Turnwise line 302 ("Telematics/GPS Feeds"), line 339, line 376 ("Vehicle Data - Telematics") | No — product claim only | **Yes (full)** in UTAM v2 | Connector table line 378 (Telematics Connector, MQTT/REST/OPC-UA); Connector Detail lines 423-438; Edge Data Ingestor line 175 | **Reverse-check: out-of-scope connector.** RFP requires GSE detection via video (FR17), not telematics. Gold-plating. |
| 16 | **Weather (METAR / TAF)** | **Not in RFP or Response Sheet.** Turnwise line 345 ("WEATHER"), line 355 ("METAR/TAF") | No — product claim only | **Yes (full)** in UTAM v2 | Connector table line 380 (Weather Connector, METAR/TAF); Connector Detail lines 455-468; Edge Data Ingestor line 175 | **Reverse-check: out-of-scope connector.** RFP/Response Sheet never require weather. Gold-plating. |
| 17 | **RVR (Runway Visual Range)** | **Not in RFP or Response Sheet.** Turnwise line 342 ("RVR"), line 355 ("RVR") | No — product claim only | **Yes (full)** in UTAM v2 | Connector table line 381 (RVR Connector, REST/SNMP/TCP/IP); Connector Detail lines 470-481; Edge Data Ingestor line 175 | **Reverse-check: out-of-scope connector.** RFP/Response Sheet never require RVR. Gold-plating. |

---

## Discrepancy List — RFP/Response-Sheet required systems NOT fully covered by UTAM v2

Every item below is mandatory ("Must Have") in the Response Sheet and is only partially (or narrowly) addressed in UTAM v2.

| # | Source system | Requiring line (RFP / Response Sheet) | UTAM v2 gap |
|---|---|---|---|
| 1 | **AIDX** | FR15 (line 326, Must Have), FR43 (line 422, Must Have), FR54 (line 454, Must Have) | No AIDX connector in §3.1 connector table (lines 374-383) or §3.2 Connector Detail (lines 385-481). AIDX only appears as a parenthetical "A-CDM ( AIDX)" at line 344. No protocol, data type, or data fields for AIDX. FR15's aircraft-identification dependency on AIDX is unsupported by any connector description. |
| 2 | **FIDS** | FR54 (line 454, Must Have) | FIDS has **no row in the §3.1 connector table and no §3.2 Connector Detail entry**. Mentioned only in narrative (lines 143, 304, 343) and the Mermaid diagram (line 1079). No connector, protocol, data type, or data fields specified. This is the flagged FIDS gap. |
| 3 | **A-CDM** | FR54 (line 454, Must Have) | A-CDM has no row in the §3.1 connector table and no §3.2 Connector Detail entry. Mentioned only in prose/diagram (lines 143, 306, 344, 355, 1079). No protocol or data fields. |
| 4 | **Airline systems** (planned/estimated times, alternate branch) | FR33 (line 397, Must Have — "AODB **or** airline systems") | AODB branch covered by AODB connector (line 376). The "airline systems" alternate branch is not explicitly named as a connector/source. The OR means AODB alone can satisfy FR33, but airline-systems ingest is undescribed. |
| 5 | **Aerobridge camera / pax counting / crew boarding** | FR72 (line 499, Must Have, Phase 2) | No explicit mention of "aerobridge camera", "pax counting", or "crew boarding" anywhere in UTAM v2. General video/analytics coverage (lines 176, 379) does not evidence this specific Phase 2 capability. |
| 6 | **Airline data integration** (Phase 2) | FR72 (line 499, Must Have, Phase 2) | Phase 2 "airline data integration" not explicitly scoped or detailed; only AIDX (line 344) partially overlaps. |
| 7 | **MFA (general / configurable)** | FR67 (line 484, Must Have), NF35 (line 601, Must Have) | UTAM v2 limits mandatory MFA to "administrative and privileged access" (line 889). MFA for all users and BAC-configurable MFA policy (FR67: "BAC to be able to define password parameters (… MFA)") is not explicitly confirmed. |

---

## Reverse Check — UTAM v2 connectors / integrations NOT required by RFP / Response Sheet

Source systems UTAM v2 claims to integrate that the RFP and Response Sheet never ask for (out-of-scope / gold-plating):

| # | System | UTAM v2 line | Required by RFP/Response Sheet? | Note |
|---|---|---|---|---|
| 1 | **ADS-B** | Connector table line 377; Connector Detail lines 406-421 | No | Not in any FR/NF. RFP detects aircraft arrival/departure via video (FR13/FR14). Reasonable product capability, but not mandated. |
| 2 | **GSE Telematics / GPS** | Connector table line 378; Connector Detail lines 423-438 | No | RFP requires GSE detection via video (FR17-19), not telematics feeds. |
| 3 | **Weather (METAR/TAF)** | Connector table line 380; Connector Detail lines 455-468 | No | Not in any FR/NF. |
| 4 | **RVR** | Connector table line 381; Connector Detail lines 470-481 | No | Not in any FR/NF. |
| 5 | **Stand Management System** | System Integration Module line 300 | No | Not in RFP/Response Sheet. (Stand allocation handled by AODB in the RFP model.) |
| 6 | **RMS (Resource Management System)** | Deployment line 355 ("AODB, A-CDM, RMS, ADS-B, Weather,") | No | Not in RFP/Response Sheet. Appears in the on-prem edge list without explanation. |
| 7 | **Network Manager Messaging Services** | Business Services line 213 | No | Not in RFP/Response Sheet. FR43 only requires alert delivery via dashboard, email, and AIDX API — not Network Manager messaging. |

**Note on multi-channel notifications:** UTAM v2 line 212 lists "Email, SMS, WhatsApp, Teams, mobile push" connectors. RFP FR43 (line 419-422) requires only Operations dashboard + Email + API integration (AIDX). SMS/WhatsApp/Teams/push are beyond RFP scope (not non-compliant, but gold-plating).

**Note on identity provider choices:** Keycloak (line 231) and OpenLDAP/OneLogin (line 816) are product choices that satisfy FR67/NF42; they are acceptable, not gold-plating.

---

## Methodology notes

- The RFP (lines 223-229) defers all functional/non-functional requirements to "TAB.F Requirements in Response Sheet", so the Response Sheet's MoSCoW column is treated as the binding requirement authority. "Must Have" = mandatory.
- The RFP body itself names no specific source system by acronym; it references "operational flight data" (line 177), "camera and video ingestion" (line 176), and "BAC operational, enterprise and data systems" (line 183) generically.
- AIDX, ADS-B, telematics, weather, and RVR are not separately defined in the RFP body; AIDX/ADS-B/telematics/weather/RVR acronyms come from the Response Sheet FRs and the Turnwise/UTAM collateral. Of these, only **AIDX** is mandated by the Response Sheet (FR15, FR43, FR54). **ADS-B, GSE telematics, weather, and RVR are NOT mandated by the RFP/Response Sheet** — they originate in the Turnwise product collateral and are reproduced in UTAM v2.
- UTAM v2's connector table is at §3.1 "Connectors" (lines 374-383) and §3.2 "CONNECTOR DETAIL" (lines 385-481). These two sections together list exactly six connectors: AODB, ADS-B, Telematics, Vision Analytics, Weather, RVR. FIDS, A-CDM, and AIDX do not appear in either section.