# Kaggle Submission Bible — PANTANAL-1

**Authority:** Subordinate to `docs/pantanal-1.md`. Used to verify Kaggle notebook formatting and debugging discipline.

Related: `docs/kaggle/notebook_smoke.md`, `docs/kaggle/kaggle_setup_runbook.md`, `docs/kaggle/kaggle_setup_evidence.md`.

---

## Notebook modes

| Mode | Purpose | Evidence implication |
|------|---------|-------------------|
| **Interactive** | Debugging, path checks, smoke runs | Does **not** imply scored submission |
| **Commit / submit** | Required for competition scoring | Must be recorded explicitly in evidence |

Every Kaggle evidence record must state which mode was used.

---

## Required Kaggle paths

| Path | Role |
|------|------|
| `/kaggle/input/...` | Mounted datasets (e.g. competition data under `competitions/`) |
| `/kaggle/working/` | Writable working directory for generated outputs |
| `/kaggle/working/submission.csv` | **Required** final path for real scored submissions |

M02 smoke notebooks may write only under `tmp/submissions/...` for synthetic smoke (e.g. `tmp/submissions/m02_smoke_submission.csv`). Do not conflate smoke paths with scored submission paths.

---

## Required output file for real submission

- Final file name must be **`submission.csv`**
- Must be written under **`/kaggle/working/`**
- Do not claim real submission readiness unless this path is observed in commit/submit-mode evidence

---

## Competition runtime constraints

- **CPU** notebook runtime ≤ **90 minutes** for scored submission
- **Internet disabled** during scoring
- **GPU** effectively disabled for BirdCLEF+ 2026 (~1 minute if submitted)
- Record accelerator and internet settings in `docs/kaggle/kaggle_setup_evidence.md`

---

## Dependency rules

- Prefer Kaggle-preinstalled libraries
- Do not rely on internet installs during scoring
- Do not add repo dependencies casually
- Avoid pandas, torch, librosa unless a future milestone explicitly needs them
- M02 synthetic smoke uses **stdlib only** (package import optional; inline fallback documented)

---

## Debug output standard

Future Kaggle notebooks should print at minimum:

- Python version
- Platform
- Current working directory (`cwd`)
- First `sys.path` entries
- `KAGGLE_KERNEL_RUN_TYPE`
- `KAGGLE_URL_BASE`
- `/kaggle`, `/kaggle/input`, `/kaggle/working` existence and children (truncated listing)
- Dataset path discoveries
- Output path written
- Row count / column count
- Header or CSV line preview
- Runtime timing when relevant

Reference implementation: `notebooks/pantanal_1_m02_smoke.ipynb` (output-cleared in git).

---

## Import strategy

- Repo package imports (`pantanal_1`) may fail in copied Kaggle notebooks unless package files are uploaded or installed
- Smoke notebooks may include **inline fallback** only when explicitly documented as synthetic smoke (see M02 notebook)
- Real submission notebooks require a controlled packaging strategy in a later milestone

---

## Evidence rules

Every Kaggle debug or submission attempt should record in `docs/kaggle/kaggle_setup_evidence.md`:

- Notebook URL (if available; otherwise state “not recorded”)
- Notebook version / commit (if available)
- Mode: interactive or commit/submit
- Accelerator
- Internet setting
- Data attached
- Input paths observed
- Output path produced
- Runtime
- Errors / warnings
- Whether submission was attempted
- Score **only if actually observed**

---

## Prohibited claims without evidence

Do not claim any of the following without matching evidence:

- Kaggle execution success (specify mode: interactive vs commit/submit)
- Active competition submission eligibility
- Real `sample_submission.csv` compatibility
- CPU 90-minute scoring compliance
- Model inference
- Leaderboard submission
- Competition score

---

## M02 evidence summary

M02 **interactive** synthetic smoke ran on Kaggle with:

- `KAGGLE_KERNEL_RUN_TYPE`: Interactive
- `pantanal_1` import failed; **inline fallback** succeeded
- Output: `tmp/submissions/m02_smoke_submission.csv` (28134 bytes, 24 rows, 234 synthetic class columns)
- **Did not** produce `/kaggle/working/submission.csv`
- **Did not** submit to the competition or record a leaderboard score

See `docs/kaggle/kaggle_setup_evidence.md` for full observed values.

**DEF-002A** (interactive synthetic smoke): evidenced in M02.

**DEF-002B** (scored/commit-mode real submission path): open.
