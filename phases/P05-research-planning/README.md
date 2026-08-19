# P05 — Research Planning

## Purpose

Turn the gap into research questions, contributions, and a concrete target for
the code to aim at.

## Outputs

`docs/RESEARCH-PLAN.md` containing:

- **Research questions** — what this paper answers
- **Claimed contributions** — what you'll assert, in the venue's idiom
- **Figure and table sketches** — the contract with P06
- **Draft abstract** — the abstract you *hope* to write

## Figure and table sketches — the contract with code planning

Sketch the 5–7 figures and 3–4 tables that would **prove** the claim, on paper,
before any code exists. Not just counts — each one's rough content:

> Fig. 4: per-client benefit, grouped by network, showing stratification
> Table III: performance by regime, mean ± std across seeds

Then P06 designs a pipeline that produces exactly these.

**This is a target, not a fixed contract.** New figures appear during execution
— that's normal, and often where findings come from. The sketch exists so the
pipeline has direction. Without it you generate 14 figures and ship 7.

## The draft abstract

Write the abstract you hope to write. **It will be wrong.** That's fine — the
point is naming the claim before you're invested in a result, so that when the
result differs you notice, rather than quietly reframing.

Keep it. At P09 you compare it against what actually happened. The gap between
them is often the most interesting thing you learned.

## Notation

Check `research-index/NOTATION.md`. If a quantity already has a symbol in your
prior papers, use that symbol. Reconstruction error being `MAE` in one paper
and `ε_rec` in another turns your eventual thesis or journal extension into a
translation exercise, and reviewers of the extension notice the inconsistency.

## Standing rule 5

Write your own RQs and contributions in `DECISIONS.md` first, then have the
chat attack them. Contributions you didn't formulate yourself are contributions
you can't defend at a defense.
