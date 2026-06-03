# M02 Plan — Kaggle Notebook Smoke

**Status:** In progress

---

## Objective

Create the first minimal Kaggle notebook smoke path for PANTANAL-1: a checked-in, output-cleared notebook and dependency-free mirror script that import the M01 submission contract, use synthetic fixtures only, and document Kaggle vs local paths—without claiming Kaggle execution, inference, or leaderboard score.

---

## Definition of done

- [x] `src/pantanal_1/synthetic_schema.py` with `SYNTHETIC_CLASS_LABELS` and `SYNTHETIC_SOUNDSCAPE_STEMS`
- [x] `tests/fixtures/synthetic_submission_schema.py` re-exports from package
- [x] `notebooks/pantanal_1_m02_smoke.ipynb` (cleared outputs, safety markdown)
- [x] `scripts/run_m02_notebook_smoke.py` writes `tmp/submissions/m02_smoke_submission.csv`
- [x] `docs/kaggle/notebook_smoke.md` documents claims and non-claims
- [x] `tests/test_notebook_smoke.py` and `tests/test_synthetic_schema.py`
- [x] `docs/pantanal-1.md` updated (M02 in progress; closed at closeout)
- [x] Local verification green
- [ ] PR CI green; no merge without owner approval

---

## In scope

1. Package-level synthetic schema refactor (M01 audit FIX-001)
2. Notebook smoke artifact + static JSON tests
3. Mirror smoke script (stdlib + existing package only)
4. Documentation: local vs Kaggle, archival intent, deadline passed
5. Preserve M00/M01 guardrails and `verify_repo_state.py`

---

## Out of scope

- Real Kaggle notebook commit/submit proof
- Real `sample_submission.csv` / taxonomy alignment
- Competition audio, model inference, runtime budget proof
- Leaderboard submission or score
- Jupyter, nbconvert, papermill, Kaggle API, pandas, torch, librosa
- M03 implementation

---

## Allowed claim (after success)

PANTANAL-1 contains a checked-in, output-cleared Kaggle-oriented smoke notebook and dependency-free mirror smoke script that exercise the synthetic M01 submission contract surface without using competition data.

---

## Explicit non-claims

- M02 does not prove the notebook ran on Kaggle.
- M02 does not prove active competition submission eligibility.
- M02 does not prove real `sample_submission.csv` compatibility.
- M02 does not prove CPU 90-minute runtime compliance.
- M02 does not prove inference.
- M02 does not prove leaderboard submission or score.

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

## Branch

`m02-kaggle-notebook-smoke`
