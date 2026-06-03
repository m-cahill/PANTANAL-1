# M08 Plan — Working-Note Outline / Evidence Narrative Seed

**Status:** In progress (branch `m08-working-note-outline`)

**Objective:** Create a structured working-note outline and evidence map that organize M00–M07 governance, Kaggle, and audit evidence into a public narrative seed — without drafting a full paper, changing notebooks, or claiming model quality.

**Definition of done (repo-side):**

- `docs/working_note/working_note_outline.md` — fixed section skeleton per locked structure; cautious language; 0.500 as pipeline acceptance only.
- `docs/working_note/evidence_map.md` — primary evidence table (multi-row per section where needed) + Secondary Audit Sources; explicit 0.500 non-claim.
- `docs/working_note/README.md` — short pointer; outline-only disclaimer.
- `tests/test_m08_working_note_outline.py` — stdlib-only doc/governance honesty tests (13 checks).
- `docs/milestones/M08/M08_plan.md` expanded; `M08_toolcalls.md` maintained.
- `docs/pantanal-1.md` — M08 in artifact table and §7 ledger; narrow M08 in-progress claim; M08 non-claims; preserve all prior non-claims.
- PR-head CI green; no competition data, weights, submissions, or notebook behavior changes.

**Closeout (owner approval gate):** M08 summary, audit, merge, seed M09 — not part of this implementation commit.

---

## Context

- M00–M07 closed: governed zero-baseline Kaggle path (public score **0.500**), post-competition analysis (M05), audit hardening (M06), security gates (M07).
- M05 matrix selected working-note seed (M06D → M08) over immediate inference spike (M08A).
- Working-note **readiness** remains not proven; M08 delivers outline + evidence map only.

---

## In scope

1. Expand this plan from stub to full plan.
2. Maintain `M08_toolcalls.md` as work proceeds.
3. Add `docs/working_note/` outline, evidence map, README.
4. Add `tests/test_m08_working_note_outline.py`.
5. Update `docs/pantanal-1.md` (M08 in progress; artifact links; M08 claim/non-claims).
6. Preserve green CI; no CI workflow changes required.

---

## Out of scope

- Full working-note draft or CLEF submission readiness.
- Model inference, training, audio feature extraction, heavy ML dependencies.
- Kaggle notebook behavior changes or new submissions.
- Leaderboard, competitive-quality, or RediAI certification claims.
- SBOM/provenance/action-pinning.
- M08 summary/audit/merge closeout until owner approval.

---

## Locked owner decisions (2026-06-03)

| Topic | Decision |
|-------|----------|
| Ultimate Truth ledger | Add M08 to artifact table and §7; status `in progress` until closeout |
| README | Create short pointer under `docs/working_note/` |
| Evidence map depth | Multiple rows per section when multiple milestones contribute |
| Audits | Secondary Audit Sources section; summaries/primary docs remain core |
| Outline structure | Exact top-level section titles from M08 prompt; cautious tone inside |
| Commit / push / PR | Yes after local verification; stop before merge |

---

## Deliverables map

| Path | Role |
|------|------|
| `docs/working_note/working_note_outline.md` | Section outline seed |
| `docs/working_note/evidence_map.md` | Section ↔ evidence mapping |
| `docs/working_note/README.md` | Directory index |
| `tests/test_m08_working_note_outline.py` | Doc/governance honesty tests |
| `docs/pantanal-1.md` | Ultimate Truth M08 status and claims |

---

## Allowed claim after M08

PANTANAL-1 contains a working-note outline and evidence map that organize the M00–M07 governance, Kaggle, and audit evidence into a public narrative seed.

---

## M08 explicit non-claims

- M08 does not create a full working-note draft.
- M08 does not make the project CLEF submission-ready.
- M08 does not implement model inference.
- M08 does not prove model quality.
- M08 does not improve leaderboard score.
- M08 does not claim RediAI certification.

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
