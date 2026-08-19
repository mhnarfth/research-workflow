PHASE: Pre-submission

WHAT I'M DECIDING: what to do about each attack, and everything that has to be
true before I hit submit.

REQUIRED CONTEXT: CLAIMS.md, DECISIONS.md, VENUE.md, SECTION-PLAN.md
ATTACHMENTS: the attack lists from adversarial review; my advisor's comments;
the current draft

WHAT I WANT OUT: a triaged action list, a release plan, and a submission
checklist specific to this venue.

---

HOW TO WORK THIS:

1. TRIAGE. Merge every attack list and my advisor's comments into ONE ranked
   action list, deduplicated. For each item, categorize:
   - INVALIDATES A CLAIM in CLAIMS.md -> back to code
   - WEAKENS A CLAIM -> give me the replacement wording
   - NEEDS AN EXPERIMENT I DON'T HAVE -> give me the Limitations sentence
   - FRAMING/PRESENTATION -> say exactly what to change
   - DEFER to the extension

   Be conservative with the first category. "More evidence would be nice" is
   not the same as "the claim shown is not supported by the evidence shown."

2. TIME CHECK. Given the schedule in VENUE.md and today's date, tell me what is
   realistically achievable. If something can't fit, say so and show me the
   numbers. Do not decide what to cut — that's mine.

3. RELEASE PLAN. Which files ship in the public repo and which don't. Apply
   the invertibility test: does any file contain scaling parameters, raw
   values, or model weights trained on restricted data? If yes it doesn't ship.
   Give me the exact commands to build the public repo FRESH — never by
   flipping the private repo, since its history would go public too.

4. SUBMISSION CHECKLIST. Specific to this venue, from VENUE.md and the CFP:
   page limit and what's excluded, every form field, LLM-usage disclosure if
   asked, funding acknowledgments, artifact appendix if applicable, anything
   the CFP requires that I'd forget.

COACHING: As we work, teach me inline — briefly, where it comes up, not saved
for the end. If a metric, plot, statistic, or convention appears that I may be
reading wrong, say what it means and which direction is good. If I state
something incorrect, correct me directly rather than working around it. Keep it
to a line or two each time; don't turn the session into a lecture.
