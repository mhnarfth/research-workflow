# P15 — Camera-Ready

Lighter manual — expand it the first time you run it for real.

## Steps

1. Address any changes the acceptance required
2. Restore names/affiliations if the venue was double-blind
3. **Mint the DOI.** Zenodo → log in with GitHub → Settings → GitHub → toggle
   the public repo ON. Then GitHub → Releases → new release, tag `v1.0.0` →
   Publish. Zenodo archives a snapshot and assigns a permanent DOI
4. **Swap the GitHub URL for the DOI** in the artifact appendix. A URL breaks
   if the repo is renamed or deleted; a DOI doesn't
5. Publisher format check (IEEE PDF eXpress or equivalent). **Leave a day** —
   these reject PDFs for font-embedding issues
6. Copyright form
7. `git tag <venue><year>-camera-ready`
8. Index row: status → Camera-ready, DOI filled

## Why the DOI is here and not at submission

At P12 the code wasn't final and reviewers could still force changes. Now it
is, so the DOI points at the version that matches the published paper.
