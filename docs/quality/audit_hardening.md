# Audit Hardening — M06

## Purpose

M06 begins closing **DEF-001** by adding coverage and type-checking gates for `src/pantanal_1` in CI, with documented thresholds and honest non-claims.

## What M06 Adds

- **coverage.py / pytest-cov** gate for `src/pantanal_1` (branch coverage, 80% fail-under via `.coveragerc`)
- **mypy** gate for `src/pantanal_1` (configured in `pyproject.toml`)
- CI enforcement for both in `.github/workflows/ci.yml`
- `docs/quality/audit_hardening.md` (this file) and stdlib doc/config tests in `tests/test_m06_audit_hardening.py`

M07 extends this M06 audit-hardening slice with security and dependency gates; see `docs/quality/security_supply_chain.md`.

## What M06 Does Not Add

- Model inference
- Kaggle submission or notebook behavior changes
- Heavy ML dependencies
- Security scans (Bandit, pip-audit) — added in M07; SBOM/provenance/action pinning remain optional
- Full enterprise hardening or a 5/5 audit guarantee
- Separate `coverage_policy.md` / `type_checking_policy.md` documents

## Current Thresholds

| Gate | Setting |
|------|---------|
| Coverage fail-under | **80%** total (branch coverage enabled in `.coveragerc`) |
| Coverage source | `src/pantanal_1` |
| MyPy scope | `src/pantanal_1` only (`strict = false`; tests not type-checked) |

## DEF-001 Status

**Substantially addressed in M07** (not fully closed). Coverage and mypy gates were added in M06; Bandit and pip-audit gates were added in M07 (`docs/quality/security_supply_chain.md`). Optional future hardening: SBOM, GitHub Actions SHA pinning, provenance/attestation.

Exit criteria for **full** DEF-001 closure (from `docs/pantanal-1.md`): all agreed gates green **and** any remaining optional hardening items explicitly scoped or waived.

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

Existing steps preserved: Ruff check/format, compileall, pytest with coverage, `coverage report --fail-under=80`, mypy, Bandit, pip-audit, `verify_repo_state.py`.
