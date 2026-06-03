"""Uniform epsilon non-zero baseline from sample_submission schema (stdlib csv only)."""

from __future__ import annotations

import csv
from collections.abc import Mapping, Sequence
from pathlib import Path

from pantanal_1.sample_baseline import (
    class_columns_from_fieldnames,
    read_sample_submission_csv,
)
from pantanal_1.submission_contract import (
    SubmissionValidationError,
    UnsafeSubmissionPathError,
    build_zero_submission_rows,
    is_safe_submission_output_path,
)
from pantanal_1.synthetic_schema import (
    SYNTHETIC_CLASS_LABELS,
    SYNTHETIC_SOUNDSCAPE_STEMS,
)

DEFAULT_EPSILON = 0.001


class EpsilonValidationError(SubmissionValidationError):
    """Raised when epsilon is outside the allowed (0, 1] range."""


def validate_epsilon(epsilon: float) -> float:
    """Validate epsilon is in (0, 1]; return normalized float."""
    if isinstance(epsilon, bool) or not isinstance(epsilon, int | float):
        raise EpsilonValidationError(f"epsilon must be numeric, got {type(epsilon).__name__}")
    value = float(epsilon)
    if value <= 0.0:
        raise EpsilonValidationError(f"epsilon must be > 0, got {value!r}")
    if value > 1.0:
        raise EpsilonValidationError(f"epsilon must be <= 1, got {value!r}")
    return value


def format_probability_string(epsilon: float) -> str:
    """Format a probability value as a Kaggle-style float string."""
    validated = validate_epsilon(epsilon)
    text = f"{validated:g}"
    if "." not in text and "e" not in text.lower():
        text = f"{text}.0"
    return text


def build_uniform_nonzero_rows(
    sample_rows: Sequence[Mapping[str, str]],
    fieldnames: Sequence[str],
    epsilon: float = DEFAULT_EPSILON,
) -> list[dict[str, str]]:
    """Build uniform-epsilon rows preserving sample row order and column set."""
    validated = validate_epsilon(epsilon)
    prob_str = format_probability_string(validated)
    class_columns_from_fieldnames(fieldnames)
    names = list(fieldnames)
    nonzero_rows: list[dict[str, str]] = []

    for index, sample_row in enumerate(sample_rows):
        if "row_id" not in sample_row:
            raise SubmissionValidationError(f"sample row {index} missing row_id")
        row = {name: sample_row["row_id"] if name == "row_id" else prob_str for name in names}
        nonzero_rows.append(row)

    return nonzero_rows


def validate_nonzero_sample_rows(
    rows: Sequence[Mapping[str, str]],
    fieldnames: Sequence[str],
    epsilon: float = DEFAULT_EPSILON,
) -> None:
    """Validate uniform non-zero baseline rows against sample header schema."""
    validated = validate_epsilon(epsilon)
    expected_prob = format_probability_string(validated)
    class_cols = class_columns_from_fieldnames(fieldnames)
    if not rows:
        raise SubmissionValidationError("rows must not be empty")

    saw_nonzero = False
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
            if not isinstance(value, str):
                raise SubmissionValidationError(
                    f"row {index} column {col!r} must be a string, got {type(value).__name__}"
                )
            try:
                numeric = float(value)
            except ValueError as exc:
                raise SubmissionValidationError(
                    f"row {index} column {col!r} must be float-convertible: {value!r}"
                ) from exc
            if not 0.0 <= numeric <= 1.0:
                raise SubmissionValidationError(
                    f"row {index} column {col!r} must be in [0, 1], got {value!r}"
                )
            if numeric != 0.0:
                saw_nonzero = True
            if value != expected_prob:
                raise SubmissionValidationError(
                    f"row {index} column {col!r} must be uniform epsilon {expected_prob!r}, "
                    f"got {value!r}"
                )

    if not saw_nonzero:
        raise SubmissionValidationError("at least one class probability must be non-zero")


def write_nonzero_submission_csv(
    rows: Sequence[Mapping[str, str]],
    output_path: Path,
    fieldnames: Sequence[str],
    epsilon: float = DEFAULT_EPSILON,
) -> Path:
    """Write validated uniform non-zero baseline CSV using exact fieldnames order."""
    validate_nonzero_sample_rows(rows, fieldnames, epsilon)
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


def write_nonzero_baseline_from_sample(
    sample_submission_path: Path,
    output_path: Path,
    epsilon: float = DEFAULT_EPSILON,
) -> Path:
    """Read sample_submission.csv and write uniform-epsilon baseline submission."""
    fieldnames, sample_rows = read_sample_submission_csv(sample_submission_path)
    rows = build_uniform_nonzero_rows(sample_rows, fieldnames, epsilon=epsilon)
    return write_nonzero_submission_csv(rows, output_path, fieldnames, epsilon=epsilon)


def build_synthetic_nonzero_fieldnames_and_rows(
    epsilon: float = DEFAULT_EPSILON,
) -> tuple[list[str], list[dict[str, str]]]:
    """Build M01 synthetic schema rows with uniform epsilon class probabilities."""
    class_labels = list(SYNTHETIC_CLASS_LABELS)
    stems = list(SYNTHETIC_SOUNDSCAPE_STEMS)
    zero_rows = build_zero_submission_rows(stems, class_labels)
    fieldnames = ["row_id", *class_labels]
    sample_rows = [{"row_id": str(row["row_id"])} for row in zero_rows]
    rows = build_uniform_nonzero_rows(sample_rows, fieldnames, epsilon=epsilon)
    return fieldnames, rows


def write_synthetic_nonzero_baseline(
    output_path: Path,
    epsilon: float = DEFAULT_EPSILON,
) -> Path:
    """Write uniform-epsilon baseline using the M01 synthetic schema."""
    fieldnames, rows = build_synthetic_nonzero_fieldnames_and_rows(epsilon=epsilon)
    return write_nonzero_submission_csv(rows, output_path, fieldnames, epsilon=epsilon)
