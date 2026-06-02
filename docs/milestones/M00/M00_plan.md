# M00 — Public Repo Bootstrap and Governance Initialization

## Milestone

**M00 — Public Repo Bootstrap and Governance Initialization**

## Purpose

Initialize PANTANAL-1 as the public BirdCLEF+ 2026 Kaggle-facing repository with a minimal, auditable, competition-safe scaffold.

This milestone does **not** implement model training, inference quality, leaderboard submission, Kaggle notebook execution, or working-note claims. It creates the governance, safety, policy, and CI foundation required before competition implementation work begins.

## Authoritative Context

PANTANAL-1 is the public BirdCLEF+ 2026 repository.

Boundary model:

```text
AURORA owns governed acoustic runtime boundaries.
ORNITHOS owns private bioacoustic model development.
PANTANAL-1 owns public Kaggle/BirdCLEF submission packaging.
RediAI owns certification verdicts.
```

PANTANAL-1 must not import private ORNITHOS code, commit private artifacts, commit Kaggle data, commit model weights, commit secrets, or overclaim benchmark/submission readiness.

## Acceptance Criteria

M00 is complete only if:

1. `docs/pantanal-1.md` is initialized as Ultimate Truth.
2. M00 plan and toolcalls files exist.
3. Boundary, Kaggle snapshot, submission contract, and policy docs exist.
4. Minimal package imports successfully.
5. Repo verifier passes.
6. Ruff check passes.
7. Ruff format check passes.
8. Compileall passes.
9. Pytest passes.
10. GitHub Actions CI is green.
11. No Kaggle data, credentials, model weights, generated runs, or `submission.csv` are committed.
12. No claims are made about model quality, leaderboard score, Kaggle notebook execution, or submission readiness.

## Branch and PR

- Branch: `m00-public-repo-bootstrap`
- Commit: `chore(m00): initialize public repo governance scaffold`
- PR title: `M00 — Public Repo Bootstrap and Governance Initialization`

Do not merge unless explicitly authorized.

See full plan in milestone chat / governance record for file list and detailed requirements.
