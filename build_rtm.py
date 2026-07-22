#!/usr/bin/env python3
"""Build a single Requirements Traceability Matrix from:
- Final requirements.xlsx.md (register)
- AddendumA_Use_Case_Coverage_Matrix.md (use cases)
- Airport_Eye_Consolidated_Proposal_FINAL.txt (packages / milestones)

Output: /Users/sujoymukherjee/code/doc2md/parse2wiki/requirements-traceability-matrix.md
"""
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/sujoymukherjee/code/doc2md/parse2wiki")
REGISTER_FILE = ROOT / "sources/Airport Eye/Final requirements.xlsx.md"
ADDENDUM_FILE = ROOT / "sources/Airport Eye/_analysis/proposal_v11/AddendumA_Use_Case_Coverage_Matrix.md"
PROPOSAL_FILE = ROOT / "sources/Airport Eye/_analysis/proposal_v12/Airport_Eye_Consolidated_Proposal_FINAL.txt"
OUT_FILE = ROOT / "requirements-traceability-matrix.md"

# -----------------------------------------------------------------------------
# 1. Static Addendum A use-case catalogue (extracted from AddendumA file)
# -----------------------------------------------------------------------------
ADDENDUM_CASES = [
    # P&E
    {"id": "ABR-3.1-01", "name": "Borewell recharge monitoring with IoT", "owner": "IoT Gateway + Geo Digital Twin", "status": "Future (Phase 2)"},
    {"id": "ABR-3.1-02", "name": "Stormwater analysis with IoT monitoring", "owner": "Geo Digital Twin - Flood Simulation + IoT Gateway", "status": "Delivered (data feed TBC)"},
    # S&V
    {"id": "ABR-3.2-01", "name": "Reverse-entry detection in restricted zones", "owner": "Security & Perimeter agent + ACS/CCTV", "status": "Delivered"},
    {"id": "ABR-3.2-02", "name": "Unattended-baggage detection", "owner": "Security & Perimeter agent", "status": "Delivered"},
    {"id": "ABR-3.2-03", "name": "Behaviour analytics for threat detection", "owner": "Security & Perimeter agent", "status": "Delivered"},
    {"id": "ABR-3.2-04", "name": "Predictive security monitoring", "owner": "Security & Perimeter agent", "status": "Delivered"},
    {"id": "ABR-3.2-05", "name": "Security asset mapping", "owner": "Geo Digital Twin - 3D Space Management", "status": "Delivered"},
    # Commercial Aero
    {"id": "ABR-3.3-01", "name": "Google Maps / satellite integration (landside)", "owner": "Geo Digital Twin - external basemap layer", "status": "Future (Phase 2)"},
    {"id": "ABR-3.3-02", "name": "Identification of space-allocation changes", "owner": "Geo Digital Twin - 3D Space Management + change-detection", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-3.3-03", "name": "GIS-based analytics for planning and utilisation", "owner": "Geo Digital Twin - Space Management Application", "status": "Delivered"},
    # Operations
    {"id": "ABR-3.4-01", "name": "Surface navigation in low-visibility (fog)", "owner": "Geo Digital Twin + RVR/METAR feeds", "status": "Future (Phase 2)"},
    {"id": "ABR-3.4-02", "name": "What-if scenario analytics", "owner": "Simulation & What-If engine", "status": "Delivered"},
    {"id": "ABR-3.4-03", "name": "Monitoring / alerting of all IT systems", "owner": "AIOP backbone + Passenger Flow agent + OI layer", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-3.4-04", "name": "Live operations monitoring dashboard", "owner": "Operational Digital Twin - 50+ airside KPIs", "status": "Delivered"},
    {"id": "ABR-3.4-05", "name": "Identification of overstaying / unidentified passengers", "owner": "Passenger Flow agent + Reverse PaxFlow", "status": "Delivered"},
    # SPG §4.1
    {"id": "ABR-4.1-01", "name": "IROPS Simulation", "owner": "Simulation engine + IROPs/DDE feed", "status": "Delivered"},
    {"id": "ABR-4.1-02", "name": "Evacuation & Fire Scenarios", "owner": "Fire Safety & Life Safety agent + Simulation engine", "status": "Delivered"},
    {"id": "ABR-4.1-03", "name": "Breach Detection", "owner": "Security & Perimeter agent + PIDS", "status": "Delivered"},
    {"id": "ABR-4.1-04", "name": "Retail Optimisation (footfall, dwell)", "owner": "Simulation engine + Passenger Flow agent + retail sensors", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.1-05", "name": "Simulation architecture (4 components)", "owner": "Simulation & What-If engine", "status": "Delivered"},
    # SPG §4.2 Commercial
    {"id": "ABR-4.2-C-01", "name": "Store Mix Optimisation", "owner": "Simulation engine", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-C-02", "name": "Shelf Merchandising Optimisation", "owner": "Simulation engine", "status": "Future (Phase 2)"},
    {"id": "ABR-4.2-C-03", "name": "Store Location Optimisation", "owner": "Simulation engine + 3D Space Management", "status": "Delivered"},
    {"id": "ABR-4.2-C-04", "name": "Dwell Time Monetisation", "owner": "Simulation engine + Passenger Flow agent", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-C-05", "name": "Campaign & Promotion Simulation", "owner": "Simulation engine", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-C-06", "name": "Queue vs Revenue Trade-off", "owner": "Simulation engine + Passenger Flow + POS", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-C-07", "name": "Gate Allocation Optimisation", "owner": "Simulation engine + AODB/RMS", "status": "Delivered"},
    {"id": "ABR-4.2-C-08", "name": "Lounge vs Retail Trade-off", "owner": "Simulation engine", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-C-09", "name": "Staffing vs Sales Optimisation", "owner": "Simulation engine + WFM + POS", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-C-10", "name": "Disruption Monetisation Strategy", "owner": "Simulation engine + IROPs/DDE", "status": "Delivered"},
    # SPG §4.2 Operational
    {"id": "ABR-4.2-O-01", "name": "Passenger Flow Optimisation", "owner": "Passenger Flow agent + Simulation engine", "status": "Delivered"},
    {"id": "ABR-4.2-O-02", "name": "Queue Management Optimisation", "owner": "Passenger Flow agent + XOVIS/Kloudspot + Simulation", "status": "Delivered"},
    {"id": "ABR-4.2-O-03", "name": "Check-in & Security Capacity Planning", "owner": "Simulation engine + CUPPS/CUSS/E-Gates", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-O-04", "name": "Gate Allocation & Utilisation", "owner": "Simulation engine + AODB/RMS", "status": "Delivered"},
    {"id": "ABR-4.2-O-05", "name": "Disruption Management Simulation", "owner": "Simulation engine + IROPs/DDE", "status": "Delivered"},
    {"id": "ABR-4.2-O-06", "name": "Workforce Deployment Optimisation", "owner": "Simulation engine + WFM", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-O-07", "name": "Baggage Flow Optimisation", "owner": "Simulation engine + BHS/BRS", "status": "Delivered"},
    {"id": "ABR-4.2-O-08", "name": "Landside Traffic & Curbside Management", "owner": "Simulation engine + landside traffic feed", "status": "Future (Phase 2)"},
    # SPG §4.2 Engineering
    {"id": "ABR-4.2-E-01", "name": "Thermal Load Simulation", "owner": "Simulation engine + Mechanical & HVAC agent + BMS", "status": "Delivered"},
    {"id": "ABR-4.2-E-02", "name": "Passenger Load vs HVAC Demand", "owner": "Simulation engine + Passenger Flow + Mechanical & HVAC", "status": "Delivered"},
    {"id": "ABR-4.2-E-03", "name": "Retail Expansion Energy Impact", "owner": "Simulation engine + Energy agent", "status": "Delivered (data feed TBC)"},
    {"id": "ABR-4.2-E-04", "name": "Zone-Based Cooling Optimisation", "owner": "Simulation engine + Mechanical & HVAC agent", "status": "Delivered"},
    {"id": "ABR-4.2-E-05", "name": "Power Infrastructure Stress Testing", "owner": "Simulation engine + Electrical agent + ECMS", "status": "Delivered"},
    # CIO Review Passenger-journey IT
    {"id": "CIO-10-01", "name": "Availability monitoring of passenger-journey IT assets", "owner": "Passenger Flow agent + OI layer + AIOP backbone", "status": "Delivered (data feed TBC)"},
    {"id": "CIO-10-02", "name": "Downtime reporting", "owner": "Passenger Flow agent + OI layer", "status": "Delivered (data feed TBC)"},
    {"id": "CIO-10-03", "name": "Real-time alerts on passenger-journey IT assets", "owner": "Passenger Flow agent + Alerts & Rules Engine", "status": "Delivered (data feed TBC)"},
    {"id": "CIO-10-04", "name": "Impact analysis (IT asset outage → passenger journey)", "owner": "OI layer + Passenger Flow + Simulation engine", "status": "Delivered (data feed TBC)"},
    {"id": "CIO-10-05", "name": "Root-cause correlation across IT/OT assets", "owner": "OI layer + cross-agent correlation", "status": "Delivered (data feed TBC)"},
    {"id": "CIO-10-06", "name": "What-if scenario modelling (IT asset scenarios)", "owner": "Simulation engine + Passenger Flow", "status": "Delivered (data feed TBC)"},
    # CIO Review APOC
    {"id": "CIO-11-01", "name": "APOC integration — situational awareness & operational intelligence surface", "owner": "OI layer + APOC/OneAPOC integration", "status": "Delivered (data feed TBC)"},
    {"id": "CIO-11-02", "name": "APOC Phase-2 integration", "owner": "OI layer + APOC Phase-2 interface", "status": "Delivered (data feed TBC)"},
]

CASE_BY_NAME = {c["name"]: c for c in ADDENDUM_CASES}

# -----------------------------------------------------------------------------
# Helpers for context-aware mapping
# -----------------------------------------------------------------------------
RE_ID_PREFIX = re.compile(r"^([A-Z]+(?:-[A-Za-z0-9]+)+)-\d+")


def looks_like_req_id(value: str) -> bool:
    """Return True if the component value looks like a requirement ID rather than a real component name."""
    if not value:
        return False
    return bool(re.match(r"^(BIMM|INTF|FR-DTW|ROW|AI|ODT)-[A-Z0-9\-]+$", value.strip()))


def looks_like_section_label(value: str) -> bool:
    """Return True if the component value is actually a section header, not a real component name."""
    if not value:
        return False
    v = value.strip().upper()
    section_markers = [
        "REQUIREMENTS", "WIDGETS", "USECASES", "SIMULATION", "AI AGENTS",
        "NON-FUNCTIONAL", "PLATFORM", "COMMON FUNCTIONALITY", "TESTING",
        "DEPLOYMENTS", "OUT OF SCOPE", "REGISTRY", "FEDERATION", "COMMONS",
        "MODELING", "INTEGRATIONS", "VISUALIZATION", "CAPABILITIES",
    ]
    return any(m in v for m in section_markers)


def family_prefix(req_id: str) -> str:
    """Extract a family prefix for component inheritance (e.g. FR-DTW-AOPS-04 -> FR-DTW-AOPS)."""
    m = RE_ID_PREFIX.match(req_id.strip())
    return m.group(1) if m else ""


# -----------------------------------------------------------------------------
# 2. Parse the Final Requirements Register markdown
# -----------------------------------------------------------------------------
def parse_register(path):
    with open(path, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    # -------------------------------------------------------------------------
    # Reconstruct logical table rows. The source markdown sometimes wraps a
    # single Excel row across multiple physical lines (multi-line cells). A table
    # row that starts with "|" but does not end with "|" is incomplete; we
    # collect subsequent non-pipe lines until we reach a line that ends with "|".
    # -------------------------------------------------------------------------
    logical_lines = []  # (1-based line_no, line_text, is_table_row)
    i = 0
    while i < len(raw_lines):
        raw = raw_lines[i]
        line = raw.rstrip("\n")
        i += 1
        if not line.startswith("|"):
            logical_lines.append((i, line, False))
            continue
        # Start of a table row; buffer until it is complete (ends with "|")
        buffer = [line]
        while i < len(raw_lines):
            next_line = raw_lines[i].rstrip("\n")
            if next_line.startswith("|"):
                break
            buffer.append(next_line)
            i += 1
        logical_lines.append((i, " ".join(buffer), True))

    rows = []
    current_section = "Final Requirements"
    current_section_label = ""
    last_component_by_family = {}

    # Heuristic to detect table-only section labels that should become the current component
    def is_section_label(id_field, comp_field, scope_field):
        label = (id_field or comp_field or "").strip()
        return (
            scope_field == ""
            and not re.match(r"^(BIMM|INTF|FR-DTW|ROW-|AI-|T\d\s|Common\s|IT\s|WTP|STP|MRSS|VHT|FDAS|HVAC|BHS|PBB|VDGS|GPU|PCA|ATRS|LCMS|ECMS|SAC)", label)
            and (":" in label or "Integrations" in label or "Assets" in label or "Requirements" in label
                 or "Ops DT" in label or "Geokno" in label or "BIM" in label or "Functional" in label
                 or "Simulation" in label or "AI Agents" in label or "Non-Functional" in label
                 or "Platform" in label or "Common" in label or "Testing" in label or "Deployments" in label
                 or "Out of Scope" in label or "Registry" in label or "Federation" in label)
        )

    for line_no, line, is_table in logical_lines:
        if not is_table:
            line = line.strip()
            # Multi-line scope continuation: a non-empty, non-header text line immediately following
            # a table row is treated as a continuation of the previous requirement's scope cell.
            if line and not line.startswith("## ") and rows:
                rows[-1]["scope"] += " " + line
            elif line.startswith("## "):
                current_section = line[3:].strip()
            continue

        cells = [c.strip() for c in line.split("|")]
        cells = cells[1:-1] if cells[0] == "" and cells[-1] == "" else cells
        if len(cells) < 3:
            continue

        id_field = cells[0]
        comp_field = cells[1] if len(cells) > 1 else ""
        scope_field = cells[2] if len(cells) > 2 else ""

        # Skip markdown header separator and column-title rows
        if id_field in ("ID", "") and comp_field == "Component" and scope_field == "Scope":
            continue
        if re.fullmatch(r"[-:]+", id_field.replace(" ", "")):
            continue

        # Section label row: ID non-empty, scope empty
        if is_section_label(id_field, comp_field, scope_field):
            current_section_label = id_field or comp_field
            continue

        # Section label row: ID empty, component present, scope empty
        if id_field == "" and comp_field and scope_field == "":
            current_section_label = comp_field
            continue

        # Continuation row: ID empty, component empty, scope continues previous requirement
        if id_field == "" and comp_field == "" and scope_field and rows:
            rows[-1]["scope"] += " " + scope_field
            continue

        # Continuation row: ID empty, component present, scope present (component is actual component)
        if id_field == "" and comp_field and scope_field:
            req_id = f"ROW-{line_no}"
            component = comp_field
            scope = scope_field
        elif id_field:
            req_id = id_field
            # Inherit component within the same ID family when the component cell is empty
            prefix = family_prefix(req_id)
            if comp_field:
                component = comp_field
            elif prefix and prefix in last_component_by_family:
                component = last_component_by_family[prefix]
            else:
                component = current_section_label
            scope = scope_field
        else:
            continue

        # Gather other useful fields (best-effort by position)
        phase = cells[11] if len(cells) > 11 else ""
        delivery_month = cells[9] if len(cells) > 9 else ""
        complexity = cells[7] if len(cells) > 7 else ""
        counts = cells[5] if len(cells) > 5 else ""
        dependency = cells[10] if len(cells) > 10 else ""

        if not scope:
            continue

        # Remember the last real component for each ID family
        prefix = family_prefix(req_id)
        if component and not looks_like_req_id(component) and not looks_like_section_label(component) and prefix:
            last_component_by_family[prefix] = component

        # Clean up component values that are actually prior requirement IDs
        if looks_like_req_id(component):
            component = last_component_by_family.get(prefix, component)

        group = classify_group(req_id, component, scope, current_section_label)

        rows.append({
            "line": line_no,
            "id": req_id,
            "component": component,
            "scope": scope,
            "counts": counts,
            "complexity": complexity,
            "delivery_month": delivery_month,
            "phase": phase,
            "dependency": dependency,
            "group": group,
            "section_label": current_section_label,
        })
    return rows


def classify_group(req_id, component, scope, section_label=""):
    text = f"{req_id} {component} {scope}".upper()
    section = section_label.upper()

    # Section-label overrides first (the source uses table rows as section headers)
    if "OUT OF SCOPE" in section:
        return "Out of Scope"
    if "NON-FUNCTIONAL REQUIREMENTS" in section:
        return "Non-Functional Requirements"
    if "PLATFORM REQUIREMENTS" in section:
        return "Platform / Protocol"
    if "COMMON FUNCTIONALITY" in section or "COMMON" in section:
        return "Common Functionality"
    if "TESTING" in section or "DEPLOYMENTS" in section:
        return "Testing / Environments"
    if "AI AGENTS" in section:
        return "AI Agents"
    if "ASSET REGISTRY" in section or "ASSET FEDERATION" in section or "ASSET COMMONS" in section or "ASSET MODELING" in section:
        return "Asset Registry & Modeling"
    if "FUNCTIONAL REQUIREMENTS - DT WIDGETS" in section or "FUNCTIONAL REQUIREMENTS - OT & IT WIDGETS" in section:
        return "DT Widget / Functional Requirement"
    if "FUNCTIONAL REQUIREMENTS - SIMULATION" in section:
        return "Simulation / What-If"
    # IT data feeds are consumed by DT widgets / simulation; only ITOM/middleware health stays in OT/IT Integration
    if section == "INTEGRATIONS - IT":
        if component and ("ITOM" in component.upper() or "MANAGE ENGINE" in component.upper()):
            return "OT/IT Integration"
        return "DT Widget / Functional Requirement"
    if "OPS DT: CAPABILITIES" in section:
        return "DT Widget / Functional Requirement"
    if "OPS DT" in section or "VISUALIZATION" in section or "GEOKNO" in section or "BIM MODELING" in section or "LIDAR" in section:
        return "BIM / Geo DT"
    if "INTEGRATIONS" in section:
        return "OT/IT Integration"

    # High-level content overrides
    if "OUT OF SCOPE" in text:
        return "Out of Scope"
    if "NON-FUNCTIONAL" in text or re.search(r"\b(PLATFORM UPTIME|LATENCY|INCIDENT RESPONSE|RTO|RPO|ENCRYPTION|MFA|AUTHENTICAT|SERVICE AND SUPPORT)\b", text):
        return "Non-Functional Requirements"
    if "PLATFORM REQUIREMENTS" in text or re.search(r"\b(OPC|BACNET|MODBUS|MQTT|ON-PREM|CLOUD CONNECTOR|IOT DATA|ON-PREM)\b", text):
        return "Platform / Protocol"
    if "COMMON FUNCTIONALITY" in text or re.search(r"\b(USER ONBOARDING|SINGLE-SESSION|USER AUDIT TRAIL)\b", text):
        return "Common Functionality"
    if "TESTING" in text or "DEPLOYMENTS" in text or re.search(r"\b(DEV INSTANCE|UAT INSTANCE|PROD INSTANCE|NW \+ FIREWALLS)\b", text):
        return "Testing / Environments"
    if "AI AGENTS" in text or re.search(r"\b(AI-0\d|AI ORCHESTRATION|MLFLOW|PASSENGER FLOW MONITORING|HVAC -|ENERGY & HVAC|FIRE SAFETY|SECURITY & PERIMETER|STRUCTURAL|ELECTRICAL SYSTEMS|WATER & DRAINAGE|NL QUERY|MODEL LIFECYCLE|EXPLAINABILITY)\b", text):
        return "AI Agents"
    if "SIMULATION" in text or re.search(r"\b(WHAT IF|WHAT-IF|DISRUPTION|IROPS|NOTAM|EWS|EARLY WARNING|PASSENGER JOURNEY)\b", text):
        return "Simulation / What-If"
    if re.search(r"\b(SAC|SMART CITY|SMART WASHROOM|SMART BUGGY|SMART TROLLEY|SMART TRAFFIC|IOT GATEWAY)\b", text):
        return "SAC / Smart City / IoT"
    if re.search(r"\b(ASSET REGISTRY|ASSET FEDERATION|ASSET MODELING|TAXONOMY|ONTOLOGY|CLG|CAI|METADATA STORE|SYNC FRAMEWORK)\b", text):
        return "Asset Registry & Modeling"
    if req_id.startswith("FR-DTW") or re.search(r"\b(WIDGET|CURBSIDE|TERMINAL OPS|AIRPORT SUMMARY|TERMINAL SUMMARY|AIRSIDE SUMMARY|SECURITY|CAMERA ACCESS|COUNTER|DESK|RETAIL|F&B|STORE|QUEUE|CROWD|DWELL|FIDS|CUPPS|E-GATES|CHECK-IN|SBD|BOARDING|BAGGAGE|VMS/CCTV|UTAM|AODB|RMS|KLoudspot|XOVIS|TELEMATICS|ARC|PTM|ADS-B)\b", text):
        return "DT Widget / Functional Requirement"
    if req_id.startswith("INTF") or re.search(r"\b(INTEGRATIONS - |T1 INTEGRATIONS|T2 INTEGRATIONS|T3 - INTEGRATIONS|COMMON INTEGRATIONS|INTEGRATIONS - IT)\b", text):
        return "OT/IT Integration"
    if re.search(r"\b(BIMM|BIM MODELING|BIRDS EYE|GEOKNO|LIDAR|VISUALIZATION - STRUCTURE|VISUALIZATION - INTERIORS|OT ASSETS VISUALIZATION|UNDERGROUND UTILITY|GPR|DTM|DSM|ORTHOPHOTO|OLS|SPACE MANAGEMENT|GIS ANALYTICAL|FLOOD|3D SPACE|LOD|ODT-BE)\b", text):
        return "BIM / Geo DT"
    return "Other"


# -----------------------------------------------------------------------------
# 3. Map each register row to Addendum A use cases, owner module, package/milestone
# -----------------------------------------------------------------------------
def _is_visualization(component: str, scope: str) -> bool:
    t = (component + " " + scope).lower()
    markers = ["visualize", "display", "let users", "show/hide", "zoom", "navigate", "visualisation", "visualization", "exterior view", "interior view", "layers"]
    return any(m in t for m in markers)


def _is_security_context(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in [
        "intrusion", "reverse-entry", "reverse entry", "unattended baggage", "unattended bag",
        "suspicious behaviour", "suspicious behavior", "prolonged loitering", "perimeter",
        "cctv", "vms/cctv", "security event", "security zones",
    ])


def _is_retail_analytics(text: str) -> bool:
    t = text.lower()
    strong = [
        "store performance", "store mix", "shelf merchandising", "dwell time monetisation",
        "dwell time monetization", "retail optimisation", "retail optimization", "footfall",
        "queue vs revenue", "campaign & promotion", "campaign and promotion", "lounge vs retail",
        "staffing vs sales", "retail expansion", "store location analysis", "revenue trade-off",
        "retail and f&b", "retail & f&b",
    ]
    return any(k in t for k in strong)


def _is_queue_context(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in [
        "queue length", "wait time", "processing time", "queue management", "crowd management",
        "heatmaps", "passenger flow", "journey time", "dwell and journey",
    ])


def _is_curbside_context(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in [
        "curbside", "arrival ramp", "departure ramp", "landside traffic", "vehicle classification",
        "curb occupancy", "vehicle dwell", "trolley bay", "ground transport", "parking occupancy",
    ])


def _is_it_asset_context(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in [
        "it asset", "passenger-journey", "passenger journey", "availability monitoring",
        "downtime reporting", "real-time alerts", "impact analysis", "root cause correlation",
        "root-cause correlation", "fids", "cupps", "cuss", "e-gate", "e gate", "sbd", "boarding gate",
        "baggage scanner", "2d barcode", "aftn", "digiyatra", "check-in", "check in",
    ])


def _is_disruption_context(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in [
        "disruption simulation", "disruption management", "irops", "dde", "fog and storm",
        "what-if simulation", "what if simulation", "early warning", "ews",
    ])


def _is_summary_dashboard_row(text: str) -> bool:
    t = text.lower()
    return "kpi summary" in t or "summary covering" in t or "consolidated" in t or "display a consolidated" in t


def map_row(row):
    text = f"{row['id']} {row['component']} {row['scope']}".lower()
    cases = []
    basis = []
    owner = ""
    package = ""
    milestone = ""

    # --- Context predicates used to guard cross-domain keyword matches ---
    is_viz = _is_visualization(row["component"], row["scope"])
    is_sec = _is_security_context(text)
    is_ret = _is_retail_analytics(text)
    is_que = _is_queue_context(text)
    is_curb = _is_curbside_context(text)
    is_it = _is_it_asset_context(text)
    is_disr = _is_disruption_context(text)
    is_summary = _is_summary_dashboard_row(text)
    g = row["group"]
    is_ai = g == "AI Agents"

    # --- Group-driven default package / milestone ---
    if g == "BIM / Geo DT":
        package = "D-05 / D-16 / D-20 — Federated BIM, Geo Digital Twin, Underground Utilities"
        milestone = "MS3 (Mo5) / MS4 (Mo7)"
    elif g == "OT/IT Integration":
        package = "D-09 — BMS/OT Integration Report; D-11 — API Documentation Portal"
        milestone = "MS4 (Mo7)"
    elif g == "DT Widget / Functional Requirement":
        package = "D-08 — Deployed and Tested Digital Twin Platform (UAT sign-off)"
        milestone = "MS4 (Mo7)"
    elif g == "Simulation / What-If":
        package = "D-21 — Spatial Decision & Simulation Engine"
        milestone = "MS5 (Mo9)"
    elif g == "SAC / Smart City / IoT":
        package = "D-08 + Smart City/IoT Gateway integration (§2.5.10)"
        milestone = "MS4 (Mo7)"
    elif g == "Asset Registry & Modeling":
        package = "D-06 — Asset Attribute Data Register; D-07 — Existing Data Migration Report"
        milestone = "MS3 (Mo5) / MS4 (Mo7)"
    elif g == "AI Agents":
        package = "D-10 — AI Agent Estate"
        milestone = "MS5 (Mo9)"
    elif g == "Non-Functional Requirements":
        package = "D-12 — Cybersecurity Architecture & Controls; D-22 — Security Operations Pack; cross-cutting SLA (§4.5)"
        milestone = "MS4 (Mo7) / MS5 (Mo9) / MS6 (Mo9+90d)"
    elif g == "Platform / Protocol":
        package = "D-08 / D-09 — Platform & Integration backbone"
        milestone = "MS4 (Mo7)"
    elif g == "Common Functionality":
        package = "D-08 — Digital Twin Platform"
        milestone = "MS4 (Mo7)"
    elif g == "Testing / Environments":
        package = "D-13 / D-14 — Training & As-Built Docs; UAT instances under D-08/D-09"
        milestone = "MS4–MS6"
    elif g == "Out of Scope":
        package = "Not in base scope; Phase 2 / change request"
        milestone = "Post-Mo9 / Phase 2"
    else:
        package = "D-08 — Digital Twin Platform (inferred)"
        milestone = "MS4 (Mo7)"

    # --- Use-case accumulator ---
    def add_case(name, reason):
        if name not in cases:
            cases.append(name)
            basis.append(reason)

    # --- Equipment-family / component-driven direct mapping ---
    comp_scope = f"{row['component']} {row['scope']}".lower()
    comp_lower = row["component"].lower()

    # --- Refine security context so that CCTV/DFMD mentions inside baggage, resource-master,
    #     BIM-visualisation, or queue/retail widgets do not over-map to security use cases.
    if is_sec:
        if g == "BIM / Geo DT" and "security" not in comp_lower:
            is_sec = False
        elif (is_que or is_ret) and "security" not in comp_lower and "cctv" not in comp_lower and "vms" not in comp_lower:
            is_sec = False
        elif "bhs" in comp_scope or ("baggage" in comp_scope and "unattended" not in comp_scope):
            is_sec = False
        elif "resource master" in comp_scope:
            is_sec = False

    if not is_ai:
        if "hvac" in comp_scope or "chiller" in comp_scope or ("pump" in comp_scope and "water" not in comp_scope.split("pump")[0].split()[-3:]) or "cooling tower" in comp_scope or "ahu" in comp_scope or "pahu" in comp_scope or "cassette" in comp_scope or "fcu" in comp_scope or "air compressor" in comp_scope:
            add_case("Thermal Load Simulation", "component family: HVAC")
            add_case("Passenger Load vs HVAC Demand", "component family: HVAC")
            add_case("Zone-Based Cooling Optimisation", "component family: HVAC")
            owner = "Simulation engine + Mechanical & HVAC agent + BMS"

    if not is_ai:
        if "fdas" in comp_scope or "fire alarm" in comp_scope or "smoke detector" in comp_scope or "sprinkler" in comp_scope or "flow switch" in comp_scope:
            add_case("Evacuation & Fire Scenarios", "component family: FDAS/fire safety")
            owner = "Fire Safety & Life Safety agent + Simulation engine"

    if not is_sec and not is_ai:
        if "bhs" in comp_scope or ("baggage" in comp_scope and "unattended" not in comp_scope):
            add_case("Baggage Flow Optimisation", "component family: BHS/baggage")
            owner = "Simulation engine + BHS/BRS"

    if not is_ai:
        if "ecms" in comp_scope or "mrss" in comp_scope or ("electrical" in comp_scope and "scada" not in comp_scope) or "transformer" in comp_scope or "breaker" in comp_scope or "incoming line" in comp_scope:
            add_case("Power Infrastructure Stress Testing", "component family: electrical power")
            owner = "Simulation engine + Electrical agent + ECMS"

    if not is_ai:
        if "wtp" in comp_scope or "stp" in comp_scope or ("water" in comp_scope and "chilled" not in comp_scope) or "drainage" in comp_scope or "stormwater" in comp_scope:
            add_case("Stormwater analysis with IoT monitoring", "component family: water/stormwater")
            owner = "Geo Digital Twin - Flood Simulation + IoT Gateway"

    if is_sec:
        add_case("Reverse-entry detection in restricted zones", "security context")
        add_case("Unattended-baggage detection", "security context")
        add_case("Behaviour analytics for threat detection", "security context")
        add_case("Predictive security monitoring", "security context")
        add_case("Security asset mapping", "security context")
        add_case("Breach Detection", "security context")
        owner = "Security & Perimeter agent + CCTV/VMS/ACS"
    elif comp_lower and any(k in comp_lower for k in ["security", "cctv", "vms/cctv", "dfmd", "x-ray", "pesc"]):
        add_case("Unattended-baggage detection", "component family: security/CCTV")
        add_case("Behaviour analytics for threat detection", "component family: security/CCTV")
        add_case("Breach Detection", "component family: security/PIDS")
        add_case("Security asset mapping", "component family: security asset")
        owner = "Security & Perimeter agent + CCTV/VMS/ACS"

    if is_curb:
        add_case("Landside Traffic & Curbside Management", "component family: curbside/landside traffic")
        owner = "Simulation engine + landside traffic feed"

    if is_que and not is_summary:
        add_case("Queue Management Optimisation", "component family: queue management")
        add_case("Passenger Flow Optimisation", "component family: passenger flow/queue")
        owner = "Passenger Flow agent + XOVIS/Kloudspot + Simulation"

    if is_ret and not is_summary and not is_viz:
        add_case("Retail Optimisation (footfall, dwell)", "component family: retail")
        add_case("Store Location Optimisation", "component family: retail/store")
        add_case("Dwell Time Monetisation", "component family: retail/dwell")
        owner = "Simulation engine + Passenger Flow agent + retail sensors"

    if is_it and not is_sec:
        add_case("Monitoring / alerting of all IT systems", "component family: passenger-journey IT")
        add_case("Availability monitoring of passenger-journey IT assets", "component family: IT asset availability")
        if "downtime" in text:
            add_case("Downtime reporting", "keyword 'downtime reporting'")
        if "real-time alerts" in text or "real time alerts" in text:
            add_case("Real-time alerts on passenger-journey IT assets", "keyword 'real-time alerts IT'")
        if "impact analysis" in text:
            add_case("Impact analysis (IT asset outage → passenger journey)", "keyword 'impact analysis'")
        if "root-cause" in text or "root cause" in text:
            add_case("Root-cause correlation across IT/OT assets", "keyword 'root-cause correlation'")
        owner = "AIOP backbone + Passenger Flow agent + OI layer"

    if "apoc" in comp_scope or "oneapoc" in comp_scope:
        add_case("APOC integration — situational awareness & operational intelligence surface", "component family: APOC/OneAPOC")
        add_case("APOC Phase-2 integration", "component family: APOC/OneAPOC")
        owner = "OI layer + APOC/OneAPOC integration"

    if ("smart city" in comp_scope or "smart washroom" in comp_scope or "smart buggy" in comp_scope
            or "smart trolley" in comp_scope or "smart traffic" in comp_scope or "iot gateway" in comp_scope
            or "ble" in comp_scope) and not is_ai:
        add_case("Monitoring / alerting of all IT systems", "component family: SAC/Smart City/IoT")
        owner = "IoT Gateway + Geo Digital Twin"

    # --- Use-case keyword matching (guarded to avoid cross-domain over-match) ---
    if "borewell" in text:
        add_case("Borewell recharge monitoring with IoT", "keyword 'borewell'")
    if "stormwater" in text or "flood" in text:
        add_case("Stormwater analysis with IoT monitoring", "keyword 'stormwater/flood'")
    if "reverse-entry" in text or "reverse entry" in text:
        add_case("Reverse-entry detection in restricted zones", "keyword 'reverse-entry/intrusion'")
    if "unattended baggage" in text or "unattended bag" in text:
        add_case("Unattended-baggage detection", "keyword 'unattended baggage'")
    if "suspicious" in text or "behaviour" in text or "behavior" in text or "prolonged loitering" in text:
        add_case("Behaviour analytics for threat detection", "keyword 'suspicious/behaviour'")
    if "predictive security" in text or "security monitoring" in text:
        add_case("Predictive security monitoring", "keyword 'predictive security'")
    if "security asset" in text or "pids" in text:
        add_case("Security asset mapping", "keyword 'security asset/PIDS'")
        add_case("Breach Detection", "keyword 'PIDS/breach'")
    if "google" in text or "satellite" in text or "external basemap" in text:
        add_case("Google Maps / satellite integration (landside)", "keyword 'Google/satellite'")
    if "space allocation" in text or "space-allocation" in text or ("allocation" in text and "space" in text):
        add_case("Identification of space-allocation changes", "keyword 'space allocation'")
    if "gis" in text and ("analytics" in text or "planning" in text or "utilisation" in text or "land use" in text):
        add_case("GIS-based analytics for planning and utilisation", "keyword 'GIS analytics/planning'")
    if "fog" in text or "low visibility" in text or "rvr" in text:
        add_case("Surface navigation in low-visibility (fog)", "keyword 'fog/RVR/low visibility'")
    if "what-if" in text or "what if" in text or "scenario" in text:
        add_case("What-if scenario analytics", "keyword 'what-if/scenario'")
        add_case("What-if scenario modelling (IT asset scenarios)", "keyword 'what-if scenario'")
    if "live operations" in text or "operations monitoring dashboard" in text or "airport summary" in text or "terminal summary" in text or "airside summary" in text:
        add_case("Live operations monitoring dashboard", "keyword 'live operations/dashboard/summary'")
    if "overstaying" in text or "unidentified passenger" in text or "reverse paxflow" in text:
        add_case("Identification of overstaying / unidentified passengers", "keyword 'overstaying/unidentified'")
    if is_disr and not is_sec:
        if "irop" in text or "dde" in text or "disruption" in text:
            add_case("IROPS Simulation", "keyword 'IROPS/DDE'")
            add_case("Disruption Management Simulation", "keyword 'disruption'")
            add_case("Disruption Monetisation Strategy", "keyword 'disruption'")
    if "evacuation" in text or "fire scenario" in text or ("fire" in text and "simulation" in text) or ("emergency" in text and "response" in text):
        add_case("Evacuation & Fire Scenarios", "keyword 'evacuation/fire'")
    if "breach detection" in text or "pids" in text:
        add_case("Breach Detection", "keyword 'breach/PIDS'")

    # Retail keyword block - only for genuine retail-analytics rows, not generic zone lists
    if is_ret and not is_summary and not is_viz:
        if "retail" in text or "footfall" in text or "dwell" in text:
            add_case("Retail Optimisation (footfall, dwell)", "keyword 'retail/dwell'")
            add_case("Dwell Time Monetisation", "keyword 'dwell'")
            add_case("Store Location Optimisation", "keyword 'retail/store'")
        if "store mix" in text:
            add_case("Store Mix Optimisation", "keyword 'store mix'")
        if "shelf" in text:
            add_case("Shelf Merchandising Optimisation", "keyword 'shelf'")
        if "campaign" in text or "promotion" in text:
            add_case("Campaign & Promotion Simulation", "keyword 'campaign/promotion'")
        if "queue vs revenue" in text or ("revenue" in text and "queue" in text):
            add_case("Queue vs Revenue Trade-off", "keyword 'queue revenue'")
        if "lounge" in text:
            add_case("Lounge vs Retail Trade-off", "keyword 'lounge'")
        if "staffing" in text or "workforce" in text or "wfm" in text:
            add_case("Workforce Deployment Optimisation", "keyword 'workforce/WFM'")
            add_case("Staffing vs Sales Optimisation", "keyword 'staffing'")
        if "retail expansion" in text:
            add_case("Retail Expansion Energy Impact", "keyword 'retail expansion'")

    if "baggage flow" in text or "bhs" in text:
        if not is_sec:
            add_case("Baggage Flow Optimisation", "keyword 'baggage/BHS'")
    if is_curb:
        add_case("Landside Traffic & Curbside Management", "keyword 'curbside/landside traffic'")
    if "thermal load" in text or ("thermal" in text and "load" in text) or "hvac demand" in text or "passenger load vs hvac" in text:
        add_case("Thermal Load Simulation", "keyword 'thermal load'")
        add_case("Passenger Load vs HVAC Demand", "keyword 'passenger load/HVAC'")
    if "zone-based cooling" in text or "zone based cooling" in text:
        add_case("Zone-Based Cooling Optimisation", "keyword 'zone-based cooling'")
    if "power infrastructure" in text or "stress testing" in text or "mrss" in text or "electrical" in text:
        add_case("Power Infrastructure Stress Testing", "keyword 'power/electrical stress'")
    if is_que and not is_summary:
        add_case("Passenger Flow Optimisation", "keyword 'passenger flow'")
        add_case("Queue Management Optimisation", "keyword 'queue management'")
    if "check-in" in text and "capacity" in text:
        add_case("Check-in & Security Capacity Planning", "keyword 'check-in capacity'")
    if "gate allocation" in text or "gate utilisation" in text or "stand" in text:
        add_case("Gate Allocation Optimisation", "keyword 'gate allocation'")
        add_case("Gate Allocation & Utilisation", "keyword 'gate allocation'")
    if "apoc" in text or "oneapoc" in text:
        add_case("APOC integration — situational awareness & operational intelligence surface", "keyword 'APOC/OneAPOC'")
        add_case("APOC Phase-2 integration", "keyword 'APOC Phase-2'")
    if ("smart city" in text or "smart washroom" in text or "smart buggy" in text
            or "smart trolley" in text or "smart traffic" in text or "iot gateway" in text) and not is_ai:
        add_case("Monitoring / alerting of all IT systems", "keyword 'Smart City/IoT'")

    # --- If no Addendum A case matched, assign a functional umbrella based on group ---
    if not cases:
        if g == "BIM / Geo DT":
            add_case("GIS-based analytics for planning and utilisation", "Group-level default: BIM/Geo DT")
        elif g == "OT/IT Integration":
            add_case("Live operations monitoring dashboard", "Group-level default: OT/IT integration feeds the live dashboard")
        elif g == "DT Widget / Functional Requirement":
            add_case("Live operations monitoring dashboard", "Group-level default: widget requirement")
        elif g == "Simulation / What-If":
            add_case("What-if scenario analytics", "Group-level default: simulation requirement")
        elif g == "SAC / Smart City / IoT":
            add_case("Monitoring / alerting of all IT systems", "Group-level default: SAC/IoT integration")
        elif g == "Asset Registry & Modeling":
            add_case("Identification of space-allocation changes", "Group-level default: asset registry supports space/allocation use cases")
        elif g == "AI Agents":
            add_case("Live operations monitoring dashboard", "Group-level default: AI agent output feeds operational dashboard")
        elif g == "Non-Functional Requirements":
            add_case("Live operations monitoring dashboard", "Group-level default: NFR enables dashboard")
        elif g == "Platform / Protocol":
            add_case("Live operations monitoring dashboard", "Group-level default: platform enables dashboard")
        elif g == "Common Functionality":
            add_case("Live operations monitoring dashboard", "Group-level default: common functionality")
        elif g == "Out of Scope":
            add_case("Landside Traffic & Curbside Management", "Group-level default: out-of-scope items")
        else:
            add_case("Live operations monitoring dashboard", "Group-level default")
        basis[-1] = basis[-1].replace("keyword", "group-level default")

    # --- Derive owner module from the most specific matched Addendum A case ---
    # Prefer domain-specific owners over generic dashboard/IT umbrella
    preferred_order = [
        "Security & Perimeter", "Fire Safety & Life Safety", "Mechanical & HVAC", "Electrical",
        "Simulation engine + Passenger Flow", "Passenger Flow agent", "OI layer + APOC",
        "Geo Digital Twin", "IoT Gateway", "AIOP backbone",
    ]
    chosen_owner = None
    for case_name in cases:
        case = CASE_BY_NAME.get(case_name, {})
        case_owner = case.get("owner", "")
        if not case_owner:
            continue
        # Prefer the first owner that matches a domain-specific marker
        for marker in preferred_order:
            if marker.lower() in case_owner.lower():
                chosen_owner = case_owner
                break
        if chosen_owner:
            break
    owner = chosen_owner or CASE_BY_NAME.get(cases[0], {}).get("owner", "TBD")

    # --- Refine package for specific register items based on description keywords ---
    if row["id"] == "ODT-BE-01" or "birds eye" in text or "airborne lidar" in text or "dtm" in text or "dsm" in text or "orthophoto" in text or "point cloud" in text:
        package = "D-02 / D-03 / D-04 — Airborne/Indoor LiDAR, DTM/DSM, Orthophoto, Accuracy Report"
        milestone = "MS2 (Mo3)"
    if "underground" in text or "utility" in text or "gpr" in text:
        package = "D-20 — Underground Utility Maps"
        milestone = "MS3 (Mo5)"
    if "bim" in text and ("model" in text or "ifc" in text) and not ("asset attribution" in text or "asset attribute" in text):
        package = "D-05 — IFC-Compliant Federated BIM Models"
        milestone = "MS3 (Mo5)"
    if "asset attribute" in text or "asset register" in text or "cafm" in text or "cmms" in text:
        package = "D-06 — Asset Attribute Data Register; D-07 — Existing Data Migration Report"
        milestone = "MS3 (Mo5)"
    if "cyber" in text or "penetration" in text or "siem" in text or "sbom" in text:
        package = "D-12 / D-12b / D-22 — Cybersecurity, Penetration Test, Security Operations Pack"
        milestone = "MS4 (Mo7) / MS5 (Mo9)"
    if "ols" in text or "obstacle" in text:
        package = "D-18 — OLS Monitoring Application"
        milestone = "MS5 (Mo9)"
    if "training" in text or "as-built" in text or "post-implementation" in text or re.search(r"\b(user|operations|training|o&m|maintenance) manual\b", text):
        package = "D-13 / D-14 / D-15 — Training, As-Built Docs, Post-Implementation Review"
        milestone = "MS6 (Mo9 + 90d)"

    return {
        "cases": cases,
        "basis": basis,
        "owner": owner,
        "package": package,
        "milestone": milestone,
    }


# -----------------------------------------------------------------------------
# 4. Extract vendor / protocol / location inventory from the register
# -----------------------------------------------------------------------------
def extract_vendors_protocols(rows):
    """Return a structured inventory of integration vendors and protocols with locations."""
    vendors = defaultdict(lambda: {"systems": set(), "locations": set(), "sources": set()})
    it_systems = []  # list of dicts
    protocols = defaultdict(lambda: {"locations": set(), "sources": set()})

    # Normalise terminal / location from component or requirement id
    def location_from(row):
        comp = (row.get("component") or "").upper()
        rid = (row.get("id") or "").upper()
        scope = (row.get("scope") or "").upper()
        # Explicit multi-terminal statements such as "Applicable for terminals: T1, T2, T3"
        multi_match = re.search(r"(?:TERMINALS?|APPLICABLE FOR)\s*:?\s*(T\d(?:\s*,\s*T\d)*)", scope)
        if multi_match:
            terms = re.findall(r"T\d", multi_match.group(1))
            if terms:
                return ", ".join(sorted(set(terms)))
        if "COMMON" in rid or "CM-" in rid or "CM_" in rid:
            return "Common / Airport-wide"
        if "T1" in comp or "T1" in rid:
            locs = []
            if "T2" in comp or "T2" in rid:
                locs.append("T2")
            if "T3" in comp or "T3" in rid:
                locs.append("T3")
            if locs:
                return "T1, " + ", ".join(locs)
            return "T1"
        if "T2" in comp or "T2" in rid:
            if "T3" in comp or "T3" in rid:
                return "T2, T3"
            return "T2"
        if "T3" in comp or "T3" in rid:
            return "T3"
        # Default for IT systems: read location hints from scope
        if "TERMINAL 1" in scope and "TERMINAL 2" in scope and "TERMINAL 3" in scope:
            return "T1, T2, T3"
        if "TERMINAL 1" in scope and "TERMINAL 2" in scope:
            return "T1, T2"
        if "TERMINAL 1" in scope and "TERMINAL 3" in scope:
            return "T1, T3"
        if "TERMINAL 2" in scope and "TERMINAL 3" in scope:
            return "T2, T3"
        if "TERMINAL 1" in scope:
            return "T1"
        if "TERMINAL 2" in scope:
            return "T2"
        if "TERMINAL 3" in scope:
            return "T3"
        # Avoid matching stray T1/T2/T3 in unrelated words if component is generic
        if comp in ("RPO", "PLATFORM REQUIREMENTS", "NFR"):
            return "Airport-wide"
        if "AIRSIDE" in comp or "AIRSIDE" in scope:
            return "Airside"
        if "CURBSIDE" in comp or "CURBSIDE" in scope or "LANDSIDE" in scope:
            return "Landside / Curbside"
        return "Airport-wide"

    # Known vendor names that appear in the register (or as OEM sub-supplier)
    OEM_RE = re.compile(r"OEM\s*-\s*([^,]+?)(?:\s*,\s*Pt|\s+Pt|\s*-\s*Pt|$)", re.IGNORECASE)

    for r in rows:
        scope = r.get("scope") or ""
        comp = r.get("component") or ""
        rid = r.get("id") or ""
        loc = location_from(r)

        # 1. OEM vendors from OT integration rows
        m = OEM_RE.search(scope)
        if m:
            raw_vendor = m.group(1).strip()
            # Clean unknown placeholders
            if raw_vendor.upper() in ("X", "NA", "N/A", "TBD", "UNKNOWN"):
                vendor = "Unknown / TBC"
            else:
                vendor = raw_vendor
            # System name from component, e.g. "T1 - HVAC" -> "HVAC"
            system = comp.split("-")[-1].strip() if "-" in comp else comp.strip()
            system = system or rid
            vendors[vendor]["systems"].add(system)
            vendors[vendor]["locations"].add(loc)
            vendors[vendor]["sources"].add(rid)

        # 2. IT system / service names from Integrations - IT and other named feeds
        section = (r.get("section_label") or "").strip()
        if section == "Integrations - IT" or (section == "Integrations - Facilities" and rid.startswith("ROW-")):
            if comp and not looks_like_section_label(comp) and not looks_like_req_id(comp):
                it_systems.append({
                    "name": comp,
                    "scope_hint": scope[:120] + "..." if len(scope) > 120 else scope,
                    "location": loc,
                    "source": rid,
                })

        # 3. Protocols from explicit mentions
        text = f"{rid} {comp} {scope}".upper()
        protocol_patterns = [
            (r"\bOPC/DA\b", "OPC/DA"),
            (r"\bOPC/UA\b", "OPC/UA"),
            (r"\bOPC-DA\b", "OPC-DA"),
            (r"\bOPC-UA\b", "OPC-UA"),
            (r"\bBACNET\s+IP\b", "BACnet IP"),
            (r"\bBACNET\b", "BACnet"),
            (r"\bMODBUS\s+IP\b", "Modbus IP"),
            (r"\bMODBUS\b", "Modbus"),
            (r"\bMQTT\b", "MQTT"),
            (r"\bSAML\s*2\.0\b", "SAML 2.0"),
            (r"\bSAML\b", "SAML"),
            (r"\bOAUTH\s*2\.0\b", "OAuth 2.0"),
            (r"\bOAUTH\b", "OAuth"),
            (r"\bTLS\s*1\.2\+?\b", "TLS 1.2+"),
            (r"\bTLS\b", "TLS"),
            (r"\bAES-256\b", "AES-256"),
            (r"\bIEC\s*62443\b", "IEC 62443"),
            (r"\bAFTN\b", "AFTN"),
            (r"\bREST\s*API\b", "REST API"),
            (r"\bREST\b", "REST"),
            (r"\bSOAP\b", "SOAP"),
            (r"\bJSON\b", "JSON"),
            (r"\bXML\b", "XML"),
            (r"\bSQL\b", "SQL"),
            (r"\bSNMP\b", "SNMP"),
            (r"\bSMTP\b", "SMTP"),
            (r"\bLDAP\b", "LDAP"),
            (r"\bKERBEROS\b", "Kerberos"),
            (r"\bIPSEC\b", "IPSec"),
            (r"\bVPN\b", "VPN"),
            (r"\bSFTP\b", "SFTP"),
            (r"\bSSH\b", "SSH"),
            (r"\bWEBSOCKET\b", "WebSocket"),
            (r"\bAMQP\b", "AMQP"),
            (r"\bKAFKA\b", "Kafka"),
            (r"\bDDS\b", "DDS"),
            (r"\bHTTPS?\b", "HTTP/HTTPS"),
            (r"\bTCP/IP\b", "TCP/IP"),
            (r"\bUDP\b", "UDP"),
        ]
        for pat, name in protocol_patterns:
            if re.search(pat, text):
                protocols[name]["locations"].add(loc)
                protocols[name]["sources"].add(rid)

    # 4. Supplemental scan: integration rows with a component name but empty scope
    #    are dropped by the main parser (no requirement text) but still represent
    #    systems/protocols the platform must integrate with.
    with open(REGISTER_FILE, "r", encoding="utf-8") as f:
        raw = f.read()
    in_it_section = False
    for line in raw.splitlines():
        if "Integrations - IT" in line and line.strip().startswith("|"):
            in_it_section = True
            continue
        if not in_it_section:
            continue
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = cells[1:-1] if cells and cells[0] == "" and cells[-1] == "" else cells
        if len(cells) < 3:
            continue
        id_field = cells[0]
        comp_field = cells[1] if len(cells) > 1 else ""
        scope_field = cells[2] if len(cells) > 2 else ""
        # Stop when we hit another section header row
        if id_field == "" and looks_like_section_label(comp_field):
            in_it_section = False
            continue
        if id_field == "" and comp_field and not scope_field.strip():
            if (comp_field not in [s["name"] for s in it_systems]
                    and not looks_like_section_label(comp_field)
                    and not looks_like_req_id(comp_field)):
                it_systems.append({
                    "name": comp_field,
                    "scope_hint": "Integration target; vendor/protocol TBC",
                    "location": "Airport-wide",
                    "source": "Integrations - IT",
                })

    return {"vendors": dict(vendors), "it_systems": it_systems, "protocols": dict(protocols)}


# -----------------------------------------------------------------------------
# 5. Render the RTM as Markdown
# -----------------------------------------------------------------------------
def escape_md(cell):
    return str(cell).replace("|", "\\|").replace("\n", "<br>")


def main():
    rows = parse_register(REGISTER_FILE)
    out_lines = []

    out_lines.append("# Requirements Traceability Matrix")
    out_lines.append("")
    out_lines.append("**Airport Eye — Integrated Airport Digital Twin Platform**")
    out_lines.append("")
    out_lines.append("**Sources (user-selected):**")
    out_lines.append(f"- `{REGISTER_FILE}` — Final Requirements Register")
    out_lines.append(f"- `{ADDENDUM_FILE}` — Addendum A Use-Case Coverage Matrix")
    out_lines.append(f"- `{PROPOSAL_FILE}` — Consolidated Technical Proposal v12")
    out_lines.append("")
    out_lines.append("**Scope note:** This RTM maps every row of the Final Requirements Register to an Addendum A use case, an owner module/agent, a proposal deliverable package, and a milestone. Where a register row does not have a direct Addendum A counterpart, the mapping is marked *Inferred* and assigned to the most relevant umbrella use case. Mapping of individual OT/IT widget rows is by system family; the per-row mapping is retained for traceability.")
    out_lines.append("")
    out_lines.append("---")
    out_lines.append("")

    # Summary by group
    groups = defaultdict(int)
    for r in rows:
        groups[r["group"]] += 1

    out_lines.append("## 1. Register Row Count by Group")
    out_lines.append("")
    out_lines.append("| Group | Rows |")
    out_lines.append("|---|---|")
    for g, c in sorted(groups.items(), key=lambda x: -x[1]):
        out_lines.append(f"| {g} | {c} |")
    out_lines.append(f"| **Total** | **{len(rows)}** |")
    out_lines.append("")
    out_lines.append("---")
    out_lines.append("")

    # Addendum A use-case coverage summary
    case_rows = defaultdict(int)
    for r in rows:
        mapped = map_row(r)
        for case_name in mapped["cases"]:
            case_rows[case_name] += 1

    out_lines.append("## 2. Addendum A Use-Case Coverage Summary")
    out_lines.append("")
    out_lines.append("| Addendum A Use Case | Register Rows Mapped | Status |")
    out_lines.append("|---|---|---|")
    for case in ADDENDUM_CASES:
        count = case_rows.get(case["name"], 0)
        status = case["status"]
        out_lines.append(f"| {escape_md(case['name'])} | {count if count else '0 (gap)'} | {escape_md(status)} |")
    out_lines.append("")
    out_lines.append("---")
    out_lines.append("")

    # Full matrix grouped
    group_order = [
        "BIM / Geo DT",
        "OT/IT Integration",
        "DT Widget / Functional Requirement",
        "Simulation / What-If",
        "SAC / Smart City / IoT",
        "Asset Registry & Modeling",
        "AI Agents",
        "Non-Functional Requirements",
        "Platform / Protocol",
        "Common Functionality",
        "Testing / Environments",
        "Out of Scope",
        "Other",
    ]
    grouped = {g: [] for g in group_order}
    for r in rows:
        grouped.setdefault(r["group"], []).append(r)

    section_num = 1
    for g in group_order:
        if not grouped[g]:
            continue
        out_lines.append(f"## 3.{section_num}. {g}")
        section_num += 1
        out_lines.append("")
        out_lines.append(f"*{len(grouped[g])} register rows*")
        out_lines.append("")
        out_lines.append("| Register ID / Row | Component / Area | Requirement / Scope | Addendum A Use Case(s) | Owner Module / Agent | Proposal Package | Milestone | Mapping Basis |")
        out_lines.append("|---|---|---|---|---|---|---|---|")
        for r in grouped[g]:
            mapped = map_row(r)
            cases_str = "<br><br>".join([f"**{c}**" for c in mapped["cases"]])
            basis_str = "<br><br>".join(mapped["basis"])
            scope_short = (r["scope"][:300] + "...") if len(r["scope"]) > 300 else r["scope"]
            out_lines.append(
                f"| {escape_md(r['id'])} | {escape_md(r['component'])} | {escape_md(scope_short)} | {escape_md(cases_str)} | {escape_md(mapped['owner'])} | {escape_md(mapped['package'])} | {escape_md(mapped['milestone'])} | {escape_md(basis_str)} |"
            )
        out_lines.append("")

    out_lines.append("")
    out_lines.append("---")
    out_lines.append("")
    out_lines.append("## 4. Legend")
    out_lines.append("")
    out_lines.append("- **Mapping Basis = Direct**: the register row explicitly describes the Addendum A use case or a direct sub-requirement of it.")
    out_lines.append("- **Mapping Basis = Keyword**: a keyword in the register row matched an Addendum A use case name or data dependency.")
    out_lines.append("- **Mapping Basis = Group-level default**: no direct Addendum A use case was found; the row is traced to the umbrella use case that most logically consumes or enables it.")
    out_lines.append("- **Milestone codes**: MS1=Mo1, MS2=Mo3, MS3=Mo5, MS4=Mo7, MS5=Mo9, MS6=Mo9+90d. See proposal §4.1.2.")
    out_lines.append("- **Delivery phases in register**: Phase 1a = 0–3 months; Phase 1b = 4–6 months; Phase 1c = 7–9 months; Phase 2 = 12+ months.")
    out_lines.append("")
    out_lines.append("## 5. Important Caveats")
    out_lines.append("")
    out_lines.append("1. The mapping of widget/equipment rows is by **system family**, not by individual sensor. The register lists equipment counts (e.g., T3 FDAS 65,000 points); these are all traced to the same owner and use-case family rather than 65,000 separate rows.")
    out_lines.append("2. Rows tagged **Phase 2** in the register may still be base-scope in the proposal if they are part of the 9-month programme (e.g., BHS T1/T3, MRSS, WTP/STP). The package/milestone in this RTM follows the **proposal** milestone when the proposal explicitly covers the item.")
    out_lines.append("3. **T2 OT systems** are marked in the register as 'Doesn’t exist / Not Present / Upcoming'. The proposal treats T2 integration as Wave 3 with a dormant-binding fallback (§2.1.3, §2.5.6). The RTM reflects this as MS4/MS5 pending DIAL confirmation.")
    out_lines.append("4. Some register rows (e.g., ITOM, SAC, asset registry UI, curbside Phase-2 features) have **no direct Addendum A use case**; they are mapped to the closest umbrella use case and flagged as group-level defaults for the bidder to validate in the Mo1 workshop.")
    out_lines.append("5. **Integrations - IT data feeds** (UTAM, AODB, ADS-B, ARC, RMS, Kloudspot, XOVIS, PTM, GIS, SAP, VMS/CCTV, etc.) are treated as widget/simulation data inputs and mapped to **D-08** with the consuming Addendum A use case; only ITOM/Manage Engine and the OT/BMS integration rows remain in **D-09**.")
    out_lines.append("6. **BIM/Geo DT UI capability rows** (Desktop, Web, login/profile, exterior/navigation visualisation, layer selection) are mapped to **D-08 / MS4** as part of the deployed Digital Twin platform rather than to the BIM-model deliverables D-05/D-16/D-20.")
    out_lines.append("7. **Security-context guard**: stray mentions of CCTV/DFMD inside baggage, resource-master, or queue/retail widgets are prevented from over-mapping to the security use cases; only rows whose component or primary scope is genuinely security-related are traced to S&V use cases.")
    out_lines.append("8. **Component labels** for register rows whose component cell was empty, contained a prior requirement ID, or contained a section header have been inferred from the same ID family; section-header values are no longer used as component names. Validate these in the Mo1 workshop.")
    out_lines.append("")

    # Vendor / protocol inventory
    inventory = extract_vendors_protocols(rows)
    out_lines.append("## 6. Integration Vendor & Protocol Inventory")
    out_lines.append("")
    out_lines.append("### 6.1. OT System Vendors / OEMs")
    out_lines.append("")
    out_lines.append("| Vendor / OEM | System(s) | Location(s) | Register Source(s) |")
    out_lines.append("|---|---|---|---|")
    for vendor, data in sorted(inventory["vendors"].items(), key=lambda x: x[0].upper()):
        systems = ", ".join(sorted(data["systems"]))
        locs = ", ".join(sorted(data["locations"]))
        sources = ", ".join(sorted(data["sources"]))
        out_lines.append(f"| {escape_md(vendor)} | {escape_md(systems)} | {escape_md(locs)} | {escape_md(sources)} |")
    out_lines.append("")
    out_lines.append("### 6.2. IT Data-Feed Systems")
    out_lines.append("")
    out_lines.append("| IT System / Feed | Scope Hint | Location | Register Source |")
    out_lines.append("|---|---|---|---|")
    for item in inventory["it_systems"]:
        out_lines.append(
            f"| {escape_md(item['name'])} | {escape_md(item['scope_hint'])} | {escape_md(item['location'])} | {escape_md(item['source'])} |"
        )
    out_lines.append("")
    out_lines.append("### 6.3. Protocols & Standards")
    out_lines.append("")
    out_lines.append("| Protocol / Standard | Location(s) | Register Source(s) |")
    out_lines.append("|---|---|---|")
    for proto, data in sorted(inventory["protocols"].items(), key=lambda x: x[0].upper()):
        locs = ", ".join(sorted(data["locations"]))
        sources = ", ".join(sorted(data["sources"]))
        out_lines.append(f"| {escape_md(proto)} | {escape_md(locs)} | {escape_md(sources)} |")
    out_lines.append("")
    out_lines.append("---")
    out_lines.append("")
    out_lines.append("*End of Requirements Traceability Matrix*")

    OUT_FILE.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Wrote RTM to {OUT_FILE} ({len(rows)} register rows mapped).")


if __name__ == "__main__":
    main()
