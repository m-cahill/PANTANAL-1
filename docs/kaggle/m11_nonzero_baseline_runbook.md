# M11 Non-Zero Baseline Kaggle Runbook

## Status

Runbook only unless evidence is recorded. Not model-quality proof.

## Purpose

Run the M10 uniform-ε baseline on Kaggle and record whether it produces a valid `/kaggle/working/submission.csv` and any observed score.

## Inputs

- M10 non-zero baseline logic (`src/pantanal_1/nonzero_baseline.py`)
- BirdCLEF+ 2026 competition data mounted in Kaggle
- real `sample_submission.csv`

## Required Settings

- CPU
- Internet disabled if scoring-compatible
- Competition data attached

## Manual Steps

1. Open or create a Kaggle notebook from `notebooks/pantanal_1_m11_nonzero_baseline.ipynb` (output-cleared in git).
2. Confirm accelerator is **CPU**.
3. Confirm internet is **disabled** when preparing for commit/submit scoring.
4. Confirm BirdCLEF+ 2026 competition data is attached.
5. **Interactive run first** — execute all cells for debugging and `sample_submission.csv` path confirmation. Record results in `docs/kaggle/m11_nonzero_baseline_evidence.md` under **Interactive** only. Do not infer scored behavior from interactive output.
6. Confirm `sample_submission.csv` path (notebook prints candidates and selected path).
7. Generate uniform-ε `/kaggle/working/submission.csv` when real sample is available (`EPSILON = 0.001`).
8. Confirm row count, column count, header preview, epsilon value, and file size in notebook logs.
9. **Commit run second** — commit the notebook on Kaggle (not interactive-only). Record commit-mode logs and artifacts under **Commit** in the evidence file.
10. **Submit/scoring third** — submit only if Kaggle allows and the owner chooses. Record public score only if Kaggle shows it under **Submit**.
11. Compare any observed public score to the prior all-zero baseline **0.500** only as a factual note; do not claim score improvement unless directly observed and recorded.

## Evidence Rules

- Record mode separately: **Interactive**, **Commit**, **Submit**.
- Record exact output path (`/kaggle/working/submission.csv` when real sample mode succeeds).
- Record runtime if available.
- Record public score only if Kaggle shows it.
- Do not infer score improvement.
- Do not claim model quality, trained inference, or audio understanding.

## Artifacts

| Path | Role |
|------|------|
| `notebooks/pantanal_1_m11_nonzero_baseline.ipynb` | Dedicated M11 notebook (M03 diagnostics + M10 uniform-ε) |
| `docs/kaggle/m11_nonzero_baseline_evidence.md` | Owner evidence template |
| `docs/kaggle/nonzero_baseline.md` | M10 method reference |

## Non-claims

- Uniform ε baseline only; no model quality proof.
- Interactive success does not prove commit/submit success.
- Score improvement requires direct observation; prior zero baseline was **0.500** (pipeline acceptance, not model quality).
