PHASE: Code planning

WHAT I'M DECIDING: the pipeline stages, the config, and the plumbing that has
to exist before any real run.

REQUIRED CONTEXT: RESEARCH-PLAN.md (the figure and table sketches are the
target), FEASIBILITY.md, VENUE.md
ATTACHMENTS: the project template structure; a listing of my data files and
their schemas

WHAT I WANT OUT: STAGE-PLAN.md, a populated config, src/plotting.py, and a
pilot-run plan.

---

MY ANSWERS FIRST:

Rough stage breakdown as I see it: <...>
Known constraints (memory, runtime, data quirks): <...>

---

HOW TO WORK THIS:

1. STAGES. Map the figure and table sketches onto pipeline stages. For each
   stage give me a row: number | what it reads | what it writes | what it
   CACHES | estimated runtime | which sketched figures/tables it produces.
   Every sketched figure must be produced by some stage. Flag any sketch that
   nothing produces.

2. CONFIG. List every knob that will exist. Mark which are primary and which
   are DERIVED from others. Anything derivable must be computed, never
   hardcoded twice — two independent constants for the same quantity will
   silently disagree and produce plausible-but-wrong figures.

3. METRIC DIRECTION TABLE. For every metric this pipeline will produce, one
   line: metric | lower or higher is better | typical range | what I should
   expect to see if my claim holds. Write it plainly enough that I can read it
   later while tired and know whether a number is good.

4. LOADER. Design ONE loader with three modes: real, public_only (runs on just
   the public dataset), synthetic (correctly-shaped fake data). This must exist
   from the start — retrofitting it after the paper is written means rewriting
   the loader.

5. PLOTTING. Specify src/plotting.py: palette, style knobs as module-level
   variables, and save_figure() writing BOTH the PDF and
   results/figdata/<name>.json. The JSON must be sufficient to redraw the
   figure with no access to models, caches, or the pipeline.
   ASCII only in all figure text — matplotlib's PDF backend silently drops
   en/em dashes from the embedded text layer.

6. PILOT RUN. Define the smallest end-to-end run that exercises every stage:
   one seed, tiny subset. What should it output, and what would tell me the
   plumbing is broken?

7. SLURM — only if warranted. If any stage exceeds ~6 hours or a sweep exceeds
   ~20 configurations, sketch the array. Otherwise say interactive is fine and
   move on.

COACHING: As we work, teach me inline — briefly, where it comes up, not saved
for the end. If a metric, plot, statistic, or convention appears that I may be
reading wrong, say what it means and which direction is good. If I state
something incorrect, correct me directly rather than working around it. Keep it
to a line or two each time; don't turn the session into a lecture.
