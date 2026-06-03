# M04 Plan — Kaggle Commit-Mode Submission Path Probe

**Status:** Closed (PR #5; branch `m04-kaggle-commit-mode-probe`)

**Objective:** Probe and document whether the M03 zero-baseline notebook path can run in Kaggle **commit/submit mode** and produce `/kaggle/working/submission.csv`, with honest evidence and without overclaiming eligibility, score, or model quality.

**Definition of done (repo-side):**

- `docs/kaggle/m04_commit_mode_probe.md` runbook exists with manual steps and claim rules.
- `docs/kaggle/m04_commit_mode_evidence.md` records owner Kaggle commit/scored run (executed).
- Static tests (`tests/test_m04_commit_mode_docs.py`) enforce doc presence, recorded evidence, and honest claim boundaries.
- `docs/pantanal-1.md` marks M04 in progress; DEF-002B evidenced; DEF-003B narrowed/evidenced.
- `docs/kaggle/kaggle_submission_bible.md` links M04 probe/evidence docs without success claims.
- PR-head CI green; no competition data, weights, or `submission.csv` in git.

**Manual step (owner, after green CI):** Run commit-mode probe per runbook; record observed values in evidence file. Do not close DEF-002B or DEF-003B without direct commit/submit-mode evidence.

---

## Context

- M03 closed with **interactive** evidence only: real `sample_submission.csv` discovered; `/kaggle/working/submission.csv` produced (3 rows, 235 columns). See `docs/kaggle/m03_kaggle_evidence.md`.
- **DEF-002A** closed (M02). **DEF-003A** evidenced (M03 interactive). **DEF-002B** evidenced (M04). **DEF-003B** narrowed/evidenced (M04 scored acceptance).
- BirdCLEF+ 2026 final deadline has passed. M04 must not assume active eligibility, scoring, or submission availability unless directly evidenced. If Kaggle blocks commit/submit/scoring, record **blocked — deadline passed** (or the exact observed blocker).

---

## In scope

1. Expand this plan from stub to full plan.
2. Maintain `M04_toolcalls.md` as work proceeds.
3. Add `docs/kaggle/m04_commit_mode_probe.md` (runbook + claim rules).
4. Add `docs/kaggle/m04_commit_mode_evidence.md` (template with status vocabulary: `yes` / `no` / `blocked — deadline passed` / `N/A — not attempted`).
5. Add `tests/test_m04_commit_mode_docs.py` (~12–16 assertions).
6. Update `docs/pantanal-1.md` (M04 in progress; preserve DEF-002B/DEF-003B open).
7. Update `docs/kaggle/kaggle_submission_bible.md` (M04 links; no M04 success claims).
8. Preserve green CI; no notebook logic changes unless a clear defect is found.

---

## Out of scope

- Model training or acoustic inference.
- Improving leaderboard score.
- Downloading Kaggle data into the repo.
- Committing `sample_submission.csv`, `taxonomy.csv`, audio, model weights, generated `submission.csv`, or Kaggle outputs.
- Kaggle API dependency or Jupyter execution in CI.
- `scripts/prepare_m04_kaggle_copy.py` (skipped unless a future need is proven).
- Claims of scored submission, active eligibility, leaderboard score, or CPU scoring compliance without direct evidence.
- M04 summary/audit/merge closeout (owner approval gate).

---

## Deferred issues (M04 targets)

| ID | M04 role | Exit criteria (unchanged) |
|----|----------|---------------------------|
| **DEF-002B** | Primary probe target | Commit/submit-mode run produces `/kaggle/working/submission.csv` with recorded evidence |
| **DEF-003B** | Secondary | Commit/submit-mode run confirms scored/hidden test schema behavior |

Interactive evidence does **not** close DEF-002B. M03 interactive output does not close DEF-003B.

---

## Evidence status vocabulary

Use in `m04_commit_mode_evidence.md`:

| Value | When to use |
|-------|-------------|
| `yes` | Directly observed affirmative |
| `no` | Directly observed negative |
| `blocked — deadline passed` | Kaggle blocks commit/submit/scoring because deadline passed |
| `N/A — not attempted` | Step was not tried |

If a different blocker is observed, record the exact blocker instead of assuming deadline.

---

## Deliverables map

| Path | Role |
|------|------|
| `docs/kaggle/m04_commit_mode_probe.md` | Owner runbook |
| `docs/kaggle/m04_commit_mode_evidence.md` | Evidence template / recorded run |
| `tests/test_m04_commit_mode_docs.py` | Doc and claim discipline tests |
| `notebooks/pantanal_1_m03_baseline.ipynb` | Unchanged unless defect found |
| `docs/pantanal-1.md` | M04 in progress; claims unchanged |
| `docs/kaggle/kaggle_submission_bible.md` | M04 cross-links |

---

## Verification (local)

```bash
ruff check .
ruff format --check .
python -m compileall src tests scripts
pytest -q
python scripts/verify_repo_state.py
```

---

## Stop point

Stop after PR-head CI is green. Do not merge without owner approval. Manual Kaggle evidence may follow using the runbook.
