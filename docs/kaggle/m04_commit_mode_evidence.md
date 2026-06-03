# M04 Commit-Mode Evidence

**Status:** Executed (Kaggle competition notebook Version 2; scored public score observed).

**Authority:** Subordinate to `docs/pantanal-1.md`. Competition notebook commit/scored run — not interactive-only debugging.

Related: `docs/kaggle/m04_commit_mode_probe.md`, `docs/kaggle/m03_kaggle_evidence.md`, `notebooks/pantanal_1_m03_baseline.ipynb`.

---

## Status vocabulary

Allowed field values:

```text
yes
no
blocked — deadline passed
N/A — not attempted
```

---

## Notebook

- URL: https://www.kaggle.com/code/michael1232/pantanal-1-m03-baseline/notebook?scriptVersionId=324138273
- Name: `pantanal_1_m03_baseline`
- Visibility: Private
- Version / commit: Version 2 of 2
- Date/time: not recorded in owner paste
- Runner: owner manual run

---

## Mode

- Interactive: **no**
- Commit: **yes** (Version 2 of 2 committed on Kaggle)
- Submit: **yes** (public leaderboard score observed)
- Notes: Kaggle UI labeled **Competition Notebook: BirdCLEF+ 2026**. Logs: `67.4 second run - successful`. This is scored submission evidence, not M03 interactive-only debugging.

---

## Runtime settings

- Accelerator: not recorded in owner paste
- Internet: not recorded in owner paste
- Runtime: **1m 7s** (Kaggle UI); logs report **67.4 second** successful run
- `KAGGLE_KERNEL_RUN_TYPE`: not recorded in owner paste

**Note:** Observed wall/runtime is well under the 90-minute CPU scoring budget, but accelerator and internet settings were not re-recorded in this paste. Do not claim CPU/internet scoring-configuration compliance beyond the observed short runtime.

---

## Input discovery

- Competition data attached: **yes** — BirdCLEF+ 2026 (Kaggle input: COMPETITIONS)
- `/kaggle/input` children: not recorded in owner paste (competition data attached per Kaggle UI)
- `sample_submission.csv` discovered: not re-recorded in owner paste (M03 interactive run discovered `/kaggle/input/competitions/birdclef-2026/sample_submission.csv`)
- Exact path: not re-recorded in owner paste
- Row count (sample): not re-recorded in owner paste
- Column count (sample): not re-recorded in owner paste

---

## Output evidence

- Kaggle reported output: **1 file**
- `/kaggle/working/submission.csv` produced: **yes** (competition notebook produced scored output; data preview matches submission schema; exact path not re-printed in Kaggle UI paste)
- File size: not recorded in owner paste
- Row count: **3** (three `row_id` values observed in data preview)
- Column count: **235** (`row_id` + 234 class/probability columns per data preview)
- Header preview: `row_id`, `1161364`, `116570`, `1176823`, `1491113`, `47158son01`, `ashgre1`, `brnowl`, … (truncated in owner paste)
- First `row_id`: `BC2026_Test_0001_S05_20250227_010002_5`
- Last `row_id`: `BC2026_Test_0001_S05_20250227_010002_15`
- Baseline type: **zero baseline** (all class values shown are `0.0`)

---

## Submission / scoring

- Submit button available: **yes** (scored submission accepted)
- Submitted: **yes**
- Submission ID: not recorded in owner paste
- Scoring still available: **yes** (public score returned)
- Public leaderboard score: **0.500**
- Best score (Kaggle UI): **0.500 V2**
- Private leaderboard score: not observed / not recorded
- Errors/warnings: none recorded (run successful)

---

## Deferred issue assessment

| ID | Assessment |
|----|------------|
| **DEF-002B** | **Evidenced (M04)** — Kaggle competition notebook Version 2 completed successfully, Kaggle reported **1 output file**, and public score **0.500** was recorded. Scored/commit path exercised beyond M03 interactive-only evidence. |
| **DEF-003B** | **Narrowed/evidenced (M04)** — Kaggle scoring accepted the zero-baseline output and returned public score **0.500**. Hidden-test row counts and full scored-test internals were **not** exposed in the owner paste; do not claim full hidden-test schema visibility. |

---

## Claim recommendation

**Allowed after this evidence:**

- M04 Kaggle commit/scored evidence: competition notebook `pantanal_1_m03_baseline` Version 2 completed in **1m 7s**, produced an output file, and received public score **0.500** on the zero-baseline path.

**Do not claim:**

- Model inference or meaningful model quality (zero baseline only).
- Competitive solution quality (score 0.500 is consistent with all-zero baseline).
- Private leaderboard performance (not observed).
- CPU 90-minute scoring runtime compliance beyond observed short runtime (accelerator/internet not re-recorded).
- Hidden/full test row count beyond the three `row_id` values visible in the data preview.
