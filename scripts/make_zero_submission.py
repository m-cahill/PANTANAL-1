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
from pantanal_1.synthetic_schema import (  # noqa: E402
    SYNTHETIC_CLASS_LABELS,
    SYNTHETIC_SOUNDSCAPE_STEMS,
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
    class_labels = list(SYNTHETIC_CLASS_LABELS)
    rows = build_zero_submission_rows(list(SYNTHETIC_SOUNDSCAPE_STEMS), class_labels)
    output_path = write_submission_csv(rows, args.output, class_labels)
    print(f"Wrote zero-baseline submission to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
