Produce a handoff bundle for this phase. Output ONE markdown document using
exactly the block format below.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [paper-plan].

---

=== FILE: docs/SECTION-PLAN.md | CREATE ===
<final content:
- SECTION TABLE — section | pages | word budget | contains | figures/tables |
  contribution delivered
- FIGURES SHIPPING — with the paper-facing number for each and its source file
- FIGURES CUT — with the reason
- TABLES SHIPPING / CUT — same
- FIGURE NUMBER MAP — generated filename -> paper figure number, so the two
  never have to be reconciled later>
=== END ===

=== FILE: docs/CLAIMS.md | CREATE ===
## As planned

<every number the paper will report:
| # | claim | value | source artifact file | verified |
Include a HONEST-FRAMING section listing any claim that was weakened here and
the wording it was weakened to.>
=== END ===

=== FILE: docs/DECISIONS.md | APPEND ===
### YYYY-MM-DD — [paper-plan] <framing and structure decisions>
<include any claim weakened, and why>
=== END ===

If the finding changed from what was planned, also:

=== FILE: docs/NOTES.md | APPEND_UNDER: ## What actually happened ===
<how the framing shifted from the P05 draft abstract, and what caused it>
=== END ===

=== HANDOFF: P09-paper-planning ===
Long. Cover:
1. What we decided — structure, what ships, how claims are framed
2. What we cut, and why
3. Current state — the full section plan and claims ledger, since drafting
   works directly from them
4. What's next, in order
5. Open questions
6. What a fresh chat would get wrong without this context
7. Which files drafting should load, including the style exemplars from VENUE.md
=== END ===

=== META: P09-paper-planning ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet? In particular,
   flag any number in the ledger that does not trace to a file.
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
