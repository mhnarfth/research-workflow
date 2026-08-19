Produce a handoff bundle for this phase.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [post-submission].

---

=== FILE: docs/NOTES.md | REPLACE ===
<the completed working notes, in full. Only produce this block if I gave you
NOTES.md as input; otherwise use APPEND blocks for the new sections.>
=== END ===

=== FILE: docs/CLAIMS.md | APPEND ===
## As submitted
<frozen: every number exactly as it appears in the submitted paper, with source
files. The rebuttal will use this section.>
=== END ===

=== FILE: docs/NOTES.md | APPEND_UNDER: ## Extensions ===
<ranked extension ideas, each with: what it is, why it matters, rough cost, and
which objection to this paper it answers>
=== END ===

=== FILE: docs/NOTES.md | APPEND_UNDER: ## Collection note ===
<what this would need if folded into a larger work: reframing, notation
alignment, missing connective tissue>
=== END ===

Also produce FILE blocks for:
- the research-index paper row (status, venue, date, repo, key result)
- one scannable line per extension idea in the research-index idea backlog,
  tagged with this paper as the source

=== HANDOFF: P13-post-submission ===
Cover: what was preserved and where; the frozen claims; ranked extensions; and
what P14 will need when reviews arrive.
=== END ===

=== META: P13-post-submission ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
