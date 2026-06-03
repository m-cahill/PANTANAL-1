# Security and Supply-Chain Audit Gate — M07

## Purpose

M07 continues **DEF-001** by adding source security and dependency vulnerability gates.

M06 added coverage and mypy gates; M07 adds Bandit and pip-audit.

## What M07 Adds

- **Bandit** on `src/pantanal_1`
- **pip-audit** on `requirements-dev.txt`
- CI enforcement for both checks

## What M07 Does Not Add

- SBOM generation
- provenance or artifact attestation
- GitHub Actions SHA pinning
- model inference
- Kaggle submission behavior changes
- a guarantee of total security

## Commands

```bash
bandit -r src/pantanal_1
pip-audit -r requirements-dev.txt
```

## DEF-001 Status

Coverage and mypy were added in M06. M07 adds Bandit and pip-audit. **DEF-001** may be considered **substantially addressed in M07** if both pass in CI; SBOM/provenance/action pinning remain optional future hardening items unless explicitly scoped.

See also `docs/quality/audit_hardening.md` for the M06 coverage/mypy slice.

## Non-Claims

M07 security gates reduce obvious source/dependency risk; they do not prove the project is vulnerability-free.
