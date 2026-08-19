# P16 — Artifact Evaluation

**Only if the venue runs one** — checked at P03. Skip entirely otherwise.

## What it is

Some venues run a separate process after acceptance where a committee tries to
**run your code and reproduce your results**. You submit the repo plus
instructions; they attempt it; badges go on the paper (ACM: *Artifacts
Available*, *Artifacts Evaluated*, *Results Reproduced*).

Lighter venues run only an Artifact Description appendix — a description, not
an evaluation, often used as a tiebreaker.

## Restricted data — three layers

This is why P06 built three loader modes.

| Layer | Gets you |
|---|---|
| Public archive + DOI | **Artifacts Available** — always achievable |
| `public_only` config | An evaluator runs the pipeline end to end on the public dataset; a documented subset of claims reproduces |
| `synthetic` generator | Correctly-shaped fake data; nothing reproduces numerically, but the *pipeline* runs — which is what most evaluators are actually checking |

## The README is the deliverable that matters

Written for someone with **no context**: install, run, expected outputs,
runtime, what reproduces and what can't and why.

Be explicit about restricted data. Evaluators reward honest scoping over an
unqualified claim — and an unqualified claim that fails is much worse than a
scoped one that succeeds.

## Test it

Clone the public repo into a clean directory and follow your own README exactly
as written. Everything you had to figure out is a gap in the README.
