# tools/

## apply_handoff.py

Applies a handoff bundle from a phase's closing prompt: writes the file
updates, saves the narrative and meta into `docs/handoffs/`, prints the diff
and a commit command. **It never commits.**

> **THE ONE RULE: clean tree before, `git checkout .` after.**
> That single command undoes anything this script did. Nothing else to know.

### The whole procedure

```bash
cd <your project repo>

git status                                  # must say "working tree clean"
                                            # if not:
                                            #   git add -A && git commit -m "wip"

# drop handoff-bundle.md in the repo root, then:
python tools/apply_handoff.py handoff-bundle.md

git diff                                    # read what actually changed
git diff --stat                             # or just the file list

# happy:
git add -A && git commit -m "<message it printed>" && git push

# unhappy:
git checkout .
```

Add `--dry-run` to see what it would do without writing anything (and without
requiring a clean tree).

### Failure cases

| It says | What happened | Do this |
|---|---|---|
| `Working tree is dirty` | Uncommitted changes exist, so a later `git checkout .` would destroy them too | `git add -A && git commit -m "wip"`, rerun |
| `Heading '## X' not found` | An `APPEND_UNDER` block targeted a heading that isn't in the file. **Nothing was written for that block**; other blocks applied normally | Fix the heading in the file, or paste that one block by hand |
| `CREATE but <file> already exists` | The chat thought it was a new file | Change that block's mode to `REPLACE`, rerun |
| `REPLACE but <file> does not exist` | The chat thought the file existed | Change that block's mode to `CREATE`, rerun |
| `No blocks found` | The bundle isn't in the expected format | Check the `=== FILE: ... ===` / `=== END ===` delimiters |
| Applied fine, but the diff looks wrong | A bad REPLACE, most likely | `git checkout .` — everything undone, nothing lost |
| Script crashed partway | Rare | `git checkout .`, then apply the blocks by hand |

If it stops partway it prints what it already applied. `git checkout .` still
undoes all of it.

### Write modes

| Mode | Means |
|---|---|
| `CREATE` | file must not exist |
| `REPLACE` | file must exist; rewritten whole |
| `APPEND` | added to the end |
| `APPEND_UNDER: ## Heading` | inserted under that heading, before the next one of the same or higher level |

**A phase may only REPLACE a file it received as input.** If it never saw the
file, a REPLACE would silently drop content. That constraint is stated in every
`closing.md`.

### Bundle format

```
=== FILE: docs/DECISIONS.md | APPEND ===
### 2026-08-09 — [feasibility] <decision>
=== END ===

=== HANDOFF: P02-feasibility ===
<narrative — goes to docs/handoffs/P02-feasibility.md>
=== END ===

=== META: P02-feasibility ===
<workflow notes — goes to docs/handoffs/P02-feasibility-meta.md>
=== END ===

=== COMMIT ===
Feasibility gate: constraints, anonymization, authorship
=== END ===
```

---

## Coming in the project template (batch 4)

- **`preflight.py`** — pre-release safety scan. Greps tracked files for real
  filesystem paths, provider names, and credentials; flags large binaries
  (`.npz` numpy data, `.pt` PyTorch checkpoints — the two formats most likely
  to leak restricted data); checks every committed figure has its
  `figdata/*.json`. Reports only; you decide.
- **`schedule.py`** — prints where you are against the reverse schedule in
  `VENUE.md`.
