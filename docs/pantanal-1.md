# PANTANAL-1 — Ultimate Truth

**Repository:** https://github.com/m-cahill/PANTANAL-1  
**Competition:** [BirdCLEF+ 2026](https://www.kaggle.com/competitions/birdclef-2026/)  
**Last updated:** 2026-06-03 (M05 in progress)

---

## Milestone artifacts

| Milestone | Plan | Summary | Audit | Toolcalls |
|-----------|------|---------|-------|-----------|
| M00 | [M00_plan.md](milestones/M00/M00_plan.md) | [M00_summary.md](milestones/M00/M00_summary.md) | [M00_audit.md](milestones/M00/M00_audit.md) | [M00_toolcalls.md](milestones/M00/M00_toolcalls.md) |
| M01 | [M01_plan.md](milestones/M01/M01_plan.md) | [M01_summary.md](milestones/M01/M01_summary.md) | [M01_audit.md](milestones/M01/M01_audit.md) | [M01_toolcalls.md](milestones/M01/M01_toolcalls.md) |
| M02 | [M02_plan.md](milestones/M02/M02_plan.md) | [M02_summary.md](milestones/M02/M02_summary.md) | [M02_audit.md](milestones/M02/M02_audit.md) | [M02_toolcalls.md](milestones/M02/M02_toolcalls.md) |
| M03 | [M03_plan.md](milestones/M03/M03_plan.md) | [M03_summary.md](milestones/M03/M03_summary.md) | [M03_audit.md](milestones/M03/M03_audit.md) | [M03_toolcalls.md](milestones/M03/M03_toolcalls.md) |
| M04 | [M04_plan.md](milestones/M04/M04_plan.md) | [M04_summary.md](milestones/M04/M04_summary.md) | [M04_audit.md](milestones/M04/M04_audit.md) | [M04_toolcalls.md](milestones/M04/M04_toolcalls.md) |
| M05 | [M05_plan.md](milestones/M05/M05_plan.md) | — | — | [M05_toolcalls.md](milestones/M05/M05_toolcalls.md) |

**M05 note:** Post-competition analysis and next-direction planning ([analysis](analysis/post_competition_analysis.md), [decision matrix](analysis/next_milestone_decision_matrix.md), [M00–M04 index](analysis/M00_M04_evidence_index.md)). Summary/audit after closeout.

---

## 1. Project identity

PANTANAL-1 is the **public**, **Kaggle-facing** repository for BirdCLEF+ 2026: machine learning to identify wildlife species (birds, amphibians, mammals, reptiles, insects) from passive acoustic monitoring audio in the Brazilian Pantanal.

This repo owns competition-facing packaging: governance, submission contracts, Kaggle notebook path, and auditable milestone evidence. It does **not** replace private upstream model development in ORNITHOS.

---

## 2. Source-of-truth rule

If documents disagree about milestone truth, claims, or boundaries, **`docs/pantanal-1.md` wins.**

Derived docs (`docs/boundaries.md`, `docs/kaggle/*`, `docs/policies/*`) must stay aligned with this file.

---

## 3. Boundary model

```text
AURORA owns governed acoustic runtime boundaries.
ORNITHOS owns private bioacoustic model development.
PANTANAL-1 owns public Kaggle/BirdCLEF submission packaging.
RediAI owns certification verdicts.
```

Hard rules:

- Do not import private ORNITHOS code into this repo.
- Do not commit Kaggle competition data, credentials, model weights, or generated runs.
- Do not claim RediAI certification unless explicitly implemented and evidenced here.

See `docs/boundaries.md`.

---

## 4. Competition constraints (binding)

- Submission must be made through **Kaggle Notebooks**.
- **CPU** notebook runtime must be **≤ 90 minutes**.
- GPU notebook submissions are effectively disabled (≈1 minute runtime).
- **Internet access is disabled** during submission scoring.
- Freely and publicly available external data/models are allowed if rules-compliant.
- Submission output must be named **`submission.csv`**.
- Each row covers a **5-second** audio window.
- There are **234** species/class probability columns.
- Competition data is **CC BY-NC-SA 4.0** and must **not** be redistributed from this repo.

Local reference: `docs/BirdCLEFrules.md`, `docs/kaggle/competition_snapshot.md`, `docs/kaggle/submission_contract.md`.

---

## 5. License posture

| Asset | License |
|-------|---------|
| This repository (code/docs scaffold) | Apache 2.0 (`LICENSE`) |
| Kaggle competition data | CC BY-NC-SA 4.0 (non-commercial; do not commit or redistribute) |

---

## 6. Data / weights / secrets non-commit policy

Prohibited in git (enforced by `.gitignore` and `scripts/verify_repo_state.py`):

- Kaggle credentials (`.kaggle/`, `kaggle.json`, `.env`, keys)
- Competition audio and soundscapes (`train_audio/`, `test_soundscapes/`, `train_soundscapes/`, raw audio extensions)
- Model weights and checkpoints
- Generated submissions (`submission.csv`), runs, wandb/mlruns artifacts

See `docs/policies/data_policy.md`, `docs/policies/model_policy.md`, `docs/policies/secrets_policy.md`.

---

## 7. Milestone ledger

| Milestone | Title | Status | Notes |
|-----------|-------|--------|-------|
| M00 | Public repo bootstrap and governance initialization | closed | PR #1; [summary](milestones/M00/M00_summary.md), [audit](milestones/M00/M00_audit.md) |
| M01 | submission.csv skeleton + sample_submission contract | closed | PR #2; [summary](milestones/M01/M01_summary.md), [audit](milestones/M01/M01_audit.md) |
| M02 | Kaggle notebook smoke | closed | PR #3; [summary](milestones/M02/M02_summary.md), [audit](milestones/M02/M02_audit.md); DEF-002A evidenced |
| M03 | Baseline inference notebook / first scored attempt | closed | PR #4; [summary](milestones/M03/M03_summary.md), [audit](milestones/M03/M03_audit.md); DEF-003A evidenced |
| M04 | Kaggle commit-mode submission path probe | closed | PR #5; [summary](milestones/M04/M04_summary.md), [audit](milestones/M04/M04_audit.md); [evidence](kaggle/m04_commit_mode_evidence.md); DEF-002B evidenced; DEF-003B narrowed |
| M05 | Baseline improvement planning / post-competition analysis | in progress | [plan](milestones/M05/M05_plan.md); [analysis](analysis/post_competition_analysis.md); [matrix](analysis/next_milestone_decision_matrix.md); no inference in M05 |

**Ideal handoff path (ORNITHOS M40 charter):** M00 bootstrap → M01 Kaggle site smoke → M02 submission skeleton → M03 baseline notebook → M04 runtime budget → M05 first scored submission → M06 improvement → M07 final lock → M08 working note seed.

**Live deadline compression:** Final submission **2026-06-03 23:59 UTC**. The full M00–M08 sequence is not feasible before the deadline; execute M00 first for safety, then compress to M01–M03 aggressively. Record evidence; do not overclaim.

---

## 8. Current claims

**Implemented:**

- Public repo governance scaffold (M00).
- BirdCLEF rules stored as local documentation (`docs/BirdCLEFrules.md`).
- Boundary, policy, Kaggle snapshot, and submission contract docs.
- Minimal importable package `pantanal_1` at version `0.0.0`.
- Repo state verifier and GitHub Actions CI (lint, compile, pytest, verify).
- Synthetic submission contract: generate and validate zero-baseline submission-shaped CSV with 234 synthetic class columns and 5-second row windows (M01).
- Kaggle-oriented smoke notebook and dependency-free mirror script exercising the synthetic M01 contract surface without competition data (M02; see `docs/kaggle/notebook_smoke.md`).
- Kaggle setup runbook, evidence file, and submission bible (`docs/kaggle/kaggle_setup_runbook.md`, `docs/kaggle/kaggle_setup_evidence.md`, `docs/kaggle/kaggle_submission_bible.md`).
- M02 smoke notebook includes Kaggle environment diagnostics and inline synthetic fallback when `pantanal_1` is not installed.
- **M02 Kaggle interactive evidence:** patched smoke notebook ran in Kaggle interactive mode via inline fallback and produced synthetic smoke CSV at `tmp/submissions/m02_smoke_submission.csv` without competition data (see `docs/kaggle/kaggle_setup_evidence.md`).
- PANTANAL-1 contains a baseline-oriented Kaggle notebook scaffold that can either generate a local synthetic fallback CSV or, when real Kaggle `sample_submission.csv` is available in the Kaggle environment, generate a zero-baseline `/kaggle/working/submission.csv` using that schema (M03 repo-side; see `docs/kaggle/baseline_inference_notebook.md`).
- **M03 Kaggle interactive evidence:** baseline notebook (inline fallback) discovered real `sample_submission.csv` at `/kaggle/input/competitions/birdclef-2026/sample_submission.csv`, selected `REAL_SAMPLE_ZERO_BASELINE`, and produced `/kaggle/working/submission.csv` with 3 rows and 235 columns using the sample schema (see `docs/kaggle/m03_kaggle_evidence.md`). **Interactive mode only** — not scored commit/submit mode.
- **M04 Kaggle commit/scored evidence:** Kaggle competition notebook `pantanal_1_m03_baseline` Version 2 completed successfully in **1m 7s**, Kaggle reported **1 output file**, and received public score **0.500** using the zero-baseline submission path (see `docs/kaggle/m04_commit_mode_evidence.md`).
- PANTANAL-1 contains a post-competition analysis and next-milestone decision matrix evaluating the zero-baseline scored path, remaining gaps, and recommended future directions (M05; see `docs/analysis/post_competition_analysis.md`, `docs/analysis/next_milestone_decision_matrix.md`, `docs/analysis/M00_M04_evidence_index.md`).

**Not yet proven:**

- CPU-only 90-minute **scoring-configuration** compliance (M04 observed short runtime; accelerator/internet not re-recorded in evidence paste).
- Model inference or meaningful model quality.
- Private leaderboard performance beyond observed public score.
- Full hidden/scored-test row count and internals (DEF-003B narrowed for scored acceptance only).
- Working note readiness.

**M01 explicit non-claims:**

- M01 does not prove real Kaggle `sample_submission.csv` compatibility.
- M01 does not prove Kaggle notebook execution.
- M01 does not prove model inference.
- M01 does not prove CPU runtime compliance.
- M01 does not prove leaderboard submission or score.
- M01 does not prove working-note readiness.

**M02 explicit non-claims:**

- M02 does not prove active competition submission eligibility (final deadline passed).
- M02 does not prove real `/kaggle/working/submission.csv` generation or scored commit/submit-mode execution.
- M02 does not prove real Kaggle `sample_submission.csv` compatibility.
- M02 does not prove CPU 90-minute scoring runtime compliance.
- M02 does not prove model inference.
- M02 does not prove leaderboard submission or score.

**M03 explicit non-claims:**

- M03 does not prove active competition submission eligibility.
- M03 does not prove commit/submit-mode or scored submission execution (DEF-002B evidenced in M04).
- M03 does not prove leaderboard submission or score.
- M03 does not prove CPU 90-minute **scoring** runtime compliance (interactive runtime observed only).
- M03 does not prove model inference or meaningful model quality (zero baseline only).
- M03 does not prove hidden/full test row count (sample had 3 rows in observed run).

**M04 explicit non-claims (preserve after scored evidence):**

- M04 does not prove model inference or meaningful model quality (zero baseline only).
- M04 does not prove a competitive solution (public score 0.500 is consistent with all-zero baseline).
- M04 does not prove private leaderboard performance beyond the observed public score.
- M04 does not change the fact that the submitted baseline is all-zero.
- M04 does not prove full hidden/scored-test schema visibility (scored acceptance evidenced; hidden-test internals not exposed in owner paste).
- M04 does not prove CPU/internet scoring-configuration compliance beyond observed short runtime unless those settings are directly re-recorded.

**M05 explicit non-claims:**

- M05 does not implement model inference.
- M05 does not improve leaderboard score.
- M05 does not prove model quality.
- M05 does not add audit hardening gates.
- M05 does not create working-note readiness unless separately scoped.

---

## 9. Explicit non-claims

PANTANAL-1 does **not** currently claim:

- Useful model training or inference quality
- Full hidden/scored-test internals and row counts (DEF-003B narrowed for scored acceptance in M04; not full hidden-test exposure)
- BirdCLEF submission readiness as a competitive solution or meaningful leaderboard performance
- ORNITHOS private artifact reuse in this repo
- AURORA runtime consumption in this repo
- RediAI certification
- Working-note or CLEF publication readiness

---

## 10. Ecosystem reference material (non-binding)

| Path | Role |
|------|------|
| `docs/manuals/` | Operating manuals for adjacent programs (AURORA, ORNITHOS, etc.); context only unless reproduced here |
| `docs/enhancements/` | **Ecosystem reference material**, not binding PANTANAL-1 deliverables. Full-stack items (FastAPI, React/Vite, Netlify, Render, PostgreSQL, Storybook, E2E preview deploys) are **out of scope** unless a future milestone explicitly introduces a web app. Applicable subset: CI truthfulness, linting, tests, artifact discipline, security hygiene, auditable milestone evidence |
| `docs/rediai33/` | RediAI v3.3 reference bundle; certification claims require explicit implementation |
| `docs/prompts/` | Audit/summary/workflow prompt templates for milestones |

Do not rename files in `docs/manuals/`; naming inconsistency is acknowledged and accepted.

---

## 11. Deferred issues register

| ID | Issue | Deferred to | Exit criteria |
|----|-------|-------------|---------------|
| DEF-001 | Coverage / mypy / security audit gates | Post-M00 hardening | CI jobs green with agreed thresholds |
| DEF-002A | Kaggle interactive synthetic smoke | M02 (evidenced) | Patched smoke notebook runs in Kaggle interactive mode and produces synthetic CSV under `tmp/submissions/` (see `docs/kaggle/kaggle_setup_evidence.md`) |
| DEF-002B | Kaggle scored/commit-mode real submission path | M04 (evidenced) | Kaggle competition notebook Version 2 completed successfully, produced an output file, and received public score 0.500 (see `docs/kaggle/m04_commit_mode_evidence.md`) |
| DEF-003A | Real sample_submission.csv schema discovery and zero-baseline alignment | M03 (evidenced) | Real `sample_submission.csv` discovered on Kaggle; zero baseline preserves sample header/row order (see `docs/kaggle/m03_kaggle_evidence.md`) |
| DEF-003B | Scored/hidden test submission schema behavior | M04 (narrowed/evidenced) | Kaggle scoring accepted zero-baseline output and returned public score 0.500; hidden-test internals not exposed in evidence paste |

---

## 12. Next milestone recommendation

**M05 (in progress):** Post-competition analysis and decision matrix complete in repo; see `docs/analysis/post_competition_analysis.md` and `docs/analysis/next_milestone_decision_matrix.md`.

**Recommended after M05 closeout:**

- **Primary — M06B:** Audit hardening / evidence consolidation (address **DEF-001**) if the goal is enterprise-grade closure and a stronger audit score.
- **Secondary — M06A:** Smallest real inference baseline spike if the goal is research momentum (accept dependency/runtime/claim risk).

Also evaluated: M06C (Kaggle packaging), M06D (working-note outline seed), M06E (archive/template cleanup). M05 does not draft the working note.

Do not begin M06 implementation until M05 is merged and owner approves direction.
