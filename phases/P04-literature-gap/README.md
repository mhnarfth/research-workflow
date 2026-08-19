# P04 — Literature & Gap

**Multi-chat: `P04-lit-0` plans, `P04-lit-1..N` execute.**

## Purpose

Find the gap. The gap determines the contribution, which is why this comes
before research planning rather than inside it.

## Structure

**`lit-0` — survey and plan.** One chat. Search broadly, report what's out
there, what the clusters are, what each cluster argues. You read it and vet it.
Output: `LITERATURE-PLAN.md` — themes, how many chats, what each covers, and
the specific questions each must answer.

**`lit-1..N` — execute per theme.** Each finds papers for its theme, verifies
URLs, summarizes. You vet, add to Zotero, move on.

How many chats depends on ground to cover: an extension paper may need one
(`LINEAGE.md` carries the prior bibliography); a new topic typically three; a
genuinely broad survey four or five.

## Three checks, run in lit-0 against whatever themes emerge

1. What's the canon here?
2. What's closest to what I'm doing?
3. **What would a reviewer be angry I didn't cite?**

The third is the highest-value question in this phase. It's a gap check on the
plan, not a theme of its own. On INDIS it produced `zhu2019deep` (gradient
inversion — the paper's central privacy premise depends on acknowledging it)
and FedRep (an entire subfield built on the mechanism finding's premise).
Omitting either would have been serious.

## Hard rule: nothing from memory

Every citation is either found by live search in-session or verified from a
primary source. The chat marks provenance explicitly — *found this session* vs.
*from my knowledge, verify before adding*. You click through and confirm.

This caught a wrong URL on INDIS (dblp instead of proceedings.mlsys.org). It
will catch more.

## Zotero flow

Collection per project → add papers as you vet them → Better BibTeX
auto-exports `references.bib` into the repo's `paper/` folder. You never
hand-assemble BibTeX again, and the `.bib` is version-controlled with the paper.

## Recency

**A target, not a constraint.** Aim for roughly 30–40% from the last 2–3 years;
foundational work stays old because it should. The phase output includes a
**year histogram** so you can see the shape before a reviewer tells you. If
recent work genuinely doesn't exist, that's a finding — occasionally a gap
worth naming in the paper.

## Placement discipline

Every citation must *do work*, not decorate. When a citation is added, note
what argumentative job it does — that note becomes the Related Work structure
at P09.

## Outputs

- `docs/LITERATURE.md` — gap statement, themes, per-theme summaries, year
  histogram, draft Related Work structure
- `paper/references.bib` — via Zotero
