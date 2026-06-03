# M15 Private-Lane Evidence Packet Template

**Purpose:** Copy/paste template for the ORNITHOS/5090 Blackwell private training lane to fill out when submitting evidence for M15A ingest.

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/analysis/M14_evidence_contract.md`.

**Status:** Template only — placeholders only, not real evidence.

---

## Instructions

1. Complete all sections below
2. Replace all `[PLACEHOLDER]` values with actual data
3. Verify no prohibited content is included
4. Package all files listed in the checklist
5. Submit to PANTANAL-1 owner for M15A ingest review

---

## Evidence Bundle Checklist

| # | File | Included | Notes |
|---|------|----------|-------|
| 1 | `m15a_[MODEL_ID]_manifest.json` | [ ] | |
| 2 | `m15a_[MODEL_ID]_model_card.md` | [ ] | |
| 3 | `M15A_validation_summary.json` | [ ] | |
| 4 | `M15A_nonconstant_prediction_summary.md` | [ ] | Required for G1 |
| 5 | `M15A_cpu_timing_summary.md` | [ ] | Required for G2 |
| 6 | `M15A_license_provenance_summary.md` | [ ] | |

---

## 1. Model Manifest (JSON)

Save as `m15a_[MODEL_ID]_manifest.json`:

```json
{
  "model_id": "[PLACEHOLDER: stable model identifier, e.g., pantanal1_embedding_head_v1]",
  "model_name": "[PLACEHOLDER: human-readable name]",
  "version": "[PLACEHOLDER: version string, e.g., 1.0.0]",
  "created_at": "[PLACEHOLDER: ISO-8601 UTC timestamp, e.g., 2026-06-03T12:00:00Z]",
  "status": "[PLACEHOLDER: planning_only | private_trained_summary | owner_approved_binary]",
  "architecture": {
    "type": "[PLACEHOLDER: e.g., embedding_head, mel_cnn, etc.]",
    "base_model": "[PLACEHOLDER: e.g., BirdNET, PANNs, custom]",
    "num_classes": 234,
    "input_format": "[PLACEHOLDER: e.g., 5-second audio windows]"
  },
  "training": {
    "dataset": "[PLACEHOLDER: public-safe description only]",
    "framework": "[PLACEHOLDER: e.g., PyTorch 2.x]",
    "hardware": "[PLACEHOLDER: e.g., NVIDIA RTX 5090]",
    "training_time": "[PLACEHOLDER: e.g., 4 hours]"
  },
  "inference": {
    "cpu_compatible": "[PLACEHOLDER: true | false]",
    "estimated_runtime_90min_budget": "[PLACEHOLDER: e.g., 45 minutes estimated]"
  },
  "provenance": {
    "source_repo": "[PLACEHOLDER: ORNITHOS or other private repo name]",
    "license": "[PLACEHOLDER: e.g., Apache 2.0, proprietary]",
    "data_license": "[PLACEHOLDER: CC BY-NC-SA 4.0 for BirdCLEF data]"
  },
  "non_claims": [
    "[PLACEHOLDER: list explicit non-claims]"
  ]
}
```

---

## 2. Model Card (Markdown)

Save as `m15a_[MODEL_ID]_model_card.md`:

```markdown
# Model Card: [PLACEHOLDER: Model Name]

## Model Details

- **Model ID:** [PLACEHOLDER]
- **Version:** [PLACEHOLDER]
- **Created:** [PLACEHOLDER: ISO-8601 UTC]
- **Status:** [PLACEHOLDER: planning_only | private_trained_summary | owner_approved_binary]

## Intended Use

[PLACEHOLDER: Describe intended use case — BirdCLEF+ 2026 species classification from audio]

## Architecture

[PLACEHOLDER: Describe model architecture without revealing proprietary details]

## Training Data

[PLACEHOLDER: Public-safe description only — no raw data paths, no sample counts that reveal competition splits]

## Evaluation

[PLACEHOLDER: Public-safe aggregate metrics only]

## Limitations

[PLACEHOLDER: Document known limitations]

## Ethical Considerations

[PLACEHOLDER: Any relevant ethical notes]

## Non-Claims

- [PLACEHOLDER: List what this model does NOT prove]
- Does not prove competitive performance
- Does not prove private leaderboard ranking
- [Add more as applicable]

## Boundary Compliance

- No raw audio committed
- No Kaggle competition CSVs committed
- No private ORNITHOS code committed
- No secrets or credentials committed
```

---

## 3. Validation Summary (JSON)

Save as `M15A_validation_summary.json`:

```json
{
  "schema_version": "m14-1",
  "model_id": "[PLACEHOLDER: must match manifest model_id]",
  "status": "[PLACEHOLDER: private_trained_summary]",
  "created_at": "[PLACEHOLDER: ISO-8601 UTC timestamp]",
  "prediction_summary": "[PLACEHOLDER: public-safe aggregate description of predictions, e.g., 'Predictions span 234 classes with non-uniform distribution']",
  "class_coverage": {
    "total_classes": 234,
    "classes_with_nonzero_predictions": "[PLACEHOLDER: integer]",
    "coverage_percentage": "[PLACEHOLDER: float, e.g., 0.95]"
  },
  "metrics": {
    "oof_macro_auroc": "[PLACEHOLDER: float or null]",
    "oof_lrap": "[PLACEHOLDER: float or null]",
    "validation_loss": "[PLACEHOLDER: float or null]"
  },
  "claim_gate": "[PLACEHOLDER: G1 | G2 | G3 | G4]",
  "non_claims": [
    "Does not prove competitive performance",
    "Does not prove private leaderboard ranking",
    "Does not prove score improvement over baseline unless public score > 0.500 observed",
    "[PLACEHOLDER: add more as applicable]"
  ],
  "non_constant_predictions_verified": "[PLACEHOLDER: true | false]"
}
```

---

## 4. Non-Constant Prediction Summary (Markdown)

Save as `M15A_nonconstant_prediction_summary.md`:

```markdown
# Non-Constant Prediction Summary

**Model ID:** [PLACEHOLDER]
**Verification Date:** [PLACEHOLDER: ISO-8601 UTC]

## Verification Method

[PLACEHOLDER: Describe how non-constant predictions were verified, e.g., "Computed standard deviation across OOF predictions for each class"]

## Results

- **Total samples checked:** [PLACEHOLDER]
- **Classes with non-constant predictions:** [PLACEHOLDER] / 234
- **Mean prediction variance:** [PLACEHOLDER]
- **Conclusion:** [PLACEHOLDER: Predictions are non-constant / constant]

## Evidence

[PLACEHOLDER: Public-safe summary of verification output — no raw predictions]

## Non-Claims

- This summary does not prove model quality
- This summary does not prove score improvement
```

---

## 5. CPU Timing Summary (Markdown)

Save as `M15A_cpu_timing_summary.md`:

```markdown
# CPU Timing Summary

**Model ID:** [PLACEHOLDER]
**Measurement Date:** [PLACEHOLDER: ISO-8601 UTC]

## Test Configuration

- **Hardware:** [PLACEHOLDER: CPU model used for timing]
- **Test data:** [PLACEHOLDER: synthetic or subset description]
- **Inference samples:** [PLACEHOLDER: number of 5-second windows]

## Timing Results

- **Total inference time:** [PLACEHOLDER] minutes
- **Per-sample time:** [PLACEHOLDER] seconds
- **Estimated full-test runtime:** [PLACEHOLDER] minutes

## Budget Assessment

- **Kaggle CPU limit:** 90 minutes
- **Estimated runtime:** [PLACEHOLDER] minutes
- **Within budget:** [PLACEHOLDER: Yes | No | Marginal]

## Non-Claims

- Timing may vary on Kaggle hardware
- Does not guarantee Kaggle submission success
```

---

## 6. License/Provenance Summary (Markdown)

Save as `M15A_license_provenance_summary.md`:

```markdown
# License and Provenance Summary

**Model ID:** [PLACEHOLDER]
**Created:** [PLACEHOLDER: ISO-8601 UTC]

## Code Provenance

- **Training code source:** [PLACEHOLDER: ORNITHOS private repository]
- **Code license:** [PLACEHOLDER: e.g., proprietary, Apache 2.0]

## Data Provenance

- **Training data:** BirdCLEF+ 2026 competition data
- **Data license:** CC BY-NC-SA 4.0
- **Data redistribution:** Not permitted in PANTANAL-1

## Model Weights Provenance

- **Weights generated by:** [PLACEHOLDER: training process description]
- **Weights license:** [PLACEHOLDER]
- **Weights committed to PANTANAL-1:** [PLACEHOLDER: No, unless owner-approved]

## Third-Party Components

[PLACEHOLDER: List any third-party models, libraries, or pretrained weights used]

## Compliance Checklist

- [ ] No raw audio committed
- [ ] No Kaggle competition CSVs committed
- [ ] No private ORNITHOS code committed
- [ ] No credentials or secrets committed
- [ ] License terms respected
```

---

## Prohibited Content Checklist

Before submitting, verify **NONE** of the following are included:

- [ ] Raw audio files (`.wav`, `.ogg`, `.flac`, `.mp3`)
- [ ] Kaggle competition CSVs
- [ ] Model binaries (`.pt`, `.onnx`, `.h5`, `.pkl`) — unless owner-approved
- [ ] Private ORNITHOS source code
- [ ] Generated `submission.csv`
- [ ] Credentials, API keys, or `.env` files
- [ ] Private file paths or internal hostnames
- [ ] Raw per-sample predictions (if leakage risk)

---

## Submission

When complete:

1. Verify all placeholders are filled
2. Verify prohibited content checklist is clear
3. Package files into a single directory
4. Notify PANTANAL-1 owner that evidence bundle is ready
5. Await M15A ingest decision per `docs/analysis/M15_ingest_decision_gate.md`
