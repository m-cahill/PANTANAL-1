# M15 CI Run 1

**Milestone:** M15 — Private-Lane Evidence Request Packet / Pre-Ingest Readiness Gate  
**PR:** https://github.com/m-cahill/PANTANAL-1/pull/16  
**Branch:** `m15-private-lane-evidence-request`  
**Head SHA:** `c9a3aaac9c47f530e44cc30f7b6879939c65f767`  
**Run:** https://github.com/m-cahill/PANTANAL-1/actions/runs/26916594679  
**Verdict:** success (25s)  
**Trigger:** pull_request  
**Baseline (main):** `1d723c91db4a462ed2fa293351e3777c5049b3dc` (M14 closeout on main)

---

## Step 1 — Workflow inventory

| Job / Check | Required? | Purpose | Pass/Fail | Notes |
|-------------|-----------|---------|-----------|-------|
| `ci` (single job) | Yes | Merge-blocking quality gate | PASS | Workflow name: CI |

All steps in the `ci` job are merge-blocking. No `continue-on-error` observed.

---

## Step 2 — Signal integrity

### Tests

- **310** tests passed, **1** skipped (275 baseline + **35** new M15 governance tests).
- Failures: none.
- M15 surface: docs, analysis request packet, decision gate, template, governance tests only.

### Coverage

- **90%** on `src/pantanal_1` (unchanged vs M14).
- Gate: `--fail-under=80` — PASS.
- No `src/` logic changes in M15.

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

**Change context:** M15 pre-ingest readiness — no owner-supplied private-lane evidence bundle; pivot from M15A ingest to evidence request packet, go/no-go decision gate, and packet template for ORNITHOS/5090 private lane.

**Files changed vs main (`1d723c9` … `c9a3aaa`):** 7 files, +1,080 / −44 lines.

| Zone | Touched | Unexpected delta |
|------|---------|------------------|
| `src/pantanal_1` | No | None |
| CI workflow | No | None |
| Dependencies | No | None |
| Kaggle notebooks | No | None |
| Docs / analysis / tests | Yes | Expected |

**Signal drift:** None. CI workflow unchanged; test count increase expected from M15 governance tests.

---

## Step 4 — Failure analysis

No failures in authoritative PR-head run.

---

## Step 5 — Invariants and guardrails

| Invariant | Held |
|-----------|------|
| Required CI checks enforced | Yes |
| No prohibited artifacts | Yes (`verify_repo_state.py` PASS) |
| M15 request-packet / pre-ingest only | Yes |
| No real private-lane evidence ingested | Yes |
| No G1/G2/G3/G4 evidence claimed | Yes |
| No score/model-quality/RediAI/working-note claims | Yes |
| M06/M07 gates not weakened | Yes (no `ci.yml` change) |

**Prohibited artifact confirmation:** No raw audio, Kaggle competition data, model weights/checkpoints/binaries, generated `submission.csv`, private ORNITHOS code, credentials/secrets, generated runs, or fabricated validation metrics presented as real evidence.

**M15 scope confirmation:** No model training, audio inference, audio/ML dependencies, Kaggle notebook changes, or private-lane evidence ingest.

---

## Step 6 — Verdict

**Verdict:** This run is safe to merge. CI truthfully validates the M15 pre-ingest readiness delta: 310 tests pass (1 skipped), 90% coverage on unchanged `src/`, and repo-state verifier confirms public-safe boundary.

**✅ Merge approved** (contingent on closeout docs commit CI green).

---

## Step 7 — Next actions

| Owner | Action | Milestone |
|-------|--------|-----------|
| Agent | Merge PR #16 (squash); post-merge main CI | M15 closeout |
| Owner | Supply public-safe bundle for M16A ingest, or authorize M16B/M16C | M16 (seed only) |

---

## Local verification (PR branch)

| Command | Result |
|---------|--------|
| `ruff check .` | PASS |
| `ruff format --check .` | PASS |
| `mypy src/pantanal_1` | PASS |
| `python -m compileall src tests scripts` | PASS |
| `pytest -q --cov=src/pantanal_1 --cov-report=term-missing` | PASS (**310** passed, **1** skipped) |
| `coverage report --fail-under=80` | PASS (**90%**) |
| `bandit -r src/pantanal_1` | PASS |
| `pip-audit -r requirements-dev.txt` | PASS |
| `python scripts/verify_repo_state.py` | PASS |

**Warnings/notes:** Untracked `coverage.xml` locally (pytest output); not committed.

**Evidence ingest:** None. M15 remained request-packet / pre-ingest only.
