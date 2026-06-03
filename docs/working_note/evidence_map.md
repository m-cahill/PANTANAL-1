# PANTANAL-1 Working Note — Evidence Map

**Authority:** Subordinate to `docs/pantanal-1.md` and [working_note_outline.md](working_note_outline.md).

**Purpose:** Map each working-note outline section to primary evidence sources, milestones, supported claims, and explicit limitations.

---

## Score interpretation (binding)

**Public score 0.500 supports scored pipeline acceptance only.**

It does **not** support predictive model quality.

---

## Primary evidence table

| Working note section | Evidence source | Milestone | Claim supported | Non-claim / limitation |
|----------------------|-----------------|-----------|-----------------|------------------------|
| 1. Introduction | `docs/pantanal-1.md` | M00+ | Public Kaggle-facing repo identity; governance-first posture | Does not prove model quality or CLEF readiness |
| 1. Introduction | `docs/analysis/post_competition_analysis.md` | M05 | Post-deadline context; what is proven vs not proven | Does not implement inference |
| 2. Repository Governance and Boundary Model | `docs/pantanal-1.md` | M00 | Ultimate Truth, boundaries, policies | RediAI certification not claimed |
| 2. Repository Governance and Boundary Model | `docs/milestones/M00/M00_summary.md` | M00 | Bootstrap governance scaffold | Not competition scoring proof |
| 3. Submission Contract Development | `docs/milestones/M01/M01_summary.md` | M01 | Synthetic 234-column, 5-second contract | No real Kaggle sample proof in M01 |
| 3. Submission Contract Development | `docs/kaggle/kaggle_submission_bible.md` | M01–M04 | Submission contract vocabulary and guardrails | Bible is guidance, not scored proof alone |
| 4. Kaggle Notebook Path | `docs/milestones/M02/M02_summary.md` | M02 | Interactive synthetic smoke path | No scored commit/submit; no public score |
| 4. Kaggle Notebook Path | `docs/kaggle/kaggle_submission_bible.md` | M02 | Kaggle setup and smoke expectations | Does not replace interactive evidence files |
| 4. Kaggle Notebook Path | `docs/milestones/M03/M03_summary.md` | M03 | Real `sample_submission.csv` discovery; interactive zero baseline | Interactive only — not scored |
| 4. Kaggle Notebook Path | `docs/analysis/M00_M04_evidence_index.md` | M03–M04 | Indexed Kaggle evidence chain | Index does not add new runtime proof |
| 4. Kaggle Notebook Path | `docs/kaggle/m04_commit_mode_evidence.md` | M04 | Commit/scored path; public score **0.500**; short runtime | **0.500 = pipeline acceptance, not model quality**; not competitive solution |
| 4. Kaggle Notebook Path | `docs/milestones/M04/M04_summary.md` | M04 | M04 scoped claims and non-claims | Preserves zero-baseline and non-competitive framing |
| 5. Audit Hardening | `docs/quality/audit_hardening.md` | M06 | Coverage + mypy gates; DEF-001 partial (M06) | Does not prove vulnerability-free stack |
| 5. Audit Hardening | `docs/milestones/M06/M06_summary.md` | M06 | M06 audit-hardening milestone closure | No model inference |
| 5. Audit Hardening | `docs/quality/security_supply_chain.md` | M07 | Bandit + pip-audit; DEF-001 substantially addressed | SBOM/pinning not implemented |
| 5. Audit Hardening | `docs/milestones/M07/M07_summary.md` | M07 | M07 security gate closure | Does not prove vulnerability-free |
| 6. Results | `docs/kaggle/m04_commit_mode_evidence.md` | M04 | Scored acceptance; public **0.500** | **Not predictive model quality** |
| 6. Results | `docs/analysis/post_competition_analysis.md` | M05 | Interprets 0.500 as pipeline evidence | Does not improve score |
| 6. Results | `docs/pantanal-1.md` | M04+ | Ultimate Truth scored-path claim | Working-note readiness not claimed |
| 7. Limitations | `docs/pantanal-1.md` | M00–M07 | Explicit non-claims register | Authoritative limitation list |
| 7. Limitations | `docs/analysis/post_competition_analysis.md` | M05 | Gap analysis (inference, competitiveness) | Planning doc only |
| 8. Future Work | `docs/analysis/next_milestone_decision_matrix.md` | M05 | M08 vs M08A and deferred directions | Recommendations, not commitments |
| 8. Future Work | `docs/milestones/M05/M05_summary.md` | M05 | Post-competition planning closure | No inference implemented |
| Evidence Appendix (cross-milestone) | `docs/analysis/M00_M04_evidence_index.md` | M00–M04 | Consolidated early evidence index | Stops at M04; M05–M07 in summaries/quality docs |

---

## Secondary Audit Sources

Milestone **audits** support audit posture, milestone score trends, and governance discipline. They are **secondary** evidence — not substitutes for Kaggle runtime evidence, Ultimate Truth, or milestone summaries.

| Audit file | Milestone | Typical use in narrative |
|------------|-----------|--------------------------|
| `docs/milestones/M00/M00_audit.md` | M00 | Bootstrap and governance audit posture |
| `docs/milestones/M01/M01_audit.md` | M01 | Contract milestone audit posture |
| `docs/milestones/M02/M02_audit.md` | M02 | Smoke notebook milestone audit posture |
| `docs/milestones/M03/M03_audit.md` | M03 | Baseline notebook milestone audit posture |
| `docs/milestones/M04/M04_audit.md` | M04 | Commit-mode probe audit posture |
| `docs/milestones/M05/M05_audit.md` | M05 | Planning milestone audit posture |
| `docs/milestones/M06/M06_audit.md` | M06 | Coverage/mypy hardening audit posture |
| `docs/milestones/M07/M07_audit.md` | M07 | Security/supply-chain gate audit posture |

Do not cite audits alone to justify public score **0.500**, real Kaggle execution, or model quality. Pair audit references with primary sources (e.g. `docs/kaggle/m04_commit_mode_evidence.md`, `docs/pantanal-1.md`).
