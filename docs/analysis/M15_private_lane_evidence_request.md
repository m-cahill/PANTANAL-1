# M15 Private-Lane Evidence Request

**Purpose:** Exact checklist of files requested from the ORNITHOS/5090 Blackwell private training lane for a future M15A evidence ingest milestone.

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/analysis/M14_evidence_contract.md`.

**Status:** Request packet only — no evidence has been ingested.

---

## Required Evidence Files

The private lane must produce the following public-safe artifacts:

| # | Artifact | Format | Reference | Required for |
|---|----------|--------|-----------|--------------|
| 1 | Model manifest | JSON | `docs/models/M14_MODEL_MANIFEST_SCHEMA.md` | Any ingest |
| 2 | Model card | Markdown | `docs/models/M14_model_card_template.md` | Any ingest |
| 3 | Validation summary | JSON | `schemas/m14_validation_summary.schema.json` | Any ingest |
| 4 | Non-constant prediction summary | JSON or Markdown | M13 evaluation plan | G1 claim |
| 5 | CPU timing summary | JSON or Markdown | M13 evaluation plan | G2 claim |
| 6 | License/provenance summary | Markdown or JSON | M14 evidence contract | Any ingest |

---

## Validation Summary Required Fields

Per `schemas/m14_validation_summary.schema.json`:

- `schema_version` — e.g., `"m14-1"`
- `model_id` — stable model identifier
- `status` — one of: `planning_only`, `private_trained_summary`, `owner_approved_binary`
- `created_at` — ISO-8601 UTC timestamp
- `prediction_summary` — public-safe aggregate description
- `class_coverage` — species/class coverage summary object
- `metrics` — metric names to values (null permitted if training not complete)
- `claim_gate` — target gate label (G0–G5)
- `non_claims` — array of explicit non-claim strings (minimum 1)
- `non_constant_predictions_verified` — boolean (true only when non-constant check passed)

---

## Public-Safe Constraints

All evidence files **must** comply with the following constraints:

### Explicitly Prohibited

| Prohibited Content | Reason |
|--------------------|--------|
| Raw audio files (`.wav`, `.ogg`, `.flac`, `.mp3`, etc.) | Data policy; CC BY-NC-SA non-redistribution |
| Kaggle competition CSVs (`train.csv`, `test.csv`, `sample_submission.csv`) | Data policy |
| Model binaries (`.pt`, `.onnx`, `.h5`, `.pkl`, etc.) | Model policy unless owner-approved |
| Private ORNITHOS source code | Boundary rules |
| Generated `submission.csv` | Generated runs policy |
| Credentials (`.env`, `kaggle.json`, API keys) | Secrets policy |
| Private file paths or internal hostnames | Security; reveals infrastructure |
| Raw predictions over private data (if leakage risk) | May expose labels or competition rows |
| Unverifiable public score claims | Claim ladder; require observed Kaggle score |

### Required Public-Safe Practices

- Aggregate metrics only (no per-sample predictions unless anonymized)
- Redact any internal paths, hostnames, or credentials
- Mark synthetic examples explicitly with `synthetic: true`
- Include explicit `non_claims` array in validation summary
- Use allowed `status` values only

---

## Claim Ladder Reference

Per M13/M14 evaluation plan:

| Gate | Evidence Required | What It Proves |
|------|-------------------|----------------|
| G0 | Planning/evidence contract only | Contract readiness |
| G1 | Non-constant OOF/local evidence | Model produces varied predictions |
| G2 | CPU export dry-run or timing estimate | Kaggle runtime feasibility |
| G3 | Kaggle commit success + `submission.csv` | Submission path works |
| G4 | Observed public score > 0.500 | Score improvement over baseline |
| G5 | Working-note contribution evidence | Publication readiness |

---

## Validation Procedure

Before PANTANAL-1 can accept the evidence bundle:

1. Owner reviews bundle against this checklist
2. Run `python scripts/validate_m14_evidence.py <path-to-validation-summary.json>`
3. Run `python scripts/verify_repo_state.py` to confirm no prohibited artifacts
4. Open PANTANAL-1 PR with docs/summaries only (no binaries unless separately approved)
5. Update `docs/pantanal-1.md` with claim-safe language only

---

## Delivery Instructions for Private Lane

1. Complete private training runbook phases 1–7 per `docs/analysis/M14_private_training_runbook.md`
2. Generate all artifacts in the table above
3. Verify no prohibited content is included
4. Package as a single directory or archive
5. Notify PANTANAL-1 owner that evidence is ready for M15A ingest

---

## Non-Claims

This request packet:

- Does not ingest real private-lane evidence
- Does not fabricate metrics or validation results
- Does not claim G1/G2/G3/G4 evidence exists
- Does not prove model quality or score improvement
