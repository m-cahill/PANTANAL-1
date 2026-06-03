# M06 Plan — Audit Hardening / Evidence Consolidation

**Status:** Stub only. Awaiting owner-approved plan.

---

## Purpose

Address DEF-001 by adding the next audit-hardening layer for PANTANAL-1 without changing Kaggle notebook behavior or adding model inference.

---

## Context

M05 recommended M06B as the primary next direction because the zero-baseline scored path is proven, the competition deadline has passed, and DEF-001 remains the largest enterprise/audit posture gap.

---

## Expected focus

- Decide exact audit-hardening slice before implementation.
- Candidate gates may include coverage, mypy on `src/`, security scan, or evidence consistency checks.
- Keep scope small and CI-green.
- Preserve data/weights/secrets guardrails.
- Do not add model inference, training, Kaggle submissions, heavy ML dependencies, or new leaderboard claims.
- Do not claim audit hardening completed until implemented and evidenced.

---

## Out of scope (until plan is locked)

- Implementation
- Model training or weights in git
- Kaggle notebook behavior changes
- Leaderboard or competitive-quality claims without evidence
