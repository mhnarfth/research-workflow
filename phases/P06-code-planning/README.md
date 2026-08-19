# P06 — Code Planning

## Purpose

Turn the figure and table sketches into a pipeline that produces exactly them.

## What this phase decides

**1. Stages.** A stage is one script in `pipeline/` — one step. For each:
what it reads, what it writes, **what it caches** (so the next stage loads
instead of recomputing), and estimated runtime.

**2. Config knobs.** Every number that means something lives in
`config/config.py`. Anything derivable is **derived, never duplicated** — two
independently hardcoded twins will silently disagree eventually, and produce
plausible-but-wrong figures.

**3. The metric direction table.** For every metric the pipeline produces,
written down now while you're calm rather than while staring at output:

```
reconstruction MAE  — lower is better — typical 0.1-0.5 — fed should beat local-only
linear probe acc.   — higher is better — 0.5 is chance, 1.0 perfect
p-value             — lower = stronger evidence — <0.05 conventional threshold
```

This goes in `STAGE-PLAN.md` and into project knowledge, so every chat has it
too. It's what turns "I don't know if this number is good" into a lookup.

**4. Three loader paths — decided now, not at artifact evaluation.**
One loader, three modes:

| Mode | For |
|---|---|
| `real` | your actual data |
| `public_only` | just the public dataset — an outside evaluator gets a working pipeline and a documented subset of results |
| `synthetic` | correctly-shaped fake data — reproduces nothing numerically, but the pipeline runs for anyone |

Retrofitting this after the paper is written means rewriting the loader.

**5. `src/plotting.py`.** Palette, style knobs, ASCII-only rule, and
`save_figure()` that writes **both** the PDF and `results/figdata/<name>.json`.
Set up here so every figure gets its JSON automatically, forever. That JSON is
what lets you restyle at P10 and again at P17 without touching the GPU.

**ASCII only in figure text.** matplotlib's PDF backend renders en/em dashes
visually but silently drops them from the embedded text layer, breaking search,
copy, and publisher full-text indexing.

**6. Slurm — optional.** Record estimated runtime per stage. If any stage
exceeds ~6 hours or a sweep exceeds ~20 configurations, design it as a Slurm
array with `--dependency=afterok` and `--mail-type=END,FAIL`. Below that,
interactive is less friction.

## Structure

`src/` is importable library code with **no side effects on import**.
`pipeline/` is scripts you run. That split is why you never end up duplicating
a class to avoid triggering a training run.

## Ends with a pilot run

Whole pipeline, one seed, tiny subset, end to end. Validates the plumbing in
minutes instead of after fifteen minutes × five seeds. **Do not proceed to P07
until the pilot passes.**

## Output

`docs/STAGE-PLAN.md` · populated `config/config.py` · `src/plotting.py` ·
passing pilot run
