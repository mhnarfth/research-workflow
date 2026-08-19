# P07 — Checklist

## Per session
- [ ] `RUNLOG.md` entry written — ran / got / **surprised by**
- [ ] "Surprised by" is not blank. If I don't understand something, *that's the
      entry* — write it and ask
- [ ] Committed and pushed

## Before leaving the phase
- [ ] Every stage in `STAGE-PLAN.md` has run successfully
- [ ] Every figure has a matching `results/figdata/<name>.json`
- [ ] Every figdata JSON can redraw its figure with no pipeline access
- [ ] Metric tables written to `results/metrics/`
- [ ] Every non-obvious choice is in `DECISIONS.md`, tagged `[execution]`
- [ ] Superseded scripts moved to `archive/` with a line in `archive/README.md`
      — **archived, not deleted**
- [ ] Nothing hardcoded in stage code that belongs in config
- [ ] I know which results reproduce reliably and which don't
- [ ] **I did not rerun anything to get a more favorable number**
- [ ] The execution debrief exists and is exhaustive

## The debrief test

Read it as if you'd never seen the project. Could you write the Limitations
section from it? Could you explain why each design choice was made? If not,
it's too compressed — go back and ask for more.
