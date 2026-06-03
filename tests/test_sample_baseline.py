"""Tests for real sample_submission zero baseline helpers."""

from __future__ import annotations

from pathlib import Path

import pytest

from pantanal_1.sample_baseline import (
    build_zero_rows_from_sample,
    class_columns_from_fieldnames,
    read_sample_submission_csv,
    validate_real_sample_zero_rows,
    write_submission_csv_with_fieldnames,
)
from pantanal_1.submission_contract import SubmissionValidationError


def test_read_and_zero_baseline_preserves_order(tmp_path: Path) -> None:
    sample = tmp_path / "sample_submission.csv"
    sample.write_text(
        "row_id,species_a,species_b\nid_5,0.1,0.2\nid_10,0.3,0.4\n",
        encoding="utf-8",
    )
    fieldnames, sample_rows = read_sample_submission_csv(sample)
    assert fieldnames == ["row_id", "species_a", "species_b"]
    assert [r["row_id"] for r in sample_rows] == ["id_5", "id_10"]

    rows = build_zero_rows_from_sample(fieldnames, sample_rows)
    validate_real_sample_zero_rows(rows, fieldnames)
    assert rows[0]["species_a"] == 0.0
    assert rows[1]["row_id"] == "id_10"

    out = tmp_path / "out" / "submission.csv"
    write_submission_csv_with_fieldnames(rows, out, fieldnames)
    text = out.read_text(encoding="utf-8")
    assert text.splitlines()[0] == "row_id,species_a,species_b"
    assert "id_5,0.0,0.0" in text


def test_class_columns_requires_row_id() -> None:
    with pytest.raises(SubmissionValidationError):
        class_columns_from_fieldnames(["species_a"])
