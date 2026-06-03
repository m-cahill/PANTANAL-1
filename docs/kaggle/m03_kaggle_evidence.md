# M03 Kaggle Evidence — Baseline Notebook

**Status:** Executed (Interactive mode). See observed values below.

**Authority:** Subordinate to `docs/pantanal-1.md`. Interactive mode does **not** imply scored commit/submit-mode submission.

Related: `notebooks/pantanal_1_m03_baseline.ipynb`, `docs/kaggle/baseline_inference_notebook.md`, `docs/kaggle/kaggle_submission_bible.md`.

---

## Notebook

- Source notebook in repo: `notebooks/pantanal_1_m03_baseline.ipynb`
- Kaggle notebook URL: not recorded / interactive session only
- Kaggle notebook version / commit: not recorded / interactive session only
- Date/time run: not recorded / interactive session only
- Runner: owner manual run

---

## Mode

- Interactive: **yes**
- Commit: **no** (not evidenced)
- Submit: **no** (not evidenced)
- Notes: `KAGGLE_KERNEL_RUN_TYPE` was Interactive. This does not prove scored commit/submit-mode execution (**DEF-002B** remains open).

---

## Runtime settings

- Accelerator: not recorded
- Internet: not recorded
- Observed `KAGGLE_KERNEL_RUN_TYPE`: Interactive
- Python version: 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0]
- Platform: Linux-6.6.122+-x86_64-with-glibc2.35
- cwd: `/kaggle/working`

---

## Input discovery

- `/kaggle/input` exists: **yes**
- `/kaggle/input` children: `competitions`
- `/kaggle` children: `lib`, `input`, `working`
- `sample_submission.csv` discovered: **yes**
- Exact sample path: `/kaggle/input/competitions/birdclef-2026/sample_submission.csv`
- Discovery method: explicit candidate (first of 2 candidates; second path `/kaggle/input/birdclef-2026/sample_submission.csv` did not exist)

**Candidates observed:**

| Candidate | Exists |
|-----------|--------|
| `/kaggle/input/competitions/birdclef-2026/sample_submission.csv` | yes |
| `/kaggle/input/birdclef-2026/sample_submission.csv` | no |

---

## Import behavior

- `pantanal_1` package import: **failed** (`ModuleNotFoundError: No module named 'pantanal_1'`)
- Inline fallback: **used** (`SOURCE = inline fallback`)

---

## Output evidence

- Mode selected by notebook: **`REAL_SAMPLE_ZERO_BASELINE`** (not `SYNTHETIC_FALLBACK_ONLY`)
- `/kaggle/working/submission.csv` produced: **yes**
- Synthetic fallback output produced: **no**
- Output path: `/kaggle/working/submission.csv`
- Row count: **3**
- Column count: **235** (`row_id` + 234 class columns)
- Class column count: **234**
- Header preview: `row_id`, `1161364`, `116570`, `1176823`, `1491113`, `1595929`, `209233`, `22930`, …
- First `row_id`: `BC2026_Test_0001_S05_20250227_010002_5`
- Last `row_id`: `BC2026_Test_0001_S05_20250227_010002_15`
- File size bytes: **4778**
- CSV preview (observed):
  - Line 0: `row_id,1161364,116570,1176823,1491113,1595929,209233,22930,...`
  - Line 1: `BC2026_Test_0001_S05_20250227_010002_5,0.0,0.0,0.0,...`
  - Line 2: `BC2026_Test_0001_S05_20250227_010002_10,0.0,0.0,0.0,...`

---

## Runtime / errors

- Runtime seconds (notebook path): **301.131**
- Errors: `ModuleNotFoundError` for `pantanal_1` (handled by inline fallback)
- Warnings: none recorded

**Note:** Interactive runtime does not prove CPU 90-minute **scoring** compliance.

---

## Submission / scoring

- Submitted to competition: **no** (not attempted / not evidenced)
- Submission ID: n/a
- Public leaderboard score: n/a
- Private leaderboard score: n/a
- Scoring still available: not recorded
- Notes: Notebook printed claim summary; no submission or score observed.

---

## Deferred issue assessment (from this run)

| ID | Assessment |
|----|------------|
| **DEF-002B** | **Open** — `/kaggle/working/submission.csv` produced in **Interactive** mode only; commit/submit-mode not evidenced. |
| **DEF-003A** | **Evidenced (M03 interactive)** — real `sample_submission.csv` discovered; zero baseline preserved sample header/row order (3 rows, 235 columns). |
| **DEF-003B** | **Open** — scored/hidden test submission behavior not evidenced in this run. |

---

## Claim recommendation

**Allowed after this evidence:**

- M03 Kaggle **interactive** evidence: baseline notebook discovered real `sample_submission.csv`, selected `REAL_SAMPLE_ZERO_BASELINE`, and produced `/kaggle/working/submission.csv` with observed row/column counts using sample schema (inline fallback).

**Do not claim:**

- Active competition submission eligibility
- Successful scored submission or commit/submit-mode execution
- Leaderboard score (public or private)
- CPU 90-minute scoring runtime compliance (interactive runtime ≠ scoring proof)
- Model inference or meaningful model quality
- Hidden/full test row count (sample had 3 rows only)
