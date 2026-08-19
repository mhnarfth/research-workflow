# Updating the Framework

Short version. Full detail in `phases/P19-framework-maintenance/README.md`.

---

## The two rules

**Collect during, change between.** Note friction while it happens; act on it
between papers. Never change your process mid-project.

**A paper runs on the version it started with.** Record it in the project's
`NOTES.md` at P02. Changes apply to the next paper. Nothing is retrofitted.

---

## The loop

```bash
cd ~/research/research-workflow
git status                                        # clean

python tools/bundle_context.py --preset <preset>  # -> context.md
grep -rn "<the thing>" . --include="*.md"         # confirm nothing missed
```

Open a chat, attach or paste `context.md`, paste
`phases/P19-framework-maintenance/opening.md` with the blanks filled. Work.
Then paste `closing.md`.

```bash
python tools/apply_handoff.py handoff-bundle.md
git diff
git add -A && git commit -m "..." && git push
git tag v1.2 && git push --tags                   # after a CHANGELOG entry
```

---

## Which preset

| Change | Preset | ~tokens |
|---|---|---|
| Fix one phase's prompt or checklist | `tweak-phase P07` | ~4k |
| Add / remove / merge a phase | `add-phase` | ~10k |
| Change a standing rule | `standing-rule` | ~12k |
| Change the bundle format or write modes | `bundle-format` | ~13k |
| Change the coaching clause | `coaching` | ~13k |
| Change scheduling ratios | `schedule` | ~8k |
| Docs, ledgers, reading list | `top-level` | ~13k |
| Structural rework | `--all` | ~49k |

Or name files directly:

```bash
python tools/bundle_context.py --files WORKFLOW.md phases/P07-execution
```

**Always grep.** The preset is a starting point. If grep finds a file the
preset didn't load, add it with `--files`.

---

## The other repos

**`research-index`** — small; load it whole. Nothing depends on it.

**`research-project-template`** — existing projects are **clones**. A template
change reaches the next clone only. To apply one to a running project, do it by
hand and note it.

**A paper's own repo** — `docs/` there are project artifacts, not framework
files. Edit them directly; that's normal work.

---

## Before you change anything

- Is the friction real, or imagined?
- Am I fixing the cause or the symptom?
- Is there a **smaller** change? Editing a phase beats adding one.
- Does the framework still fit in my head afterward? If not, the right change
  is **removal**.
