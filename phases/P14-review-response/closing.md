Produce a handoff bundle for this phase.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [review-response].

---

=== FILE: research-index/reviews/<venue><year>.md | CREATE ===
<the archive: each review point, my disposition, and what actually changed.
This is the file the next paper's adversarial review will be checked against.>
=== END ===

=== FILE: docs/DECISIONS.md | APPEND ===
### YYYY-MM-DD — [review-response] <what I decided about the reviews>
<including, if rejected: the next venue and why>
=== END ===

<IF REJECTED, also:>
=== FILE: docs/VENUE.md | REPLACE ===
<only if I gave you VENUE.md as input: updated ladder with the new target, and
a recomputed schedule for the new deadline>
=== END ===

=== HANDOFF: P14-review-response ===
Cover: what the reviews said; what I agreed with and what I contested; what
changed; and — if rejected — the next venue, what must change first, and the
new schedule.
=== END ===

=== META: P14-review-response ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. PATTERN — does anything in these reviews resemble objections raised on my
   previous papers? If so, name the pattern; it belongs in PATTERNS.md.
4. SELF-CHECK — against the phase checklist: anything unmet?
=== END ===

=== COMMIT ===
<one line>
=== END ===
