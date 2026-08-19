# Changelog

Framework versions. A paper runs on the version it started with — record that
version in the project's `docs/NOTES.md` at P02. Nothing is retrofitted.

**Minor bump** — added phases, changed rules, new tools.
**Major bump** — the bundle format or the four-file phase convention changed.
Those break compatibility with in-flight papers.

---

## Unreleased

<!-- P19 appends here. Move to a version heading when you tag. -->

---

## v1.1 — 2026-08-19

**Added**
- `P19-framework-maintenance` — the framework's own phase, for changing it
- `tools/bundle_context.py` — assembles only the files a change touches
- `CHANGELOG.md` and framework versioning
- `BLUEPRINT.md` — the meta-method: how this framework was built, reusable for
  building others

**Rules established**
- Collect during, change between: never change the framework mid-paper
- A paper runs on the framework version it started with
- Existing project repos are clones, not links — template changes reach the
  next clone only

## v1.0 — 2026-08-19

Initial framework.

- `WORKFLOW.md`, `QUICKSTART.md`, `MAINTENANCE.md`, `PROMPTING.md`, `READING.md`
- Three ledgers: tooling, reading, improvements
- `phases/README.md` — the four-file convention, bundle format, write modes,
  coaching clause
- `tools/apply_handoff.py` + docs
- Phases P00–P18, each with README, opening, closing, checklist
- `research-index` — tracker, dataset registry, backlog, rejection log, venue
  notes, funding, `PROFILE.md`, `NOTATION.md`, `CONTACTS.md`, `reviews/`
- `research-project-template` — config, `src/plotting.py` with figdata,
  `analysis/restyle_figures.py`, gitignore
