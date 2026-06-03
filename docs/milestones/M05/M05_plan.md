# M05 Plan — Baseline Improvement Planning / Post-Competition Analysis

**Status:** Closed (PR #6; branch `m05-baseline-improvement-planning`)

**Objective:** Analyze the completed zero-baseline Kaggle path (M00–M04), public score evidence, remaining gaps, and recommend the next project direction without implementing inference, training, or new submissions.

**Definition of done (repo-side):**

- `docs/analysis/post_competition_analysis.md` — proven/unproven summary, score interpretation, gaps, ranked recommendation.
- `docs/analysis/next_milestone_decision_matrix.md` — M06A–M06E scored on impact/risk/time/dependency weight/evidence value/alignment; decision-ready recommendation (M06B primary, M06A secondary).
- `docs/analysis/M00_M04_evidence_index.md` — concise milestone evidence index for future sessions.
- `tests/test_m05_post_competition_analysis.py` — stdlib-only tests for analysis docs and honest claim boundaries.
- `docs/milestones/M05/M05_plan.md` expanded from stub; `M05_toolcalls.md` maintained.
- `docs/pantanal-1.md` marks M05 in progress; adds M05 artifact links and allowed claim; preserves M04 non-claims.
- PR-head CI green; no competition data, weights, or submissions in git.

**Closeout (owner approval gate):** M05 summary, audit, merge, seed M06 — not part of this implementation commit.

---

## Context

- M04 closed with Kaggle commit/scored evidence: competition notebook Version 2, **1m 7s**, **1 output file**, public score **0.500** (zero baseline). See `docs/kaggle/m04_commit_mode_evidence.md`.
- BirdCLEF+ 2026 final deadline **2026-06-03 23:59 UTC** has passed.
- **DEF-001** (coverage/mypy/security gates) remains open.
- **DEF-002B** and **DEF-003B** evidenced/narrowed in M04; real inference and competitive quality remain unproven.

---

## In scope

1. Expand this plan from stub to full plan.
2. Maintain `M05_toolcalls.md` as work proceeds.
3. Add `docs/analysis/post_competition_analysis.md`.
4. Add `docs/analysis/next_milestone_decision_matrix.md`.
5. Add `docs/analysis/M00_M04_evidence_index.md`.
6. Add `tests/test_m05_post_competition_analysis.py`.
7. Update `docs/pantanal-1.md` (M05 in progress; M05 claim; M05 non-claims; milestone artifacts table).
8. Preserve green CI.

---

## Out of scope

- Real inference implementation.
- Model training or weights in git.
- Additional Kaggle submission or leaderboard score improvement.
- Heavy ML/audio dependencies or Kaggle API.
- Committing competition data, real `sample_submission.csv`, taxonomy, audio, weights, generated submissions, or runs.
- Working-note draft (M06D evaluated in matrix only).
- Audit hardening implementation (DEF-001 gates).
- M05 summary/audit/merge closeout until owner approval.

---

## Locked owner decisions (2026-06-03)

| Topic | Decision |
|-------|----------|
| Recommendation bias | Primary: **M06B** audit hardening; secondary: **M06A** real inference spike if owner wants ML progress |
| Evidence index | **Yes** — `docs/analysis/M00_M04_evidence_index.md` |
| Working-note seed | Real candidate in matrix; **no** working-note draft in M05 |
| Branch | `m05-baseline-improvement-planning` |

---

## Deliverables map

| Path | Role |
|------|------|
| `docs/analysis/post_competition_analysis.md` | Post-competition narrative and recommendation |
| `docs/analysis/next_milestone_decision_matrix.md` | Scored candidate directions M06A–M06E |
| `docs/analysis/M00_M04_evidence_index.md` | Concise evidence index M00–M04 |
| `tests/test_m05_post_competition_analysis.py` | Doc presence and non-claim discipline |
| `docs/pantanal-1.md` | Ultimate Truth M05 status and claims |

---

## Allowed claim after M05

PANTANAL-1 contains a post-competition analysis and next-milestone decision matrix evaluating the zero-baseline scored path, remaining gaps, and recommended future directions.

## Explicit non-claims (preserve)

- M05 does not implement model inference.
- M05 does not improve leaderboard score.
- M05 does not prove model quality.
- M05 does not add audit hardening gates.
- M05 does not create working-note readiness unless separately scoped.

---

## Verification (local, before commit)

```bash
ruff check .
ruff format --check .
python -m compileall src tests scripts
pytest -q
python scripts/verify_repo_state.py
```

---

## Git / PR

- Branch: `m05-baseline-improvement-planning`
- Commit message: `docs(m05): add post-competition decision analysis`
- PR title: `M05 — Baseline Improvement Planning / Post-Competition Analysis`
- Stop after PR-head CI green; do not merge without owner approval.
