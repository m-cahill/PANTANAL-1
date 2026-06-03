# M11 Plan — Kaggle Non-Zero Baseline Evidence Probe

**Status:** In progress (owner-approved 2026-06-03).

**Branch:** `m11-kaggle-nonzero-baseline-evidence`

---

## Single objective

Prepare and document an owner-run Kaggle path for the M10 deterministic uniform-ε non-zero baseline, with honest evidence boundaries — without claiming model quality, trained inference, or score improvement unless directly observed.

---

## Definition of done

- [ ] `docs/kaggle/m11_nonzero_baseline_runbook.md` — interactive + commit/submit guidance
- [ ] `docs/kaggle/m11_nonzero_baseline_evidence.md` — unfilled template (“Not yet executed”)
- [ ] `notebooks/pantanal_1_m11_nonzero_baseline.ipynb` — output-cleared; M03 diagnostics + M10 logic + inline fallback
- [ ] `tests/test_m11_nonzero_evidence.py` and `tests/test_m11_nonzero_notebook.py` — stdlib governance tests
- [ ] `docs/pantanal-1.md` — M11 in progress, narrow pre-evidence claim, explicit non-claims
- [ ] `docs/kaggle/nonzero_baseline.md` — references M11 runbook/evidence/notebook
- [ ] PR opened; PR-head CI green; **no merge** without owner permission
- [ ] Owner Kaggle evidence (optional follow-up commit after manual run)

---

## Questions M11 answers

1. Can the M10 non-zero baseline run in a Kaggle-compatible notebook path?
2. Does it produce `/kaggle/working/submission.csv` using real `sample_submission.csv` schema?
3. If submitted/scored, what is the observed public score?
4. Does the result show score improvement over 0.500, or simply another accepted pipeline?
5. What claims are and are not justified?

---

## In scope

| Item | Path |
|------|------|
| Runbook | `docs/kaggle/m11_nonzero_baseline_runbook.md` |
| Evidence template | `docs/kaggle/m11_nonzero_baseline_evidence.md` |
| Notebook | `notebooks/pantanal_1_m11_nonzero_baseline.ipynb` |
| Tests | `tests/test_m11_nonzero_evidence.py`, `tests/test_m11_nonzero_notebook.py` |
| Governance | `docs/pantanal-1.md`, `docs/kaggle/nonzero_baseline.md` |

**Locked settings:** `EPSILON = 0.001`; dedicated M11 notebook (no M03 edits); interactive then commit then optional submit.

---

## Out of scope

- Training, neural inference, audio features, model weights, public model downloads
- Kaggle API; notebook execution in CI
- Committing competition data, real `sample_submission.csv`, generated `submission.csv`, scored artifacts
- Claiming score improvement without observation; model quality; RediAI certification
- M11A audio dependency planning pivot

---

## Allowed claims

**Before owner Kaggle run (initial PR):**

> PANTANAL-1 contains a runbook and evidence template for evaluating the M10 deterministic non-zero baseline on Kaggle without overclaiming model quality.

**After owner evidence (follow-up only):**

> M11 recorded Kaggle evidence for the M10 uniform-ε non-zero baseline, including output path, runtime, and public score if observed.

---

## Explicit non-claims

- M11 does not prove model quality.
- M11 does not prove audio understanding.
- M11 does not prove trained model inference.
- M11 does not claim score improvement unless directly observed.
- M11 does not add model weights.
- M11 does not claim RediAI certification.

---

## Authoritative context

- `docs/pantanal-1.md`
- `docs/kaggle/nonzero_baseline.md`
- `docs/kaggle/m04_commit_mode_evidence.md` (zero baseline scored 0.500)
- `docs/milestones/M10/M10_summary.md`
- `src/pantanal_1/nonzero_baseline.py`

---

## Stop point

Stop after PR-head CI is green. Do not merge. Owner may run Kaggle manually and provide evidence in a follow-up commit.
