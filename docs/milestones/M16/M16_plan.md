# M16C — Working-Note Draft v0 / Final Evidence Lock

**Status:** Closed  
**Branch:** `m16c-working-note-draft-v0`  
**Authority:** `docs/pantanal-1.md`

---

## Time constraint

BirdCLEF+ 2026 final submission deadline: **2026-06-03 23:59 UTC**. M16C is intentionally small, documentation-first, and CI-safe.

---

## Objective

Create a concise working-note draft v0 and final evidence lock that consolidates M00–M15 into a truthful public narrative before the deadline.

This milestone does **not** attempt new model work, Kaggle packaging, audio inference, dependency changes, or private-lane evidence ingest.

---

## Rationale

| Option | Status at M16C start |
|--------|----------------------|
| M16A private-lane evidence ingest | Not actionable — no owner-supplied public-safe bundle |
| M16B Kaggle audio packaging | Not actionable — no CPU-compatible export evidenced |
| **M16C working-note draft v0** | **Selected** — highest-value final pre-deadline milestone |

---

## Deliverables

| Artifact | Purpose |
|----------|---------|
| `docs/working_note/M16_working_note_draft_v0.md` | Complete concise working-note v0 |
| `docs/working_note/M16_final_evidence_lock.md` | Final pre-deadline evidence index |
| `docs/analysis/M16_final_submission_decision.md` | Final Kaggle selection decision memo |
| `tests/test_m16c_working_note_final_lock.py` | Governance tests |
| `docs/pantanal-1.md` | M16 ledger, claim, non-claims |

---

## Verification

```bash
ruff check .
ruff format --check .
mypy src/pantanal_1
python -m compileall src tests scripts
pytest -q --cov=src/pantanal_1 --cov-report=term-missing
coverage report --fail-under=80
bandit -r src/pantanal_1
pip-audit -r requirements-dev.txt
python scripts/verify_repo_state.py
```

---

## Non-Claims

- M16 does not train a model.
- M16 does not implement audio inference.
- M16 does not add audio or ML dependencies.
- M16 does not ingest private-lane evidence.
- M16 does not package a Kaggle audio baseline.
- M16 does not submit to Kaggle.
- M16 does not improve leaderboard score.
- M16 does not claim G1/G2/G3/G4 evidence exists.
- M16 does not prove model quality.
- M16 does not claim RediAI certification.
- M16 does not create final CLEF-ready working-note readiness.

---

## PR stop point

Push branch, open PR, wait for PR-head CI, do not merge, report status.

---

## Closeout (later, owner approval)

Create `M16_run1.md`, `M16_summary.md`, `M16_audit.md`. ensure all documentation is updated as necessary.

Do not begin any further milestone after closeout without owner authorization.
