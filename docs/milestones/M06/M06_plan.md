# M06 Plan — Audit Hardening / Evidence Consolidation

**Status:** In progress (branch `m06-audit-hardening-evidence-consolidation`)

**Objective:** Begin closing **DEF-001** by adding coverage and mypy CI gates for `src/pantanal_1`, plus audit-hardening evidence and doc tests — without changing Kaggle notebook behavior or adding model inference.

**Definition of done (repo-side):**

- `docs/quality/audit_hardening.md` — M06 scope, thresholds, DEF-001 partial status, verification commands.
- `.coveragerc` — branch coverage on `src/pantanal_1`, fail-under 80%.
- `requirements-dev.txt` — `pytest-cov`, `coverage`, `mypy`.
- `pyproject.toml` — mypy configuration for `src/pantanal_1`.
- `.github/workflows/ci.yml` — mypy + pytest-cov + `coverage report --fail-under=80`; preserve existing checks.
- `tests/test_m06_audit_hardening.py` — stdlib-only doc/CI/config tests.
- `tests/test_m06_source_coverage.py` — minimal tests to satisfy 80% branch coverage gate (if needed).
- `docs/milestones/M06/M06_plan.md` expanded; `M06_toolcalls.md` maintained.
- `docs/pantanal-1.md` — M06 in progress; M06 artifact links; narrow M06 claim; DEF-001 partially addressed; preserve inference/score non-claims.
- PR-head CI green; no competition data, weights, or submissions in git.

**Closeout (owner approval gate):** M06 summary, audit, merge, seed M07 — not part of this implementation commit.

---

## Context

- M05 recommended **M06B** (audit hardening) as primary next direction; zero-baseline scored path is proven (M04 public score **0.500**).
- **DEF-001** (coverage / mypy / security audit gates) remains the largest enterprise posture gap.
- Security and supply-chain scans, such as Bandit, pip-audit, and SBOM generation, are intentionally deferred to **M07+** unless separately authorized.

---

## In scope

1. Expand this plan from stub to full plan.
2. Maintain `M06_toolcalls.md` as work proceeds.
3. Add `docs/quality/audit_hardening.md`.
4. Add `.coveragerc`, update `requirements-dev.txt` and `pyproject.toml`.
5. Update `.github/workflows/ci.yml` with coverage and mypy gates.
6. Add `tests/test_m06_audit_hardening.py` and minimal source coverage tests if needed for 80% branch gate.
7. Update `docs/pantanal-1.md` (M06 in progress; DEF-001 partial; M06 claim/non-claims).
8. Preserve green CI and all existing workflow steps.

---

## Out of scope

- Model inference, training, audio loading, heavy ML dependencies.
- Kaggle notebook behavior changes or new submissions.
- Leaderboard or competitive-quality claims.
- Bandit, pip-audit, SBOM, or full enterprise security stack in M06.
- Separate `coverage_policy.md` / `type_checking_policy.md` (deferred; consolidated in `audit_hardening.md`).
- M06 summary/audit/merge closeout until owner approval.

---

## Locked owner decisions (2026-06-03)

| Topic | Decision |
|-------|----------|
| Coverage threshold | **80%** fail-under; add minimal tests if needed; document only if structural reason forces lower |
| Security scans | **None** in M06; defer to M07+ |
| Policy docs | Only `docs/quality/audit_hardening.md` |
| Commit / push / PR | Yes after local verification; stop before merge |
| M07 follow-up | Security/supply-chain scans deferred to M07+ |

---

## Deliverables map

| Path | Role |
|------|------|
| `docs/quality/audit_hardening.md` | Audit-hardening evidence and DEF-001 partial status |
| `.coveragerc` | Coverage configuration and 80% gate |
| `pyproject.toml` | MyPy settings |
| `.github/workflows/ci.yml` | CI enforcement |
| `tests/test_m06_audit_hardening.py` | Doc/config honesty tests |
| `docs/pantanal-1.md` | Ultimate Truth M06 status and claims |

---

## Allowed claim after M06

PANTANAL-1 adds audit-hardening gates for source coverage and mypy type checking, improving enterprise CI posture without changing Kaggle notebook behavior.

---

## M06 explicit non-claims

- M06 does not implement model inference.
- M06 does not improve leaderboard score.
- M06 does not prove model quality.
- M06 does not add a complete security/supply-chain hardening stack unless explicitly implemented.
- M06 does not claim DEF-001 is fully closed unless all exit criteria are met.

---

## Verification (local)

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
