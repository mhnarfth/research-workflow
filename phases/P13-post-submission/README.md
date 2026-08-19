# P13 — Post-Submission

**Short, mechanical, and the one people skip.** Skipping it is how six months
of provenance gets reconstructed by hand a year later.

Do it the same day you submit, while everything is fresh.

## The steps

1. `git tag <venue><year>-submitted` and push tags
2. `pip freeze > requirements-frozen.txt`, committed — `torch>=2.0` reproduces
   nothing in three years; `torch==2.4.1` might
3. **Finish `NOTES.md` while fresh** — decisions, bugs, what didn't work,
   result stability, headline numbers with their source files
4. **Freeze `CLAIMS.md`** — copy `## As planned` into `## As submitted`. The
   rebuttal uses as-submitted, because that's what reviewers read
5. **Extension ideas** — paragraphs with reasoning in `NOTES.md`, one scannable
   line each in the research-index backlog. Best time is now, while you still
   remember what you wished you'd done
6. **Collection note** — "if this gets folded into a larger work, here's what
   needs reframing, and which notation needs aligning." Five minutes now versus
   reconstructing it later
7. Index row updated
8. **Retro chat** (below)
9. Preprint, only if `VENUE.md` says it's permitted — and the default is to
   wait for acceptance

## The retro chat

A fresh chat. Input: `cat docs/handoffs/*-meta.md` plus `RUNLOG.md` and
`NOTES.md`. One question: *where did I waste time, what did I do
non-standardly, what should I learn?*

Output appends to `research-workflow/LEDGER-improvements.md`.

This is the whole payoff of passive capture — the `## Meta` blocks were
collected as you went, with no ongoing obligation, and the retro distills them
once, when you have perspective anyway.

## Extension discipline

**Build the next paper from new experiments, not withheld figures.** A reviewer
will ask what's new, and "we also show the plots we had all along" is a weak
answer.

Rank them. The reviewer's strongest objection to this paper is usually the
definition of the next one's contribution.
