# M09 Next-Direction Recommendation

**Authority:** Subordinate to `docs/pantanal-1.md`, `docs/working_note/draft_decision_gate.md`, and `docs/analysis/next_milestone_decision_matrix.md`.

**Status:** Planning recommendation from M09 closeout planning. Not an implemented milestone.

---

## Recommended M10 ordering

| Priority | Direction |
|----------|-----------|
| **Primary** | **M10B — Real inference baseline spike** |
| **Secondary** | **M10A — Full working-note draft** |
| **Tertiary** | **M10C — Archive / governed Kaggle template cleanup** |

Also evaluated if owner prioritizes packaging or supply-chain work: **M10D** (Kaggle packaging hardening), **M10E** (optional SBOM/provenance hardening).

---

## Rationale

### Why M10B first (primary)

- M08 and M09 established a **narrative scaffold** (outline, evidence map, decision gate, this checklist).
- A full working note **without any real inference** remains governance-interesting but **scientifically thin**.
- A **minimal inference spike** — smallest proof that predictions are not all-zero — would make a future M10A draft more substantive while preserving strict non-claims.
- Post-deadline posture favors honest evidence over leaderboard chasing; spike scope should stay narrow.

### Why M10A second (secondary)

- Evidence chain, audit posture, and Kaggle path are strong enough to **draft** a public technical narrative.
- Drafting before inference risks a paper that documents governance well but cannot discuss meaningful acoustic modeling results.
- M10A remains valuable after M10B or in parallel only if owner explicitly prioritizes publication over research.

### Why M10C third (tertiary)

- If the owner prefers **closure and reuse** over further BirdCLEF research, template cleanup is the safer path.
- PANTANAL-1 already demonstrates governed Kaggle packaging; M10C crystallizes that for reuse without new science.

---

## What M10B should mean (scope sketch, not M09 implementation)

- Read competition audio in Kaggle-offline constraints where feasible.
- Produce **non-all-zero** predictions with the smallest honest baseline (heuristic or documented public-model path).
- Document runtime, dependencies, and non-claims in Ultimate Truth.
- **Do not** commit competition data, weights, or credentials.

---

## Careful non-claims (binding for this document)

- **Do not claim** that M10B will produce a competitive model.
- **Do not claim** that M10A is submission-ready or CLEF-ready from current repo state.
- **Do not claim** that current PANTANAL-1 has predictive model quality.
- Public score **0.500** on the zero baseline evidences **pipeline acceptance only**, not model quality.

---

## Owner gate

Official M10 direction requires **owner approval after M09 closeout** (merge and summary/audit). M09 records this recommendation only; it does not start M10 work.
