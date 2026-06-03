# M12 — Scoring Methodology and Working-Note Criteria Audit

## Milestone intent

Audit the BirdCLEF+ 2026 scoring methodology and CLEF working-note award criteria in light of the M03/M04 all-zero baseline and M10/M11 uniform-ε non-zero baseline both scoring **0.500**.

M12 is a **documentation / analysis / governance milestone**. It should explain why non-informative baselines can score 0.500 under the competition metric, assess whether the project has enough evidence for a working note, and recommend the next smallest milestone.

M12 must not implement trained inference, audio feature extraction, model weights, Kaggle submissions, public-model downloads, or working-note final drafting unless explicitly authorized later.

## Current context

M11 closed successfully.

Evidence:

- M11 uniform-ε baseline notebook Version 2 succeeded on Kaggle.
- Public score: **0.500**.
- Prior all-zero baseline score: **0.500**.
- Score improvement: **no**.

## Branch

`m12-scoring-working-note-criteria-audit`

## In scope

1. Scoring methodology audit (`docs/analysis/M12_scoring_methodology_audit.md`)
2. Working-note criteria audit (`docs/working_note/M12_working_note_criteria_audit.md`)
3. Next-direction decision (`docs/analysis/M12_next_direction_decision.md`)
4. Update `docs/pantanal-1.md` with M12 status, claims, and non-claims
5. Tests: `tests/test_m12_scoring_working_note_audit.py`
6. M12 plan/toolcalls; summary/audit after closeout only

## Out of scope

No model training, trained inference, audio features, audio dependencies, model weights, public model downloads, new Kaggle submissions, new Kaggle notebooks (unless docs-only and justified), generated `submission.csv`, competition data, credentials, RediAI certification, full working-note manuscript, score improvement claims, model quality claims, working-note readiness claims.

## Acceptance criteria

- Scoring audit explains 0.500 equality without overclaiming
- Working-note criteria audit honestly assesses readiness
- Next-direction decision document exists with M13 recommendation
- `docs/pantanal-1.md` records M12 claims and non-claims
- Tests enforce M12 document presence and non-claim discipline
- Local verification passes; PR CI green
- Next milestone stub seeded after closeout only

## Suggested PR title

`docs(m12): audit scoring methodology and working-note criteria`

## Stop point

Stop after implementation, local verification, PR opened, PR CI green. Do not merge without owner approval.
