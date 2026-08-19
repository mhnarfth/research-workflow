# P07 — Execution

**Several chats: `P07-exec-1`, `P07-exec-2`, …** Split per pipeline stage or
per experiment family.

## The working loop

**When a stage errors:** paste the traceback into the same execution chat, get
a fix, apply, rerun. Same chat — it has the code in context. This is normal and
fine.

**When a stage succeeds:** paste the *summary* output. Key numbers, shapes,
what it printed. Not everything.

**The trap to avoid.** On INDIS, everything got pasted — every output, every
figure — and the chat drove. That's what ballooned the context to 600k and made
the work feel like orchestration rather than research. So: **read the output
yourself first**, then paste what the chat needs to make the next decision. If
you don't know whether a number is right, that's the moment to think and to
check the metric direction table — not to paste.

## `RUNLOG.md` — you write this, by hand

Three lines per **session** (one sitting where you ran something — not per
chat, not per day):

```
## 2026-07-14
- **Ran:** stage 03, seed 42
- **Got:** local-only MAE 0.26, worse than federated 0.24
- **Surprised by:** the local curve dips below the others around epoch 250 —
  that contradicts the table and I don't know why
```

**Never leave "surprised by" blank because you don't understand something.**
Not understanding *is* the entry. Write what you saw and that it doesn't make
sense, then paste it into the chat and ask. On INDIS that exact pattern caught
the survivorship-bias bug — the observation came first, the explanation after.

If genuinely nothing was unexpected, write "nothing unexpected." That's
information too.

This is the one thing in the framework that stays manual, deliberately. "What
surprised me" is your observation; a chat can't have it. Thirty seconds, and
it's what feeds the debrief and eventually the paper.

## The execution debrief

The real deliverable of this phase, produced by the closing prompt of the
**final** execution chat.

It is deliberately **open-ended**, not a form. Enumerated sections cap the
answer at the sections someone thought of in advance — and on INDIS the paper's
best content came from things nobody planned: a survivorship-bias bug became a
methodological note, an unstable configuration became a statement of honest
reporting, a reversed communication-cost calculation became an entire
crossover analysis.

So the debrief asks for an exhaustive account, then explicitly asks for
**anything else from this phase that doesn't fit the above but shouldn't be
lost.**

## Discipline while running

- `DECISIONS.md` gets an entry for every non-obvious choice, tagged
  `[execution]`
- Superseded scripts go to `archive/` with a line in `archive/README.md`
  saying what each superseded and why — **archive, don't delete**; how a result
  came to be is part of the result
- Every figure writes its `figdata` JSON automatically (P06 set this up)

## Mid-phase splits

Same LLM project, same inputs, numbered. Only a short continuation note
advances between sub-chats: "stages 01–03 done, numbers are X, next is 04, open
question is Y." The full three-part closing prompt runs once, at the end.
