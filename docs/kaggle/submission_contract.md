# Submission Contract — BirdCLEF+ 2026

**Authority:** Subordinate to `docs/pantanal-1.md`.

---

## File

- **Name:** `submission.csv`
- **Format:** CSV with header row

---

## Columns

| Column | Description |
|--------|-------------|
| `row_id` | Slug: `[soundscape_filename]_[end_time]` (segment end time in seconds within the 1-minute file) |
| *234 species columns* | One column per class; column names match `primary_label` / taxonomy (`taxonomy.csv`) |

Example row id: for soundscape `BC2026_Test_0001_S05_20250227_010002.ogg`, segment 00:15–00:20 → `BC2026_Test_0001_S05_20250227_010002_20`.

---

## Semantics

- **One row per 5-second window** across test soundscapes
- Each species column: predicted **probability** of presence (0–1)
- Must align with `sample_submission.csv` row ids and column set at scoring time

---

## Validation

M01 provides a **synthetic validation surface** in `src/pantanal_1/submission_contract.py` with package-level fixtures in `src/pantanal_1/synthetic_schema.py` (re-exported from `tests/fixtures/synthetic_submission_schema.py` for tests). M02 adds a smoke notebook and mirror script; see `docs/kaggle/notebook_smoke.md`. Tests validate:

- `row_id` presence and BirdCLEF-style segment suffix
- exactly 234 synthetic class probability columns
- one row per 5-second window (12 rows per 60-second soundscape)
- probabilities numeric and in `[0, 1]`
- no duplicate row ids
- safe output paths (repo-root `submission.csv` rejected)

This does **not** prove compatibility with the real Kaggle `sample_submission.csv` or taxonomy labels until a future milestone uses local competition files outside git.

Future milestones may add checks against `sample_submission.csv` schema when that file is available locally (not committed to git).
