# 07 — Integration, Data, and Technical Approach

## Integration philosophy

BAC requires "seamless integration across BAC operational, enterprise and data systems" (RFP §3.3). UTAM's integration layer is built on an API Gateway (REST/SOAP), event streaming, and a connector framework, with the Edge Data Ingestor performing protocol adaptation (REST, SOAP, file-based, streaming, OPC-UA) and schema normalisation. [GROUNDED: UTAM External Interfacing table; UTAM Edge Data Ingestor]

## Connectors

UTAM lists connectors for AODB, ADS-B, telematics, vision analytics, weather, and RVR (NF16). [GROUNDED: UTAM Integration Layer; UTAM connectors table — coverage-matrix NF15/NF16]

For BAC we will add:

- **AIDX connector** (FR15, FR43, FR54) — published and consumed via the API Gateway. [ASSERTION: AIDX publication/consumption via API Gateway — coverage-matrix FR15/FR43/FR54]
- **FIDS connector** (FR54) — via the same connector framework. [ASSERTION: UTAM A-CDM; FIDS not named, to be added — coverage-matrix FR54]
- **A-CDM milestone synchronisation** — UTAM's NM Message Service handles A-CDM milestones (TOBT, TSAT, A-CDM milestones) and is adaptable to BNE's A-CDM context. [ASSERTION: UTAM NM Message Service is Eurocontrol-NM-oriented; adaptable to BNE A-CDM — UTAM NM Message Service]

## Data architecture

The Lakehouse uses a medallion architecture (Bronze raw, Silver curated, Gold business-ready) with schema evolution, time travel, and high-performance query. [GROUNDED: UTAM Lakehouse] An Operational Database holds current state for real-time dashboards. [GROUNDED: UTAM Operational Database] A Data Catalogue & Governance layer provides metadata, lineage, schema registry, and quality enforcement. [GROUNDED: UTAM Data Catalogue & Governance]

Data quality is first-class: every ingested record carries a quality score; low-quality records are flagged, quarantined, and logged; every derived KPI carries full provenance; all access/modification/deletion events are logged to an immutable audit trail. [GROUNDED: UTAM Data Quality, Lineage, and Audit Trail]

## Data flow and event metadata separation

Event metadata is stored as structured data in the Lakehouse, separate from video — satisfying FR57 in principle. [ASSERTION: UTAM lakehouse separates structured metadata; video stored separately — coverage-matrix FR57] Configurable retention policies (FR58) are grounded. [GROUNDED: UTAM retention policies — coverage-matrix FR58] Automated retention enforcement with configurable periods per data category is available. [GROUNDED: UTAM Additional assurances — retention policies]

## APIs and event publishing

The API Gateway is the central control point for all external APIs — routing, authentication, rate limiting, security — enabling secure exposure of platform services. [GROUNDED: UTAM API Gateway — coverage-matrix FR55] Actual timestamps can be published to consuming systems via the API Gateway and event streaming (FR56). [ASSERTION: API Gateway supports publish — coverage-matrix FR56]

## Master data management

Shared entity definitions (flights, stands, gates, resources) are managed centrally and resolved across all source systems — eliminating the entity-conflict problem that plagues multi-system airport analytics. [GROUNDED: UTAM Data Quality, Lineage, and Audit Trail — master data management] This directly supports BAC's "single source of truth" objective.

## Self-service BI and reporting

Self-Service BI enables authorised stakeholders to build custom reports, dashboards, and data explorations without IT dependency, querying curated Gold-layer datasets through controlled templates (no raw SQL for business roles), with timeouts, rate limits, and full audit logging. [GROUNDED: UTAM Self-Service BI & Reporting — coverage-matrix NF25, FR52] Export controls are governed by role-based permissions with audit logging (NF02). [GROUNDED: UTAM export controls — coverage-matrix NF02]

## Parameterisation and rules

The Business Rules Engine provides a low-code environment for configurable alerts, automated workflows, and event-driven actions — version-controlled with approval workflow and rollback. [GROUNDED: UTAM Rules Engine] This grounds FR40 (turnaround SLA alerts) and FR41 (unsafe/prohibited activity alerts) and supports FR42 (AI-confidence-degradation alerts via rules). [GROUNDED: Turnwise Alerts; UTAM Rules Engine — coverage-matrix FR40/FR41] [ASSERTION: UTAM Rules Engine could raise AI-confidence-degradation alerts — coverage-matrix FR42]

## Deployment models

The platform is deployment-agnostic: AWS cloud (multi-AZ) or BAC private cloud, with identical functional, security, and performance commitments. [GROUNDED: UTAM Deployment Architecture note] For BAC we commit to Australian hosting (see Section 08).

## DevOps and CI/CD

Fully automated commit-to-production pipeline with policy gates for security, performance, and compliance; Infrastructure as Code (Terraform + GitOps) with drift detection; environment parity (DEV/TST/PROD from the same IaC templates); automated testing pyramid. [GROUNDED: UTAM DevOps & CI/CD Framework]

> Security, ISRA, and compliance are covered in Section 08.