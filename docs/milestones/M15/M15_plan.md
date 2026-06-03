# M15 — Private-Lane Evidence Request Packet / Pre-Ingest Readiness Gate

**Status:** Closing (PR #16 closeout)  
**Branch:** `m15-private-lane-evidence-request`  
**Authority:** `docs/pantanal-1.md`

---

## Background

M14 established the public-safe evidence contract (validation schema, fixtures, stdlib validator, manifest guidance, model card template, private runbook). M15A was originally planned as a private-lane evidence ingest milestone.

**Decision:** No owner-supplied public-safe private-lane evidence bundle has been provided yet. M15 pivots from ingest execution to **pre-ingest readiness**.

---

## Objective

Create the smallest possible public-safe packet that tells the ORNITHOS/private 5090 training lane exactly what evidence must be produced for a future M15A ingest milestone.

This is a **pre-ingest readiness milestone**, not a training, inference, Kaggle packaging, or evidence-ingest milestone.

---

## Required Outcome

Produce a concise, implementation-ready evidence request package that the private lane can use to generate the future public-safe bundle required by M14.

---

## Scope

### In Scope

1. `docs/milestones/M15/M15_plan.md` — this document (replace seeded stub)
2. `docs/milestones/M15/M15_toolcalls.md` — record all tool calls and decisions
3. `docs/analysis/M15_private_lane_evidence_request.md` — exact checklist of files requested from private lane with public-safe constraints
4. `docs/analysis/M15_ingest_decision_gate.md` — go/no-go criteria for future M15A
5. `docs/analysis/M15_private_lane_evidence_packet_template.md` — copy/paste template for private lane to fill out
6. `tests/test_m15_private_lane_evidence_request.py` — governance tests
7. `docs/pantanal-1.md` — update with M15 in-progress status, claims, non-claims

### Out of Scope

- Fabricating private-lane evidence
- Creating fake validation metrics as real evidence
- Training or running inference
- Adding dependencies
- Modifying Kaggle notebooks
- Committing weights, raw audio, Kaggle data, private ORNITHOS code, or generated submissions
- Claiming G1/G2/G3/G4 evidence exists

Synthetic examples are allowed only if clearly labeled synthetic and not used as claims.

---

## Deliverables

| Artifact | Purpose |
|----------|---------|
| `docs/analysis/M15_private_lane_evidence_request.md` | Checklist of required files + public-safe constraints |
| `docs/analysis/M15_ingest_decision_gate.md` | Go/no-go criteria for future M15A |
| `docs/analysis/M15_private_lane_evidence_packet_template.md` | Copy/paste template for private lane |
| `tests/test_m15_private_lane_evidence_request.py` | Governance tests |
| Updated `docs/pantanal-1.md` | M15 ledger entry, claims, non-claims |

---

## Evidence Request Summary

The private lane must produce:

1. **Model manifest JSON** — per `docs/models/M14_MODEL_MANIFEST_SCHEMA.md`
2. **Model card markdown** — per `docs/models/M14_model_card_template.md`
3. **Validation summary JSON** — per `schemas/m14_validation_summary.schema.json`
4. **Non-constant prediction summary** — required for G1 claim
5. **CPU timing summary** (if available) — required for G2 claim
6. **License/provenance summary** — required for any ingest

All files must be **public-safe**: no raw audio, no Kaggle competition CSVs, no private ORNITHOS code, no model binaries (unless owner-approved), no generated `submission.csv`, no secrets or private paths.

---

## Decision Gate Summary

Future M15A proceeds only when:

- Validation summary passes `scripts/validate_m14_evidence.py`
- Non-constant evidence exists (for G1)
- CPU timing evidence exists (for G2)
- Public score evidence exists (for G4)

If evidence is incomplete, return to private lane or switch direction.

---

## Verification Commands

```bash
ruff check .
ruff format --check .
mypy src/pantanal_1
python -m compileall src tests scripts
pytest -q --cov=src/pantanal_1 --cov-report=term-missing
coverage report --fail-under=80
bandit -r src/pantanal_1
pip-audit -r requirements-dev.txt
python scripts/verify_repo_state.py
```

---

## PR Stop Point

After implementation:

1. Push branch
2. Open PR
3. Wait for PR-head CI
4. Do not merge
5. Report: branch, PR URL, SHA, CI verdict, files changed, tests added, verification results, claims/non-claims, confirmation no evidence ingested

---

## Closeout Instructions

Do not close or merge until owner approval.

At closeout, create:

- `docs/milestones/M15/M15_run1.md` using `docs/prompts/workflowprompt.md`
- `docs/milestones/M15/M15_summary.md` using `docs/prompts/summaryprompt.md`
- `docs/milestones/M15/M15_audit.md` using `docs/prompts/unifiedmilestoneauditpromptV2.md`

Closeout must include the language: `ensure all documentation is updated as necessary`

After closeout and merge, seed M16 only. Do not begin M16 implementation unless separately authorized.

---

## Non-Claims

- M15 does not ingest real private-lane evidence.
- M15 does not train a model.
- M15 does not implement audio inference.
- M15 does not add audio/ML dependencies.
- M15 does not add model weights.
- M15 does not ingest raw audio or Kaggle competition data.
- M15 does not submit to Kaggle.
- M15 does not improve leaderboard score.
- M15 does not prove model quality.
- M15 does not claim RediAI certification.
- M15 does not create working-note readiness.
