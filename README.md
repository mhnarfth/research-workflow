# Research Workflow

The manual for how I run a research project, ideation to presentation.

**Start here:** [`WORKFLOW.md`](WORKFLOW.md)
**Forgot what to update?** [`MAINTENANCE.md`](MAINTENANCE.md)
**Output came back wrong?** [`PROMPTING.md`](PROMPTING.md)

## The five repos

| Repo | Holds |
|---|---|
| `research-workflow` | This one. The manual. |
| `research-index` | Tracker, datasets, ideas, rejections, reviews, notation, contacts, profile |
| `research-project-template` | Cloned per paper |
| `<topic>-private` | One per paper |
| `<topic>` | Public, cut fresh at submission |

## Running a phase

1. Read `phases/PNN-<name>/README.md`
2. Copy `opening.md`, fill the blanks, paste as the chat's first message
3. Work through it
4. Paste `closing.md` as the final message
5. Check `checklist.md`
6. `python tools/apply_handoff.py handoff-bundle.md`, review the diff, commit

Shared conventions for all phases: [`phases/README.md`](phases/README.md)

## Build status

- [x] `WORKFLOW.md`, `MAINTENANCE.md`, `PROMPTING.md`, `READING.md`
- [x] Ledgers
- [x] `phases/README.md` — shared conventions
- [x] `tools/apply_handoff.py` + docs
- [ ] Phase folders P00–P05 *(batch 2)*
- [ ] Phase folders P06–P11 *(batch 3)*
- [ ] Phase folders P12–P18 + `research-index` + `research-project-template` *(batch 4)*
