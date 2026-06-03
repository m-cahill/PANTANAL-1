# M10 Non-Zero Baseline

**Authority:** Subordinate to `docs/pantanal-1.md`.

Related: `docs/kaggle/baseline_inference_notebook.md`, `docs/kaggle/kaggle_submission_bible.md`.

---

## What M10 Proves

PANTANAL-1 can generate deterministic non-zero probability submissions while preserving sample schema (header order, row order, and `row_id` values).

---

## What M10 Does Not Prove

- Model inference quality
- Audio understanding
- Competitive score
- Leaderboard improvement
- Trained model behavior
- RediAI certification

Public score **0.500** on the prior all-zero baseline evidences **pipeline acceptance only**, not predictive model quality.

---

## Method

**Uniform epsilon baseline:** every non-`row_id` column is set to the same small probability ε (default `0.001`), written as float strings (e.g. `"0.001"`). Stdlib only; no training or model weights.

| Artifact | Role |
|----------|------|
| `src/pantanal_1/nonzero_baseline.py` | Builders, ε validation, safe CSV write |
| `scripts/run_m10_nonzero_baseline_local.py` | Local mirror (`--epsilon`, optional `--sample-submission`) |

Reuses `sample_baseline.py`, `submission_contract.py`, `synthetic_schema.py`, and `kaggle_paths.py` for schema and path safety.

---

## Why This Matters

This is the smallest step beyond the all-zero baseline and establishes a reproducible non-zero submission path for future real inference work.

---

## Local behavior

Synthetic default (M01 schema: 234 class columns, synthetic soundscape stems, 5-second rows):

```bash
python scripts/run_m10_nonzero_baseline_local.py
```

Output: `tmp/submissions/m10_nonzero_baseline.csv`

Optional real sample (file must stay **outside git**):

```bash
python scripts/run_m10_nonzero_baseline_local.py --sample-submission /path/to/sample_submission.csv
```

Output: `tmp/submissions/m10_sample_nonzero_baseline.csv`

Custom ε (`0 < epsilon <= 1`):

```bash
python scripts/run_m10_nonzero_baseline_local.py --epsilon 0.002
```

Never write repository-root `submission.csv`.

---

## M11 Kaggle evidence path (repo-side; owner-run)

M11 adds a dedicated Kaggle notebook and evidence/runbook artifacts. Evidence is recorded in `docs/kaggle/m11_nonzero_baseline_evidence.md`.

| Artifact | Role |
|----------|------|
| `notebooks/pantanal_1_m11_nonzero_baseline.ipynb` | M03-style diagnostics + M10 uniform-ε + inline fallback |
| `docs/kaggle/m11_nonzero_baseline_runbook.md` | Interactive → commit → optional submit steps |
| `docs/kaggle/m11_nonzero_baseline_evidence.md` | Owner evidence template (starts not yet executed) |

When an owner runs the M11 notebook on Kaggle:

| Condition | Output |
|-----------|--------|
| Real `sample_submission.csv` under `/kaggle/input` (see `kaggle_paths.py`) | `/kaggle/working/submission.csv` with uniform ε (`0.001` default) |
| No real sample file | Synthetic fallback under `tmp/submissions/m11_synthetic_nonzero_baseline.csv` |

The M03 baseline notebook remains **unchanged**. Compare any new public score to the prior all-zero baseline **0.500** only as a factual note; do not claim score improvement without direct observation.

**M11 interactive evidence (2026-06-03):** Owner interactive run selected `REAL_SAMPLE_NONZERO_BASELINE` with ε **0.001** and wrote `/kaggle/working/submission.csv` (3 rows, 235 columns). See `docs/kaggle/m11_nonzero_baseline_evidence.md`.

**M11 scored evidence:** the uniform-ε baseline was submitted/scored on Kaggle (notebook Version 2, status Succeeded) and received public score **0.500**, matching the prior all-zero baseline. This supports pipeline acceptance for the non-zero path, not model quality or score improvement.

---

## Scoring and working-note planning (not a milestone plan)

Uniform epsilon may not improve ROC-AUC-style scoring because it does not create meaningful ranking separation. Score improvement must be empirically observed, not inferred.

M12 completed that planning evaluation in-repo: see `docs/analysis/M12_scoring_methodology_audit.md` and `docs/working_note/M12_working_note_criteria_audit.md`. The working-note prize may still reward reproducibility, clarity, and scientific communication independently of leaderboard position.

---

## Safety

No competition data, `sample_submission.csv`, generated `submission.csv`, or model weights are committed to this repository.

---

## Future Work

- Audio-based inference and public-model baselines
- Kaggle notebook wiring and scored evidence (owner-run)
- Working-note expansion (M10A, deferred)
- Archive/template cleanup (M10C, deferred)
