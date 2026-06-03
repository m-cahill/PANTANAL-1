"""Tests that M03 Kaggle evidence template exists and remains honest (pre-execution)."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = REPO_ROOT / "docs" / "kaggle" / "m03_kaggle_evidence.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"


def test_m03_kaggle_evidence_file_exists() -> None:
    assert EVIDENCE_PATH.is_file()


def test_m03_kaggle_evidence_not_yet_executed() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "not yet executed" in text or "awaiting owner manual kaggle run" in text


def test_m03_kaggle_evidence_contains_baseline_modes() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "REAL_SAMPLE_ZERO_BASELINE" in text
    assert "SYNTHETIC_FALLBACK_ONLY" in text


def test_m03_kaggle_evidence_contains_scored_submission_path() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "/kaggle/working/submission.csv" in text


def test_m03_kaggle_evidence_asks_for_exact_sample_path() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "exact sample path" in text


def test_m03_kaggle_evidence_does_not_claim_leaderboard_score() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "Public leaderboard score:" in text
    lines = text.splitlines()
    for line in lines:
        if line.strip().startswith("- Public leaderboard score:"):
            value = line.split(":", 1)[1].strip()
            assert value == "", "must not record a score before manual run"
            break
    else:
        raise AssertionError("missing Public leaderboard score field")


def test_pantanal_1_keeps_def_002b_open() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "DEF-002B" in text
    assert "DEF-002B" in text and (
        "remains open" in text.lower() or "not yet proven" in text.lower() or "open" in text.lower()
    )


def test_pantanal_1_keeps_def_003_open() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "DEF-003" in text
    deferred_section = text.split("## 11. Deferred issues register", 1)[-1]
    assert "DEF-003" in deferred_section
