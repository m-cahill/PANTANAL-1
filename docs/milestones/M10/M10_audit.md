# Milestone Audit — M10: Real Inference Baseline Spike

## 1. Header

| Field | Value |
|-------|--------|
| **Milestone** | M10 — Real Inference Baseline Spike (M10B) |
| **Mode** | DELTA AUDIT |
| **Range** | `8a68e56` (M09 merge on main) … closeout PR head (`5fd1f0a` + closeout commit) |
| **CI Status** | Green (PR #11 run 26878270030) |
| **Audit Verdict** | 🟢 — Uniform-ε non-zero baseline added with schema preservation and strict non-claims; no Kaggle run, training, weights, or model-quality drift |

**Score:** **5.0 / 5.0** (delta **0.0** from M09 **5.0**)

---

## 2. Executive Summary

**Improvements**

- `src/pantanal_1/nonzero_baseline.py` — deterministic uniform-ε baseline (default `0.001`); float-string class values; ε validation `(0, 1]`
- `scripts/run_m10_nonzero_baseline_local.py` — synthetic M01 schema default; optional `--sample-submission`; `--epsilon`
- `docs/kaggle/nonzero_baseline.md` — method, claims, non-claims, documented Kaggle path (no notebook execution in M10)
- Reuse of `sample_baseline`, `submission_contract`, `synthetic_schema` — no duplicated path-safety logic
- 16 new tests (185 total); M06/M07 CI gates unchanged
- Ultimate Truth: narrow M10 claim + explicit M10 non-claims

**Risks**

- Milestone title “Real Inference Baseline” could imply trained inference — mitigated by docs, tests, and non-claims (“spike” = uniform ε placeholder only)
- `nonzero_baseline.py` module coverage ~79% — total package coverage 90%; gate passes
- No Kaggle evidence for non-zero path yet — deferred to M11; do not claim score without owner run

**Next action:** Merge PR #11 after closeout CI green; seed M11 stub; do not begin M11 without plan approval.

---

## 3. Delta Map & Blast Radius

| Zone | Touched | Risk |
|------|---------|------|
| Auth | No | None |
| Persistence | No | None |
| CI glue | No workflow change | None — tests extend pytest |
| Contracts | Extended (non-zero rows) | Low — validated writes; root `submission.csv` blocked |
| Notebooks | No change | None — M03 unchanged per owner lock |
| ML/inference | No trained inference | None — uniform ε only |
| `src/pantanal_1` | New module | Low — stdlib csv; reuses helpers |
| Kaggle runtime | Documented only | Low — no execution in M10 |

**Changed (PR head `5fd1f0a` vs `8a68e56`):** 7 files (+715 / −11 lines).

---

## 4. Architecture & Modularity

### Keep

- M10 logic isolated in `nonzero_baseline.py`; schema read/write reuse from `sample_baseline`
- Synthetic path via `synthetic_schema` + `build_zero_submission_rows` row_ids
- Local outputs only under `tmp/submissions/`; `is_safe_submission_output_path` enforced
- Stdlib-only runtime; no new dependencies

### Fix Now (≤ 90 min)

- Update `test_pantanal_marks_m10_in_progress` → closed assertion at closeout

### Defer

- Kaggle non-zero evidence → **M11** (recommended)
- Audio dependency planning → **M11A**
- Full working-note draft → **M11B** (M10A deferred)
- M03/M10 notebook integration → future if owner approves
- SBOM, action pinning → DEF-001 optional / M11C or later

---

## 5. CI/CD & Workflow Integrity

| Check | Assessment |
|-------|------------|
| Required checks | CI on PR/push |
| Workflow diff | **None** in M10 |
| New tests | 16 governance + module tests |
| M06/M07 gates | Preserved |

**CI truthfulness:** PASS — https://github.com/m-cahill/PANTANAL-1/actions/runs/26878270030 (success, 28s).

---

## 6. Tests & Coverage (Delta-Only)

| Metric | M09 | M10 |
|--------|-----|-----|
| Tests added | 12 | **16** |
| Total tests | 169 | **185** |
| Measured coverage (`src/pantanal_1`) | 95% | **90%** (new module; gate ≥80% passes) |
| `nonzero_baseline.py` module | — | ~79% |
| MyPy / Bandit / pip-audit | PASS | PASS |

**Missing tests (non-blocking):** Some error branches in `validate_nonzero_sample_rows` (column order mismatch, invalid string) not individually asserted; acceptable for spike scope.

---

## 7. Security & Supply Chain

| Area | Status |
|------|--------|
| Runtime dependencies | Unchanged (stdlib) |
| Dev dependencies | Unchanged |
| Bandit / pip-audit | PASS |
| Secrets / competition data | Not committed |
| Kaggle notebook surface | Unchanged (M03 only) |

**Boundary compliance:** PASS.

**Data/weights/secrets policy:** PASS.

---

## 8. Guardrail Compliance Table

| Guardrail | Compliant | Evidence |
|-----------|-----------|----------|
| No Kaggle data in git | Yes | `verify_repo_state.py` |
| No weights in git | Yes | Diff excludes weights |
| No secrets in git | Yes | Unchanged |
| No root `submission.csv` in git | Yes | Verifier + script tests |
| No trained model inference | Yes | Uniform ε only |
| No audio dependencies added | Yes | No audio code in diff |
| No M03 notebook change | Yes | Owner lock; no notebook in diff |
| No Kaggle run in M10 PR | Yes | No evidence doc; non-claims |
| No score improvement claim | Yes | Ultimate Truth + `nonzero_baseline.md` |
| No class priors (owner lock) | Yes | Uniform ε only |
| M06/M07 gates not weakened | Yes | No `ci.yml` change |
| Float-string probabilities | Yes | `format_probability_string`; tests |

---

## 9. Evidence Table

| Artifact | Present | Role |
|----------|---------|------|
| `src/pantanal_1/nonzero_baseline.py` | Yes | Uniform-ε baseline core |
| `scripts/run_m10_nonzero_baseline_local.py` | Yes | Local mirror + diagnostics |
| `docs/kaggle/nonzero_baseline.md` | Yes | Method, claims, Kaggle path (documented) |
| `tests/test_m10_nonzero_baseline.py` | Yes | 16 tests |
| `docs/pantanal-1.md` | Yes | M10 claim, ledger, non-claims |
| Kaggle non-zero run evidence | **No** | Not invented — deferred M11 |
| New public score | **No** | Not invented |
| Model weights | **No** | Not committed |
| Trained inference | **No** | Not implemented |

---

## 10. Boundary Compliance

| Boundary | Assessment |
|----------|------------|
| ORNITHOS private code | Not imported |
| Competition data | Not committed |
| Kaggle-facing packaging | Extended locally; notebook unchanged |
| RediAI certification | Not claimed |
| Working-note readiness | Not claimed |
| Model quality / competitive score | Not claimed |

**Verdict:** PASS.

---

## 11. Non-Zero Baseline Assessment

| Criterion | PASS/FAIL | Evidence |
|-----------|-----------|----------|
| Uniform ε on all class columns | PASS | `build_uniform_nonzero_rows`; default `0.001` |
| Header order preserved | PASS | Tests + `validate_nonzero_sample_rows` |
| Row order preserved | PASS | Tests |
| `row_id` preserved | PASS | Tests |
| Values in `[0, 1]` | PASS | Validation + tests |
| At least one non-zero | PASS | ε > 0; validation `saw_nonzero` |
| Float-string output | PASS | `format_probability_string`; CSV round-trip test |
| ε bounds `(0, 1]` | PASS | `validate_epsilon`; script rejects invalid |
| Synthetic M01 schema default | PASS | 235 columns, 24 rows in test |
| No class priors | PASS | Owner lock; single ε for all classes |

**Verdict:** PASS for M10 baseline scope.

---

## 12. Determinism / Schema Preservation Assessment

| Criterion | PASS/FAIL | Evidence |
|-----------|-----------|----------|
| Deterministic default output | PASS | `test_default_epsilon_is_deterministic` |
| Sample schema read reuse | PASS | `read_sample_submission_csv` from `sample_baseline` |
| Safe output paths | PASS | `is_safe_submission_output_path`; tmp/ only |
| Local script does not write root submission | PASS | Subprocess test |

**Verdict:** PASS.

---

## 13. CI Truthfulness Assessment

| Criterion | Assessment |
|-----------|------------|
| Failures block merge | Yes — required CI on PR |
| New tests run on PR #11 | Yes — 185 passed |
| Signals match local verification | Yes — same command set |
| No workflow signal drift | Yes — `ci.yml` unchanged |

**Verdict:** PASS for M10 closeout.

---

## 14. Documentation Alignment Assessment

| Document | Aligned |
|----------|---------|
| `docs/pantanal-1.md` | Yes — M10 claim, non-claims, ledger (closeout → closed) |
| `docs/kaggle/nonzero_baseline.md` | Yes — matches implementation |
| `docs/milestones/M10/M10_plan.md` | Yes |
| M03 notebook docs | Unchanged — M10 docs reference without modifying M03 |

---

## 15. Top Issues

No HIGH blocking issues for M10 scope.

| ID | Category | Severity | Note |
|----|----------|----------|------|
| DEF-001-OPT | CI/Sec | Low | SBOM, action pinning — optional |
| EVID-001 | Kaggle | Low | No M10 Kaggle run; plan M11 if owner wants evidence |
| COV-001 | Tests | Low | `nonzero_baseline.py` branch coverage ~79%; total 90% |
| HYGIENE-001 | Repo | Low | `coverage.xml` untracked locally — do not commit |

---

## 16. Recommended M11 Guardrails

1. M11 = Kaggle evidence probe **or** audio-dependency planning gate — owner approves plan first
2. Do not claim model quality, audio understanding, or score improvement without direct owner evidence
3. Do not commit competition data, weights, `sample_submission.csv`, `taxonomy.csv`, or generated `submission.csv`
4. If Kaggle run: record output path, row/column counts, runtime, public score **only if shown** — no inference from 0.500 zero baseline
5. Preserve M06/M07/M10 CI and honesty tests
6. Do not wire M10 into M03 notebook without explicit scope
7. Do not add training or heavy audio deps without separate approved milestone

---

## 17. Deferred Issues Registry

| ID | Status after M10 |
|----|------------------|
| **DEF-001** | Substantially addressed in M07 — unchanged |
| **DEF-001 optional** | SBOM, pinning, provenance — future |
| Kaggle non-zero baseline evidence | Deferred — **M11** recommended |
| Trained inference / model quality | Not implemented |
| Full working-note draft | Deferred — **M11B** (M10A deferred) |
| DEF-002A / DEF-002B / DEF-003A / DEF-003B | Unchanged (prior milestones; zero baseline scored 0.500) |

---

## 18. Score Trend

| Milestone | Arch | Mod | Health | CI | Sec | Docs | Overall |
|-----------|------|-----|--------|----|-----|------|---------|
| M09 | 4.6 | 4.6 | 4.7 | 4.9 | 4.2 | 5.0 | **5.0** |
| M10 | 4.7 | 4.7 | 4.7 | 4.9 | 4.2 | 5.0 | **5.0** |

**Weighting:** Modularity improved via focused `nonzero_baseline` module and helper reuse. Docs and non-claims discipline maintained. **Delta: 0.0** overall (maintains audit-ready posture).

---

## 19. Flake & Regression Log

| Item | Type | Status |
|------|------|--------|
| None new | — | No flakes on PR #11 CI |

---

## 20. Machine-Readable Appendix

```json
{
  "milestone": "M10",
  "mode": "DELTA AUDIT",
  "commit": "5fd1f0a",
  "range": "8a68e56...closeout",
  "verdict": "green",
  "score": 5.0,
  "score_delta_from_m09": 0.0,
  "quality_gates": {
    "ci": "pass",
    "tests": "pass_185",
    "coverage": "pass_80_gate_90_measured",
    "mypy": "pass",
    "bandit": "pass",
    "pip_audit": "pass",
    "workflows": "unchanged",
    "kaggle_notebook_unchanged": true,
    "kaggle_run_in_m10": false,
    "model_quality_claimed": false,
    "trained_inference_implemented": false,
    "nonzero_baseline_uniform_epsilon": true,
    "default_epsilon": 0.001
  },
  "deferred_registry_updates": [
    "kaggle nonzero evidence → M11 recommended",
    "audio planning → M11A",
    "full draft → M11B"
  ],
  "score_trend_update": {"M10": 5.0}
}
```
