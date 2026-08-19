# Phase Conventions

Everything in this file applies to **every** phase. Individual phase folders
only add what's specific to them.

---

## Using a phase

1. Read `PNN-<name>/README.md` — the manual, for you
2. Copy `opening.md`, fill the `<blanks>`, paste as the chat's first message
3. Work through it
4. Paste `closing.md` as the final message
5. Check `checklist.md` before you leave
6. Apply the bundle, commit, push

**The manual is never given to the chat.** Only the opening message, which is a
separate file for exactly that reason.

---

## The opening message

Every `opening.md` has the same skeleton, with phase-specific additions:

```
PHASE: <name>
WHAT I'M DECIDING: <one line>
REQUIRED CONTEXT: <files — load however your tool supports>
ATTACHMENTS: <big/single-use files, or "none">
WHAT I WANT OUT: <the artifacts>

<phase-specific framing>

COACHING: <see below>
```

`REQUIRED CONTEXT` names files, never a loading method. That's the portability
guarantee — Projects, per-chat upload, or `cat`-and-paste all work.

---

## The coaching clause

Included verbatim in every `opening.md`:

> **Coaching.** As we work, teach me inline — briefly, where it comes up, not
> saved for the end. If a metric, plot, statistic, or convention appears that I
> may be reading wrong, say what it means and which direction is good. If I
> state something incorrect, correct me directly rather than working around it.
> Keep it to a line or two each time; don't turn the session into a lecture.

This is real-time learning while working. It is **not** the same as `## Meta`
(workflow improvement, distilled later by the retro chat).

---

## The closing prompt — three parts

Every `closing.md` asks for these, in this order.

### Part A — File updates

Paste-ready blocks. One per target file, each with a mode:

```
=== FILE: docs/DECISIONS.md | APPEND ===
### 2026-08-09 — [feasibility] Anonymize the regional ISP as ISP_A
**Chose:** codename ISP_A in all tracked source
**Over:** using the real name and scrubbing before release
**Why:** deciding this at write-up last time created a global find-replace
under deadline pressure
=== END ===
```

**Write modes:**

| Mode | Means | You do |
|---|---|---|
| `APPEND` | add to the end of an existing file | scroll to bottom, paste |
| `APPEND_UNDER: ## Heading` | insert under a named heading | find heading, paste before the next one |
| `CREATE` | file doesn't exist yet | new file, paste |
| `REPLACE` | rewrite the whole file | select all, paste over |

**Constraint on REPLACE:** a phase may only REPLACE a file it received as
input. If it never saw the file, it must APPEND. Otherwise a REPLACE silently
drops content the chat never had.

Content must be final — correct provenance tag, ISO date, no placeholders,
ready to paste with zero editing.

### Part B — Handoff narrative

For the next chat. **Long.** This is the only thing that survives, and
compression is where the useful detail dies.

1. What we decided, and the reasoning behind each decision
2. What we considered and rejected, and why
3. Current state — what exists, what runs, what the numbers are
4. What's next, in order
5. Open questions and anything unresolved
6. What a fresh chat would get wrong without this context
7. Which files the next phase should load

Saved as `docs/handoffs/<phase>.md`.

### Part C — Meta

Saved **separately** as `docs/handoffs/<phase>-meta.md`. Never sent to the next
chat — it's about the workflow, not the research, and would be pure noise
downstream.

1. **Improvement note** — what would have been a smarter, faster, or more
   standard way to do what we just did?
2. **Assumptions flagged** — anything the chat inferred rather than being told.
   Surfacing these at close is when you can still correct them before they
   propagate into five downstream phases.
3. **Checklist self-check** — verify against `checklist.md`, name anything unmet
4. **Draft commit message**

At P13 the retro chat reads `cat docs/handoffs/*-meta.md` and distills it into
`LEDGER-improvements.md`. Nothing is filed along the way.

---

## Bundle format

The closing prompt asks for all three parts in **one file**, `handoff-bundle.md`,
so `tools/apply_handoff.py` can apply it in one command. Structure:

```
=== FILE: <path> | <MODE> ===
<content>
=== END ===

=== HANDOFF: <phase-name> ===
<part B>
=== END ===

=== META: <phase-name> ===
<part C>
=== END ===

=== COMMIT ===
<one-line commit message>
=== END ===
```

Download it, drop it in the repo root, run the tool. See `tools/README.md`.

---

## Splitting a phase

Numbered sub-chats in the same LLM project: `P07-exec-1`, `P04-lit-2`.

| Phase | Natural boundary |
|---|---|
| Literature | per theme, as planned in `lit-0` |
| Execution | per pipeline stage or experiment family |
| Drafting | per section group |

Same inputs each time; only a short **continuation handoff** advances
("stages 01–03 done, numbers are X, next is 04, open question is Y"). The full
three-part closing prompt runs only at the *end of the phase*, not at every
split.

Soft cap 100k tokens, hard cap 200k. Past the soft cap, split at the next
natural boundary.

---

## Mid-chat updates

When something outside the chat changes a file the chat is working from
(usually the red team changing the stage plan): **paste the delta, not the file.**

> Update — red team flagged window-length sensitivity. Adding stage 08:
> <the new lines>. Everything else unchanged.

The file is the record for future chats. The delta paste keeps the current chat
current. Two different jobs.

---

## Writing prompts that work

Four elements, used throughout these phases (see `PROMPTING.md`):

1. **Name the output type** — "produce a ranked list of cuts", not "make this
   shorter"
2. **Name what must not happen** — "do not rewrite the paper"
3. **Name the failure mode you're avoiding** — "summarizing would delete the
   caveats"
4. **Give the format** — a table with named columns produces a table
