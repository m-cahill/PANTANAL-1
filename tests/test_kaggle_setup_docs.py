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

EVIDENCE_INTERACTIVE_MARKERS = (
    "interactive",
    "inline fallback",
    "tmp/submissions/m02_smoke_submission.csv",
    "def-002a",
)


def test_kaggle_setup_runbook_exists() -> None:
    assert RUNBOOK_PATH.is_file()


def test_kaggle_setup_evidence_template_exists() -> None:
    assert EVIDENCE_PATH.is_file()


def test_runbook_contains_required_non_claims() -> None:
    text = RUNBOOK_PATH.read_text(encoding="utf-8").lower()
    for phrase in RUNBOOK_NON_CLAIMS:
        assert phrase in text, f"missing runbook non-claim: {phrase}"


def test_evidence_records_interactive_smoke_success() -> None:
    raw = EVIDENCE_PATH.read_text(encoding="utf-8")
    text = raw.lower()
    for marker in EVIDENCE_INTERACTIVE_MARKERS:
        assert marker in text, f"missing evidence marker: {marker}"
    assert "tmp/submissions/m02_smoke_submission.csv`: **yes**" in raw
    assert "/kaggle/working/submission.csv`: **no**" in raw


def test_notebook_smoke_links_runbook_and_evidence() -> None:
    text = NOTEBOOK_SMOKE_PATH.read_text(encoding="utf-8")
    assert "kaggle_setup_runbook.md" in text
    assert "kaggle_setup_evidence.md" in text


def test_pantanal_truth_m04_scored_evidence_without_overclaiming() -> None:
    text = PANTANAL_TRUTH_PATH.read_text(encoding="utf-8")
    implemented = text.split("**Implemented:**", 1)[-1].split("**Not yet proven:**", 1)[0]
    assert "M04 Kaggle commit/scored evidence" in implemented
    assert "0.500" in implemented
    assert "model inference" in text.lower()
    assert "meaningful model quality" in text.lower() or "competitive" in text.lower()


def test_pantanal_truth_splits_def_002() -> None:
    text = PANTANAL_TRUTH_PATH.read_text(encoding="utf-8")
    assert "DEF-002A" in text
    assert "DEF-002B" in text
    assert "evidenced" in text.lower()
