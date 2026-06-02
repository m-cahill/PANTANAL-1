#!/usr/bin/env python
"""Generate a zero-baseline synthetic submission.csv to a safe output path."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT))

from pantanal_1.submission_contract import (  # noqa: E402
    build_zero_submission_rows,
    write_submission_csv,
)
from tests.fixtures.synthetic_submission_schema import (  # noqa: E402
    synthetic_class_labels,
    synthetic_soundscape_stems,
)

DEFAULT_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "submission.csv"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a zero-baseline synthetic submission.csv artifact."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output CSV path (default: tmp/submissions/submission.csv)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    class_labels = synthetic_class_labels()
    rows = build_zero_submission_rows(synthetic_soundscape_stems(), class_labels)
    output_path = write_submission_csv(rows, args.output, class_labels)
    print(f"Wrote zero-baseline submission to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
