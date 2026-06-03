"""Tests for Kaggle setup runbook and evidence template documentation."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNBOOK_PATH = REPO_ROOT / "docs" / "kaggle" / "kaggle_setup_runbook.md"
EVIDENCE_PATH = REPO_ROOT / "docs" / "kaggle" / "kaggle_setup_evidence.md"
NOTEBOOK_SMOKE_PATH = REPO_ROOT / "docs" / "kaggle" / "notebook_smoke.md"
PANTANAL_TRUTH_PATH = REPO_ROOT / "docs" / "pantanal-1.md"

RUNBOOK_NON_CLAIMS = (
    "does not prove kaggle execution",
    "does not prove submission eligibility",
    "does not prove real `sample_submission.csv` compatibility",
    "does not prove cpu 90-minute runtime compliance",
    "does not prove model inference",
    "does not prove leaderboard submission or score",
)

EVIDENCE_NOT_EXECUTED_MARKERS = (
    "not yet executed",
    "no evidence recorded",
)


def test_kaggle_setup_runbook_exists() -> None:
    assert RUNBOOK_PATH.is_file()


def test_kaggle_setup_evidence_template_exists() -> None:
    assert EVIDENCE_PATH.is_file()


def test_runbook_contains_required_non_claims() -> None:
    text = RUNBOOK_PATH.read_text(encoding="utf-8").lower()
    for phrase in RUNBOOK_NON_CLAIMS:
        assert phrase in text, f"missing runbook non-claim: {phrase}"


def test_evidence_template_status_not_yet_executed() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert any(marker in text for marker in EVIDENCE_NOT_EXECUTED_MARKERS)


def test_notebook_smoke_links_runbook_and_evidence() -> None:
    text = NOTEBOOK_SMOKE_PATH.read_text(encoding="utf-8")
    assert "kaggle_setup_runbook.md" in text
    assert "kaggle_setup_evidence.md" in text


def test_pantanal_truth_does_not_claim_kaggle_execution() -> None:
    text = PANTANAL_TRUTH_PATH.read_text(encoding="utf-8").lower()
    implemented, not_yet = text.split("**not yet proven:**", 1)
    implemented = implemented.split("**implemented:**", 1)[-1]
    assert "kaggle notebook execution in the kaggle cpu environment" in not_yet
    assert "kaggle notebook execution in the kaggle cpu environment" not in implemented


def test_pantanal_truth_keeps_def_002_open() -> None:
    text = PANTANAL_TRUTH_PATH.read_text(encoding="utf-8")
    assert "DEF-002" in text
    assert "live execution" in text.lower() or "Kaggle CPU" in text
    assert "recorded evidence" in text.lower()
