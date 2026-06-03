# Kaggle Setup Runbook — PANTANAL-1

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/kaggle/notebook_smoke.md`.

---

## Status

- Repo-side smoke scaffold exists (`notebooks/pantanal_1_m02_smoke.ipynb`, `scripts/run_m02_notebook_smoke.py`).
- **Live Kaggle execution is not yet proven.**
- **Active competition submission eligibility is not proven** and may no longer be available because the BirdCLEF+ 2026 final deadline has passed.

M02 currently proves only the repo-side smoke scaffold unless Kaggle-side evidence is later recorded in `docs/kaggle/kaggle_setup_evidence.md`.

---

## Preconditions

- User has a Kaggle account.
- User has accepted the BirdCLEF+ 2026 rules if the competition still allows access.
- User can create or edit Kaggle notebooks.
- User can attach competition data or access the competition input mount.
- **No Kaggle credentials are committed to this repo.**

---

## Manual Kaggle Setup Steps

1. Open the [BirdCLEF+ 2026](https://www.kaggle.com/competitions/birdclef-2026/) competition page.
2. Confirm competition access/rules status.
3. Create a new Kaggle notebook.
4. Set accelerator to **CPU**.
5. Disable **internet** for scoring-compatible configuration.
6. Attach the BirdCLEF+ 2026 competition dataset if available.
7. Copy or upload the M02 smoke notebook content from `notebooks/pantanal_1_m02_smoke.ipynb` (or adapt cells to import `pantanal_1` if the package is installed in the notebook environment).
8. Confirm imports work in the Kaggle environment (`pantanal_1.submission_contract`, `pantanal_1.synthetic_schema`).
9. Confirm expected competition input path, usually under `/kaggle/input/...`.
10. Confirm final output path for an actual submission must be `/kaggle/working/submission.csv`.
11. For **M02 smoke only**, run synthetic contract logic without competition data (synthetic labels only).
12. Save/commit the Kaggle notebook.
13. If commit output is available, capture run time and output file evidence.
14. Do **not** claim leaderboard submission unless the Kaggle submit action is actually performed and evidenced.

Record observed results in `docs/kaggle/kaggle_setup_evidence.md`.

---

## Evidence To Capture

- Kaggle notebook URL
- Notebook version / commit ID if available
- Whether internet was disabled
- Whether CPU was used
- Whether competition data was attached
- Whether `/kaggle/working/submission.csv` was produced
- Runtime
- Any Kaggle errors or warnings
- Screenshot or copied log summary if available
- Whether the notebook was submitted to the competition
- Leaderboard score **only if actually scored**

---

## Expected Evidence File

Future manual execution evidence should be recorded in:

`docs/kaggle/kaggle_setup_evidence.md`

Do not update `docs/pantanal-1.md` claims or resolve **DEF-002** until that file contains actual observed results.

---

## Non-Claims

- This runbook does not prove Kaggle execution.
- This runbook does not prove submission eligibility.
- This runbook does not prove real `sample_submission.csv` compatibility.
- This runbook does not prove CPU 90-minute runtime compliance.
- This runbook does not prove model inference.
- This runbook does not prove leaderboard submission or score.
