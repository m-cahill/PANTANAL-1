# Data Policy

**Authority:** Subordinate to `docs/pantanal-1.md`.

---

## Principles

1. **Never commit** Kaggle competition data to this repository.
2. **Never redistribute** competition data (CC BY-NC-SA 4.0; competition rules).
3. Load data only from Kaggle at notebook runtime or from local paths excluded by `.gitignore`.

---

## Prohibited paths (git)

- `train_audio/`, `test_soundscapes/`, `train_soundscapes/`
- Raw audio: `*.ogg`, `*.wav`, `*.mp3`, `*.flac`
- Competition CSVs downloaded for local dev should stay outside the repo or in gitignored locations

---

## Allowed

- Documentation describing file layouts and column contracts
- Synthetic fixtures for tests (minimal, generated in CI if needed — future milestones)

---

## Enforcement

- `.gitignore`
- `scripts/verify_repo_state.py`
- CI runs verifier on every push/PR
