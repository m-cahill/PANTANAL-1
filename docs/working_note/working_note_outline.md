# PANTANAL-1 Working Note Outline

## Status

Outline only. Not a full working note. Not submission-ready.

This document is a disciplined **section skeleton** and narrative seed. It organizes existing M00–M07 evidence for a possible future public technical writeup. It does not assert model quality, competitive performance, or CLEF publication readiness.

---

## Proposed Title

A governed Kaggle submission pipeline for BirdCLEF+ 2026: from zero-baseline contract validation to scored submission evidence

---

## Abstract Placeholder

*(Short placeholder — do not treat as a final abstract.)*

This working-note seed would describe how PANTANAL-1 built a governance-first, public Kaggle-facing repository that validated submission contracts, exercised interactive and commit-mode notebook paths, and recorded a scored zero-baseline public result. The narrative emphasizes evidence discipline and explicit non-claims rather than predictive performance.

---

## 1. Introduction

- **BirdCLEF+ 2026 context:** Passive acoustic monitoring in the Brazilian Pantanal; multi-taxa species identification from audio; Kaggle Notebooks as the submission surface; CPU runtime and offline scoring constraints.
- **PANTANAL-1 as public Kaggle-facing repo:** Owns competition packaging, contracts, notebook path, and auditable milestone evidence — not private ORNITHOS model development.
- **Governance-first objective:** Ultimate Truth (`docs/pantanal-1.md`), milestone workflow, data/weights/secrets guardrails, and CI honesty before ML complexity.
- **Strict non-claims:** No model inference implemented; no meaningful or competitive solution demonstrated; public score **0.500** evidences pipeline acceptance only (see §6).

---

## 2. Repository Governance and Boundary Model

- **Ultimate Truth:** `docs/pantanal-1.md` as source of truth for claims, milestones, and boundaries.
- **Milestone workflow:** Phased plans, tool-call logs, CI run analysis, audits, and summaries (M00–M07 closed).
- **Data / weights / secrets policy:** No competition data, credentials, weights, or generated submissions in git; enforced by `.gitignore` and `scripts/verify_repo_state.py`.
- **AURORA / ORNITHOS / PANTANAL-1 boundary:** AURORA (acoustic runtime boundaries), ORNITHOS (private model development), PANTANAL-1 (public Kaggle packaging), RediAI (certification verdicts — not claimed here).

---

## 3. Submission Contract Development

- **M01 synthetic contract:** Generate and validate submission-shaped CSV without real competition data.
- **234 class columns:** Species probability columns per competition rules.
- **5-second windows:** Each `row_id` covers a 5-second audio segment.
- **`row_id` shape:** Contract alignment with expected submission schema (synthetic phase).
- **No real data committed:** CC BY-NC-SA 4.0 competition data stays off-repo; synthetic path only in git.

---

## 4. Kaggle Notebook Path

Evidence-first progression (synthetic → interactive → real sample → scored zero-baseline):

- **M02 — interactive synthetic smoke:** Dependency-free / inline-fallback notebook path; synthetic smoke CSV without competition data in repo.
- **M03 — real sample discovery and interactive `/kaggle/working/submission.csv`:** Real `sample_submission.csv` discovered on Kaggle; zero-baseline CSV aligned to sample schema; **interactive mode only** — not scored commit/submit.
- **M04 — commit/scored path and public score 0.500:** Competition notebook Version 2 completed; output file produced; public score **0.500** on zero baseline — **pipeline acceptance**, not predictive value.

---

## 5. Audit Hardening

- **M06 — coverage + mypy:** Enterprise CI posture; 80% branch coverage fail-under; mypy on `src/pantanal_1` (`docs/quality/audit_hardening.md`).
- **M07 — Bandit + pip-audit:** Security and dependency audit gates without changing Kaggle notebook behavior (`docs/quality/security_supply_chain.md`); DEF-001 substantially addressed.
- **Remaining optional hardening:** SBOM generation, GitHub Actions SHA pinning, provenance/attestation — explicitly deferred.

---

## 6. Results

- **Zero-baseline scored path accepted:** Kaggle scoring accepted the M04 commit-mode zero-baseline submission.
- **Public score 0.500:** Observed public leaderboard score consistent with all-zero predictions.
- **Runtime evidence:** Short successful run (~67s in owner paste) — does not by itself prove full 90-minute scoring-configuration compliance unless separately re-recorded.
- **Pipeline evidence, not model quality:** Score **0.500** supports that the governed submission path can produce a scored output file accepted by Kaggle. It does **not** support claims about predictive model quality, useful inference, or competitive performance.

---

## 7. Limitations

- **No model inference:** Predictions remain zero-baseline; no trained model or audio feature pipeline in repo.
- **No competitive score:** 0.500 is consistent with baseline acceptance, not leaderboard competitiveness.
- **No private leaderboard claim:** Only observed public score is documented.
- **No full hidden-test internals:** DEF-003B narrowed for scored acceptance; hidden row counts and schema not fully exposed in evidence paste.
- **No working-note readiness yet:** This file is an outline seed only; a full draft and CLEF submission review remain future work.

---

## 8. Future Work

- **Real inference baseline:** Minimal non-zero prediction path under Kaggle offline constraints (M08A / separate milestone).
- **Kaggle packaging hardening:** Reduce inline-fallback reliance; improve `pantanal_1` import on Kaggle.
- **Optional SBOM / provenance / action-pinning:** Further DEF-001 optional hardening if scoped.
- **Working-note full draft:** Expand sections with prose, figures, and external review — out of M08 scope.

---

## Evidence Appendix

Section-to-source mapping: see [evidence_map.md](evidence_map.md).

Secondary audit references: see **Secondary Audit Sources** in `evidence_map.md`.
