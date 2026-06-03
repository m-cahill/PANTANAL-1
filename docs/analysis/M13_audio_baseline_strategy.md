# M13 Audio-Derived Baseline Strategy

## Status

Planning gate only. No implementation.

**Authority:** Subordinate to `docs/pantanal-1.md`.

---

## Goal

Define the smallest audio-derived prediction path that can produce **ranking signal** beyond constant baselines, while preserving Kaggle submission schema, public/private boundaries, and honest claim discipline.

M12 established that all-zero and uniform-ε baselines both scored public **0.500** because they do not create meaningful ranking separation under macro ROC-AUC. M13 selects a planning path toward non-constant, audio-informed predictions without training or implementing models in this milestone.

---

## Why Constant Baselines Failed

| Baseline | Public score | Problem |
|----------|--------------|---------|
| All-zero (M04) | 0.500 | Every row receives identical class probabilities (0.0) |
| Uniform-ε (M11) | 0.500 | Every row receives identical class probabilities (ε) |

ROC-AUC is **rank-based**: it measures whether predicted probabilities rank true positives above negatives per class. Constant predictions assign the same score to every row for each class, so they do not create positive-vs-negative **ranking separation**. A non-zero constant and a zero constant are equally non-informative for discrimination.

**Implication:** Meaningful score movement requires **per-row or per-class variation** derived from audio content or model outputs, not placeholder constants.

See `docs/analysis/M12_scoring_methodology_audit.md`.

---

## Candidate Approaches

| # | Approach | M13 role | M14/M15 role |
|---|----------|----------|--------------|
| 1 | Spectrogram + lightweight CNN baseline | Document as candidate family | Implement/evaluate in M14 if selected |
| 2 | Public pretrained bioacoustic embedding + shallow classifier | **Primary recommendation** | Train/evaluate on 5090 Blackwell in M14 |
| 3 | Public model inference-only baseline | Document as option | Use if license/offline packaging permits |
| 4 | Simple signal-derived heuristic baseline | Document as exploratory | Fallback if ML path blocked |
| 5 | Ensemble / calibration | Document as **later** only | Not first; after single viable baseline |

### Additional candidates (comparison only — not M13 commitments)

| Candidate | Notes |
|-----------|-------|
| BirdNET-style bioacoustic embeddings | Strong domain fit; check license and export size |
| PANNs / CNN14-style embeddings | General audio; widely used; ONNX/torchscript export paths |
| AudioMAE / AST-style transformers | Higher compute; CPU inference risk |
| EfficientNet-style mel-spectrogram classifier | Train-from-scratch or fine-tune; dependency-lighter fallback |
| YAMNet / OpenL3-style general embeddings | Possible but less bioacoustic-specific |

---

## Recommended Approach

### Primary

**Public pretrained bioacoustic/audio embedding or spectrogram model candidate evaluation**, followed by a small classifier or deterministic scoring head, trained privately on the 5090 Blackwell if license and competition rules allow.

Rationale:

1. Embeddings encode acoustic structure without training a full model from scratch in-repo.
2. A shallow head can produce **per-window, per-class score variation** from real audio features.
3. Pretrained weights stay in the private training lane until a public-safe export is validated.
4. Aligns with M12 conclusion that ranking signal is the minimum scientific step beyond pipeline evidence.

### Fallback

**Dependency-light mel-spectrogram baseline** with a small CPU-exportable classifier (e.g., sklearn-compatible or tiny ONNX).

Rationale:

1. Reduces dependency surface for Kaggle CPU offline execution.
2. Keeps artifact size and load time more predictable under 90-minute CPU budget.
3. Useful if pretrained embedding export or license blocks the primary path.

### Not first

Ensemble, calibration stacks, and multi-model blending — defer until one baseline produces validated non-constant predictions and local/OOF evidence.

---

## Minimal Success Criteria

- Produces **non-constant** per-row or per-class scores (not identical across all rows for all classes).
- Preserves Kaggle submission schema: `row_id`, 234 species columns, probabilities in `[0, 1]`, 5-second row semantics.
- Has documented validation evidence (local/OOF and/or Kaggle public score if submitted in a future milestone).
- Can be packaged for Kaggle CPU inference with internet disabled (see `docs/analysis/M13_kaggle_inference_packaging_plan.md`).
- Does **not** claim quality before scoring or validation evidence exists.

---

## Constraints (binding)

| Constraint | Source |
|------------|--------|
| CPU notebook ≤ 90 minutes | Competition rules; `docs/kaggle/kaggle_submission_bible.md` |
| Internet disabled during scoring | Competition rules |
| Output `/kaggle/working/submission.csv` | Kaggle submission path |
| No competition data in git | `docs/policies/data_policy.md` |
| No model weights in git unless owner-approved | `docs/policies/model_policy.md` |
| No private ORNITHOS code import | `docs/boundaries.md` |
| No audio/ML dependencies added in M13 | M13 scope |

---

## M14 Handoff

M13 recommends M14 — **5090 Blackwell Audio-Derived Baseline Training Sprint** — to execute candidate evaluation, private training, validation reports, and export planning. See `docs/analysis/M13_blackwell_training_plan.md`.

---

## Non-Claims

- No trained model exists yet in PANTANAL-1.
- No score improvement is proven in M13.
- No audio inference is implemented in M13.
- No model quality or audio understanding is claimed.
- Candidate names in this document are planning options, not selected architectures.
- Public score improvement is **not** expected until non-constant predictions are evidenced and scored.
