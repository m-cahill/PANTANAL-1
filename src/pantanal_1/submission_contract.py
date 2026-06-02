"""Synthetic submission contract helpers for BirdCLEF+ 2026-shaped CSV artifacts."""

from __future__ import annotations

import csv
import re
from collections.abc import Mapping, Sequence
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

ROW_ID_SUFFIX_PATTERN = re.compile(r"_(\d+)$")


class SubmissionContractError(ValueError):
    """Base error for submission contract validation failures."""


class SubmissionValidationError(SubmissionContractError):
    """Raised when submission rows do not match the expected contract."""


class UnsafeSubmissionPathError(SubmissionContractError):
    """Raised when a submission writer target is not allowed."""


def build_row_id(soundscape_stem: str, end_time_seconds: int) -> str:
    """Build a BirdCLEF-style row id from a soundscape stem and segment end time."""
    if not soundscape_stem:
        raise SubmissionValidationError("soundscape_stem must not be empty")
    if end_time_seconds <= 0:
        raise SubmissionValidationError("end_time_seconds must be positive")
    return f"{soundscape_stem}_{end_time_seconds}"


def build_segment_end_times(
    duration_seconds: int = 60,
    window_seconds: int = 5,
) -> list[int]:
    """Return segment end times for fixed-width windows across a soundscape."""
    if duration_seconds <= 0:
        raise SubmissionValidationError("duration_seconds must be positive")
    if window_seconds <= 0:
        raise SubmissionValidationError("window_seconds must be positive")
    if duration_seconds % window_seconds != 0:
        raise SubmissionValidationError("duration_seconds must be divisible by window_seconds")

    return list(range(window_seconds, duration_seconds + 1, window_seconds))


def build_zero_submission_rows(
    soundscape_stems: Sequence[str],
    class_labels: Sequence[str],
) -> list[dict[str, float | str]]:
    """Build zero-baseline submission rows for synthetic soundscapes."""
    if not soundscape_stems:
        raise SubmissionValidationError("soundscape_stems must not be empty")
    if not class_labels:
        raise SubmissionValidationError("class_labels must not be empty")

    rows: list[dict[str, float | str]] = []
    for stem in soundscape_stems:
        for end_time in build_segment_end_times():
            row: dict[str, float | str] = {"row_id": build_row_id(stem, end_time)}
            for label in class_labels:
                row[label] = 0.0
            rows.append(row)
    return rows


def _parse_row_id_end_time(row_id: str) -> int:
    match = ROW_ID_SUFFIX_PATTERN.search(row_id)
    if match is None:
        raise SubmissionValidationError(
            f"row_id must end with an integer segment end time: {row_id!r}"
        )
    return int(match.group(1))


def _expected_columns(class_labels: Sequence[str]) -> list[str]:
    return ["row_id", *class_labels]


def validate_submission_rows(
    rows: Sequence[Mapping[str, object]],
    class_labels: Sequence[str],
) -> None:
    """Validate submission rows against the synthetic BirdCLEF contract."""
    if not class_labels:
        raise SubmissionValidationError("class_labels must not be empty")
    if not rows:
        raise SubmissionValidationError("rows must not be empty")

    expected_columns = _expected_columns(class_labels)
    seen_row_ids: set[str] = set()

    for index, row in enumerate(rows):
        if "row_id" not in row:
            raise SubmissionValidationError(f"row {index} is missing row_id")

        row_id = row["row_id"]
        if not isinstance(row_id, str):
            raise SubmissionValidationError(f"row {index} row_id must be a string")
        if row_id in seen_row_ids:
            raise SubmissionValidationError(f"duplicate row_id: {row_id!r}")
        seen_row_ids.add(row_id)
        _parse_row_id_end_time(row_id)

        row_columns = list(row.keys())
        if row_columns != expected_columns:
            missing = [column for column in expected_columns if column not in row]
            extra = [column for column in row_columns if column not in expected_columns]
            if missing:
                raise SubmissionValidationError(
                    f"row {index} missing expected columns: {', '.join(missing)}"
                )
            if extra:
                raise SubmissionValidationError(
                    f"row {index} has unexpected columns: {', '.join(extra)}"
                )

        for label in class_labels:
            value = row[label]
            if isinstance(value, bool) or not isinstance(value, int | float):
                raise SubmissionValidationError(
                    f"row {index} column {label!r} must be numeric, got {type(value).__name__}"
                )
            if not 0.0 <= float(value) <= 1.0:
                raise SubmissionValidationError(
                    f"row {index} column {label!r} must be in [0, 1], got {value!r}"
                )


def is_safe_submission_output_path(
    output_path: Path,
    repo_root: Path = REPO_ROOT,
) -> bool:
    """Return True when output_path is not the prohibited repo-root submission.csv."""
    return output_path.resolve() != (repo_root / "submission.csv").resolve()


def write_submission_csv(
    rows: Sequence[Mapping[str, object]],
    output_path: Path,
    class_labels: Sequence[str],
) -> Path:
    """Write validated submission rows to CSV using stdlib csv."""
    validate_submission_rows(rows, class_labels)
    if not is_safe_submission_output_path(output_path):
        raise UnsafeSubmissionPathError(
            "refusing to write submission.csv at repository root; "
            "use tmp/submissions/submission.csv or a pytest temp directory"
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = _expected_columns(class_labels)

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row[column] for column in fieldnames})

    return output_path
