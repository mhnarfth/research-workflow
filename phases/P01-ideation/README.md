# P01 — Ideation

**Standalone chat. No repo, no LLM project yet** — those get created at P02,
once the idea passes the feasibility gate. Outputs go to `research-index`.

## Purpose

Choose one idea, and record why you rejected the others.

The rejection *reasons* are the more durable output. "I can't defend Dask
internals to an SC systems audience" is reusable for years; the rejected idea
usually isn't.

## Two entry points

**Backlog-driven** — an idea in the backlog has matured. Start from it.

**Deadline-driven** — a CFP appeared. Legitimate, and how INDIS 2026 happened.
The discipline is: **pull candidates from the backlog first**, then generate
only if the backlog has nothing that fits. Never brainstorm cold under time
pressure.

## Inputs

| File | Why it's needed |
|---|---|
| `research-index/PROFILE.md` | **Grounding.** Without it a chat generates ideas you can't execute or defend |
| `research-index` dataset registry | Data access determines what's possible |
| Idea backlog | Candidates |
| Rejection log | What you've already turned down, and why |
| The CFP | If deadline-driven — shapes framing and scope |
| `LINEAGE.md` | If this extends a prior paper |

## What matters here

**Standing rule 5 applies hardest in this phase.** Write your pick and your
reasoning in `DECISIONS.md` *first*, then ask the chat to attack it. If you let
the chat pick, you will spend six weeks on someone else's idea and be unable to
defend it in review.

**Reject on your own grounds, out loud.** "I'm not a stats student" and "the
supercomputing audience will interrogate internals I can't defend" are correct
calls about your defensible surface area. No model can make them for you.

**Ideas that turn a constraint into the question are stronger than ideas that
work around it.** The NDA became the research question in INDIS; that's what
made the paper.

## Outputs

- The chosen idea — one paragraph, in your words
- Rejection log rows for everything considered and dropped
- Backlog updates for anything parked rather than rejected

## Then

Go to P02. Do not create the repo yet — the gate might not pass.
