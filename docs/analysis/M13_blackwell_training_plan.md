# M13 5090 Blackwell Training Plan for M14

## Status

Planning only. Training not started.

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/analysis/M13_audio_baseline_strategy.md`.

**Hardware assumption:** A **5090 Blackwell** GPU is available for private/off-repo training in the ORNITHOS/private lane. PANTANAL-1 remains the public Kaggle-facing packaging and evidence repository.

---

## M14 Training Objectives

1. Produce the **first audio-derived baseline** with non-constant predictions.
2. Generate **validation evidence** (OOF/local metrics, class coverage, failure cases).
3. Export a **CPU-compatible inference artifact** suitable for offline Kaggle packaging.
4. Preserve **public/private boundary** — no raw data, weights, or private code in git without explicit approval.

---

## Training Inputs

Document what data would be needed **without committing it** to PANTANAL-1:

| Input | Location | Notes |
|-------|----------|-------|
| BirdCLEF+ 2026 training audio | Private lane only | CC BY-NC-SA 4.0; not redistributed |
| Training metadata / labels | Private lane | Species labels per segment/window |
| Validation split definition | Private lane + manifest in public repo | Document split policy; no raw audio in git |
| Public pretrained weights | Download in private lane | Record license, version, hash in manifest |
| Test soundscapes (Kaggle) | Kaggle runtime only | Never commit |

M14 must record data provenance in the artifact manifest (see `docs/analysis/M13_artifact_boundary_plan.md`).

---

## Candidate Families (M14 evaluation required)

M13 does **not** lock a single architecture. M14 must evaluate and document each candidate below.

### Baseline A — Pretrained bioacoustic embedding + shallow classifier

| Field | Planning expectation |
|-------|---------------------|
| **Examples** | BirdNET-style, domain-specific bioacoustic embeddings |
| **License / public availability** | M14 must verify license allows competition use and offline inference packaging |
| **Offline Kaggle feasibility** | Embedding model + head exported; all deps vendored or notebook-attached |
| **CPU inference feasibility** | Medium — depends on embedding size; profile load + per-window time |
| **Expected artifact form** | ONNX or torchscript embedding + small head weights (manifest only in public repo until approved) |
| **Training/eval split** | Stratified by species/recording; OOF predictions for calibration check |
| **5090 use** | Fine-tune head; optional light embedding adaptation |
| **Risks** | Large export; license restrictions; domain mismatch |
| **Fallback** | Switch to Baseline B or mel fallback |

### Baseline B — PANNs / CNN14-style audio embeddings

| Field | Planning expectation |
|-------|---------------------|
| **Examples** | PANNs, CNN14 pretrained on AudioSet |
| **License / public availability** | M14 documents upstream license |
| **Offline Kaggle feasibility** | Common export paths; test in dry-run notebook |
| **CPU inference feasibility** | Medium-high — CNN14 smaller than large transformers |
| **Expected artifact form** | Embedding extractor + logistic/linear head |
| **Training/eval split** | Same as A |
| **5090 use** | Head training; optional partial fine-tune |
| **Risks** | Less bioacoustic-specific than BirdNET-style |
| **Fallback** | Mel-spectrogram classifier |

### Baseline C — AudioMAE / AST-style transformer embeddings

| Field | Planning expectation |
|-------|---------------------|
| **Examples** | AudioMAE, AST fine-tuned checkpoints |
| **License / public availability** | M14 verifies HuggingFace/model card license |
| **Offline Kaggle feasibility** | Harder — large deps and model size |
| **CPU inference feasibility** | **High risk** under 90-minute CPU budget |
| **Expected artifact form** | Likely too heavy unless heavily distilled |
| **Training/eval split** | Same as A |
| **5090 use** | Feature extraction + small head |
| **Risks** | Runtime, package size, import failures on Kaggle |
| **Fallback** | Deprioritize if CPU profiling fails |

### Baseline D — EfficientNet-style mel-spectrogram classifier

| Field | Planning expectation |
|-------|---------------------|
| **Examples** | Mel bins + EfficientNet or small custom CNN |
| **License / public availability** | Training code/weights documented by M14 |
| **Offline Kaggle feasibility** | Good if mel + tiny CNN exported |
| **CPU inference feasibility** | Better than large transformers if model small |
| **Expected artifact form** | ONNX mel pipeline + classifier |
| **Training/eval split** | Same as A |
| **5090 use** | Full training on 5090 |
| **Risks** | More training time; may underperform embeddings |
| **Fallback** | Dependency-light mel baseline |

### Baseline E — Fallback: dependency-light mel-spectrogram baseline

| Field | Planning expectation |
|-------|---------------------|
| **Examples** | Log-mel features + sklearn/lightweight model |
| **License / public availability** | Stdlib-friendly or minimal deps |
| **Offline Kaggle feasibility** | **Best** among candidates for packaging simplicity |
| **CPU inference feasibility** | **Best** — target primary CPU path if A/B fail export |
| **Expected artifact form** | Small ONNX or pickled coefficients + feature spec JSON |
| **Training/eval split** | Same as A |
| **5090 use** | Train classifier; feature extraction can be CPU-exported |
| **Risks** | Weaker ranking signal than strong embeddings |
| **Fallback** | Heuristic signal baseline (last resort) |

---

## Experiment Plan

| Phase | Activity | Owner lane |
|-------|----------|------------|
| 1 | Candidate shortlist + license screen | Private (ORNITHOS) |
| 2 | Embedding extraction smoke on sample windows | Private (5090) |
| 3 | Baseline A/B shallow head training | Private (5090) |
| 4 | Baseline D mel-CNN if A/B blocked | Private (5090) |
| 5 | OOF validation — non-constant score check | Private + manifest summary to public |
| 6 | CPU export + dry-run timing estimate | Private → public-safe export plan |
| 7 | Optional calibration (temperature/scaling) | Private — **after** non-constant OOF confirmed |

**Do not include runnable training commands in M13.** M14 runbooks will add commands when training is authorized.

---

## Output Artifacts (M14 → public handoff)

| Artifact | Public repo (default) | Private lane |
|----------|----------------------|--------------|
| Model manifest (JSON/YAML) | Yes | Source copy |
| Training config summary | Yes (no secrets) | Full config |
| Validation report (metrics, coverage) | Yes (summary) | Full logs |
| Export format spec (ONNX/torchscript/sklearn) | Yes | Binary artifact |
| Kaggle inference package candidate | Plan doc only in M13; package in M15 | Build tree |
| Weights / checkpoints | **No** unless owner approves | Yes |
| Raw audio / competition data | **No** | Yes |

Handoff procedures: `docs/analysis/M13_artifact_boundary_plan.md`.

---

## Public Repo Boundary

Only the following enter PANTANAL-1 by default after private training:

- Model cards and manifest summaries
- Hashes and size metadata
- License summaries
- Config summaries (hyperparameters without paths to private data)
- Tiny synthetic fixtures for contract tests
- Inference contract documentation

Weights, raw audio, full training logs, and private ORNITHOS code remain prohibited unless the owner explicitly approves inclusion.

---

## Non-Claims

- M13 does not train any model.
- M13 does not claim any candidate will beat public score **0.500**.
- Named families are evaluation targets for M14, not commitments.
- 5090 availability is an assumption for planning, not evidenced training in M13.
