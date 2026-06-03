# M10 Plan — Real Inference Baseline Spike

**Status:** In progress (owner-approved 2026-06-03; M10B locked).

**Branch:** `m10-real-inference-baseline-spike`

---

## Purpose

Implement the smallest deterministic **non-zero** submission baseline for PANTANAL-1: uniform ε on every class column, preserving real `sample_submission.csv` schema when available locally, without training, model weights, or audio inference.

This proves the repo can move beyond all-zero predictions while preserving strict non-claims about model quality.

---

## Scope

### In scope

| Deliverable | Path |
|-------------|------|
| Non-zero baseline module | `src/pantanal_1/nonzero_baseline.py` |
| Local mirror script | `scripts/run_m10_nonzero_baseline_local.py` |
| Kaggle behavior documentation | `docs/kaggle/nonzero_baseline.md` |
| Tests | `tests/test_m10_nonzero_baseline.py` |
| Milestone plan + toolcalls | `docs/milestones/M10/M10_plan.md`, `M10_toolcalls.md` |
| Ultimate Truth update | `docs/pantanal-1.md` (M10 in progress, narrow claims/non-claims) |

**Baseline method:** uniform ε = `0.001` default on all class columns; values written as float strings (e.g. `"0.001"`). Reuse `sample_baseline.py`, `submission_contract.py`, `synthetic_schema.py`, `kaggle_paths.py` for schema/path safety.

**Local outputs:** `tmp/submissions/m10_nonzero_baseline.csv` (synthetic default); `tmp/submissions/m10_sample_nonzero_baseline.csv` (optional `--sample-submission`).

**Script:** `--epsilon` exposed; reject `epsilon <= 0` or `epsilon > 1`.

### Out of scope

- Training, neural inference, public model downloads, model weights in git
- Audio feature extraction (non-trivial / heavy deps)
- M03 notebook changes; new M10 notebook (docs only for Kaggle path)
- Kaggle run, commit/submit, score claims in initial PR
- Competition data, real `sample_submission.csv`, generated submissions in git
- M10A full working-note draft; M10C archive cleanup
- RediAI certification; leaderboard improvement claims

---

## Definition of done

1. `nonzero_baseline.py` implements uniform-ε builders, validation, and safe writes.
2. Local script runs synthetic default and optional real sample path under `tmp/`.
3. `docs/kaggle/nonzero_baseline.md` documents method, claims, non-claims, Kaggle path (documented only).
4. Tests cover schema preservation, ε validation, determinism, script safety, governance strings.
5. Full local verification passes (ruff, mypy, pytest ≥80% coverage, bandit, pip-audit, `verify_repo_state.py`).
6. PR to `main` with green PR-head CI; **no merge** until owner approval.

---

## Verification

```bash
pip install -r requirements-dev.txt
ruff check .
ruff format --check .
mypy src/pantanal_1
python -m compileall src tests scripts
pytest -q --cov=src/pantanal_1 --cov-report=term-missing --cov-report=xml
coverage report --fail-under=80
bandit -r src/pantanal_1
pip-audit -r requirements-dev.txt
python scripts/verify_repo_state.py
```

---

## Claims (in progress / post-implementation)

**Allowed narrow claim:**

PANTANAL-1 contains a deterministic non-zero baseline generator that preserves submission schema and produces valid non-zero probability values without adding model weights or training.

**Explicit non-claims:**

- M10 does not implement trained model inference.
- M10 does not prove audio understanding.
- M10 does not prove model quality.
- M10 does not improve leaderboard score unless separately scored and evidenced.
- M10 does not add model weights.
- M10 does not claim RediAI certification.

---

## Stop point

Stop after PR-head CI is green. Report branch, SHA, PR URL, CI URL, files changed, verification results. Do not merge without owner approval.

Manual Kaggle evidence may follow in a separate commit if owner runs Kaggle and provides evidence.
