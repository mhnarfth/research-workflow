# P19 — Checklist

## Before changing anything
- [ ] **No paper is mid-flight** — or if one is, this change is queued, not
      applied
- [ ] The change addresses a **real friction** I actually hit, not an
      imagined improvement
- [ ] I diagnosed the cause, not just the symptom
- [ ] I considered a **smaller** change first — editing a phase beats adding one
- [ ] Loaded the right context: `bundle_context.py` preset **plus**
      `grep -rn "<the thing>" .` to catch what the preset missed

## Consistency
- [ ] Doesn't contradict the core principle
- [ ] Doesn't break the four-file phase convention
- [ ] Doesn't weaken a standing rule without explicitly retiring it
- [ ] Doesn't move a decision from me to the tool
- [ ] If a new phase: it has all four files, and it's in the tables in
      `WORKFLOW.md` **and** `QUICKSTART.md`

## Applying
- [ ] Clean tree before running `apply_handoff.py`
- [ ] `git diff` reviewed
- [ ] Every file in FOLLOW-UP either handled in a second pass or logged

## Releasing
- [ ] `CHANGELOG.md` entry written
- [ ] Version bumped — minor for additions, **major** if the bundle format or
      four-file convention changed
- [ ] `git tag vX.Y && git push --tags`
- [ ] Originating item in `LEDGER-improvements.md` marked done

## Sanity
- [ ] The framework still fits in my head. If it doesn't, the right change is
      **removal**, not addition
