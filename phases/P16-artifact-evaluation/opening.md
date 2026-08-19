PHASE: Artifact evaluation

WHAT I'M DECIDING: what I can honestly claim reproduces, and how to write
instructions for a stranger.

REQUIRED CONTEXT: RELEASE.md, STAGE-PLAN.md, CLAIMS.md
ATTACHMENTS: the venue's artifact evaluation instructions; the public repo's
current README

WHAT I WANT OUT: an artifact README written for someone with zero context, and
the AE submission text.

---

HOW TO WORK THIS:

1. BADGE SCOPE. Given my data restrictions, which badges are realistically
   achievable? Be honest — an overclaimed badge that fails is much worse than
   a scoped one that succeeds.

2. WHAT REPRODUCES. Map claims to loader modes:
   - which claims reproduce with the real data only (i.e. not by an evaluator)
   - which reproduce with public_only
   - which don't reproduce numerically but whose pipeline runs with synthetic
   Give me a table an evaluator can read.

3. THE README. Write it for someone with no context and no memory of this
   project: prerequisites, install, exactly what to run in what order, expected
   outputs, runtime per stage, hardware assumed, and a clear statement of what
   cannot be reproduced and why.
   Assume they will not read anything else. Assume they will get stuck at the
   first ambiguity.

4. HONEST SCOPING. Write the paragraph that states plainly what's restricted
   and what substitution is possible. Do not soften it.

5. A test plan: what should I do to verify the README actually works from a
   clean clone?

COACHING: teach me inline where something comes up that I may be reading wrong.
