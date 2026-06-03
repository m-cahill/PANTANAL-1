# M14 Model Manifest Schema

Human-readable schema for future audio-derived baseline model manifests ingested from the private ORNITHOS/5090 Blackwell lane.

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/analysis/M13_artifact_boundary_plan.md`.

**M14 status:** Schema contract only. No trained manifest is committed in M14.

---

## Purpose

Define required fields and status values so private-lane training can produce a public-safe manifest without exposing raw audio, competition data, private code, or unapproved binaries.

---

## Required top-level fields

| Field | Type | Description |
|-------|------|-------------|
| `manifest_version` | string | Schema version (e.g. `"1"`) |
| `model_id` | string | Stable identifier (e.g. `m14-baseline-a-v0`) |
| `display_name` | string | Human-readable name |
| `status` | enum | See status values below |
| `source` | object | Training lane and backbone provenance |
| `artifacts` | array | Export artifacts (may be empty or null paths in planning) |
| `training_eval_context` | object | Validation type, metrics summary, non-constant flag |
| `kaggle_packaging` | object | CPU feasibility and internet-at-score-time |
| `provenance` | object | Creation and handoff metadata |

---

## Status values

| Status | Meaning |
|--------|---------|
| `planning-only` | Documentation contract; no trained artifact |
| `private-trained-summary` | Training completed in private lane; public-safe summary only (no binary in git unless approved) |
| `owner-approved-binary` | Owner approved inclusion of a binary artifact in public repo or Kaggle dataset |

Promotion from `planning-only` to `private-trained-summary` or `owner-approved-binary` requires owner approval and completed handoff checklist (`docs/analysis/M14_private_training_runbook.md`).

---

## `source` object

Required nested fields (denoted `source.training_lane`, `source.pretrained_backbone`, `source.backbone_license`):

| Field | Required | Description |
|-------|----------|-------------|
| `training_lane` | yes | e.g. `ORNITHOS-private` |
| `pretrained_backbone` | yes | Backbone name/version or `TBD` in planning |
| `backbone_license` | yes | SPDX or documented license; `TBD` in planning |

---

## `artifacts[]` entries

| Field | Description |
|-------|-------------|
| `role` | e.g. `inference_export` |
| `format` | e.g. `onnx`, `torchscript` |
| `path_in_public_repo` | null until owner-approved |
| `sha256` | null in planning-only; required when binary approved |
| `size_bytes` | null in planning-only |
| `public_private_status` | e.g. `owner-approved-binary-required` |

---

## `training_eval_context` object

| Field | Description |
|-------|-------------|
| `validation_type` | e.g. `OOF`, `holdout` |
| `metrics_summary` | Public-safe text or null in planning |
| `non_constant_predictions_verified` | boolean; must be `true` before G1+ claims |

---

## `kaggle_packaging` object

| Field | Description |
|-------|-------------|
| `cpu_feasibility` | e.g. `TBD`, `estimated_ok`, `at_risk` |
| `internet_required_at_score_time` | must be `false` for BirdCLEF commit mode |

---

## `provenance` object

| Field | Description |
|-------|-------------|
| `created_at` | ISO-8601 UTC |
| `created_by` | e.g. `private-lane` |
| `handoff_reviewed_by` | reviewer id or `TBD` |

---

## Reference JSON example (planning-only)

Based on M13 artifact boundary manifest. Fields may use `null` or `TBD` while status is `planning-only`.

```json
{
  "manifest_version": "1",
  "model_id": "m14-baseline-a-v0",
  "display_name": "Bioacoustic embedding + shallow head (planning placeholder)",
  "status": "planning-only",
  "source": {
    "training_lane": "ORNITHOS-private",
    "pretrained_backbone": "TBD-M14",
    "backbone_license": "TBD-M14"
  },
  "artifacts": [
    {
      "role": "inference_export",
      "format": "onnx",
      "path_in_public_repo": null,
      "sha256": null,
      "size_bytes": null,
      "public_private_status": "owner-approved-binary-required"
    }
  ],
  "training_eval_context": {
    "validation_type": "OOF",
    "metrics_summary": "TBD-M14",
    "non_constant_predictions_verified": false
  },
  "kaggle_packaging": {
    "cpu_feasibility": "TBD-M14",
    "internet_required_at_score_time": false
  },
  "provenance": {
    "created_at": "TBD",
    "created_by": "private-lane",
    "handoff_reviewed_by": "TBD"
  }
}
```

---

## Non-claims

- This schema does not imply a trained model exists in PANTANAL-1.
- Manifest JSON in git is not required in M14; schema is guidance for future ingest.
- Hash verification and binary ingest are future milestone steps when owner approves.
