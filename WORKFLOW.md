# Research Workflow

The manual. One paper, ideation to presentation.

> **Core principle: files are the memory, chats are disposable.**
> Every chat ends by writing to a file. Every chat starts by reading files.
> Chats never talk to each other — the handoff document is the only channel.

**Portability.** This framework assumes only a chat interface with a context
window. Projects, Skills, file upload, web search are optimizations. If a model
can read text and write text, this runs. Nothing here is tied to one vendor.

---

## 1. Repos

| Repo | Visibility | Obsidian vault | Holds |
|---|---|---|---|
| `research-workflow` | Private | Yes | This file. Phase folders, ledgers, `MAINTENANCE.md`, `PROMPTING.md`, `READING.md`, `tools/` |
| `research-index` | Private | Yes | Paper tracker, dataset registry, idea backlog, rejection log, venue notes, `reviews/`, `PROFILE.md`, `NOTATION.md`, `CONTACTS.md`, funding list |
| `research-project-template` | Private (template) | — | Cloned per paper |
| `<topic>-private` | Private | Yes | One per paper. Contains `LINEAGE.md` if it extends prior work |
| `<topic>` | **Public** | — | Cut fresh at submission from the private repo |

**Naming.** By topic, never by venue — a rejected paper resubmits without
renaming. `-private` on the working repo; the public repo name stays clean
because it appears in the paper. No ID numbers. Venue lives in git tags.

```
federated-traffic-repr-private     ← working repo
federated-traffic-repr             ← public release repo
git tag indis2026-submitted        ← venue lives here
```

**One repo per paper.** An extension gets its own repo plus `LINEAGE.md`
pointing back to the prior repo and its submission tag. No shared code.

**Never flip a private repo public.** Git history goes public with it and
cannot be reliably scrubbed. The public repo is built fresh, one clean commit.

**Tooling.** GitHub is the hub. Obsidian edits and commits the markdown (one
vault per repo, so the Obsidian Git plugin works). VS Code for code and LaTeX.
Zotero for citations. GitLab mirror, refreshed yearly, against account loss.

---

## 2. Context architecture

```
Chat A ──(closing prompt)──▶ handoff.md ──▶ [project knowledge] ──▶ Chat B
```

- **One LLM project per paper.** An extension gets a new one, seeded with
  `LINEAGE.md`.
- **Project knowledge** — small, stable, needed by 2+ phases:
  `DECISIONS.md` · `NOTES.md` · `RUNLOG.md` · `CLAIMS.md` · `VENUE.md` ·
  `FEASIBILITY.md` · `config/config.py` · `LINEAGE.md`
- **Chat attachments** — big or single-use: literature PDFs, venue style
  exemplars, review text, draft `.tex`, results CSVs.
- **Rule of thumb:** if you'd be annoyed to pay for it in every chat for three
  months, it's an attachment.

Each phase's `opening.md` declares **which** files it needs, never **how** to
load them. Load via a Projects feature, per-chat attachment, or
`cat file1 file2` and paste. Keeping project knowledge small is what makes the
paste option viable, which is what makes the framework portable.

**Splitting.** Any phase may span N chats, numbered `P07-exec-1`, `P04-lit-2`.
Split on natural boundaries — per literature theme, per pipeline stage, per
section group — not purely on token count. Soft cap 100k, hard cap 200k.

**Backward jumps.** A phase's output *document* is living; a phase's *chat* is
dead. Never reopen a closed chat. Edit the document, then paste **the delta**
(not the whole file) into the chat that needs to know. Open a new numbered chat
for that phase only when the architecture or the claim changes.

---

## 3. Four files per phase

```
phases/P05-research-planning/
├── README.md      ← the manual. Yours. Never given to a chat.
├── opening.md     ← copy, fill blanks, paste as the chat's first message
├── closing.md     ← the handoff prompt
└── checklist.md   ← what must be true before you leave this phase
```

| | Phase README | Opening message | Phase output |
|---|---|---|---|
| Written | once, ever | once, ever, with blanks | every paper, new |
| Read by | **you**, before starting | **the chat**, first message | **next phase's chat** |

Output files are **not** renamed per phase — most are written by several
phases. Provenance goes inside the file, by phase **name** (numbers shift when
phases are added):

```
### 2026-06-14 — [feasibility] Anonymize the regional ISP as ISP_A
### 2026-08-02 — [red-team] Add local-epoch ablation
```

Dates are ISO (`YYYY-MM-DD`), no timestamps — ISO sorts correctly as text.

See `phases/README.md` for the conventions every phase inherits.

---

## 4. The phases

| # | Phase | Notes |
|---|---|---|
| 00 | **Continuous** | Zotero · idea backlog · index updates · peer reviews you accept |
| 01 | Ideation | Grounded by `PROFILE.md` + dataset registry. Rejection *reasons* are the durable output |
| 02 | **Feasibility gate** | Repo + LLM project created here. Data constraints · **anonymization decided** · defensibility · budget · novelty firewall · kill criterion · authorship & order · ethics/IRB/data-use · funding attribution |
| 03 | Venue calibration | Ladder incl. **never** · style observations · 2 style exemplars named · preprint policy · artifact-evaluation check · **reverse schedule computed** |
| 04 | Literature & gap | `lit-0` surveys and plans; `lit-1..N` execute per theme. Nothing from memory. Zotero → `references.bib`. Year histogram |
| 05 | Research planning | RQs · claimed contributions · **figure and table sketches** · draft abstract |
| 06 | Code planning | Stages · config knobs · **metric direction table** · **three loader paths** · `plotting.py` + figdata · pilot run |
| 07 | **Execution** *(several)* | Error loop in-chat · `RUNLOG.md` by hand, per session · **execution debrief** at the end |
| 08 | Red team | Fires when the primary result exists and defensive work hasn't started. Outputs notes content **and** a delta paragraph. May re-fire |
| 09 | Paper planning | `SECTION-PLAN.md` with **word budgets** · `CLAIMS.md` complete · notation check |
| 10 | Drafting | Split by section group · **figure restyling** · **compression = cut list only** · advisor draft at the end |
| 11 | Adversarial review | **Fresh chat, zero context.** 2–3 framings. External reviews get their own fresh chat |
| 12 | Pre-submission | Triage → back-to-code gate · public repo cut · preflight · submission checklist · **24h buffer floor** |
| 13 | Post-submission | Tag · freeze env · `NOTES.md` · extension ideas · collection note · index row · **retro chat** |
| 14 | Review response | Rebut, **or** rejected → ladder → resubmit. Archive reviews |
| 15 | Camera-ready | **Zenodo DOI minted here**, swapped into the appendix · publisher format check · copyright |
| 16 | Artifact evaluation | Only if the venue runs one (checked at P03) |
| 17 | Talk or poster | Third styling profile · speaker transcript · top-3 attack prep |
| 18 | Conference logistics | **Visa first** · travel request approval · registration · grants · expense report after |

---

## 5. Reverse scheduling

Ratios of the runway, not fixed offsets — a 10-day deadline and a 3-month
deadline get the same shape at different scales. Computed at P03 from today's
date and the deadline, recorded in `VENUE.md`.

| Block | Share | Ends at |
|---|---|---|
| Setup — ideation → research planning | 20% | T−80% |
| Execution + red team | 40% | T−40% |
| Paper planning + drafting + figures | 25% | T−15% |
| Adversarial review + revision | 8% | T−7% |
| Advisor draft | — | computed default; compresses when the runway is short |
| Submission buffer | 5% | T−2%, **floor: 24 hours** |

Only the submission buffer has a hard floor — portals break, PDFs fail format
checks, page counts shift when a float moves.

The system computes dates and shows where you are. It **may advise** on scope.
**Every scope decision is yours.** Nothing acts on it.

---

## 6. Standing rules

1. **Every figure writes `results/figdata/<name>.json`** — one JSON per figure,
   fully redrawable without the pipeline, so restyling never touches the GPU.
2. **`CLAIMS.md` is versioned** — `## As planned` / `## As submitted`. The
   rebuttal uses as-submitted.
3. **Write no number not in the claims ledger.** If a number appears while
   drafting that isn't there, it came from recall (suspect) or the ledger is
   incomplete — fix it from the artifact, never from memory.
4. **Anonymization and authorship are Phase 02 decisions**, never write-up
   decisions. Codenames in tracked source from the first commit; real names
   only in gitignored `config/local_paths.py`.
5. **Your `DECISIONS.md` answer gets written before you ask a model** — then
   use the model to attack it. Directing, not orchestrating.
6. **Improvement capture is passive** — a `## Meta` block per handoff; the
   per-paper retro distills it into `LEDGER-improvements.md`.
7. **Extension ideas live in two places** — one scannable line in the index,
   paragraphs with reasoning in the paper's `NOTES.md`.
8. **Never flip a private repo public.** Build the public repo fresh.
9. **Never cut a limitation, a caveat on a claim, a named outlier, or a
   negative result to fit a page limit.** That is how honest papers become
   dishonest ones under deadline pressure.

---

## 7. Automation

`tools/apply_handoff.py` — one bundle in, files written, `git diff` shown,
commit command printed, **never auto-committed**.

```bash
git status                                  # must be clean
python tools/apply_handoff.py bundle.md
git diff                                    # review
git add -A && git commit -m "..." && git push
# or, to undo everything:
git checkout .
```

**Clean tree before; `git checkout .` after.** One command undoes any mess.
Full failure-case table in `tools/README.md`.

Also in the project template: `tools/preflight.py` (pre-release safety scan),
`tools/schedule.py` (where you are against `VENUE.md`).

**Slurm is optional.** Mention it only when a stage exceeds ~6 hours or a sweep
exceeds ~20 configurations. Otherwise run interactively.

---

## 8. Ledgers

`LEDGER-tooling.md` · `LEDGER-reading.md` · `LEDGER-improvements.md`

**Tooling adoption order** — don't adopt all at once:
Zotero + Better BibTeX → jupytext + nbstripout → Hydra → MLflow →
Snakemake or Makefile → Apptainer/Singularity.

---

## See also

`phases/README.md` — conventions every phase inherits (bundle format, write
modes, prompt pattern, coaching clause).
`MAINTENANCE.md` — what to update, when.
`PROMPTING.md` — how to get what you asked for.
`READING.md` — the reading list.
