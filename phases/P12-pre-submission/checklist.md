# P12 — Checklist

## Triage
- [ ] Every attack and every advisor comment has a disposition in `DECISIONS.md`
- [ ] Anything invalidating a claim in `CLAIMS.md` went **back to code**
- [ ] Every dismissal has a stated reason, not just "no time"
- [ ] Limitations section reflects everything conceded

## Release
- [ ] Public repo built **fresh** — not a flipped private repo
- [ ] `grep -ri "<provider name>" .` returns nothing
- [ ] `grep -ri "/mnt/" .` finds no real paths in tracked source
- [ ] No `.npz`, `.pt`, or other file invertible to restricted data
- [ ] Metric tables and paper figures included
- [ ] `README`, `LICENSE`, `CITATION.cff`, `requirements.txt` present
- [ ] `preflight.py` run and reviewed
- [ ] Pushed, tagged `<venue><year>-submitted`
- [ ] **URL in the paper resolves to something truthful**
- [ ] **No DOI yet** — that's P15

## Submission
- [ ] Page limit verified **after** final edits (floats move)
- [ ] Every number in the text matches `CLAIMS.md` one final time
- [ ] All form fields complete
- [ ] LLM-usage disclosure, if the venue asks
- [ ] Funding acknowledgments pulled from the index, not memory
- [ ] Artifact appendix included if the venue has one
- [ ] Figure text is searchable in the PDF (ASCII rule held)
- [ ] References complete, no broken keys
- [ ] **Submitted with at least 24 hours to spare**

## After
- [ ] Index row updated to Submitted, with the date
- [ ] Go straight to P13. Do not skip it — that's where provenance is preserved
