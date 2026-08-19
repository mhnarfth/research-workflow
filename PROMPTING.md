# Prompting

Not a vocabulary list. Four elements that reliably change what you get back.

---

## The four elements

**1. Name the output type.** The single biggest lever.

> "Produce a ranked list of cuts" ≠ "make this shorter"

A model has seen a million cut-lists and a million summaries. You're choosing
which pattern it reaches for. Name the artifact: a table, a ranked list, a
checklist, a diff, a critique.

**2. Name what must not happen.** Negative constraints are enforced well and
prevent the specific failure you're worried about.

> "Do not rewrite the paper."
> "Never propose cutting a limitation or a caveat."

**3. Name the failure mode you're avoiding.** This generalizes to cases you
didn't think to list.

> "Summarizing would delete the caveats — I need to keep prose I already
> approved."

**4. Give the format.** A table with named columns produces a table. A vague
request produces prose.

---

## What doesn't matter much

Length, politeness, magic words. Long rambling prompts work fine — they're rich
in intent. The gain isn't from shortening them; it's from adding the four
elements above when precision matters.

---

## The habit that teaches you this

When the output is wrong, **don't rephrase and retry.** Ask:

> "Why did you produce that instead of what I wanted?"

The answer usually names the missing constraint. Add it. That's how this gets
learned — from your own failures, not from a list.

---

## Patterns that have worked

Append as you find them.

| Situation | What worked | Why |
|---|---|---|
| Cutting a paper to fit | "Produce a ranked list of specific cuts. Do not rewrite the paper. Quote the exact text to remove." | "Make it shorter" triggers summarization, which deletes specifics and caveats first |
| Getting an honest critique | Fresh chat, zero project context, framed as a specific reviewer role | A chat that helped build something can't attack it honestly |
| Avoiding invented numbers | "Every number must trace to a file I've given you. If it isn't there, say so rather than filling it in." | Recall is fluent and wrong |
| Extracting the full picture at chat close | "Be exhaustive. Don't summarize away specifics — names, numbers, file names." + an explicit "anything else that doesn't fit above" section | Enumerated sections cap the answer at the sections you thought of |
