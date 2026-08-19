# P02 — Feasibility Gate

**This is where the repo and the LLM project get created** — once the gate
passes. `FEASIBILITY.md` is the first commit.

## Purpose

Decide, cheaply, whether to spend six weeks on this. And settle four things now
that are expensive to settle later.

## Should be fast

Most of this is a **lookup** from the dataset registry, not fresh analysis.
Thirty minutes if the registry is current. That's the payoff of P00.

## The nine sections

1. **Data** — which registry entries, and do their constraints permit what I want?
2. **Anonymization** — decided **here**, not at write-up. Codenames (`ISP_A`,
   `NET_1`) go in tracked source from the first commit; real names live only in
   gitignored `config/local_paths.py`. Deciding this late is what forced a
   global find-replace under deadline pressure on INDIS.
3. **Defensibility** — can I defend this to *this* audience, and what will they
   attack first? Anything I'd have to hand-wave is the weak point — name it.
4. **Budget** — compute, wall-clock, calendar weeks, each with a 2× buffer.
5. **Novelty firewall** — anything of mine under review this could overlap?
   **Overlap includes methodology, not just results.** If a manuscript under
   review presents the mathematics of a method, re-deriving it elsewhere is
   overlap even with different plots. This constraint shaped the entire INDIS
   project.
6. **Kill criterion** — what result makes me abandon this? Write it now, while
   you're not invested. This is what stops results-shopping in week six.
7. **Authorship** — who's on it, in what order, who presents. Settled now, not
   during submission. Anything that's your advisor's own (his bio, wording he
   prefers), ask for early and use his canonical version.
8. **Ethics / IRB / data-use** — probably not needed for network telemetry, but
   check once, cheaply, rather than discovering it at review.
9. **Funding attribution** — which grants apply. Pull the numbers from the
   index; never retype them from memory.

## Outputs

- `docs/FEASIBILITY.md`
- New dataset registry entries, if any
- Gate decision: proceed / proceed modified / park / reject

## If the gate fails

Park it in the backlog or reject it into the rejection log, with the reason.
A failed gate is a cheap win — it cost you thirty minutes instead of six weeks.

## If the gate passes — create the repo

```bash
cd ~/research/projects
git clone https://github.com/<you>/research-project-template.git <topic>-private
cd <topic>-private && rm -rf .git && git init
cp config/local_paths.example.py config/local_paths.py   # gitignored
git add -A && git commit -m "Initial: feasibility gate"
```

Then create the LLM project and load the project-knowledge files.
