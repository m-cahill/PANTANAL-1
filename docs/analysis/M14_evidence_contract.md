# M14 Evidence Contract

Defines the exact **public-safe evidence bundle** expected from private-lane audio-derived baseline training before PANTANAL-1 may update claims beyond the M14 evidence contract.

**Authority:** Subordinate to `docs/pantanal-1.md`, `docs/analysis/M13_artifact_boundary_plan.md`, and `docs/analysis/M13_evaluation_plan.md`.

**M14 status:** Contract definition and validation tooling only. No trained evidence is ingested in M14.

---

## Purpose

Operationalize M13’s ORNITHOS → PANTANAL-1 handoff into checkable artifacts:

- Machine-validatable validation summary JSON
- Human-readable manifest and model card guidance
- Stdlib validator and CI governance tests
- Synthetic fixtures demonstrating allowed shapes without implying real scores

M14 targets **G1/G2 readiness** (non-constant OOF summary, CPU timing summary) without claiming G1/G2 evidence exists yet.

---

## Required future evidence files (when training completes)

| Artifact | Format | Required when |
|----------|--------|---------------|
| Model manifest | JSON per `docs/models/M14_MODEL_MANIFEST_SCHEMA.md` | Any ingest |
| Model card | Markdown per `docs/models/M14_model_card_template.md` | Any ingest |
| Validation summary | JSON per `schemas/m14_validation_summary.schema.json` | Any ingest |
| Non-constant prediction summary | JSON (aggregates) | Before G1 claims |
| CPU timing summary | JSON (estimates) | Before G2 claims |
| License / provenance summary | Markdown or JSON | Any ingest |

All files must be **public-safe**: no private paths, no raw audio, no competition CSVs, no ORNITHOS code.

---

## Validation summary contract

Validated by `scripts/validate_m14_evidence.py`.

**Required fields:**

- `schema_version`
- `model_id`
- `status` — `planning_only`, `private_trained_summary`, or `owner_approved_binary`
- `created_at` — ISO-8601 UTC
- `prediction_summary` — public-safe aggregate description
- `class_coverage` — species/class coverage summary
- `metrics` — object; metric values may be **null** when training has not occurred
- `claim_gate` — target gate label (e.g. `G0`, `G1`)
- `non_claims` — array of explicit non-claim strings
- `non_constant_predictions_verified` — boolean

**Planning-only rules:**

- `status` must be `planning_only`
- `non_constant_predictions_verified` must be `false`
- Must not contain score improvement, model quality, or training-completion claims in `prediction_summary`, `metrics`, or `non_claims` negation

---

## Explicitly prohibited in evidence bundles

| Prohibited | Reason |
|----------|--------|
| Raw predictions over private data (if leakage risk) | May expose labels or competition rows |
| Audio files (`.wav`, `.ogg`, `.flac`, etc.) | Data policy; CC BY-NC-SA non-redistribution |
| Kaggle competition CSVs | Data policy |
| Model binaries (`.pt`, `.onnx`, etc.) | Model policy unless owner-approved |
| Private ORNITHOS source code | Boundary rules |
| Generated `submission.csv` | Generated runs policy |
| Credentials, `.env`, `kaggle.json` | Secrets policy |
| Unverifiable public score claims | Claim ladder; require observed Kaggle score |

---

## Allowed in M14 repository (this milestone)

| Allowed | Notes |
|---------|-------|
| Schema JSON | `schemas/m14_validation_summary.schema.json` |
| Synthetic fixtures | Clearly labeled; not real BirdCLEF scores |
| Validator script | Stdlib only |
| Governance tests | Phrase and structural checks |
| Markdown contracts | Manifest schema, model card template, runbook |

---

## Fixture policy

| Fixture | Purpose |
|---------|---------|
| `fixtures/m14/validation_summary_planning_only.json` | Valid G0 shape; no training implied |
| `fixtures/m14/validation_summary_nonconstant_example.json` | Synthetic G1-shaped example; **not** real scores |

Synthetic fixtures must include `synthetic: true` or equivalent labeling in `prediction_summary` / `non_claims`.

---

## Ingest workflow (future)

1. Private lane completes runbook phases 1–7.
2. Owner reviews bundle against this contract.
3. Run `python scripts/validate_m14_evidence.py <path>`.
4. Run `python scripts/verify_repo_state.py`.
5. Open PANTANAL-1 PR with docs/summaries only unless binary exception approved.
6. Update `docs/pantanal-1.md` with claim-safe language only.

---

## Non-claims

- M14 does not ingest real training evidence.
- This contract does not guarantee future M15 Kaggle success.
- Satisfying the schema does not prove model quality or score improvement.
