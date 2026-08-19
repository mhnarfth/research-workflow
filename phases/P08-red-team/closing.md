Produce a handoff bundle for this phase. Output ONE markdown document using
exactly the block format below.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [red-team].

This phase has TWO deliverables that matter: the record, and a delta I paste
into my live execution chat.

---

=== FILE: docs/NOTES.md | APPEND_UNDER: ## Red team ===
<the record: dated attack list in priority order, the experiment recommended
for each, the cost estimate, and which claims should be weakened rather than
defended. Include the reasoning — future me needs to know why an experiment
was added.>
=== END ===

=== FILE: docs/STAGE-PLAN.md | REPLACE ===
<ONLY if I gave you STAGE-PLAN.md as input. Reproduce it in full with the new
defensive stages folded in — same format, same existing rows preserved, new
stages added in place. If I did not give it to you, omit this block entirely
and use APPEND instead.>
=== END ===

=== FILE: docs/DECISIONS.md | APPEND ===
### YYYY-MM-DD — [red-team] <what changed and why>
=== END ===

=== HANDOFF: P08-red-team ===
Part 1 — the full attack list and reasoning, for the record.

Part 2 — DELTA PARAGRAPH FOR THE EXECUTION CHAT. Write a short standalone
paragraph I can paste directly into my live execution chat. It must state what
changed and why, name the new stages concretely, and say that everything else
is unchanged. Do not restate the whole stage plan — the chat already has it.
Mark this section clearly so I can find and copy it.
=== END ===

=== META: P08-red-team ===
1. IMPROVEMENT — a smarter, faster, or more standard way to have done this?
2. ASSUMPTIONS — anything you inferred rather than being told
3. SELF-CHECK — against the phase checklist: anything unmet?
4. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
