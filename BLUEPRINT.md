# Blueprint

**How this framework was built — so I can build the next one faster.**

This is not about research. It's the reusable method: the moves that produced
a working system out of a vague dissatisfaction, and the traps that were
avoided along the way.

Use it for any domain where you keep redoing something and keep getting it
slightly wrong: job search, teaching a course, running a project, a side
business, a health routine, learning a skill.

---

## Part 1 — The moves, in order

### 1. Start from a real failure, not from theory

This framework did not start with "what would a good research workflow look
like?" It started with a specific painful experience: one chat that reached
600k tokens, rate-limited to one prompt per five hours, holding the only record
of six months of work.

**Why this matters:** theory produces frameworks that are elegant and unused.
A failure produces a framework that solves something you actually feel.

**The move:** before designing anything, write an honest post-mortem of the last
time you did this badly. What went wrong, in detail, with specifics.

### 2. Separate the symptom from the cause

The obvious problem was "the chat got too big." That's a symptom. The cause was:

> There was no external record, so the chat was the only memory, so leaving it
> meant losing the project, so it had to hold everything forever.

Fixing the symptom would have produced advice like "start new chats more often"
— which fails immediately, because you can't leave a chat that holds your only
copy of the work.

**The move:** for each pain point, ask "why does this happen?" three times.
Design against the third answer.

### 3. Find the one principle everything hangs off

Once the cause was named, one sentence organized the entire design:

> **Files are the memory. Chats are disposable.**

Every later decision — handoff documents, project knowledge, the four-file phase
structure, the portability constraint — is a consequence of that sentence.

**The move:** compress your diagnosis into one sentence. If you can't, you
haven't found the principle yet. A framework with three competing principles
will contradict itself.

### 4. Separate invariants from specifics

An early draft listed five specific bugs from the last project and built checks
for each. That was **overfitting to one instance** — those exact bugs won't
recur.

Generalizing them gave the actual invariant: *silent failure is the enemy —
code that produces a plausible wrong answer costs more than code that crashes.*
That applies to any domain and any tooling.

**The move:** whenever you write a specific rule, ask "what class of thing is
this an instance of?" Keep the class. Keep one specific as an illustration.

**The counter-move:** don't over-generalize either. "Be careful" is useless.
The right altitude is the level at which the rule still tells you what to *do*.

### 5. Name the unit of work and give it a fixed shape

The framework has one unit: **the phase**. Every phase has exactly four files —
README (for you), opening (for the tool), closing (the handoff), checklist (the
gate).

Fixed shape means: nothing to invent per phase, you learn the pattern once,
gaps are visible (an empty checklist is obviously wrong), and adding a phase
later is mechanical.

**The move:** find your repeating unit. Give it a fixed skeleton. Resist making
each instance special.

### 6. Make state external, and the process stateless

Chats hold no state. Files hold all of it. That's what makes chats disposable,
tools swappable, and a two-week absence survivable.

**The generalization:** any process where the *thing doing the work* also
*holds the only record* is fragile — a person who leaves, a tool that gets
deprecated, a session that expires. Separate the two, always.

### 7. Decide automation vs. manual deliberately, and keep some things manual on purpose

Automated: applying handoff bundles, git mechanics, schedule arithmetic, figure
restyling, pre-release safety scans.

Manual **on purpose**: the `RUNLOG.md` "what surprised me" line, every
`DECISIONS.md` answer, all scope decisions, the research index.

The manual ones aren't leftovers. They're the places where *your* judgment is
the actual product, and automating them would remove the thing that makes the
work yours.

**The move:** list every step. For each, ask "if a tool did this perfectly,
would I lose something?" If yes, keep it manual and say why in writing —
otherwise future-you will automate it thinking it was an oversight.

### 8. Push irreversible decisions as early as possible

Anonymization, authorship, data constraints, and the venue's "never" list all
got moved to the earliest phase where they could be decided.

**Why:** these are cheap when made early and expensive when made late.
Anonymization decided at write-up meant a global find-replace under deadline
pressure. Decided at the gate, it costs one line.

**The move:** for each decision in your process, ask "what does this cost if I
decide it now vs. at the last possible moment?" Anything with a steep curve
moves to the front.

### 9. Build escape hatches before you need them

Every mechanism has a defined failure path: `git checkout .` undoes any bundle;
backward jumps have a rule (edit the doc, paste the delta); the red team can
re-fire; a phase can span N chats; the applier fails loudly and names the fix.

**Why:** a framework with no escape hatches gets abandoned the first time
reality doesn't match it. One that bends gets kept.

**The move:** for each rule, ask "what happens when this doesn't work?" Write
that down *inside* the rule.

### 10. Design for the amnesiac future self

The recurring test question was: *"I've been away two weeks and forgotten
everything — does this still work?"*

That question produced: the phase READMEs, `MAINTENANCE.md`, `QUICKSTART.md`,
git commands written out longhand for someone who doesn't live in git, and the
failure-case table with exact commands.

**The move:** don't design for you-now, who has all the context. Design for
you-in-six-months, who has none. If a step needs context you'd have to
reconstruct, write the context down next to the step.

### 11. Constrain for portability up front

A late question — *"is this locked to one tool?"* — surfaced one real
dependency and one design consequence: project knowledge must stay **small
enough to paste**, because pasting is the fallback that works everywhere.

That constraint improved the design independently of portability: small,
stable, cross-cutting context is better context.

**The move:** ask early — what happens if my main tool disappears? The
constraint usually makes the design better, not just more portable.

### 12. Put guardrails on the tool's authority, not just its behavior

One rule appears throughout: **the system may advise on scope; it never acts.
Every scope decision is yours.**

Similarly: write your own answer in `DECISIONS.md` *before* asking a model,
then use the model to attack it — not to generate it.

**Why:** without this, a framework that's supposed to help you think becomes one
that thinks for you, and you end up unable to defend your own work.

**The move:** name explicitly which decisions are yours by rule. Write them
down. Otherwise erosion happens gradually and invisibly.

### 13. Prefer passive capture over active discipline

Improvement notes aren't filed as you go. Each handoff carries a `## Meta`
block; once per paper, a retro chat reads them all and distills. **Zero ongoing
obligation.**

**Why:** any system requiring sustained willpower fails during the exact busy
periods when it's most needed.

**The move:** wherever you're about to require discipline, ask whether the
information can instead be a *byproduct* of something you already do.

### 14. Trigger-based beats cadence-based — but name the exceptions

Most maintenance is triggered by something you're already doing ("you submit"
→ these five things). Those survive on their own.

The handful with no trigger — the yearly distillation — are listed separately
and explicitly, because **that's exactly where systems rot.**

**The move:** sort every maintenance task into triggered vs. scheduled. Attach
triggered ones to existing events. Put scheduled ones on a calendar, and accept
that anything on neither list will not happen.

### 15. Build the foundation first, leaves last

Order was: principle → repos and context architecture → the four-file
convention → the shared tool → then all 18 phases in batches.

Anything wrong in the foundation propagates into 72 leaf files. Anything wrong
in a leaf is one file.

**The move:** identify what everything else references. Build and validate that
first. Deliberately delay the parts that feel most concrete and satisfying.

---

## Part 2 — The process that produced it

The method mattered as much as the moves.

### Iterate on paper before building anything

Roughly twenty exchanges happened before a single file was written. Several
whole designs were proposed and discarded — a merge chat that turned out
unnecessary, a shared-repo lineage scheme that collapsed under one objection,
timestamps that would never have been used.

Discarding a paragraph is free. Discarding 72 built files is not.

### Read it back out loud, with your confusions attached

The single most productive habit: taking each proposal and narrating a response
to it — what was understood, what wasn't, what felt wrong, what raised a new
question.

This caught things a "sounds good" would have buried: that the reverse schedule
needed ratios rather than fixed offsets, that figure sketches are a target
rather than a contract, that a merge chat had no job, that meta notes would
bloat the next chat.

**Do this.** Narrate rather than approve. Confusion is signal.

### Say "I don't understand this part"

Several times the response was some version of *"I didn't get this at all."*
Every one of those produced a better explanation and often a better design —
the Obsidian vault mechanics, the write modes, the compression failure mode.

Not understanding something is usually evidence that it's explained badly or
designed badly. It's rarely just you.

### Push back on the specific, not the general

The most valuable corrections were narrow and concrete:

- *"the bug list is overfit — I won't hit those same bugs"* → produced the
  invariants
- *"I won't reuse the code, so why share a repo?"* → collapsed an
  over-engineered scheme
- *"scope cutting is my decision, don't put it anywhere"* → became a standing
  guardrail
- *"30-40% recent isn't always possible"* → target, not constraint

Narrow objections improve a design. "I don't like it" doesn't.

### Delay building until the whole map exists

The explicit instruction — *walk all 18 phases before producing anything* — was
correct. Later phases changed earlier ones: artifact evaluation forced three
loader modes into code planning; the compression failure mode changed drafting;
DOI placement moved from post-submission to camera-ready.

Building P01 early would have meant rebuilding it.

### Pre-fill everything you can

Nothing shipped as an empty skeleton. Real papers, real dataset quirks, real
grant numbers, real rejection reasons, real notation extracted from actual
papers — with `<FILL: ...>` markers for the rest.

**Why:** an empty template is a task. A pre-filled one is a draft to correct,
which is far easier to start.

---

## Part 3 — Using this for the next framework

### The sequence

1. **Post-mortem.** Write the last failure honestly, with specifics.
2. **Root cause.** Three "why"s. Design against the third.
3. **One principle.** Compress it to a sentence.
4. **Unit of work.** Name it. Give it a fixed shape.
5. **State model.** Where does state live? Not in the thing doing the work.
6. **Map the whole thing on paper.** All phases. Change nothing until the map
   is complete.
7. **Read it back with your confusions attached.** Iterate until nothing is
   unclear.
8. **Automation split.** What's automated, what's manual on purpose, why.
9. **Early decisions.** Which choices are cheap now and expensive later?
10. **Guardrails.** Which decisions are yours by rule?
11. **Escape hatches.** For each rule: what happens when it doesn't work?
12. **Amnesia test.** Read it as someone with no context.
13. **Build foundation first**, leaves in batches, pre-filled.
14. **Maintenance map.** Triggered vs. scheduled.
15. **Run it once**, then revise from real friction rather than imagination.

### Where each artifact came from

If you're building the equivalent for another domain, these map across:

| Artifact | Its job | Domain-general form |
|---|---|---|
| `WORKFLOW.md` | The map | The full system, one document |
| `QUICKSTART.md` | The TLDR | One page for when there's no time |
| `MAINTENANCE.md` | What to update, when | Triggered + scheduled upkeep |
| Phase `README.md` | How this step works | Per-step manual, for you |
| Phase `opening.md` | Setup for the tool | The invocation, with blanks |
| Phase `closing.md` | Structured output | What must be produced to move on |
| Phase `checklist.md` | The gate | What must be true to leave |
| `DECISIONS.md` | Provenance | Why things are the way they are |
| `RUNLOG.md` | Raw observation | What happened, unfiltered |
| Ledgers | Accumulated learning | What to adopt, read, do differently |
| The applier tool | Removes friction | Automating the boring part of the loop |

### Two failure modes to watch

**Over-specification.** A framework that dictates every keystroke gets
abandoned at the first mismatch with reality. The hybrid — verbatim where it's
always the same, checklist where it varies — is the right altitude.

**Fossilization.** A framework never revised from real use becomes a museum
piece. That's what `LEDGER-improvements.md` and the per-run retro are for: the
system is supposed to change, and the mechanism for changing it is part of the
system.

### The one-line version

> **Find the real failure. Name its cause. Compress it to one principle.
> Externalize state. Map it all on paper. Keep judgment manual on purpose.
> Build the foundation first. Run it, then fix it from friction rather than
> imagination.**
