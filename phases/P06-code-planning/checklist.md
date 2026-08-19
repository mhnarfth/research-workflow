# P06 — Checklist

Before leaving this phase:

- [ ] Every sketched figure and table is produced by some stage
- [ ] Every stage says what it **caches**, so analysis never retrains
- [ ] Estimated runtime recorded per stage
- [ ] No literal number with meaning lives outside `config/config.py`
- [ ] Derivable quantities are **derived**, not hardcoded twice
- [ ] **Metric direction table written** — I can look up whether a number is good
- [ ] Loader has all three modes: `real`, `public_only`, `synthetic`
- [ ] `src/plotting.py` exists; `save_figure()` writes the PDF **and**
      `results/figdata/<name>.json`
- [ ] A figdata JSON is sufficient to redraw its figure with no pipeline access
- [ ] All figure text is ASCII — no en/em dashes
- [ ] `src/` has no side effects on import
- [ ] `config/local_paths.py` is gitignored and holds the only real names
- [ ] **Pilot run passes end to end**

Do not start P07 until the pilot passes. Finding a plumbing bug after five
seeds is the whole thing this step prevents.
