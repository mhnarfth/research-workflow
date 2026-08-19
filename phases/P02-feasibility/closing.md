Produce a handoff bundle for this phase. Output ONE markdown document using
exactly the block format below — I apply it with a script, so delimiters and
modes must be exact.

WRITE MODES: CREATE (file doesn't exist) | REPLACE (rewrite whole file; only
for files I gave you as input) | APPEND (add to end) |
APPEND_UNDER: ## Heading.

Dates are ISO (YYYY-MM-DD). Provenance tags use the phase NAME: [feasibility].

---

=== FILE: docs/FEASIBILITY.md | CREATE ===
<all nine sections, filled in, final. Include the gate verdict.>
=== END ===

=== FILE: docs/DECISIONS.md | CREATE ===
<one entry per decision made here — at minimum: anonymization scheme,
authorship and order, kill criterion. Format each as:

### YYYY-MM-DD — [feasibility] <decision>
**Chose:** ...
**Over:** ...
**Why:** ...
**Would revisit if:** ...
>
=== END ===

Also produce FILE blocks for any new dataset registry entries
(APPEND_UNDER the registry heading in the research-index README).

=== HANDOFF: P02-feasibility ===
Long. Cover:
1. What we decided, and the reasoning behind each decision
2. What we considered and rejected, and why
3. Current state — the gate verdict, constraints in force, codenames chosen
4. What's next, in order
5. Open questions and anything unresolved
6. What a fresh chat would get wrong without this context
7. Which files venue calibration should load

Be specific. Don't summarize away detail.
=== END ===

=== META: P02-feasibility ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
