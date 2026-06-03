# M15 — Owner-Choice Milestone (Stub)

**Status:** Stub only. Implementation not started. Owner approval required before any M15 work.

---

## Purpose

M14 delivered the public-safe evidence contract (validation schema, fixtures, stdlib validator, manifest guidance, model card template, private runbook). **M15** is the next execution fork — owner selects direction based on available artifacts.

**Do not begin M15 until:**

1. M14 is closed on `main`.
2. Owner approves this plan (or a successor) in writing.
3. Owner selects **M15A** or **M15B** below.

---

## M15A — Private-Lane Training Evidence Ingest

**Use when:** Owner supplies a completed **public-safe** private-lane training summary from ORNITHOS/5090 Blackwell.

**Likely scope (when approved):**

- Ingest manifest, model card, validation summary JSON (docs/metadata only unless owner approves binary)
- Run `scripts/validate_m14_evidence.py` on validation summaries
- Update `docs/pantanal-1.md` with claim-safe language only (G1/G2 per M13 evaluation plan)
- Governance tests for ingest boundary

**Out of scope unless separately authorized:**

- Kaggle notebook packaging
- Kaggle submissions
- Model weights in git without owner approval

---

## M15B — Kaggle Audio Baseline Packaging

**Use when:** A **CPU-compatible** export/package candidate exists from private lane.

**Likely scope (when approved):**

- Wire notebook/package evidence for offline CPU inference
- Runtime budget documentation (≤ 90 minutes)
- Preserve no score claims unless public score > **0.500** is observed

**Out of scope unless separately authorized:**

- Raw audio, Kaggle competition data, weights, or private ORNITHOS code in git without owner approval
- Score improvement or model quality claims without evidence

---

## Shared guardrails (binding)

- ORNITHOS remains private upstream; PANTANAL-1 remains public packaging
- Validate against `docs/analysis/M14_evidence_contract.md`
- No score claims without observed public score > **0.500**
- Follow M14 non-claims until appropriate evaluation gate

---

## Owner gate

Do not begin M15 implementation until the owner approves direction (M15A or M15B) in writing.
