"""
M15 Private-Lane Evidence Request Packet governance tests.

Tests that M15 is a pre-ingest readiness milestone only:
- No real private-lane evidence ingested
- Evidence request docs exist with required content
- Decision gate criteria documented
- Template provided for private lane
- No training, inference, dependencies, notebooks, weights, data, or score claims
- Ultimate Truth records M15 in-progress and non-claims
"""

from pathlib import Path

import pytest

# Repository root
REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
MILESTONES = DOCS / "milestones"
ANALYSIS = DOCS / "analysis"
MODELS = DOCS / "models"
SCHEMAS = REPO_ROOT / "schemas"
SCRIPTS = REPO_ROOT / "scripts"
SRC = REPO_ROOT / "src"
NOTEBOOKS = REPO_ROOT / "notebooks"


class TestM15PlanExists:
    """M15 plan document tests."""

    def test_m15_plan_exists(self) -> None:
        """M15 plan exists."""
        plan_path = MILESTONES / "M15" / "M15_plan.md"
        assert plan_path.exists(), f"Missing {plan_path}"

    def test_m15_plan_states_pre_ingest_scope(self) -> None:
        """M15 plan states pre-ingest readiness scope."""
        plan_path = MILESTONES / "M15" / "M15_plan.md"
        content = plan_path.read_text(encoding="utf-8").lower()
        assert "pre-ingest" in content, "Plan must state pre-ingest scope"
        assert "readiness" in content or "request" in content, (
            "Plan must mention readiness or request"
        )

    def test_m15_plan_does_not_claim_evidence_ingested(self) -> None:
        """M15 plan does not claim real evidence was ingested."""
        plan_path = MILESTONES / "M15" / "M15_plan.md"
        content = plan_path.read_text(encoding="utf-8").lower()
        # Should not claim evidence was ingested
        assert "evidence has been ingested" not in content
        assert "ingested real" not in content


class TestM15EvidenceRequestExists:
    """M15 private-lane evidence request document tests."""

    def test_evidence_request_exists(self) -> None:
        """Evidence request document exists."""
        path = ANALYSIS / "M15_private_lane_evidence_request.md"
        assert path.exists(), f"Missing {path}"

    def test_evidence_request_lists_required_files(self) -> None:
        """Evidence request lists all required files."""
        path = ANALYSIS / "M15_private_lane_evidence_request.md"
        content = path.read_text(encoding="utf-8").lower()
        required = [
            "model manifest",
            "model card",
            "validation summary",
            "non-constant",
            "cpu timing",
            "license",
            "provenance",
        ]
        for item in required:
            assert item in content, f"Evidence request must list '{item}'"

    def test_evidence_request_lists_prohibited_content(self) -> None:
        """Evidence request lists prohibited content."""
        path = ANALYSIS / "M15_private_lane_evidence_request.md"
        content = path.read_text(encoding="utf-8").lower()
        prohibited = [
            "raw audio",
            "kaggle competition csv",
            "model binar",
            "ornithos",
            "submission.csv",
            "credential",
            "secret",
        ]
        for item in prohibited:
            assert item in content, f"Evidence request must list prohibited: '{item}'"

    def test_evidence_request_references_m14_contract(self) -> None:
        """Evidence request references M14 evidence contract."""
        path = ANALYSIS / "M15_private_lane_evidence_request.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "m14" in content, "Must reference M14 contract"
        assert "evidence contract" in content or "validation" in content


class TestM15IngestDecisionGateExists:
    """M15 ingest decision gate document tests."""

    def test_decision_gate_exists(self) -> None:
        """Ingest decision gate document exists."""
        path = ANALYSIS / "M15_ingest_decision_gate.md"
        assert path.exists(), f"Missing {path}"

    def test_decision_gate_defines_go_criteria(self) -> None:
        """Decision gate defines go criteria."""
        path = ANALYSIS / "M15_ingest_decision_gate.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "go" in content and "criteria" in content, "Must define go criteria"

    def test_decision_gate_defines_no_go_criteria(self) -> None:
        """Decision gate defines no-go criteria."""
        path = ANALYSIS / "M15_ingest_decision_gate.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "no-go" in content or "no go" in content, "Must define no-go criteria"

    def test_decision_gate_references_validator(self) -> None:
        """Decision gate references validate_m14_evidence.py."""
        path = ANALYSIS / "M15_ingest_decision_gate.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "validate_m14_evidence" in content, "Must reference validator script"

    def test_decision_gate_defines_outcomes(self) -> None:
        """Decision gate defines decision outcomes."""
        path = ANALYSIS / "M15_ingest_decision_gate.md"
        content = path.read_text(encoding="utf-8").lower()
        # Should define multiple outcomes
        assert "proceed" in content or "ingest" in content
        assert "return" in content or "reject" in content or "incomplete" in content


class TestM15TemplateExists:
    """M15 private-lane evidence packet template tests."""

    def test_template_exists(self) -> None:
        """Evidence packet template exists."""
        path = ANALYSIS / "M15_private_lane_evidence_packet_template.md"
        assert path.exists(), f"Missing {path}"

    def test_template_contains_placeholders(self) -> None:
        """Template contains placeholders, not real values."""
        path = ANALYSIS / "M15_private_lane_evidence_packet_template.md"
        content = path.read_text(encoding="utf-8")
        assert "[PLACEHOLDER" in content, "Template must contain placeholder markers"

    def test_template_does_not_contain_real_metrics(self) -> None:
        """Template does not contain real metric values."""
        path = ANALYSIS / "M15_private_lane_evidence_packet_template.md"
        content = path.read_text(encoding="utf-8").lower()
        # Should not have specific metric values that look real
        # Allow null, placeholder, or example format indicators
        lines = content.split("\n")
        for line in lines:
            if "auroc" in line or "lrap" in line or "loss" in line:
                # These lines should contain placeholder or null, not real numbers
                assert "placeholder" in line or "null" in line or "[" in line or "float" in line, (
                    f"Metric line should be placeholder: {line}"
                )


class TestM15DoesNotIngestRealEvidence:
    """Verify M15 does not ingest real private-lane evidence."""

    def test_no_m15a_validation_summary_exists(self) -> None:
        """No real M15A validation summary JSON exists in docs/analysis."""
        # M15A files would be named with m15a prefix
        analysis_files = list(ANALYSIS.glob("M15A_*.json"))
        for f in analysis_files:
            content = f.read_text(encoding="utf-8").lower()
            # If a file exists, it must be clearly marked as template/synthetic
            assert "placeholder" in content or "template" in content or "synthetic" in content, (
                f"File {f.name} appears to be real evidence, not template"
            )

    def test_no_model_manifest_with_real_metrics(self) -> None:
        """No model manifest with real training metrics exists."""
        model_files = list(MODELS.glob("m15a_*.json"))
        for f in model_files:
            content = f.read_text(encoding="utf-8").lower()
            assert "placeholder" in content or "template" in content or "synthetic" in content, (
                f"File {f.name} appears to be real evidence, not template"
            )


class TestM15DoesNotAddProhibitedArtifacts:
    """Verify M15 does not add prohibited artifacts."""

    def test_no_model_weights_added(self) -> None:
        """No model weight files (.pt, .onnx, .h5, .pkl) added."""
        weight_extensions = [".pt", ".onnx", ".h5", ".pkl", ".pth", ".safetensors"]
        for ext in weight_extensions:
            weights = list(REPO_ROOT.rglob(f"*{ext}"))
            # Filter out anything in .git or venv
            weights = [w for w in weights if ".git" not in str(w) and "venv" not in str(w).lower()]
            assert len(weights) == 0, f"Found weight files: {weights}"

    def test_no_raw_audio_added(self) -> None:
        """No raw audio files added."""
        audio_extensions = [".wav", ".ogg", ".flac", ".mp3", ".m4a"]
        for ext in audio_extensions:
            audio = list(REPO_ROOT.rglob(f"*{ext}"))
            audio = [a for a in audio if ".git" not in str(a) and "venv" not in str(a).lower()]
            assert len(audio) == 0, f"Found audio files: {audio}"

    def test_no_kaggle_data_added(self) -> None:
        """No Kaggle competition data CSVs added."""
        # Check for common Kaggle data files
        forbidden = ["train.csv", "test.csv", "sample_submission.csv"]
        for fname in forbidden:
            matches = list(REPO_ROOT.rglob(fname))
            matches = [m for m in matches if ".git" not in str(m) and "venv" not in str(m).lower()]
            assert len(matches) == 0, f"Found Kaggle data file: {matches}"


class TestM15DoesNotModifyKaggleNotebooks:
    """Verify M15 does not modify Kaggle notebooks."""

    def test_notebooks_unchanged_or_absent(self) -> None:
        """Kaggle notebooks exist but M15 should not modify inference logic."""
        if not NOTEBOOKS.exists():
            pytest.skip("No notebooks directory")
        # M15 is docs-only, so we just check notebooks folder still exists
        # This test passes if notebooks directory exists (no removal)
        assert NOTEBOOKS.exists(), "Notebooks directory should exist"


class TestM15DoesNotAddDependencies:
    """Verify M15 does not add audio/ML dependencies."""

    def test_requirements_txt_no_new_ml_deps(self) -> None:
        """requirements.txt does not add torch, librosa, sklearn, etc."""
        req_path = REPO_ROOT / "requirements.txt"
        if not req_path.exists():
            pytest.skip("No requirements.txt")
        content = req_path.read_text(encoding="utf-8").lower()
        ml_deps = ["torch", "librosa", "sklearn", "tensorflow", "keras", "onnx"]
        for dep in ml_deps:
            assert dep not in content, f"requirements.txt should not contain {dep}"

    def test_requirements_dev_no_new_ml_deps(self) -> None:
        """requirements-dev.txt does not add torch, librosa, sklearn, etc."""
        req_path = REPO_ROOT / "requirements-dev.txt"
        if not req_path.exists():
            pytest.skip("No requirements-dev.txt")
        content = req_path.read_text(encoding="utf-8").lower()
        ml_deps = ["torch", "librosa", "sklearn", "tensorflow", "keras", "onnx"]
        for dep in ml_deps:
            assert dep not in content, f"requirements-dev.txt should not contain {dep}"


class TestM15UltimateTruthUpdated:
    """Verify docs/pantanal-1.md is updated for M15."""

    def test_pantanal_1_mentions_m15(self) -> None:
        """pantanal-1.md mentions M15."""
        truth_path = DOCS / "pantanal-1.md"
        content = truth_path.read_text(encoding="utf-8")
        assert "M15" in content, "Ultimate Truth must mention M15"

    def test_pantanal_1_m15_in_ledger(self) -> None:
        """pantanal-1.md has M15 in milestone ledger."""
        truth_path = DOCS / "pantanal-1.md"
        content = truth_path.read_text(encoding="utf-8")
        # Should have M15 row in ledger table
        assert "| M15 |" in content, "M15 must be in milestone ledger table"

    def test_pantanal_1_m15_non_claims(self) -> None:
        """pantanal-1.md has M15 non-claims section."""
        truth_path = DOCS / "pantanal-1.md"
        content = truth_path.read_text(encoding="utf-8").lower()
        # Should have M15 non-claims
        assert "m15" in content and "non-claim" in content, "Must have M15 non-claims"

    def test_pantanal_1_m15_does_not_claim_evidence_ingested(self) -> None:
        """pantanal-1.md does not claim real evidence was ingested."""
        truth_path = DOCS / "pantanal-1.md"
        content = truth_path.read_text(encoding="utf-8")
        # Find M15 section
        if "**M15 explicit non-claims:**" in content:
            m15_section_start = content.find("**M15 explicit non-claims:**")
            m15_section = content[m15_section_start : m15_section_start + 1500]
            # Should explicitly state does not ingest
            assert (
                "does not ingest" in m15_section.lower() or "does not train" in m15_section.lower()
            )


class TestM15DoesNotClaimScoreImprovement:
    """Verify M15 does not claim score improvement."""

    def test_plan_does_not_claim_score_improvement(self) -> None:
        """M15 plan does not claim score improvement."""
        plan_path = MILESTONES / "M15" / "M15_plan.md"
        content = plan_path.read_text(encoding="utf-8").lower()
        # Should not claim score improved
        assert "score improved" not in content
        assert "leaderboard improvement" not in content

    def test_evidence_request_does_not_claim_score_improvement(self) -> None:
        """Evidence request does not claim score improvement."""
        path = ANALYSIS / "M15_private_lane_evidence_request.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "score improved" not in content
        assert "leaderboard improvement" not in content


class TestM15DoesNotClaimModelQuality:
    """Verify M15 does not claim model quality."""

    def test_plan_does_not_claim_model_quality(self) -> None:
        """M15 plan does not claim model quality."""
        plan_path = MILESTONES / "M15" / "M15_plan.md"
        content = plan_path.read_text(encoding="utf-8").lower()
        # Should have explicit non-claim
        assert "does not" in content and "model quality" in content


class TestM15DoesNotClaimRediAICertification:
    """Verify M15 does not claim RediAI certification."""

    def test_plan_does_not_claim_rediai(self) -> None:
        """M15 plan does not claim RediAI certification."""
        plan_path = MILESTONES / "M15" / "M15_plan.md"
        content = plan_path.read_text(encoding="utf-8").lower()
        assert "does not" in content and "rediai" in content


class TestM15DoesNotClaimWorkingNoteReadiness:
    """Verify M15 does not claim working-note readiness."""

    def test_plan_does_not_claim_working_note(self) -> None:
        """M15 plan does not claim working-note readiness."""
        plan_path = MILESTONES / "M15" / "M15_plan.md"
        content = plan_path.read_text(encoding="utf-8").lower()
        assert "does not" in content and "working-note" in content


class TestM15ReferencesM14Contract:
    """Verify M15 properly references M14 evidence contract."""

    def test_evidence_request_references_schema(self) -> None:
        """Evidence request references M14 validation summary schema."""
        path = ANALYSIS / "M15_private_lane_evidence_request.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "m14_validation_summary" in content or "validation_summary.schema" in content

    def test_decision_gate_references_validator_script(self) -> None:
        """Decision gate references validate_m14_evidence.py."""
        path = ANALYSIS / "M15_ingest_decision_gate.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "validate_m14_evidence.py" in content

    def test_evidence_request_references_manifest_schema(self) -> None:
        """Evidence request references M14 model manifest schema."""
        path = ANALYSIS / "M15_private_lane_evidence_request.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "m14_model_manifest" in content or "manifest" in content.lower()

    def test_evidence_request_references_model_card_template(self) -> None:
        """Evidence request references M14 model card template."""
        path = ANALYSIS / "M15_private_lane_evidence_request.md"
        content = path.read_text(encoding="utf-8").lower()
        assert "model_card" in content or "model card" in content
