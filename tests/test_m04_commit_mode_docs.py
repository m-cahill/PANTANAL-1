"""Tests for M04 commit-mode probe docs and honest claim boundaries."""

from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = REPO_ROOT / "docs" / "kaggle" / "m04_commit_mode_probe.md"
EVIDENCE_PATH = REPO_ROOT / "docs" / "kaggle" / "m04_commit_mode_evidence.md"
BIBLE_PATH = REPO_ROOT / "docs" / "kaggle" / "kaggle_submission_bible.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"
NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "pantanal_1_m03_baseline.ipynb"

NOTEBOOK_URL = (
    "https://www.kaggle.com/code/michael1232/pantanal-1-m03-baseline/"
    "notebook?scriptVersionId=324138273"
)

STATUS_VALUES = (
    "yes",
    "no",
    "blocked — deadline passed",
    "N/A — not attempted",
)


def test_m04_commit_mode_probe_doc_exists() -> None:
    assert PROBE_PATH.is_file()


def test_m04_commit_mode_evidence_doc_exists() -> None:
    assert EVIDENCE_PATH.is_file()


def test_probe_mentions_working_submission_csv() -> None:
    assert "/kaggle/working/submission.csv" in PROBE_PATH.read_text(encoding="utf-8")


def test_probe_distinguishes_interactive_and_commit_submit_modes() -> None:
    text = PROBE_PATH.read_text(encoding="utf-8").lower()
    assert "interactive" in text
    assert "commit" in text
    assert "submit" in text


def test_evidence_records_kaggle_notebook_url() -> None:
    assert NOTEBOOK_URL in EVIDENCE_PATH.read_text(encoding="utf-8")


def test_evidence_records_version_2_of_2() -> None:
    assert "Version 2 of 2" in EVIDENCE_PATH.read_text(encoding="utf-8")


def test_evidence_records_runtime_1m_7s() -> None:
    assert "1m 7s" in EVIDENCE_PATH.read_text(encoding="utf-8")


def test_evidence_records_public_score_0_500() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "0.500" in text
    for line in text.splitlines():
        if line.strip().startswith("- Public leaderboard score:"):
            assert "0.500" in line
            return
    raise AssertionError("missing Public leaderboard score field")


def test_evidence_executed_not_template_only() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "executed" in text
    assert "not yet executed" not in text


def test_pantanal_1_records_m04_scored_evidence() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "M04 Kaggle commit/scored evidence" in text
    assert "0.500" in text
    assert "m04_commit_mode_evidence.md" in text


def test_pantanal_1_does_not_claim_model_inference_or_quality() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    m04_section = text.split("**M04 explicit non-claims", 1)[-1].split("---", 1)[0]
    assert "model inference" in m04_section.lower()
    assert "meaningful model quality" in m04_section.lower() or "competitive" in m04_section.lower()


def test_pantanal_1_def_002b_evidenced_not_open() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    deferred = text.split("## 11. Deferred issues register", 1)[-1]
    assert "DEF-002B" in deferred
    assert "M04 (evidenced)" in deferred
    not_proven = text.split("**Not yet proven:**", 1)[-1].split("**M01", 1)[0]
    assert "DEF-002B" not in not_proven


def test_pantanal_1_def_003b_narrowed_or_evidenced() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    deferred = text.split("## 11. Deferred issues register", 1)[-1]
    assert "DEF-003B" in deferred
    assert "M04" in deferred.split("DEF-003B", 1)[1][:120]
    assert "narrowed" in deferred.lower() or "evidenced" in deferred.lower()
    not_proven = text.split("**Not yet proven:**", 1)[-1].split("**M01", 1)[0]
    assert "DEF-003B narrowed" in not_proven or "def-003b narrowed" in not_proven.lower()
    assert "Scored/hidden test submission schema behavior" not in not_proven


def test_pantanal_1_m04_still_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    assert "in progress" in ledger.lower()


def test_kaggle_submission_bible_records_m04_evidence() -> None:
    text = BIBLE_PATH.read_text(encoding="utf-8")
    assert "m04_commit_mode_evidence.md" in text
    assert "0.500" in text
    assert "DEF-002B" in text
    assert "evidenced" in text.lower()


def test_m03_baseline_notebook_outputs_remain_cleared() -> None:
    with NOTEBOOK_PATH.open(encoding="utf-8") as handle:
        notebook = json.load(handle)
    for cell in notebook.get("cells", []):
        assert cell.get("outputs") in (None, [])
