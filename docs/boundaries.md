# PANTANAL-1 Boundaries

**Authority:** Subordinate to `docs/pantanal-1.md`.

---

## Roles

```text
PANTANAL-1 is public and Kaggle-facing.
ORNITHOS is private and upstream.
AURORA is a governed acoustic runtime dependency surface.
RediAI certification claims are out of scope unless explicitly implemented and evidenced.
```

---

## Dependency direction

```text
AURORA (released runtime seams) → optional downstream consumption
ORNITHOS (private model dev) → handoff rules only; no private code import
PANTANAL-1 (this repo) → Kaggle notebook, submission.csv, public narrative
RediAI → external certification verdicts; artifact-only integration
```

---

## Forbidden in PANTANAL-1

- Importing or vendoring private ORNITHOS source
- Committing competition datasets, weights, secrets, or scored submissions
- Claiming certification, benchmark scores, or submission readiness without evidence in Ultimate Truth

---

## Allowed

- Public-safe architecture summaries from upstream handoff charters
- Pre-trained models referenced by URL/hash in notebooks when Kaggle rules allow
- Local documentation copies of competition rules (not data)
