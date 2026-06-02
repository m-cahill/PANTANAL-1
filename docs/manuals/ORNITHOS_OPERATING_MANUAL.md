# ORNITHOS — Operating manual

**Purpose:** Practical guide for contributors and AI agents working in this repository.  
**Authority:** Governance claims, milestone ledger, and binding non-claims live in [`ORNITHOS.md`](ORNITHOS.md). This manual does not strengthen those claims.

**Last updated:** 2026-06-02 (M40 freeze + public Kaggle repo handoff)

---

## Current state for new agents

- M39 is closed with green CI.
- M40 freezes ORNITHOS for public Kaggle handoff.
- ORNITHOS remains private.
- ORNITHOS is not the public Kaggle/BirdCLEF submission repository.
- Public Kaggle notebook, submission.csv generation, leaderboard evidence, and working-note/public narrative work should happen in a separate public PANTANAL-1 / BirdCLEF-facing repository.
- `docs/ARCHITECTURE.md` is a derived orientation guide and remains subordinate to `docs/ORNITHOS.md`.

---

## 1. Interpretation rules

1. **Contracts over assumptions** — do not assume behavior that is not documented or enforced by tests/CI.
2. **Honesty** — when uncertain, use language like *implemented*, *planned*, *not yet proven*, *out of scope*.
3. **Source of truth** — if documents disagree about milestone truth or claims, **docs/ORNITHOS.md wins.**

---

## 2. What ORNITHOS is / is not

**ORNITHOS is:**

- A **private** repository for **bioacoustic model-stack** work positioned **downstream of AURORA** and **upstream of PANTANAL-1**.
- A place to grow **disciplined** experiments, evaluation records, and packaging narratives **without** turning this repo into the governed runtime or the competition-facing product.

**ORNITHOS is not:**

- AURORA (governed acoustic runtime / ARB surfaces)
- RediAI (external certification system)
- PANTANAL-1 (BirdCLEF-facing deployment and submission packaging)
- The public Kaggle / BirdCLEF submission repository
- A MediaPipe fork or rewrite
- A place to commit raw **datasets**, **weights**, **secrets**, or bulky generated **runs**

---

## 3. Current implemented surface after M39

ORNITHOS currently owns governance and metadata surfaces:

- `docs/ORNITHOS.md` Ultimate Truth / milestone ledger
- `docs/ARCHITECTURE.md` derived architecture guide
- `docs/specs/`, `schemas/`, `fixtures/` contract and evidence metadata
- `scripts/` validators and deterministic emitters
- `tests/` contract, governance, and verifier tests
- `.github/workflows/ci.yml` tiered CI

ORNITHOS still does not claim:

- useful model training
- BirdCLEF submission generation
- Kaggle notebook execution
- benchmark readiness
- RediAI certification
- AURORA runtime consumption
- public-release readiness

---

## 4. Boundary model (exact)

```text
AURORA owns the governed acoustic runtime boundary.
ORNITHOS owns private bioacoustic model development.
PANTANAL-1 owns the final BirdCLEF-facing deployment.
RediAI owns certification verdicts.
```

Hard rules are summarized in [`boundary_rules.md`](boundary_rules.md).

---

## 5. Kaggle / public repository handoff rule

ORNITHOS must remain private and upstream. BirdCLEF/Kaggle implementation belongs in a fresh public PANTANAL-1-facing repository.

**Allowed ORNITHOS role:**

- freeze private governance posture
- provide public-safe architecture summary
- provide handoff rules
- record what may and may not be copied into the public repo

**Forbidden ORNITHOS role:**

- no Kaggle notebooks (do not host)
- generate `submission.csv`
- commit Kaggle data
- commit credentials
- execute public leaderboard workflow
- claim final BirdCLEF submission readiness

See also: [`public_kaggle_repo_handoff_charter.md`](public_kaggle_repo_handoff_charter.md).

---

## 6. Recommended public repo milestone path

Fresh public repo numbering should restart at M00:

- PANTANAL-1 M00 — Public repo bootstrap
- PANTANAL-1 M01 — Kaggle site smoke
- PANTANAL-1 M02 — submission.csv skeleton
- PANTANAL-1 M03 — baseline inference notebook
- PANTANAL-1 M04 — runtime budget pass
- PANTANAL-1 M05 — first scored submission
- PANTANAL-1 M06 — focused improvement pass
- PANTANAL-1 M07 — final submission lock
- PANTANAL-1 M08 — working note seed

---

## 7. Minimum context bundle for a new ChatGPT project

Upload these files to any new ChatGPT / Cursor project before asking for implementation plans:

- `docs/ORNITHOS.md`
- `docs/ARCHITECTURE.md`
- `docs/ORNITHOS_OPERATING_MANUAL.md`
- `docs/milestones/M39/M39_summary.md`
- `docs/milestones/M39/M39_audit.md`
- `docs/milestones/M40/M40_plan.md`
- `docs/milestones/M40/M40_summary.md` after M40 closes
- `docs/milestones/M40/M40_audit.md` after M40 closes
- public repo handoff charter document added in M40 (`docs/public_kaggle_repo_handoff_charter.md`)

---

## 8. Verification commands (local)

From the repository root (Python **3.11**):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .

python scripts/verify_repo_state.py
python -m compileall src tests scripts
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
```

On Linux/macOS, activate with `source .venv/bin/activate`.

---

## 9. Milestones and where plans live

- **Ledger / Ultimate Truth:** `docs/ORNITHOS.md`
- **Milestone plan stubs:** `docs/milestones/MNN/MNN_plan.md`
- **Milestone tooling log:** `docs/milestones/MNN/MNN_toolcalls.md`
- **M40 handoff charter:** `docs/public_kaggle_repo_handoff_charter.md`

M40 objective and acceptance criteria: `docs/milestones/M40/M40_plan.md`.

**No ORNITHOS M41** is selected at M40 closeout unless the maintainer explicitly authorizes continued ORNITHOS work; Kaggle implementation moves to a fresh public PANTANAL-1 / BirdCLEF-facing repository with independent M00+ numbering.

---

## 10. AI agent guardrails

- Prefer **small milestones** with one primary question each.
- Do not “temporarily” add **weights**, **datasets**, **secrets**, or **generated runs** to git — the verifier and policy reject typical paths.
- Do not add `import mediapipe`, `import aurora`, or `import rediai` under `src/ornithos/` unless a future milestone *explicitly* relaxes boundary rules and updates **Ultimate Truth** accordingly.
- Do not claim certification, benchmark performance, or submission readiness unless `docs/ORNITHOS.md` records the evidence.
- no Kaggle notebooks, `submission.csv` generation, or public repo creation inside ORNITHOS unless explicitly instructed.

---

## 11. Ecosystem manuals (local reference only)

Adjacent programs (AURORA, EZRA, DARIA, RediAI, Foundry, QuantLab, and others) may have operating manuals in external/local reference bundles or may be provided separately. Those documents are useful **context** for terminology and boundaries but are **not** authoritative for ORNITHOS unless reproduced here or cited with a clear scope.

---

## 12. Strongest allowed opening claim (until proven otherwise)

See **section 10** of [`ORNITHOS.md`](ORNITHOS.md).

**M40** does not strengthen §10. This manual records freeze and handoff posture only; it does not add model training, inference, Kaggle execution, PANTANAL/BirdCLEF execution, RediAI certification, AURORA runtime consumption, or public-release readiness claims.
