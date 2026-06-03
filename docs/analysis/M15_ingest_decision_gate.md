# M15 Ingest Decision Gate

**Purpose:** Define go/no-go criteria for future M15A private-lane evidence ingest.

**Authority:** Subordinate to `docs/pantanal-1.md` and `docs/analysis/M14_evidence_contract.md`.

**Status:** Decision gate definition only — no evidence has been evaluated yet.

---

## Decision Gate Overview

When the private lane provides an evidence bundle, use this gate to determine whether PANTANAL-1 should:

1. **Proceed to M15A ingest** — evidence is complete and valid
2. **Return to private lane** — evidence is incomplete or invalid
3. **Switch to M15B Kaggle packaging** — if CPU-compatible export exists but summary evidence is incomplete
4. **Defer** — pivot to working-note/archive track if no viable path forward

---

## Go Criteria (ALL must pass for M15A ingest)

### Mandatory Checks

| # | Criterion | Validation Method | Required |
|---|-----------|-------------------|----------|
| 1 | Validation summary exists | File present | Yes |
| 2 | Validation summary passes validator | `python scripts/validate_m14_evidence.py <path>` | Yes |
| 3 | Model manifest exists | File present | Yes |
| 4 | Model card exists | File present | Yes |
| 5 | License/provenance summary exists | File present | Yes |
| 6 | No prohibited artifacts | `python scripts/verify_repo_state.py` | Yes |
| 7 | `status` is `private_trained_summary` or `owner_approved_binary` | Validator check | Yes |

### Gate-Specific Checks

| Gate | Additional Criterion | Validation Method |
|------|---------------------|-------------------|
| G1 | `non_constant_predictions_verified` is `true` | Validator check |
| G1 | Non-constant prediction summary exists | File present |
| G2 | CPU timing summary exists | File present |
| G2 | Timing estimate ≤ 90 minutes documented | Manual review |
| G3 | Kaggle commit success evidence | Screenshot/log in evidence bundle |
| G4 | Public score > 0.500 observed | Screenshot/log with score |

---

## No-Go Criteria (ANY triggers rejection)

| # | No-Go Condition | Resolution |
|---|-----------------|------------|
| 1 | Validation summary fails validator | Fix and resubmit |
| 2 | `status` is `planning_only` but claims G1+ | Change status or remove claims |
| 3 | `non_constant_predictions_verified` is `false` but claims G1 | Run non-constant check in private lane |
| 4 | Prohibited artifacts present (audio, CSVs, binaries, secrets) | Remove and resubmit |
| 5 | Missing required files | Complete bundle |
| 6 | Unverifiable score claims | Provide Kaggle screenshot evidence |
| 7 | Private ORNITHOS code included | Remove all private code |

---

## Decision Outcomes

### Outcome A: Proceed to M15A Ingest

**When:** All mandatory checks pass, target gate criteria satisfied.

**Action:**
1. Create branch `m15a-private-lane-evidence-ingest`
2. Add evidence files to appropriate `docs/` paths
3. Run full verification suite
4. Update `docs/pantanal-1.md` with claim-safe language
5. Open PR and wait for CI

### Outcome B: Return to Private Lane

**When:** Evidence is incomplete or validation fails.

**Action:**
1. Document specific failures in M15 toolcalls
2. Provide feedback to private lane with this checklist
3. Wait for corrected evidence bundle
4. Re-evaluate when resubmitted

### Outcome C: Switch to M15B Kaggle Packaging

**When:** CPU-compatible export exists but summary evidence is incomplete; Kaggle packaging is higher priority.

**Action:**
1. Document decision in M15 toolcalls
2. Create M15B plan for Kaggle packaging
3. Defer evidence ingest to M16 or later

### Outcome D: Defer to Working-Note/Archive Track

**When:** No viable path forward; private lane cannot produce required evidence.

**Action:**
1. Document decision in M15 toolcalls
2. Update `docs/pantanal-1.md` with project status
3. Consider M15C archive/template hardening or working-note draft

---

## Claim Upgrade Rules

| Current Gate | Upgrade To | Required Evidence |
|--------------|------------|-------------------|
| G0 | G1 | `non_constant_predictions_verified: true` + prediction summary |
| G1 | G2 | CPU timing summary with ≤ 90 min estimate |
| G2 | G3 | Kaggle commit success screenshot/log |
| G3 | G4 | Public score > 0.500 screenshot/log |
| G4 | G5 | Working-note contribution evidence |

---

## Non-Claims

This decision gate:

- Does not ingest real private-lane evidence
- Does not evaluate actual evidence (no evidence exists yet)
- Does not claim G1/G2/G3/G4 evidence exists
- Does not prove model quality or score improvement
