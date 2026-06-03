"""Minimal tests to satisfy M06 branch coverage gate for src/pantanal_1."""

from __future__ import annotations

from pathlib import Path

import pytest

from pantanal_1.kaggle_paths import (
    all_sample_submission_candidates,
    discover_sample_submission_paths,
    is_kaggle_environment,
)
from pantanal_1.sample_baseline import (
    build_zero_rows_from_sample,
    read_sample_submission_csv,
    validate_real_sample_zero_rows,
    write_submission_csv_with_fieldnames,
)
from pantanal_1.submission_contract import (
    REPO_ROOT,
    SubmissionValidationError,
    UnsafeSubmissionPathError,
    build_row_id,
    build_segment_end_times,
    build_zero_submission_rows,
    validate_submission_rows,
    write_submission_csv,
)
from pantanal_1.synthetic_schema import synthetic_class_labels
from tests.fixtures.synthetic_submission_schema import synthetic_class_labels as fixture_labels


def test_is_kaggle_environment_true_when_env_set(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KAGGLE_KERNEL_RUN_TYPE", "Interactive")
    assert is_kaggle_environment() is True


def test_discover_sample_submission_paths_empty_on_oserror(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def raise_oserror(self: Path, pattern: str) -> object:
        raise OSError("access denied")

    monkeypatch.setattr(Path, "rglob", raise_oserror)
    assert discover_sample_submission_paths(tmp_path) == ()


def test_all_sample_submission_candidates_deduplicates(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    nested = tmp_path / "competitions" / "birdclef-2026"
    nested.mkdir(parents=True)
    sample = nested / "sample_submission.csv"
    sample.write_text("row_id,a\nx,0\n", encoding="utf-8")
    input_root = tmp_path

    monkeypatch.setattr("pantanal_1.kaggle_paths.KAGGLE_INPUT_ROOT", input_root)
    monkeypatch.setattr(
        "pantanal_1.kaggle_paths.EXPLICIT_SAMPLE_SUBMISSION_CANDIDATES",
        (sample,),
    )

    candidates = all_sample_submission_candidates()
    assert sample in candidates
    assert candidates.count(sample) == 1


def test_read_sample_submission_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        read_sample_submission_csv(tmp_path / "missing.csv")


def test_read_sample_submission_no_header(tmp_path: Path) -> None:
    path = tmp_path / "sample_submission.csv"
    path.write_text("", encoding="utf-8")
    with pytest.raises(SubmissionValidationError, match="no header"):
        read_sample_submission_csv(path)


def test_build_zero_rows_missing_row_id() -> None:
    with pytest.raises(SubmissionValidationError, match="missing row_id"):
        build_zero_rows_from_sample(["row_id", "a"], [{"b": "x"}])


def test_validate_real_sample_zero_rows_errors() -> None:
    fieldnames = ["row_id", "species_a"]
    with pytest.raises(SubmissionValidationError, match="must not be empty"):
        validate_real_sample_zero_rows([], fieldnames)

    bad_order = [{"species_a": 0.0, "row_id": "id_5"}]
    with pytest.raises(SubmissionValidationError, match="column order"):
        validate_real_sample_zero_rows(bad_order, fieldnames)

    with pytest.raises(SubmissionValidationError, match="non-empty string"):
        validate_real_sample_zero_rows([{"row_id": "", "species_a": 0.0}], fieldnames)

    with pytest.raises(SubmissionValidationError, match="must be numeric"):
        validate_real_sample_zero_rows([{"row_id": "id_5", "species_a": "x"}], fieldnames)

    with pytest.raises(SubmissionValidationError, match="must be 0.0"):
        validate_real_sample_zero_rows([{"row_id": "id_5", "species_a": 0.5}], fieldnames)


def test_write_submission_csv_with_fieldnames_unsafe_root() -> None:
    rows = [{"row_id": "id_5", "species_a": 0.0}]
    with pytest.raises(UnsafeSubmissionPathError):
        write_submission_csv_with_fieldnames(
            rows,
            REPO_ROOT / "submission.csv",
            ["row_id", "species_a"],
        )


def test_submission_contract_validation_edges() -> None:
    labels = fixture_labels()[:3]
    with pytest.raises(SubmissionValidationError):
        build_row_id("", 5)
    with pytest.raises(SubmissionValidationError):
        build_row_id("stem", 0)
    with pytest.raises(SubmissionValidationError):
        build_segment_end_times(duration_seconds=7, window_seconds=5)
    with pytest.raises(SubmissionValidationError):
        build_zero_submission_rows([], labels)
    with pytest.raises(SubmissionValidationError):
        build_zero_submission_rows(["stem"], [])

    rows = build_zero_submission_rows(["stem_a"], labels)
    bad = [{**rows[0], "row_id": "no_suffix"}]
    with pytest.raises(SubmissionValidationError):
        validate_submission_rows(bad, labels)

    with pytest.raises(SubmissionValidationError):
        validate_submission_rows([], labels)

    dup = [rows[0], rows[0]]
    with pytest.raises(SubmissionValidationError, match="duplicate"):
        validate_submission_rows(dup, labels)

    extra_col = [{**rows[0], "extra": 0.0}]
    with pytest.raises(SubmissionValidationError, match="unexpected"):
        validate_submission_rows(extra_col, labels)

    bool_row = [{**rows[0], labels[0]: True}]
    with pytest.raises(SubmissionValidationError, match="numeric"):
        validate_submission_rows(bool_row, labels)

    out_of_range = [{**rows[0], labels[0]: 1.5}]
    with pytest.raises(SubmissionValidationError, match="\\[0, 1\\]"):
        validate_submission_rows(out_of_range, labels)


def test_write_submission_csv_unsafe_root() -> None:
    labels = fixture_labels()[:2]
    rows = build_zero_submission_rows(["stem_a"], labels)
    with pytest.raises(UnsafeSubmissionPathError):
        write_submission_csv(rows, REPO_ROOT / "submission.csv", labels)


def test_synthetic_class_labels_rejects_invalid_count() -> None:
    with pytest.raises(ValueError, match="at least 1"):
        synthetic_class_labels(0)
