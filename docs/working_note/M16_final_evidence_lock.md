# M16 Final Evidence Lock

**Status:** Pre-deadline evidence lock (2026-06-03). Authoritative claims remain in `docs/pantanal-1.md`.

**Purpose:** Single index of what PANTANAL-1 has proven, what it has not proven, and how to act before/after the BirdCLEF+ 2026 deadline.

---

## M00–M15 evidence chain (high level)

| Phase | Milestones | Evidence type |
|-------|------------|---------------|
| Bootstrap | M00 | Governance, policies, CI scaffold |
| Contract | M01 | Synthetic `submission.csv` contract (234 classes, 5s windows) |
| Kaggle path | M02–M04 | Interactive smoke → sample schema → **scored 0.500** |
| Analysis | M05 | Post-competition analysis, decision matrix |
| CI hardening | M06–M07 | Coverage, mypy, Bandit, pip-audit |
| Narrative seed | M08–M09 | Working-note outline, draft gate |
| Baseline probes | M10–M11 | Uniform-ε generator; **scored 0.500** (no gain) |
| Audits | M12 | Scoring methodology, working-note criteria |
| Audio planning | M13–M14 | Strategy, evidence contract, validator |
| Pre-ingest | M15 | Evidence request packet (no bundle supplied) |
| **Final lock** | **M16C** | This document + draft v0 + submission decision |

Each milestone M00–M15: closed on `main` with PR, CI, summary, and audit (see `docs/pantanal-1.md` ledger).

---

## Scored evidence currently available

| Submission path | Notebook | Version | Public score | Evidence doc |
|-----------------|----------|---------|--------------|--------------|
| All-zero baseline | `pantanal_1_m03_baseline` | 2 | **0.500** | `docs/kaggle/m04_commit_mode_evidence.md` |
| Uniform-ε baseline | `pantanal_1_m11_nonzero_baseline` | 2 | **0.500** | `docs/kaggle/m11_nonzero_baseline_evidence.md` |

**No other scored submissions are documented in PANTANAL-1.**

No audio-derived model submission exists. No public score > **0.500** has been observed.

---

## What is proven

- Public repo governance and Ultimate Truth discipline (M00+)
- Submission contract for 234 classes and 5-second windows (M01)
- Kaggle interactive paths without competition data in git (M02–M03)
- **Commit/scored submission path accepts zero baseline** with public score **0.500** (M04)
- **Commit/scored uniform-ε path** also scores **0.500** with no improvement (M11)
- CI gates: lint, types, tests (≥80% coverage on `src/`), security scans (M06–M07)
- Constant-prediction scoring interpretation documented (M12)
- Audio-derived **planning** and M14 **evidence contract** exist (M13–M14)
- Private-lane **evidence request packet** exists; no ingest performed (M15)
- Working-note draft v0 and this evidence lock (M16C)

---

## What is not proven

- Model inference or meaningful model quality
- Audio understanding or species discrimination
- Score improvement over baseline **0.500**
- G1 (non-constant OOF), G2 (CPU timing), G3 (new commit), G4 (score > 0.500)
- Private leaderboard performance beyond observed public scores
- Full hidden-test row counts and internals
- CPU 90-minute **scoring-configuration** compliance (short runtime observed only)
- RediAI certification
- CLEF-ready or final working-note publication readiness
- Private-lane training evidence in PANTANAL-1

---

## Final submission posture

**Before deadline (2026-06-03 23:59 UTC):**

- PANTANAL-1 contains **no new model** and **no new Kaggle notebook changes** in M16C.
- The only **evidenced scored paths** are M04 (all-zero) and M11 (uniform-ε), both **0.500**.
- If Kaggle requires a final notebook selection, see `docs/analysis/M16_final_submission_decision.md`.

**Recommended posture:** Prefer the **already-scored, accepted** M04 zero-baseline over any unvalidated new submission in the remaining time.

---

## Post-deadline next-step options

These are **post-M16C** options only—not implemented in M16C:

| Option | When | Action |
|--------|------|--------|
| **M16A / future private-lane ingest** | Owner supplies public-safe evidence bundle | Validate with `scripts/validate_m14_evidence.py`; ingest per M15 gate |
| **M16B / future Kaggle packaging** | CPU-compatible export exists | Package for offline CPU inference; no score claims without evidence |
| **Working-note refinement** | Stronger evidence exists | Expand draft v0 toward publication quality |
| **DEF-001 optional** | Owner scopes hardening | SBOM, action pinning, provenance |

Do not begin post-deadline work without owner authorization.

---

## Lock statement

As of M16C closeout on the PR branch, PANTANAL-1’s competitive submission story is **baseline-only**: two accepted **0.500** scores, governance-complete milestone chain M00–M15, and honest non-claims preserved in Ultimate Truth.

No fabricated metrics, no private-lane ingest, no deadline-risk unvalidated notebook in M16C.
