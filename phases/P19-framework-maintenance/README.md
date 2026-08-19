# P19 — Framework Maintenance

**The framework's own phase.** Same four-file shape as every other phase,
because if the convention doesn't survive contact with itself it isn't a
convention.

## The two rules

**1. Collect during, change between.**

Never change the framework mid-paper. Friction gets *noted* while it happens
(`RUNLOG.md`, or the `## Meta` block of a handoff) and *acted on* between
papers. Changing your process mid-project is exactly the churn this framework
exists to prevent.

**2. A paper runs on the framework version it started with.**

Record the version in the project's `docs/NOTES.md` at P02. Framework changes
apply to the **next** paper. Nothing is retrofitted. This is why in-flight work
is never disrupted by an improvement.

## Where change requests come from

| Source | When |
|---|---|
| The P13 retro chat | Per paper — the main channel |
| Real friction mid-paper | Noted, not acted on |
| The yearly review | Once a year |
| A phase that never got used | Yearly — dead weight is a change too |

They queue in `LEDGER-improvements.md` under **Framework changes queued**.
Batch them; a release is worth more than five one-line commits.

## Blast radius — load only what a change touches

The whole repo is ~40k tokens. Loading all of it for a three-file change puts
you back in the big-context problem. Use `tools/bundle_context.py` with the
preset that matches:

| Change | Preset | Loads |
|---|---|---|
| Fix one phase's prompt or checklist | `tweak-phase P07` | that phase's 4 files + `phases/README.md` |
| Add a new phase | `add-phase` | `WORKFLOW.md`, `QUICKSTART.md`, `phases/README.md`, one example phase |
| Remove or merge phases | `add-phase` + the affected folders | same, plus neighbours |
| Change a standing rule | `standing-rule` | `WORKFLOW.md`, `QUICKSTART.md`, `MAINTENANCE.md` — then grep for affected phases |
| Change the bundle format or write modes | `bundle-format` | `phases/README.md`, `tools/`, **every `closing.md`** |
| Change the coaching clause | `coaching` | **every `opening.md`** |
| Change scheduling ratios | `schedule` | `WORKFLOW.md`, `QUICKSTART.md`, `P03` |
| Tooling / ledger / reading updates | `top-level` | top-level `.md` files only |
| Genuinely structural rework | `all` | everything (~40k tokens) |

Always `grep -rn "<the thing>" .` first. The preset is a starting point, not a
guarantee — if the grep finds a file the preset didn't load, add it.

## The other repos

**`research-index`** — small enough to load whole. Nothing depends on it, so
changes are safe and immediate.

**`research-project-template`** — existing projects are **clones**, not links.
A template change reaches the next clone only. If a change matters to a project
already running, apply it there by hand and note it.

**A paper's own repo** — its `docs/` are project artifacts, not framework
files. Edit them directly; that's normal work, not framework maintenance.

## Versioning

`research-workflow` gets tags: `v1.0`, `v1.1`, … and a `CHANGELOG.md` entry per
release. That's what lets a project say "started on v1.2" and mean something.

Bump **minor** for added phases, changed rules, new tools. Bump **major** if
the bundle format or the four-file convention changes — those break
compatibility with in-flight papers.

## The loop

Same as any other phase: `bundle_context.py` → paste into a chat with
`opening.md` → work → `closing.md` → `apply_handoff.py` → `git diff` → commit →
tag → changelog.

The framework updates itself with its own tooling. If that ever stops working,
that's the strongest possible signal something in the design is wrong.
