#!/usr/bin/env python
"""Mirror M10 uniform-epsilon nonzero baseline locally (synthetic default; optional sample)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from pantanal_1.nonzero_baseline import (  # noqa: E402
    DEFAULT_EPSILON,
    EpsilonValidationError,
    build_synthetic_nonzero_fieldnames_and_rows,
    validate_epsilon,
    write_nonzero_baseline_from_sample,
    write_synthetic_nonzero_baseline,
)
from pantanal_1.sample_baseline import read_sample_submission_csv  # noqa: E402

DEFAULT_SYNTHETIC_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m10_nonzero_baseline.csv"
DEFAULT_SAMPLE_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m10_sample_nonzero_baseline.csv"


def _tmp_guard(output_path: Path) -> bool:
    return str(output_path.resolve()).startswith(str((REPO_ROOT / "tmp").resolve()))


def _print_diagnostics(
    mode: str,
    output_path: Path,
    epsilon: float,
    fieldnames: list[str],
    row_count: int,
    first_row_id: str = "(none)",
) -> None:
    header_preview = ",".join(fieldnames[:5])
    if len(fieldnames) > 5:
        header_preview += ",..."
    size = output_path.stat().st_size if output_path.is_file() else 0
    print(f"M10 local mode: {mode}")
    print(f"M10 local row_count: {row_count}")
    print(f"M10 local column_count: {len(fieldnames)}")
    print(f"M10 local epsilon: {epsilon}")
    print(f"M10 local first_row_id: {first_row_id}")
    print(f"M10 local header_preview: {header_preview}")
    print(f"M10 local output_path: {output_path}")
    print(f"M10 local file_size_bytes: {size}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="M10 local nonzero baseline: synthetic default or optional real sample file."
    )
    parser.add_argument(
        "--sample-submission",
        type=Path,
        default=None,
        help=(
            "Path to real sample_submission.csv on local disk only; must not be committed to git."
        ),
    )
    parser.add_argument(
        "--epsilon",
        type=float,
        default=DEFAULT_EPSILON,
        help="Uniform class probability (default 0.001); must satisfy 0 < epsilon <= 1.",
    )
    args = parser.parse_args()

    try:
        epsilon = validate_epsilon(args.epsilon)
    except EpsilonValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.sample_submission is not None:
        output = DEFAULT_SAMPLE_OUTPUT
        if not _tmp_guard(output):
            print("ERROR: sample output must be under tmp/", file=sys.stderr)
            return 1
        result = write_nonzero_baseline_from_sample(
            args.sample_submission.resolve(),
            output,
            epsilon=epsilon,
        )
        fieldnames, sample_rows = read_sample_submission_csv(args.sample_submission.resolve())
        first_id = sample_rows[0]["row_id"] if sample_rows else "(none)"
        _print_diagnostics(
            "REAL_SAMPLE_UNIFORM_EPSILON",
            result,
            epsilon,
            list(fieldnames),
            len(sample_rows),
            first_row_id=first_id,
        )
        return 0

    output = DEFAULT_SYNTHETIC_OUTPUT
    if not _tmp_guard(output):
        print("ERROR: default output must be under tmp/", file=sys.stderr)
        return 1
    result = write_synthetic_nonzero_baseline(output, epsilon=epsilon)
    fieldnames, rows = build_synthetic_nonzero_fieldnames_and_rows(epsilon=epsilon)
    first_id = rows[0]["row_id"] if rows else "(none)"
    _print_diagnostics(
        "SYNTHETIC_UNIFORM_EPSILON",
        result,
        epsilon,
        fieldnames,
        len(rows),
        first_row_id=first_id,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
