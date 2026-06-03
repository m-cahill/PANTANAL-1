# PANTANAL-1 — Ultimate Truth

**Repository:** https://github.com/m-cahill/PANTANAL-1  
**Competition:** [BirdCLEF+ 2026](https://www.kaggle.com/competitions/birdclef-2026/)  
**Last updated:** 2026-06-03 (M12 in progress)

---

## Milestone artifacts

| Milestone | Plan | Summary | Audit | Toolcalls |
|-----------|------|---------|-------|-----------|
| M00 | [M00_plan.md](milestones/M00/M00_plan.md) | [M00_summary.md](milestones/M00/M00_summary.md) | [M00_audit.md](milestones/M00/M00_audit.md) | [M00_toolcalls.md](milestones/M00/M00_toolcalls.md) |
| M01 | [M01_plan.md](milestones/M01/M01_plan.md) | [M01_summary.md](milestones/M01/M01_summary.md) | [M01_audit.md](milestones/M01/M01_audit.md) | [M01_toolcalls.md](milestones/M01/M01_toolcalls.md) |
| M02 | [M02_plan.md](milestones/M02/M02_plan.md) | [M02_summary.md](milestones/M02/M02_summary.md) | [M02_audit.md](milestones/M02/M02_audit.md) | [M02_toolcalls.md](milestones/M02/M02_toolcalls.md) |
| M03 | [M03_plan.md](milestones/M03/M03_plan.md) | [M03_summary.md](milestones/M03/M03_summary.md) | [M03_audit.md](milestones/M03/M03_audit.md) | [M03_toolcalls.md](milestones/M03/M03_toolcalls.md) |
| M04 | [M04_plan.md](milestones/M04/M04_plan.md) | [M04_summary.md](milestones/M04/M04_summary.md) | [M04_audit.md](milestones/M04/M04_audit.md) | [M04_toolcalls.md](milestones/M04/M04_toolcalls.md) |
| M05 | [M05_plan.md](milestones/M05/M05_plan.md) | [M05_summary.md](milestones/M05/M05_summary.md) | [M05_audit.md](milestones/M05/M05_audit.md) | [M05_toolcalls.md](milestones/M05/M05_toolcalls.md) |
| M06 | [M06_plan.md](milestones/M06/M06_plan.md) | [M06_summary.md](milestones/M06/M06_summary.md) | [M06_audit.md](milestones/M06/M06_audit.md) | [M06_toolcalls.md](milestones/M06/M06_toolcalls.md) |
| M07 | [M07_plan.md](milestones/M07/M07_plan.md) | [M07_summary.md](milestones/M07/M07_summary.md) | [M07_audit.md](milestones/M07/M07_audit.md) | [M07_toolcalls.md](milestones/M07/M07_toolcalls.md) |
| M08 | [M08_plan.md](milestones/M08/M08_plan.md) | [M08_summary.md](milestones/M08/M08_summary.md) | [M08_audit.md](milestones/M08/M08_audit.md) | [M08_toolcalls.md](milestones/M08/M08_toolcalls.md) |
| M09 | [M09_plan.md](milestones/M09/M09_plan.md) | [M09_summary.md](milestones/M09/M09_summary.md) | [M09_audit.md](milestones/M09/M09_audit.md) | [M09_toolcalls.md](milestones/M09/M09_toolcalls.md) |
| M10 | [M10_plan.md](milestones/M10/M10_plan.md) | [M10_summary.md](milestones/M10/M10_summary.md) | [M10_audit.md](milestones/M10/M10_audit.md) | [M10_toolcalls.md](milestones/M10/M10_toolcalls.md) |
| M11 | [M11_plan.md](milestones/M11/M11_plan.md) | [M11_summary.md](milestones/M11/M11_summary.md) | [M11_audit.md](milestones/M11/M11_audit.md) | [M11_toolcalls.md](milestones/M11/M11_toolcalls.md) |
| M12 | [M12_plan.md](milestones/M12/M12_plan.md) | — | — | [M12_toolcalls.md](milestones/M12/M12_toolcalls.md) |

**M05 analysis:** [post_competition_analysis.md](analysis/post_competition_analysis.md), [next_milestone_decision_matrix.md](analysis/next_milestone_decision_matrix.md), [M00_M04_evidence_index.md](analysis/M00_M04_evidence_index.md).

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
| M05 | Baseline improvement planning / post-competition analysis | closed | PR #6; [summary](milestones/M05/M05_summary.md), [audit](milestones/M05/M05_audit.md); [analysis](analysis/post_competition_analysis.md); [matrix](analysis/next_milestone_decision_matrix.md); [index](analysis/M00_M04_evidence_index.md) |
| M06 | Audit hardening / evidence consolidation | closed | PR #7; [summary](milestones/M06/M06_summary.md), [audit](milestones/M06/M06_audit.md); [audit hardening](quality/audit_hardening.md); coverage + mypy gates (DEF-001 partial through M06) |
| M07 | Security and supply-chain audit gate | closed | PR #8; [summary](milestones/M07/M07_summary.md), [audit](milestones/M07/M07_audit.md); [security supply chain](quality/security_supply_chain.md); DEF-001 substantially addressed (Bandit + pip-audit) |
| M08 | Working-note outline / evidence narrative seed | closed | PR #9; [summary](milestones/M08/M08_summary.md), [audit](milestones/M08/M08_audit.md); [outline](working_note/working_note_outline.md), [evidence map](working_note/evidence_map.md) |
| M09 | Working-note draft planning / public narrative decision gate | closed | PR #10; [summary](milestones/M09/M09_summary.md), [audit](milestones/M09/M09_audit.md); [decision gate](working_note/draft_decision_gate.md), [readiness checklist](working_note/draft_readiness_checklist.md), [recommendation](analysis/M09_next_direction_recommendation.md) |
| M10 | Real inference baseline spike | closed | PR #11; [summary](milestones/M10/M10_summary.md), [audit](milestones/M10/M10_audit.md); uniform-ε nonzero baseline (M10B); [nonzero baseline doc](kaggle/nonzero_baseline.md) |
| M11 | Kaggle non-zero baseline evidence probe | closed | PR #12; [summary](milestones/M11/M11_summary.md), [audit](milestones/M11/M11_audit.md); [runbook](kaggle/m11_nonzero_baseline_runbook.md), [evidence](kaggle/m11_nonzero_baseline_evidence.md); `notebooks/pantanal_1_m11_nonzero_baseline.ipynb` |
| M12 | Scoring Methodology and Working-Note Criteria Audit | in progress | [plan](milestones/M12/M12_plan.md); [scoring audit](analysis/M12_scoring_methodology_audit.md), [working-note criteria audit](working_note/M12_working_note_criteria_audit.md), [next direction](analysis/M12_next_direction_decision.md) |

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
- PANTANAL-1 adds audit-hardening CI gates for source coverage and mypy type checking, improving enterprise CI posture without changing Kaggle notebook behavior (M06; see `docs/quality/audit_hardening.md`).
- PANTANAL-1 adds security and dependency audit gates using Bandit and pip-audit, further hardening CI without changing Kaggle notebook behavior (M07; see `docs/quality/security_supply_chain.md`).
- PANTANAL-1 contains a working-note outline and evidence map that organize the M00–M07 governance, Kaggle, and audit evidence into a public narrative seed (M08; see `docs/working_note/working_note_outline.md`, `docs/working_note/evidence_map.md`).
- PANTANAL-1 contains a working-note draft decision gate, readiness checklist, and next-direction recommendation that evaluate whether to draft, pivot to inference, or archive/template the project (M09; see `docs/working_note/draft_decision_gate.md`, `docs/working_note/draft_readiness_checklist.md`, `docs/analysis/M09_next_direction_recommendation.md`).
- PANTANAL-1 contains a deterministic non-zero baseline generator that preserves submission schema and produces valid non-zero probability values without adding model weights or training (M10; see `docs/kaggle/nonzero_baseline.md`, `src/pantanal_1/nonzero_baseline.py`).
- PANTANAL-1 contains a runbook, evidence template, and output-cleared notebook for evaluating the M10 deterministic non-zero baseline on Kaggle without overclaiming model quality (M11; see `docs/kaggle/m11_nonzero_baseline_runbook.md`, `docs/kaggle/m11_nonzero_baseline_evidence.md`, `notebooks/pantanal_1_m11_nonzero_baseline.ipynb`).
- M11 recorded Kaggle evidence for the uniform-ε non-zero baseline. The notebook produced a valid Kaggle submission path and received public score **0.500**, matching the prior all-zero baseline score of **0.500** (`pantanal_1_m03_baseline` Version 2); **no score improvement was observed** (see `docs/kaggle/m11_nonzero_baseline_evidence.md`). Interactive run also evidenced `/kaggle/working/submission.csv` (3 rows, 235 columns) with ε **0.001** and inline fallback.
- PANTANAL-1 contains M12 scoring methodology and working-note criteria audits that explain why all-zero and uniform-ε baselines both scored **0.500**, assess working-note readiness, and recommend the next milestone (M12; see `docs/analysis/M12_scoring_methodology_audit.md`, `docs/working_note/M12_working_note_criteria_audit.md`, `docs/analysis/M12_next_direction_decision.md`).

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

**M06 explicit non-claims:**

- M06 does not implement model inference.
- M06 does not improve leaderboard score.
- M06 does not prove model quality.
- M06 does not add a complete security/supply-chain hardening stack.
- M06 does not fully close DEF-001.

**M07 explicit non-claims:**

- M07 does not implement model inference.
- M07 does not improve leaderboard score.
- M07 does not prove model quality.
- M07 does not add SBOM/provenance/action pinning.
- M07 does not prove the project is vulnerability-free.

**M08 explicit non-claims:**

- M08 does not create a full working-note draft.
- M08 does not make the project CLEF submission-ready.
- M08 does not implement model inference.
- M08 does not prove model quality.
- M08 does not improve leaderboard score.
- M08 does not claim RediAI certification.

**M09 explicit non-claims:**

- M09 does not create a full working-note draft.
- M09 does not make the project CLEF submission-ready.
- M09 does not implement model inference.
- M09 does not prove model quality.
- M09 does not improve leaderboard score.
- M09 does not claim RediAI certification.

**M10 explicit non-claims:**

- M10 does not implement trained model inference.
- M10 does not prove audio understanding.
- M10 does not prove model quality.
- M10 does not improve leaderboard score unless separately scored and evidenced.
- M10 does not add model weights.
- M10 does not claim RediAI certification.

**M11 explicit non-claims:**

- M11 does not prove model quality.
- M11 does not prove audio understanding.
- M11 does not prove trained model inference.
- M11 does not prove score improvement.
- M11 does not add model weights.
- M11 does not claim RediAI certification.
- M11 does not prove competitive performance.
- M11 does not prove working-note readiness.

**M12 explicit non-claims:**

- M12 does not implement model inference.
- M12 does not improve leaderboard score.
- M12 does not add audio dependencies.
- M12 does not add model weights.
- M12 does not create a full working-note draft.
- M12 does not prove working-note readiness.
- M12 does not claim RediAI certification.
- M12 does not prove model quality or audio understanding.

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
| DEF-001 | Coverage / mypy / security audit gates | substantially addressed (M07) | **Status: substantially addressed in M07** (not fully closed). **Evidence:** coverage + mypy gates in M06 (`docs/quality/audit_hardening.md`); Bandit + pip-audit gates in M07 (`docs/quality/security_supply_chain.md`). **Remaining optional hardening:** SBOM generation, GitHub Actions SHA pinning, provenance/attestation |
| DEF-002A | Kaggle interactive synthetic smoke | M02 (evidenced) | Patched smoke notebook runs in Kaggle interactive mode and produces synthetic CSV under `tmp/submissions/` (see `docs/kaggle/kaggle_setup_evidence.md`) |
| DEF-002B | Kaggle scored/commit-mode real submission path | M04 (evidenced) | Kaggle competition notebook Version 2 completed successfully, produced an output file, and received public score 0.500 (see `docs/kaggle/m04_commit_mode_evidence.md`) |
| DEF-003A | Real sample_submission.csv schema discovery and zero-baseline alignment | M03 (evidenced) | Real `sample_submission.csv` discovered on Kaggle; zero baseline preserves sample header/row order (see `docs/kaggle/m03_kaggle_evidence.md`) |
| DEF-003B | Scored/hidden test submission schema behavior | M04 (narrowed/evidenced) | Kaggle scoring accepted zero-baseline output and returned public score 0.500; hidden-test internals not exposed in evidence paste |

---

## 12. Next milestone recommendation

**M13 — Audio-Derived Baseline Planning Gate** (primary; pending owner-approved plan). See `docs/milestones/M13/M13_plan.md` when seeded after M12 closeout.

M12 audited scoring methodology (all-zero and uniform-ε both **0.500**), working-note criteria readiness, and next direction (`docs/analysis/M12_scoring_methodology_audit.md`, `docs/working_note/M12_working_note_criteria_audit.md`, `docs/analysis/M12_next_direction_decision.md`). Before adding audio dependencies, M13 should choose the smallest CPU-compatible, license-safe, Kaggle-compatible audio-derived baseline path.

| Priority | Direction |
|----------|-----------|
| **Primary** | **M13 — Audio-Derived Baseline Planning Gate** |
| **Secondary** | **M13B — Working-note draft v0** |
| **Tertiary** | **M13C — Archive / template hardening** |
| Also available | **M13D — Kaggle packaging hardening**; **DEF-001 optional** — SBOM/provenance |

Do not begin M13 until owner approves `docs/milestones/M13/M13_plan.md` after M12 closeout.
