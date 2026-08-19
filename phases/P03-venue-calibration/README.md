# P03 — Venue Calibration

## Purpose

Pick the venue, learn how it writes, and compute the schedule.

## The rule

**Choose by the NATURE of the contribution, not the AMOUNT of material.**

A measurement study, a systems build, and a theory result belong at different
venues regardless of page count. More material never turns a simulation into a
systems paper — which is why NSDI and EuroSys were wrong for INDIS, and why a
GLOBECOM workshop deadline appearing didn't make an all-wireless venue fit.

Amount of material only decides **short vs. full paper within a venue class.**
That's the 5→8 page move on INDIS, and it was correct.

## The ladder

```
Target:   <venue, length, deadline>
Up:       <better venue> — only if <specific result lands>
Down:     <fallback> — deadline <date>
Never:    <venues that structurally don't fit> — because <reason>
```

**The Never line is as valuable as the target.** It stops you being talked into
a mismatched venue mid-project — by a person, a model, or a deadline.

## Calibration — read real papers

Fetch 2–3 recent papers from the target venue and actually read them. This
directly shaped INDIS's length, structure, and framing. Record: page limit and
what's excluded, prose style, what counts as a contribution here, typical
evidence bar, appendix rules, preprint policy, whether artifact evaluation
runs, this year's theme, relevant CFP topic numbers.

**Pick 2 style exemplars and name them in `VENUE.md`.** They get attached at
P10 drafting. A note describing the style isn't enough — the model needs the
exemplar in front of it to match register.

## The reverse schedule

Computed here from today's date and the deadline. Ratios, not fixed offsets:

| Block | Share | Ends at |
|---|---|---|
| Setup (P01–P05) | 20% | T−80% |
| Execution + red team | 40% | T−40% |
| Paper planning + drafting | 25% | T−15% |
| Adversarial + revision | 8% | T−7% |
| Advisor draft | — | computed; compresses on a short runway |
| Submission buffer | 5% | T−2%, **floor 24h** |

Only the buffer has a hard floor. Portals break, PDFs fail format checks, page
counts shift when a float moves.

## Advisor touchpoint

Optional, informational, nothing blocks on it. But this is the **cheapest
possible moment to be redirected** — idea and venue go together in one
conversation, before six weeks are spent.

## Outputs

`docs/VENUE.md` — ladder, style observations, 2 named exemplars, preprint
policy, AE applicability, computed schedule with real dates.
