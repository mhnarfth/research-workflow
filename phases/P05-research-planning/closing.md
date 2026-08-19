Produce a handoff bundle for this phase. Output ONE markdown document using
exactly the block format below — I apply it with a script, so delimiters and
modes must be exact.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading.

Dates are ISO (YYYY-MM-DD). Provenance tags use the phase NAME: [research-plan].

---

=== FILE: docs/RESEARCH-PLAN.md | CREATE ===
<final content:
- RESEARCH QUESTIONS
- CLAIMED CONTRIBUTIONS — each with the evidence required and what would falsify it
- FIGURE SKETCHES — table with columns: ID | working title | what it shows |
  supports which contribution | what it looks like if the claim is false
- TABLE SKETCHES — same structure
- DRAFT ABSTRACT — clearly marked as the abstract I HOPE to write, dated
- NOTATION — symbols this paper will use, and any conflicts with prior papers>
=== END ===

=== FILE: docs/DECISIONS.md | APPEND ===
### YYYY-MM-DD — [research-plan] <the claim and contributions>
**Chose:** ...
**Over:** ...
**Why:** ...
**Would revisit if:** ...
=== END ===

If any new notation is introduced, also produce a FILE block appending to
research-index NOTATION.md (APPEND_UNDER the symbol table heading).

=== HANDOFF: P05-research-planning ===
Long. Cover:
1. What we decided — RQs, contributions, and the reasoning
2. What we considered and cut, and why
3. Current state — the figure and table sketches in full, since these are the
   target code planning builds toward
4. What's next, in order
5. Open questions
6. What a fresh chat would get wrong without this context
7. Which files code planning should load
=== END ===

=== META: P05-research-planning ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
