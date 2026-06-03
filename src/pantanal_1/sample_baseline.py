"""Zero baseline generation from real sample_submission.csv (stdlib csv only)."""

from __future__ import annotations

import csv
from collections.abc import Mapping, Sequence
from pathlib import Path

from pantanal_1.submission_contract import (
    SubmissionValidationError,
    UnsafeSubmissionPathError,
    is_safe_submission_output_path,
)


def read_sample_submission_csv(
    sample_path: Path,
) -> tuple[list[str], list[dict[str, str]]]:
    """Read sample_submission.csv preserving header order and row order."""
    if not sample_path.is_file():
        raise FileNotFoundError(f"sample submission not found: {sample_path}")

    with sample_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SubmissionValidationError("sample_submission.csv has no header row")
        fieldnames = list(reader.fieldnames)
        rows = [dict(row) for row in reader]

    return fieldnames, rows


def class_columns_from_fieldnames(fieldnames: Sequence[str]) -> list[str]:
    """Return all columns except row_id (treated as class/probability columns)."""
    if "row_id" not in fieldnames:
        raise SubmissionValidationError("sample_submission.csv must include row_id column")
    class_cols = [name for name in fieldnames if name != "row_id"]
    if not class_cols:
        raise SubmissionValidationError(
            "sample_submission.csv must have at least one non-row_id column"
        )
    return class_cols


def build_zero_rows_from_sample(
    fieldnames: Sequence[str],
    sample_rows: Sequence[Mapping[str, str]],
) -> list[dict[str, float | str]]:
    """Build zero-baseline rows preserving sample row order and column set."""
    class_cols = class_columns_from_fieldnames(fieldnames)
    zero_rows: list[dict[str, float | str]] = []

    for index, sample_row in enumerate(sample_rows):
        if "row_id" not in sample_row:
            raise SubmissionValidationError(f"sample row {index} missing row_id")
        row: dict[str, float | str] = {"row_id": sample_row["row_id"]}
        for col in class_cols:
            row[col] = 0.0
        zero_rows.append(row)

    return zero_rows


def validate_real_sample_zero_rows(
    rows: Sequence[Mapping[str, object]],
    fieldnames: Sequence[str],
) -> None:
    """Validate zero baseline built from real sample_submission.csv schema."""
    class_cols = class_columns_from_fieldnames(fieldnames)
    if not rows:
        raise SubmissionValidationError("rows must not be empty")

    for index, row in enumerate(rows):
        if list(row.keys()) != list(fieldnames):
            raise SubmissionValidationError(
                f"row {index} column order must match sample header exactly"
            )
        row_id = row["row_id"]
        if not isinstance(row_id, str) or not row_id:
            raise SubmissionValidationError(f"row {index} row_id must be a non-empty string")

        for col in class_cols:
            value = row[col]
            if isinstance(value, bool) or not isinstance(value, int | float):
                raise SubmissionValidationError(
                    f"row {index} column {col!r} must be numeric, got {type(value).__name__}"
                )
            if float(value) != 0.0:
                raise SubmissionValidationError(
                    f"row {index} column {col!r} must be 0.0 for zero baseline, got {value!r}"
                )
            if not 0.0 <= float(value) <= 1.0:
                raise SubmissionValidationError(
                    f"row {index} column {col!r} must be in [0, 1], got {value!r}"
                )


def write_submission_csv_with_fieldnames(
    rows: Sequence[Mapping[str, object]],
    output_path: Path,
    fieldnames: Sequence[str],
) -> Path:
    """Write submission CSV using exact fieldnames order from sample header."""
    validate_real_sample_zero_rows(rows, fieldnames)
    if not is_safe_submission_output_path(output_path):
        raise UnsafeSubmissionPathError("refusing to write submission.csv at repository root")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    names = list(fieldnames)

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=names)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row[column] for column in names})

    return output_path
