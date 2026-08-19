Produce a handoff bundle for this phase. Output ONE markdown document using
exactly the block format below — I apply it with a script, so delimiters and
modes must be exact.

WRITE MODES: CREATE (file doesn't exist) | REPLACE (rewrite whole file; only
for files I gave you as input) | APPEND (add to end) |
APPEND_UNDER: ## Heading (insert under a named heading).

Dates are ISO (YYYY-MM-DD). Provenance tags use the phase NAME: [ideation].

---

=== FILE: <path> | <MODE> ===
<final, paste-ready content — no placeholders>
=== END ===

Produce FILE blocks for:
- research-index rejection log — APPEND_UNDER the rejection log heading — one
  row per rejected idea: date | idea | verdict | why | revisit if. The "why"
  must be specific enough to be useful to me in a year.
- research-index idea backlog — APPEND_UNDER the backlog heading — anything
  parked rather than rejected.
- The chosen idea, one paragraph, to carry into the feasibility gate.

=== HANDOFF: P01-ideation ===
Long. This is the only thing that survives this chat. Cover:
1. What we decided, and the reasoning behind each decision
2. What we considered and rejected, and why
3. Current state — the chosen idea, its scope, what's assumed
4. What's next, in order
5. Open questions and anything unresolved
6. What a fresh chat would get wrong without this context
7. Which files the feasibility gate should load

Be specific — names, numbers, terms. Don't summarize away detail.
=== END ===

=== META: P01-ideation ===
1. IMPROVEMENT — what would have been a smarter, faster, or more standard way
   to do what we just did?
2. ASSUMPTIONS — anything you inferred rather than being told. List them so I
   can correct them before they propagate downstream.
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Nothing above that belongs here but shouldn't be lost.
=== END ===

=== COMMIT ===
<one line>
=== END ===
