"""
M16C Working-Note Draft v0 / Final Evidence Lock governance tests.

Tests that M16C is documentation/evidence consolidation only:
- Working-note draft, evidence lock, submission decision exist
- Baseline scores 0.500 recorded; M04 recommended for final selection
- No model quality, score improvement, G1-G4, RediAI, or CLEF-ready claims
- No notebook changes, deps, ingest, or training
"""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
MILESTONES = DOCS / "milestones"
ANALYSIS = DOCS / "analysis"
WORKING_NOTE = DOCS / "working_note"
NOTEBOOKS = REPO_ROOT / "notebooks"


class TestM16cDocumentsExist:
    """M16C required documents exist."""

    def test_working_note_draft_exists(self) -> None:
        path = WORKING_NOTE / "M16_working_note_draft_v0.md"
        assert path.exists(), f"Missing {path}"

    def test_final_evidence_lock_exists(self) -> None:
        path = WORKING_NOTE / "M16_final_evidence_lock.md"
        assert path.exists(), f"Missing {path}"

    def test_final_submission_decision_exists(self) -> None:
        path = ANALYSIS / "M16_final_submission_decision.md"
        assert path.exists(), f"Missing {path}"

    def test_m16_plan_exists(self) -> None:
        path = MILESTONES / "M16" / "M16_plan.md"
        assert path.exists(), f"Missing {path}"
        content = path.read_text(encoding="utf-8").lower()
        assert "m16c" in content or "working-note" in content


class TestM16cWorkingNoteDraftContent:
    """Working-note draft v0 has required sections."""

    def test_draft_has_title_and_abstract(self) -> None:
        content = WORKING_NOTE / "M16_working_note_draft_v0.md"
        text = content.read_text(encoding="utf-8").lower()
        assert "title" in text or "## title" in text
        assert "abstract" in text

    def test_draft_records_baseline_scores(self) -> None:
        text = WORKING_NOTE / "M16_working_note_draft_v0.md"
        content = text.read_text(encoding="utf-8")
        assert "0.500" in content
        assert "m04" in content.lower() or "all-zero" in content.lower()
        assert "m11" in content.lower() or "uniform" in content.lower() or "ε" in content

    def test_draft_records_scoring_interpretation(self) -> None:
        text = WORKING_NOTE / "M16_working_note_draft_v0.md"
        content = text.read_text(encoding="utf-8").lower()
        assert "constant" in content or "ranking" in content
        assert "0.500" in content

    def test_draft_has_methodology_timeline(self) -> None:
        text = WORKING_NOTE / "M16_working_note_draft_v0.md"
        content = text.read_text(encoding="utf-8")
        for m in ("M00", "M04", "M11", "M15"):
            assert m in content, f"Timeline must reference {m}"

    def test_draft_does_not_claim_clef_ready(self) -> None:
        text = WORKING_NOTE / "M16_working_note_draft_v0.md"
        content = text.read_text(encoding="utf-8").lower()
        assert "not clef submission-ready" in content or "not cleft submission-ready" in content
        assert "is clef-ready" not in content
        assert "clef submission-ready" not in content.replace("not clef submission-ready", "")


class TestM16cFinalEvidenceLockContent:
    """Final evidence lock has required content."""

    def test_lock_has_proven_and_not_proven(self) -> None:
        text = WORKING_NOTE / "M16_final_evidence_lock.md"
        content = text.read_text(encoding="utf-8").lower()
        assert "what is proven" in content or "proven" in content
        assert "not proven" in content

    def test_lock_has_post_deadline_options(self) -> None:
        text = WORKING_NOTE / "M16_final_evidence_lock.md"
        content = text.read_text(encoding="utf-8").lower()
        assert "post-deadline" in content or "post deadline" in content
        assert "m16a" in content or "private-lane" in content


class TestM16cFinalSubmissionDecision:
    """Final submission decision memo content."""

    def test_recommends_m04_zero_baseline(self) -> None:
        path = ANALYSIS / "M16_final_submission_decision.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "pantanal_1_m03_baseline" in content
        assert "version 2" in content or "version **2**" in path.read_text(encoding="utf-8").lower()
        assert "0.500" in content
        assert "m04" in content

    def test_notes_m11_no_improvement(self) -> None:
        path = ANALYSIS / "M16_final_submission_decision.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "m11" in content
        assert "0.500" in content
        assert "no improvement" in content or "no evidenced reason" in content

    def test_no_new_kaggle_packaging_in_m16c(self) -> None:
        path = ANALYSIS / "M16_final_submission_decision.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "no new kaggle packaging in m16c" in content
        assert "modify kaggle notebooks" in content
        assert "not" in content

    def test_no_private_lane_bundle(self) -> None:
        path = ANALYSIS / "M16_final_submission_decision.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "no owner-supplied" in content or "not been ingested" in content


class TestM16cNoProhibitedClaims:
    """M16C docs must not make prohibited claims."""

    @pytest.fixture
    def m16_docs_text(self) -> str:
        paths = [
            WORKING_NOTE / "M16_working_note_draft_v0.md",
            WORKING_NOTE / "M16_final_evidence_lock.md",
            ANALYSIS / "M16_final_submission_decision.md",
            MILESTONES / "M16" / "M16_plan.md",
        ]
        return "\n".join(p.read_text(encoding="utf-8").lower() for p in paths)

    def test_no_score_improvement_claim(self, m16_docs_text: str) -> None:
        assert "score improved" not in m16_docs_text
        assert "leaderboard improvement" not in m16_docs_text
        assert "improve score" not in m16_docs_text.replace("does not improve", "")

    def test_no_model_quality_claim(self, m16_docs_text: str) -> None:
        assert (
            "does not prove model quality" in m16_docs_text
            or "not prove model quality" in m16_docs_text
        )
        assert "proves model quality" not in m16_docs_text

    def test_no_g1_g2_g3_g4_claim(self, m16_docs_text: str) -> None:
        assert "g1 evidence exists" not in m16_docs_text
        assert "claims g1" not in m16_docs_text
        assert "satisfies g1" not in m16_docs_text
        assert "g4 satisfied" not in m16_docs_text

    def test_no_rediai_claim(self, m16_docs_text: str) -> None:
        assert "rediai certification" in m16_docs_text
        assert "claims rediai" not in m16_docs_text


class TestM16cNoProhibitedArtifacts:
    """M16C did not add prohibited artifacts."""

    def test_no_model_weights(self) -> None:
        for ext in (".pt", ".onnx", ".h5", ".pkl", ".pth"):
            matches = [
                w
                for w in REPO_ROOT.rglob(f"*{ext}")
                if ".git" not in str(w) and "venv" not in str(w).lower()
            ]
            assert not matches, f"Found weights: {matches}"

    def test_no_ml_deps_in_requirements(self) -> None:
        for req in ("requirements.txt", "requirements-dev.txt"):
            path = REPO_ROOT / req
            if path.exists():
                content = path.read_text(encoding="utf-8").lower()
                for dep in ("torch", "librosa", "tensorflow"):
                    assert dep not in content


class TestM16cUltimateTruth:
    """pantanal-1.md records M16."""

    def test_pantanal_mentions_m16(self) -> None:
        truth = DOCS / "pantanal-1.md"
        content = truth.read_text(encoding="utf-8")
        assert "M16" in content

    def test_pantanal_m16_in_ledger(self) -> None:
        truth = DOCS / "pantanal-1.md"
        content = truth.read_text(encoding="utf-8")
        assert "| M16 |" in content

    def test_pantanal_m16_ledger_recorded(self) -> None:
        truth = DOCS / "pantanal-1.md"
        content = truth.read_text(encoding="utf-8").lower()
        assert "m16" in content
        # Milestone ledger row (not artifacts table)
        idx = content.find("| m16 | working-note")
        assert idx != -1, "M16 ledger row not found"
        section = content[idx : idx + 200]
        assert "in progress" in section or "closed" in section

    def test_pantanal_m16_non_claims(self) -> None:
        truth = DOCS / "pantanal-1.md"
        content = truth.read_text(encoding="utf-8")
        assert "**M16 explicit non-claims:**" in content
        m16_section = content.split("**M16 explicit non-claims:**")[1][:1200]
        assert "does not train" in m16_section.lower()
        assert "does not submit" in m16_section.lower()
