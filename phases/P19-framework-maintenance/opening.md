PHASE: Framework maintenance

WHAT I'M DECIDING: how to change my research workflow framework, and what else
that change touches.

REQUIRED CONTEXT: <output of tools/bundle_context.py — see the preset table in
this phase's README>
ATTACHMENTS: <LEDGER-improvements.md if the change comes from a retro>

WHAT I WANT OUT: a handoff bundle that applies cleanly with apply_handoff.py,
plus a CHANGELOG entry.

---

WHAT I WANT TO CHANGE:
<describe it. Be specific about the problem, not just the proposed fix — the
fix may be wrong.>

WHERE IT CAME FROM:
<retro / friction during paper X / yearly review / a phase I never used>

CURRENT FRAMEWORK VERSION: <from CHANGELOG.md>

---

HOW TO WORK THIS:

1. DIAGNOSE FIRST. Is my proposed fix aimed at the symptom or the cause? If the
   underlying problem is different from what I described, say so before we
   design anything. A framework change made against a symptom adds weight
   without removing pain.

2. BLAST RADIUS. Given the files I've loaded, tell me every place this change
   propagates — including any file I did NOT load that you can infer must be
   affected. Name those explicitly so I can go get them; do not guess at their
   contents or write blocks for files you haven't seen.

3. CONSISTENCY CHECK. Does this change contradict anything already in the
   framework? Specifically:
   - the core principle (files are the memory, chats are disposable)
   - the four-file phase convention
   - the standing rules
   - the guardrail that scope decisions are always mine
   If it contradicts one of those, say so. Either the change is wrong or the
   rule is — but they can't both stand.

4. MINIMALITY. Is there a smaller change that solves the same problem? Prefer
   editing an existing phase over adding one. A framework that grows a phase
   per annoyance becomes unusable.

5. Then produce the change.

Do not rewrite files I haven't given you. If a file needs changing and you
don't have it, say so and stop.

COACHING: As we work, teach me inline — briefly, where it comes up. If I state
something incorrect about my own framework, correct me directly.
