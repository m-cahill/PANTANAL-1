# M13 Kaggle Inference Packaging Plan

## Goal

Plan how a future audio-derived model would run inside Kaggle CPU notebook constraints after M14 private training and export.

**Status:** Planning decision only. Not proof of runtime compliance or score improvement.

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/kaggle/kaggle_submission_bible.md`.

---

## Constraints

| Constraint | Binding detail |
|------------|----------------|
| CPU runtime | ≤ **90 minutes** for scored submission |
| Internet | **Disabled** during scoring |
| Output path | `/kaggle/working/submission.csv` |
| Schema | `row_id` + **234** species probability columns |
| Row semantics | Each row = **5-second** audio window |
| Dependencies | Must be preinstalled, vendored, or notebook-attached — no pip from internet at score time |
| Data | Test soundscapes via Kaggle mount only; never committed to git |

---

## Packaging Options

| Option | Description | M13 assessment |
|--------|-------------|----------------|
| 1 | Inline notebook fallback (stdlib or pasted minimal code) | Good for smoke; **insufficient** for real audio model |
| 2 | Public Kaggle dataset artifact attached | Strong for weights/features; size/license review required |
| 3 | Committed small inference package in repo | Good for tiny exports; git size policy applies |
| 4 | External public model only (rules/license) | Viable if offline-loadable and size acceptable |

---

## Recommended Primary Path

**Train externally on the 5090 Blackwell (private lane), export a compact public-safe inference artifact, and package CPU-only Kaggle inference with all dependencies and models vendored or notebook-attached for internet-disabled execution.**

### Rationale

1. Matches ORNITHOS → PANTANAL-1 boundary: training stays private; public repo carries contracts and manifests.
2. Satisfies internet-off constraint by bundling deps at notebook build time.
3. Avoids large weight commits to git when Kaggle Dataset attachment is cleaner.
4. Enables reproducible commit-mode runs with explicit version pins in evidence docs.

### Implementation sketch (M15 target — not M13)

```text
Build phase (private/M14):
  train → validate non-constant OOF → export ONNX/torchscript → profile CPU timing

Package phase (M15):
  attach artifact to Kaggle Dataset OR vendor minimal wheel in notebook
  notebook: load test soundscapes → window → infer → write submission.csv

Evidence phase (M15+):
  interactive run → commit/scored run → record score only if observed
```

---

## Fallback / Decision Branches (M14/M15)

| Branch | When to use |
|--------|-------------|
| Kaggle Dataset attachment | Export > few MB or many files; keeps git lean |
| Committed tiny package | ONNX < agreed size threshold; owner approves |
| Inline fallback only | Contract smoke after failure — not production baseline |
| Preinstalled Kaggle libs only | If export uses torch/numpy already on kernel — verify version pins |

---

## Runtime Risks

| Risk | Mitigation plan |
|------|-----------------|
| Audio loading time | Profile per-file decode; batch windows; limit debug I/O |
| Spectrogram compute | Precompute or lightweight mel; cache per soundscape |
| Model load time | Single load at startup; small ONNX |
| Per-window inference cost | Batch inference; vectorize; cap debug rows |
| Package import failures | Pin versions; test commit-mode dry run; inline fallback for diagnostics only |
| 90-minute overrun | Early timing checkpoints in notebook; reduce model size |
| Memory pressure | Stream soundscapes; avoid loading full competition train set |

---

## Notebook Contract (future)

Future Kaggle notebooks should preserve M03/M11 diagnostics standard:

- Python version, platform, cwd, `KAGGLE_KERNEL_RUN_TYPE`
- Input path discoveries under `/kaggle/input`
- Confirm write to `/kaggle/working/submission.csv`
- Row count, column count (expect 235 with `row_id`)
- Mode: interactive vs commit/submit
- Runtime timing
- Score **only if observed**

---

## M14 / M15 Implication

| Milestone | Responsibility |
|-----------|----------------|
| **M14** | Train/evaluate on 5090; OOF evidence; export candidate; CPU timing estimate |
| **M15** | Wire notebook; attach artifacts; run Kaggle evidence; compare to 0.500 baselines |

M13 does not modify existing notebooks (`pantanal_1_m03_baseline.ipynb`, `pantanal_1_m11_nonzero_baseline.ipynb`).

---

## Non-Claims

- Primary packaging path is a **planning recommendation**, not evidenced Kaggle execution.
- No claim that packaged inference will finish within 90 minutes until profiled in M14/M15.
- No claim of score improvement unless public score > **0.500** is observed.
- M13 does not add torch, librosa, or other audio/ML dependencies to the repo.
