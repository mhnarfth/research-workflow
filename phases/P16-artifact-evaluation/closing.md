Produce a handoff bundle for this phase.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [artifact-eval].

---

=== FILE: docs/AE-SUBMISSION.md | CREATE ===
<the artifact evaluation submission text: artifact identification, what the
artifacts contribute, reproducibility scope, and the honest restricted-data
statement>
=== END ===

Also produce a FILE block with the full artifact README for the PUBLIC repo,
written for a stranger. Mark it clearly — I copy it into the public repo by
hand, since that's a different repository.

=== FILE: docs/NOTES.md | APPEND_UNDER: ## Artifact evaluation ===
<what was claimed, which badges, what reproduces under which loader mode>
=== END ===

=== HANDOFF: P16-artifact-evaluation ===
Cover: badges targeted; what reproduces and how; what was scoped out and why;
and anything the evaluators will likely ask.
=== END ===

=== META: P16-artifact-evaluation ===
1. IMPROVEMENT — what would have made this easier if done earlier in the
   project? (Answers here belong in the code-planning phase next time.)
2. SELF-CHECK — against the phase checklist: anything unmet?
=== END ===

=== COMMIT ===
<one line>
=== END ===
