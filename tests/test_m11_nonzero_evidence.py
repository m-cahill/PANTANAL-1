"""Tests for M11 Kaggle non-zero baseline evidence docs and governance."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNBOOK_PATH = REPO_ROOT / "docs" / "kaggle" / "m11_nonzero_baseline_runbook.md"
EVIDENCE_PATH = REPO_ROOT / "docs" / "kaggle" / "m11_nonzero_baseline_evidence.md"
NONZERO_DOC = REPO_ROOT / "docs" / "kaggle" / "nonzero_baseline.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"

SAMPLE_PATH = "/kaggle/input/competitions/birdclef-2026/sample_submission.csv"


def test_m11_runbook_exists() -> None:
    assert RUNBOOK_PATH.is_file()


def test_m11_evidence_file_exists() -> None:
    assert EVIDENCE_PATH.is_file()


def test_m11_evidence_records_interactive_execution() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "Executed" in text or "Interactive" in text
    assert "not yet executed" not in text.lower()
    assert "REAL_SAMPLE_NONZERO_BASELINE" in text
    assert "Interactive" in text


def test_m11_evidence_records_epsilon() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "0.001" in text
    assert "Epsilon" in text or "epsilon" in text


def test_m11_evidence_records_sample_path_and_output() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert SAMPLE_PATH in text
    assert "/kaggle/working/submission.csv" in text
    assert "6182" in text


def test_m11_evidence_does_not_claim_public_score() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    lower = text.lower()
    assert "not observed" in lower or "n/a" in lower
    for line in text.splitlines():
        if line.strip().startswith("- Public score:"):
            value = line.split(":", 1)[1].strip().lower()
            assert "not observed" in value or value in ("", "n/a")
            return
    raise AssertionError("missing Public score field")


def test_m11_evidence_score_improvement_not_claimed() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "score improvement claimed" in text
    assert "**no**" in text or "no" in text


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


def test_nonzero_baseline_doc_scoring_planning_note() -> None:
    text = NONZERO_DOC.read_text(encoding="utf-8").lower()
    assert "roc-auc" in text or "ranking separation" in text
    assert "empirically observed" in text
    assert "working-note" in text or "working note" in text


def test_pantanal_marks_m11_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    m11_row = ledger.split("| M11 |", 1)[-1].split("\n", 1)[0]
    assert "in progress" in m11_row.lower()


def test_pantanal_m11_interactive_evidence_claim() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "M11 Kaggle interactive evidence" in text
    assert "REAL_SAMPLE_NONZERO_BASELINE" in text
    assert "0.001" in text
    assert "Interactive mode only" in text or "interactive mode only" in text.lower()


def test_pantanal_does_not_claim_m11_model_quality() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "m11 does not prove model quality" in text
    claims = text.split("## 8. current claims", 1)[-1].split("**not yet proven:**", 1)[0]
    assert "model quality" not in claims.split("m11 kaggle interactive", 1)[-1][:400]


def test_pantanal_does_not_claim_m11_score_improvement() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    claims = text.split("## 8. current claims", 1)[-1]
    implemented = claims.split("**not yet proven:**", 1)[0]
    assert "score improvement" not in implemented or "no score improvement" in implemented
    assert "m11 does not claim score improvement" in text
