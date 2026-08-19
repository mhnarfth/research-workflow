Produce a handoff bundle for this change. Output ONE markdown document using
exactly the block format below — I apply it with tools/apply_handoff.py from
the research-workflow repo root, so delimiters and modes must be exact.

WRITE MODES: CREATE | REPLACE (only for files I gave you as input) | APPEND |
APPEND_UNDER: ## Heading. Dates ISO. Provenance tag: [framework].

CRITICAL: only produce FILE blocks for files I actually loaded. For anything
else that needs changing, list it under FOLLOW-UP so I can load it and run
another pass.

---

=== FILE: <path> | <MODE> ===
<final, paste-ready content>
=== END ===

=== FILE: CHANGELOG.md | APPEND_UNDER: ## Unreleased ===
- <what changed, in one line, and why>
=== END ===

=== FILE: LEDGER-improvements.md | APPEND_UNDER: ## Framework changes queued ===
<mark the originating item as done, with the date — or add follow-up items>
=== END ===

=== HANDOFF: P19-framework-<short-name> ===
1. WHAT CHANGED and why
2. WHAT WE CONSIDERED AND REJECTED — including any smaller change that was
   weighed and dismissed
3. CONSISTENCY — anything this now contradicts, or any rule it supersedes
4. FOLLOW-UP — every file that still needs changing but wasn't loaded, with
   what needs to change in each. Be exhaustive here; this is what I work from
   in the next pass.
5. VERSION — should this be a minor or major bump, and why?
=== END ===

=== META: P19-framework-<short-name> ===
1. Did the framework's own tooling handle this change cleanly? If applying this
   was awkward, that is itself a design signal — say so.
2. ASSUMPTIONS — anything you inferred about files you couldn't see
3. Anything else that shouldn't be lost
=== END ===

=== COMMIT ===
<one line>
=== END ===
