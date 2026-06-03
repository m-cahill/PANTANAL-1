# M12 Scoring Methodology Audit

**Authority:** Subordinate to `docs/pantanal-1.md`.

**Status:** Analysis document from M12. Does not implement inference or claim score improvement.

---

## Purpose

Explain the observed public-score equality between:

- M03/M04 all-zero baseline: **0.500**
- M10/M11 uniform-ε non-zero baseline: **0.500**

This audit records what local evidence and competition documentation support. It does not infer hidden-label internals beyond observed evidence.

---

## Source materials

| Document | Role |
|----------|------|
| `docs/pantanal-1.md` | Ultimate Truth; M04/M11 scored claims and non-claims |
| `docs/BirdCLEFrules.md` | Metric description; working-note criteria pointer |
| `docs/kaggle/competition_snapshot.md` | Metric summary; submission constraints |
| `docs/kaggle/submission_contract.md` | Row/column semantics; probability columns |
| `docs/kaggle/m04_commit_mode_evidence.md` | All-zero scored evidence (Version 2, 0.500) |
| `docs/kaggle/m11_nonzero_baseline_evidence.md` | Uniform-ε scored evidence (Version 2, 0.500) |
| `docs/kaggle/nonzero_baseline.md` | Uniform-ε method; ranking-separation planning note |

External reference (pointer only; not required to read for this audit): [BirdCLEF ROC-AUC metric](https://www.kaggle.com/code/metric/birdclef-roc-auc) as cited in `docs/BirdCLEFrules.md`.

---

## Metric summary

From local competition documentation:

| Aspect | Summary |
|--------|---------|
| **Metric name** | Macro-averaged ROC-AUC variant |
| **Class handling** | Classes without true positive labels are skipped (per `docs/BirdCLEFrules.md` and `docs/kaggle/competition_snapshot.md`) |
| **Per-class behavior** | ROC-AUC measures how well predicted probabilities **rank** positives above negatives for each class |
| **Submission shape** | One row per 5-second window; 234 species probability columns in `[0, 1]` |
| **Ranking implication** | AUC depends on **order** of predictions relative to labels, not on absolute probability values alone |

ROC-AUC at chance level is **0.5** when a predictor does not systematically rank true positives above true negatives. Constant predictions assign the same score to every row for a given class, so they do not create positive-vs-negative **ranking separation**.

---

## Observed baseline behavior

| Baseline | Public score | Evidence | Interpretation |
|----------|--------------|----------|----------------|
| all-zero | 0.500 | `docs/kaggle/m04_commit_mode_evidence.md` (M03 notebook Version 2) | Pipeline acceptance only; non-informative predictions |
| uniform-ε (0.001) | 0.500 | `docs/kaggle/m11_nonzero_baseline_evidence.md` (M11 notebook Version 2) | Pipeline acceptance only; no ranking separation vs labels |

Both submissions were accepted by Kaggle scoring and returned the same public score. M11 evidence explicitly records **no score improvement** versus the prior all-zero baseline.

---

## Why 0.500 is plausible

The following explanation is **conservative** and limited to documented metric properties plus observed scores.

1. **ROC-AUC is rank-based.** For each class (when evaluated), the metric reflects whether higher predicted probabilities align with positive labels. It is not a simple accuracy or calibration score on absolute values.

2. **Constant predictions do not rank positives above negatives.** If every row receives the same probability for a class (0.0 for all-zero, or 0.001 for uniform-ε), no row is ranked higher than another for that class. Any tie-breaking behavior in the implementation does not constitute meaningful model-driven separation.

3. **A non-zero constant and a zero constant can be equally non-informative.** Changing every probability from 0 to a small uniform ε does not encode species- or segment-specific signal. Both baselines are **placeholder** submissions that satisfy schema and file requirements without acoustic or model-derived discrimination.

4. **Therefore uniform ε may not improve score even though values are non-zero.** M11 observed public score **0.500**, matching M04/M03 all-zero **0.500**. This is consistent with chance-level AUC behavior for non-separating predictions, not with evidence of predictive quality.

**Do not claim:** exact per-class AUC on hidden labels, private leaderboard behavior, or full test-set label distribution. Hidden-test internals were not exposed in owner evidence pastes.

---

## What this proves

- Kaggle submission acceptance for **all-zero** and **uniform-ε** paths.
- PANTANAL-1 can create schema-valid `submission.csv` outputs on Kaggle (interactive and commit/scored modes evidenced in M04 and M11).
- Uniform ε does **not** improve public score over all-zero in **observed** evidence (both **0.500**).

---

## What this does not prove

- Model quality
- Audio understanding
- Trained inference
- Competitive performance
- Private leaderboard performance
- Working-note readiness
- That future audio-derived or model-based submissions will score 0.500
- RediAI certification

---

## Related milestones

| Milestone | Relevance |
|-----------|-----------|
| M04 | First scored all-zero baseline (0.500) |
| M10 | Repo-side uniform-ε generator |
| M11 | Kaggle scored uniform-ε evidence (0.500; no score improvement) |
| M12 | This audit |
| M13 (recommended) | Audio-derived baseline **planning gate** — not implemented in M12 |

---

## Non-claims

M12 scoring audit does not implement model inference, add audio dependencies, or claim score improvement, model quality, or working-note readiness.
