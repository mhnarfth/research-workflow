MID-PHASE SPLIT? If more execution chats follow, output ONLY a short
continuation note plus a COMMIT block:

=== HANDOFF: P07-exec-<N> ===
Stages done, the numbers they produced, what's next, and any open question the
next chat needs. Keep it short — the full debrief runs at the end of the phase.
=== END ===

=== COMMIT ===
<one line>
=== END ===

---

END OF PHASE? Produce the full handoff bundle below.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [execution].

=== FILE: docs/DECISIONS.md | APPEND ===
<every non-obvious choice made during execution, one entry each>
=== END ===

=== FILE: docs/NOTES.md | APPEND_UNDER: ## What actually happened ===
<design decisions that mattered, bugs found and fixed with cause and fix,
result stability — what reproduces and what doesn't>
=== END ===

=== FILE: archive/README.md | APPEND ===
<any superseded script: what it did, what superseded it, and why it's kept>
=== END ===

=== HANDOFF: P07-execution ===
THE EXECUTION DEBRIEF. This is the only record that reaches the paper-writing
phases, and details that seem minor now are often what makes a paper
defensible. Be exhaustive. Do not compress.

Cover everything that happened: what we built; every number produced and the
file it came from; every figure and table generated and where it lives. What we
tried that didn't work. Where we got stuck and why. What we changed mid-course
and what forced the change. What surprised us. What turned out harder or easier
than expected. Anything about the data, the environment, or the method that a
reader would need to know. Anything I said in passing that turned out to
matter. Anything I flagged in RUNLOG.md that we never resolved.

Then add a final section: ANYTHING ELSE from this phase that doesn't fit the
above but shouldn't be lost.

Don't summarize away specifics — names, numbers, file names, exact settings.
=== END ===

=== META: P07-execution ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
