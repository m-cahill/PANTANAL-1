# M07 Plan — Security and Supply-Chain Audit Gate

**Status:** Stub only. Awaiting owner-approved plan.

---

## Purpose

Continue addressing **DEF-001** by adding the next security/supply-chain audit-hardening slice after M06 coverage and mypy gates.

---

## Context

M06 partially addressed **DEF-001** with coverage and mypy CI gates. M07 should add a small security/dependency gate without changing Kaggle notebook behavior or adding model inference.

Security and supply-chain scans, such as Bandit, pip-audit, and SBOM generation, are intentionally deferred to M07+ unless separately authorized.

---

## Expected focus

- Decide exact security slice before implementation.
- Candidate gates may include Bandit and pip-audit.
- Keep scope small and CI-green.
- Preserve data/weights/secrets guardrails.
- Do not add model inference, training, Kaggle submissions, heavy ML dependencies, or new leaderboard claims.
- Do not claim **DEF-001** fully closed unless all agreed exit criteria are met.

---

## Out of scope (until plan is locked)

- Implementation
- Model training or weights in git
- Kaggle notebook behavior changes
- Leaderboard or competitive-quality claims without evidence
