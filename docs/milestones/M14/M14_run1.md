# M14 CI Run 1

**Milestone:** M14 — 5090 Blackwell Audio-Derived Baseline Evidence Contract  
**PR:** https://github.com/m-cahill/PANTANAL-1/pull/15  
**Branch:** `m14-audio-baseline-evidence-contract`  
**Head SHA:** `8481cf952243f35c1d40ca91478bc6a561fbc4bf`  
**Run:** https://github.com/m-cahill/PANTANAL-1/actions/runs/26913828912  
**Verdict:** success (25s)  
**Trigger:** pull_request  
**Baseline (main):** `4666bbe` (M13 closeout telemetry on main)

---

## Step 1 — Workflow inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
|-------------|-----------|---------|-----------|-------|
| `ci` (single job) | Yes | Merge-blocking quality gate | PASS | Workflow name: CI |

All steps in the `ci` job are merge-blocking. No `continue-on-error` observed.

---

## Step 2 — Signal integrity

### Tests

- **275** tests passed (28 new M14 governance/validator tests; baseline was 247).
- Failures: none.
- M14 surface: docs, schema, fixtures, stdlib validator script, governance tests only.

### Coverage

- **90%** on `src/pantanal_1` (unchanged vs M13).
- Gate: `--fail-under=80` — PASS.
- No `src/` logic changes in M14; coverage gate unchanged.

### Static / policy gates

| Step | Result |
|------|--------|
| Ruff check | PASS |
| Ruff format | PASS |
| MyPy (`src/pantanal_1`) | PASS |
| Compileall (`src`, `tests`, `scripts`) | PASS |
| Bandit | PASS |
| pip-audit | PASS |
| `verify_repo_state.py` | PASS |

### Performance

- Not applicable (no benchmarks in this workflow).

---

## Step 3 — Delta analysis

**Change context:** M14 evidence-contract milestone — operationalize M13 planning into validation schema, fixtures, stdlib validator, manifest guidance, model card template, private runbook, governance tests.

**Files changed vs main (`4666bbe` … `8481cf9`):** 13 files, +1287 / −44 lines.

| Zone | Touched | Unexpected delta |
|------|---------|------------------|
| `src/pantanal_1` | No | None |
| CI workflow | No | None |
| Dependencies | No | None |
| Kaggle notebooks | No | None |
| Docs / schemas / fixtures / scripts / tests | Yes | Expected |

**Signal drift:** None. CI workflow unchanged; test count increase is expected from M14 governance tests.

---

## Step 4 — Failure analysis

No failures in authoritative PR-head run.

---

## Step 5 — Invariants and guardrails

| Invariant | Held |
|-----------|------|
| Required CI checks enforced | Yes |
| No prohibited artifacts | Yes (`verify_repo_state.py` PASS) |
| M14 evidence-contract only (no training/inference/deps) | Yes |
| No score/model-quality/RediAI/working-note claims | Yes |
| M06/M07 gates not weakened | Yes (no `ci.yml` change) |

**Prohibited artifact confirmation:** No raw audio, Kaggle competition data, model weights, `submission.csv`, private ORNITHOS code, credentials, or generated runs committed.

**M14 scope confirmation:** No model training, audio inference, audio/ML dependencies, Kaggle notebook changes, or overclaiming validation summaries (validator rejects planning-only overclaims).

---

## Step 6 — Verdict

**Verdict:** This run is safe to merge. CI truthfully validates the M14 evidence-contract delta: 275 tests pass, 90% coverage on unchanged `src/`, and repo-state verifier confirms public-safe boundary.

**✅ Merge approved** (contingent on closeout docs commit CI green).

---

## Step 7 — Next actions

| Owner | Action | Milestone |
|-------|--------|-----------|
| Agent | Merge PR #15 (squash); post-merge main CI | M14 closeout |
| Owner | Choose M15A (private ingest) vs M15B (Kaggle packaging) | M15 (seed only) |

---

## Local verification (PR branch)

| Command | Result |
|---------|--------|
| `ruff check .` | PASS |
| `ruff format --check .` | PASS |
| `mypy src/pantanal_1` | PASS |
| `python -m compileall src tests scripts` | PASS |
| `pytest -q --cov=src/pantanal_1 --cov-report=term-missing` | PASS (275) |
| `coverage report --fail-under=80` | PASS (90%) |
| `bandit -r src/pantanal_1` | PASS |
| `pip-audit -r requirements-dev.txt` | PASS |
| `python scripts/verify_repo_state.py` | PASS |
| `validate_m14_evidence.py` on both fixtures | PASS |

**Warnings:** Untracked local `coverage.xml` (not committed). Node.js 20 deprecation annotation on Actions setup (informational).
