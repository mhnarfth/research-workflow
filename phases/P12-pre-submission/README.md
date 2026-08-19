# P12 — Pre-Submission

## Purpose

Resolve the attack list, build the public repo, and submit.

## Three checklists, in order

**1. Triage resolution.** Every attack from P11 has a disposition, recorded in
`DECISIONS.md`. The back-to-code gate:

| Attack | Action |
|---|---|
| **Invalidates a claim in `CLAIMS.md`** | **Back to code.** Non-negotiable |
| Weakens a claim | Soften the wording |
| Needs an experiment you don't have | Concede in Limitations |
| Framing or presentation | Fix in text |

Most of the time the answer is "fix in text." The gate exists so the call is
*deliberate* rather than made by deadline panic at 2am.

**2. Release.** Build the public repo — **fresh, never a flipped private repo**
(git history goes public with it and can't be reliably scrubbed). Run
`preflight.py`. Push. Tag. Put the URL in the paper.

**No DOI yet.** The code isn't final and reviewers may force changes. The DOI
gets minted at P15 camera-ready, when the code matches the published paper.

**3. Submission.** Page limit verified **after** the final edits — floats move
and a late change can cost you half a page. All form fields, LLM-usage
disclosure if the venue asks, funding acknowledgments pulled from the index,
figures rendering in the PDF text layer, references complete.

## The buffer is real

**24-hour floor, no exceptions.** Portals break, PDFs fail publisher format
checks, uploads time out. This is the one hard floor in the whole schedule.

## Advisor

His comments and the adversarial findings get worked in parallel — that's why
the draft went out at the end of P10 rather than after P11.
