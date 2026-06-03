"""Tests for M05 post-competition analysis docs and honest claim boundaries."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_PATH = REPO_ROOT / "docs" / "analysis" / "post_competition_analysis.md"
MATRIX_PATH = REPO_ROOT / "docs" / "analysis" / "next_milestone_decision_matrix.md"
INDEX_PATH = REPO_ROOT / "docs" / "analysis" / "M00_M04_evidence_index.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"

M06_CANDIDATES = (
    "M06A",
    "M06B",
    "M06C",
    "M06D",
    "M06E",
    "real inference",
    "audit hardening",
    "Kaggle packaging",
    "working-note",
    "archive",
    "template",
)


def test_post_competition_analysis_exists() -> None:
    assert ANALYSIS_PATH.is_file()


def test_analysis_mentions_public_score_0_500() -> None:
    assert "0.500" in ANALYSIS_PATH.read_text(encoding="utf-8")


def test_analysis_score_proves_pipeline_not_model_quality() -> None:
    text = ANALYSIS_PATH.read_text(encoding="utf-8").lower()
    assert "pipeline" in text and "accepted" in text or "scored" in text
    assert "not" in text and ("predictive" in text or "model quality" in text)


def test_analysis_preserves_inference_and_quality_non_claims() -> None:
    text = ANALYSIS_PATH.read_text(encoding="utf-8").lower()
    assert "model inference" in text
    assert "competitive" in text or "useful" in text
    assert "not proven" in text or "what is not proven" in text


def test_decision_matrix_exists() -> None:
    assert MATRIX_PATH.is_file()


def test_matrix_includes_all_candidate_directions() -> None:
    text = MATRIX_PATH.read_text(encoding="utf-8")
    for token in M06_CANDIDATES:
        assert token.lower() in text.lower(), f"missing candidate token: {token}"


def test_matrix_includes_recommendation() -> None:
    text = MATRIX_PATH.read_text(encoding="utf-8")
    assert "recommendation" in text.lower()
    assert "M06B" in text
    assert "M06A" in text


def test_evidence_index_exists() -> None:
    assert INDEX_PATH.is_file()


def test_pantanal_1_marks_m05_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    m05_row = ledger.split("| M05 |", 1)[-1].split("\n", 1)[0]
    assert "in progress" in m05_row.lower()


def test_pantanal_1_does_not_claim_model_inference() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    claims = text.split("## 8. current claims", 1)[-1].split("## 9.", 1)[0]
    assert "implements model inference" not in claims
    assert "model inference implemented" not in claims
    if "m05" in claims:
        m05_block = claims.split("m05", 1)[-1][:800]
        assert "implements model inference" not in m05_block


def test_pantanal_1_does_not_claim_improved_score() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "improved score" not in text
    assert "improve leaderboard" not in text or "m05 does not improve" in text
