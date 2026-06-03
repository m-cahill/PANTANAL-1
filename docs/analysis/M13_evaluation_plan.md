# M13 Evaluation Plan

## Purpose

Define evidence required before claiming audio-derived baseline improvement, model quality, or working-note scientific contribution.

**Status:** Planning gate only. No evaluation runs in M13.

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/analysis/M12_scoring_methodology_audit.md`.

---

## Baselines (observed)

| Baseline | Milestone | Public score | Interpretation |
|----------|-----------|--------------|----------------|
| All-zero | M04 | **0.500** | Pipeline acceptance; no ranking signal |
| Uniform-ε (0.001) | M11 | **0.500** | Pipeline acceptance; no ranking signal |

Both baselines are **placeholder** submissions. Public **0.500** is consistent with chance-level ROC-AUC for non-separating predictions.

---

## Required Future Evidence (before strong claims)

### Local / OOF validation (M14 private lane)

- [ ] Per-class and macro metrics on held-out split (document metric names; align with competition ROC-AUC where possible)
- [ ] Proof of **non-constant** predictions (histogram / variance per column)
- [ ] Class coverage report (which species receive varying scores)
- [ ] Failure cases (silent segments, unknown species, label noise)
- [ ] Calibration note (optional; not required for first baseline)

### Kaggle public scoring (M15+ if submitted)

- [ ] Commit/submit-mode notebook success
- [ ] `/kaggle/working/submission.csv` produced
- [ ] Public score recorded **only if observed**
- [ ] Compare to **0.500** baselines as factual delta — not as implied quality

### Runtime evidence

- [ ] Total notebook runtime in commit mode
- [ ] Per-stage timing (load audio, feature, infer, write CSV)
- [ ] Confirmation internet disabled and CPU accelerator in evidence paste

### Schema compliance

- [ ] 234 species columns + `row_id`
- [ ] Probabilities in `[0, 1]`
- [ ] Row order aligned to test `sample_submission.csv` when on Kaggle

### Public / private claim limits

- [ ] Public score claims only from observed public leaderboard
- [ ] Private leaderboard claims only if directly observed and documented
- [ ] No hidden-label internals claimed beyond evidence paste

---

## Evaluation Gates (claim ladder)

| Gate | Evidence required | Allowed claim |
|------|-------------------|---------------|
| G0 | M13 planning docs only | Planning package exists; no model |
| G1 | Non-constant OOF/local | Audio-derived signal exists offline |
| G2 | CPU export dry-run | Packaging feasible (timing estimate) |
| G3 | Kaggle commit success + CSV | Scored path accepts submission |
| G4 | Public score > **0.500** | Factual score improvement vs placeholders |
| G5 | Sustained validation + narrative | Working-note contribution (separate milestone) |

M13 stops at **G0**. M14 targets G1–G2. M15 targets G3–G4 if authorized.

---

## Claim Rules

- **No model quality** without validation or score evidence.
- **No score improvement** unless public score **> 0.500** is observed on Kaggle.
- **No private leaderboard claim** unless directly observed and recorded.
- **No RediAI certification** unless separately implemented and evidenced.
- **No working-note readiness** from planning docs alone.
- **No competitive solution claim** from beating 0.500 alone — document magnitude and stability.
- Uniform non-zero values do **not** count as improvement (M11 proved ε path still **0.500**).

---

## What M13 Evaluation Proves

- PANTANAL-1 has a documented evaluation ladder for future milestones.
- Claim discipline remains aligned with M12 scoring audit.
- Baseline comparison references are explicit.

---

## What M13 Evaluation Does Not Prove

- Model quality
- Audio understanding
- Score improvement
- Kaggle runtime compliance for audio model
- Working-note readiness

---

## Cross-References

| Document | Role |
|----------|------|
| `docs/analysis/M13_audio_baseline_strategy.md` | Approach and success criteria |
| `docs/analysis/M13_blackwell_training_plan.md` | M14 training and OOF |
| `docs/analysis/M13_artifact_boundary_plan.md` | Manifest and handoff |
| `docs/analysis/M13_kaggle_inference_packaging_plan.md` | Runtime and packaging |
| `docs/kaggle/m04_commit_mode_evidence.md` | All-zero 0.500 |
| `docs/kaggle/m11_nonzero_baseline_evidence.md` | Uniform-ε 0.500 |

---

## Non-Claims

M13 does not run evaluation, submit to Kaggle, or claim any gate above G0.
