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

## Documented Kaggle behavior (not executed in initial M10 PR)

When a future Kaggle notebook or manual run uses this path:

| Condition | Output |
|-----------|--------|
| Real `sample_submission.csv` under `/kaggle/input` (see `kaggle_paths.py`) | `/kaggle/working/submission.csv` with uniform ε |
| No real sample file | Use synthetic fallback locally only (`tmp/submissions/`) |

The M03 baseline notebook is **unchanged** in M10; integrate a Kaggle notebook only in a later milestone if needed.

**No Kaggle run, commit/submit, or score claims** are made in the initial M10 PR unless owner provides separate evidence.

---

## Safety

No competition data, `sample_submission.csv`, generated `submission.csv`, or model weights are committed to this repository.

---

## Future Work

- Audio-based inference and public-model baselines
- Kaggle notebook wiring and scored evidence (owner-run)
- Working-note expansion (M10A, deferred)
- Archive/template cleanup (M10C, deferred)
