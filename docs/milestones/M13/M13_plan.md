# M13 — Audio-Derived Baseline Planning Gate

**Status:** Stub only. Implementation not started. Owner approval required before any M13 work.

---

## Purpose

Decide the smallest CPU-compatible, license-safe, Kaggle-compatible path for a minimal **audio-derived** baseline (not placeholder all-zero or uniform-ε predictions).

M12 documented that both baselines scored public **0.500** with no score improvement observed. M13 is a **planning gate** only unless the owner explicitly expands scope in an approved plan.

---

## Likely scope (when approved)

- Compare candidate approaches (heuristic audio features, documented public models, etc.)
- Document runtime, dependency, and offline Kaggle constraints
- Define non-claims and evidence requirements for a future implementation milestone
- Preserve data/weights/secrets guardrails

---

## Out of scope until explicitly authorized

- Audio dependency additions
- Public model downloads or model weights in git
- Trained inference implementation
- New Kaggle submissions
- Competition data in git
- Full working-note draft
- Claims of model quality, score improvement, or working-note readiness

---

## Owner gate

Do not begin M13 implementation until the owner approves this plan (or a successor plan) in writing.
