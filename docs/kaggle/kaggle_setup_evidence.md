# Kaggle Setup Evidence — PANTANAL-1

**Status:** Interactive synthetic smoke evidenced (M02). Scored/commit-mode real submission path not evidenced.

---

## Kaggle notebook

- URL: not recorded / interactive session only
- Version / commit: not recorded / interactive session only
- Created by: manual copy from `notebooks/pantanal_1_m02_smoke.ipynb` (patched fallback version)
- Date/time: not recorded / interactive session only

---

## Runtime settings

- Accelerator: not recorded (interactive session; CPU expected for scored runs)
- Internet: not recorded
- Competition data attached: yes (`/kaggle/input` children included `competitions`)
- Observed input path: `/kaggle/input` (children: `competitions`)

---

## Kaggle environment (observed)

| Field | Value |
|-------|--------|
| Python | 3.12.13 |
| Platform | Linux-6.6.122+-x86_64-with-glibc2.35 |
| cwd | `/kaggle/working` |
| `KAGGLE_KERNEL_RUN_TYPE` | Interactive |
| `KAGGLE_URL_BASE` | https://www.kaggle.com |
| `/kaggle` exists | yes |
| `/kaggle/input` exists | yes |
| `/kaggle/input` children | `competitions` |
| `/kaggle/working` exists | yes |

**Mode:** Interactive (debugging). Does **not** imply scored submission or commit/submit-mode compliance.

---

## Import behavior

- `pantanal_1` package import failed with `ModuleNotFoundError`.
- Inline fallback was used successfully (`SOURCE = inline fallback`).

---

## Synthetic smoke result (observed)

| Field | Value |
|-------|--------|
| Class label count | 234 |
| First labels | `synthetic_class_000` … `synthetic_class_004` |
| Last labels | `synthetic_class_229` … `synthetic_class_233` |
| Soundscape stems | `BC2026_Test_0001_S05_20250227_010002`, `BC2026_Test_0002_S05_20250227_010003` |
| Row count | 24 |
| Expected rows | 24 |
| First `row_id` | `BC2026_Test_0001_S05_20250227_010002_5` |
| Last `row_id` | `BC2026_Test_0002_S05_20250227_010003_60` |
| First row column count | 235 (`row_id` + 234 classes) |
| Output path | `tmp/submissions/m02_smoke_submission.csv` |
| Output exists | yes |
| Size bytes | 28134 |
| CSV header | begins with `row_id` plus synthetic class columns |

---

## Execution evidence (patched notebook — interactive)

- Notebook ran on Kaggle: **yes** (interactive mode)
- Used inline fallback: **yes**
- Produced `/kaggle/working/submission.csv`: **no** (M02 smoke only; not attempted)
- Produced `tmp/submissions/m02_smoke_submission.csv`: **yes**
- Runtime: not recorded
- Errors/warnings: `ModuleNotFoundError` for `pantanal_1` (handled by fallback)

---

## First manual attempt (pre-import-fallback patch)

**Observed error:** `ModuleNotFoundError: No module named 'pantanal_1'` on direct package import.

**Resolution:** Patched notebook with diagnostics and inline fallback (commit `9e57484` on `m02-kaggle-notebook-smoke`).

---

## Submission evidence

- Submitted to competition: **no**
- Submission ID: n/a
- Public leaderboard score: n/a
- Private leaderboard score: n/a
- Notes: Interactive smoke only; no commit/submit-mode run recorded.

---

## Claim update recommendation

**Allowed after this evidence:**

M02 has evidence that the patched smoke notebook ran in Kaggle interactive mode using inline fallback and produced a synthetic smoke CSV under `tmp/submissions/m02_smoke_submission.csv`.

**Do not claim:**

- Active competition submission eligibility
- Real `/kaggle/working/submission.csv` generation
- Real `sample_submission.csv` compatibility
- CPU 90-minute scoring compliance
- Model inference
- Leaderboard submission or score

**Deferred issues:**

- **DEF-002A** — evidenced in M02 (interactive synthetic smoke)
- **DEF-002B** — open (scored/commit-mode `/kaggle/working/submission.csv`)
