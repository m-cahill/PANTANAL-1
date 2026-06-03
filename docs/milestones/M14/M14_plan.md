# M14 — 5090 Blackwell Audio-Derived Baseline Training Sprint

**Status:** Stub only. Implementation not started. Owner approval required before any M14 work.

---

## Purpose

Execute the first **audio-derived** baseline training and validation sprint in the private ORNITHOS/5090 Blackwell lane, producing non-constant predictions and a public-safe export plan per M13.

M13 delivered planning only (`docs/analysis/M13_*.md`). M14 is the first milestone authorized to **train** and **evaluate**—not to commit private artifacts to PANTANAL-1 without manifest approval.

---

## Authoritative inputs (from M13)

| Document | Role |
|----------|------|
| `docs/analysis/M13_audio_baseline_strategy.md` | Primary: pretrained embedding + shallow head; fallback: mel baseline |
| `docs/analysis/M13_blackwell_training_plan.md` | Candidate families and M14 experiment plan |
| `docs/analysis/M13_artifact_boundary_plan.md` | ORNITHOS → PANTANAL-1 handoff, manifest, hashes |
| `docs/analysis/M13_kaggle_inference_packaging_plan.md` | CPU offline packaging target |
| `docs/analysis/M13_evaluation_plan.md` | Claim ladder; no improvement unless public score > 0.500 |

---

## Likely scope (when approved)

- Private-lane training on 5090 Blackwell
- Candidate evaluation (BirdNET-style, PANNs/CNN14, AudioMAE/AST, EfficientNet-mel, mel fallback)
- OOF validation proving **non-constant** predictions
- CPU export timing estimate
- Public-safe manifest and validation summary (no weights in git unless owner-approved)

---

## Out of scope until explicitly authorized

- Committing raw audio, Kaggle competition data, credentials, or private ORNITHOS code to PANTANAL-1
- Committing model weights to git without owner approval and manifest
- Kaggle notebook changes (defer to M15)
- Kaggle submissions without separate authorization
- Claims of score improvement, model quality, or working-note readiness without evidence
- RediAI certification

---

## Guardrails (binding)

- ORNITHOS remains private upstream; PANTANAL-1 remains public packaging
- No score claims without observed public score > **0.500**
- Follow `docs/analysis/M13_artifact_boundary_plan.md` for any public ingest
- Blackwell training is **planned in M14** but not executed during M13 closeout

---

## Owner gate

Do not begin M14 implementation until the owner approves this plan (or a successor plan) in writing.
