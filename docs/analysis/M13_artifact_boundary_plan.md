# M13 Artifact Boundary and Provenance Plan

## Purpose

Define what can and cannot enter PANTANAL-1 after private training on the 5090 Blackwell (ORNITHOS/private lane), and specify **concrete ORNITHOS → PANTANAL-1 handoff procedures**.

**Authority:** Subordinate to `docs/pantanal-1.md`, `docs/boundaries.md`, and `docs/manuals/ORNITHOS_OPERATING_MANUAL.md`.

**Ecosystem rule:** ORNITHOS remains private upstream; it must not host Kaggle notebooks, generate `submission.csv`, execute public leaderboard workflow, or claim final BirdCLEF submission readiness. PANTANAL-1 owns public Kaggle/BirdCLEF packaging and submission evidence.

---

## Prohibited in PANTANAL-1 (default)

| Category | Examples | Enforcement |
|----------|----------|-------------|
| Raw audio | `.wav`, `.ogg`, `.flac`, soundscape trees | `.gitignore`, `verify_repo_state.py` |
| Kaggle competition data | `train_audio/`, `test_soundscapes/`, competition CSVs | Data policy |
| Model weights / checkpoints | `.pt`, `.pth`, `.onnx` (unless owner-approved) | Model policy |
| Private ORNITHOS code | Imports, copied modules, private configs | Boundary rules |
| Generated runs | `submission.csv`, wandb/mlruns, run logs | `.gitignore` |
| Credentials | `.kaggle/`, `kaggle.json`, `.env` | Secrets policy |
| Large artifacts | Multi-GB bundles, full training dumps | Owner gate + size review |

---

## Potentially Allowed in PANTANAL-1

| Category | Condition |
|----------|-----------|
| Model cards | Public-safe summary; no private paths |
| Manifests | JSON/YAML per schema below |
| Hashes | SHA-256 of approved artifacts |
| License summaries | SPDX or plain-text summary with source URL |
| Config summaries | Hyperparameters, architecture name — no secret paths |
| Tiny synthetic fixtures | Contract tests only; not competition audio |
| Inference contract docs | Input/output shapes, column order, runtime budget |

**Weights:** prohibited unless owner explicitly approves inclusion with documented license, size, and Kaggle packaging plan.

---

## Required Metadata (all handoffs)

Every public-safe artifact reference in PANTANAL-1 must include:

| Field | Description |
|-------|-------------|
| `source` | ORNITHOS private lane / public model hub / synthetic |
| `license` | SPDX or documented competition-compliant license |
| `hash` | SHA-256 of binary if binary is approved for inclusion |
| `size_bytes` | File size if binary included |
| `creation_date` | ISO-8601 UTC |
| `training_eval_context` | Split, metric summary, non-claim language |
| `public_private_status` | `public-safe-doc-only` or `owner-approved-binary` |

---

## Manifest Shape (ORNITHOS → PANTANAL-1)

Recommended manifest file: `docs/models/<model_id>_manifest.json` (or `.yaml`) — **documentation manifest only in M13**; file created in M14+ when training exists.

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

M13 defines the schema; M14 populates fields after training. `status: planning-only` until owner approves promotion.

---

## Hash Verification Expectations

Before any owner-approved binary enters PANTANAL-1:

1. Compute **SHA-256** in the private lane at export time.
2. Record hash in the manifest committed to PANTANAL-1.
3. On ingest, recompute hash and assert match (`scripts/` or CI check in a future milestone).
4. If hash mismatch, **reject** ingest; do not update Ultimate Truth claims.

Documentation-only manifests (M13) may use `null` hashes with `status: planning-only`.

---

## ORNITHOS → PANTANAL-1 Handoff Procedure

### Step 1 — Private lane completion checklist (ORNITHOS)

- [ ] Training used only private-stored competition data (not copied to public repo)
- [ ] Export artifact produced with documented format
- [ ] OOF or validation report shows **non-constant** predictions (when training exists)
- [ ] License screen completed for backbone and head
- [ ] CPU inference dry-run timing recorded (estimate for 90-minute budget)
- [ ] No credentials, raw audio, or competition CSVs in export bundle

### Step 2 — Public-safe package assembly

- [ ] Strip private absolute paths from configs
- [ ] Generate manifest JSON per schema above
- [ ] Write model card (architecture, limits, non-claims)
- [ ] List prohibited residues (no ORNITHOS code snippets in copy-paste)

### Step 3 — PANTANAL-1 ingest review

- [ ] Run `python scripts/verify_repo_state.py`
- [ ] Confirm `.gitignore` still blocks weights unless exception filed
- [ ] Update `docs/pantanal-1.md` only with claim-safe language
- [ ] Add governance tests if new doc paths added

### Step 4 — Owner approval gate

- [ ] Owner approves manifest + any binary inclusion
- [ ] Owner approves Ultimate Truth claim updates
- [ ] No automatic promotion from planning-only to production-ready

---

## Validation Checklist Before Anything Enters PANTANAL-1

| Check | Pass criterion |
|-------|----------------|
| Data policy | No competition audio or redistribution |
| Model policy | No weights unless approved |
| Secrets policy | No keys or tokens |
| Boundary | No ORNITHOS code import |
| License | Documented and competition-compliant |
| Size | Under agreed limit or attached via Kaggle dataset, not git |
| Claims | No score improvement without public score > 0.500 observed |
| Provenance | Manifest complete per Required Metadata |
| Kaggle | Packaging plan acknowledges CPU ≤ 90 min, internet off |

---

## Allowed vs Prohibited (quick reference)

| Allowed (default) | Prohibited (default) |
|-------------------|---------------------|
| Manifest JSON/YAML | Raw audio |
| Model card markdown | Kaggle competition data |
| Hash + size metadata | Private ORNITHOS code |
| License summary | Generated `submission.csv` in git |
| Config summary | Credentials |
| Inference contract doc | Full training logs |
| Tiny synthetic fixture | Unapproved large weights |

---

## Non-Claims

- M13 does not ingest any trained artifact.
- Manifest schema is a **planning contract** for M14.
- Handoff procedures do not imply ORNITHOS code may be copied into PANTANAL-1.
