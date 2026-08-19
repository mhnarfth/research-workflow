#!/usr/bin/env python3
"""Assemble exactly the framework files a change touches, into one pasteable file.

Run from the research-workflow repo root.

    python tools/bundle_context.py --preset tweak-phase P07
    python tools/bundle_context.py --preset add-phase
    python tools/bundle_context.py --preset bundle-format
    python tools/bundle_context.py --files WORKFLOW.md phases/P07-execution
    python tools/bundle_context.py --all

Writes context.md and prints a token estimate. Paste or attach it, then run the
P19 opening message.

The whole repo is roughly 40k tokens. Loading all of it for a three-file change
puts you back in the big-context problem this framework exists to avoid — so
use the narrowest preset that covers the change, and always grep to confirm:

    grep -rn "<the thing you're changing>" .
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

TOP = [
    "README.md", "QUICKSTART.md", "WORKFLOW.md", "MAINTENANCE.md",
    "PROMPTING.md", "READING.md", "CHANGELOG.md",
    "LEDGER-tooling.md", "LEDGER-reading.md", "LEDGER-improvements.md",
]

PRESETS = {
    # change one phase's wording, prompts, or checklist
    "tweak-phase":   {"files": ["phases/README.md"], "phase_arg": True},
    # add, remove, or merge phases
    "add-phase":     {"files": ["WORKFLOW.md", "QUICKSTART.md",
                                "phases/README.md", "phases/P07-execution"]},
    # change a standing rule
    "standing-rule": {"files": ["WORKFLOW.md", "QUICKSTART.md",
                                "MAINTENANCE.md", "phases/README.md"]},
    # change the handoff bundle format or write modes -> every closing.md
    "bundle-format": {"files": ["phases/README.md", "tools/README.md",
                                "tools/apply_handoff.py"],
                      "glob": "phases/*/closing.md"},
    # change the coaching clause -> every opening.md
    "coaching":      {"files": ["phases/README.md"],
                      "glob": "phases/*/opening.md"},
    # change scheduling ratios
    "schedule":      {"files": ["WORKFLOW.md", "QUICKSTART.md",
                                "phases/P03-venue-calibration"]},
    # docs, ledgers, reading list
    "top-level":     {"files": TOP},
}

SKIP_SUFFIX = {".pyc", ".zip", ".png", ".pdf"}
SKIP_NAME = {".gitkeep", "context.md"}


def collect(paths: list[str], globs: list[str]) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            out += sorted(f for f in path.rglob("*") if f.is_file())
        elif path.is_file():
            out.append(path)
        else:
            print(f"  ! not found, skipping: {p}", file=sys.stderr)
    for g in globs:
        out += sorted(Path(".").glob(g))
    seen, uniq = set(), []
    for f in out:
        if f in seen or f.name in SKIP_NAME or f.suffix in SKIP_SUFFIX:
            continue
        seen.add(f)
        uniq.append(f)
    return uniq


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--preset", choices=sorted(PRESETS))
    ap.add_argument("phase", nargs="?",
                    help="phase prefix for tweak-phase, e.g. P07")
    ap.add_argument("--files", nargs="*", default=[],
                    help="explicit files or directories")
    ap.add_argument("--all", action="store_true", help="the whole repo")
    ap.add_argument("-o", "--out", default="context.md")
    args = ap.parse_args()

    paths: list[str] = list(args.files)
    globs: list[str] = []

    if args.all:
        paths += TOP + ["phases", "tools"]
    elif args.preset:
        spec = PRESETS[args.preset]
        paths += spec["files"]
        if "glob" in spec:
            globs.append(spec["glob"])
        if spec.get("phase_arg"):
            if not args.phase:
                print("tweak-phase needs a phase prefix, e.g. P07",
                      file=sys.stderr)
                return 1
            matches = sorted(Path("phases").glob(f"{args.phase}*"))
            if not matches:
                print(f"no phase folder matching {args.phase}*", file=sys.stderr)
                return 1
            paths += [str(m) for m in matches]
    elif not paths:
        ap.print_help()
        return 1

    files = collect(paths, globs)
    if not files:
        print("nothing collected", file=sys.stderr)
        return 1

    chunks = [
        "# Framework context bundle\n",
        "These are the CURRENT contents of the framework files relevant to "
        "this change.\nDo not propose edits to files that are not listed here "
        "— name them as follow-up instead.\n",
        f"Files included ({len(files)}):\n",
        *(f"- `{f}`\n" for f in files),
        "\n---\n",
    ]
    for f in files:
        try:
            body = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"  ! not text, skipping: {f}", file=sys.stderr)
            continue
        fence = "```python" if f.suffix == ".py" else "```markdown"
        chunks.append(f"\n## FILE: {f}\n\n{fence}\n{body}\n```\n")

    text = "".join(chunks)
    Path(args.out).write_text(text, encoding="utf-8")

    chars = len(text)
    print(f"\n  {len(files)} files -> {args.out}")
    print(f"  {chars:,} chars  (~{chars // 4:,} tokens)\n")
    if chars // 4 > 60_000:
        print("  This is large. Consider a narrower preset.\n")
    print("  Next: grep to confirm nothing was missed —")
    print('      grep -rn "<the thing you are changing>" . --include="*.md"\n')
    return 0


if __name__ == "__main__":
    sys.exit(main())
