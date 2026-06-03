# M14 Private Training Runbook (Public-Safe)

Public-safe runbook for executing the first audio-derived baseline training in the **private ORNITHOS/5090 Blackwell lane**. This document does **not** include runnable commands that assume private paths, credentials, or competition data locations.

**Authority:** Subordinate to `docs/pantanal-1.md`, M13 planning package, and `docs/analysis/M14_evidence_contract.md`.

**M14 status:** Runbook contract only. Training is **not** executed in PANTANAL-1 during M14.

---

## Boundary reminder

| Lane | Role |
|------|------|
| ORNITHOS / private | Training, feature extraction, OOF evaluation, export |
| PANTANAL-1 / public | Evidence contract, manifest guidance, future ingest review |

ORNITHOS must not host Kaggle notebooks, generate `submission.csv` for leaderboard workflow, or claim final BirdCLEF submission readiness. PANTANAL-1 owns public packaging (M15+).

---

## Primary and fallback candidates (preserved from M13)

| Priority | Approach |
|----------|----------|
| **Primary** | Public pretrained bioacoustic/audio embedding + shallow classifier head |
| **Fallback** | Dependency-light mel-spectrogram baseline with small CPU-exportable head |

M14 does not lock a single architecture; private lane should document which candidate was selected in the manifest and model card.

---

## Phase 1 — License screen

**Goal:** Confirm competition rules and license compliance before downloading weights or training.

Checklist (private lane):

- [ ] Backbone license permits competition use and offline inference packaging
- [ ] No NC-incompatible redistribution into public repo
- [ ] Record `source.pretrained_backbone` and `source.backbone_license` in manifest
- [ ] Document license summary for PANTANAL-1 ingest (public-safe text only)

**Stop if:** License blocks offline CPU packaging or competition use.

---

## Phase 2 — Candidate selection

**Goal:** Choose primary or fallback path with documented rationale.

Checklist:

- [ ] Evaluate primary embedding + shallow head feasibility (export size, CPU dry-run estimate)
- [ ] If blocked, document switch to mel-spectrogram fallback
- [ ] Record candidate family in model card (no private code in public copy)
- [ ] Do not commit selection as a score or quality claim until G1+ evidence exists

Reference: `docs/analysis/M13_blackwell_training_plan.md` candidate families (BirdNET-style, PANNs/CNN14, mel fallback, etc.).

---

## Phase 3 — Private feature extraction and training

**Goal:** Train first audio-derived baseline with non-constant predictions.

Checklist (private lane only):

- [ ] Use BirdCLEF+ 2026 training data only in private storage (never commit audio)
- [ ] Define validation split (stratified by species/recording where possible)
- [ ] Train shallow head (optional light backbone adaptation on 5090)
- [ ] Save checkpoints only in private storage unless owner approves public binary

**Public repo:** No weights, no raw audio, no competition CSVs in git.

---

## Phase 4 — OOF / local evaluation

**Goal:** Produce validation evidence suitable for public-safe summary ingest.

Checklist:

- [ ] Compute per-class and macro metrics on held-out split (metric names documented)
- [ ] Allow null metrics in planning-only summaries; populate when training completes
- [ ] Document failure cases (silent segments, label noise) in public-safe prose
- [ ] Do not paste raw prediction vectors that could leak private labels or audio linkage

Output target: `validation_summary` JSON per `schemas/m14_validation_summary.schema.json`.

---

## Phase 5 — Non-constant prediction check

**Goal:** Prove predictions vary beyond M04/M11 constant baselines (G1 gate).

Checklist:

- [ ] Verify per-class or per-row score variance (not identical across all rows)
- [ ] Set `non_constant_predictions_verified: true` only when check passes
- [ ] Produce public-safe `non_constant_prediction_summary` (aggregates only; no raw private predictions if leakage risk)
- [ ] Reject G1 claims if predictions are uniform or constant

---

## Phase 6 — CPU export profiling

**Goal:** Estimate Kaggle CPU ≤ 90-minute feasibility (G2 gate).

Checklist:

- [ ] Record model load time estimate
- [ ] Record per 5-second window inference time estimate
- [ ] Document dependency footprint for offline notebook packaging
- [ ] Confirm `internet_required_at_score_time: false` in manifest
- [ ] Flag `cpu_feasibility: at_risk` if transformer-scale export is too heavy

Output target: public-safe CPU timing summary JSON (future ingest; not required in M14).

---

## Phase 7 — Manifest and model card generation

**Goal:** Assemble public-safe documentation package.

Checklist:

- [ ] Fill manifest per `docs/models/M14_MODEL_MANIFEST_SCHEMA.md`
- [ ] Set `status` to `private-trained-summary` when training exists (not `planning-only`)
- [ ] Copy and complete `docs/models/M14_model_card_template.md`
- [ ] Strip all private absolute paths
- [ ] Use `null` hashes until owner approves binary ingest

---

## Phase 8 — PANTANAL-1 ingest review

**Goal:** Owner-gated review before any public claim update.

Checklist:

- [ ] Run `python scripts/verify_repo_state.py` in PANTANAL-1
- [ ] Run `python scripts/validate_m14_evidence.py <validation_summary.json>`
- [ ] Confirm no prohibited artifacts in git diff
- [ ] Owner approves manifest, validation summary, and any binary exception
- [ ] Update `docs/pantanal-1.md` only with claim-safe language (no score > 0.500 unless observed on Kaggle)

Defer Kaggle notebook wiring to **M15** unless separately authorized.

---

## Claim ladder alignment (M13 evaluation plan)

| Gate | This runbook phase |
|------|-------------------|
| G0 | M13/M14 planning and evidence contract |
| G1 | Phases 4–5 (OOF + non-constant) |
| G2 | Phase 6 (CPU export profiling) |
| G3–G4 | M15+ Kaggle commit and public score |
| G5 | Separate working-note milestone |

---

## Non-claims

- This runbook does not authorize training inside PANTANAL-1.
- Completing the runbook in private lane does not automatically update Ultimate Truth claims.
- No score improvement claim unless public Kaggle score **> 0.500** is observed and documented.
