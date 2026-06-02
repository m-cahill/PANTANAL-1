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

## Validation (future milestones)

M01+ should add automated checks against `sample_submission.csv` schema when that file is available locally (not committed to git).
