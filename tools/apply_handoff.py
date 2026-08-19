#!/usr/bin/env python3
"""Apply a handoff bundle produced by a phase's closing prompt.

Usage:
    git status                              # MUST be clean
    python tools/apply_handoff.py bundle.md
    git diff                                # review what changed
    git add -A && git commit -m "..." && git push
    # or, to undo everything:
    git checkout .

The invariant that makes this safe: CLEAN TREE BEFORE, `git checkout .` AFTER.
One command undoes any mess.

This script writes files. It never commits.

Bundle format
-------------
    === FILE: <path> | <MODE> ===
    <content>
    === END ===

    === HANDOFF: <phase> ===
    <narrative>
    === END ===

    === META: <phase> ===
    <workflow notes>
    === END ===

    === COMMIT ===
    <one-line message>
    === END ===

MODE is one of:
    CREATE                      file must not exist
    REPLACE                     file must exist; rewritten whole
    APPEND                      appended to the end
    APPEND_UNDER: ## Heading    inserted under a named heading
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

BLOCK = re.compile(
    r"^=== (FILE|HANDOFF|META|COMMIT):?\s*(.*?)\s*===\s*$\n(.*?)^=== END ===\s*$",
    re.MULTILINE | re.DOTALL,
)


class BundleError(Exception):
    pass


def git(*args: str) -> str:
    out = subprocess.run(
        ["git", *args], capture_output=True, text=True, check=False
    )
    return out.stdout.strip()


def require_clean_tree() -> None:
    if not Path(".git").is_dir():
        raise BundleError(
            "Not a git repository. Run this from the repo root.\n"
            "Without git there is no undo, and this script will not run."
        )
    if git("status", "--porcelain"):
        raise BundleError(
            "Working tree is dirty. Commit or stash first, so `git diff`\n"
            "shows only what this script changed and `git checkout .` undoes it.\n\n"
            "    git add -A && git commit -m \"wip\"\n"
        )


def parse(text: str) -> list[tuple[str, str, str]]:
    blocks = [(k, h.strip(), b) for k, h, b in BLOCK.findall(text)]
    if not blocks:
        raise BundleError(
            "No blocks found. Every block must look like:\n\n"
            "    === FILE: docs/NOTES.md | APPEND ===\n"
            "    ...content...\n"
            "    === END ===\n"
        )
    return blocks


def split_header(header: str) -> tuple[str, str, str | None]:
    """'docs/NOTES.md | APPEND_UNDER: ## Extensions' -> (path, mode, heading)"""
    if "|" not in header:
        raise BundleError(f"FILE block header missing '| MODE': {header!r}")
    path, _, mode = header.partition("|")
    path, mode = path.strip(), mode.strip()
    heading = None
    if mode.upper().startswith("APPEND_UNDER"):
        _, _, heading = mode.partition(":")
        heading, mode = heading.strip(), "APPEND_UNDER"
    return path, mode.upper(), heading


def apply_file(path_s: str, mode: str, heading: str | None, body: str) -> str:
    path = Path(path_s)
    body = body.rstrip("\n") + "\n"

    if mode == "CREATE":
        if path.exists():
            raise BundleError(
                f"CREATE but {path} already exists.\n"
                f"Change the mode to REPLACE in the bundle and rerun."
            )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        return f"created  {path}  (+{body.count(chr(10))} lines)"

    if mode == "REPLACE":
        if not path.exists():
            raise BundleError(
                f"REPLACE but {path} does not exist.\n"
                f"Change the mode to CREATE in the bundle and rerun."
            )
        before = path.read_text(encoding="utf-8").count("\n")
        path.write_text(body, encoding="utf-8")
        return f"replaced {path}  ({before} -> {body.count(chr(10))} lines)"

    if mode == "APPEND":
        if not path.exists():
            raise BundleError(
                f"APPEND but {path} does not exist.\n"
                f"Change the mode to CREATE in the bundle and rerun."
            )
        existing = path.read_text(encoding="utf-8").rstrip("\n")
        path.write_text(existing + "\n\n" + body, encoding="utf-8")
        return f"appended {path}  (+{body.count(chr(10))} lines)"

    if mode == "APPEND_UNDER":
        if not path.exists():
            raise BundleError(f"APPEND_UNDER but {path} does not exist.")
        lines = path.read_text(encoding="utf-8").splitlines()
        try:
            start = next(
                i for i, ln in enumerate(lines) if ln.strip() == (heading or "").strip()
            )
        except StopIteration:
            raise BundleError(
                f"Heading {heading!r} not found in {path}.\n"
                f"NOTHING was written for this block. Either fix the heading in\n"
                f"the file, or paste this one block in by hand. Other blocks in\n"
                f"the bundle were unaffected."
            )
        level = len(lines[start]) - len(lines[start].lstrip("#"))
        end = len(lines)
        for i in range(start + 1, len(lines)):
            s = lines[i].lstrip("#")
            if lines[i].startswith("#") and (len(lines[i]) - len(s)) <= level:
                end = i
                break
        new = lines[:end] + body.rstrip("\n").splitlines() + [""] + lines[end:]
        path.write_text("\n".join(new) + "\n", encoding="utf-8")
        return f"inserted {path}  under {heading!r}"

    raise BundleError(
        f"Unknown mode {mode!r}. Use CREATE, REPLACE, APPEND, or APPEND_UNDER."
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("bundle", help="path to handoff-bundle.md")
    ap.add_argument(
        "--dry-run", action="store_true", help="show what would happen, write nothing"
    )
    ap.add_argument(
        "--handoff-dir", default="docs/handoffs", help="where narrative/meta go"
    )
    args = ap.parse_args()

    try:
        text = Path(args.bundle).read_text(encoding="utf-8")
        blocks = parse(text)
        if not args.dry_run:
            require_clean_tree()
    except (BundleError, OSError) as e:
        print(f"\nSTOPPED: {e}\n", file=sys.stderr)
        return 1

    hdir = Path(args.handoff_dir)
    results: list[str] = []
    commit_msg = "Phase output"

    for kind, header, body in blocks:
        try:
            if kind == "FILE":
                path, mode, heading = split_header(header)
                if args.dry_run:
                    results.append(f"[dry-run] {mode:12} {path}")
                else:
                    results.append(apply_file(path, mode, heading, body))

            elif kind in ("HANDOFF", "META"):
                name = header or "phase"
                suffix = "" if kind == "HANDOFF" else "-meta"
                target = hdir / f"{name}{suffix}.md"
                if args.dry_run:
                    results.append(f"[dry-run] write        {target}")
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(body.rstrip("\n") + "\n", encoding="utf-8")
                    results.append(f"wrote    {target}")

            elif kind == "COMMIT":
                commit_msg = body.strip().splitlines()[0] if body.strip() else commit_msg

        except BundleError as e:
            print(f"\nSTOPPED: {e}\n", file=sys.stderr)
            print("Already applied:", file=sys.stderr)
            for r in results:
                print(f"  {r}", file=sys.stderr)
            print("\nUndo everything with:  git checkout .\n", file=sys.stderr)
            return 1

    print()
    for r in results:
        print(f"  {r}")

    if args.dry_run:
        print("\nDry run — nothing written.\n")
        return 0

    stat = git("diff", "--stat")
    if stat:
        print(f"\n{stat}")
    print("\nReview, then commit:\n")
    print(f'    git diff')
    print(f'    git add -A && git commit -m "{commit_msg}" && git push')
    print("\nOr undo everything:\n")
    print("    git checkout .\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
