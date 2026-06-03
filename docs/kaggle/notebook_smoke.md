# M02 — Kaggle Notebook Smoke

**Authority:** Subordinate to `docs/pantanal-1.md`.

---

## What M02 proves

PANTANAL-1 contains a checked-in, output-cleared Kaggle-oriented smoke notebook and dependency-free mirror smoke script that exercise the synthetic M01 submission contract surface without using competition data.

Artifacts:

| Path | Role |
|------|------|
| `notebooks/pantanal_1_m02_smoke.ipynb` | Minimal smoke notebook (outputs cleared) |
| `scripts/run_m02_notebook_smoke.py` | Pure-Python mirror of notebook logic |
| `src/pantanal_1/synthetic_schema.py` | Package-level synthetic labels and soundscape stems |
| `docs/kaggle/kaggle_setup_runbook.md` | Manual Kaggle setup checklist (not execution proof) |
| `docs/kaggle/kaggle_setup_evidence.md` | Evidence template for future live Kaggle runs |

---

## Kaggle setup (manual)

To set up the notebook on Kaggle from scratch, follow `docs/kaggle/kaggle_setup_runbook.md`. Record observed results in `docs/kaggle/kaggle_setup_evidence.md`.

The first manual copy attempt failed with `ModuleNotFoundError: No module named 'pantanal_1'` because a blank Kaggle notebook does not install this repository. The patched `notebooks/pantanal_1_m02_smoke.ipynb` adds verbose environment diagnostics and an inline synthetic fallback when the package is unavailable.

---

## Troubleshooting: `ModuleNotFoundError: pantanal_1`

**Symptom:** `from pantanal_1.submission_contract import ...` raises `ModuleNotFoundError` on Kaggle.

**Cause:** The notebook was copied without installing the PANTANAL-1 package (`src/pantanal_1/` is not on `sys.path` by default).

**M02 fix:** Re-copy or sync `notebooks/pantanal_1_m02_smoke.ipynb` from this repo. The notebook:

1. Prints Kaggle path diagnostics (`/kaggle/input`, `/kaggle/working`, `KAGGLE_KERNEL_RUN_TYPE`, etc.).
2. Tries package import first; on failure, uses an inline fallback with the same synthetic stems and 234 labels as `pantanal_1.synthetic_schema`.
3. Writes only to `tmp/submissions/m02_smoke_submission.csv` (not `/kaggle/working/submission.csv`).

For a real Kaggle submission notebook, the final output path must be `/kaggle/working/submission.csv`. M02 intentionally does not enable that path in the inline fallback because M02 is synthetic smoke only. A future milestone must add real Kaggle sample/schema alignment before enabling real submission output.

---

## What M02 does not prove

- M02 does **not** prove the notebook ran on Kaggle.
- M02 does **not** prove active competition submission eligibility (BirdCLEF+ 2026 final deadline has passed).
- M02 does **not** prove real `sample_submission.csv` compatibility.
- M02 does **not** prove CPU 90-minute runtime compliance.
- M02 does **not** prove inference.
- M02 does **not** prove leaderboard submission or score.

Real Kaggle execution remains **DEF-002** until directly evidenced.

---

## Archival / governance intent

M02 preserves a Kaggle-oriented smoke path for **reproducibility**, **retrospective documentation**, and possible future BirdCLEF/Kaggle reuse. It is not an active competition submission milestone.

---

## Local smoke behavior

1. Install the package in editable or `src`-layout mode (same as CI: `src` on `PYTHONPATH` via tests/scripts).
2. Optionally run the mirror script:

   ```bash
   python scripts/run_m02_notebook_smoke.py
   ```

3. Output is written only to:

   ```text
   tmp/submissions/m02_smoke_submission.csv
   ```

4. `tmp/` is gitignored; `scripts/verify_repo_state.py` must pass with no generated artifacts committed.
5. Do **not** write `submission.csv` at the repository root.

Static tests in `tests/test_notebook_smoke.py` validate notebook JSON structure, cleared outputs, safety language, and import paths without executing Jupyter.

---

## Kaggle expected paths

When adapted for a real Kaggle notebook run (future milestone, with evidence):

| Path | Purpose |
|------|---------|
| `/kaggle/input/...` | Mounted competition data (e.g. `birdclef-2026`) |
| `/kaggle/working/submission.csv` | Required final submission output name |

M02 local smoke intentionally uses `tmp/submissions/m02_smoke_submission.csv` instead of `/kaggle/working/submission.csv` to avoid committing or producing root-level submissions in the repo.

---

## Runtime constraints (competition binding)

- **CPU** notebook runtime must be **≤ 90 minutes** for scored submissions.
- **Internet access is disabled** during submission scoring.
- **GPU** notebook submissions are effectively disabled (~1 minute runtime).

M02 does not measure or prove compliance with these constraints.

---

## Synthetic data only

M02 uses `pantanal_1.synthetic_schema` (`synthetic_class_000` … `synthetic_class_233`, synthetic soundscape stems). It does **not** read real `taxonomy.csv`, `sample_submission.csv`, or competition audio.
