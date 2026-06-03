# M16 — Owner-Choice Milestone (Stub)

**Status:** Stub only. Implementation not started. Owner approval required before any M16 work.

---

## Purpose

M15 delivered the private-lane evidence request packet, ingest decision gate, and placeholder template. **M16** is the next execution fork — owner selects direction based on available artifacts.

**Do not begin M16 until:**

1. M15 is closed on `main`.
2. Owner approves this plan (or a successor) in writing.
3. Owner selects **M16A**, **M16B**, or **M16C** below.

---

## M16A — Private-Lane Evidence Ingest

**Use when:** Owner supplies a completed **public-safe** private-lane training summary from ORNITHOS/5090 Blackwell (per M15 request packet).

**Likely scope (when approved):**

- Ingest manifest, model card, validation summary JSON (docs/metadata only unless owner approves binary)
- Run `scripts/validate_m14_evidence.py` on validation summaries
- Update `docs/pantanal-1.md` with claim-safe language only (G1/G2 per M13 evaluation plan)
- Governance tests for ingest boundary

**Out of scope unless separately authorized:**

- Raw audio, Kaggle competition data, weights, private ORNITHOS code, generated submissions
- Kaggle notebook packaging
- Kaggle submissions

---

## M16B — Kaggle Audio Baseline Packaging

**Use when:** A **CPU-compatible** export/package candidate exists from private lane.

**Likely scope (when approved):**

- Wire notebook/package evidence for offline CPU inference
- Runtime budget documentation (≤ 90 minutes)
- Preserve no score claims unless public score > **0.500** is observed

**Out of scope unless separately authorized:**

- Raw audio, Kaggle competition data, weights, or private ORNITHOS code in git without owner approval
- Score improvement or model quality claims without evidence

---

## M16C — Working-Note Draft v0

**Use when:** Owner chooses narrative consolidation using M00–M15 evidence before further model work.

**Likely scope (when approved):**

- Draft working-note sections from evidence map and milestone summaries
- Preserve non-claims; avoid claiming model quality or competitive performance

**Out of scope unless separately authorized:**

- Full CLEF submission readiness claims
- Model quality or score improvement claims without evidence

---

## Shared guardrails (binding)

- ORNITHOS remains private upstream; PANTANAL-1 remains public packaging
- Validate against `docs/analysis/M14_evidence_contract.md` and M15 request packet
- No score claims without observed public score > **0.500**
- Follow M14/M15 non-claims until appropriate evaluation gate

---

## Owner gate

Do not begin M16 implementation until the owner approves direction (M16A, M16B, or M16C) in writing.
