# M11 Non-Zero Baseline Evidence

**Status:** Executed (Interactive mode; Kaggle Version 2 commit/submit succeeded; public score observed).

**Authority:** Subordinate to `docs/pantanal-1.md`. Interactive and scored runs are documented separately; interactive output does not imply scored commit/submit behavior.

Related: `notebooks/pantanal_1_m11_nonzero_baseline.ipynb`, `docs/kaggle/m11_nonzero_baseline_runbook.md`, `docs/kaggle/nonzero_baseline.md`.

---

## Notebook / Run

- Source notebook in repo: `notebooks/pantanal_1_m11_nonzero_baseline.ipynb`
- Kaggle notebook URL: https://www.kaggle.com/code/michael1232/pantanal-1-m11-nonzero-baseline?scriptVersionId=324302733
- Kaggle notebook name: `pantanal_1_m11_nonzero_baseline`
- Kaggle notebook version / commit: **Version 2**
- Submission label (owner paste): `pantanal_1_m11_nonzero_baseline - Version 2`
- Date/time: not recorded
- Runner: owner manual run

---

## Mode — Interactive

- Interactive attempted: **yes**
- Interactive successful: **yes**
- Notes: `KAGGLE_KERNEL_RUN_TYPE` was **Interactive**. Package import failed; inline fallback used. See runtime/output fields below for interactive-run details. Do not infer scored commit/submit behavior from this section alone.

---

## Mode — Commit

- Commit attempted: **yes** (Version 2 submission on Kaggle)
- Commit successful: **yes** (submission status **Succeeded**)
- Version / commit: **Version 2**
- Runtime: not recorded
- `KAGGLE_KERNEL_RUN_TYPE`: not recorded
- Notes: Scored competition submission path evidenced by Version 2 success and public score **0.500**. Exact commit logs not pasted.

---

## Mode — Submit

- Submit attempted: **yes**
- Submit successful: **yes** (public leaderboard score observed)
- Public score: **0.500**
- Notes: Prior all-zero baseline notebook `pantanal_1_m03_baseline` Version 2 also scored **0.500**. No score improvement observed.

---

## Runtime Settings

### Interactive run

- Accelerator: not recorded
- Internet: not recorded
- Runtime (notebook path): **123.981** seconds
- `KAGGLE_KERNEL_RUN_TYPE`: **Interactive**
- Python version: 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0]
- Platform: Linux-6.6.122+-x86_64-with-glibc2.35
- cwd: `/kaggle/working`
- `KAGGLE_URL_BASE`: https://www.kaggle.com

### Commit/submit run (Version 2)

- Accelerator: not recorded
- Internet: not recorded
- Runtime: not recorded
- `KAGGLE_KERNEL_RUN_TYPE`: not recorded

---

## Input Discovery

*(From interactive run; commit/submit paste did not repeat discovery fields.)*

- sample_submission.csv discovered: **yes**
- exact path: `/kaggle/input/competitions/birdclef-2026/sample_submission.csv`
- row count (sample): **3**
- column count (sample header): **235** (`row_id` + 234 class columns)
- Discovery method: explicit candidate (first of 2 candidates; second path `/kaggle/input/birdclef-2026/sample_submission.csv` did not exist)

**Candidates observed (interactive):**

| Candidate | Exists |
|-----------|--------|
| `/kaggle/input/competitions/birdclef-2026/sample_submission.csv` | yes |
| `/kaggle/input/birdclef-2026/sample_submission.csv` | no |

---

## Import behavior

*(Interactive run.)*

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

*(Interactive run; commit/submit paste did not repeat file metrics.)*

- /kaggle/working/submission.csv produced: **yes** (interactive)
- row count: **3**
- column count: **235**
- class column count: **234**
- header preview: `row_id`, `1161364`, `116570`, `1176823`, `1491113`, `1595929`, `209233`, `22930`, …
- first row_id: `BC2026_Test_0001_S05_20250227_010002_5`
- last row_id: `BC2026_Test_0001_S05_20250227_010002_15`
- file size bytes: **6182** (interactive)
- non-zero check (first class col): `0.001` (not zero)

---

## Submission / Scoring

- Submitted: **yes** (Version 2; status **Succeeded**)
- Public score: **0.500**
- Prior all-zero baseline notebook: `pantanal_1_m03_baseline` Version 2
- Prior all-zero baseline public score: **0.500**
- Score compared to zero baseline 0.500: **equal** (M11 uniform-ε score equals prior all-zero baseline score)
- Score improvement claimed: **no**
- Errors/warnings: interactive — package import failed; inline fallback succeeded. Commit/submit — none recorded in owner paste.

---

## Owner non-claim text (notebook)

Uniform epsilon baseline only; does not prove model inference or competitive quality. Does not prove leaderboard submission, score, or score improvement unless Kaggle shows a score and it is recorded in evidence. Does not prove audio understanding or trained model inference. Does not prove CPU 90-minute scoring runtime unless commit/submit-mode evidence is recorded. Does not prove Kaggle commit/submit-mode execution unless explicitly run and documented. Synthetic fallback does not prove real `sample_submission.csv` compatibility. Record public score only if shown by Kaggle. Prior all-zero baseline public score was **0.500** (pipeline acceptance, not model quality).

---

## Claim Recommendation

Uniform epsilon baseline only. Version 2 commit/submit succeeded with public score **0.500**, matching the prior all-zero baseline — **no score improvement observed**. Do not claim model quality, audio understanding, trained inference, or competitive performance. Pipeline acceptance for the non-zero path is evidenced; predictive quality is not.
