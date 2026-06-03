# M03 Plan — Baseline Inference Notebook / First Scored Attempt If Eligible

**Status:** In progress  
**Branch:** `m03-baseline-inference-notebook`

---

## Objective

Create the first baseline inference-oriented Kaggle notebook path for PANTANAL-1, building on M01 synthetic contract and M02 Kaggle smoke, with honest evidence boundaries.

BirdCLEF+ 2026 final deadline has passed. M03 does not assume active scoring unless directly evidenced.

---

## Definition of done

### Repo-side (this milestone PR)

- [x] Full `M03_plan.md`
- [x] `notebooks/pantanal_1_m03_baseline.ipynb` (output-cleared, five phases)
- [x] `scripts/run_m03_baseline_local.py` (synthetic default; optional `--sample-submission`)
- [x] `src/pantanal_1/kaggle_paths.py` + `sample_baseline.py`
- [x] `docs/kaggle/baseline_inference_notebook.md`
- [x] Static tests (`test_m03_baseline_notebook.py`, `test_kaggle_paths.py`, `test_sample_baseline.py`)
- [x] `docs/pantanal-1.md` M03 status in progress + structural claim when implemented
- [x] PR-head CI green (run 26862042794, commit `0c8b2ed`)
- [x] `docs/kaggle/m03_kaggle_evidence.md` evidence template (awaiting owner fill-in)
- [ ] Owner manual Kaggle run + evidence recorded in template (follow-up; do not close DEF-002B/003 without criteria)
- [ ] M03 closeout deferred until owner decides on manual Kaggle run and evidence commit

### Out of scope

- Model training or inference quality
- Committing competition data, weights, real submissions
- Kaggle API, heavy ML deps, Jupyter in CI
- Leaderboard score claims without evidence

---

## Implementation shape

| Path | Purpose |
|------|---------|
| `notebooks/pantanal_1_m03_baseline.ipynb` | Kaggle baseline notebook |
| `scripts/run_m03_baseline_local.py` | Local mirror |
| `src/pantanal_1/kaggle_paths.py` | Path candidates + discovery |
| `src/pantanal_1/sample_baseline.py` | Real sample zero baseline |
| `docs/kaggle/baseline_inference_notebook.md` | M03 documentation |
| `docs/kaggle/m03_kaggle_evidence.md` | Manual Kaggle run evidence template (not executed until owner fills in) |
| `tests/test_m03_baseline_notebook.py` | Notebook/script safety tests |
| `tests/test_m03_kaggle_evidence.py` | Evidence template honesty tests |

---

## Notebook phases

1. Environment diagnostics (Kaggle Submission Bible debug standard)
2. Path discovery for `sample_submission.csv` (explicit + bounded rglob under `/kaggle/input`)
3. Mode selection: `REAL_SAMPLE_ZERO_BASELINE` vs `SYNTHETIC_FALLBACK_ONLY`
4. Validation and write
5. Claim warning (non-claims preserved)

---

## Output paths

| Mode | Path |
|------|------|
| Real sample on Kaggle | `/kaggle/working/submission.csv` |
| Synthetic fallback | `tmp/submissions/m03_synthetic_baseline.csv` |
| Local `--sample-submission` | `tmp/submissions/m03_sample_zero_baseline.csv` |

---

## Deferred issues

| ID | M03 action |
|----|------------|
| DEF-002B | Remains open until commit/submit-mode `/kaggle/working/submission.csv` evidence |
| DEF-003 | Remains open until real sample schema observed and recorded on Kaggle |

---

## Verification

```bash
ruff check .
ruff format --check .
python -m compileall src tests scripts
pytest -q
python scripts/verify_repo_state.py
```

---

## Stop point

Repo-side implementation and evidence-readiness pass complete after green PR-head CI.

**Next (owner):** Copy/run `notebooks/pantanal_1_m03_baseline.ipynb` on Kaggle; paste observed values into `docs/kaggle/m03_kaggle_evidence.md` for a follow-up evidence commit.

No merge, summary, audit, or closeout without express permission.
