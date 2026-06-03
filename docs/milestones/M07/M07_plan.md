# M07 Plan — Security and Supply-Chain Audit Gate

**Status:** In progress (branch `m07-security-supply-chain-gate`)

**Objective:** Continue **DEF-001** by adding Bandit source security linting and pip-audit dependency vulnerability scanning in CI, with evidence docs and stdlib honesty tests — without changing Kaggle notebook behavior or adding model inference.

**Definition of done (repo-side):**

- `docs/quality/security_supply_chain.md` — M07 scope, commands, DEF-001 substantially-addressed wording, non-claims.
- `requirements-dev.txt` — `bandit`, `pip-audit`.
- `.github/workflows/ci.yml` — `bandit -r src/pantanal_1` and `pip-audit -r requirements-dev.txt` after coverage gate; preserve all M06 steps; `verify_repo_state.py` last.
- `docs/quality/audit_hardening.md` — cross-link to security doc.
- `tests/test_m07_security_supply_chain.py` — stdlib-only doc/CI/config tests.
- `docs/milestones/M07/M07_plan.md` expanded; `M07_toolcalls.md` maintained.
- `docs/pantanal-1.md` — M07 in progress; artifact links; narrow M07 claim; DEF-001 substantially addressed (M07) after gates pass; preserve inference/score/vuln-free non-claims.
- PR-head CI green; no competition data, weights, or submissions in git.

**Closeout (owner approval gate):** M07 summary, audit, merge, seed M08 — not part of this implementation commit.

---

## Context

- M06 partially addressed **DEF-001** with coverage (80% fail-under) and mypy gates (`docs/quality/audit_hardening.md`).
- M07 adds the security/dependency slice deferred from M06.
- Zero-baseline Kaggle path is proven (M04); no notebook behavior changes in M07.

---

## In scope

1. Expand this plan from stub to full plan.
2. Maintain `M07_toolcalls.md` as work proceeds.
3. Add `docs/quality/security_supply_chain.md`.
4. Add `bandit` and `pip-audit` to `requirements-dev.txt`.
5. Update `.github/workflows/ci.yml` with Bandit and pip-audit gates.
6. Cross-link `audit_hardening.md` and `security_supply_chain.md`.
7. Add `tests/test_m07_security_supply_chain.py`.
8. Update `docs/pantanal-1.md` (M07 in progress; DEF-001 substantially addressed after gates pass).
9. Preserve green CI and all existing workflow steps.

---

## Out of scope

- SBOM generation, GitHub Actions SHA pinning, SLSA/provenance (unless owner explicitly authorizes).
- Model inference, training, audio loading, heavy ML dependencies.
- Kaggle notebook behavior changes or new submissions.
- Leaderboard or competitive-quality claims.
- `--ignore-vuln`, `continue-on-error`, or soft-passing security failures.
- M07 summary/audit/merge closeout until owner approval.

---

## Locked owner decisions (2026-06-03)

| Topic | Decision |
|-------|----------|
| Bandit | Plain `bandit -r src/pantanal_1`; no `.bandit`; `# nosec` only for narrow documented false positives |
| pip-audit | `pip-audit -r requirements-dev.txt`; upgrade/pin fixes when straightforward; no ignore without approval |
| DEF-001 wording | **Substantially addressed (M07)** after gates pass; not fully closed until optional hardening scoped |
| Ledger | M07 in artifact table and §7 during implementation; closed at closeout |
| Cross-link | Yes between audit_hardening and security_supply_chain |
| Commit / push / PR | Yes after local verification; stop before merge |

---

## Deliverables map

| Path | Role |
|------|------|
| `docs/quality/security_supply_chain.md` | Security/dependency evidence and DEF-001 M07 status |
| `requirements-dev.txt` | Bandit and pip-audit dev deps |
| `.github/workflows/ci.yml` | CI enforcement |
| `tests/test_m07_security_supply_chain.py` | Doc/config honesty tests |
| `docs/pantanal-1.md` | Ultimate Truth M07 status and claims |

---

## Allowed claim after M07

PANTANAL-1 adds security and dependency audit gates using Bandit and pip-audit, further hardening CI without changing Kaggle notebook behavior.

---

## M07 explicit non-claims

- M07 does not implement model inference.
- M07 does not improve leaderboard score.
- M07 does not prove model quality.
- M07 does not add SBOM/provenance/action pinning unless explicitly implemented.
- M07 does not prove the project is vulnerability-free.

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
bandit -r src/pantanal_1
pip-audit -r requirements-dev.txt
python scripts/verify_repo_state.py
```
