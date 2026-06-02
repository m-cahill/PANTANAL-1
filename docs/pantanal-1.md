# PANTANAL-1 — Ultimate Truth

**Repository:** https://github.com/m-cahill/PANTANAL-1  
**Competition:** [BirdCLEF+ 2026](https://www.kaggle.com/competitions/birdclef-2026/)  
**Last updated:** 2026-06-03 (M00 bootstrap)

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
| M00 | Public repo bootstrap and governance initialization | in progress | Scaffold, CI, verifier, policies |
| M01 | submission.csv skeleton + sample_submission contract | planned | Compressed path (deadline) |
| M02 | Kaggle notebook smoke | planned | Compressed path |
| M03 | Baseline inference notebook / first scored attempt | planned | If eligible |

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

**Not yet proven:**

- Kaggle notebook execution.
- Valid `submission.csv` generation against `sample_submission.csv`.
- CPU-only 90-minute runtime compliance.
- Model inference.
- Leaderboard submission.
- Competition score.
- Working note readiness.

---

## 9. Explicit non-claims

PANTANAL-1 does **not** currently claim:

- Useful model training or inference quality
- BirdCLEF submission readiness or leaderboard performance
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
| DEF-002 | Kaggle notebook smoke | M02 | Notebook runs in Kaggle CPU environment |
| DEF-003 | Valid submission.csv vs sample | M01 | Schema/column contract tests pass |

---

## 12. Next milestone recommendation

After M00 CI is green: **M01 — submission.csv skeleton + sample_submission contract** (see `docs/baselines/baseline_strategy.md`).
