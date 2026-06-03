# Kaggle Setup Evidence — PANTANAL-1

**Status:** Attempted; blocked by package import failure on first manual run. Patched notebook pending re-test.

---

## First manual attempt (pre-import-fallback patch)

**Observed error:**

```text
ModuleNotFoundError: No module named 'pantanal_1'
```

Traceback occurred at:

```python
from pantanal_1.submission_contract import (
    build_zero_submission_rows,
    validate_submission_rows,
    write_submission_csv,
)
```

**Interpretation:** The initial copied Kaggle notebook did not have the repository package installed or available on `sys.path`.

**Resolution planned:** M02 notebook updated to include verbose environment diagnostics and an inline synthetic fallback path aligned with `pantanal_1.synthetic_schema` (see commit `fix(m02): add Kaggle notebook import fallback diagnostics` on branch `m02-kaggle-notebook-smoke`).

**Claims from this failure:** This failure does **not** prove Kaggle execution success, submission generation, runtime compliance, inference, or leaderboard score.

**DEF-002:** Remains open until the patched notebook runs in the Kaggle CPU environment with recorded evidence below.

---

## Kaggle notebook

- URL:
- Version / commit:
- Created by:
- Date/time:

---

## Runtime settings

- Accelerator:
- Internet:
- Competition data attached:
- Observed input path:

---

## Execution evidence (patched notebook re-test)

- Notebook ran on Kaggle: yes / no / unknown
- Used inline fallback (`SOURCE = inline fallback`): yes / no / unknown
- Produced `/kaggle/working/submission.csv`: yes / no / unknown (M02 smoke uses `tmp/submissions/m02_smoke_submission.csv` only)
- Produced `tmp/submissions/m02_smoke_submission.csv`: yes / no / unknown
- Runtime:
- Errors/warnings:

---

## Submission evidence

- Submitted to competition: yes / no
- Submission ID:
- Public leaderboard score:
- Private leaderboard score:
- Notes:

---

## Claim update recommendation

Do **not** update `docs/pantanal-1.md` claims unless evidence above is filled with actual observed results from a successful patched-notebook run.

Do **not** mark **DEF-002** resolved until live Kaggle CPU execution is documented here with verifiable links or logs.
