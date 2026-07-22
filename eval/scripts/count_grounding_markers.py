#!/usr/bin/env python3
"""Count [GROUNDED: ...] vs [ASSERTION: ...] markers across section-drafter output.

Grounding ratio = grounded / (grounded + assertion). Higher is better — it means
more of the draft's substantive claims are traced to source evidence rather than
asserted without support.

Usage:
    count_grounding_markers.py <file_or_glob> [<file_or_glob> ...]
    count_grounding_markers.py --json <file_or_glob> ...
"""
import re
import sys
import json
import glob

GROUNDED_RE = re.compile(r"\[GROUNDED:")
ASSERTION_RE = re.compile(r"\[ASSERTION:")


def count_file(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    grounded = len(GROUNDED_RE.findall(text))
    assertion = len(ASSERTION_RE.findall(text))
    return {"file": path, "grounded": grounded, "assertion": assertion}


def main(argv):
    as_json = "--json" in argv
    patterns = [a for a in argv if a != "--json"]
    if not patterns:
        print(__doc__)
        return 1

    paths = []
    for p in patterns:
        matches = glob.glob(p)
        paths.extend(matches if matches else [p])

    per_file = [count_file(p) for p in paths]
    total_grounded = sum(r["grounded"] for r in per_file)
    total_assertion = sum(r["assertion"] for r in per_file)
    denom = total_grounded + total_assertion
    ratio = round(total_grounded / denom, 3) if denom else None

    result = {
        "files": per_file,
        "total_grounded": total_grounded,
        "total_assertion": total_assertion,
        "grounding_ratio": ratio,
    }

    if as_json:
        print(json.dumps(result, indent=2))
        return 0

    for r in per_file:
        print(f"{r['file']:<60} grounded={r['grounded']:>4} assertion={r['assertion']:>4}")
    print("-" * 80)
    print(f"TOTAL grounded={total_grounded} assertion={total_assertion} grounding_ratio={ratio}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
