Produce a handoff bundle for this phase. Output ONE markdown document using
exactly the block format below — I apply it with a script, so delimiters and
modes must be exact.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading.

Dates are ISO (YYYY-MM-DD). Provenance tags use the phase NAME: [code-plan].

---

=== FILE: docs/STAGE-PLAN.md | CREATE ===
<final content:
- STAGES — table: # | reads | writes | caches | est. runtime | produces which
  figures/tables
- CONFIG KNOBS — table: name | primary or derived | value or formula | why
- METRIC DIRECTION TABLE — metric | direction | typical range | expected if the
  claim holds
- LOADER MODES — real / public_only / synthetic, and what each supports
- PILOT RUN — exactly what to run, and what output means the plumbing works
- SLURM — needed or not, with the reason>
=== END ===

=== FILE: docs/DECISIONS.md | APPEND ===
### YYYY-MM-DD — [code-plan] <non-obvious design choices>
<one entry per choice a future reader might "simplify" without knowing the
reason — derived constants, split-before-window, per-unit normalization, etc.>
=== END ===

Also produce FILE blocks with the actual starting code for:
- config/config.py
- src/plotting.py (palette, knobs, save_figure writing PDF + figdata JSON)

=== HANDOFF: P06-code-planning ===
Long. Cover:
1. What we decided, and the reasoning behind each design choice
2. What we considered and rejected, and why
3. Current state — full stage plan, since execution builds directly from it
4. What's next, in order (starting with the pilot run)
5. Open questions
6. What a fresh chat would get wrong without this context
7. Which files execution should load
=== END ===

=== META: P06-code-planning ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told, especially about
   my data's schema or shape
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
