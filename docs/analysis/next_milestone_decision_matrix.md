# PANTANAL-1 Next-Milestone Decision Matrix

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/analysis/post_competition_analysis.md`.

**Scale:** 1 = low / weak / poor fit — 5 = high / strong / excellent fit (subjective planning scores, not leaderboard metrics).

---

## Candidates

| ID | Candidate | Description |
|----|-----------|-------------|
| **M06A** | Real inference baseline spike | Minimal audio-reading + simple non-trained heuristic or documented public-model path; smallest proof that predictions are not all-zero |
| **M06B** | Audit hardening | Coverage, mypy, security gates; address **DEF-001** |
| **M06C** | Kaggle packaging hardening | Better package import strategy on Kaggle; reduce inline fallback reliance |
| **M06D** | Working-note seed | Post-competition working-note **outline** turning M00–M04 evidence into a public narrative: governed Kaggle pipeline, zero-baseline scoring proof, strict non-claims, future inference roadmap. Sources: `post_competition_analysis.md`, `M00_M04_evidence_index.md`, `kaggle_submission_bible.md`, `m04_commit_mode_evidence.md`. **Outline only** — not full draft in M06D unless explicitly scoped |
| **M06E** | Archive / reusable template cleanup | Refactor PANTANAL-1 into a reusable Kaggle competition template (governance, verifier, milestone layout) |

---

## Scoring matrix

| Candidate | Impact | Risk | Time (5=fast) | Dep. weight (5=light) | Evidence value | Alignment | **Total** |
|-----------|--------|------|---------------|------------------------|----------------|-----------|-----------|
| **M06A** | 4 | 4 | 3 | 2 | 4 | 3 | **20** |
| **M06B** | 4 | 2 | 4 | 5 | 5 | 5 | **25** |
| **M06C** | 3 | 2 | 4 | 4 | 3 | 4 | **20** |
| **M06D** | 3 | 1 | 4 | 5 | 4 | 3 | **20** |
| **M06E** | 3 | 2 | 2 | 4 | 3 | 3 | **17** |

**Column notes:**

- **Impact:** Value toward stated project goals (governance, honest competition packaging, audit posture).
- **Risk:** 5 = lowest risk of regressions, bad claims, or CI breakage.
- **Time:** 5 = fastest to meaningful done (inverse of calendar effort).
- **Dep. weight:** 5 = fewest new runtime/ML dependencies.
- **Evidence value:** How much auditable proof the milestone adds for future sessions.
- **Alignment:** Fit with post-deadline posture and `docs/pantanal-1.md` boundaries.

---

## Per-candidate summary

### M06A — Real inference baseline spike

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Impact | 4 | Unblocks “not proven: model inference” |
| Risk | 4 | New deps, runtime, claim discipline |
| Time | 3 | Audio path + Kaggle offline constraints take longer than docs-only work |
| Dep. weight | 2 | Likely needs audio/ML stack decisions |
| Evidence value | 4 | Strong if scoped with honest non-claims |
| Alignment | 3 | Good for research; less urgent post-deadline |

### M06B — Audit hardening

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Impact | 4 | Closes **DEF-001**; raises enterprise/audit posture |
| Risk | 2 | CI/config changes; manageable scope |
| Time | 4 | Incremental CI jobs + thresholds |
| Dep. weight | 5 | Dev tooling only |
| Evidence value | 5 | Directly improves audit score trend |
| Alignment | 5 | Matches governance-first repo identity post-M04 |

### M06C — Kaggle packaging hardening

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Impact | 3 | Reduces inline-fallback fragility |
| Risk | 2 | Packaging experiments on Kaggle |
| Time | 4 | Smaller than full inference |
| Dep. weight | 4 | Mostly packaging, not training |
| Evidence value | 3 | Helps future submissions |
| Alignment | 4 | Supports Kaggle-facing mission |

### M06D — Working-note seed

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Impact | 3 | Publication narrative; no ML proof |
| Risk | 1 | Documentation-only if outline-only |
| Time | 4 | Can reuse M05 analysis artifacts |
| Dep. weight | 5 | No new ML deps |
| Evidence value | 4 | Consolidates public story |
| Alignment | 3 | Valuable for CLEF path; not blocking inference |

### M06E — Archive / template cleanup

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Impact | 3 | Reuse for future competitions |
| Risk | 2 | Refactor scope creep |
| Time | 2 | Broad rename/doc pass |
| Dep. weight | 4 | Mostly structural |
| Evidence value | 3 | Template value for new repos |
| Alignment | 3 | Secondary to DEF-001 and inference |

---

## Recommendation

### Primary: **M06B — Audit hardening / evidence consolidation**

If the goal is **enterprise-grade closure** and a **stronger audit score**, do audit hardening next.

- Competition deadline has passed; zero-baseline scored path is proven (M04, public **0.500**).
- **DEF-001** is the largest remaining honesty gap vs. ideal enterprise posture.
- Low dependency weight; high evidence value; aligns with M00–M05 governance arc.

### Secondary: **M06A — Real inference baseline spike**

If the goal is **research momentum**, do the **smallest possible** real inference spike next.

- Accept higher risk and dependency weight.
- Require explicit non-claims until quality is evidenced.
- Do not conflate any new score with competitive performance without baseline comparison.

### When to prefer M06C, M06D, or M06E

| Choose | When |
|--------|------|
| **M06C** | Next Kaggle submission is likely and inline fallback is the main friction |
| **M06D** | Publication/working-note timeline matters more than ML or CI gates |
| **M06E** | Starting a new competition repo from this scaffold is the near-term goal |

---

## Decision-ready statement

```text
Primary recommendation: M06B — Audit hardening / evidence consolidation
Secondary option: M06A — Real inference baseline spike, if the owner wants continued ML progress

If the goal is enterprise-grade closure and a stronger audit score, do audit hardening next.
If the goal is research momentum, do the smallest possible real inference spike next.
```

M05 evaluates M06D (working-note seed) as a real candidate; M05 does **not** draft the working note.
