# P09 — Paper Planning

## Purpose

Decide what the paper says, section by section, and lock down every number
before a word gets drafted.

## Two outputs

**`docs/SECTION-PLAN.md`** — section by section against the page limit, with
**word budgets per section**, not just page counts. Word budgets are what keep
drafting overshoot at 20% instead of 50%, which is the difference between
trimming and gutting.

Also: which figures and tables actually ship (usually fewer than produced — 14
generated, 7 shipped on INDIS), and where each contribution lands.

**`docs/CLAIMS.md`** — every number you intend to report, with the artifact
file it came from. Filled in **here**, before drafting.

## The claims ledger

This is what makes standing rule 3 enforceable:

> **Write no number not in the claims ledger.**

While drafting, if a number appears that isn't on the list, one of two things
is true — it came from the model's recall (possibly wrong), or your ledger is
incomplete. Either way you go to the artifact, never to memory. It's the
tripwire against a number in your text disagreeing with the number in your
table, which is the most common and most damaging paper error.

`CLAIMS.md` is versioned: `## As planned` (here) and `## As submitted` (frozen
at P13). The rebuttal uses as-submitted, because that's what reviewers read.

## Honest-framing checks

Run against every claim before it goes near the paper:

- Is a difference inside noise being reported as an improvement?
- Is "not significantly different" being written as "equivalent"? It isn't —
  that needs an equivalence test.
- Is an outlier driving an aggregate? Report mean **and** median, and name the
  outlier before a reviewer finds it.
- Is a pooled correlation actually a between-group artifact?
- Is any metric name ambiguous against my other papers?

## Also here

**Notation check** against `research-index/NOTATION.md`, before drafting locks
it in.

**Compare the draft abstract** written at P05 against what actually happened.
The gap between what you hoped to find and what you found is often the most
interesting thing you learned — and sometimes it's the paper's real framing.
