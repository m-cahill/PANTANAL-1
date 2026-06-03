"""Tests for M11 Kaggle non-zero baseline evidence docs and governance."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNBOOK_PATH = REPO_ROOT / "docs" / "kaggle" / "m11_nonzero_baseline_runbook.md"
EVIDENCE_PATH = REPO_ROOT / "docs" / "kaggle" / "m11_nonzero_baseline_evidence.md"
NONZERO_DOC = REPO_ROOT / "docs" / "kaggle" / "nonzero_baseline.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"

SAMPLE_PATH = "/kaggle/input/competitions/birdclef-2026/sample_submission.csv"
NOTEBOOK_URL = (
    "https://www.kaggle.com/code/michael1232/pantanal-1-m11-nonzero-baseline"
    "?scriptVersionId=324302733"
)


def test_m11_runbook_exists() -> None:
    assert RUNBOOK_PATH.is_file()


def test_m11_evidence_file_exists() -> None:
    assert EVIDENCE_PATH.is_file()


def test_m11_evidence_records_interactive_execution() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "not yet executed" not in text.lower()
    assert "REAL_SAMPLE_NONZERO_BASELINE" in text
    assert "Interactive" in text


def test_m11_evidence_records_notebook_url_and_version() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "324302733" in text
    assert "pantanal-1-m11-nonzero-baseline" in text
    assert "Version 2" in text


def test_m11_evidence_records_public_score() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "0.500" in text
    for line in text.splitlines():
        if line.strip().startswith("- Public score:"):
            assert "0.500" in line
            return
    raise AssertionError("missing Public score field")


def test_m11_evidence_records_prior_zero_baseline_score() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "pantanal_1_m03_baseline" in text
    assert "Prior all-zero baseline public score" in text or "prior all-zero" in text.lower()
    assert "0.500" in text


def test_m11_evidence_records_no_score_improvement() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "no score improvement" in text
    assert "score improvement claimed" in text


def test_m11_evidence_records_commit_submit_success() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "Succeeded" in text
    assert "Commit successful" in text or "commit successful" in text.lower()


def test_m11_evidence_records_epsilon() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "0.001" in text


def test_m11_evidence_records_sample_path_and_output() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert SAMPLE_PATH in text
    assert "/kaggle/working/submission.csv" in text
    assert "6182" in text


def test_m11_runbook_distinguishes_interactive_commit_submit() -> None:
    text = RUNBOOK_PATH.read_text(encoding="utf-8")
    lower = text.lower()
    assert "interactive" in lower
    assert "commit" in lower
    assert "submit" in lower


def test_nonzero_baseline_doc_m11_scored_evidence_note() -> None:
    text = NONZERO_DOC.read_text(encoding="utf-8")
    assert "m11_nonzero_baseline_evidence.md" in text
    assert "0.500" in text
    lower = text.lower()
    assert "pipeline acceptance" in lower
    assert "not model quality" in lower or "not model quality or score improvement" in lower


def test_nonzero_baseline_doc_scoring_planning_note() -> None:
    text = NONZERO_DOC.read_text(encoding="utf-8").lower()
    assert "roc-auc" in text or "ranking separation" in text
    assert "empirically observed" in text


def test_pantanal_marks_m11_closed() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    m11_row = ledger.split("| M11 |", 1)[-1].split("\n", 1)[0]
    assert "closed" in m11_row.lower()


def test_pantanal_m11_recorded_kaggle_evidence_claim() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "M11 recorded Kaggle evidence" in text
    assert "0.500" in text
    assert "no score improvement was observed" in text.lower()
    assert "runbook, evidence template, and output-cleared notebook" in text.lower()


def test_pantanal_does_not_claim_m11_model_quality() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "m11 does not prove model quality" in text
    claims = text.split("## 8. current claims", 1)[-1].split("**not yet proven:**", 1)[0]
    scored = claims.split("m11 kaggle scored evidence", 1)[-1][:500]
    assert "competitive performance" not in scored or "not" in scored


def test_pantanal_does_not_claim_m11_score_improvement() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    claims = text.split("## 8. current claims", 1)[-1]
    implemented = claims.split("**not yet proven:**", 1)[0]
    assert "no score improvement was observed" in implemented
    assert "m11 does not prove score improvement" in text
    assert "score improvement over" not in implemented
