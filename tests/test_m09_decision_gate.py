"""Tests for M09 working-note draft decision gate, readiness checklist, and M10 recommendation."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DECISION_GATE_PATH = REPO_ROOT / "docs" / "working_note" / "draft_decision_gate.md"
CHECKLIST_PATH = REPO_ROOT / "docs" / "working_note" / "draft_readiness_checklist.md"
RECOMMENDATION_PATH = REPO_ROOT / "docs" / "analysis" / "M09_next_direction_recommendation.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"

M10_OPTION_MARKERS = (
    "M10A",
    "M10B",
    "M10C",
)


def test_draft_decision_gate_exists() -> None:
    assert DECISION_GATE_PATH.is_file()


def test_draft_readiness_checklist_exists() -> None:
    assert CHECKLIST_PATH.is_file()


def test_m09_next_direction_recommendation_exists() -> None:
    assert RECOMMENDATION_PATH.is_file()


def test_decision_gate_states_not_full_draft() -> None:
    text = DECISION_GATE_PATH.read_text(encoding="utf-8").lower()
    assert "decision gate only" in text
    assert "not a full working-note draft" in text or "not a full working note" in text


def test_decision_gate_includes_draft_inference_archive_options() -> None:
    text = DECISION_GATE_PATH.read_text(encoding="utf-8")
    for marker in M10_OPTION_MARKERS:
        assert marker in text, f"missing option: {marker}"
    lower = text.lower()
    assert "working-note draft" in lower or "full working-note draft" in lower
    assert "inference" in lower
    assert "archive" in lower or "template" in lower


def test_checklist_states_not_working_note_ready() -> None:
    text = CHECKLIST_PATH.read_text(encoding="utf-8")
    assert "PANTANAL-1 is not working-note ready until a full draft exists and is reviewed." in text


def test_recommendation_primary_m10b_inference_spike() -> None:
    text = RECOMMENDATION_PATH.read_text(encoding="utf-8")
    assert "M10B" in text
    assert (
        "Real inference baseline spike" in text or "real inference baseline spike" in text.lower()
    )
    primary_idx = text.lower().find("primary")
    m10b_idx = text.find("M10B")
    assert primary_idx != -1 and m10b_idx != -1
    assert (
        m10b_idx < text.lower().find("secondary", primary_idx)
        or "primary" in text[: m10b_idx + 200]
    )


def test_recommendation_preserves_competitive_model_non_claims() -> None:
    text = RECOMMENDATION_PATH.read_text(encoding="utf-8").lower()
    assert "competitive model" in text or "competitive" in text
    assert "not claim" in text or "do not claim" in text
    assert "predictive model quality" in text or "model quality" in text


def test_pantanal_marks_m09_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1]
    assert "| M09 |" in ledger
    assert "in progress" in ledger.lower()


def test_pantanal_does_not_claim_model_inference() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    claims = text.split("## 8. current claims", 1)[-1]
    implemented = claims.split("**not yet proven:**", 1)[0]
    assert "implements model inference" not in implemented
    assert "implemented model inference" not in implemented
    assert "m09 does not implement model inference" in text or "not yet proven" in text


def test_pantanal_does_not_claim_working_note_readiness() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "working-note readiness" in text or "working note readiness" in text
    assert "m09 does not make the project clef submission-ready" in text or (
        "not yet proven" in text and "working note readiness" in text
    )


def test_pantanal_does_not_claim_rediai_certification() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "rediAI certification" in text or "rediai certification" in text
    assert "m09 does not claim rediai certification" in text or "does not claim rediai" in text
