#!/usr/bin/env python3
"""Pre-release safety scan. Run from the PRIVATE repo root before P12.

    python tools/preflight.py

Reports only. Every finding is a judgement call and the decision is yours —
this exists so nothing reaches a public repo unexamined, not to block you.

Checks
  1. Real filesystem paths in tracked source
  2. Codenames resolving to real entity names (from local_paths.py)
  3. Credential-shaped strings
  4. Large binaries and data formats invertible to restricted data
  5. Figures missing their figdata JSON (breaks restyling)
  6. Notebooks staged for commit
  7. local_paths.py not ignored
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

PATH_PATTERNS = [r"/mnt/", r"/work/", r"/home/[a-z]", r"C:\\\\Users"]
CRED_PATTERNS = [
    r"(?i)\b(api[_-]?key|secret|password|token)\s*[=:]\s*['\"][^'\"]{8,}",
    r"gh[pousr]_[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
]
RISKY_SUFFIX = {".npz", ".npy", ".pt", ".pth", ".ckpt", ".h5", ".pkl", ".joblib"}
TEXT_SUFFIX = {".py", ".md", ".txt", ".yml", ".yaml", ".json", ".tex",
               ".cfg", ".toml", ".sh", ".bib"}
SIZE_WARN = 1_000_000  # 1 MB


def tracked() -> list[Path]:
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
    if out.returncode != 0:
        print("Not a git repository.", file=sys.stderr)
        sys.exit(1)
    return [Path(p) for p in out.stdout.split("\n") if p]


def real_names() -> list[str]:
    """Entity names from the gitignored local_paths.py, to grep for."""
    p = Path("config/local_paths.py")
    if not p.exists():
        return []
    names: list[str] = []
    for m in re.finditer(r"['\"]([^'\"]{3,})['\"]\s*:\s*['\"]([^'\"]{3,})['\"]",
                         p.read_text(encoding="utf-8")):
        names.append(m.group(2))
    return [n for n in names if not n.startswith("/")]


def main() -> int:
    files = tracked()
    findings: list[tuple[str, str]] = []
    notes: list[str] = []

    secrets = real_names()
    if secrets:
        notes.append(f"checking {len(secrets)} real entity name(s) from local_paths.py")
    else:
        notes.append("no ENTITY_NAMES found in config/local_paths.py "
                     "(fine if this project has nothing to anonymize)")

    for f in files:
        if f.suffix in RISKY_SUFFIX:
            findings.append(("DATA", f"{f} — invertible/restricted format, should not be tracked"))
        try:
            if f.exists() and f.stat().st_size > SIZE_WARN:
                findings.append(("SIZE", f"{f} — {f.stat().st_size // 1000} KB"))
        except OSError:
            pass
        if f.suffix == ".ipynb":
            findings.append(("NOTEBOOK", f"{f} — commit the .py instead"))
        if f.suffix not in TEXT_SUFFIX:
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for pat in PATH_PATTERNS:
                if re.search(pat, line):
                    findings.append(("PATH", f"{f}:{i} — {line.strip()[:90]}"))
                    break
            for pat in CRED_PATTERNS:
                if re.search(pat, line):
                    findings.append(("CREDENTIAL", f"{f}:{i} — possible secret"))
                    break
            for name in secrets:
                if name.lower() in line.lower():
                    findings.append(("REAL NAME", f"{f}:{i} — '{name}' appears in tracked source"))
                    break

    figs = {p.stem for p in Path("results/figures").glob("*.pdf")}
    data = {p.stem for p in Path("results/figdata").glob("*.json")}
    for missing in sorted(figs - data):
        findings.append(("FIGDATA", f"{missing}.pdf has no figdata JSON — cannot be restyled"))

    ign = subprocess.run(["git", "check-ignore", "config/local_paths.py"],
                         capture_output=True, text=True)
    if Path("config/local_paths.py").exists() and ign.returncode != 0:
        findings.append(("CRITICAL", "config/local_paths.py is NOT gitignored"))

    print(f"\n  preflight — {len(files)} tracked files")
    for n in notes:
        print(f"  note: {n}")

    if not findings:
        print("\n  Nothing flagged.\n")
        return 0

    print(f"\n  {len(findings)} item(s) to review:\n")
    order = ["CRITICAL", "REAL NAME", "CREDENTIAL", "DATA", "PATH",
             "NOTEBOOK", "FIGDATA", "SIZE"]
    for kind in order:
        rows = [m for k, m in findings if k == kind]
        if rows:
            print(f"  [{kind}]")
            for m in rows[:20]:
                print(f"    {m}")
            if len(rows) > 20:
                print(f"    ... and {len(rows) - 20} more")
            print()

    print("  These are findings, not errors. Decide each one yourself.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
