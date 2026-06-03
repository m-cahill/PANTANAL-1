# M12 Next-Direction Decision

**Authority:** Subordinate to `docs/pantanal-1.md`, `docs/analysis/M12_scoring_methodology_audit.md`, and `docs/working_note/M12_working_note_criteria_audit.md`.

**Status:** Planning recommendation from M12. Not an implemented milestone.

---

## Context

After M11, both submission baselines received public score **0.500**:

| Path | Public score | Score improvement |
|------|--------------|-------------------|
| All-zero (M04) | 0.500 | — |
| Uniform-ε (M11) | 0.500 | **no** |

M12 scoring audit explains this as consistent with non-informative, constant predictions under a rank-based ROC-AUC metric. Working-note criteria audit finds strong engineering evidence but weak model/science contribution.

---

## Decision matrix

| Option | Description | Benefit | Risk | Recommended? |
|--------|-------------|---------|------|--------------|
| **Audio-derived baseline** | Attempt minimal real audio inference (smallest honest path) | Scientific value; stronger future working-note credibility | Dependencies, runtime, license/offline constraints | **Yes — primary (via planning gate)** |
| **Working-note draft v0** | Draft from governance evidence (M08 outline + M00–M11 trail) | Fast narrative; documents reproducible packaging | Weak model contribution; may read as process-only | Secondary |
| **Template/archive hardening** | Reusable Kaggle evidence template repo | Strong reusable artifact for future competitions | Less BirdCLEF-specific science | Viable tertiary |
| **Packaging hardening** | Improve notebook reproducibility (package install on Kaggle) | Practical; reduces inline fallback | Low scientific contribution | Optional |
| **Security/provenance** | SBOM, action pinning, attestation (DEF-001 optional) | Enterprise polish | Not central to competition science | Optional |

---

## Recommended next milestone

**M13 — Audio-Derived Baseline Planning Gate**

### Rationale

1. M11 established pipeline acceptance for the uniform-ε path but **no score improvement** versus all-zero (**0.500** both).
2. Current evidence is strong on governance and submission mechanics, weak on scientific/model contribution.
3. Before adding audio dependencies or public models, a **planning gate** should select the smallest CPU-compatible, license-safe, Kaggle-compatible baseline path (heuristic features, documented public model, or other owner-approved scope).
4. A future working note is more credible if the project either attempts a minimal audio-derived baseline or explicitly frames itself as a governance/evidence-template case study.

### M13 scope sketch (not M12 implementation)

- Document candidate approaches and constraints (CPU ≤ 90 min, internet off, no competition data in git).
- Choose one minimal path with explicit non-claims.
- Do **not** start training or large model work without owner approval of M13 plan.

---

## Alternatives if owner overrides

| Owner priority | Suggested milestone |
|----------------|---------------------|
| Publication over research | M13B — Working-note draft v0 |
| Reuse over BirdCLEF science | M13C — Template/archive hardening |
| Kaggle ergonomics | M13D — Kaggle packaging hardening |
| Supply-chain only | DEF-001 optional hardening |

---

## Careful non-claims

- **Do not claim** that M13 will produce a competitive model.
- **Do not claim** that M12 or current repo state is working-note ready.
- **Do not claim** model quality, audio understanding, or trained inference.
- Public score **0.500** evidences **pipeline acceptance only**, not predictive performance.
- **No score improvement** was observed between all-zero and uniform-ε baselines.

---

## Owner gate

Official M13 direction requires owner approval of `docs/milestones/M13/M13_plan.md` after M12 closeout. M12 records this recommendation only.
