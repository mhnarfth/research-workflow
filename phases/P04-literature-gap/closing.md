Produce a handoff bundle for this phase. Output ONE markdown document using
exactly the block format below — I apply it with a script, so delimiters and
modes must be exact.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading.

Dates are ISO (YYYY-MM-DD). Provenance tags use the phase NAME: [literature].

NOTE: if this is a mid-phase split (lit-0 → lit-1, or lit-1 → lit-2), produce
ONLY the HANDOFF and COMMIT blocks as a short continuation note. The full
bundle below runs at the END of the phase.

---

=== FILE: docs/LITERATURE-PLAN.md | CREATE ===
<lit-0 only: themes, chat split, questions each chat must answer>
=== END ===

=== FILE: docs/LITERATURE.md | CREATE ===
<final content:
- GAP STATEMENT — one paragraph, what is missing and why it matters
- THEMES — per theme: what the cluster argues, key papers, where they disagree
- PAPERS THAT COMPLICATE MY CLAIM — listed separately, not buried
- YEAR HISTOGRAM — count by year, so the shape is visible
- DRAFT RELATED WORK STRUCTURE — subsections, and for each citation the
  argumentative job it does
- PROVENANCE — every citation marked [SEARCHED] with URL, or [RECALL] pending
  my verification>
=== END ===

Do NOT produce a references.bib block — I build that in Zotero and Better
BibTeX exports it. Instead list the papers I need to add to the Zotero
collection, with enough detail to find each one.

=== HANDOFF: P04-literature-gap ===
Long. Cover:
1. What we decided — the gap, and why it's a real gap
2. What we considered and set aside, and why
3. Current state — themes covered, papers vetted, year distribution, anything
   still unverified
4. What's next, in order
5. Open questions
6. What a fresh chat would get wrong without this context
7. Which files research planning should load
=== END ===

=== META: P04-literature-gap ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet? In particular,
   flag any citation still marked [RECALL].
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
