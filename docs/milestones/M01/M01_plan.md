# M01 Plan — submission.csv Skeleton + sample_submission Contract

**Status:** Stub only. Awaiting owner-approved plan.

## Purpose

Create a synthetic or zero-baseline submission generator and validation surface for BirdCLEF+ 2026 `submission.csv` structure without committing Kaggle data.

## Expected focus

- Generate a valid-shaped synthetic submission.csv fixture outside prohibited committed output paths, or a test-only temporary artifact.
- Validate `row_id` semantics.
- Validate 234 species/class probability columns when `sample_submission.csv` or a synthetic schema fixture is available.
- Keep competition data, real submissions, and model weights out of git.
- Preserve M00 safety verifier.

## Out of scope (until plan is locked)

- Kaggle notebook execution
- Model inference
- Leaderboard submission
