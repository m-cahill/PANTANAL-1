"""Tests that M03 Kaggle evidence is recorded honestly after manual run."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = REPO_ROOT / "docs" / "kaggle" / "m03_kaggle_evidence.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"

SAMPLE_PATH = "/kaggle/input/competitions/birdclef-2026/sample_submission.csv"


def test_m03_kaggle_evidence_file_exists() -> None:
    assert EVIDENCE_PATH.is_file()


def test_m03_kaggle_evidence_records_execution() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "REAL_SAMPLE_ZERO_BASELINE" in text
    assert "Executed" in text or "Interactive mode" in text
    assert "not yet executed" not in text.lower()


def test_m03_kaggle_evidence_records_sample_path() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert SAMPLE_PATH in text


def test_m03_kaggle_evidence_records_working_submission() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "/kaggle/working/submission.csv" in text
    assert "produced: **yes**" in text.lower() or "produced: yes" in text.lower()


def test_m03_kaggle_evidence_records_interactive_mode() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "Interactive" in text
    assert "DEF-002B" in text
    assert "Open" in text or "open" in text


def test_m03_kaggle_evidence_does_not_claim_leaderboard_score() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    for line in lines:
        if line.strip().startswith("- Public leaderboard score:"):
            value = line.split(":", 1)[1].strip()
            assert value.lower() in ("n/a", "none", ""), "must not record an actual score"
            return
    raise AssertionError("missing Public leaderboard score field")


def test_pantanal_1_def_002b_evidenced_after_m04() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    deferred = text.split("## 11. Deferred issues register", 1)[-1]
    assert "DEF-002B" in deferred
    assert "M04 (evidenced)" in deferred


def test_pantanal_1_def_003a_evidenced() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    deferred = text.split("## 11. Deferred issues register", 1)[-1]
    assert "DEF-003A" in deferred
    assert "evidenced" in deferred.lower() or "M03" in deferred
