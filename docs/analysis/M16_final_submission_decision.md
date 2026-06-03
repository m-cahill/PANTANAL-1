# M16 Final Submission Decision

**Status:** Pre-deadline decision memo (2026-06-03).  
**Authority:** Subordinate to `docs/pantanal-1.md` and [M16_final_evidence_lock.md](../working_note/M16_final_evidence_lock.md).

**M16C scope:** Documentation only. **No Kaggle submit or notebook modification in this milestone.**

---

## Decision summary

If Kaggle requires a **final notebook selection** before the deadline, the recommended choice is the **already-scored, accepted** baseline:

| Field | Value |
|-------|-------|
| Path | M04 all-zero baseline |
| Notebook | `pantanal_1_m03_baseline` |
| Version | **2** |
| Observed public score | **0.500** |
| Evidence | `docs/kaggle/m04_commit_mode_evidence.md` |

This is the **safest evidenced selection**. It is **not** a competitive or model-quality claim. It is only the **known accepted scored path** with documented commit/submit success (~67s runtime in owner paste).

---

## Facts at decision time

### No new model in PANTANAL-1

- No trained audio-derived model is available in this repository.
- No model weights, checkpoints, or inference pipeline are committed.
- M10–M11 used deterministic placeholder logic only (zero and uniform-ε).

### No private-lane evidence bundle

- No owner-supplied public-safe private-lane evidence bundle has been ingested (M15 request packet only).
- M16A-style ingest was not actionable before the deadline.

### No new Kaggle packaging in M16C

- M16C will **not** modify Kaggle notebooks.
- M16C will **not** attempt new commit/submit runs.
- M16B-style audio packaging requires a CPU-compatible export that is **not** currently evidenced in-repo.

### Only scored evidence on record

| Notebook | Score | Notes |
|----------|-------|-------|
| `pantanal_1_m03_baseline` V2 | **0.500** | All-zero; primary evidenced path |
| `pantanal_1_m11_nonzero_baseline` V2 | **0.500** | Uniform-ε; **no improvement** vs M04 |

**No public score > 0.500** has been observed. **No new score claims** are made in this memo.

---

## Why not prefer M11 or a new notebook?

### M11 uniform-ε (also 0.500)

- M11 demonstrated that a uniform non-zero baseline (ε = 0.001) also scores **0.500**.
- M12 scoring audit explains: near-constant predictions yield **no ranking signal**.
- There is **no evidenced reason** to prefer M11 over M04 for competitive value—both are pipeline probes, not model improvements.

### Unvalidated new notebook (not recommended)

With limited time before the deadline:

- A new or modified notebook has **not** been scored in commit mode during M16C.
- Risk: failed run, invalid `submission.csv`, or unknown score—without time to recover.
- **Do not risk an unvalidated final notebook** when an accepted **0.500** path already exists.

---

## Recommended action

| Situation | Recommendation |
|-----------|----------------|
| Final selection required | Select **M04** / `pantanal_1_m03_baseline` **Version 2** (public score **0.500**) |
| No selection required | No M16C Kaggle action; preserve existing evidenced submissions |
| Hoping for score improvement | **Not supported** by current evidence; would require new model + validated packaging |

---

## Explicit non-claims

This decision memo does **not** claim:

- That **0.500** is competitive or useful for ranking
- That the zero baseline demonstrates audio understanding
- That selecting M04 improves score (it is already **0.500**)
- That M11 is worse or better for competition purposes (both are constant-signal baselines)
- G1/G2/G3/G4 evidence
- Model quality, RediAI certification, or working-note final readiness

---

## Post-deadline

After the deadline, post-M16 options (not M16C implementation) remain:

- Private-lane evidence ingest if a bundle is supplied (M16A track)
- Kaggle audio packaging if CPU export exists (M16B track)
- Working-note refinement when stronger evidence exists

See `docs/working_note/M16_final_evidence_lock.md`.
