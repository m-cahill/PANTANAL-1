"""Tests for synthetic submission contract generation and validation."""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

import pytest

from pantanal_1.submission_contract import (
    SubmissionValidationError,
    UnsafeSubmissionPathError,
    build_row_id,
    build_segment_end_times,
    build_zero_submission_rows,
    is_safe_submission_output_path,
    validate_submission_rows,
    write_submission_csv,
)
from scripts.verify_repo_state import find_violations
from tests.fixtures.synthetic_submission_schema import (
    SYNTHETIC_CLASS_COUNT,
    synthetic_class_labels,
    synthetic_soundscape_stems,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_build_segment_end_times_for_sixty_second_soundscape() -> None:
    assert build_segment_end_times() == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


def test_build_row_id_example_format() -> None:
    row_id = build_row_id("BC2026_Test_0001_S05_20250227_010002", 20)
    assert row_id == "BC2026_Test_0001_S05_20250227_010002_20"


def test_build_zero_submission_rows_one_soundscape_has_twelve_rows() -> None:
    stems = [synthetic_soundscape_stems()[0]]
    rows = build_zero_submission_rows(stems, synthetic_class_labels())
    assert len(rows) == 12


def test_build_zero_submission_rows_two_soundscapes_has_twenty_four_rows() -> None:
    rows = build_zero_submission_rows(synthetic_soundscape_stems(), synthetic_class_labels())
    assert len(rows) == 24


def test_zero_submission_has_row_id_plus_234_class_columns() -> None:
    class_labels = synthetic_class_labels()
    rows = build_zero_submission_rows([synthetic_soundscape_stems()[0]], class_labels)
    assert len(rows[0]) == 1 + SYNTHETIC_CLASS_COUNT
    assert list(rows[0].keys()) == ["row_id", *class_labels]


def test_zero_submission_probabilities_are_zero() -> None:
    class_labels = synthetic_class_labels()
    rows = build_zero_submission_rows([synthetic_soundscape_stems()[0]], class_labels)
    for row in rows:
        for label in class_labels:
            assert row[label] == 0.0


def test_validate_submission_rows_accepts_valid_rows() -> None:
    rows = build_zero_submission_rows([synthetic_soundscape_stems()[0]], synthetic_class_labels())
    validate_submission_rows(rows, synthetic_class_labels())


def test_validate_submission_rows_rejects_missing_class_column() -> None:
    rows = build_zero_submission_rows([synthetic_soundscape_stems()[0]], synthetic_class_labels())
    del rows[0][synthetic_class_labels()[0]]
    with pytest.raises(SubmissionValidationError, match="missing expected columns"):
        validate_submission_rows(rows, synthetic_class_labels())


def test_validate_submission_rows_rejects_out_of_range_probability() -> None:
    rows = build_zero_submission_rows([synthetic_soundscape_stems()[0]], synthetic_class_labels())
    rows[0][synthetic_class_labels()[0]] = 1.5
    with pytest.raises(SubmissionValidationError, match="must be in \\[0, 1\\]"):
        validate_submission_rows(rows, synthetic_class_labels())


def test_validate_submission_rows_rejects_duplicate_row_ids() -> None:
    rows = build_zero_submission_rows([synthetic_soundscape_stems()[0]], synthetic_class_labels())
    rows[1]["row_id"] = rows[0]["row_id"]
    with pytest.raises(SubmissionValidationError, match="duplicate row_id"):
        validate_submission_rows(rows, synthetic_class_labels())


def test_write_submission_csv_round_trip(tmp_path: Path) -> None:
    class_labels = synthetic_class_labels()
    rows = build_zero_submission_rows([synthetic_soundscape_stems()[0]], class_labels)
    output_path = tmp_path / "submission.csv"
    write_submission_csv(rows, output_path, class_labels)

    with output_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        read_rows = list(reader)

    assert len(read_rows) == 12
    assert reader.fieldnames == ["row_id", *class_labels]
    assert read_rows[0]["row_id"] == build_row_id(synthetic_soundscape_stems()[0], 5)


def test_write_submission_csv_rejects_repo_root_submission_csv() -> None:
    rows = build_zero_submission_rows([synthetic_soundscape_stems()[0]], synthetic_class_labels())
    with pytest.raises(UnsafeSubmissionPathError, match="repository root"):
        write_submission_csv(rows, REPO_ROOT / "submission.csv", synthetic_class_labels())


def test_is_safe_submission_output_path_allows_tmp_submissions() -> None:
    assert is_safe_submission_output_path(REPO_ROOT / "tmp" / "submissions" / "submission.csv")


def test_verifier_rejects_root_submission_csv(tmp_path: Path) -> None:
    (tmp_path / "submission.csv").write_text("row_id\n", encoding="utf-8")
    violations = find_violations(tmp_path)
    assert any("submission.csv" in violation for violation in violations)


def test_repo_verifier_passes_after_contract_tests() -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "verify_repo_state.py")],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
