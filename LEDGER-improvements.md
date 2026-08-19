# Improvements Ledger

Distilled once per paper by the retro chat (P13) from that paper's
`docs/handoffs/*-meta.md`. Not filed continuously — capture is passive.

## Entries

| Date | Paper | What happened | Do instead |
|---|---|---|---|
| 2026-08 | INDIS 2026 | One chat held the entire project — 600k tokens, rate-limited to one prompt per five hours, and it became the only record of how anything was decided | One chat per phase. Files are the memory; chats are disposable |
| 2026-08 | INDIS 2026 | Anonymization was decided at write-up, so the codebase named an entity the paper anonymized. Fixing it meant a global find-replace under deadline | Decide anonymization at the feasibility gate. Codenames in tracked source from the first commit |
| 2026-08 | INDIS 2026 | Nothing was under version control while the work happened; six months of provenance had to be reconstructed by hand afterward | `git init` on day one. Commit with the *why* in the message |
| 2026-08 | INDIS 2026 | Defensive ablations added the week before the deadline became the paper's actual contribution | Run reviewer-anticipation work when the primary result exists, not at the deadline |
| 2026-08 | INDIS 2026 | A GLOBECOM workshop CFP appeared the day before its deadline and looked briefly tempting despite being all-wireless | A deadline appearing is not evidence that a venue fits. The **never** line in `VENUE.md` exists for this |

## Patterns
_(review yearly)_
