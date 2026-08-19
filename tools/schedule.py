#!/usr/bin/env python3
"""Where you are against the reverse schedule. Run from the project repo root.

    python tools/schedule.py --start 2026-06-15 --deadline 2026-08-12

Or put those two dates in docs/VENUE.md as:

    START: 2026-06-15
    DEADLINE: 2026-08-12

Ratios of the runway (WORKFLOW.md §5). Only the submission buffer has a hard
floor: 24 hours.

Prints where you are. Makes no recommendation and cuts nothing — scope
decisions are yours.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

BLOCKS = [
    ("Setup (P01-P05)",                    0.20),
    ("Execution + red team (P06-P08)",     0.40),
    ("Paper planning + drafting (P09-P10)", 0.25),
    ("Adversarial + revision (P11)",       0.08),
    ("Submission buffer (P12)",            0.05),
]


def from_venue() -> tuple[str | None, str | None]:
    p = Path("docs/VENUE.md")
    if not p.exists():
        return None, None
    t = p.read_text(encoding="utf-8")
    s = re.search(r"START:\s*(\d{4}-\d{2}-\d{2})", t)
    d = re.search(r"DEADLINE:\s*(\d{4}-\d{2}-\d{2})", t)
    return (s.group(1) if s else None, d.group(1) if d else None)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--start")
    ap.add_argument("--deadline")
    a = ap.parse_args()

    vs, vd = from_venue()
    start_s, dl_s = a.start or vs, a.deadline or vd
    if not (start_s and dl_s):
        print("Need --start and --deadline, or START:/DEADLINE: lines in "
              "docs/VENUE.md", file=sys.stderr)
        return 1

    start = datetime.strptime(start_s, "%Y-%m-%d").date()
    deadline = datetime.strptime(dl_s, "%Y-%m-%d").date()
    today = date.today()
    runway = (deadline - start).days
    if runway <= 0:
        print("Deadline is not after the start date.", file=sys.stderr)
        return 1

    print(f"\n  {start} -> {deadline}   ({runway} days)")
    print(f"  today: {today}\n")

    cursor, rows = start, []
    for name, share in BLOCKS:
        days = max(1, round(runway * share))
        end = cursor + timedelta(days=days)
        if name.startswith("Submission buffer"):
            end = min(end, deadline)
            if (deadline - cursor).days < 1:
                cursor = deadline - timedelta(days=1)   # 24h floor
                end = deadline
        rows.append((name, cursor, end))
        cursor = end

    width = max(len(n) for n, _, _ in rows)
    for name, s, e in rows:
        if today > e:
            mark, note = "done", ""
        elif today >= s:
            left = (e - today).days
            mark, note = ">> NOW", f"  ({left} day{'s' if left != 1 else ''} left in this block)"
        else:
            mark, note = "", ""
        print(f"  {name:<{width}}  {s} -> {e}  {mark}{note}")

    left = (deadline - today).days
    elapsed = (today - start).days
    pct = int(100 * elapsed / runway) if runway else 0
    print(f"\n  {left} day{'s' if left != 1 else ''} to deadline "
          f"({pct}% of runway elapsed)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
