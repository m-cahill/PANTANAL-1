# M03 — Baseline Inference Notebook

**Authority:** Subordinate to `docs/pantanal-1.md`.

Related: `docs/kaggle/kaggle_submission_bible.md`, `docs/kaggle/notebook_smoke.md`, `docs/kaggle/kaggle_setup_evidence.md`.

---

## What M03 proves (repo-side)

PANTANAL-1 contains a baseline-oriented Kaggle notebook scaffold that can either:

- Generate a **local synthetic fallback** CSV under `tmp/submissions/m03_synthetic_baseline.csv`, or
- When real Kaggle `sample_submission.csv` is available in the Kaggle environment, generate a **zero baseline** at `/kaggle/working/submission.csv` using that schema (all non-`row_id` columns set to `0.0`, header and row order preserved).

Artifacts:

| Path | Role |
|------|------|
| `notebooks/pantanal_1_m03_baseline.ipynb` | Baseline notebook (outputs cleared) |
| `scripts/run_m03_baseline_local.py` | Local mirror (synthetic default; optional `--sample-submission`) |
| `src/pantanal_1/kaggle_paths.py` | Kaggle path discovery |
| `src/pantanal_1/sample_baseline.py` | Real sample zero-baseline helpers |

---

## What M03 does not prove

- Model inference or competitive quality (zero baseline only).
- Kaggle commit/submit-mode execution unless explicitly run and recorded (**DEF-002B**).
- Leaderboard submission, acceptance, or score.
- Active BirdCLEF+ 2026 submission eligibility (final deadline passed).
- CPU 90-minute scoring runtime compliance unless commit/submit evidence records runtime.
- Real `sample_submission.csv` compatibility in synthetic fallback mode.

---

## Baseline modes

| Mode | Trigger | Output path |
|------|---------|-------------|
| `REAL_SAMPLE_ZERO_BASELINE` | `sample_submission.csv` found under `/kaggle/input` | `/kaggle/working/submission.csv` |
| `SYNTHETIC_FALLBACK_ONLY` | No real sample file on Kaggle (or local default) | `tmp/submissions/m03_synthetic_baseline.csv` |

The notebook prints all candidate paths, discovery results, and the selected path.

---

## Local behavior

Default (synthetic only):

```bash
python scripts/run_m03_baseline_local.py
```

Output: `tmp/submissions/m03_synthetic_baseline.csv`

Optional real sample (file must stay **outside git**, never committed):

```bash
python scripts/run_m03_baseline_local.py --sample-submission /path/to/sample_submission.csv
```

Output: `tmp/submissions/m03_sample_zero_baseline.csv`

Local runs never write repository-root `submission.csv`. `tmp/` is gitignored; `scripts/verify_repo_state.py` must pass.

---

## Kaggle real sample behavior

When competition data is attached on Kaggle, the notebook:

1. Prints environment diagnostics (Python, platform, cwd, `sys.path`, Kaggle env vars, `/kaggle` paths).
2. Lists explicit candidates and discovers any `sample_submission.csv` under `/kaggle/input`.
3. Reads the selected file with stdlib `csv`.
4. Treats every column except `row_id` as a class/probability column.
5. Writes zero baseline to `/kaggle/working/submission.csv`.

If `pantanal_1` is not installed, inline fallback mirrors the same logic.

---

## Evidence required to close deferred issues

**DEF-002B** (scored/commit-mode real submission path):

- Commit/submit-mode notebook run in CPU environment.
- Recorded evidence that `/kaggle/working/submission.csv` was produced in that mode.
- Documented in `docs/kaggle/kaggle_setup_evidence.md`.

Interactive-only runs that produce `/kaggle/working/submission.csv` narrow the path but do **not** alone close DEF-002B unless criteria explicitly include interactive proof.

**DEF-003** (real `sample_submission.csv` alignment):

- Observed real sample path on Kaggle.
- Recorded row count, column count, and header preview matching competition sample.
- Schema alignment validated in notebook output and recorded in evidence.

Repo-side structural tests do not close DEF-003 without Kaggle observation.

---

## Manual Kaggle evidence (owner step)

After green PR-head CI, copy/run `notebooks/pantanal_1_m03_baseline.ipynb` on Kaggle and record in `docs/kaggle/kaggle_setup_evidence.md`:

- Whether `sample_submission.csv` was discovered and exact path
- Whether `/kaggle/working/submission.csv` was produced
- Row count, column count, runtime if visible
- Mode: Interactive or Commit/Submit
- Whether submission/scoring was possible

Do not close M03 on repo implementation alone if manual Kaggle evidence is planned.

---

## Zero baseline reminder

M03 zero baseline sets all class probabilities to `0.0`. It is **not** meaningful model inference and is not expected to be competitive.
