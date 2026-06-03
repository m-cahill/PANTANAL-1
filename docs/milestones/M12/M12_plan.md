# M12 Plan — Scoring Methodology and Working-Note Criteria Audit

**Status:** Stub only. Awaiting owner-approved plan.

---

## Purpose

Audit the official BirdCLEF+ scoring methodology and working-note / CLEF criteria, then recommend whether to pursue an audio-derived baseline, working-note draft, or reusable template next.

---

## Context

M11 recorded that the uniform-ε non-zero baseline scored **0.500**, matching the prior all-zero baseline. This suggests the current non-signal baselines do not create useful ranking separation and do not prove model quality.

---

## Expected focus

- Review official scoring methodology.
- Explain why all-zero and uniform-ε baselines can both score **0.500**.
- Review working-note award / CLEF criteria.
- Determine what evidence is needed for a compelling working note.
- Recommend the smallest next implementation milestone, likely an audio-derived baseline if research momentum is desired.
- Preserve data/weights/secrets guardrails.
- Do not add model inference, training, Kaggle submissions, heavy ML dependencies, or new leaderboard claims in M12.
