Produce a handoff bundle for this phase. Output ONE markdown document using
exactly the block format below — I apply it with a script, so delimiters and
modes must be exact.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading.

Dates are ISO (YYYY-MM-DD). Provenance tags use the phase NAME: [venue].

---

=== FILE: docs/VENUE.md | CREATE ===
<final content: ladder (target/up/down/never with reasons), style observations
table, the 2 named style exemplars with full citations, preprint policy,
artifact-evaluation applicability, and the dated reverse schedule.>
=== END ===

=== FILE: docs/DECISIONS.md | APPEND ===
### YYYY-MM-DD — [venue] <venue choice>
**Chose:** ...
**Over:** ...
**Why:** (nature of the contribution, not amount of material)
**Would revisit if:** ...
=== END ===

Also produce a FILE block appending to the venue notes table in the
research-index README (APPEND_UNDER the venue notes heading) so I never
re-derive this venue's rules.

=== HANDOFF: P03-venue-calibration ===
Long. Cover:
1. What we decided, and the reasoning
2. What we considered and rejected — especially venues ruled out, and why
3. Current state — target, ladder, schedule dates, style constraints
4. What's next, in order
5. Open questions
6. What a fresh chat would get wrong without this context
7. Which files the literature phase should load
=== END ===

=== META: P03-venue-calibration ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
