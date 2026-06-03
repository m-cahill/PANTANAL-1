# M11 Plan — Kaggle Non-Zero Baseline Evidence Probe

**Status:** Stub only. Awaiting owner-approved plan.

---

## Purpose

Optionally run or prepare the M10 deterministic non-zero baseline path on Kaggle and record evidence without overclaiming model quality.

---

## Context

M10 added a deterministic uniform-epsilon non-zero baseline generator. It did not run Kaggle, submit a new score, or prove model quality. M11 should determine whether to gather Kaggle evidence for the M10 path or pivot to audio-dependency planning.

---

## Expected focus

- Decide whether an owner manual Kaggle run is desired.
- If run, record exact evidence: output path, row count, column count, runtime, public score if shown.
- Preserve data/weights/secrets guardrails.
- Do not commit competition data, model weights, real `sample_submission.csv`, real `taxonomy.csv`, real `submission.csv`, or generated runs.
- Do not claim score improvement, model quality, trained inference, or audio understanding without direct evidence.
