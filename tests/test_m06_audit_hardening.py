"""Tests for M06 audit-hardening docs, CI config, and honest claim boundaries."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
AUDIT_DOC = REPO_ROOT / "docs" / "quality" / "audit_hardening.md"
COVERAGERC = REPO_ROOT / ".coveragerc"
CI_WORKFLOW = REPO_ROOT / ".github" / "workflows" / "ci.yml"
REQUIREMENTS_DEV = REPO_ROOT / "requirements-dev.txt"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"


def test_audit_hardening_doc_exists() -> None:
    assert AUDIT_DOC.is_file()


def test_audit_doc_states_coverage_and_mypy_gates() -> None:
    text = AUDIT_DOC.read_text(encoding="utf-8").lower()
    assert "coverage" in text
    assert "mypy" in text
    assert "gate" in text or "gates" in text


def test_audit_doc_preserves_inference_and_submission_non_claims() -> None:
    text = AUDIT_DOC.read_text(encoding="utf-8").lower()
    assert "model inference" in text
    assert "kaggle submission" in text or "kaggle" in text


def test_coveragerc_exists() -> None:
    assert COVERAGERC.is_file()


def test_ci_workflow_mentions_mypy_on_src() -> None:
    text = CI_WORKFLOW.read_text(encoding="utf-8")
    assert "mypy src/pantanal_1" in text


def test_ci_workflow_mentions_coverage() -> None:
    text = CI_WORKFLOW.read_text(encoding="utf-8").lower()
    assert "pytest-cov" in text or "--cov=src/pantanal_1" in text
    assert "coverage report" in text


def test_requirements_dev_includes_mypy() -> None:
    text = REQUIREMENTS_DEV.read_text(encoding="utf-8").lower()
    assert "mypy" in text


def test_requirements_dev_includes_coverage_tooling() -> None:
    text = REQUIREMENTS_DEV.read_text(encoding="utf-8").lower()
    assert "pytest-cov" in text or "coverage" in text


def test_pantanal_marks_m06_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "M06" in text
    assert "in progress" in text.lower()


def test_pantanal_does_not_claim_inference_or_score_improvement() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    m06_section = text
    if "**M06 explicit non-claims:**" in text:
        m06_section = text.split("**M06 explicit non-claims:**", 1)[1]
    lower = m06_section.lower()
    assert "does not implement model inference" in lower or "not yet proven" in lower
    assert "improve leaderboard score" not in lower or "does not improve" in lower
