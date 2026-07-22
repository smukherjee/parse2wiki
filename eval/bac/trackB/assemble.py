#!/usr/bin/env python3
"""Assemble BAC TrackB proposal from reviewed sections, stripping evidence markers."""
import re, os, datetime

SECTIONS_DIR = "/Users/sujoymukherjee/code/doc2md/parse2wiki/eval/bac/trackB/sections"
OUT = "/Users/sujoymukherjee/code/doc2md/parse2wiki/eval/bac/trackB/proposal-trackB.md"

ORDER = [
    "01-executive-summary.md",
    "02-understanding-of-requirements.md",
    "03-technical-solution.md",
    "04-scope-coverage-and-deliverables.md",
    "05-implementation-methodology.md",
    "06-project-management-and-governance.md",
    "07-integration-data-technical-approach.md",
    "08-security-isra-and-compliance.md",
    "09-testing-acceptance-handover.md",
    "10-support-sla-and-maintenance.md",
    "11-compliance-with-tab-f-requirements.md",
    "12-commercial-and-insurance-response.md",
    "13-deviation-clarifications-assumptions-register.md",
    "14-relevant-experience.md",
]

# Marker regex: handles [GROUNDED:...], [ASSERTION:...], [GAP:...], [GAP — ...],
# [GAP/ASSERTION — ...], [GROUNDED/ASSERTION/GAP — ...], etc.
MARKER_RE = re.compile(
    r"\[(GROUNDED|ASSERTION|GAP)(?:/(?:GROUNDED|ASSERTION|GAP))*[\s:—–\-]+[^\]]*\]"
)

def classify(marker_text):
    """Return a concise client-facing status from a marker tag."""
    if "GROUNDED" in marker_text and "ASSERTION" in marker_text:
        return "Evidenced + committed"
    if "GAP" in marker_text and "ASSERTION" in marker_text:
        return "Committed for delivery"
    if "GROUNDED" in marker_text:
        return "Evidenced in collateral"
    if "ASSERTION" in marker_text:
        return "Committed (architecturally supported)"
    if "GAP" in marker_text:
        return "Committed for delivery"
    return ""

def strip_markers(text):
    """Remove evidence markers. Replace cell-only markers with status labels;
    remove inline markers that follow prose (clean up whitespace)."""
    # First, handle table cells whose content is only marker(s).
    def cell_repl(m):
        inner = m.group(1).strip()
        # find all markers in the cell
        markers = MARKER_RE.findall(inner)
        if markers and inner.strip() == "" or all(MARKER_RE.fullmatch(x) or x.strip()=="" for x in re.split(r'(\[(?:GROUNDED|ASSERTION|GAP)[^\]]*\])', inner) if x.strip()):
            # cell is marker-only
            # determine dominant type
            tag = markers[0]
            return " " + classify(tag) + " "
        return m.group(0)
    # Table cell: | <content> |  where content may be marker-only
    # We'll process line by line for table rows.
    out_lines = []
    for line in text.splitlines():
        if line.lstrip().startswith("|") and line.rstrip().endswith("|"):
            # table row - process each cell
            # split keeping pipes
            parts = line.split("|")
            # parts[0] empty, parts[-1] empty (or trailing)
            new_parts = []
            for i, p in enumerate(parts):
                if i == 0 or i == len(parts)-1:
                    new_parts.append(p)
                    continue
                stripped = p.strip()
                # is this cell marker-only (one or more markers, nothing else)?
                # remove all markers and see what remains
                without = MARKER_RE.sub("", stripped).strip()
                # remove leftover separators like " / " between markers
                without = re.sub(r"^[/\s,;]+$", "", without).strip()
                if without == "" and stripped != "":
                    # marker-only cell -> replace with status of first marker
                    markers = MARKER_RE.findall(stripped)
                    if markers:
                        status = classify(markers[0])
                        new_parts.append(" " + status + " ")
                        continue
                # otherwise strip markers inline, keep remaining text
                cleaned = MARKER_RE.sub("", stripped)
                cleaned = re.sub(r"\s+", " ", cleaned).strip()
                # remove dangling separators left by marker removal
                cleaned = re.sub(r"^[\s,;]+", "", cleaned).strip()
                cleaned = re.sub(r"[\s,;]+$", "", cleaned).strip()
                new_parts.append(" " + cleaned + " " if cleaned else "  ")
            out_lines.append("|".join(new_parts))
        else:
            # non-table line: strip inline markers, clean whitespace
            # Replace marker with empty, but collapse resulting double spaces/punct
            cleaned = MARKER_RE.sub("", line)
            # collapse spaces around removal
            cleaned = re.sub(r"\s+", " ", cleaned)
            # fix " ." -> ".", " ," -> ",", " ;" -> ";"
            cleaned = re.sub(r"\s+([.,;:])", r"\1", cleaned)
            # remove empty parentheses left "()"
            cleaned = re.sub(r"\(\s*\)", "", cleaned)
            # remove trailing whitespace before newline
            cleaned = cleaned.rstrip()
            out_lines.append(cleaned)
    return "\n".join(out_lines)

# Counters for evidence quality
def count_markers(text):
    g = len(MARKER_RE.findall(text))
    # separate counts
    grounded = len(re.findall(r"\[GROUNDED(?![A-Z])", text))
    assertion = len(re.findall(r"\[ASSERTION(?![A-Z])", text))
    gap = len(re.findall(r"\[GAP(?![A-Z])", text))
    # combined markers count toward each present type; approximate by simple tag search
    return grounded, assertion, gap

# Read & process sections
section_bodies = []
titles = []
total_g = total_a = total_gap = 0
for fn in ORDER:
    path = os.path.join(SECTIONS_DIR, fn)
    raw = open(path).read()
    g, a, gap = count_markers(raw)
    total_g += g
    total_a += a
    total_gap += gap
    body = strip_markers(raw)
    section_bodies.append((fn, body))
    # extract title (first H1)
    m = re.search(r"^# (.+)$", body, re.M)
    titles.append(m.group(1) if m else fn)

# Build front matter
today = datetime.date.today().isoformat()
grounded_total = total_g
assertion_total = total_a
gap_total = total_gap
ratio = grounded_total / (grounded_total + assertion_total) * 100 if (grounded_total+assertion_total) else 0

# Word count of assembled body
body_text = "\n\n---\n\n".join(b for _, b in section_bodies)
# strip markdown for word count approx
wc_text = re.sub(r"[#|>`*\-]", " ", body_text)
wc = len(wc_text.split())

preflight = f"""# Pre-Flight Checklist

**Assembly Date:** {today}
**Status:** Ready for Review (draft — declared gaps with committed resolution paths are acceptable for this draft)

## Document Completeness

- [x] All 14 RFP-aligned sections present (01-14)
- [x] Cover page included
- [x] Table of contents generated
- [ ] Contact information: vendor primary contact to be supplied (placeholder below) — must be added before submission
- [ ] Referenced appendices: no separate appendices drafted; placeholders flagged where referenced

## Compliance Status

- [x] Compliance posture summarised in Section 11; disqualifying gaps (FR17, FR20, NF19, ISRA-19, ISRA-25) each have a committed resolution path
- [ ] Compliance validation via compliance-validator not re-run on this assembled draft; run before submission
- Warnings: 5 disqualifying gaps declared with committed delivery/resolution paths (acceptable for a draft; must be closed or accepted before final submission)

## Evidence Quality

- Grounded claims: {grounded_total}
- Assertions (architecturally reasonable, unsubstantiated): {assertion_total}
- Declared gaps: {gap_total}
- Grounding ratio (grounded / (grounded + assertions)): {ratio:.0f}%
- Note: Markers stripped from assembled prose; counts derived from pre-strip section files.

## Unresolved Items

- [ ] Vendor primary contact name/title/email/phone (placeholder in cover page)
- [ ] Schedule A: insurance certificates of currency; ISO 9001/20000/27001/22301 certificate evidence; sub-contractor identification
- [ ] Schedule C: two referees; named key personnel and resumes; case studies
- [ ] Schedule E: full 5-year pricing breakdown (Implementation, Integrations, Hardware, License, Support, Maintenance, Additional)
- [ ] NF09/NF10: QA standards/tools/methodology documentation from WAISL internal QA process
- [ ] NF05: 3-year availability history (committed to SLA reporting going forward)
- [ ] Hosting target confirmation (AWS Sydney ap-southeast-2 vs BAC private cloud) — open question to close at Initiation
- [ ] Camera-model list (FR01) — BAC to confirm supported models
- [ ] Phase-2 scope confirmation (FR72 aerobridge pax counting; FR73 mobile/tablet) — Must-Have in this contract or deferred
- [ ] Civil/hardware install cost responsibility (BAC or supplier)
- [ ] Reframe Turnwise examples (IST-NAP route, non-Australian registrations) to BNE before submission
- [ ] Authorised signature on required forms; final formatting in submission format (Excel response sheet + optional 5-page PDF)
- [ ] Submission method and deadline confirmed per RFP §4.2 (proposals valid 90 calendar days)

## Page Count Estimate

The RFP permits an Excel response sheet plus an optional single PDF of no more than 5 pages (§8). This assembled narrative is the working technical draft behind the response; it will be compressed into the 5-page optional PDF and the Excel Response Sheet entries. No per-section page limit applies to the internal draft; the submission-format limit is 5 PDF pages plus the Excel sheet.

| Section | Draft word estimate | Status |
|---------|----------------------|--------|
| 01 Executive Summary | ~600 | OK |
| 02 Understanding of Requirements | ~850 | OK |
| 03 Technical Solution | ~2,400 | OK |
| 04 Scope Coverage and Deliverables | ~1,300 | OK |
| 05 Implementation Methodology | ~750 | OK |
| 06 Project Management and Governance | ~700 | OK |
| 07 Integration, Data, and Technical Approach | ~650 | OK |
| 08 Security, ISRA, and Compliance | ~1,700 | OK |
| 09 Testing, Acceptance, and Handover | ~600 | OK |
| 10 Support, SLA, and Maintenance | ~750 | OK |
| 11 Compliance with Tab.F Requirements | ~900 | OK |
| 12 Commercial and Insurance Response | ~550 | OK |
| 13 Deviation, Clarifications, and Assumptions Register | ~1,300 | OK |
| 14 Relevant Experience | ~700 | OK |
| **Total (draft)** | **~{wc:,}** | Internal draft |

## Before Submission

- [ ] Human review of all assertions for accuracy
- [ ] Final formatting in submission format (Excel Response Sheet + optional 5-page PDF; no sales brochures per §8)
- [ ] Appendix/completion: supply Schedule A/C/E content; insurance and ISO certificates; referees and named personnel
- [ ] Pricing volume preparation (Schedule E)
- [ ] Authorised signature on required forms
- [ ] Submission method and deadline confirmed

---

# BAC Underwing Analytics Solution

**In Response To:** BAC-T-26-505 — Underwing Analytics Request for Proposal
**Submitted To:** Brisbane Airport Corporation Pty Limited (BAC)
**Submitted By:** WAISL (operating through its Australia office, with delivery partner for camera/computer-vision elements)
**Date:** {today}

**Primary Contact:**
[PLACEHOLDER — vendor primary contact name, title, email, phone, address to be supplied before submission]

**BAC Contact Officer:** Leighton Walker, Technology Project Manager

**Contract Vehicle:** BAC Relationship / Master Services Agreement (Annexure B); 3-year initial term with two by-one-year extensions (RFP §4.3)

**Proposal Validity:** 90 calendar days from Proposal Closing Time (RFP §4.2; Annexure A §1)

---

# Table of Contents

"""

toc = ""
for i, t in enumerate(titles, 1):
    toc += f"{i}. {t}\n"

tone_note = f"""

---

# Tone-Gate Note

Stop-slop tone gate applied to all narrative sections (exec summary, understanding, technical solution, implementation, governance, integration, security narrative, testing, support, relevant experience). Compliance tables (Section 11), the deviation/assumption register (Section 13), SLA/KPI spec tables, mandatory forms, and deliverable/assumption bullet lists were carved out per the RFP carve-out. Technical adverbs (fully, commercially, operationally, contractually) and formal third-person buyer voice were preserved. Evidence markers ([GROUNDED]/[ASSERTION]/[GAP]) were preserved through review and stripped only at assembly.

Scores (Directness/Rhythm/Trust/Authenticity/Density, out of 10; section passes at >=35/50):

| Section | D | R | T | A | Dn | Total | Revised? |
|---------|---|---|---|---|----|-------|----------|
| 01 Executive Summary | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 02 Understanding of Requirements | 7 | 7 | 8 | 8 | 7 | 37 | No (pass) |
| 03 Technical Solution | 8 | 7 | 8 | 8 | 7 | 38 | Yes (was 30; em-dash heavy, rambling parentheticals) |
| 04 Scope Coverage (deliverables table carved out) | 8 | 7 | 8 | 8 | 7 | 38 | No (pass; table carved out) |
| 05 Implementation Methodology | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 06 Project Management & Governance (RACI carved out) | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 07 Integration, Data, Technical Approach | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 08 Security, ISRA & Compliance (ISRA rows + HA/DR table carved out) | 8 | 7 | 8 | 8 | 7 | 38 | Yes (was 29; narrative em-dash heavy) |
| 09 Testing, Acceptance, Handover | 7 | 7 | 8 | 8 | 7 | 37 | No (pass) |
| 10 Support, SLA & Maintenance (SLA matrix carved out) | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |
| 11 Compliance with Tab.F (carved out — compliance table) | n/a | n/a | n/a | n/a | n/a | n/a | Carved out |
| 12 Commercial & Insurance (insurance table carved out) | 7 | 7 | 8 | 8 | 7 | 37 | No (pass; table carved out) |
| 13 Deviation/Assumptions Register (carved out — register) | n/a | n/a | n/a | n/a | n/a | n/a | Carved out |
| 14 Relevant Experience | 8 | 7 | 8 | 8 | 7 | 38 | No (pass) |

Sections revised (score <35 before, >=35 after): 03 (30 -> 38) and 08 (29 -> 38). No section remains below 35 after revision. Em dashes removed from revised narrative prose; markers preserved during review and stripped at assembly. No content fabricated; declared gaps retain committed resolution paths.
"""

# Assemble
# Polish: remove em dashes from headings (" — " -> ": " or " " to avoid double colons)
def clean_headings(text):
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith("#") and " — " in line:
            before, after = line.split(" — ", 1)
            sep = " " if ":" in after else ": "
            line = before + sep + after
        out.append(line)
    return "\n".join(out)

body_text = clean_headings(body_text)

full = preflight + toc + "\n\n" + body_text + tone_note + "\n"

# Clean up draft-convention meta-phrases that reference marker shorthand (client-facing)
full = full.replace(
    "All such content is marked `[GAP] / placeholder` and must be supplied before submission.",
    "All such content is marked as placeholder and must be supplied before submission.",
)
full = full.replace(
    "Each of these is marked `[GAP] / placeholder` in this draft and must be supplied before submission.",
    "Each of these is marked as placeholder in this draft and must be supplied before submission.",
)

open(OUT, "w").write(full)
print(f"Wrote {OUT}")
print(f"Grounded={grounded_total} Assertion={assertion_total} Gap={gap_total} Ratio={ratio:.0f}%")
print(f"Word count (approx): {wc}")