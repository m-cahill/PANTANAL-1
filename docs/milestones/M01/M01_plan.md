# M01 Plan — submission.csv Skeleton + sample_submission Contract

**Status:** In progress (owner-approved 2026-06-03)

**Branch:** `m01-submission-skeleton-contract`

---

## 1. Objective

Create a minimal, auditable submission-generation and validation surface for BirdCLEF+ 2026 using synthetic fixtures only. Prove PANTANAL-1 can generate a correctly shaped `submission.csv`-style artifact and validate the required contract without committing Kaggle competition data.

M01 is **not** a model milestone.

---

## 2. Definition of done

- [ ] Synthetic submission contract module with row_id, validation, and CSV writer
- [ ] Reusable synthetic 234-class fixture module
- [ ] Zero-baseline submission generator script writing to `tmp/submissions/submission.csv`
- [ ] Contract tests covering row counts, schema, validation failures, and safe output paths
- [ ] Repo verifier still rejects root-level `submission.csv`
- [ ] `tmp/` gitignored; no real submission artifacts committed
- [ ] Local verification green (ruff, compileall, pytest, verifier)
- [ ] PR opened with green CI
- [ ] `docs/pantanal-1.md` updated with narrow M01 claim and non-claims

---

## 3. In scope

1. `src/pantanal_1/submission_contract.py` — contract helpers and validator
2. `tests/fixtures/synthetic_submission_schema.py` — 234 synthetic class labels and soundscape stems
3. `scripts/make_zero_submission.py` — CLI for zero-baseline artifact generation
4. `tests/test_submission_contract.py` — contract and verifier regression tests
5. `.gitignore` — add `tmp/`
6. Documentation updates (`docs/pantanal-1.md`, `docs/kaggle/submission_contract.md`)

---

## 4. Out of scope

- Kaggle notebook execution (M02)
- Reading real `sample_submission.csv` or `taxonomy.csv`
- Competition audio or Kaggle data in git
- Model inference, runtime budget proof, leaderboard submission
- Heavy ML dependencies (no pandas)
- Full audit/security hardening (DEF-001)

---

## 5. Contract surface

| Function | Purpose |
|----------|---------|
| `build_row_id(stem, end_time_seconds)` | BirdCLEF-style row id |
| `build_segment_end_times(duration=60, window=5)` | Segment end times for one soundscape |
| `build_zero_submission_rows(stems, class_labels)` | Zero-baseline rows |
| `validate_submission_rows(rows, class_labels)` | Contract validation |
| `write_submission_csv(rows, output_path, class_labels)` | Stdlib CSV writer |

**Exceptions:** `SubmissionContractError`, `SubmissionValidationError`, `UnsafeSubmissionPathError`

---

## 6. Validation rules

Validator fails when:

- `row_id` missing or duplicate
- class count/columns mismatch (expected 234 synthetic labels)
- extra class columns present
- probabilities not numeric or outside `[0, 1]`
- row id does not end with integer segment end time
- output path is repo-root `submission.csv`

---

## 7. Safe output rule

- Generated artifacts write only to `tmp/submissions/submission.csv` (gitignored) or pytest temp directories
- M00 verifier unchanged — still rejects root-level `submission.csv`
- Test proves verifier regression

---

## 8. Verification commands

```bash
ruff check .
ruff format --check .
python -m compileall src tests scripts
pytest -q
python scripts/verify_repo_state.py
```

---

## 9. Claims (after success)

**Allowed:**

> PANTANAL-1 can generate and validate a synthetic zero-baseline submission-shaped CSV artifact using 234 synthetic class columns and 5-second row windows.

**Non-claims (unchanged):**

- Real Kaggle `sample_submission.csv` compatibility
- Kaggle notebook execution
- Inference, CPU runtime compliance, leaderboard submission or score

---

## 10. Stop point

Stop after PR-head CI is green. Do not merge without owner approval.
