# M11 Non-Zero Baseline Evidence

**Status:** Executed (Interactive mode). Commit/submit and public score not yet evidenced.

**Authority:** Subordinate to `docs/pantanal-1.md`. Interactive mode does **not** imply scored commit/submit-mode submission.

Related: `notebooks/pantanal_1_m11_nonzero_baseline.ipynb`, `docs/kaggle/m11_nonzero_baseline_runbook.md`, `docs/kaggle/nonzero_baseline.md`.

---

## Notebook / Run

- Source notebook in repo: `notebooks/pantanal_1_m11_nonzero_baseline.ipynb`
- Kaggle notebook URL: not recorded / interactive session only
- Kaggle notebook version / commit: not recorded / interactive session only
- Date/time run: not recorded / interactive session only
- Runner: owner manual run

---

## Mode — Interactive

- Interactive attempted: **yes**
- Interactive successful: **yes**
- Notes: `KAGGLE_KERNEL_RUN_TYPE` was **Interactive**. Package import failed; inline fallback used. Do not infer commit/submit or scored behavior from this section.

---

## Mode — Commit

- Commit attempted: **no** (not evidenced)
- Commit successful: **no** (not evidenced)
- Version / commit: not recorded
- Runtime: not recorded
- `KAGGLE_KERNEL_RUN_TYPE`: not recorded for commit mode
- Notes: Commit-mode evidence pending owner run per runbook.

---

## Mode — Submit

- Submit attempted: **no** (not evidenced)
- Submit successful: **no** (not evidenced)
- Public score: **not observed**
- Notes: Submit/scoring not attempted in this run.

---

## Runtime Settings

- Accelerator: not recorded
- Internet: not recorded
- Runtime (notebook path): **123.981** seconds
- `KAGGLE_KERNEL_RUN_TYPE`: **Interactive**
- Python version: 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0]
- Platform: Linux-6.6.122+-x86_64-with-glibc2.35
- cwd: `/kaggle/working`
- `KAGGLE_URL_BASE`: https://www.kaggle.com

---

## Input Discovery

- sample_submission.csv discovered: **yes**
- exact path: `/kaggle/input/competitions/birdclef-2026/sample_submission.csv`
- row count (sample): **3**
- column count (sample header): **235** (`row_id` + 234 class columns)
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

## Baseline Configuration

- Method: uniform epsilon
- Epsilon: **0.001**
- Baseline mode: **REAL_SAMPLE_NONZERO_BASELINE**
- Class values non-zero: **yes** (uniform `0.001` on all 234 class columns)
- Deterministic: **yes**

---

## Output Evidence

- /kaggle/working/submission.csv produced: **yes**
- row count: **3**
- column count: **235**
- class column count: **234**
- header preview: `row_id`, `1161364`, `116570`, `1176823`, `1491113`, `1595929`, `209233`, `22930`, …
- first row_id: `BC2026_Test_0001_S05_20250227_010002_5`
- last row_id: `BC2026_Test_0001_S05_20250227_010002_15`
- file size bytes: **6182**
- non-zero check (first class col): `0.001` (not zero)

---

## Submission / Scoring

- Submitted: **no** (not attempted / not evidenced)
- Public score: **not observed**
- Score compared to zero baseline 0.500: **N/A** (no score observed)
- Score improvement claimed: **no**
- Errors/warnings: package import failed; inline fallback succeeded

---

## Claim Recommendation

Do not update model-quality claims. Uniform epsilon baseline only. Interactive mode only — no submit/score evidence yet. Do not claim score improvement unless Kaggle shows a different score in a future commit/submit run.
