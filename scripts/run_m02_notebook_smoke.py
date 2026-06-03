#!/usr/bin/env python
"""Mirror M02 notebook smoke logic: generate and validate a synthetic submission CSV."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from pantanal_1.submission_contract import (  # noqa: E402
    build_zero_submission_rows,
    validate_submission_rows,
    write_submission_csv,
)
from pantanal_1.synthetic_schema import (  # noqa: E402
    SYNTHETIC_CLASS_LABELS,
    SYNTHETIC_SOUNDSCAPE_STEMS,
)

DEFAULT_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m02_smoke_submission.csv"


def main() -> int:
    class_labels = list(SYNTHETIC_CLASS_LABELS)
    stems = list(SYNTHETIC_SOUNDSCAPE_STEMS)
    rows = build_zero_submission_rows(stems, class_labels)
    validate_submission_rows(rows, class_labels)
    output_path = write_submission_csv(rows, DEFAULT_OUTPUT, class_labels)
    print(f"M02 smoke: wrote and validated submission at {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
