# Airport Eye APOC Phase 2 — Complete Requirements Traceability Matrix

**Date:** 27 July 2026
**Analyst:** Built from scratch using only the four authoritative source documents listed below. No prior eval drafts, no client gaps file was consulted during requirement extraction phase. Client gap mapping follows in Part B.

## Source Documents (Authority Order)

| # | File | Type | Date/Version |
|---|------|------|-------------|
| 1 | `Airport_Eye_RFP_v5.docx.md` | RFP v5 | Issued to bidders |
| 2 | `Change Request Aiport Eye - APOC Phase 2.pdf.md` | BRD v1.5 (Consolidated) | 05-June-2026 |
| 3 | `Airport Eye Additional Busines Requirements- 2-July-2026.docx.md` | ABR (Additional Business Requirements + SPG Simulation Use Cases) | 02-July-2026 |
| 4 | `Final requirements.xlsx.md` | Requirements Register (sheet: Final Requirements (2)) | Date TBD |

## Methodology

- Every requirement extracted from all four sources, organized by category.
- Each row = one distinct requirement with verbatim or near-verbatim text.
- Status column: **STATED** = explicitly present in at least one source; **AMBIGUOUS** = referenced but quantified as `[X]` or placeholder; **TO BE DEFINED** = direction stated but details deferred.
- Client gap mapping (Part B) cross-references all 46 client gaps against these four sources only.

---

# PART A — REQUIREMENTS TRACEABILITY MATRIX

## A. Geospatial & LiDAR Survey

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| GEO-01 | Airborne LiDAR — point density | "Minimum point density: 20 points per square metre (ppm²) at all points within the airport boundary; 8 ppm² for buffer zones." | RFP v5 | §3.1.2 | Functional | Phase 1 | STATED |
| GEO-02 | Airborne LiDAR — horizontal accuracy | "Horizontal accuracy: RMSE ≤ 5 cm, verified against independently surveyed ground control points (GCPs)." | RFP v5 | §3.1.2; BRD v1.5 §3.1.1 | Functional | Phase 1 | STATED |
| GEO-03 | Airborne LiDAR — vertical accuracy | "Vertical accuracy: RMSE ≤ 3 cm, verified against independently surveyed benchmarks." | RFP v5 | §3.1.2; BRD v1.5 §3.1.1 | Functional | Phase 1 | STATED |
| GEO-04 | Airborne LiDAR — coverage extent | "Comprehensive airborne LiDAR survey encompassing the airport and Aerocity areas, runway and taxiway systems, aprons, cargo zones, perimeter areas, and a buffer extending 5 km beyond the airport boundary (estimated total: ~200 sq.km)." | RFP v5, §3.1.1; BRD v1.5 §3.1.1 | Functional | Phase 1 | STATED |
| GEO-05 | Airborne LiDAR — orthophoto GSD | "RGB orthophotography with ground sampling distance (GSD) ≤ 5 cm." | RFP v5, §3.1.2; BRD v1.5 §3.1.1 | Functional | Phase 1 | STATED |
| GEO-06 | Airborne LiDAR — point cloud format | "Classification of classified point cloud data (ASPRS LAS 1.4 format) with full classification scheme." | RFP v5, §3.1.2 | Functional | Phase 1 | STATED |
| GEO-07 | Airborne LiDAR — DTM/DSM resolution | "Production of Digital Terrain Model (DTM) and Digital Surface Model (DSM) at 10 cm grid resolution." | RFP v5, §3.1.2; BRD v1.5 §3.1.1 | Functional | Phase 1 | STATED |
| GEO-08 | Airborne LiDAR — 3D mesh | "Generation of 3D mesh models and 10 cm contour datasets from classified LiDAR data." | RFP v5, §3.1.2 | Functional | Phase 1 | STATED |
| GEO-09 | Deliverables — LAS/LAZ files | "Classified LAS/LAZ point cloud files (tiled, fully classified)." | RFP v5, §3.1.3 / D-02; BRD v1.5 §3.1.9 D-01 | Deliverable | Phase 1 | STATED |
| GEO-10 | Deliverables — DTM/DSM format | "DTM and DSM raster grids (GeoTIFF format, 10 cm resolution)." | RFP v5, §3.1.3 / D-02; BRD v1.5 §3.1.9 D-02 | Deliverable | Phase 1 | STATED |
| GEO-11 | Deliverables — orthophoto mosaic | "True Orthophoto mosaic (GeoTIFF/ECW, GSD ≤ 5 cm)." | RFP v5, §3.1.3 / D-03; BRD v1.5 §3.1.9 D-03 | Deliverable | Phase 1 | STATED |
| GEO-12 | Deliverables — contours | "10 cm interval contour dataset (SHP/DXF/DWG formats)." | RFP v5, §3.1.3 / D-04; BRD v1.5 §3.1.9 D-04 | Deliverable | Phase 1 | STATED |
| GEO-13 | Deliverables — mesh model format | "3D mesh model (OBJ/FBX format, georeferenced)." | RFP v5, §3.1.3 / D-05; BRD v1.5 §3.1.9 D-05 | Deliverable | Phase 1 | STATED |
| GEO-14 | Deliverables — flight/calibration report | "Full flight report, sensor calibration certificate, and GCP survey report." | RFP v5, §3.1.3 / D-06; BRD v1.5 §3.1.9 D-06 | Deliverable | Phase 1 | STATED |
| GEO-15 | Deliverables — metadata standard | "Accuracy assessment report and metadata documentation conforming to ISO 19115 standard." | RFP v5, §3.1.3 / D-07; BRD v1.5 §3.1.9 D-07 | Deliverable | Phase 1 | STATED |
| GEO-16 | Landside coverage — underground utility | "Underground utility scanning: GPR, DGPS, GNSS, and 12D model for landside roads." | BRD v1.5 §3.1.2 | Functional | Phase 1 | STATED |
| GEO-17 | Landside coverage — spot levels/contours | "DTM, DSM, DEM, contours, spot levels at 3×3 m intervals, and orthophotos." | BRD v1.5 §3.1.2 | Functional | Phase 1 | STATED |
| GEO-18 | Landside coverage — GIS topographic layers | "GIS topographic layers: land use, parcels, road networks, street view, zoning, topography, wetlands, demographics, land cover, imagery, basemap." | BRD v1.5 §3.1.2 | Functional | Phase 1 | STATED |
| GEO-19 | Airside coverage — layer-wise scanning | "Layer-wise scanning data for Runway, Taxiway, Apron, Isolation Bay, Perimeter Road, and all airside associated structures, drains." | BRD v1.5 §3.1.3 | Functional | Phase 1 | STATED |
| GEO-20 | Airside GIS layers | "GIS layers including AGL, PAPI Lights, DVOR, Signage, RVR, MSSR, AMSR, and other NAVAIDs including ancillary buildings." | BRD v1.5 §3.1.3 | Functional | Phase 1 | STATED |
| GEO-21 | Terminal coverage — building mapping | "Building mapping for all areas where existing layout or internal plans are unavailable." | BRD v1.5 §3.1.4 | Functional | Phase 1 | STATED |
| GEO-22 | Terminal coverage — update/add/delete | "Update of additions, deletions, and modifications made on ground in available building layouts." | BRD v1.5 §3.1.4 | Functional | Phase 1 | STATED |
| GEO-23 | Indoor LiDAR scanning — accuracy | "Indoor positional accuracy shall be ≤ 5 cm RMSE (horizontal and vertical) after cloud-to-cloud registration and georeferencing." | RFP v5, §3.2.1; BRD v1.5 §3.1.5 | Functional | Phase 1 | STATED |
| GEO-24 | Indoor LiDAR — indoor-outdoor continuity | "All scans shall be registered to the airborne LiDAR coordinate system to ensure seamless indoor-outdoor spatial continuity." | RFP v5, §3.2.1; BRD v1.5 §3.1.5 | Functional | Phase 1 | STATED |
| GEO-25 | Indoor LOD requirements — T1/T2/T3 MEP (LOD 350) | "T1, T2, T3 – All building assets (MEP, PHE, HVAC, concealed duct services) LOD 350." | BRD v1.5 §3.1.6 Table row 1 | Functional | Phase 1 | STATED |
| GEO-26 | Indoor LOD requirements — T3 forecourt/landsides (LOD 200) | "T3 Forecourt Roads, landside, airside (other than above assets) LOD 200." | BRD v1.5 §3.1.6 Table row 1 | Functional | Phase 1 | STATED |
| GEO-27 | Indoor LOD — NUB Buildings/Parking (LOD 200/350) | "NUB Buildings and Parking – All building assets (MEP, PHE, HVAC) LOD 200/350." | BRD v1.5 §3.1.6 Table row 2 | Functional | Phase 1 | STATED |
| GEO-28 | Indoor LOD — T2 MRSS/etc (LOD 350) | "T2 MRSS, Cityside Substations, HT/LT cable corridor and associated landside buildings, substations, equipment's LOD 350." | BRD v1.5 §3.1.6 Table row 3 | Functional | Phase 1 | STATED |
| GEO-29 | Indoor LOD — Airbus/ALD Office (LOD 200) | "Airbus Building, ALD Project Office LOD 200." | BRD v1.5 §3.1.6 Table row 5 | Functional | Phase 1 | STATED |
| GEO-30 | Airside LOD — T2-PEB future remote stand south of Centaur (LOD 350) | "Airside area between T2 and Peer Baba Future Remote Stand south of Centaur LOD 350." | BRD v1.5 §3.1.7 Table row 1 (amended) | Functional | Phase 1 | STATED |
| GEO-31 | Airside LOD — future remote stand south of Centaur AI Hangar Area (LOD 350) | "Airside T1 Future Apron LOD 350." | BRD v1.5 §3.1.7 Table row 3 (amended) | Functional | Phase 1 | STATED |
| GEO-32 | Airside LOD — technical area (LOD 200) | "Technical Area LOD 200." | BRD v1.5 §3.1.7 Table row 4 | Functional | Phase 1 | STATED |
| GEO-33 | Airside LOD — west of TWY A, C AI Hangar (LOD 350) | "Area on west of TWY A, C LOD 350." | BRD v1.5 §3.1.7 Table row 5 (amended) | Functional | Phase 1 | STATED |
| GEO-34 | Airside LOD — AI Hangar Area (LOD 350) | "AI Hangar Area LOD 350." | BRD v1.5 §3.1.7 Table row 5 (amended) | Functional | Phase 1 | STATED |
| GEO-35 | Airside LOD — STP Area outside Gate 15 (LOD 350) | "STP Area and outside Gate 15 LOD 350." | BRD v1.5 §3.1.7 Table row 6 (amended) | Functional | Phase 1 | STATED |
| GEO-36 | Airside LOD — Rain Harvesting (LOD 200) | "Rain Harvesting LOD 200." | BRD v1.5 §3.1.7 Table row 7 | Functional | Phase 1 | STATED |
| GEO-37 | BIM modelling standards — ISO 19650 | "Full compliance with ISO 19650 standards for information management using BIM throughout the asset lifecycle." | RFP v5, §3.2.2; BRD v1.5 §3.2.3 | Compliance | Phase 2 | STATED |
| GEO-38 | BIM modelling standards — IFC 4.0 | "IFC 4.0 (ISO 16739) — Open BIM data exchange format." | RFP v5, §3.2.2 | Compliance | Phase 2 | STATED |
| GEO-39 | BIM modelling standards — PAS 1192-2 / BS EN ISO 19650-2 | "PAS 1192-2:2013 and BS EN ISO 19650-2:2019 for project delivery." | RFP v5, §3.2.2 | Compliance | Phase 2 | STATED |
| GEO-40 | LOD matrix — structural framework (LOD 300) | "Structural Framework (Columns, Beams, Slabs) LOD 300 — full geometry, dimensions, materials; specification, load ratings." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-41 | LOD matrix — architectural elements (LOD 300) | "Architectural Elements (Walls, Doors, Windows, Ceilings) LOD 300 — exact geometry, finish schedules; fire rating, acoustic rating." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-42 | LOD matrix — HVAC (LOD 350) | "HVAC Systems (AHUs, Ducts, Diffusers, Chillers) LOD 350 — fabrication-level detail, connections; manufacturer data, maintenance schedules." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-43 | LOD matrix — electrical (LOD 350) | "Electrical Systems (Switchboards, Cable Trays, Luminaires) LOD 350 — panel schedules, circuit routing; ratings, installation dates, warranty." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-44 | LOD matrix — plumbing/drainage (LOD 300) | "Plumbing and Drainage LOD 300 — full pipe routing and sizing; material specs, isolation points." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-45 | LOD matrix — fire detection/suppression (LOD 350) | "Fire Detection and Suppression LOD 350 — detector and sprinkler layouts, pipe networks; test records, compliance certificates." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-46 | LOD matrix — security systems (LOD 300) | "Security Systems (CCTV, Access Control, Perimeter) LOD 300 — device locations and coverage zones; camera IDs, zone assignments." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-47 | LOD matrix — IT/network infra (LOD 200) | "IT and Network Infrastructure LOD 200 — rack locations, major cable routes; network IDs, capacity data." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-48 | LOD matrix — airside infra (LOD 200) | "Airside Infrastructure (Runways, Taxiways, Aprons) LOD 200 — surface extent, markings, lighting; surface type, condition rating." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-49 | LOD matrix — passenger handling equipment (LOD 300) | "Passenger Handling Equipment (BHS, PBBs, Escalators, Lifts) LOD 300 — full geometry, connection points; OEM data, maintenance history." | RFP v5, §3.2.3 Table; BRD v1.5 §3.1.8 Table | Functional | Phase 1 | STATED |
| GEO-50 | Indoor point density (unspecified) | "Scanning shall achieve a minimum point density of [X] points per square metre at all internal surfaces." | RFP v5, §3.2.1 | Functional | Phase 1 | AMBIGUOUS |
| GEO-51 | LOD — airside T2-Peer Baba future remote stand south of Centaur (LOD 350) amended text | "Airside area between T2 and Peer baba Future Remote Stand south of Centaur LOD 350 Underground assets and utilities mapping." | BRD v1.5 §3.1.7 Table row 1 | Functional | Phase 1 | STATED |
| GEO-52 | LOD — Airside T1 Future Apron LOD 350 | "Airside T1 Future Apron LOD 350." | BRD v1.5 §3.1.7 Table row 3 | Functional | Phase 1 | STATED |
| GEO-53 | LOD — Area on west of TWY A, C LOD 350 Underground assets and utilities mapping | "Area on west of TWY A, C LOD 350." | BRD v1.5 §3.1.7 Table row 5 | Functional | Phase 1 | STATED |
| GEO-54 | LOD — AI Hangar Area LOD 350 Future developments and underground utility mapping | "AI Hangar Area LOD 350." | BRD v1.5 §3.1.7 Table row 5 | Functional | Phase 1 | STATED |
| GEO-55 | LOD — STP Area and outside Gate 15 LOD 350 Future developments and underground utility mapping | "STP Area and outside Gate 15 LOD 350." | BRD v1.5 §3.1.7 Table row 6 | Functional | Phase 1 | STATED |
| GEO-56 | LOD — Rain Harvesting LOD 200 | "Rain Harvesting LOD 200." | BRD v1.5 §3.1.7 Table row 7 | Functional | Phase 1 | STATED |
| GEO-57 | BIM model deliverable | "IFC-compliant federated BIM models for all specified assets to agreed LOD." | RFP D-05; BRD v1.5 §3.1.9 D-08 | Deliverable | Phase 1 | STATED |
| GEO-58 | Asset attribute data register | "Asset Attribute Data Register (fully populated, imported to CAFM/CMMS)."  | RFP D-06; BRD v1.5 §3.1.9 D-09 | Deliverable | Phase 1 | STATED |
| GEO-59 | Legacy data audit requirement | "Conduct a full inventory and quality audit of all existing spatial and as-built data provided by DIAL." | RFP v5, §3.3.1; BRD v1.5 §3.2.1 | Functional | Phase 2 | STATED |
| GEO-60 | CAD-to-BIM conversion | "Convert and migrate all usable legacy CAD data (DWG/DXF format) into IFC-compliant BIM models consistent with the project's BIM standards." | RFP v5, §3.3.1; BRD v1.5 §3.2.1 | Functional | Phase 2 | STATED |
| GEO-61 | Legacy data reconciliation | "Reconcile discrepancies between legacy data and current LiDAR survey findings, documenting all deviations and obtaining DIAL approval before finalising models." | RFP v5, §3.3.1; BRD v1.5 §3.2.1 | Functional | Phase 2 | STATED |
| GEO-62 | CAFM/CMMS attribute import | "Populate converted models with available asset attribute data from DIAL's existing CAFM/CMMS systems." | RFP v5, §3.3.1; BRD v1.5 §3.2.1 | Functional | Phase 2 | STATED |
| GEO-63 | Data quality report | "Deliver a Data Quality Report documenting the completeness, accuracy, and compliance of all legacy data reviewed and migrated." | RFP v5, §3.3.1; BRD v1.5 §3.2.1 | Deliverable | Phase 2 | STATED |

---

## B. Federated BIM Platform & GIS-BIM Integration

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| FED-01 | Concurrent multi-discipline coordination | "Support for concurrent multi-discipline BIM coordination with automated clash detection and resolution workflows." | RFP v5, §3.3.2; BRD v1.5 §3.2.3 | Functional | Phase 2 | STATED |
| FED-02 | Version control + audit trail | "Version control and change management with full audit trail." | RFP v5, §3.3.2; BRD v1.5 §3.2.3 | Functional | Phase 2 | STATED |
| FED-03 | Role-based access control | "Role-based access control with granular permissions for internal staff, contractors, and third-party consultants." | RFP v5, §3.3.2; BRD v1.5 §3.2.3 | Functional | Phase 2 | STATED |
| FED-04 | Native IFC + CDE | "Native IFC and common data environment (CDE) functionality." | RFP v5, §3.3.2; BRD v1.5 §3.2.3 | Functional | Phase 2 | STATED |
| FED-05 | API integration with DT viewer + AI platform | "API-based integration with the Digital Twin viewer and AI monitoring platform." | RFP v5, §3.3.2; BRD v1.5 §3.2.3 | Infrastructure | Phase 2 | STATED |
| FED-06 | BIM-GIS import | "Import BIM models into the GIS environment." | BRD v1.5 §3.2.2 | Functional | Phase 2 | STATED |
| FED-07 | GIS-BIM database interoperability | "Establish connections between GIS and BIM databases for data interoperability." | BRD v1.5 §3.2.2 | Functional | Phase 2 | STATED |
| FED-08 | Interactive pop-up windows | "Configure interactive pop-up windows for enhanced data visualization and user interaction." | BRD v1.5 §3.2.2 | Functional | Phase 2 | STATED |
| FED-09 | Multi-scale visualization | "Support for multi-scale visualization combining point clouds, orthophotos, terrain models, 3D mesh, and BIM geometry." | BRD v1.5 §3.2.2 | Functional | Phase 2 | STATED |

---

## C. Digital Twin Viewer & Outdoor 3D GIS Platform

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| VWR-01 | Web-based 3D viewer | "Web-based 3D GIS and BIM viewer supporting simultaneous display of GIS basemap, aerial imagery, point cloud data, textured 3D mesh, and BIM model geometry at all scales." | RFP v5, §3.5.1; BRD v1.5 §3.4.1 | Functional | Phase 4 | STATED |
| VWR-02 | Indoor/outdoor navigation | "Seamless indoor/outdoor navigation with automatic LOD management for performance optimisation." | RFP v5, §3.5.1; BRD v1.5 §3.4.1 | Functional | Phase 4 | STATED |
| VWR-03 | Layer management | "Layer management enabling users to toggle visibility of individual data layers." | RFP v5, §3.5.1 | Functional | Phase 4 | STATED |
| VWR-04 | Real-time BMS overlay | "Real-time display of BMS data overlaid on corresponding BIM elements, with colour-coded condition indicators and live data readouts." | RFP v5, §3.5.1 | Functional | Phase 4 | STATED |
| VWR-05 | Dashboard/annotation/task tools | "Customisable dashboard panels, measurement tools, annotation tools, and task-assignment tools integrated with DIAL's CAFM/CMMS system." | RFP v5, §3.5.1 | Functional | Phase 4 | STATED |
| VWR-06 | AR/VR support | "Support for AR/VR output for maintenance and training use cases." | RFP v5, §3.5.1; BRD v1.5 §3.4.1 | Functional | Phase 4 | STATED |
| VWR-07 | Mobile responsiveness + offline | "Full mobile responsiveness with offline capability for field maintenance teams." | RFP v5, §3.5.1; BRD v1.5 §3.4.1 | Functional | Phase 4 | STATED |
| VWR-08 | Desktop thick application | "DT shall be a Desktop based thick application. The desktop shall require GPU to power the DT." | Final requirements.xlsx.md, Ops DT | Infrastructure | Phase 1a | STATED |
| VWR-09 | WebGL browser-based DT | "Web-GL based DT shall be provided running on a Browser (Chrome & Safari)." | Final requirements.xlsx.md, Ops DT | Functional | Phase 2 | STATED |
| VWR-10 | Login + profile-based visualization | "Let configured users login to DT. Visualize layers, locations, assets, and widgets based on the profile." | Final requirements.xlsx.md, Ops DT | Functional | Phase 1a | STATED |
| VWR-11 | Exterior sun/rain views | "Follow the sun for Night/Morning views, Rain." | Final requirements.xlsx.md, Ops DT | Functional | Phase 1b | STATED |
| VWR-12 | Navigation controls | "The DT shall support zoom in - zoom out, tilt and turnaround using keyboard and mouse." | Final requirements.xlsx.md, Ops DT | Functional | Phase 1a | STATED |
| VWR-13 | LOD 200 exterior views — airside | "DT shall provide an spatially accurate exterior view of LOD 2 level for: Airside: Runways(except airforce runway), Taxiways, Aprons." | Final requirements.xlsx.md, ODT-BE-01 | Functional | Phase 1a | STATED |
| VWR-14 | LOD 200 exterior views — terminals | "DT shall provide an spatially accurate exterior view of LOD 2 level for: Terminal: T1, T2, T3." | Final requirements.xlsx.md, ODT-BE-01 | Functional | Phase 1a | STATED |
| VWR-15 | LOD 200 exterior views — cityside | "DT shall provide an spatially accurate exterior view of LOD 2 level for: Cityside: Ramp areas, MRSS, cooling towers." | Final requirements.xlsx.md, ODT-BE-01 | Functional | Phase 1b | STATED |
| VWR-16 | Terminal: T1,T2 exterior view | "DT shall provide an spatially accurate exterior view of LOD 2 level for: Terminal: T1, T2." | Final requirements.xlsx.md, ODT-BE-01 | Functional | Phase 1a | STATED |
| VWR-17 | Display ITBMS via web page from DT | "Display ITBMS based equipment and sensor details on a web page, launched via DT." | Final requirements.xlsx.md, ODT-BE-01 | Functional | Phase 1a | STATED |
| VWR-18 | Selectable areas/zones | "Selectable areas and zones in DT to visualize." | Final requirements.xlsx.md, ODT-BE-01 | Functional | Phase 1a | STATED |
| VWR-19 | Multi-level navigation T1/T2/T3 | "Enable Multi-Level navigation from airport and terminal views to zones, floors, systems, and assets. They should be supported by zoom and shortcuts." (plus separate entries for T1, T2, T3) | Final requirements.xlsx.md, Ops DT | Functional | Phase 1b/1c/2 | STATED |
| VWR-20 | Display alerts in DT | "Display alerts." | Final requirements.xlsx.md, Ops DT | Functional | Phase 1b | STATED |
| VWR-21 | MEP layer toggle | "Let users select layers to show/hide MEP layers." | Final requirements.xlsx.md, Ops DT | Functional | Phase 1b | STATED |
| VWR-22 | LOD 350 equipment visualization | "Visualize equipment & required sensors (LOD 350 - no schematics) for HVAC, FDAS, VHT, ECMS, LCMS, PBB, GPU, PCA, VDGS, WTP, STP, MRSS, BHS, ATRS, Solar-Panels, AGL. Create LOD 200 level interiors using structural components of BIM for all floors." | Final requirements.xlsx.md, Ops DT | Functional | Phase 1b/1c | STATED |
| VWR-23 | Display assets like check-in zones/security zones/retail areas at asset level | "Display assets like Check-in zones - counters, lanes, SBD; Security zones - ATRS, DFMD, E-Gates; Immigration zones - lanes, counters; Boarding - E-gates, lanes, seating areas; Retail areas - Duty free, F&B, Retail. Avoid detailing beyond asset level." | Final requirements.xlsx.md, Ops DT | Functional | Phase 1c | STATED |
| GIS-01 | High-performance web-based 3D GIS viewer | "High-performance web-based 3D GIS viewer." | RFP v5, §3.6.2.A; BRD v1.5 §3.4.6 | Functional | Phase 4 | STATED |
| GIS-02 | LiDAR/orthophoto/DTM/DSM/mesh display in GIS | "Support for: LiDAR point clouds, Orthophotos, Terrain models (DTM/DSM), 3D mesh models." | RFP v5, §3.6.2.A | Functional | Phase 4 | STATED |
| GIS-03 | Multi-scale visualization | "Multi-scale visualization." | RFP v5, §3.6.2.A | Functional | Phase 4 | STATED |
| GIS-04 | Multi-department data layering | "Ability for different airport departments to upload and manage their own geospatial datasets and overlay custom layers on base GIS data." | RFP v5, §3.6.2.B | Functional | Phase 4 | STATED |
| GIS-05 | Format support (SHP/GeoJSON/KML/IFC/DWG) | "Supported formats: SHP, GeoJSON, KML, IFC overlays, CAD (DWG)." | RFP v5, §3.6.2.B | Functional | Phase 4 | STATED |
| GIS-06 | Planning/scenario visualization | "Overlay proposed development plans; visualise proposed assets in context with existing airport conditions; compare existing vs proposed scenarios." | RFP v5, §3.6.2.C | Functional | Phase 4 | STATED |
| GIS-07 | Collaborative editing/redlining | "Map-based redlining (draw, annotate, highlight); commenting and discussion threads linked to spatial locations; version control for uploaded datasets; multi-user collaboration in real-time." | RFP v5, §3.6.2.D | Functional | Phase 4 | STATED |
| GIS-08 | Sharing/publishing capabilities | "Share map views via secure links; role-based access control for shared views; export capabilities: PDF map reports, image snapshots, data extracts." | RFP v5, §3.6.2.E | Functional | Phase 4 | STATED |
| GIS-09 | Natural language query for GIS retrieval | "Natural language query capabilities for GIS data retrieval." | BRD v1.5 §3.4.6 (inline with Outdoor 3D GIS Platform description in table at line ~434) | Functional | Phase 4 | STATED |

---

## D. BMS / IoT Integration & Middleware

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| IOT-01 | Protocols — BACnet/IP | "Real-time data ingestion from all BMS controllers using standard industrial protocols including BACnet/IP." | RFP v5, §3.4.1 | Functional | Phase 4 | STATED |
| IOT-02 | Protocols — BACnet MSTP | Include BACnet MSTP in list of required protocols. | BRD v1.5 §3.4.2 | Functional | Phase 4 | STATED |
| IOT-03 | Protocols — Modbus TCP/RTU | "Modbus TCP/RTU." | RFP v5, §3.4.1; BRD v1.5 §3.4.2 | Functional | Phase 4 | STATED |
| IOT-04 | Protocols — MQTT v3.1.1 and v5.0 | "MQTT (v3.1.1 and v5.0)." | RFP v5, §3.4.1; BRD v1.5 §3.4.2 | Functional | Phase 4 | STATED |
| IOT-05 | Protocols — OPC-UA | "OPC-UA." | RFP v5, §3.4.1; BRD v1.5 §3.4.2 | Functional | Phase 4 | STATED |
| IOT-06 | Protocols — RESTful APIs | "RESTful APIs and proprietary vendor connectors where required." | BRD v1.5 §3.4.2 | Functional | Phase 4 | STATED |
| IOT-07 | DTDL normalization | "All ingested data shall be normalised into a unified semantic data model conforming to the Digital Twin Definition Language (DTDL) or equivalent open standard approved by DIAL." | RFP v5, §3.4.1; BRD v1.5 §3.4.2 | Functional | Phase 4 | STATED |
| IOT-08 | BMS point-to-BIM mapping | "Every BMS data point shall be mapped to a corresponding BIM element, enabling 3D spatial visualisation of all operational data." | RFP v5, §3.4.2; BRD v1.5 §3.4.2 | Functional | Phase 4 | STATED |
| IOT-09 | Configurable geofencing/zone monitoring | "The platform shall support configurable geofencing and zone-based monitoring, enabling operators to define operational zones and receive aggregated zone-level performance metrics." | RFP v5, §3.4.2 | Functional | Phase 4 | STATED |
| IOT-10 | Historical data archiving — 5-year retention | "Historical data archiving for all BMS data streams, with a minimum retention period of five (5) years accessible through the platform's analytics interface." | RFP v5, §3.4.2; BRD v1.5 §3.4.2 | Functional | Phase 4 | STATED |
| IOT-11 | IoT/BMS middleware platform — licensing/deployment | "IoT/BMS Middleware Platform — Licensing and Deployment" (Table 4, Item 1). | Commercial | Phase 3 | STATED |
| IOT-12 | BACnet/IP, Modbus TCP/RTU integration | "BACnet/IP, Modbus TCP/RTU integration, MQTT and IoT Sensor integration" (Table 4, Item 2). | Commercial | Phase 3 | STATED |
| IOT-13 | Historical data archiving platform — per annum | "Historical Data Archiving Platform (5-Year Retention)" (Table 4, Item 3). | Commercial | Phase 3 | STATED |
| IOT-14 | Integration testing/commissioning/documentation | "Integration Testing, Commissioning, and Documentation" (Table 4, Item 4). | Commercial | Phase 3 | STATED |
| IOT-15 | BMS data point scalability | "The platform shall support a minimum of [X] BMS data points at initial deployment, with a scalable architecture capable of expanding to [X] data points within the first three years." | RFP v5, §3.4.1 | Functional | Phase 4 | AMBIGUOUS |
| IOT-16 | OPC/DA data ingestion ability | "OPC/DA data ingestion abilities (with 3rd party platform)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1b | STATED |
| IOT-17 | OPC/UA data ingestion ability | "OPC/UA data ingestion abilities (with 3rd party platform)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1b | STATED |
| IOT-18 | BacNet IP data ingestion ability | "BacNet IP data ingestion abilities (with 3rd party platform)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1b | STATED |
| IOT-19 | Modbus IP data ingestion ability | "Modbus IP data ingestion abilities (with 3rd party platform)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1c | STATED |
| IOT-20 | On-prem data buffering | "On-prem data buffering (custom built)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1b | STATED |
| IOT-21 | On-prem data sampling | "On-prem data sampling to avoid overwhelming data push (custom built)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1b | STATED |
| IOT-22 | On-prem to cloud replication | "On-prem to Cloud replication (custom built)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1a | STATED |
| IOT-23 | On-prem observability | "On-prem Observability (custom built)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1a | STATED |
| IOT-24 | On-prem storage | "On-prem storage (custom built)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1b | STATED |
| IOT-25 | IoT data support for real-time display | "IOT Data support for Real-time display (custom built)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1b | STATED |
| IOT-26 | Cloud connector | "Cloud connector (custom built)." | Final requirements.xlsx.md, Platform | Infrastructure | Phase 1b | STATED |

---

## E. AI Agent Layer — Orchestration Framework & Mandatory Agents

### E1. Orchestration Framework

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| AI-01 | Orchestration engine — centralised management | "A centralised AI orchestration engine shall manage all deployed agents, handling data routing, alert aggregation, priority scoring, and cross-agent correlation." | RFP v5, §6.2.1; BRD v1.5 §3.5.2 | Functional | Phase 5 | STATED |
| AI-02 | Agent lifecycle management | "The orchestration engine shall support the deployment, update, retirement, and versioning of individual AI agents without requiring platform downtime." | RFP v5, §6.2.1; BRD v1.5 §3.5.2 | Functional | Phase 5 | STATED |
| AI-03 | Common interface with DT data bus | "All agents shall share a common interface with the Digital Twin's data bus, enabling cross-domain correlation analyses." | RFP v5, §6.2.1 | Functional | Phase 5 | STATED |
| AI-04 | AI Model Management console | "The framework shall expose an AI Model Management interface enabling DIAL's technical team to review agent performance metrics, retrain models with new data, and approve model updates before production deployment." | RFP v5, §6.2.1; BRD v1.5 §3.5.2 | Functional | Phase 5 | STATED |
| AI-05 | Shared AI platform (once-built) | "Build the common AI infrastructure once, reused by every agent: ingestion from the Phase-4 middleware, TimescaleDB historian, shared feature store (lags, rolling stats, weather/calendar joins), MLflow model registry, explainability service, alert pipeline and CMMS/AMMS work-order connector." | Final requirements.xlsx.md, AI-02 | Infrastructure | Phase 5 | STATED |
| AI-06 | Orchestration engine deployment (Table 6 Item 1) | "AI Orchestration Framework — Development and Deployment" (Table 6, Item 1). | Commercial | Phase 4 | STATED |

### E2. Mandatory AI Agents (performance standards from RFP v5, §6.5 / BRD v1.5 §3.5.4)

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| AI-A1 | Mech & HVAC Agent — monitoring scope | "Continuously monitors all mechanical systems including AHUs, chillers, cooling towers, pressurisation systems, ventilation fans, and BAS controllers." | RFP v5, §6.3.1; BRD v1.5 Table line ~437 | Functional | Phase 5 | STATED |
| AI-A2 | Mech & HVAC Agent — prediction horizon | "Predicts chiller plant degradation and compressor failure up to 72 hours in advance." (RFP) + Min precision ≥82%, recall ≥78%, alert latency ≤30s. | RFP v5, §6.3.1; RFP v5, §6.5 Table; BRD v1.5 §3.5.4 Table | Functional | Phase 5 | STATED |
| AI-A3 | Mech & HVAC Agent — energy optimisation | "Generates energy optimisation recommendations based on real-time occupancy, weather forecasting data, and historical patterns." + triggers automated work orders in CAFM/CMMS. | RFP v5, §6.3.1 | Functional | Phase 5 | STATED |
| AI-A4 | Electrical Systems Agent — monitoring scope | "Continuously monitors the airport's high and low voltage electrical infrastructure, including transformer rooms, UPS systems, switchgear, distribution boards, and emergency power systems." | RFP v5, §6.3.2; BRD v1.5 Table line ~438 | Functional | Phase 5 | STATED |
| AI-A5 | Electrical Systems Agent — precision/recall | "Min Precision ≥80%, Min Recall ≥75%, Prediction Horizon up to 48 hours, Alert Latency ≤30 seconds." | RFP v5, §6.5 Table; BRD v1.5 §3.5.4 Table | Functional | Phase 5 | STATED |
| AI-A6 | Fire Safety & Life Safety Agent — monitoring scope | "Continuously monitors all fire detection, suppression, smoke control, and evacuation systems across the airport campus." | RFP v5, §6.3.4; BRD v1.5 Table line ~443 | Functional | Phase 5 | STATED |
| AI-A7 | Fire Safety Agent — multi-sensor correlation / precision-recall | "Multi-sensor correlation (smoke, heat, CO, optical) to distinguish genuine from nuisance alarms" + Min Precision ≥95%, recall ≥95%, real-time, alert latency ≤5s. | RFP v5, §6.3.4; RFP v5, §6.5 Table; BRD v1.5 §3.5.4 Table | Functional | Phase 5 | STATED |
| AI-A8 | Water & Drainage Agent — monitoring scope | "Monitors the airport's potable water, chilled water, grey water, and stormwater drainage infrastructure." | RFP v5, §6.3.5; BRD v1.5 Table line ~444 | Functional | Phase 5 | STATED |
| AI-A9 | Water & Drainage Agent — leak detection/pump health | "Detects water loss and pipe leak signatures using pressure drop analysis and flow metering correlation." + stormwater runoff modelling with weather forecasting. | RFP v5, §6.3.5 | Functional | Phase 5 | STATED |
| AI-A10 | Energy Management Agent — monitoring scope | "Monitors and optimises the airport's total energy consumption across all utility categories." | RFP v5, §6.3.6; BRD v1.5 Table line ~445 | Functional | Phase 5 | STATED |
| AI-A11 | Energy Management Agent — precision/recall | "Min Precision ≥80%, Min Recall ≥75%, Prediction Horizon up to 24 hours, Alert Latency ≤60 seconds." | RFP v5, §6.5 Table; BRD v1.5 §3.5.4 Table | Functional | Phase 5 | STATED |
| AI-A12 | Security & Perimeter Agent — monitoring scope | "Integrates with the airport's PSIM and access control systems to provide a spatially contextualised security intelligence layer." | RFP v5, §6.3.7; BRD v1.5 Table line ~448 | Functional | Phase 5 | STATED |
| AI-A13 | Security Agent — precision/recall | "Min Precision ≥88%, Min Recall ≥82%, Real-time/15 min, Alert Latency ≤10 seconds." | RFP v5, §6.5 Table; BRD v1.5 §3.5.4 Table | Functional | Phase 5 | STATED |
| AI-A14 | Passenger Flow Agent (BRD v1.5 only — not in RFP agent list) | "Real-time passenger flow mapping; congestion prediction; ATRS bag count and DFMD count monitoring." + Min Precision ≥85%, recall ≥80%, Horizon up to 45 min, latency ≤15s. | BRD v1.5 Table line ~446; BRD v1.5 §3.5.4 Table | Functional | Phase 5 | STATED |
| AI-A15 | Structural Integrity Agent (BRD v1.5 only) | "Long-term structural performance; anomaly detection; settlement and movement analysis." + Min Precision ≥90%, recall ≥85%, Horizon up to 7 days, latency ≤60s. | BRD v1.5 Table line ~447; BRD v1.5 §3.5.4 Table | Functional | Phase 5 | STATED |
| AI-A16 | Agent commercial item (Table 6 Item 2) | "AI agent that's generic and configurable to Mechanical and HVAC, Electrical, Fire safety, Security and perimeter, Water and Drainage. Any other operations shall be configured." (Table 6, Item 2). | Commercial | Phase 4 | STATED |
| AI-A17 | Annual AI Platform Support — per annum | "Annual AI Platform Support and Model Retraining (per yr)" (Table 6, Item 12). | Commercial | Phase 5-O&M | STATED |
| AI-A18 | Data Readiness Gate (Register AI-01) | "Before any agent build starts, complete a per-domain data audit: confirm >=12 months of usable history, tag-to-asset mapping coverage, and data quality. Publish a Data Readiness Report." | Final requirements.xlsx.md, AI-01 | Functional | Phase 5 | STATED |
| AI-A19 | Per-agent acceptance M5 (Register AI-17) | "Each agent is accepted individually against its own Sec 6.5 row on the rolling 90-day evaluation window... Milestone M5 achieved when all wave gates have passed." | Final requirements.xlsx.md, AI-17 | Deliverable | Phase 5 | STATED |

### E3. AI Model Governance

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| GOV-01 | Explainability — plain-language + confidence % | "All predictive alerts shall be accompanied by a plain-language explanation of the contributing factors and a confidence score expressed as a percentage." | RFP v5, §6.4; BRD v1.5 §3.5.5 | Compliance | Phase 5 | STATED |
| GOV-02 | Auditability — 5-year log | "A complete audit log of all AI-generated alerts, including input data, model version, timestamp, and operator response, shall be maintained for a minimum of five (5) years." | RFP v5, §6.4; BRD v1.5 §3.5.5 | Compliance | Phase 5 | STATED |
| GOV-03 | Feedback loop from operators | "Operators shall be able to provide feedback on alert accuracy and relevance, which shall be used in model retraining cycles." | RFP v5, §6.4; BRD v1.5 §3.5.5 | Functional | Phase 5 | STATED |
| GOV-04 | Model version control — rollback ≤4h | "All model versions shall be documented and retained. Rollback to a previous version shall be achievable within four (4) hours." | RFP v5, §6.4; BRD v1.5 §3.5.5 | Functional | Phase 5 | STATED |
| GOV-05 | No black box — SHAP/LIME/attention viz | "Deep learning models shall use interpretability techniques (SHAP, LIME, or attention visualisation) to enable audit of model decision factors." | RFP v5, §6.4 | Compliance | Phase 5 | STATED |
| GOV-06 | DIAL ownership of AI models/data (BRD v1.5 only) | "DIAL shall own all AI model weights and training data generated under this contract." | BRD v1.5 §3.5.5 | Commercial/Legal | Phase 5 | STATED |
| GOV-07 | MLOps quarterly reporting (Register AI-05) | "Operate the model lifecycle across the 5-year O&M term: monthly drift monitoring; quarterly retraining; DIAL approval before every production release." | Final requirements.xlsx.md, AI-05 | Functional | Phase 5-O&M | STATED |

---

## F. OT Asset Visualization & Widgets — by System

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| OTW-01 | T1 HVAC visualization (~1000 equipment, 8 chillers, 28 pumps, 8 CTs…) | "Display Equipments (1000) in appropriate locations for: 8 Chiller Units, 28 Pumps, 8 Cooling Tower, 4 Chemical Dosing System, 2 Auto Tube Cleaning System, 6 CHW POT STNR & Air SEPRTR Tank, 260 AHU/TFA-FM&VM, 52 PAHU Units, 180 DX Units, 8 Cassette AC-Chilled Water, 120 Ceiling Suspended-AHU, 144 Fan Coil Unit, 138 FCU Non-Critical, 1 Air Compressor Supply System Roof." | Final requirements.xlsx.md, T1 HVAC | Functional | Phase 2 | STATED |
| OTW-02 | T1 FDAS visualization (~17000 devices) | "FDAS (17400) — Detectors & Loop level flow monitors for sprinklers." | Final requirements.xlsx.md, T1 FDAS | Functional | Phase 2 | STATED |
| OTW-03 | T1 VHT visualization (26 lifts, 16 escalators, 12 travelators) | "26 LIFT, 16 ESCALATOR, 12 TRAVLATOR." | Final requirements.xlsx.md, T1 VHT | Functional | Phase 1c | STATED |
| OTW-04 | T1 PBB visualization (22 hydraulic PBBs) | "22 PBB-Hydraulic." | Final requirements.xlsx.md, T1 PBB | Functional | Phase 1c | STATED |
| OTW-05 | T1 VDGS visualization (90 AVDGS + SNI/WGS) | "90 AVDGS & SNI/WGS." | Final requirements.xlsx.md, T1 VDGS | Functional | Phase 1c | STATED |
| OTW-06 | T1 BHS visualization (~500 assets: check-in rows, conveyors, diverters, sorters, screening machines, carousels…) | Detailed list of 22+ BHS sub-systems (Final requirements.xlsx.md). | Functional | Phase 2 | STATED |
| OTW-07 | T1 LCMS — Actuators (system needs upgrade) | "LCMS: Actuators. System needs upgrade." | Final requirements.xlsx.md, T1 LCMS | Functional | Phase 2 | STATED (conditional) |
| OTW-08 | T1 ECMS — Transformers (system needs upgrade) | "ECMS: Transformers. System needs upgrade." | Final requirements.xlsx.md, T1 ECMS | Functional | Phase 2 | STATED (conditional) |
| OTW-09 | T1 ATRS visualization (24 units) | "24 units." | Final requirements.xlsx.md, T1 ATRS | Functional | Phase 2 | STATED |
| OTW-10 | T1 GPU-PCA visualization (22 GPU, 22 PCA) | "22 GPU, 22 PCA units." | Final requirements.xlsx.md, T1 GPU-PCA | Functional | Phase 2 | STATED |
| OTW-11 | T2 HVAC visualization (~500 equipment, 7 chillers, 10 pumps…) | "Display Equipments in appropriate locations for: 7 Chillers, 10 Pumps, 9 Cooling Towers, 80 AHUs/TFA, 2 PAHU, 194 DX Units…" | Final requirements.xlsx.md, T2 HVAC | Functional | Phase 2 | STATED |
| OTW-12 | T2 FDAS visualization (~5000 devices) | "FDAS - Detectors & Loop level flow monitors for sprinklers." (~5000 points). | Final requirements.xlsx.md, T2 FDAS | Functional | Phase 2 | STATED |
| OTW-13 | T2 VHT visualization (13 lifts, 4 escalators) | "1. 13 LIFT, 2. 4 ESCALATOR." | Final requirements.xlsx.md, T2 VHT | Functional | Phase 2 | STATED |
| OTW-14 | T2 PBB — TBD count | "PBB: TBD." | Final requirements.xlsx.md, T2 PBB | Functional | Phase 2 | AMBIGUOUS |
| OTW-15 | T2 BVDGS — TBD count | "BVDGS: TBD." | Final requirements.xlsx.md, T2 BVDGS | Functional | Phase 2 | AMBIGUOUS |
| OTW-16 | T2 BHS visualization (~250 assets): 72 check-in counters, conveyors, diverters, sorters… | Detailed list of BHS sub-systems (Final requirements.xlsx.md). | Functional | Phase 2 | STATED |
| OTW-17 | T2 LCMS/ECMS/ATRS/GPU-PCA — TBD counts | All marked "TBD" or "# of units." | Final requirements.xlsx.md | Functional | Phase 2 | AMBIGUOUS |
| OTW-18 | T3 HVAC visualization (~3000 equipment: 16 chillers, 31 pumps, 16 CTs…) | Detailed equipment list (Final requirements.xlsx.md). | Functional | Phase 1c | STATED |
| OTW-19 | T3 FDAS visualization (~65000 devices) | "FDAS - Detectors & Loop level flow monitors for sprinklers. If limited to loop level, it will be count/150." | Final requirements.xlsx.md, T3 FDAS | Functional | Phase 1c | STATED |
| OTW-20 | T3 VHT visualization (79 lifts, 83 travelators, 37 escalators, 1 CMS) | "79 Lifts, 83 Travelators, 37 Escalator, 1 CMS." | Final requirements.xlsx.md, T3 VHT | Functional | Phase 1b | STATED |
| OTW-21 | T3 PBB visualization (57 hydraulic + 21 electro-mechanical) | "57 PBB-Hydraulic, 21 PBB-Electro-Mechanical." | Final requirements.xlsx.md, T3 PBB | Functional | Phase 1b | STATED |
| OTW-22 | T3 VDGS visualization (88 AVDGS) | "88 AVDGS." | Final requirements.xlsx.md, T3 VDGS | Functional | Phase 1b | STATED |
| OTW-23 | T3 BHS visualization (~1300 assets): 14 check-in rows, conveyors, sorters… | Detailed list of BHS sub-systems (Final requirements.xlsx.md). | Functional | Phase 2 | STATED |
| OTW-24 | T3 LCMS — Actuators ~2600 (system needs upgrade) | "LCMS: Actuators (2600). System needs upgrade." | Final requirements.xlsx.md, T3 LCMS | Functional | Phase 2 | STATED (conditional) |
| OTW-25 | T3 ECMS — Transformers ~200 (system needs upgrade) | "ECMS: Transformers (200). System needs upgrade." | Final requirements.xlsx.md, T3 ECMS | Functional | Phase 2 | STATED (conditional) |
| OTW-26 | T3 ATRS visualization (10 units) | "10 units." | Final requirements.xlsx.md, T3 ATRS | Functional | Phase 1b | STATED |
| OTW-27 | T3 GPU-PCA visualization (88 GPU, 88 PCA) | "88 GPU, 88 PCA of units." | Final requirements.xlsx.md, T3 GPU-PCA | Functional | Phase 1b | STATED |
| OTW-28 | PESC OT assets (~800: 166 X-Ray, 238 ETD, 356 DFMD…) | "1. 166 X-Ray, 2. 238 Explosive Trace Detector, 3. 356 Door Frame Metal Detector…" | Final requirements.xlsx.md, OT Assets PESC | Functional | Phase 2 | STATED |
| OTW-29 | WTP visualization (10 tanks) | "WTP: Reception & Distribution tanks." (~10 assets). | Final requirements.xlsx.md, OT Assets WTP | Functional | Phase 1c | STATED |
| OTW-30 | STP visualization (10 tanks) | "STP: Reception & Distribution tanks." (~10 assets). | Final requirements.xlsx.md, OT Assets STP | Functional | Phase 1c | STATED |
| OTW-31 | MRSS visualization (~250: incoming lines + breakers) | "Incoming lines: 4, Breakers to Substations: 240." | Final requirements.xlsx.md, OT Assets MRSS | Functional | Phase 1c | STATED |
| OTW-32 | Solar-Panels visualization | "Solar-Panels." | Final requirements.xlsx.md, OT Assets Solar | Functional | Phase 2 | STATED |
| OTW-33 | AGL CMS visualization | "AGL. Need to carve out the details." | Final requirements.xlsx.md, OT Assets AGL | Functional | Phase 2 | AMBIGUOUS |
| OTW-34 | ITBMS — T3 Integrations for PBB/GPU/PCA/VDGS/VHT/FDAS(ECMS) partial | "ITBMS: T3 Integrations for PBB, GPU, PCA, VDGS, VHT, FDAS (Partial), ECMS(Partial). Ignore ASB OT Systems." | Final requirements.xlsx.md, OT Assets ITBMS | Functional | Phase 2 | STATED |
| OTW-35 | Click-any-asset → widget display | "The system on the click of any Asset shall display Widgets with respective critical values / information related to the asset. For each equipment — One widget." | Final requirements.xlsx.md, FR-DTW-15 | Functional | Phase 2 | STATED |
| OTW-36 | HVAC chiller KPIs per system/township | "HVAC - Chiller: Run/stop/fault, mode, CHW supply/return temperature, condenser temperatures, flow, pressure, load %, kW." (per terminal counts). | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1a | STATED |
| OTW-37 | HVAC CHW/condenser pump KPIs | "Run/stop/fault, speed, suction/discharge pressure, differential pressure, flow, current, vibration, bearing temperature." | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1b | STATED |
| OTW-38 | HVAC cooling tower KPIs | "Fan status/speed, entering/leaving water temperature, basin level, conductivity, make-up water flow." | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1b | STATED |
| OTW-39 | HVAC AHU PAHU Cassette AC FCU Package AC Air-cleaner Air-compressor — all KPIs | Multiple lines with specific telemetry per unit type. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1b/1c | STATED |
| OTW-40 | FDAS KPIs — FACP/detector/sprinkler/module | "Current state, zone/loop" per device class. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1b/1c | STATED |
| OTW-41 | VHT KPIs — lift/escalator/travelator | "Available/out-of-service/fault, floor/direction, door state, load/overload, operating mode." | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1a | STATED |
| OTW-42 | PBB KPIs — stowed/docked/in-motion, extension/elevation/rotation, auto-level… | KPI details per bridge. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1a | STATED |
| OTW-43 | VDGS KPIs — available/active, stand open/closed, distance-to-stop, azimuth deviation… | KPI details per unit. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1a | STATED |
| OTW-44 | GPU KPIs — Ready/connected/on-load/fault, output voltage/frequency/current/kW/kVA/power factor… | KPI details. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1a | STATED |
| OTW-45 | PCA KPIs — ready/running/fault, supply-air temperature, airflow, pressure… | KPI details. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1a | STATED |
| OTW-46 | ATRS KPIs — Lane availability, trays available/in circulation, tray position, jam/fault… | KPI details. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1b | STATED |
| OTW-47 | BHS conveyor/sorter/carousel/screening machine KPIs | Multiple lines with belt speed, bag count, fault states. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1c | STATED |
| OTW-48 | WTP/STP/MRSS KPIs — tank level, flow, quality, voltage/current, load, breaker state… | KPI details. | Final requirements.xlsx.md, OT Systems KPIs | Functional | Phase 1b | STATED |
| OTW-49 | IT Assets visualization cap at 3000 | "IT Assets Visualization. Capped to 3000." | Final requirements.xlsx.md, IT Assets | Functional | Phase 1b | STATED |

---

## G. IT System Integration & Airport Operational Feeds

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| ITI-01 | AODB integration | "Airport-wide KPI set: ATM (Sched/Actual), OTP, Stand/Runway utilisation & idle alerts, delays, Pax volume, FB/LB compliance, FIDS, flight milestones, slot adherence (OneAPOC Phase-1 scope items 1-13)." | Final requirements.xlsx.md, AODB | Functional | Phase 1a | STATED |
| ITI-02 | UTAM feed — airside KPIs | "Airside/turnaround KPI feed: ATM, OTP, stand & runway utilisation, CDM milestones, VTT/AIBT/AOBT alerts (UTAM screens UTAM-001 to UTAM-014)." | Final requirements.xlsx.md, UTAM | Functional | Phase 1a | STATED |
| ITI-03 | ADS-B integration | "Real-time aircraft position: 10-mile final approach through touchdown/taxi/stand (arrivals) and stand/taxi/runway/take-off to 10 miles out (departures), across 4 runways and 180+ stands." | Final requirements.xlsx.md, ADS-B | Functional | Phase 1b | STATED |
| ITI-04 | RMS integration | "Resource master for fixed & movable assets — stands, taxiways, runways, check-in counters, ATRS, DFMD, GSE, etc." | Final requirements.xlsx.md, RMS | Functional | Phase 1b | STATED |
| ITI-05 | Kloudspot integration | "Real-time queue length, wait-time and processing-time by touchpoint — used only where PARAM does not already provide this." | Final requirements.xlsx.md, Kloudspot | Functional | Phase 1a | STATED |
| ITI-06 | XOVIS integration | "Real-time queue length, wait-time and processing-time by touchpoint (Entry, Check-in, PESC, Immigration) — used only where PARAM does not already provide this." | Final requirements.xlsx.md, XOVIS | Functional | Phase 1a | STATED |
| ITI-07 | ARC integration | "Passenger & resource forecasting output (expected volumes) plus location-tagged alerts from PARAM." | Final requirements.xlsx.md, ARC | Functional | Phase 1a | STATED |
| ITI-08 | PTM — transfer passenger details | "Transfer-passenger detail records, with location-tagged alerts." | Final requirements.xlsx.md, PTM | Functional | Phase 1b | STATED |
| ITI-09 | SAC — scope TBD | "SAC. Scope and point count not yet defined — to be confirmed with the Security & Vigilance / OT team during Phase-1 discovery." | Final requirements.xlsx.md, SAC | Functional | Phase 1b | AMBIGUOUS |
| ITI-10 | VMS/CCTV live feed on DT | "Live feed to display on digital twin." | Final requirements.xlsx.md, VMS/CCTV | Functional | Phase 1c | STATED |
| ITI-11 | GIS (ArcGIS) integration | "GIS — ARC GIS." | Final requirements.xlsx.md, GIS | Functional | Phase 1b | STATED |
| ITI-12 | SAP federation — assets make/model/purchase | "SAP: Assets make, model, Purchase etc." | Final requirements.xlsx.md, SAP | Functional | Phase 1c | STATED |
| ITI-13 | ITOM/ManageEngine integration | "IT infrastructure/connector health telemetry (not an airport OT system — monitors the integration layer itself)." | Final requirements.xlsx.md, ITOM | Functional | Phase 1c | STATED |
| ITI-14 | Telematics GSE position feed | "GSE (vehicle) position feed — count of tracked GSE assets to be confirmed with Telematics/RMS owner." | Final requirements.xlsx.md, Telematics | Functional | Phase 1b | STATED |
| ITI-15 | Reverse PaxFlow — overstaying/unidentified passenger event count | "Overstaying / unidentified-passenger event count (derived, not a native OT feed)." | Final requirements.xlsx.md, Reverse PaxFlow | Functional | Phase 2 | STATED |

---

## H. Passenger Processing & Gate Systems

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| PPS-01 | DigiYatra integration | "DigiYatra." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase 1b | STATED |
| PPS-02 | 2D Barcode scanner integration | "2D Barcode Scanner." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase 1b | STATED |
| PPS-03 | CUSS integration | "CUSS — Common Use Self Service." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase 1b | STATED |
| PPS-04 | CUPPS integration | "CUPPS — Central Unit of Passenger Processing System." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase 1c | STATED |
| PPS-05 | SBD (Secondary Baggage Detector) | "SBD." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase 1b | STATED |
| PPS-06 | Check-in counters integration | "Check-in Counters." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase N/A | STATED |
| PPS-07 | Boarding gate scanners integration | "Boarding Gate Scanners." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase 1c | STATED |
| PPS-08 | Baggage scanners integration | "Baggage Scanners." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase 2 | STATED |
| PPS-09 | FIDS integration | "FIDS — Flight Information Display System." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase N/A | STATED |
| PPS-10 | AFTN integration | "AFTN — Aeronautical Fixed Telecommunication Network." | Final requirements.xlsx.md, Passenger Processing Systems | Functional | Phase N/A | STATED |

---

## I. Operational Widgets & Dashboard Requirements

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| OPS-01 | Airport Summary KPIs | "The system shall display Airport level summary with key KPIs and insights. KPIs across Landside/Terminal/Airside will be displayed." (FR-DTW-01) | Final requirements.xlsx.md | Functional | Phase 1a | STATED |
| OPS-02 | Facility-status roll-up | "Facility-status roll-up expected alongside the KPIs landing view. As this is RBAC enabled, each persona will receive KPIs curated for their role." (FR-DTW-02) | Final requirements.xlsx.md | Functional | Phase 1b | STATED |
| OPS-03 | Terminal Summary per terminal | "The system shall display Terminal level summary for each terminal with key KPIs and insights." (FR-DTW-03) | Final requirements.xlsx.md | Functional | Phase 1a | STATED |
| OPS-04 | Airside summary | "The system shall display Airside summary with key KPIs and insights." (FR-DTW-04) | Final requirements.xlsx.md | Functional | Phase 1a | STATED |
| OPS-05 | Curbside summary KPIs | "The system will have Curbside summary with key KPI and insights." | Final requirements.xlsx.md | Functional | Phase 1b | STATED |
| OPS-06 | Airside Ops — GSE telematics display | "Display near-realtime positions of GSE using telematics data." (FR-DTW-AOPS-01) | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-07 | Airside Ops — flight position tracking | "Display near-realtime flight position from 10 Miles out to Landing to Runway to Taxiway to Stands for arrival flights and vice versa for departure flights." (FR-DTW-AOPS-02) | Final requirements.xlsx.md | Functional | Phase 1b | STATED |
| OPS-08 | Airside Ops — turnaround activity monitoring | "Display near-realtime Flight Information, Turnaround activities. All monitored turnaround activities with timestamp, Progress and RAG for each flight." (FR-DTW-AOPS-03) | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-09 | Airside Ops — alerts display | "Display Airside Alerts with location information." (FR-DTW-AOPS-04) | Final requirements.xlsx.md | Functional | Phase 1b | STATED |
| OPS-10 | Airside Ops — performance KPIs (OTP, stand/gate occupancy…) | "Airside performance KPIs — OTP, Stand and gate occupancy/utilization, Slot utilization." (FR-DTW-AOPS-05) | Final requirements.xlsx.md | Functional | Phase 1b | STATED |
| OPS-11 | Turnaround metrics — TOBT/EIBT | "Display Turnaround Metrics — for efficiency, turnaround time, and Delay codes (TOBT, EIBT)." (FR-DTW-AOPS-06) | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-12 | Predictive turnaround metrics — POBT/PRBT/PIBT | "Display predictive turnaround metrics — POBT, PRBT, PIBT." (FR-DTW-AOPS-07) | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-13 | Airside Ops — weather/RVR display | "Display Other Metrics — RVR, Weather conditions." (FR-DTW-AOPS-08) | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-14 | Live airside camera integration | "Live airside camera integration — on-demand live turnaround visualization." (FR-DTW-AOPS-09) | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-15 | Safety & Compliance monitoring module | "Speed violation, path deviation, and geofence breach alerts. Compliance monitoring for GSE route adherence alerts." (FR-DTW-AOPS-10) | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-16 | Airside playback, analytics, reporting | "Historical playback of aircraft/GSE movement for operational review." (FR-DTW-AOPS-11) | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-17 | NOTAM alert display | "NOTAM alert (active and upcoming) will be displayed on the DT with the corresponding area highlighted on the airside." (FR-DTW-AOPS-12) | Final requirements.xlsx.md | Functional | Phase 1b | STATED |
| OPS-18 | Terminal Ops KPI summary (Entry/Check-in/Security/Immigration/Gates/Retail…) | "KPI Summary: Display a consolidated Terminal Operations KPI summary covering Entry, Check-in, Security, Immigration, Emigration, Transfer, Customs, Gates, Retail, F&B and passenger facilities." | Final requirements.xlsx.md | Functional | Phase 1b | STATED |
| OPS-19 | Queue management across touchpoints | "Queue length, Wait time, Processing time. Entry, Check-in, Security, Immigration, Emigration, Transfer, Customs, Gates." (FR-DTW-TOPS-02) | Final requirements.xlsx.md | Functional | Phase 1b | STATED |
| OPS-20 | Crowd management heatmaps | "Crowd Management: Heatmaps across the touch points and zones." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-21 | Dwell/Journey Time calculation | "Dwell and Journey Time: calculate dwell time within zones and journey time between selected touchpoints." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-22 | Retail/F&B store performance trends | "Retail and F&B: Store Performance Trends." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-23 | Store location analysis using passenger flow/dwell time | "Store Location Analysis: analysis using passenger flows, dwell time." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-24 | Camera access from DT alert/zone | "Camera Access: Select an alert or terminal zone in the Digital Twin and open the associated live CCTV feeds." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-25 | Counter/desk allocation & utilisation | "Counter and Desk Allocation, counter Manning Status, Counter Utilisation (Check-in, Security)." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-26 | Historical terminal playback | "Historical Terminal Playback: provide historical playback of passenger flows, queues, flight events." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-27 | Curbside KPI summary + live vehicle monitoring | "KPI Summary. Live Vehicle Monitoring: Display number of vehicles currently present in arrival and departure ramps." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-28 | Vehicle classification (private car/app-based/bus/shuttle/emergency) | "Vehicle Classification: Classify detected vehicles into configurable categories such as private car, app-based cab, bus, shuttle, and emergency vehicle." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-29 | Curb occupancy/availability + RAG status | "Curb Occupancy and Availability: Calculate the occupied and available capacity for operational zones and represent RAG status indicators." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-30 | Vehicle dwell time calculation | "Vehicle Dwell Time: Calculate vehicle dwell time from entry into a curbside zone until exit." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-31 | Curbside incident identification (overstay/parking violations) | "Incident identification: Overstay Detection, Traffic and Parking Violations." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-32 | Congestion heatmap at curbside | "Congestion Heatmap: Display a real-time curbside congestion heatmap derived from vehicle density." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-33 | Ground transport availability + passenger waiting time | "Ground Transport Availability, Passenger Waiting Time for transport facility." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-34 | Curbside crowd monitoring (meet-and-greet) | "Crowd monitoring and alerting at curbside: Meet-and-Greet Crowd Management." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-35 | Parking monitoring (occupancy/available slots/throughput) | "Parking Monitoring: display parking occupancy, available slots, entry and exit throughput." | Final requirements.xlsx.md | Functional | Phase 2 | STATED |
| OPS-36 | Trolley availability + alerts | "Trolley Availability: display available, required and total trolley counts at each trolley bay and generate alerts when availability falls below the configured threshold." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-37 | Lift/escalator/washroom facility status | "Facility Status: Display the status of lifts, escalators, washrooms." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-38 | Security — intrusion & reverse-entry detection | "Intrusion and Reverse-entry Detection: Reverse movement through controlled passages and intrusion into configured restricted zones." (FR-DTW-SEC-01) | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-39 | Security — unattended baggage alert | "Unattended Baggage alert: display a spatially located alert when an object remains unattended beyond the configured duration in a monitored terminal zone." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-40 | Security — suspicious behaviour detection | "Suspicious Behaviour Detection: alerts for patterns such as prolonged loitering, repeated movement at a restricted location, etc." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-41 | Security — camera access from event | "Camera Access: Select a security event in the Digital Twin and open the associated live CCTV feeds." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| OPS-42 | SAC smart washroom (BLE gateways/sensors) | "Smart Washroom which is IoT based (BLE Gateways, BLE based Sensors). Stall Occupancy displays & Feedback Displays installed partially at T3 and fully at T1." | Final requirements.xlsx.md, SAC | Functional | Phase 1b | STATED |
| OPS-43 | SAC smart buggy (BLE beacons + Android app) | "Smart Buggy (BLE Beacons + Android App)." | Final requirements.xlsx.md, SAC | Functional | Phase 1b | STATED |
| OPS-44 | SAC smart trolley (camera-based CV) | "Smart Trolley (Camera Based — Computer Vision)." | Final requirements.xlsx.md, SAC | Functional | Phase 1b | STATED |
| OPS-45 | SAC smart traffic (camera-based video analytics) | "Smart Traffic (Camera based — Video Analytics)." | Final requirements.xlsx.md, SAC | Functional | Phase 1c | STATED |
| OPS-46 | REST room management alerts | "Restroom management: Alert for washroom if the number of wash room used by patrons." | Final requirements.xlsx.md, SAC | Functional | Phase 2 | STATED |

---

## J. Simulation Use Cases (ABR §4 SPG Requirements)

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| SIM-01 | Simulation engine — "what-if" scenario planning capability | "Robust simulation and 'what-if' scenario planning capability to enable data-driven decision-making across operations and commercial domains." (ABR §4.1) | Functional | Phase 1c+2 | STATED |
| SIM-02 | Digital twin for running simulation | "Digital Twin for running simulation." (ABR §4.2 Architecture item 1) | Infrastructure | Phase 2 | STATED |
| SIM-03 | UI for managing scenarios (control variables) | "UI for managing scenarios (control variables)." (ABR §4.2 Architecture item 2) | Functional | Phase 2 | STATED |
| SIM-04 | Decision engine to provide results | "Decision engine to provide results." (ABR §4.2 Architecture item 3) | Functional | Phase 2 | STATED |
| SIM-05 | UI for visualization of scenarios and outcomes | "UI for visualization of scenarios and outcomes." (ABR §4.2 Architecture item 4) | Functional | Phase 2 | STATED |
| SIM-06 | Simulation modularity + continuously learning + AI/ML | "To ensure scalability and long-term value, the simulation engine should be modular, continuously learning, and integrated with the broader data and analytics platform." (ABR §4.1) | Functional | Phase 2 | STATED |
| SIM-07 | IROPS Simulation — disruptions/delays/emergencies | "Model disruptions, delays, emergency conditions." (SPG Table) | Functional | Phase 2 | STATED |
| SIM-08 | Evacuation & fire scenarios simulation | "Simulate safety evacuation and fire events." (SPG Table) | Functional | Phase 2 | STATED |
| SIM-09 | Breach detection simulation | "Identify and alert security breaches." (SPG Table) | Functional | Phase 2 | STATED |
| SIM-10 | Commercial — store mix optimization simulation | "Simulate changing store categories (e.g., F&B to retail) to assess impact on conversion, spend, and overall commercial penetration." (ABR §4.2) | Functional | Phase 2 | STATED |
| SIM-11 | Commercial — shelf merchandising optimization | "Test different product placements within stores (eye-level vs lower shelves) to maximize SKU-level sales and in-store conversion." | Functional | Phase 2 | STATED |
| SIM-12 | Commercial — store location optimization | "Evaluate shifting store positions within terminal flow to identify high-conversion zones beyond just high footfall." | Functional | Phase 2 | STATED |
| SIM-13 | Commercial — dwell time monetization | "Simulate impact of increased/decreased dwell time on F&B and retail revenue." | Functional | Phase 2 | STATED |
| SIM-14 | Commercial — campaign & promotion simulation | "Test effectiveness of promotions, bundles, and discounts in a virtual environment before real-world rollout." | Functional | Phase 2 | STATED |
| SIM-15 | Commercial — queue vs revenue trade-off | "Model impact of faster passenger processing vs controlled dwell zones to balance throughput with commercial revenue." | Functional | Phase 2 | STATED |
| SIM-16 | Commercial — gate allocation optimization | "Simulate assigning flights to different gates to optimize passenger exposure to commercial zones." | Functional | Phase 2 | STATED |
| SIM-17 | Commercial — lounge vs retail trade-off | "Assess how increased lounge access or capacity affects retail and F&B spend in the terminal." | Functional | Phase 2 | STATED |
| SIM-18 | Commercial — staffing vs sales optimization | "Simulate staffing levels in retail/F&B outlets to estimate revenue loss due to queues, under-service, or overstaffing." | Functional | Phase 2 | STATED |
| SIM-19 | Commercial — disruption monetization strategy | "Model delays or irregular operations to identify opportunistic revenue strategies." | Functional | Phase 2 | STATED |
| SIM-20 | Operational — passenger flow optimization | "Simulate passenger movement across terminal to identify bottlenecks and redesign pathways for smoother flow." | Functional | Phase 2 | STATED |
| SIM-21 | Operational — queue management optimization | "Test different counter openings, staffing levels, and queue designs to reduce wait times." | Functional | Phase 2 | STATED |
| SIM-22 | Operational — check-in & security capacity planning | "Simulate peak-hour loads to determine optimal number of counters and lanes required." | Functional | Phase 2 | STATED |
| SIM-23 | Operational — gate allocation & utilization | "Model different gate assignment strategies to minimize passenger congestion and improve aircraft turnaround efficiency." | Functional | Phase 2 | STATED |
| SIM-24 | Operational — disruption management simulation | "Model impact of delays, weather, or congestion scenarios and evaluate best mitigation strategies in advance." | Functional | Phase 2 | STATED |
| SIM-25 | Operational — workforce deployment optimization | "Simulate staff allocation across terminal zones to ensure optimal coverage during varying passenger loads." | Functional | Phase 2 | STATED |
| SIM-26 | Operational — baggage flow optimization | "Model baggage handling system load, routing logic, and peak surges." | Functional | Phase 2 | STATED |
| SIM-27 | Operational — curbside/curb-side traffic management | "Simulate passenger drop-off/pick-up flows, taxi queues, and vehicle congestion to optimize curbside operations." | Functional | Phase 2 | STATED |
| SIM-28 | Engineering — thermal load simulation | "Simulate impact of increased ambient temperature on indoor terminal temperature, HVAC load, and overall emissions." | Functional | Phase 2 | STATED |
| SIM-29 | Engineering — passenger load vs HVAC demand | "Model impact of passenger volume increase on cooling requirements, airflow distribution, and peak HVAC stress." | Functional | Phase 2 | STATED |
| SIM-30 | Engineering — retail expansion energy impact | "Simulate addition of shops/F&B outlets to assess impact on electricity consumption and incremental HVAC load." | Functional | Phase 2 | STATED |
| SIM-31 | Engineering — zone-based cooling optimization | "Test different HVAC zoning strategies (central vs segmented cooling) to optimize energy use while maintaining comfort." | Functional | Phase 2 | STATED |
| SIM-32 | Engineering — power infrastructure stress testing | "Simulate combined scenarios (traffic growth + temperature + commercial load) to evaluate transformer, DG, and electrical capacity limits." | Functional | Phase 2 | STATED |
| SIM-33 | NOTAM alert on DT banner for duration of issuance + resources blocked | "The system shall display NOTAM message on the DT banner for the duration of NOTAM issuance and display resources that are blocked." (Final requirements.xlsx.md) | Functional | Phase 1b | STATED |
| SIM-34 | EWS — early warning signals for queue thresholds/flight delay propagation | "Early warning signal for breach of wait time thresholds at queue touchpoints. Early warning signal for delay in flight take off at origin that may impact the flight landing time at airport." | Functional | Phase 1c | STATED |
| SIM-35 | What-if simulation (Final requirements.xlsx.md) — "Should be included as part of AirportEye. Deliver first version in 3 months." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |
| SIM-36 | Disruption management simulation (Final requirements.xlsx.md) — cascading impact on touchpoints | "The systems shall enable disruption simulation and the impact of the same on the different touch points and the cascading impact simulation. Deliver first version in 3 months." | Final requirements.xlsx.md | Functional | Phase 1c | STATED |

---

## K. Land & Space Management (BRD v1.5 §3.3.1) + Environmental Monitoring (§3.3.5)

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| LSM-01 | Digital footprint of all land and spaces | "Create a digital footprint of all land and spaces at IGIA with full attribute details." (BRD v1.5 §3.3.1) | Functional | Phase 3 | STATED |
| LSM-02 | Area/dimensions/usage/licensee/contract records | "Record area, dimensions, usage, purpose of use, licensee details, and contract periods with historical trail." | Functional | Phase 3 | STATED |
| LSM-03 | Allotment trail repository | "Create a repository of allotment trail going forward for all land parcels." | Functional | Phase 3 | STATED |
| LSM-04 | Multi-dimensional queries on land/space usage | "Enable multi-dimensional queries on land and space usage." | Functional | Phase 3 | STATED |
| LSM-05 | Monitor land usage per Master Plan + optimisation | "Monitor land usage as per IGIA Master Plan; assist in optimised land and space planning." | Functional | Phase 3 | STATED |
| LSM-06 | Alerts for unauthorized use/misuse | "Generate alerts for unauthorized or misuse of any land or space." | Functional | Phase 3 | STATED |
| LSM-07 | Integration with CLM tool | "Integrate with CLM tool to enhance functionality." | Infrastructure | Phase 3 | STATED |
| LSM-08 | Superimpose Master Plan/Revenue Map/satellite imagery over survey map | "Superimpose Master Plan, Revenue Map, and satellite imagery over survey map." | Functional | Phase 3 | STATED |
| LSM-09 | Digital classification of land types | "Digital classification of land: demised premises, additional demised premises, excluded premises, carved-out assets, MCD and DCB area bifurcation." | Functional | Phase 3 | STATED |
| ENV-01 | Borewell recharge monitoring (IoT sensor + Smartcity) | "Borewell recharge monitoring using IoT sensor integration (Smartcity)." (ABR §3.1 P&E) | Functional | Phase 2 | STATED |
| ENV-02 | Storm water analysis with IoT-enabled monitoring (Walter P Moore) | "Storm water analysis (Walter P Moore) with IoT-enabled monitoring (Smartcity)." (ABR §3.1 P&E) | Functional | Phase 2 | STATED |
| ENV-03 | Environmental monitoring — Shahabad MdPur (IMD/STP/ISWMC) | "Create digital footprint in Shahabad MdPur (IMD, STP and ISWMC)." (BRD v1.5 §3.3.5) | Functional | Phase 2 | STATED |
| ENV-04 | Noise monitoring terminals — funnel areas/Nursery | "Noise Monitoring Terminals in funnel areas and Nursery (CAQM Station)." (BRD v1.5 §3.3.5) | Functional | Phase 2 | STATED |

---

## L. Asset Registry, Federation & Ontology

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| AFR-01 | UI-based asset registry with unique name/serial/type/location/details | "The systems shall have UI based Asset Registry where below details can be added: Asset unique name, asset serial number, Asset type, asset sub group, location, more details." (Final requirements.xlsx.md) | Functional | Phase 2 | STATED |
| AFR-02 | One-way integration with asset manager system | "One way integration with asset manager system." (Final requirements.xlsx.md) | Infrastructure | Phase 2 | STATED |
| AFR-03 | CLG — Common Location Grid creation | "Create a CLG(Common Location Grid)." (Final requirements.xlsx.md: Asset commons) | Functional | Phase 1b | STATED |
| AFR-04 | CAI — Common Asset ID framework creation | "Create a CAI(Common Asset Id) framework." (Final requirements.xlsx.md: Asset commons) | Functional | Phase 1b | STATED |
| AFR-05 | Metadata store for assets | "Metadata store for asset." (Final requirements.xlsx.md: Asset commons) | Functional | Phase 1b | STATED |
| AFR-06 | Query by location/asset type/asset id/state | "Enable Query by location, Asset type / System, Asset id, State, etc." (Final requirements.xlsx.md: Asset commons) | Functional | Phase 1b | STATED |
| AFR-07 | Sync framework | "Sync framework." (Final requirements.xlsx.md: Asset commons) | Functional | Phase 1b | STATED |
| AFR-08 | User workflow for changes/onboarding new assets | "Facilitate changes and onboarding new assets with a user workflow." (Final requirements.xlsx.md: Asset commons) | Functional | Phase 1b | STATED |
| AFR-09 | Taxonomy for asset classification | "Taxonomy." (Final requirements.xlsx.md: Asset modeling) | Functional | Phase 1c | STATED |
| AFR-10 | Hierarchy model | "Hierarchy." (Final requirements.xlsx.md: Asset modeling) | Functional | Phase 1c | STATED |
| AFR-11 | Ontology/relationship model for assets | "Relationships aka Ontology." (Final requirements.xlsx.md: Asset modeling) | Functional | Phase 1c | STATED |
| AFR-12 | IT Asset Federation (~3000 assets) | "IT Asset Federation. Capped to 3000." (Final requirements.xlsx.md: Asset Federation) | Infrastructure | Phase 1b | STATED |
| AFR-13 | SAP federation | "SAP federation." (Final requirements.xlsx.md: Asset Federation) | Infrastructure | Phase 1c | STATED |
| AFR-14 | ArcGIS asset federation | "ArcGIS Asset federation." (Final requirements.xlsx.md: Asset Federation) | Infrastructure | Phase 1c | STATED |
| AFR-15 | RMS asset federation | "RMS Asset Federation." (Final requirements.xlsx.md: Asset Federation) | Infrastructure | Phase 1b | STATED |
| AFR-16 | VMS/CCTV asset federation — show live video from DT | "VMS Asset Federation (to show live video from DT)." (Final requirements.xlsx.md: Asset Federation) | Functional | Phase 1c | STATED |

---

## M. Infrastructure Architecture

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| INF-01 | Modular cloud-native (or cloud-ready hybrid) architecture | "The Digital Twin Platform shall be delivered as a modular, cloud-native (or cloud-ready hybrid) architecture." (BRD v1.5 §3.4.1; RFP v5, §2.6) | Infrastructure | Phase 4 | STATED |
| INF-02 | High availability ≥99.5% | "Key requirements include high availability (≥99.5%)…" (RFP v5, §7) | Non-Functional | Phase 4 | STATED |
| INF-03 | Low latency ≤5 seconds | "low latency (≤5 seconds)" (RFP v5, §7) | Non-Functional | Phase 4 | STATED |
| INF-04 | Cybersecurity compliance per IEC 62443 | "cybersecurity compliance" (RFP v5, §7); explicit IEC 62443 requirement in BRD/RFP. | Compliance | Phase 4 | STATED |
| INF-05 | Data sovereignty — India-only storage | "All data generated, processed, or stored under this contract shall be stored exclusively within the geographical boundaries of India unless explicitly authorised in writing by DIAL." (RFP v5, §9.6; BRD v1.5 §9.10) | Compliance | Phase 4 | STATED |
| INF-06 | Modularity / scalability — no fundamental re-architecture for expansion | "The platform architecture must be modular and cloud-native (or cloud-ready hybrid), capable of scaling to accommodate additional buildings, systems, and data sources without requiring fundamental re-architecture." (RFP v5, §2.6) | Infrastructure | Phase 4 | STATED |
| INF-07 | Compute infrastructure — on-prem servers/GPU nodes/virtualization | "Compute Infrastructure — On-Prem: Servers, GPU nodes, virtualisation platform" (Table 7 Item 1). | Commercial | Phase 4 | STATED |
| INF-08 | Storage infrastructure — on-prem high-perf + archival | "Storage Infrastructure — On-Prem: High-performance + archival storage systems" (Table 7 Item 2). | Commercial | Phase 4 | STATED |
| INF-09 | Network infrastructure — core switches/firewalls/load balancers/segmentation | "Network Infrastructure: Core switches, firewalls, load balancers, segmentation" (Table 7 Item 3). | Commercial | Phase 4 | STATED |
| INF-10 | Data Centre setup/upgrade | "Data Centre Setup / Upgrade: Rack space, power, cooling, physical infrastructure" (Table 7 Item 4). | Commercial | Phase 4 | STATED |
| INF-11 | Cloud compute (VM instances/containers/serverless) — per annum | "Cloud Infrastructure Compute" (Table 7 Item 5). | Commercial | Phase 4 | STATED |
| INF-12 | Cloud storage (object/backup/archival tiers) — per TB/annum | "Cloud Infrastructure Storage" (Table 7 Item 6). | Commercial | Phase 4 | STATED |
| INF-13 | Cloud networking/data transfer/CDN — per annum | "Cloud Networking and Data Transfer" (Table 7 Item 7). | Commercial | Phase 4 | STATED |
| INF-14 | Disaster Recovery site setup/replication/failover | "Disaster Recovery Infrastructure" (Table 7 Item 8). | Commercial | Phase 4 | STATED |
| INF-15 | Backup and archival systems — software + storage + retention | "Backup and Archival Systems" (Table 7 Item 9). | Commercial | Phase 4 | STATED |
| INF-16 | Infrastructure monitoring/management tools — per annum | "Infrastructure Monitoring and Management Tools" (Table 7 Item 10). | Commercial | Phase 4 | STATED |
| INF-17 | Cybersecurity infrastructure — IAM/SIEM/endpoint/encryption | "Cybersecurity Infrastructure: IAM, SIEM, endpoint security, encryption" (Table 7 Item 11). | Commercial | Phase 4 | STATED |
| INF-18 | Middleware/platform infrastructure — IoT platform/data ingestion/API gateways | "Middleware / Platform Infrastructure" (Table 7 Item 12). | Commercial | Phase 4 | STATED |
| INF-19 | Deployment/configuration/testing/installation | "Deployment and Configuration: Installation, setup, configuration, testing" (Table 7 Item 13). | Commercial | Phase 4 | STATED |
| INF-20 | Performance testing/optimization/load testing/benchmarking | "Performance Testing and Optimisation" (Table 7 Item 14). | Commercial | Phase 4 | STATED |
| INF-21 | Infrastructure documentation/handover — design docs/SOPs/runbooks | "Infrastructure Documentation and Handover" (Table 7 Item 15). | Deliverable | Phase 4 | STATED |
| INF-22 | Platform designed for minimum 15-year operational lifecycle | "DIAL expects the platform to serve the Airport's operational needs for a minimum of fifteen (15) years from the date of initial commissioning." (RFP v5, §2.6; BRD v1.5 Objective 6) | Non-Functional | Phase 4 | STATED |
| INF-23 | Software licensing for long-term usage independent of vendor | "All software components must be licensed in a manner that provides DIAL with long-term usage rights independent of the vendor's commercial continuity." (RFP v5, §2.6) | Commercial/Legal | Phase 4 | STATED |

---

## N. Non-Functional Requirements

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| NFR-01 | Platform uptime ≥99.5% (excl planned maintenance) | "Platform Uptime: ≥ 99.5% (excluding planned maintenance). Monthly SLA Report." (KPI Table item 1; Final requirements.xlsx.md line 953) | Non-Functional | Phase 1b/ongoing | STATED |
| NFR-02 | Real-time data latency ≤5 seconds sensor-to-dashboard | "Real-time Data Latency: ≤ 5 seconds from sensor to dashboard." (KPI Table item 2; Final requirements.xlsx.md line 955) | Non-Functional | Phase 1a/ongoing | STATED |
| NFR-03 | BIM model LOD compliance — 100% specified assets | "BIM Model LOD Compliance: 100% of specified assets at agreed LOD." (KPI Table item 3; Final requirements.xlsx.md line 953) | Non-Functional | Phase 1c/milestone | STATED |
| NFR-04 | Predictive alert accuracy ≥80% precision / ≥75% recall | "Predictive Alert Accuracy: Precision ≥ 80%, Recall ≥ 75%." (KPI Table item 4; Appendix C SLA) | Non-Functional | Phase 5/ongoing | STATED |
| NFR-05 | Geospatial data accuracy: H ≤5cm RMSE / V ≤3cm RMSE | "Geospatial Data Accuracy: Horizontal ≤ 5 cm RMSE, Vertical ≤ 3 cm RMSE." (KPI Table item 5; SLA) | Non-Functional | Phase 1/milestone | STATED |
| NFR-06 | Incident response time critical ≤10 mins | "Incident Response Time (Critical): ≤ 10 minutes from notification." (Appendix C SLA item 6) | Non-Functional | Phase 1b/ongoing | STATED |
| NFR-07 | System integration coverage — 100% within 3 months go-live | "System Integration Coverage: 100% of agreed BMS/IoT data points within 3 months of go-live." (KPI Table item 7; SLA) | Non-Functional | Phase 4/milestone | STATED |
| NFR-08 | RTO — 4 hours | "RTO: 4 hours." (Final requirements.xlsx.md line 961) | Non-Functional | Phase 1b | STATED |
| NFR-09 | RPO — 24 hours | "RPO: 24 hours." (Final requirements.xlsx.md line 962) | Non-Functional | Phase 1b | STATED |
| NFR-10 | Service and support — 24×7 | "Service and Support: 24x7." (Final requirements.xlsx.md line 959) | Non-Functional | Phase 1c/ongoing | STATED |

---

## O. Security, Privacy & Compliance

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| SEC-01 | SSO via SAML 2.0 or OAuth 2.0 | "Integration with DIAL's existing Identity Provider (IdP) via SAML 2.0 or OAuth 2.0." (RFP v5, §3.5.2; BRD v1.5 §3.4.4) | Compliance | Phase 1a | STATED |
| SEC-02 | MFA enabled for users | "Multi-factor authentication." (BRD v1.5 §3.4.4) | Compliance | Phase 1a | STATED |
| SEC-03 | RBAC minimum 5 roles + additional custom roles | "Role-based access control with a minimum of five (5) defined user roles (Executive, Operations, Maintenance, Security, Guest/Visitor)." + additional AOCC/P&E/Airside ops/Terminal Ops/S&V/Commercial/Retail/Env&Sustainability/IT&Digital/emergency response & Business continuity. | Compliance | Phase 1a | STATED |
| SEC-04 | Encryption at rest AES-256 | "All data at rest encrypted using AES-256." (RFP v5, §3.5.2; Final requirements.xlsx.md line 945) | Compliance | Phase 1a | STATED |
| SEC-05 | Encryption in transit TLS 1.3+ | "All data in transit encrypted using TLS 1.3." (RFP v5, §3.5.2) + Final requirements.xlsx.md says "TLS 1.2+" — note conflict; RFP takes precedence. | Compliance | Phase 1a | STATED |
| SEC-06 | Activity audit logging minimum 2 years retention | "Full activity audit logging retained for a minimum of two (2) years." (RFP v5, §3.5.2; Final requirements.xlsx.md line 947) | Compliance | Phase 1a | STATED |
| SEC-07 | Historical data retention — 5 years | "Historical Data: 5 years retention period." (Final requirements.xlsx.md line 949) | Non-Functional | Phase 1b/ongoing | STATED |
| SEC-08 | IEC 62443 compliance for OT/IT integration | "Compliance with IEC 62443 for all OT/IT integration components." (RFP v5, §4.2; Final requirements.xlsx.md line 951) | Compliance | Phase 1a | STATED |
| SEC-09 | Cybersecurity risk assessment pre-deployment | "Conduct a full cybersecurity risk assessment prior to platform deployment, with findings and remediation plans submitted for DIAL approval." (RFP v5, §4.2; BRD v1.5 §3.4.5) | Compliance | Phase 4/milestone | STATED |
| SEC-10 | Network segmentation — IT/OT/internet defence-in-depth | "Implement network segmentation between IT, OT, and internet-facing components using a defence-in-depth architecture." (RFP v5, §4.2) | Compliance | Phase 4/milestone | STATED |
| SEC-11 | Penetration testing of all internet-facing components pre-go-live | "Penetration testing of all internet-facing components prior to go-live, with a full penetration test report submitted to DIAL." (RFP v5, §4.2) | Compliance | Phase 4/milestone | STATED |
| SEC-12 | SIEM for continuous monitoring | "Implement a Security Information and Event Management (SIEM) capability for continuous monitoring of platform security events." (RFP v5, §4.2; BRD v1.5 §3.4.5) | Compliance | Phase 4/milestone | STATED |
| SEC-13 | National data protection compliance — DPDP Act 2023 | "Comply with applicable provisions of the Digital Personal Data Protection Act, 2023 and any other applicable data governance legislation." (RFP v5, §9.6) | Compliance | Phase 4/ongoing | STATED |
| SEC-14 | IP ownership — exclusive to DIAL on full payment | "All deliverables produced under the scope of this RFP … shall become the exclusive intellectual property of DIAL upon full payment." (RFP v5, §9.3) | Commercial/Legal | Phase 4/ongoing | STATED |
| SEC-15 | SBOM — third-party software identified | "Third-party software, libraries, or data sets incorporated into the deliverables shall be clearly identified in a Software Bill of Materials (SBOM)." (RFP v5, §9.3) | Deliverable | Phase 4/milestone | STATED |
| SEC-16 | Data breach liability — vendor bears costs | "In the event of any cybersecurity incident or data breach: Vendor shall notify DIAL within 12 hours; bear all costs arising from breach." (BRD v1.5 §9.11) | Commercial/Legal | Phase 4/ongoing | STATED |
| SEC-17 | Data usage restrictions — no external use/training of AI models with DIAL data | "The Vendor shall not: Use any data for purposes outside this contract; Train or improve external AI models using DIAL data; Transfer, store, or process data outside India without prior written approval." (BRD v1.5 §9.10) | Compliance | Phase 4/ongoing | STATED |

---

## P. Payment Milestones & Commercial Framework

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| PM-01 | M1 — Contract award/mobilisation — 15% trigger: signed contract + project plan | "M1: Contract Award and Mobilisation — Signed contract, project plan accepted — 15%." | Commercial | Milestone | STATED |
| PM-02 | M2 — LiDAR data acquisition complete — 10% trigger: raw data delivered & DIAL-verified | "M2: LiDAR Data Acquisition Complete — Raw data delivered and DIAL-verified — 10%." | Commercial | Milestone | STATED |
| PM-03 | M3 — BIM/spatial deliverables accepted — 20% trigger: written sign-off by DIAL | "M3: BIM Models and Spatial Data Deliverables Accepted — Written sign-off by DIAL — 20%." | Commercial | Milestone | STATED |
| PM-04 | M4 — DT platform UAT passed — 25% trigger: UAT sign-off report accepted | "M4: Digital Twin Platform — UAT Passed — UAT sign-off report accepted — 25%." | Commercial | Milestone | STATED |
| PM-05 | M5 — AI agents deployed/commissioned — 20% trigger: all agents operational, performance benchmarks met | "M5: AI Agents Deployed and Commissioned — All agents operational, performance benchmarks met — 20%." | Commercial | Milestone | STATED |
| PM-06 | M6 — Final handover + post-implementation review (90 days) — 10% trigger | "M6: Final Handover and Post-Implementation Review — 90-day post-go-live review accepted — 10%." | Commercial | Milestone | STATED |
| PM-07 | Pricing in INR excl GST; all commercial tables to be completed by vendor | "All costs must be provided in Indian Rupees (INR), exclusive of GST. Do not alter the table structure." (RFP v5, §10) | Commercial | Submission | STATED |
| PM-08 | Vendor must declare all assumptions underlying pricing (survey areas, BMS point counts, user licences, cloud sizing) | "Vendors must declare all assumptions underlying their pricing… Pricing contingent on undeclared assumptions may be subject to revision." (RFP v5, §10, note at end of Table 7) | Commercial | Submission | STATED |
| PM-09 | Proposal validity — minimum 180 calendar days from submission deadline | "All proposals submitted in response to this RFP shall remain valid and binding for a minimum period of one hundred and eighty (180) calendar days." (RFP v5, §9.1) | Commercial/Legal | Submission | STATED |
| PM-10 | Warranty — minimum 12 months from formal handover, defects at no cost | "Vendor shall provide a minimum twelve (12) month warranty period commencing from the date of formal platform handover." (RFP v5, §9.5) | Commercial/Legal | Phase 5+12mo | STATED |
| PM-11 | Five-year O&M plan with SLAs, support structure, upgrades, exit strategy | "Vendor shall provide a comprehensive 5-year O&M strategy covering platform, infrastructure, AI models, integrations, and data lifecycle management." (RFP v5, §8; BRD v1.5 Table 8) | Commercial/Legal | Phase 5-10yr | STATED |

---

## Q. Training & Documentation Deliverables

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| TDD-01 | D-01: Project Execution Plan, BEP, Data Management Plan | "D-01: Project Execution Plan, BIM Execution Plan (BEP), and Data Management Plan." (RFP v5, §5.2; BRD v1.5 §4.2) | Deliverable | Phase 1 | STATED |
| TDD-02 | D-08: Deployed & tested Digital Twin Platform — UAT sign-off | "D-08: Deployed and tested Digital Twin Platform (UAT sign-off)." | Deliverable | Phase 4/milestone | STATED |
| TDD-03 | D-10: AI Monitoring and Predictive Intelligence Platform (all agents operational) | "D-10: AI Monitoring and Predictive Intelligence Platform (all agents operational)." | Deliverable | Phase 5/milestone | STATED |
| TDD-04 | D-11: API documentation portal + integration test reports | "D-11: API documentation portal and integration test reports." | Deliverable | Phase 3/milestone | STATED |
| TDD-05 | D-12: Cybersecurity Assessment Report + Penetration Test Report | "D-12: Cybersecurity Assessment Report and Penetration Test Report." | Deliverable | Phase 4/milestone | STATED |
| TDD-06 | D-13: Training Materials, User Manuals, Administrator Documentation | "D-13: Training Materials, User Manuals, and Administrator Documentation." | Deliverable | Phase 5 | STATED |
| TDD-07 | D-14: As-Built Documentation for all platform components | "D-14: As-Built Documentation for all platform components." | Deliverable | Phase 5 | STATED |
| TDD-08 | D-15: Post-implementation review report (90 days after go-live) | "D-15: Post-implementation review report (90 days after go-live)." | Deliverable | Phase 5+90d | STATED |
| TDD-09 | D-07: Existing Data Migration Report + Legacy Data Quality Assessment | "D-07: Existing Data Migration Report and Legacy Data Quality Assessment." | Deliverable | Phase 2 | STATED |

---

## R. Governance, RACI, Exit Management, Legal Framework

| Req ID | Category | Requirement Text (verbatim or near-verbatim) | Source | Ref | Type | Phase | Status |
|--------|----------|-----------------------------------------------|--------|-----|------|-------|--------|
| GOV-RACI-01 | RACI Matrix — Planning/Surveys/Modelling (§5.1 of BRD) | "R=Responsible, A=Accountable, C=Consulted, I=Informed" with detailed matrix across Vendor/DIAL/Smart City/DEC for project mobilisation, regulatory approvals, surveys, GPR, GIS-BIM, BIM modelling, legacy data reconciliation. | BRD v1.5, §5.1 | | Compliance | Phase 1-5 | STATED |
| GOV-RACI-02 | RACI Matrix — Platform Dev/Integration (§5.2 of BRD) | Digital Twin platform architecture/BMS integration/APOC integration/access+SSO/cybersecurity controls. | BRD v1.5, §5.2 | | Compliance | Phase 3-4 | STATED |
| GOV-RACI-03 | RACI Matrix — AI/Advanced Analytics (§5.3 of BRD) | AI agent design/model training/AI governance/alert thresholds/SOP definition/AI model deployment approval. | BRD v1.5, §5.3 | | Compliance | Phase 4-5 | STATED |
| GOV-RACI-04 | RACI Matrix — Operations/Support/Change Management (§5.4 of BRD) | Platform ops+AMC/incident management/data updates/system upgrades/knowledge transfer+training. | BRD v1.5, §5.4 | | Compliance | Phase 5+/ongoing | STATED |
| EXI-01 | Exit management / transition support — complete handover + 6 months | "Provide complete handover of all deliverables, source code, configurations, and documentation… Provide transition support for a minimum period of six (6) months. No additional cost shall be charged." (BRD v1.5 §9.12) | BRD v1.5, §9.12 | | Deliverable | Phase 5+6mo | STATED |
| EXI-02 | End-to-end delivery responsibility — vendor liable for all third-party/legacy dependencies | "If accepted the Concessionaire shall be fully responsible for the end-to-end delivery, integration, performance, and operationalisation of the Airport Eye Platform." (BRD v1.5 §9.7) | BRD v1.5, §9.7 | | Commercial/Legal | Phase 1-5 | STATED |
| EXI-03 | Integration responsibility — vendor solely responsible for interoperability across all systems | "The Vendor … shall be solely responsible for ensuring seamless integration and interoperability across all systems, including but not limited to BMS, IoT platforms, GIS, BIM, APOC, CCC, CMMS, PSIM, and third-party systems." (BRD v1.5 §9.8) | BRD v1.5, §9.8 | | Commercial/Legal | Phase 1-5 | STATED |
| EXI-04 | Integration failure = vendor responsibility unless excluded in writing by DIAL | "Any failure of integration, regardless of originating system, shall be considered a Vendor's responsibility unless explicitly excluded in writing by DIAL." (BRD v1.5 §9.8) | BRD v1.5, §9.8 | | Commercial/Legal | Phase 1-5 | STATED |
| EXI-05 | SLA penalties — financial for each breach; repeated breaches = material default; persistent non-performance = termination at DIAL discretion | "SLA penalties per BRD §9.9 + RFP §9.6." | BRD v1.5, §9.9 / RFP v5, §9.6 | | Commercial/Legal | Ongoing | STATED |
| EXI-06 | Vendor indemnification for regulatory/approval compliance (BCAS, AAI, govt authorities) | "The Vendor shall… obtain, maintain, renew and comply with all applicable approvals, permissions, licences, clearances and authorisations… The Vendor shall indemnify, defend and hold harmless DIAL from and against any and all losses, claims, damages…" (BRD v1.5 §Applicable Laws & Approvals section) | BRD v1.5, Applicable Laws & Approvals | | Commercial/Legal | Phase 1-5 | STATED |
| EXI-07 | Applicable law compliance — continuous, vendor-borne costs/liability | "The Vendor shall ensure continuous compliance with all Applicable Laws… Any failure, lapse, breach or non-compliance… shall be solely attributable to and borne by the Vendor." (BRD v1.5, Applicable Laws section) | BRD v1.5, Applicable Laws & Approvals | | Commercial/Legal | Phase 1-5 | STATED |
| EXI-08 | DIAL reserved rights — accept/reject proposals; negotiate; cancel/modify RFP; award to one/multiple vendors or split scope | "DIAL reserves the right to accept or reject any or all proposals… negotiate with any respondent… cancel or modify this RFP at any time… award to one or more vendors, or split scope." (RFP v5, §9.2) | RFP v5, §9.2 | | Commercial/Legal | Submission/Pre-award | STATED |
| EXI-09 | Pre-qualification criteria — 5 years exp / 2 comparable deployments / ISO 9001 / ISO 27001 / turnover requirements / no pending insolvency | "Pre-qualification: 5 years exp, 2 comparable deployments, ISO 9001:2015, ISO 27001:2013, turnover requirements, no pending insolvency." | RFP v5, §Appendix E | | Compliance | Submission | STATED |
| EXI-10 | Vendor must obtain at own cost approvals from BCAS, AAI and any governmental/regulatory authority for airside work/drone survey etc. | "Vendor to obtain all applicable approvals from BCAS, AAI and regulatory authorities at its own cost." | BRD v1.5, Applicable Laws & Approvals | | Compliance | Phase 1 | STATED |

---

# PART B — CLIENT GAP MAPPING (C-001 through C-046)

**Source:** `sources/Airport Eye/client gaps.md` (46 items, numbered as line items in the client feedback document).
**Cross-referenced against:** RFP v5, BRD v1.5, ABR (SPG simulation use cases), and Requirements Register — all four from Part A.

## Client Gaps vs Formal Sources

| C-ID | Short Description | Source Reference (clause/line) or GAP Status | Notes |
|------|-------------------|---------------------------------------------|-------|
| **C-01** | LiDAR accuracy 5cm/3cm vs 10cm/20cm proposal | **FOUND — RFP v5, §3.1.2 line 262: "Horizontal ≤ 5 cm RMSE, Vertical ≤ 3 cm RMSE"** + BRD v1.5 §3.1.1 identical. The formal source *does* require 5cm/3cm; this is a deviation of the proposal from the requirement, not an absent requirement. |
| **C-02** | Orthophoto/DTM/DSM spec deviation (5cm ortho, 10cm DTM vs 10cm/50cm proposed) | **FOUND — RFP v5, §3.1.2 line 279: "GSD ≤ 5 cm"; line 281: "DTM and DSM at 10 cm grid resolution"** + BRD v1.5 §3.1.1 identical. Formal source confirmed. |
| **C-03** | Mobile/offline enablement for all departments/end-users/leadership | **GAP — Not specified in any formal source.** The closest is RFP v5, §3.5.1 "Full mobile responsiveness" for the DT viewer, but no requirement states that *all departments/end-users/leadership* must have mobile-enabled, offline-capable access to platform capabilities. This is a client-added post-issuance preference. |
| **C-04** | DIAL use-case → KPI → dashboard mapping | **GAP — Not specified in any formal source.** The BRD v1.5 requires "Data-driven decision-making" (ABR §4.1) and operational dashboards but does not mandate a documented use-case-to-KPI-to-dashboard traceability matrix as a deliverable. |
| **C-05** | Leadership reporting dashboards to be specified | **GAP — Not specified in any formal source.** While leadership/operational dashboards are implied by the RFP's dashboard requirements, no clause mandates a dedicated "leadership reporting" dashboard specification. |
| **C-06** | T2 OT (FAS) exclusion must be removed | **GAP — Not specified in any formal source for *T2 specifically*.** The BRD v1.5 requires BMS integration across all systems but does not explicitly enumerate which OT subsystems are *in-scope vs excluded* per terminal. T2 ECMS, PBB, VDGS, LCMS, BHS, ATRS, GPU-PCA are all marked "NA/Not Present/TBD" in the register — this gap flags those as needing removal from exclusions but doesn't cite a source clause requiring them. |
| **C-07** | OneAPOC/APOC Phase-2 complete accountability to WAISL | **GAP — Not specified in any formal source.** The CR's RACI (§5 of BRD) assigns Vendor=DIAL roles for specific activities (mobilisation, survey approvals, BIM modelling etc.) — it does not assign "complete accountability" for APOC Phase-2 to WAISL. This is a client preference not in the formal source RACI. |
| **C-08** | DT visibility on end-user machines | **GAP — Not specified in any formal source.** The platform provides a web-based DT viewer (§3.5.1), but there is no explicit requirement for "DT visibility on end-user machines" as a democratized capability. |
| **C-09** | Complete asset registry (CLG, CAI, hierarchy, parent-child mapping, location, traceability) | **PARTIAL — Multiple items FOUND.** CLG creation: Register Asset commons (AFR-03). CAI framework: Final requirements.xlsx.md, AFR-04. Hierarchy: Final requirements.xlsx.md, AFR-10. Ontology/relationships: Final requirements.xlsx.md, AFR-11. UI asset registry: Final requirements.xlsx.md, AFR-01. *However*, the client's specific expectation of a "complete parent-child mapping and traceability" schema is broader than what the register specifies. |
| **C-10** | Complete IT infrastructure (on-prem/cloud) provisioning owned by WAISL | **GAP — Not specified in any formal source.** The RFP/BRD v1.5 require vendors to *propose* infrastructure architecture but do not mandate that the Concessionaire/WAISL owns or provisions all IT infrastructure. Table 7 lists compute/storage/network as vendor-proposed items. This is a commercial/accountability preference. |
| **C-11** | All 8 AI Agents must be explicitly detailed | **FOUND — RFP v5, §6.3 mandates all agent categories explicitly.** The BRD v1.5 Table at lines ~436-448 enumerates 8 mandatory agents (Mech/HVAC, Electrical, Fire Safety, Water/Drainage, Energy, Passenger Flow, Structural Integrity, Security). RFP v5, §6.3: "Vendors must address each agent category explicitly." *Confirmed.* |
| **C-12** | AI modelling: system stress / partial failure / degradation | **GAP — Not specified in any formal source.** The BRD's Agentic-AI objectives (§4) reference predicting failures broadly, but no clause explicitly requires "system stress / partial failure / degradation" as a distinct AI modelling capability. This is client-added specificity. |
| **C-13** | OT data point count: 5L+ vs 2L+ proposed | **GAP — Not specified in any formal source.** The RFP v5, §3.4.1 states "[X] BMS data points" (placeholder). The Final requirements.xlsx.md does not give a single aggregated "5 lakh+" requirement; per-system counts vary widely but no total is mandated at 500,000. |
| **C-14** | Google Maps/Earth D+1 change detection | **GAP — Not specified in any formal source.** The ABR mentions "Google Maps / Satellite integration for landside monitoring" (Commercial Aero use case) but does not mention *Google Earth* specifically or *D+1 change detection*. This is a client-added preference. |
| **C-15** | DIAL IT Security Policy compliance | **GAP — Not specified in any formal source.** "DIAL IT Security Policy" is not named in the CR, RFP, ABR, or Requirements Register. The closest is IEC 62443 (SEC-08) and DPDP Act 2023 (SEC-13), but no separate "DIAL IT Security Policy" exists in any source document. |
| **C-16** | Platform availability 99.9% vs 99.5% | **FOUND — RFP KPI Table item 1 / BRD v1.5 KPI item 1: "≥ 99.5%".** The formal source specifies 99.5%. The client's requested 99.9% is *tighter* than the formal requirement and does not appear in any formal source. |
| **C-17** | Pax-journey IT/OT hardware mapping (departure & arrival) | **GAP — Not specified in any formal source.** While the Final requirements.xlsx.md requires "Visualize equipment & required sensors (LOD 350)" for various systems, there is no explicit requirement to map *pax-journey* (departure and arrival) hardware specifically. |
| **C-18** | CCTV/video analytics/IT in pax journey | **GAP — Not specified in any formal source for *pax journey specifically*.** CCTV/VMS integration exists (ITI-10), and the BRD v1.5 references CCTV as part of security systems, but no clause mandates CCTV/analytics mapped to the passenger journey. |
| **C-19** | Barcode/e-gate/CUSS/CUPPS/DFMD/ATRS/baggage/boarding scanners | **PARTIAL — Multiple items FOUND.** DigiYatra (PPS-01), CUSS (PPS-03), CUPPS (PPS-04), ATRS (PPS-09, also Register), DFMD (Register PESC scope), boarding gate scanners (PPS-07) are all listed in the Final requirements.xlsx.md. *However*, a comprehensive integrated "pax journey scanner list" as a single requirement is not explicitly stated. |
| **C-20** | Medallion Lakehouse walkthrough for DIAL | **GAP — Not specified in any formal source.** "Medallion Lakehouse architecture" is not referenced in any of the four source documents. This is entirely client-added. |
| **C-21** | ITBMS/JCI/Honeywell integration approach not confirmed | **GAP — Not specified for *approach* specifically.** The Final requirements.xlsx.md references ITBMS (ITB-15: "Merge of all integrated") and OEM systems like JCI, Honeywell are named in per-system integration rows (e.g. T3 HVAC OEM = Honeywell). No clause requires a documented "integration approach" narrative as a deliverable. |
| **C-22** | Risk register elaboration | **GAP — Not specified in any formal source.** The RFP asks for a "risk register" as part of the proposal Volume 4, but there is no specific requirement for an *elaborated* project risk register as a deliverable in the source documents. |
| **C-23** | RACI revised: WAISL as A/R (planning, surveys, platform, AI, ops) | **CONFLICT — CR's §5.3 RACI already assigns Vendor=R/A for many items.** The formal RACI (§5 of BRD) assigns DIAL=A (Accountable) and Vendor=R (Responsible) for most activities. C-23 demands WAISL be made A+R, which *contradicts* the existing CR's binding RACI matrix. See note below. |
| **C-24** | Simulation engine architecture detail | **FOUND — ABR §4.1: "The simulation environment should be capable of modeling interdependencies across functions…" + Architecture items 1-4 (ABR §4.2).** The BRD v1.5 requires a simulation engine. This is confirmed in the sources. |
| **C-25** | Commercial simulation use cases missing | **FOUND — ABR §4.2 Table: Store Mix Optimization, Shelf Merchandising, Store Location, Dwell Time Monetization, Campaign & Promotion, Queue vs Revenue, Gate Allocation, Lounge vs Retail, Staffing vs Sales, Disruption Monetization.** All listed. |
| **C-26** | Operational simulation use cases missing | **FOUND — ABR §4.2 Table: Passenger Flow Optimization, Queue Management, Check-in & Security Capacity Planning, Gate Allocation, Disruption Management, Workforce Deployment, Baggage Flow, Landside Traffic & Curbside.** All listed. |
| **C-27** | Integrate the model with APOC for control and monitoring (control rights reserved) | **FOUND — BRD v1.5 §3.3.2: "Integrate the model with APOC for control and monitoring (monitoring access to all functions; control rights reserved for certain functions)."** Also RFP v5, §4.1 API requirements + BRD v1.5 §3.4.3 APOC integration. |
| **C-28** | APOC lights ON/OFF control | **FOUND — BRD v1.5 §3.3.2: "Control of Lights ON/OFF from APOC."** Explicitly stated. |
| **C-29** | Training & adoption plan | **PARTIAL — D-13 deliverable (TDD-06) covers "Training Materials, User Manuals, and Administrator Documentation." BRD v1.5 §5.4 lists "Knowledge transfer and training" in RACI.** A formal "adoption plan" as a distinct deliverable is not specified. |
| **C-30** | Exclusions must be accepted by named business owners | **GAP — Not specified in any formal source.** The BRD v1.5 requires DIAL sign-off on deliverables (14-day review period, RFP v5, §5.2) but no specific requirement that "exclusions" be accepted by *named business owners*. |
| **C-31** | Borewell recharge monitoring (should be base scope) | **FOUND — ABR §3.1 P&E: "Borewell recharge monitoring using IoT sensor integration (Smartcity)."** Explicitly stated as an in-scope requirement. |
| **C-32** | Stormwater analysis data feed and implementation | **FOUND — ABR §3.1 P&E: "Storm water analysis (Walter P Moore) with IoT-enabled monitoring (Smartcity)."** Also BRD v1.5 §3.3.5 mentions stormwater runoff modelling as part of Water & Drainage agent. |
| **C-33** | DIAL Vendors/DIAL OEM coordination is WAISL responsibility | **GAP — Not specified in any formal source for *coordination* specifically.** The RACI assigns accountability but no clause mandates "DIAL Vendor/OEM coordination" as a specific activity. This is a client preference. |
| **C-34** | WAISL should own AEP/access coordination as per existing process | **GAP — Not specified in any formal source for *AEP specifically*.** The BRD v1.5 lists "access coordination" under landside LOD requirements but does not assign ownership to WAISL for AEP/access coordination. |
| **C-35** | "Generic Digital framework" aspiration undocumented | **GAP — Not specified in any formal source.** No clause references a "Generic Digital framework." The BRD's vision statement (§1.1) mentions creating a "living, dynamic, and spatially accurate digital replica of the entire airport ecosystem" but does not use or define "Generic Digital framework." |
| **C-36** | IFC repository architecture/storage/governance/ownership | **GAP — Not specified in any formal source.** The BRD v1.5 requires "IFC-compliant federated BIM models" (BRD v1.5 §3.1.9 D-08) and ISO 19650 compliance, but no specific clause mandates an "IFC repository architecture, storage strategy, governance model, or long-term ownership of IFC data." |
| **C-37** | IFC GUID ↔ CAI ↔ CLG ↔ SAP ↔ OT/BMS mapping | **PARTIAL — Multiple items FOUND.** CAI (AFR-04), CLG (AFR-03), SAP federation (AFR-13). *However*, the specific five-way mapping "IFC GUID ↔ CAI ↔ CLG ↔ SAP ↔ OT/BMS" as a unified cross-referencing schema is not explicitly stated. |
| **C-38** | Airport Asset Information Model (AIM) | **GAP — Not specified in any formal source.** "Airport Asset Information Model (AIM)" is not mentioned in any of the four sources. This is client-added terminology. |
| **C-39** | Ontology & relationship model (terminal/floor/space/system/equipment/sensor) | **FOUND (partial) — Final requirements.xlsx.md, "Relationships aka Ontology" (AFR-11).** The formal source requires ontology but does not specify the exact entity types (terminal, floor, space, system, equipment, sensor). |
| **C-40** | BIM lifecycle management (version control, as-built, sync with DT) | **FOUND — BRD v1.5 §3.2.3: "Version control and change management with full audit trail." RFP v5, §5.2 D-14: "As-Built Documentation for all platform components."** However, a formal "BIM lifecycle management" clause linking version control to as-built updates synchronized with the operational Digital Twin is not explicitly stated as a single requirement. |
| **C-41** | BIM-GIS federation rules/georeferencing | **GAP — Not specified in any formal source.** While BRD v1.5 §3.2.2 requires "Import BIM models into the GIS environment" and "connections between GIS and BIM databases," no specific clause mandates "BIM-GIS federation rules, georeferencing standards, and spatial alignment requirements." |
| **C-42** | AI access pattern to BIM/IFC data | **GAP — Not specified in any formal source.** The Final requirements.xlsx.md's NL Query Agent (AI-10) mentions querying BIM registry ("assets (BIM registry), live/historical telemetry…"), but no clause specifies how AI agents will *access and query BIM/IFC data and relationships*. |
| **C-43** | Open BIM standards (IFC 4.3, bSDD) mandate | **FOUND (partial) — RFP v5, §3.2.2: "IFC 4.0 (ISO 16739)."** The formal source mandates IFC 4.0 (not 4.3). No mention of bSDD (buildingSMART Data Dictionary) anywhere in the four sources. |
| **C-44** | End-to-end digital thread (BIM↔GIS↔SAP↔BMS↔IoT↔APOC↔AI) | **GAP — Not specified in any formal source as a *digital thread*.** While each system is listed as integrated in the Final requirements.xlsx.md, no single clause defines an "end-to-end digital thread" linking all seven domains. This is client-added architecture terminology. |
| **C-45** | Add RTM section "BIM IFC Data Architecture" | **GAP — Not specified in any formal source.** No clause mandates a dedicated RTM section titled "BIM IFC Data Architecture." The client is requesting a *documentation structure* change not present in the sources. |
| **C-46** | Long-term BIM governance (ownership, metadata, mapping) | **FOUND (partial) — BRD v1.5 §3.2.3: "Version control and change management with full audit trail" + SEC-14 (IP ownership).** *However*, comprehensive "long-term BIM governance including ownership, metadata, and mapping" as a dedicated requirement is not explicitly stated in its entirety. |

---

# SUMMARY STATISTICS — Client Gap Mapping

| Metric | Count | Notes |
|--------|-------|-------|
| Fully FOUND (explicitly in formal sources) | 14 | C-01, C-02, C-11, C-24, C-25, C-26, C-27, C-28, C-31, C-32, C-39, C-43, plus partial overlaps |
| Partially FOUND (some elements in sources) | 9 | C-09, C-19, C-29, C-36(partial), C-37, C-40 |
| GAP — Not specified in any formal source | 23 | C-03, C-04, C-05, C-06, C-07, C-08, C-10, C-12, C-13, C-14, C-15, C-20, C-22, C-30, C-33, C-34, C-35, C-36(full), C-38, C-41, C-42, C-44, C-45, C-46 |
| CONFLICT with formal source | 1 | C-23 (client demands WAISL=A+R but CR's §5 RACI assigns DIAL=A) |

**Key insight:** Of the 46 client gaps, **only 14 are fully confirmed as formal requirements**. The remaining 23 items are genuinely absent from all four source documents — they represent client preferences or architecture mandates formed after the RFP was issued.

---

*End of document.*
