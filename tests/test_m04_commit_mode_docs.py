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


def test_probe_requires_cpu_and_internet_disabled() -> None:
    text = PROBE_PATH.read_text(encoding="utf-8").lower()
    assert "cpu" in text
    assert "internet" in text
    assert "disabled" in text


def test_evidence_template_not_yet_executed() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8").lower()
    assert "not yet executed" in text


def test_evidence_template_includes_def_002b_and_def_003b() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "DEF-002B" in text
    assert "DEF-003B" in text


def test_evidence_template_supports_blocked_and_na_status_vocabulary() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    for value in STATUS_VALUES:
        assert value in text, f"missing status value: {value}"


def test_pantanal_1_keeps_def_002b_open() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    deferred = text.split("## 11. Deferred issues register", 1)[-1]
    assert "DEF-002B" in deferred
    not_proven = text.split("**Not yet proven:**", 1)[-1].split("**M01", 1)[0]
    assert "DEF-002B" in not_proven or "commit/submit" in not_proven.lower()


def test_pantanal_1_keeps_def_003b_open() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    deferred = text.split("## 11. Deferred issues register", 1)[-1]
    assert "DEF-003B" in deferred
    not_proven = text.split("**Not yet proven:**", 1)[-1]
    assert "DEF-003B" in not_proven


def test_m04_docs_do_not_claim_commit_submit_success_before_evidence() -> None:
    for path in (PROBE_PATH, EVIDENCE_PATH):
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        assert "def-002b closed" not in lower
        assert "def-003b closed" not in lower
        for line in text.splitlines():
            line_lower = line.lower()
            for phrase in ("commit/submit-mode success", "commit-mode success"):
                if phrase in line_lower and "do not" not in line_lower:
                    raise AssertionError(
                        f"affirmative success claim in {path.name}: {line.strip()}"
                    )


def test_m04_evidence_does_not_record_leaderboard_score() -> None:
    text = EVIDENCE_PATH.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.strip().startswith("- Public leaderboard score:"):
            value = line.split(":", 1)[1].strip()
            assert value == "" or value.lower() in ("n/a", "none"), (
                "must not record an actual public score before manual run"
            )
            return
        if line.strip().startswith("- Private leaderboard score:"):
            value = line.split(":", 1)[1].strip()
            assert value == "" or value.lower() in ("n/a", "none"), (
                "must not record an actual private score before manual run"
            )
    raise AssertionError("missing leaderboard score fields in evidence template")


def test_pantanal_1_m04_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    assert "M04" in ledger
    assert "in progress" in ledger.lower()
    section_12 = text.split("## 12.", 1)[-1]
    assert "m04-kaggle-commit-mode-probe" in section_12.lower()
    assert "in progress" in section_12.lower()


def test_kaggle_submission_bible_links_m04_docs() -> None:
    text = BIBLE_PATH.read_text(encoding="utf-8")
    assert "m04_commit_mode_probe.md" in text
    assert "m04_commit_mode_evidence.md" in text
    assert "M04" in text
    lower = text.lower()
    assert "do not claim m04 success" in lower
    assert "def-002b closed" not in lower


def test_m03_baseline_notebook_outputs_remain_cleared() -> None:
    with NOTEBOOK_PATH.open(encoding="utf-8") as handle:
        notebook = json.load(handle)
    for cell in notebook.get("cells", []):
        assert cell.get("outputs") in (None, [])
