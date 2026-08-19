# P08 — Mid-Execution Red Team

**A separate short chat, run in the middle of P07.** Not a sub-chat of
execution — a different chat entirely.

## Why separate

An execution chat that has spent 80k tokens helping you build something cannot
attack it honestly. Same principle as P11, just earlier and cheaper.

## When to fire it

**Not at a percentage of the schedule.** The trigger is:

> **The primary result exists, and the defensive work hasn't started.**

You've run the main experiment and you know what the headline finding is. You
have *not* yet run ablations, sensitivity checks, or robustness tests. That's
the moment, because the red team can evaluate a real finding rather than a
fragment, and there's still time to act since the defensive work hasn't been
designed yet.

The schedule position (T−40%) is a **separate, weaker signal**. If you pass it
and the primary result still doesn't exist, that's information about scope — and
what you do with it is your call.

## Re-firing

If results later change the picture substantially — a new finding, a result
that contradicts what you showed it — run it again as `P08-redteam-2`. It's a
short cheap chat, not a one-shot gate.

## Why this phase earns its place

On INDIS the FedProx sweep and the local-epoch ablation were added purely to
preempt reviewer questions. **They became the mechanism finding** — the paper's
actual contribution. Reviewer-anticipation work reliably produces contributions
when it's done with time left to act on it.

## Two outputs

The red team has everything it needs to produce both:

**A — content for `NOTES.md`** (the record: attacks, recommended experiments,
reasoning)

**B — a short delta paragraph** you paste straight into the live execution chat

Part B matters because editing a file doesn't update a chat that's already
holding the old version. Paste the delta, not the whole file.

## Scope

It may note where you are against the schedule and **advise** on scope. It asks;
it never acts. Every scope decision is yours.

## Backward jumps

If the red team's recommendation only **adds experiments**: edit
`STAGE-PLAN.md`, paste the delta into the execution chat, keep going.

If it changes the **architecture or the claim**: open a new numbered planning
chat, `P06-codeplan-2`, with the old plan plus the red team's findings as input.
