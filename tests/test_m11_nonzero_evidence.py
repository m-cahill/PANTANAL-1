"""Tests for M11 Kaggle non-zero baseline evidence docs and governance."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNBOOK_PATH = REPO_ROOT / "docs" / "kaggle" / "m11_nonzero_baseline_runbook.md"
EVIDENCE_PATH = REPO_ROOT / "docs" / "kaggle" / "m11_nonzero_baseline_evidence.md"
NONZERO_DOC = REPO_ROOT / "docs" / "kaggle" / "nonzero_baseline.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"


def test_m11_runbook_exists() -> None:
    assert RUNBOOK_PATH.is_file()


def test_m11_evidence_template_exists() -> None:
    assert EVIDENCE_PATH.is_file()


def test_m11_evidence_not_yet_executed() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "not yet executed" in text


def test_m11_evidence_includes_epsilon() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "Epsilon" in text or "epsilon" in text
    assert "0.001" in text


def test_m11_evidence_includes_public_score_field() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "Public score" in text


def test_m11_evidence_score_improvement_requires_observation() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "score improvement" in text
    assert "observed" in text or "observation" in text


def test_m11_runbook_distinguishes_interactive_commit_submit() -> None:
    text = RUNBOOK_PATH.read_text(encoding="utf-8")
    lower = text.lower()
    assert "interactive" in lower
    assert "commit" in lower
    assert "submit" in lower


def test_m11_runbook_does_not_infer_scored_from_interactive() -> None:
    text = RUNBOOK_PATH.read_text(encoding="utf-8").lower()
    assert "do not infer" in text


def test_nonzero_baseline_doc_references_m11_artifacts() -> None:
    text = NONZERO_DOC.read_text(encoding="utf-8")
    assert "m11_nonzero_baseline_runbook.md" in text
    assert "m11_nonzero_baseline_evidence.md" in text


def test_pantanal_marks_m11_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    m11_row = ledger.split("| M11 |", 1)[-1].split("\n", 1)[0]
    assert "in progress" in m11_row.lower()


def test_pantanal_m11_narrow_pre_evidence_claim() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "runbook and evidence template" in text.lower() or "runbook" in text
    assert "non-zero baseline" in text.lower() or "non-zero" in text.lower()


def test_pantanal_does_not_claim_m11_model_quality() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "m11 does not prove model quality" in text


def test_pantanal_does_not_claim_m11_score_improvement() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    claims = text.split("## 8. current claims", 1)[-1]
    implemented = claims.split("**not yet proven:**", 1)[0]
    assert "m11 recorded kaggle evidence" not in implemented
    assert "m11 does not claim score improvement" in text
