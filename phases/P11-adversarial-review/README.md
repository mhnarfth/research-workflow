# P11 — Adversarial Review

**Fresh chat. Zero project context. Not in the LLM project.**

## Why context-free

A chat that helped build the work is structurally incapable of attacking it
honestly — it will defend choices it participated in. Blindness is the point.

This is the free replacement for a paid review service, and it's better than
one in a specific way: you can run it three times with different framings.

## Run 2–3 times, separate chats

| Framing | Goes after |
|---|---|
| **Methods reviewer** | Statistics, experimental design, whether the claims follow from the evidence |
| **Domain reviewer** | Whether this matters, whether the framing fits this venue |
| **Skeptical PC member** | Why accept this over the next paper in the pile |

Each is its own chat so each stays blind.

## External reviews

If you also use a paid review service, feed its output into **another fresh
chat** (`P11-adversarial-4`), not into one that already produced its own attack
list. A chat that already attacked the paper will rank its own findings higher
and agree with itself. A fresh chat with the paper *and* the external review
triages both evenhandedly.

## `reviews/PATTERNS.md`

If you have accumulated reviews from prior papers, attach the distilled
patterns file: *"here are objections reviewers have raised on my previous
papers — check whether this draft is vulnerable to any of them."* Reviewers in
a subfield repeat themselves.

Don't attach the full review archive — attach the distillation.

## Triage

Every attack gets a disposition, recorded in `DECISIONS.md`:

| Attack | Action |
|---|---|
| **Invalidates a claim in `CLAIMS.md`** | **Back to code.** Non-negotiable |
| Weakens a claim but doesn't break it | Soften the claim's wording |
| Asks for an experiment you don't have | Concede in Limitations |
| Framing or presentation | Fix in text |
| Genuinely a next-paper question | Defer to the extension |

That table is what stops "one more experiment" from eating your deadline, and
equally what stops you shipping a claim you can't defend.

**The decision is yours**, recorded in `DECISIONS.md`. The triage list is input.
