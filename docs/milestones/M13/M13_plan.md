# M13 — Audio-Derived Baseline Planning Gate

## Milestone intent

Create a governed, implementation-ready plan for the first real audio-derived baseline after M12 showed that all-zero and uniform-ε baselines both scored public **0.500**.

M13 is a **planning gate only**. It prepares M14 — **5090 Blackwell Audio-Derived Baseline Training Sprint** — without training models, adding audio/ML dependencies, modifying Kaggle notebooks, or claiming score improvement.

## Current context

M12 closed successfully (PR #13).

Evidence:

- All-zero baseline public score: **0.500** (M04)
- Uniform-ε baseline public score: **0.500** (M11)
- No score improvement observed between placeholder baselines
- Working-note readiness: not yet proven
- M12 recommends M13 as primary next milestone

## Branch

`m13-audio-derived-baseline-planning`

## Strategic direction

```text
ORNITHOS / private training lane:
  raw data, experiments, model training, large artifacts, weights, logs

PANTANAL-1 public repo:
  contracts, inference packaging plans, manifests, small public-safe fixtures,
  evidence templates, Kaggle notebooks, claim-safe documentation
```

Do not import private ORNITHOS code into PANTANAL-1.

## In scope

1. Expand this plan from stub to full plan
2. `docs/analysis/M13_audio_baseline_strategy.md`
3. `docs/analysis/M13_blackwell_training_plan.md`
4. `docs/analysis/M13_artifact_boundary_plan.md`
5. `docs/analysis/M13_kaggle_inference_packaging_plan.md`
6. `docs/analysis/M13_evaluation_plan.md`
7. Update `docs/pantanal-1.md` — M13 in progress, claims, non-claims
8. `tests/test_m13_audio_baseline_planning.py` — governance tests (13 required + protective)
9. `docs/milestones/M13/M13_toolcalls.md`

## Out of scope

- Model training or audio feature extraction implementation
- Audio/ML dependencies (librosa, torch, torchaudio, transformers, timm, sklearn, numpy, pandas, etc.)
- Kaggle notebook changes or submissions
- Leaderboard score claims or model quality claims
- Model weights, raw competition data, private ORNITHOS imports
- Generated runs, full working-note draft, RediAI certification

## Locked planning decisions (owner-approved)

| Topic | Decision |
|-------|----------|
| Primary approach | Public pretrained bioacoustic/audio embedding evaluation + shallow head |
| Fallback | Dependency-light mel-spectrogram baseline |
| Additional candidates | Documented for M14/M15 only — not M13 commitments |
| Artifact handoff | Concrete ORNITHOS → PANTANAL-1 manifest, hash, checklist |
| Kaggle packaging | Primary: external 5090 train → compact export → CPU offline notebook package |
| M14 candidates | BirdNET-style, PANNs/CNN14, AudioMAE/AST, EfficientNet-mel, mel fallback |

## Required documents

| Path | Purpose |
|------|---------|
| `docs/analysis/M13_audio_baseline_strategy.md` | Approach hierarchy and success criteria |
| `docs/analysis/M13_blackwell_training_plan.md` | M14 5090 training sprint plan |
| `docs/analysis/M13_artifact_boundary_plan.md` | Provenance and handoff |
| `docs/analysis/M13_kaggle_inference_packaging_plan.md` | CPU Kaggle packaging |
| `docs/analysis/M13_evaluation_plan.md` | Evidence ladder and claim rules |

## Acceptance criteria

- All five analysis documents exist with required sections
- Ultimate Truth marks M13 **in progress** with narrow claim and explicit non-claims
- Tests enforce planning gate, document presence, and non-claim discipline
- No new runtime dependencies; no `src/` inference changes
- Local verification passes; PR CI green
- Stop before merge without owner approval

## Allowed M13 claim (after implementation)

PANTANAL-1 contains an audio-derived baseline planning package for a future 5090 Blackwell training sprint, including strategy, artifact boundary, Kaggle packaging, and evaluation plans.

## Explicit M13 non-claims

- M13 does not train a model.
- M13 does not implement audio inference.
- M13 does not add audio or ML dependencies.
- M13 does not improve leaderboard score.
- M13 does not add model weights.
- M13 does not claim model quality.
- M13 does not claim RediAI certification.
- M13 does not create working-note readiness.

## Suggested PR title

`M13 — Audio-Derived Baseline Planning Gate`

## Suggested commit message

`docs(m13): plan audio-derived baseline sprint`

## Stop point

Stop after implementation, local verification, PR opened, PR-head CI green. Do not merge without owner approval.

## Closeout (after owner approval only)

- `M13_summary.md`, `M13_audit.md`
- Mark M13 closed in Ultimate Truth
- Seed M14 stub
- Do not begin M14 implementation during M13 closeout
