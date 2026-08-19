# Quickstart

The whole framework on one page. Full detail in `WORKFLOW.md`.

---

## The one idea

**Files are the memory. Chats are disposable.**

Every chat ends by writing to a file. Every chat starts by reading files. Chats
never talk to each other — the handoff document is the only channel. This is
what stops one chat from becoming a 600k-token single point of failure that you
can't afford to leave.

---

## Repos (5)

| Repo | What |
|---|---|
| `research-workflow` | The manual. This. |
| `research-index` | Every paper, dataset, idea, rejection, review, contact |
| `research-project-template` | Cloned per paper |
| `<topic>-private` | One per paper. Where you work |
| `<topic>` | Public. Cut fresh at submission |

Name by **topic**, never venue — venue lives in a git tag
(`indis2026-submitted`), so a rejected paper resubmits without renaming.
Never flip a private repo public; git history goes public with it.

---

## The loop, every phase

1. Read `phases/PNN-<name>/README.md`
2. Copy `opening.md` → fill blanks → paste as the chat's first message
3. Work
4. Paste `closing.md` → get `handoff-bundle.md`
5. Check `checklist.md`
6. `git status` (clean) → `python tools/apply_handoff.py handoff-bundle.md` →
   `git diff` → commit

Undo anything: `git checkout .`

**Kill a chat at ~100k tokens.** Hard cap 200k. Split on natural boundaries
(per literature theme, per pipeline stage, per section group), numbered
`P07-exec-1`, `P07-exec-2`.

**Backward jumps:** edit the document, paste the *delta* into the live chat.
Never reopen a dead chat.

---

## The 18 phases

| | Phase | The point |
|---|---|---|
| 00 | Continuous | Zotero, idea backlog, index. No chat |
| 01 | Ideation | Pick one. Log **why** you rejected the others |
| 02 | Feasibility | Repo created. **Anonymization + authorship decided here** |
| 03 | Venue | Ladder incl. **never**. Reverse schedule computed |
| 04 | Literature | `lit-0` plans, `lit-1..N` execute. Nothing from memory |
| 05 | Research planning | RQs, contributions, **figure + table sketches** |
| 06 | Code planning | Stages, config, 3 loader paths, pilot run |
| 07 | Execution | `RUNLOG.md` by hand. Ends with the **debrief** |
| 08 | Red team | Fires when the primary result exists |
| 09 | Paper planning | Section plan + word budgets. `CLAIMS.md` complete |
| 10 | Drafting | Split by section. Compression = **cut list only** |
| 11 | Adversarial | **Fresh chat, zero context.** 2–3 framings |
| 12 | Pre-submission | Public repo, URL in paper, submit. 24h buffer |
| 13 | Post-submission | Tag, freeze, `NOTES.md`, extensions, **retro** |
| 14 | Review response | Rebut, or reject → ladder → resubmit |
| 15 | Camera-ready | **Zenodo DOI minted here** |
| 16 | Artifact evaluation | Only if the venue runs one |
| 17 | Talk/poster | Third styling profile, transcript |
| 18 | Logistics | **Visa first**, then everything else |
| 19 | Framework maintenance | Changing the framework itself. Collect during, change between |

---

## Scheduling

Ratios of the runway, computed at P03:

```
setup 20% · execution 40% · writing 25% · review 8% · buffer 5%
```

Only the submission buffer has a floor: **24 hours**. The system may advise on
scope; every scope decision is yours.

---

## The 9 standing rules

1. Every figure writes `results/figdata/<name>.json` — redrawable without the
   pipeline
2. `CLAIMS.md` is versioned: as planned / as submitted
3. **Write no number not in the claims ledger**
4. Anonymization and authorship are **P02** decisions
5. Write your `DECISIONS.md` answer *before* asking a model, then have it attack
6. Improvement capture is passive; the retro distills once
7. Extension ideas: one line in the index, paragraphs in `NOTES.md`
8. Never flip a private repo public
9. **Never cut a limitation, caveat, named outlier, or negative result** to fit
   a page limit

---

## Three things that are always yours

- **The claim.** What is this paper saying, in one sentence?
- **The venue.** By the nature of the contribution, never the amount of material.
- **Scope.** Nothing in this system cuts your work for you.

---

## When you've been away

Read this file, then the paper's `docs/NOTES.md` and latest
`docs/handoffs/*.md`. That's enough to resume.
