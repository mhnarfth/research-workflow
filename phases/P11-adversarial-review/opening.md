PHASE: Adversarial review  —  framing: <methods reviewer | domain reviewer |
skeptical PC member | external-review triage>

>>> START A FRESH CHAT FOR THIS. Do not run it inside the paper's project.
>>> This chat must have NO context about how the paper was built.

REQUIRED CONTEXT: none — that is deliberate
ATTACHMENTS: the paper PDF <plus reviews/PATTERNS.md if I have one; plus the
external review if this is the triage chat>

WHAT I WANT OUT: a prioritized attack list I can triage.

---

You are reviewing this paper for <venue>, as a <framing>.

Your job is to find what is wrong with it. Do not summarize the paper back to
me, do not list its strengths, and do not soften. I am using this to find
problems before real reviewers do, so a comfortable review is a useless one.

For each problem:
- state it specifically, pointing at the section, claim, figure, or number
- say why it damages the paper
- say what the authors would have to do to answer it
- rate severity: FATAL (invalidates a claim) / SERIOUS (weakens a claim) /
  MINOR (presentation)

Go after these in particular:
- claims stronger than the evidence supports
- aggregates that might be driven by one unit
- correlations presented as mechanisms
- null results described as equivalence
- metrics that don't actually support the interpretation drawn from them
- missing controls or baselines a reviewer would expect at this venue
- anything the paper asserts without showing

<IF PATTERNS.md ATTACHED:>
Also check this draft against the attached record of objections reviewers have
raised on my previous papers. Is it vulnerable to any of the same ones?

<IF EXTERNAL REVIEW ATTACHED:>
Also triage the attached external review: which of its points are real, which
are boilerplate, and which it got wrong. Merge them into your own list rather
than treating them separately.

Rank everything by severity. Then state plainly: would you accept this paper?
If not, what is the single change that would most improve its chances?
