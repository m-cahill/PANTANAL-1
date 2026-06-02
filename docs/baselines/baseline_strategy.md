# Baseline Strategy

**Authority:** Subordinate to `docs/pantanal-1.md`.

---

## Ideal path (ORNITHOS handoff charter)

```text
M00 — Public repo bootstrap
M01 — Kaggle site smoke
M02 — submission.csv skeleton
M03 — baseline inference notebook
M04 — runtime budget pass
M05 — first scored submission
M06 — focused improvement pass
M07 — final submission lock
M08 — working note seed
```

---

## Compressed path (deadline: 2026-06-03 23:59 UTC)

After M00 is green, prioritize:

```text
M01 — submission.csv skeleton + sample_submission contract
M02 — Kaggle notebook smoke
M03 — baseline inference notebook / first scored attempt if eligible
```

Defer M04–M08 unless time and eligibility allow.

---

## Near-term intent

| Milestone | Goal |
|-----------|------|
| M01 | Synthetic or zero baseline `submission.csv` matching contract; column/row_id validation |
| M02 | Minimal Kaggle notebook loads data path, writes `submission.csv`, respects runtime/internet rules |
| M03 | First real inference path; scored submission evidence if rules and time permit |
| M04 | CPU runtime budget measurement and trimming |
| M05 | First leaderboard evidence when eligible |

---

## Non-goals until proven

- Claiming competitive score without CI/Kaggle evidence
- Committing competition data or weights for convenience
