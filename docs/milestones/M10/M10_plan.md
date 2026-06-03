# M10 Plan — Real Inference Baseline Spike

**Status:** Stub only. Awaiting owner-approved plan.

---

## Purpose

Implement the smallest possible real, non-zero inference baseline path for PANTANAL-1, if the owner approves research momentum.

---

## Context

M09 recommended M10B as the primary next direction because M08/M09 established narrative scaffolding, while the project still has no real model inference. PANTANAL-1 currently has a scored zero-baseline public score **0.500**, which proves pipeline acceptance, not predictive model quality.

---

## Expected focus

- Define the minimal inference path before implementation.
- Prefer the smallest possible non-zero prediction proof.
- Evaluate audio dependency and Kaggle offline constraints carefully.
- Preserve data/weights/secrets guardrails.
- Do not commit competition data, model weights, real `sample_submission.csv`, real `taxonomy.csv`, real `submission.csv`, or generated runs.
- Do not claim model quality, competitiveness, or score improvement without direct evidence.
- Do not expand into training unless explicitly approved.

---

## Out of scope (until plan is locked)

- Implementation
- Model training or weights in git
- Kaggle notebook behavior changes without explicit scope
- Leaderboard or competitive-quality claims without evidence
- Full working-note draft (M10A alternative)
- Archive/template cleanup (M10C alternative)
