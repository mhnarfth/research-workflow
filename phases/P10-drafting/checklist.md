# P10 — Checklist

## Drafting
- [ ] Style exemplars from `VENUE.md` were attached and actually read
- [ ] Each section is within its word budget
- [ ] **Every number in the text is in `CLAIMS.md`** — verified, not assumed
- [ ] Every citation key resolves in `references.bib`
- [ ] No invented citations
- [ ] Limitations, caveats, and named outliers are present and intact

## Figures
- [ ] `analysis/restyle_figures.py` reads only from `results/figdata/`
- [ ] Restyling did not touch the pipeline or the GPU
- [ ] All styling knobs are variables at the top of the file
- [ ] Figure text is ASCII — no en/em dashes in the PDF text layer
- [ ] Figures are legible at print size
- [ ] Paper figure numbers match the map in `SECTION-PLAN.md`

## Compression
- [ ] I asked for a **cut list**, never a shorter paper
- [ ] Output was a ranked table with exact quoted text
- [ ] **Nothing was regenerated** — I applied cuts by hand in the `.tex`
- [ ] No limitation, caveat, named outlier, or negative result was cut
- [ ] Unused cuts kept in reserve
- [ ] Every figure and table is referenced in the text
- [ ] All cross-references resolve

## Versioning
- [ ] `git tag draft-vN` at each milestone
- [ ] Milestone PDF in `paper/versions/<date>_<label>.pdf`
- [ ] Page count verified **after** the final edits — floats move

## Advisor
- [ ] Draft sent, with as much lead time as the schedule allows
- [ ] Sent PDF saved to `paper/versions/`
