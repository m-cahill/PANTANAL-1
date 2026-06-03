# Model Card Template — Audio-Derived Baseline (M14)

Copy this template when creating a public-safe model card after private-lane training. Remove instructional comments before commit.

**Status:** Template only in M14. No populated model card is required until training exists.

---

## Model identification

| Field | Value |
|-------|-------|
| **Model ID** | `<!-- e.g. m14-baseline-a-v0 -->` |
| **Display name** | `<!-- human-readable name -->` |
| **Manifest status** | `<!-- planning-only | private-trained-summary | owner-approved-binary -->` |
| **Manifest version** | `<!-- e.g. 1 -->` |

---

## Intended use

- **Primary use:** BirdCLEF+ 2026 multi-species acoustic classification (234 species, 5-second windows).
- **Intended environment:** Private training on 5090 Blackwell; public Kaggle CPU notebook packaging (M15+).
- **Out of scope:** General-purpose speech/music; non-competition redistribution of training audio.

---

## Architecture family

| Field | Value |
|-------|-------|
| **Primary candidate** | Public pretrained bioacoustic/audio embedding + shallow classifier head |
| **Fallback candidate** | Dependency-light mel-spectrogram baseline |
| **Backbone** | `<!-- name, version, source URL -->` |
| **Head** | `<!-- e.g. linear / logistic on embeddings -->` |

---

## Training data boundary

- Training used BirdCLEF+ 2026 data **only in the private lane** (not committed to PANTANAL-1).
- Competition data is CC BY-NC-SA 4.0 — not redistributed from this repo.
- Validation split policy: `<!-- document split; no raw audio paths in public card -->`

---

## Validation summary

| Field | Value |
|-------|-------|
| **Validation type** | `<!-- OOF / holdout -->` |
| **Non-constant predictions verified** | `<!-- true/false -->` |
| **Metrics (public-safe)** | `<!-- macro ROC-AUC, per-class notes; null if planning-only -->` |
| **Validation summary JSON** | `<!-- path to public-safe summary if ingested -->` |

Link to `schemas/m14_validation_summary.schema.json` for structured summaries.

---

## Non-constant prediction evidence

- [ ] Histogram or variance summary shows per-class or per-row score variation
- [ ] Not identical to all-zero or uniform-ε baselines (M04/M11 scored 0.500)
- [ ] Evidence file: `<!-- non_constant_prediction_summary.json path if provided -->`

---

## CPU packaging risks

| Risk | Mitigation |
|------|------------|
| Model load time | `<!-- seconds; target within 90-min budget -->` |
| Per-window inference | `<!-- ms per 5s window -->` |
| Dependency weight | `<!-- vendored deps / notebook attachment plan -->` |
| Internet at score time | Must be **disabled** (BirdCLEF rules) |

---

## License and provenance

| Component | License | Source |
|-----------|---------|--------|
| Backbone | `<!-- SPDX -->` | `<!-- URL -->` |
| Head / training code | `<!-- private lane; no ORNITHOS code in repo -->` |
| Export artifact | `<!-- if owner-approved binary -->` |

---

## Limitations and non-claims

- Does **not** claim competitive leaderboard performance unless public score > **0.500** is observed and documented.
- Does **not** claim model quality, audio understanding, or working-note readiness without separate milestone evidence.
- Does **not** claim RediAI certification.
- Uniform or constant predictions do **not** constitute improvement (see M12/M11).
- Hidden-test internals are not claimed beyond evidence paste.

---

## No private paths / no raw data rule

**Prohibited in this model card and linked public artifacts:**

- Private absolute filesystem paths
- Raw audio file paths or samples
- Kaggle competition CSVs or `submission.csv` in git
- Private ORNITHOS source code snippets
- Unapproved model weight binaries

**Allowed:** Public-safe summaries, manifest references, hashes (when approved), synthetic fixtures labeled as synthetic.

---

## Cross-references

- `docs/models/M14_MODEL_MANIFEST_SCHEMA.md`
- `docs/analysis/M14_evidence_contract.md`
- `docs/analysis/M14_private_training_runbook.md`
- `docs/analysis/M13_evaluation_plan.md` (claim ladder G0–G5)
