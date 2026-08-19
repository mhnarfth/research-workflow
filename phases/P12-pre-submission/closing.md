Produce a handoff bundle for this phase.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [pre-submission].

---

=== FILE: docs/DECISIONS.md | APPEND ===
### YYYY-MM-DD — [pre-submission] triage dispositions
<every attack and what I decided to do about it, including anything dismissed
and WHY it was dismissed>
=== END ===

=== FILE: docs/RELEASE.md | CREATE ===
<what ships and what doesn't, with the invertibility reasoning; the exact
commands to build the public repo fresh; the preflight items to check>
=== END ===

=== FILE: docs/NOTES.md | APPEND_UNDER: ## Submission ===
<venue, date submitted, public repo URL, what the artifact appendix claims,
anything conceded in Limitations as a result of triage>
=== END ===

=== HANDOFF: P12-pre-submission ===
Cover: what was triaged and how; what was fixed vs. conceded vs. deferred;
what shipped in the public repo and what was withheld; the submission record;
and what post-submission needs to do.
=== END ===

=== META: P12-pre-submission ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
