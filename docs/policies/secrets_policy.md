# Secrets Policy

**Authority:** Subordinate to `docs/pantanal-1.md`.

---

## Principles

1. **Never commit** API keys, Kaggle credentials, or environment secrets.
2. Use Kaggle Secrets / environment injection at runtime, not files in the repo.
3. Rotate credentials immediately if accidental exposure occurs.

---

## Prohibited in git

- `.kaggle/` directory
- `kaggle.json`
- `.env`, `.env.*`
- `*.secret`, `*.key`, `*.pem`

---

## Enforcement

- `.gitignore`
- `scripts/verify_repo_state.py`
- Future: pre-commit secret scan (deferred post-M00)

---

## Reporting

If a secret is committed, remove from history per GitHub guidance and rotate the credential before continuing work.
