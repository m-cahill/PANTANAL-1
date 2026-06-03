# M09 Plan — Working-Note Draft Planning / Public Narrative Decision Gate

**Status:** In progress (branch `m09-working-note-draft-decision-gate`)

**Objective:** Decide whether PANTANAL-1 should expand the M08 working-note outline into a full draft, pivot to a real inference baseline, or archive as a governed Kaggle template — via decision-gate docs, readiness checklist, and next-direction recommendation. No full draft, no inference, no new Kaggle submissions.

**Definition of done (repo-side):**

- `docs/working_note/draft_decision_gate.md` — structured gate with evidence, blockers, M10 options, M10B-first recommendation (not irreversible decision).
- `docs/working_note/draft_readiness_checklist.md` — sectioned checklist with honest partial/missing statuses.
- `docs/analysis/M09_next_direction_recommendation.md` — primary M10B, secondary M10A, tertiary M10C with non-claims.
- `tests/test_m09_decision_gate.py` — stdlib-only doc/governance tests (12 checks).
- `docs/milestones/M09/M09_plan.md` expanded; `M09_toolcalls.md` maintained.
- `docs/pantanal-1.md` — M09 in artifact table and §7 ledger (`in progress`); narrow M09 claim; M09 non-claims.
- Optional minimal `docs/working_note/README.md` pointer to M09 docs.
- PR-head CI green; no competition data, weights, notebook changes, or ML dependencies.

**Closeout (owner approval gate):** M09 summary, audit, merge, seed M10 — not part of implementation commit.

---

## Context

- M00–M08 closed: governed zero-baseline Kaggle path (public score **0.500**), post-competition analysis (M05), audit/security gates (M06–M07), working-note outline + evidence map (M08).
- M08 delivered outline only; working-note and CLEF readiness remain not proven.
- M09 is a **decision gate and planning milestone** — not implementation of M10 work.

---

## In scope

1. Expand this plan from stub to full plan.
2. Maintain `M09_toolcalls.md` as work proceeds.
3. Add decision gate, readiness checklist, next-direction recommendation.
4. Add `tests/test_m09_decision_gate.py`.
5. Update `docs/pantanal-1.md` (M09 in progress; artifact links; M09 claim/non-claims).
6. Minimal README pointer to M09 docs if useful.
7. Preserve green CI; no CI workflow changes required.

---

## Out of scope

- Full working-note draft or CLEF submission readiness.
- Model inference, training, audio feature extraction, heavy ML dependencies.
- Kaggle notebook behavior changes or new submissions.
- Leaderboard, competitive-quality, or RediAI certification claims.
- SBOM/provenance/action-pinning (M10E option only).
- M09 summary/audit/merge closeout until owner approval.

---

## Locked owner decisions (2026-06-03)

| Topic | Decision |
|-------|----------|
| M10 recommendation | Primary M10B, secondary M10A, tertiary M10C (prompt default) |
| Decision gate | Mirror M10B/A/C as recommendation; official M10 requires owner approval after M09 closeout |
| Checklist statuses | Prescribed defaults (partial/strong/missing per prompt) |
| README | Minimal pointer to `draft_decision_gate.md` and `draft_readiness_checklist.md` only |
| Ultimate Truth ledger | M09 `in progress` at implementation; `closed` at closeout |
| Commit / push / PR | Yes after local verification; stop before merge |

---

## Deliverables map

| Path | Role |
|------|------|
| `docs/working_note/draft_decision_gate.md` | M09 decision gate |
| `docs/working_note/draft_readiness_checklist.md` | Draft readiness checklist |
| `docs/analysis/M09_next_direction_recommendation.md` | M10 direction recommendation |
| `tests/test_m09_decision_gate.py` | Doc/governance honesty tests |
| `docs/pantanal-1.md` | Ultimate Truth M09 status and claims |

---

## Allowed claim after M09

PANTANAL-1 contains a working-note draft decision gate, readiness checklist, and next-direction recommendation that evaluate whether to draft, pivot to inference, or archive/template the project.

---

## M09 explicit non-claims

- M09 does not create a full working-note draft.
- M09 does not make the project CLEF submission-ready.
- M09 does not implement model inference.
- M09 does not prove model quality.
- M09 does not improve leaderboard score.
- M09 does not claim RediAI certification.

---

## Verification (local)

```bash
pip install -r requirements-dev.txt
ruff check .
ruff format --check .
mypy src/pantanal_1
python -m compileall src tests scripts
pytest -q --cov=src/pantanal_1 --cov-report=term-missing --cov-report=xml
coverage report --fail-under=80
bandit -r src/pantanal_1
pip-audit -r requirements-dev.txt
python scripts/verify_repo_state.py
```
