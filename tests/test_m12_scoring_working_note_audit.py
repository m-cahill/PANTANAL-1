"""Tests for M12 scoring audit, working-note criteria audit, and next-direction decision."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCORING_AUDIT = REPO_ROOT / "docs" / "analysis" / "M12_scoring_methodology_audit.md"
WORKING_NOTE_AUDIT = REPO_ROOT / "docs" / "working_note" / "M12_working_note_criteria_audit.md"
NEXT_DIRECTION = REPO_ROOT / "docs" / "analysis" / "M12_next_direction_decision.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"


def test_m12_scoring_methodology_audit_exists() -> None:
    assert SCORING_AUDIT.is_file()


def test_scoring_audit_references_baselines_and_metric() -> None:
    text = SCORING_AUDIT.read_text(encoding="utf-8").lower()
    assert "all-zero" in text
    assert "uniform" in text
    assert "0.500" in text
    assert "roc-auc" in text
    assert "constant" in text
    assert "ranking" in text
    assert "no score improvement" in text
    assert "no model quality" in text or "does not prove" in text and "model quality" in text


def test_m12_working_note_criteria_audit_exists() -> None:
    assert WORKING_NOTE_AUDIT.is_file()


def test_working_note_audit_references_criteria_and_readiness() -> None:
    text = WORKING_NOTE_AUDIT.read_text(encoding="utf-8").lower()
    assert "originality" in text
    assert "quality" in text
    assert "contribution" in text
    assert "readability" in text or "presentation" in text
    assert "not working-note ready" in text or "not yet" in text and "working-note" in text
    assert "conditional" in text
    assert "no trained inference" in text or "does not implement trained" in text


def test_m12_next_direction_decision_exists() -> None:
    assert NEXT_DIRECTION.is_file()


def test_next_direction_recommends_m13_without_model_quality_claim() -> None:
    text = NEXT_DIRECTION.read_text(encoding="utf-8")
    lower = text.lower()
    assert "m13" in lower
    assert "audio-derived baseline planning gate" in lower
    assert "no score improvement" in lower
    assert "no model quality" in lower or "do not claim" in lower and "model quality" in lower


def test_pantanal_includes_m12_ledger_and_non_claims() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    assert "| M12 |" in ledger
    assert "Scoring Methodology and Working-Note Criteria Audit" in ledger
    assert "m12 does not implement model inference" in text.lower()
    assert "m12 does not prove working-note readiness" in text.lower()
    assert "M12_scoring_methodology_audit.md" in text


def test_pantanal_marks_m12_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    m12_row = ledger.split("| M12 |", 1)[-1].split("\n", 1)[0]
    assert "in progress" in m12_row.lower()


def test_pantanal_recommends_m13_next() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    section = text.split("## 12. Next milestone recommendation", 1)[-1]
    assert "M13" in section
    assert "Audio-Derived Baseline Planning Gate" in section
