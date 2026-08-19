# Maintenance

What to update, when. Glance here instead of trying to remember fifteen files.

---

## By trigger

Everything here is prompted by something you're already doing, so it survives
on its own.

| When this happens | Update |
|---|---|
| An idea occurs to you | `research-index` → idea backlog |
| You finish reading something good | Zotero · `LEDGER-reading.md` |
| You reject an idea | `research-index` → rejection log (the **reason** is the durable part) |
| You touch a dataset for the first time | `research-index` → dataset registry |
| You close any phase chat | apply the bundle, commit, push |
| You finish a working session on code | `RUNLOG.md` — three lines, by hand |
| You make a non-obvious choice | `DECISIONS.md`, tagged `[phase-name]` |
| A paper's status changes | `research-index` → paper row |
| You submit | tag · freeze env · retro chat · extension ideas · index row |
| Reviews arrive | `research-index/reviews/<venue><year>.md` |
| You meet someone worth remembering | `research-index/CONTACTS.md` |
| A paper is accepted | Zenodo DOI · index row · **start P18 — visa timeline first** |
| You introduce new notation | `research-index/NOTATION.md` |
| A collaborator joins a paper | `docs/COLLABORATION.md` in that project |

---

## By cadence

Nothing triggers these, which is exactly where systems rot. Put the yearly
block in your calendar once, recurring. It takes about an hour.

| Cadence | Do |
|---|---|
| **Per paper** (P13) | Retro chat → `cat docs/handoffs/*-meta.md` → distill into `LEDGER-improvements.md` |
| **Yearly** | Distill `reviews/PATTERNS.md` from accumulated reviews |
| | Review the rejection log — what do you consistently reject, and what should you go learn? |
| | Prune the idea backlog |
| | Check `NOTATION.md` for drift across papers |
| | Refresh `PROFILE.md` |
| | Mirror all repos to GitLab |
| | Review `LEDGER-tooling.md` — adopt the next one |

---

## File map

Where everything lives, if you've forgotten.

### `research-workflow`
`WORKFLOW.md` · `MAINTENANCE.md` (this) · `PROMPTING.md` · `READING.md` ·
`LEDGER-tooling.md` · `LEDGER-reading.md` · `LEDGER-improvements.md` ·
`tools/apply_handoff.py` + `tools/README.md` ·
`phases/README.md` · `phases/P00…P18/` each with `README.md`, `opening.md`,
`closing.md`, `checklist.md`

### `research-index`
`README.md` (paper tracker · dataset registry · idea backlog · rejection log ·
venue notes · funding list) · `PROFILE.md` · `NOTATION.md` · `CONTACTS.md` ·
`reviews/<venue><year>.md` · `reviews/PATTERNS.md`

### `<topic>-private` (per paper)
`docs/` — `FEASIBILITY.md` · `VENUE.md` · `LITERATURE.md` ·
`RESEARCH-PLAN.md` · `STAGE-PLAN.md` · `SECTION-PLAN.md` · `DECISIONS.md` ·
`NOTES.md` · `RUNLOG.md` · `CLAIMS.md` · `RELEASE.md` ·
`LINEAGE.md` (extensions only) · `COLLABORATION.md` (only when collaborating) ·
`handoffs/<phase>.md` + `handoffs/<phase>-meta.md`

`config/` · `src/` · `pipeline/` · `analysis/` · `ablations/` ·
`diagnostics/` · `archive/` · `data/README.md` · `tools/` ·
`results/metrics/` · `results/figures/` · `results/figdata/` ·
`paper/` + `paper/versions/`
