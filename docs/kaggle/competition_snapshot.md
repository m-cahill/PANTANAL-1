# BirdCLEF+ 2026 — Competition Snapshot

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/BirdCLEFrules.md`.

---

| Field | Value |
|-------|-------|
| **Competition** | BirdCLEF+ 2026 |
| **Task** | Identify species in continuous Pantanal audio recordings (birds, amphibians, mammals, reptiles, insects) |
| **Metric** | Macro-averaged ROC-AUC variant skipping classes with no true positives |
| **Submission** | `submission.csv` via Kaggle Notebooks |
| **Runtime** | CPU ≤ 90 minutes; internet disabled during scoring |
| **GPU** | Effectively disabled (~1 minute if submitted) |
| **Data license** | CC BY-NC-SA 4.0 — do not redistribute from this repo |
| **Final deadline** | **2026-06-03, 11:59 PM UTC** |

---

## Data layout (reference; not committed here)

- `train_audio/` — short labeled recordings (XC / iNat)
- `train_soundscapes/` — field soundscapes; subset labeled in `train_soundscapes_labels.csv`
- `test_soundscapes/` — ~600 one-minute OGG files at scoring time (hidden test)
- `train.csv`, `taxonomy.csv`, `sample_submission.csv`

---

## Code competition requirements

- Notebook-only submission
- External public data/models allowed if rules-compliant
- Output file must be named `submission.csv`
