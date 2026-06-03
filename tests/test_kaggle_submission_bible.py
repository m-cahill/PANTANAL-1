"""Tests for Kaggle submission bible and cross-doc alignment."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BIBLE_PATH = REPO_ROOT / "docs" / "kaggle" / "kaggle_submission_bible.md"
NOTEBOOK_SMOKE_PATH = REPO_ROOT / "docs" / "kaggle" / "notebook_smoke.md"
PANTANAL_TRUTH_PATH = REPO_ROOT / "docs" / "pantanal-1.md"
NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "pantanal_1_m02_smoke.ipynb"
EVIDENCE_PATH = REPO_ROOT / "docs" / "kaggle" / "kaggle_setup_evidence.md"

BIBLE_REQUIRED_PHRASES = (
    "/kaggle/input",
    "/kaggle/working/submission.csv",
    "interactive",
    "commit",
    "submit",
    "debug output",
    "sys.path",
    "kaggle_kernel_run_type",
    "prohibited claims",
    "def-002a",
    "def-002b",
    "tmp/submissions",
)

NOTEBOOK_DEBUG_FROM_BIBLE = (
    "KAGGLE_KERNEL_RUN_TYPE",
    "/kaggle/input",
    "/kaggle/working",
    "=== PANTANAL-1 M02 Kaggle Smoke Debug ===",
)


def test_kaggle_submission_bible_exists() -> None:
    assert BIBLE_PATH.is_file()


def test_bible_mentions_kaggle_input() -> None:
    assert "/kaggle/input" in BIBLE_PATH.read_text(encoding="utf-8")


def test_bible_mentions_working_submission_csv() -> None:
    assert "/kaggle/working/submission.csv" in BIBLE_PATH.read_text(encoding="utf-8")


def test_bible_distinguishes_interactive_and_commit_modes() -> None:
    text = BIBLE_PATH.read_text(encoding="utf-8").lower()
    assert "interactive" in text
    assert "commit" in text or "submit" in text


def test_bible_contains_dependency_rules() -> None:
    text = BIBLE_PATH.read_text(encoding="utf-8").lower()
    assert "dependency" in text
    assert "pandas" in text or "torch" in text or "librosa" in text


def test_bible_contains_debug_output_expectations() -> None:
    text = BIBLE_PATH.read_text(encoding="utf-8").lower()
    assert "debug" in text
    assert "python version" in text or "python" in text
    assert "kaggle_kernel_run_type" in text


def test_bible_contains_prohibited_claims_without_evidence() -> None:
    text = BIBLE_PATH.read_text(encoding="utf-8").lower()
    assert "prohibited" in text or "do not claim" in text
    assert "leaderboard" in text


def test_notebook_smoke_references_bible() -> None:
    assert "kaggle_submission_bible.md" in NOTEBOOK_SMOKE_PATH.read_text(encoding="utf-8")


def test_pantanal_truth_references_bible_or_m02_interactive_evidence() -> None:
    text = PANTANAL_TRUTH_PATH.read_text(encoding="utf-8")
    assert "kaggle_submission_bible.md" in text or "interactive" in text.lower()
    assert "DEF-002A" in text
    assert "DEF-002B" in text


def test_m02_notebook_contains_bible_debug_strings() -> None:
    notebook_text = NOTEBOOK_PATH.read_text(encoding="utf-8")
    for snippet in NOTEBOOK_DEBUG_FROM_BIBLE:
        assert snippet in notebook_text, f"missing notebook debug snippet: {snippet}"


def test_evidence_records_interactive_success() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "interactive" in text
    assert "inline fallback" in text
    assert "tmp/submissions/m02_smoke_submission.csv" in text
    assert "28134" in text
