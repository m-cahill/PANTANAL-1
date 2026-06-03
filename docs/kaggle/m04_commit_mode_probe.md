# M04 Commit-Mode Probe — Kaggle Submission Path

**Authority:** Subordinate to `docs/pantanal-1.md`.

Related: `docs/kaggle/m04_commit_mode_evidence.md`, `docs/kaggle/m03_kaggle_evidence.md`, `docs/kaggle/baseline_inference_notebook.md`, `docs/kaggle/kaggle_submission_bible.md`, `notebooks/pantanal_1_m03_baseline.ipynb`.

---

## Status

M04 is a commit/submit-mode **evidence probe**. It does not assume active competition eligibility. BirdCLEF+ 2026 final deadline has passed.

---

## Purpose

Determine whether the M03 baseline notebook can run in Kaggle **commit** or **submit** mode (not interactive-only) and produce `/kaggle/working/submission.csv`.

This probe addresses:

- **DEF-002B** — Kaggle scored/commit-mode real submission path
- **DEF-003B** — Scored/hidden test submission schema behavior

---

## Preconditions

- Owner has Kaggle account access.
- BirdCLEF+ 2026 data can be attached or is visible on Kaggle (if still mountable).
- Notebook derived from `notebooks/pantanal_1_m03_baseline.ipynb`.
- Accelerator: **CPU**.
- Internet: **disabled** (scoring-compatible configuration).
- No repo secrets or Kaggle credentials committed to git.
- Notebook outputs cleared in git before copy/commit on Kaggle.

---

## Manual steps

1. Open the Kaggle notebook derived from `notebooks/pantanal_1_m03_baseline.ipynb`.
2. Confirm accelerator is **CPU**.
3. Confirm internet is **disabled**.
4. Confirm BirdCLEF+ 2026 competition data is attached (if still available).
5. Confirm notebook is **output-cleared** before Kaggle commit.
6. **Commit** the notebook in Kaggle (commit/submit mode — not interactive-only debugging).
7. Record commit-mode logs (`KAGGLE_KERNEL_RUN_TYPE`, paths, errors).
8. Check whether `/kaggle/working/submission.csv` exists in **commit** output artifacts/logs.
9. If Kaggle permits submission, record whether a submit action was possible; otherwise record the blocker.
10. Record any score **only if actually observed**.

---

## Evidence required

Record all observed values in `docs/kaggle/m04_commit_mode_evidence.md`:

- Notebook URL / version / commit
- Mode: Interactive vs **Commit** vs **Submit**
- Accelerator
- Internet setting
- Runtime
- `/kaggle/input` children
- `sample_submission.csv` path (if discovered)
- Output path (must be `/kaggle/working/submission.csv` for DEF-002B narrowing)
- Row count, column count, file size
- Whether submission was attempted
- Score (only if observed)
- Errors / warnings

---

## Evidence status vocabulary

Use one of these values per field where applicable:

```text
yes
no
blocked — deadline passed
N/A — not attempted
```

Examples when the deadline blocks platform actions:

```text
Submit button available: blocked — deadline passed
Submitted: no
Scoring still available: blocked — deadline passed
```

Use **N/A — not attempted** only when the step was not tried. If a different blocker is observed, record the exact blocker instead of assuming deadline.

---

## Claim rules

- **Interactive evidence is not enough** for DEF-002B (see M03 interactive run).
- `/kaggle/working/submission.csv` must be observed in **commit/submit mode** to narrow or close DEF-002B.
- Hidden/scored schema behavior must be observed in commit/submit context to narrow or close DEF-003B.
- Do not update `docs/pantanal-1.md` success claims unless evidence above directly supports the change.
- Do not claim leaderboard score, active eligibility, CPU 90-minute **scoring** compliance, or model inference without direct evidence.

---

## Notebook suitability (M03 baseline)

The M03 notebook already:

- Prints `KAGGLE_KERNEL_RUN_TYPE` and Kaggle path diagnostics.
- Discovers `sample_submission.csv` under `/kaggle/input`.
- Writes `/kaggle/working/submission.csv` in `REAL_SAMPLE_ZERO_BASELINE` mode.
- Documents non-claims for commit/submit and scoring.

No notebook code change is required for M04 unless a defect is found during the manual run.

---

## If Kaggle blocks the probe

If commit/submit/scoring is unavailable because the competition deadline passed:

1. Record **blocked — deadline passed** in the evidence template.
2. Preserve DEF-002B and DEF-003B as **open** unless evidence meets exit criteria.
3. Do not infer commit-mode success from M03 interactive evidence.
