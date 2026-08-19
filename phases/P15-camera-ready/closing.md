Produce a handoff bundle for this phase.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [camera-ready].

---

=== FILE: docs/NOTES.md | APPEND_UNDER: ## Publication ===
<what changed for camera-ready and why; the DOI; the release tag; publication
date if known>
=== END ===

=== FILE: docs/DECISIONS.md | APPEND ===
### YYYY-MM-DD — [camera-ready] <any judgment call on required vs optional changes>
=== END ===

Also produce a FILE block updating this paper's row in the research-index
(status, DOI, publication date).

=== HANDOFF: P15-camera-ready ===
Cover: what changed, the DOI, what's left (artifact evaluation? talk? poster?),
and the deadlines attached to each.
=== END ===

=== META: P15-camera-ready ===
1. IMPROVEMENT — anything about this process worth doing differently next time?
2. SELF-CHECK — against the phase checklist: anything unmet?
=== END ===

=== COMMIT ===
<one line>
=== END ===
