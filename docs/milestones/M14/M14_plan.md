# M14 — 5090 Blackwell Audio-Derived Baseline Evidence Contract

**Status:** Implementation milestone (evidence contract only — not training execution).

**Branch:** `m14-audio-baseline-evidence-contract` (from `main`; not from M13 branch).

---

## Objective

Create a public-safe, CI-enforced evidence contract for the first future audio-derived baseline trained in the private/ORNITHOS lane on the 5090 Blackwell.

M14 does **not** train a model inside PANTANAL-1. It prepares the public repository to safely receive and validate future private-lane training evidence without committing raw audio, Kaggle data, weights, checkpoints, private ORNITHOS code, generated submissions, or unverifiable score claims.

M13 closed with an audio-derived baseline planning package. M14 converts that planning package into concrete public-safe validation surfaces.

---

## Authority

- `docs/pantanal-1.md` — Ultimate Truth
- M13 source documents (preserve and operationalize):
  - `docs/analysis/M13_audio_baseline_strategy.md`
  - `docs/analysis/M13_blackwell_training_plan.md`
  - `docs/analysis/M13_artifact_boundary_plan.md`
  - `docs/analysis/M13_kaggle_inference_packaging_plan.md`
  - `docs/analysis/M13_evaluation_plan.md`
  - `docs/milestones/M13/M13_summary.md`
  - `docs/milestones/M13/M13_audit.md`

---

## In-scope deliverables

| # | Path | Purpose |
|---|------|---------|
| 1 | `docs/milestones/M14/M14_plan.md` | This plan |
| 2 | `docs/milestones/M14/M14_toolcalls.md` | Tool/command log |
| 3 | `docs/models/M14_MODEL_MANIFEST_SCHEMA.md` | Human-readable manifest schema |
| 4 | `docs/models/M14_model_card_template.md` | Model card template |
| 5 | `docs/analysis/M14_private_training_runbook.md` | Public-safe private-lane runbook |
| 6 | `docs/analysis/M14_evidence_contract.md` | Evidence bundle definition |
| 7 | `schemas/m14_validation_summary.schema.json` | JSON Schema for validation summaries |
| 8 | `fixtures/m14/validation_summary_planning_only.json` | Planning-only fixture |
| 9 | `fixtures/m14/validation_summary_nonconstant_example.json` | Synthetic non-constant example |
| 10 | `scripts/validate_m14_evidence.py` | Stdlib-only CLI validator |
| 11 | `tests/test_m14_audio_baseline_evidence_contract.py` | Governance + validator tests |
| 12 | `docs/pantanal-1.md` | M14 status, claims, non-claims, next step |

---

## Out of scope

- Model training or feature extraction on real audio
- Audio inference implementation
- New audio/ML dependencies (torch, librosa, sklearn, pandas, numpy, xgboost, etc.)
- Kaggle notebook changes or submissions
- `submission.csv`, raw audio, Kaggle competition data, model weights, private ORNITHOS code
- Score improvement, model quality, RediAI certification, or working-note readiness claims
- M15 Kaggle packaging or private-lane training ingest
- Separate model manifest `.schema.json` (markdown schema only)

---

## Acceptance criteria

1. All M14 docs, schema, fixtures, script, and tests exist.
2. Evidence validator passes both fixtures; rejects malformed/overclaiming planning-only evidence.
3. Governance tests cover boundary, non-claims, evidence contract, no-dependency posture.
4. `docs/pantanal-1.md` records M14 in progress during PR.
5. Local verification suite passes (ruff, mypy, compileall, pytest, coverage ≥80%, bandit, pip-audit, verify_repo_state).
6. PR-head CI green.
7. No prohibited artifacts committed.
8. M14 remains public-safe and evidence-contract only.

---

## Verification commands

```text
ruff check .
ruff format --check .
mypy src/pantanal_1
python -m compileall src tests scripts
pytest -q --cov=src/pantanal_1 --cov-report=term-missing
coverage report --fail-under=80
bandit -r src/pantanal_1
pip-audit -r requirements-dev.txt
python scripts/verify_repo_state.py
```

---

## PR stop point

1. Push branch `m14-audio-baseline-evidence-contract`.
2. Open PR (title: `docs(m14): add audio baseline evidence contract`).
3. Wait for PR-head CI.
4. Do **not** merge.
5. Report branch, PR URL, SHA, CI verdict, files changed, tests added, local results, claims/non-claims.

---

## Closeout (owner approval required)

- Generate `M14_summary.md` and `M14_audit.md` per project prompts.
- Update `docs/pantanal-1.md` from in-progress to closed.
- Seed M15 folder only; do not begin M15 implementation.

---

## M14 claims and non-claims

**Allowed claim:** PANTANAL-1 contains a public-safe evidence contract for future private-lane audio-derived baseline training summaries (validation-summary schema, synthetic fixtures, stdlib validator, model manifest guidance, model card template, private training runbook, governance tests).

**Non-claims:**

- M14 does not train a model.
- M14 does not implement audio inference.
- M14 does not add audio or ML dependencies.
- M14 does not add model weights.
- M14 does not ingest raw audio or Kaggle competition data.
- M14 does not submit to Kaggle.
- M14 does not improve leaderboard score.
- M14 does not prove model quality.
- M14 does not claim RediAI certification.
- M14 does not create working-note readiness.

---

## Next milestone (recommendation only)

**M15** may be either private-lane training evidence ingest or Kaggle packaging, depending on whether the owner supplies a completed private training summary.
