#!/usr/bin/env python3
"""Extract Pass/Partial/Fail/Ambiguous/Blocking counts from a compliance-validator report.

The compliance-validator skill's Step 11 summary table format varies slightly between
runs (e.g. `| Verdict | Count | Note |` vs `| Metric | Count |`), so this parses by
keyword rather than assuming a fixed table shape.

Usage:
    parse_compliance_report.py <compliance-report.md> [<compliance-report.md> ...]
    parse_compliance_report.py --json <compliance-report.md> ...
"""
import re
import sys
import json

VERDICT_KEYWORDS = {
    "pass": r"\bpass\b",
    "partial": r"\bpartial\b",
    "fail": r"\bfail\b",
    "ambiguous": r"\bambiguous\b",
}
BLOCKING_KEYWORDS = r"\bblocking\b"

ROW_RE = re.compile(r"^\|\s*\**([A-Za-z ()/\-]+?)\**\s*\|\s*\**(\d+)\**\s*\|", re.IGNORECASE)


def parse_report(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    counts = {"pass": None, "partial": None, "fail": None, "ambiguous": None, "blocking": None}

    # Only scan markdown table rows to avoid matching prose mentions of these words.
    for line in lines:
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        label, value = m.group(1).strip().lower(), int(m.group(2))
        if counts["blocking"] is None and re.search(BLOCKING_KEYWORDS, label):
            counts["blocking"] = value
            continue
        for key, pattern in VERDICT_KEYWORDS.items():
            if counts[key] is None and re.search(pattern, label):
                counts[key] = value
                break

    total_checked = None
    m = re.search(r"(\d+)\s+(?:comparable\s+)?requirements?(?:\s*/\s*requirement groups)?\s+checked", text, re.IGNORECASE)
    if m:
        total_checked = int(m.group(1))

    known = [v for v in (counts["pass"], counts["partial"], counts["fail"], counts["ambiguous"]) if v is not None]
    total = total_checked if total_checked is not None else (sum(known) if known else None)

    pass_rate = None
    if total and counts["pass"] is not None:
        pass_rate = round(counts["pass"] / total, 3)

    return {
        "file": path,
        "pass": counts["pass"],
        "partial": counts["partial"],
        "fail": counts["fail"],
        "ambiguous": counts["ambiguous"],
        "blocking": counts["blocking"],
        "total_checked": total,
        "pass_rate": pass_rate,
    }


def main(argv):
    as_json = "--json" in argv
    paths = [a for a in argv if a != "--json"]
    if not paths:
        print(__doc__)
        return 1

    results = [parse_report(p) for p in paths]

    if as_json:
        print(json.dumps(results, indent=2))
        return 0

    header = f"{'file':<50} {'pass':>5} {'partial':>8} {'fail':>5} {'ambig':>6} {'block':>6} {'total':>6} {'pass_rate':>9}"
    print(header)
    print("-" * len(header))
    for r in results:
        print(
            f"{r['file'][-50:]:<50} {str(r['pass']):>5} {str(r['partial']):>8} "
            f"{str(r['fail']):>5} {str(r['ambiguous']):>6} {str(r['blocking']):>6} "
            f"{str(r['total_checked']):>6} {str(r['pass_rate']):>9}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
