# Audit Hardening — M06

## Purpose

M06 begins closing **DEF-001** by adding coverage and type-checking gates for `src/pantanal_1` in CI, with documented thresholds and honest non-claims.

## What M06 Adds

- **coverage.py / pytest-cov** gate for `src/pantanal_1` (branch coverage, 80% fail-under via `.coveragerc`)
- **mypy** gate for `src/pantanal_1` (configured in `pyproject.toml`)
- CI enforcement for both in `.github/workflows/ci.yml`
- `docs/quality/audit_hardening.md` (this file) and stdlib doc/config tests in `tests/test_m06_audit_hardening.py`

## What M06 Does Not Add

- Model inference
- Kaggle submission or notebook behavior changes
- Heavy ML dependencies
- Security scans (Bandit, pip-audit, SBOM) — deferred to M07+ unless separately authorized
- Full enterprise hardening or a 5/5 audit guarantee
- Separate `coverage_policy.md` / `type_checking_policy.md` documents

## Current Thresholds

| Gate | Setting |
|------|---------|
| Coverage fail-under | **80%** total (branch coverage enabled in `.coveragerc`) |
| Coverage source | `src/pantanal_1` |
| MyPy scope | `src/pantanal_1` only (`strict = false`; tests not type-checked) |

## DEF-001 Status

**Partially addressed.** Coverage and mypy gates are implemented and enforced in CI. Security and dependency/supply-chain scans remain for a future milestone (M07+ recommended).

Exit criteria for full DEF-001 closure (from `docs/pantanal-1.md`): CI jobs green with **agreed** thresholds for coverage, mypy, **and** security audit components.

## Verification

### Local

```bash
pip install -r requirements-dev.txt
ruff check .
ruff format --check .
mypy src/pantanal_1
python -m compileall src tests scripts
pytest -q --cov=src/pantanal_1 --cov-report=term-missing --cov-report=xml
coverage report --fail-under=80
python scripts/verify_repo_state.py
```

### CI (`.github/workflows/ci.yml`)

Existing steps preserved: Ruff check/format, compileall, pytest with coverage, `coverage report --fail-under=80`, mypy, `verify_repo_state.py`.
