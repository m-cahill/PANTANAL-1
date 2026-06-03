# Working Note Draft v0 — PANTANAL-1

**Status:** Draft v0 only. Not CLEF submission-ready. Not final publication prose.

**Authority:** Subordinate to `docs/pantanal-1.md`.

**Related:** [working_note_outline.md](working_note_outline.md), [evidence_map.md](evidence_map.md), [M16_final_evidence_lock.md](M16_final_evidence_lock.md).

---

## Title

A governed Kaggle submission pipeline for BirdCLEF+ 2026: milestone evidence from zero-baseline contract validation to pre-deadline evidence lock

---

## Abstract (draft)

PANTANAL-1 is the public, Kaggle-facing repository for the BirdCLEF+ 2026 competition. This draft v0 describes a governance-first approach: validate submission contracts, exercise interactive and commit-mode notebook paths, record scored baseline results, harden CI, and prepare a public-safe handoff for future audio-derived work—without claiming competitive model performance.

Two scored baselines were accepted by Kaggle with public score **0.500** each: an all-zero baseline (M04) and a uniform-ε non-zero baseline (M11). Both produce effectively constant predictions and therefore provide no ranking signal. The repository’s value in this phase is **evidence discipline** and **submission-path verification**, not predictive accuracy.

---

## 1. Motivation

BirdCLEF+ 2026 requires species classification from passive acoustic monitoring audio in the Brazilian Pantanal. Kaggle Notebooks are the only submission surface; CPU runtime is capped at 90 minutes; internet is disabled during scoring.

PANTANAL-1 was created to own **public competition packaging**: governance, `submission.csv` contracts, notebook paths, and auditable milestone evidence. Private model development remains in ORNITHOS; PANTANAL-1 does not import private ORNITHOS code or commit competition data, weights, or secrets.

With roughly one hour before the final submission deadline, the project prioritizes a **truthful narrative lock** (this draft and final evidence index) over unvalidated new notebook or model work.

---

## 2. Competition constraints (binding)

| Constraint | Requirement |
|------------|-------------|
| Submission surface | Kaggle Notebooks only |
| Runtime | CPU ≤ 90 minutes (GPU effectively unusable) |
| Internet | Disabled during scoring |
| Output file | `submission.csv` |
| Row window | 5 seconds per `row_id` |
| Class columns | 234 species probabilities |
| Competition data | CC BY-NC-SA 4.0 — not redistributed from this repo |

See `docs/BirdCLEFrules.md`, `docs/kaggle/competition_snapshot.md`, `docs/kaggle/submission_contract.md`.

---

## 3. Methodology timeline (M00–M15)

| Milestone | Focus | Outcome (evidence-linked) |
|-----------|-------|---------------------------|
| M00 | Repo bootstrap, governance | Public scaffold, Ultimate Truth, policies |
| M01 | Submission contract | Synthetic 234-column CSV contract |
| M02 | Kaggle smoke | Interactive synthetic path |
| M03 | Baseline notebook | Real `sample_submission.csv`; interactive zero baseline |
| M04 | Commit-mode probe | Scored path; public score **0.500** (all-zero) |
| M05 | Post-competition analysis | Decision matrix; evidence index |
| M06 | Audit hardening | Coverage + mypy CI gates |
| M07 | Security gate | Bandit + pip-audit |
| M08 | Working-note seed | Outline + evidence map |
| M09 | Draft decision gate | Readiness checklist; direction recommendation |
| M10 | Non-zero baseline spike | Deterministic uniform-ε generator (repo) |
| M11 | Kaggle ε baseline probe | Scored path; public score **0.500** (no improvement) |
| M12 | Scoring audit | Why 0.500 for constant predictions; working-note criteria |
| M13 | Audio planning | Blackwell training, packaging, evaluation plans |
| M14 | Evidence contract | M14 schema, validator, manifest, runbook |
| M15 | Evidence request | Pre-ingest packet for private lane (no bundle supplied) |

Each closed milestone has plan, summary, audit, and toolcalls under `docs/milestones/MNN/`.

---

## 4. Baseline results

### M04 — All-zero baseline (primary scored evidence)

- Notebook: `pantanal_1_m03_baseline` **Version 2**
- Mode: Commit/submit (competition notebook)
- Runtime: ~67s (owner paste)
- Public score: **0.500**
- Evidence: `docs/kaggle/m04_commit_mode_evidence.md`

### M11 — Uniform-ε non-zero baseline

- Notebook: `pantanal_1_m11_nonzero_baseline` **Version 2**
- ε = **0.001** (deterministic, no trained model)
- Public score: **0.500** (matches M04; **no improvement**)
- Evidence: `docs/kaggle/m11_nonzero_baseline_evidence.md`

**Interpretation:** Both baselines are accepted by Kaggle scoring but are not competitive. Neither demonstrates audio understanding or species discrimination.

---

## 5. Scoring interpretation

Public score **0.500** for both baselines is consistent with **constant or near-constant predictions** across classes:

- All-zero: every class probability 0.0
- Uniform-ε: every class probability ε (e.g. 0.001)

When predictions do not vary meaningfully across samples or classes, ranking metrics provide **no discriminative signal**. The score evidences **pipeline acceptance** (valid `submission.csv`, schema, commit path), not model quality.

See `docs/analysis/M12_scoring_methodology_audit.md`.

---

## 6. Governance and audit method

PANTANAL-1 uses a milestone workflow:

1. **Plan** — single objective, explicit scope and non-claims
2. **Implementation** — minimal diff; branch + PR to `main`
3. **CI** — ruff, mypy, pytest (≥80% coverage on `src/`), Bandit, pip-audit, `verify_repo_state.py`
4. **Run analysis** — `MNN_run1.md` per workflow prompt
5. **Summary and audit** — canonical closure artifacts
6. **Ultimate Truth** — `docs/pantanal-1.md` updated with claims and non-claims only when evidenced

**Boundary enforcement:** `.gitignore` + `scripts/verify_repo_state.py` block raw audio, Kaggle CSVs, weights, secrets, generated submissions.

**Audit posture:** Milestone audits (M00–M15) record delta risk, CI truthfulness, and score trends. Audits support governance; they do not substitute for Kaggle runtime evidence.

---

## 7. Audio-derived future work path (not executed in PANTANAL-1)

Planning milestones defined a post-deadline path without implementing training:

| Stage | Document | Status |
|-------|----------|--------|
| Strategy | `docs/analysis/M13_audio_baseline_strategy.md` | Planning only |
| Blackwell training | `docs/analysis/M13_blackwell_training_plan.md` | Private lane (ORNITHOS) |
| Evidence contract | `docs/analysis/M14_evidence_contract.md` | Contract + validator |
| Request packet | `docs/analysis/M15_private_lane_evidence_request.md` | No bundle ingested |

Future ingest requires a public-safe bundle validated by `scripts/validate_m14_evidence.py` and go/no-go per `docs/analysis/M15_ingest_decision_gate.md`.

---

## 8. Limitations and non-claims

This draft v0 does **not** claim:

- Useful model training or inference quality
- Score improvement over **0.500**
- G1/G2/G3/G4 evaluation-gate evidence
- Private leaderboard performance beyond observed public scores
- Full hidden-test internals (DEF-003B narrowed for acceptance only)
- RediAI certification
- CLEF-ready or final publication readiness
- Audio understanding from uniform-ε or zero baselines

**Proven in-repo:** Governance scaffold, submission contract, Kaggle interactive and commit paths, two scored **0.500** baselines, CI hardening, working-note seed, audio planning and evidence contract, pre-ingest request packet.

---

## 9. Evidence references

| Topic | Primary sources |
|-------|----------------|
| Ultimate Truth | `docs/pantanal-1.md` |
| M04 scored evidence | `docs/kaggle/m04_commit_mode_evidence.md` |
| M11 scored evidence | `docs/kaggle/m11_nonzero_baseline_evidence.md` |
| Scoring methodology | `docs/analysis/M12_scoring_methodology_audit.md` |
| Evidence map (M00–M07) | `docs/working_note/evidence_map.md` |
| M00–M15 summaries | `docs/milestones/MNN/MNN_summary.md` |
| Final evidence lock | `docs/working_note/M16_final_evidence_lock.md` |
| Submission decision | `docs/analysis/M16_final_submission_decision.md` |

---

## Version note

This file supersedes the M08 outline as the **first end-to-end readable draft**, extended through M15. It remains v0: concise, evidence-linked, and explicitly non-competitive.
