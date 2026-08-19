# P10 — Drafting

**Several chats: `P10-draft-1`, `-2`, `-3`, then a compression chat.**

## Split by section group, and it improves quality

Counter-intuitive but true: a chat holding 80k tokens of accumulated draft
attends *worse* to the section you're currently writing. A "single shot" long
chat writes worse later sections.

Coherence comes from `SECTION-PLAN.md` — every drafting chat gets it, so each
knows what the others are writing. Plus each chat receives the previous chats'
output as input.

Typical split: I–III · IV–V · VI–VII + abstract.

**No merge chat needed.** You paste sections into one `.tex` and compile —
merging already happens. A coherence pass folds into the compression chat,
which reads the whole assembled paper anyway.

## Figure styling — this is where it happens

Now that you know which figures ship, restyle them for print:
`analysis/restyle_figures.py` loads `results/figdata/*.json`, applies the knobs
(font sizes, figsize, line widths, colors, legend/title toggles), rewrites the
PDFs. **Never touches the pipeline.** This is what the figdata rule bought you.

Everything tweakable lives at the top of the file as variables. No hardcoded
values below.

## Compression — never ask for a shorter paper

If you say "cut this from 9 pages to 6," you get summarization: the model
regenerates the paper at lower fidelity, and summarization deletes specifics,
hedges, and caveats **first** — exactly the wrong things. It can collapse 9
pages to 3.

**Ask for a cut list instead.** Output is a table, not a document:

| # | Location | Cut | Lines saved | Risk |
|---|---|---|---|---|
| P1 | §V-F ¶2 | Restates the crossover already in §IV-C | 6 | None |

You apply P1, P2, P3 in your `.tex` until it fits. The prose you keep is prose
you already approved — nothing is regenerated, so nothing gets silently
rewritten. Unused cuts stay in reserve for when a float shifts and you lose
half a page.

**Cut order:** restatements across sections → hedging and qualifiers →
methodology detail that belongs in the appendix → figures that don't carry a
claim → related-work paragraphs that aren't load-bearing.

**Never cut** (standing rule 9): a limitation, a caveat on a claim, a named
outlier, or a negative result.

## Versioning

Git tags for the source: `draft-v1`, `draft-v2`, `advisor-v1`,
`adversarial-fixes`, `submitted`. Tag names describe *what the version is*, not
the venue, so the same names work on resubmission.

Milestone PDFs to `paper/versions/<date>_<label>.pdf` — date-prefixed so they
sort. Only milestones, not every compile. When your advisor returns a marked-up
PDF, save it as `<date>_advisor-v1_commented.pdf`.

## The `.tex` workflow

Clone the repo once, work in `paper/`, commit from the repo root. LaTeX
Workshop in VS Code compiles on save. Build artifacts are gitignored.

## Advisor draft goes out at the end of this phase

Not after adversarial review — he needs lead time, and his comments and the
adversarial findings can be worked in parallel.

## Standing rule 3 is enforced here

Every number checked against `CLAIMS.md`. Anything not in the ledger is either
recall (suspect) or a ledger gap (fix it from the artifact).
