#!/usr/bin/env python
"""Mirror M03 baseline notebook logic locally (synthetic default; optional real sample path)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from pantanal_1.sample_baseline import (  # noqa: E402
    build_zero_rows_from_sample,
    read_sample_submission_csv,
    write_submission_csv_with_fieldnames,
)
from pantanal_1.submission_contract import (  # noqa: E402
    build_zero_submission_rows,
    validate_submission_rows,
    write_submission_csv,
)
from pantanal_1.synthetic_schema import (  # noqa: E402
    SYNTHETIC_CLASS_LABELS,
    SYNTHETIC_SOUNDSCAPE_STEMS,
)

DEFAULT_SYNTHETIC_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m03_synthetic_baseline.csv"
DEFAULT_SAMPLE_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m03_sample_zero_baseline.csv"


def run_synthetic(output_path: Path) -> Path:
    """Generate synthetic M01/M02-style zero baseline under tmp/."""
    class_labels = list(SYNTHETIC_CLASS_LABELS)
    stems = list(SYNTHETIC_SOUNDSCAPE_STEMS)
    rows = build_zero_submission_rows(stems, class_labels)
    validate_submission_rows(rows, class_labels)
    return write_submission_csv(rows, output_path, class_labels)


def run_from_sample(sample_path: Path, output_path: Path) -> Path:
    """Generate zero baseline from a local sample_submission.csv (must not be in git)."""
    fieldnames, sample_rows = read_sample_submission_csv(sample_path.resolve())
    rows = build_zero_rows_from_sample(fieldnames, sample_rows)
    return write_submission_csv_with_fieldnames(rows, output_path, fieldnames)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="M03 local baseline: synthetic default or optional real sample file."
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
        "--output",
        type=Path,
        default=None,
        help="Output CSV path (must be under tmp/ for repo safety).",
    )
    args = parser.parse_args()

    if args.sample_submission is not None:
        output = args.output or DEFAULT_SAMPLE_OUTPUT
        if not str(output.resolve()).startswith(str((REPO_ROOT / "tmp").resolve())):
            print("ERROR: --output must be under tmp/ when using repo layout", file=sys.stderr)
            return 1
        result = run_from_sample(args.sample_submission, output)
        print(f"M03 local: REAL_SAMPLE_ZERO_BASELINE from {args.sample_submission}")
        print(f"M03 local: wrote {result}")
        return 0

    output = args.output or DEFAULT_SYNTHETIC_OUTPUT
    if not str(output.resolve()).startswith(str((REPO_ROOT / "tmp").resolve())):
        print("ERROR: default and --output must be under tmp/", file=sys.stderr)
        return 1
    result = run_synthetic(output)
    print("M03 local: SYNTHETIC_FALLBACK_ONLY")
    print(f"M03 local: wrote {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
