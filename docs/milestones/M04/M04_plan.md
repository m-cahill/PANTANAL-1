# M04 Plan — Kaggle Commit-Mode Submission Path Probe

**Status:** Stub only. Awaiting owner-approved plan.

---

## Purpose

Probe whether a Kaggle commit/submit-mode notebook can produce `/kaggle/working/submission.csv` using the M03 zero-baseline sample schema path, and record evidence without overclaiming eligibility, score, or model quality.

---

## Context

BirdCLEF+ 2026 final deadline has passed. M04 must not assume active competition eligibility, scoring, or submission availability unless directly evidenced.

---

## Expected focus

- Use the Kaggle Submission Bible rules for mode, paths, output naming, dependency policy, and evidence capture.
- Attempt or document Kaggle commit-mode behavior if available.
- Preserve data/weights/secrets guardrails.
- Do not commit competition data, model weights, real `sample_submission.csv`, real `taxonomy.csv`, real `submission.csv`, or generated runs.
- Do not claim leaderboard submission, score, CPU scoring compliance, active eligibility, or model inference without direct evidence.
- **DEF-002B** can only be narrowed or closed if commit/submit-mode evidence shows `/kaggle/working/submission.csv`.
- **DEF-003B** can only be narrowed or closed if scored/hidden test schema behavior is directly evidenced.

---

## Out of scope (until plan is locked)

- Implementation
- Model training or weights in git
- Leaderboard or score claims without evidence
