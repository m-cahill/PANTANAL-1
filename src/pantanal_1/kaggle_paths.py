"""Kaggle path discovery helpers (stdlib only)."""

from __future__ import annotations

import os
from collections.abc import Sequence
from pathlib import Path

KAGGLE_INPUT_ROOT = Path("/kaggle/input")
KAGGLE_WORKING_SUBMISSION = Path("/kaggle/working/submission.csv")

EXPLICIT_SAMPLE_SUBMISSION_CANDIDATES: tuple[Path, ...] = (
    Path("/kaggle/input/competitions/birdclef-2026/sample_submission.csv"),
    Path("/kaggle/input/birdclef-2026/sample_submission.csv"),
)

SAMPLE_SUBMISSION_FILENAME = "sample_submission.csv"


def is_kaggle_environment() -> bool:
    """Return True when typical Kaggle notebook environment signals are present."""
    if os.environ.get("KAGGLE_KERNEL_RUN_TYPE"):
        return True
    return Path("/kaggle").exists()


def candidate_sample_submission_paths() -> tuple[Path, ...]:
    """Return explicit, documented candidate paths for sample_submission.csv."""
    return EXPLICIT_SAMPLE_SUBMISSION_CANDIDATES


def discover_sample_submission_paths(
    root: Path = KAGGLE_INPUT_ROOT,
) -> tuple[Path, ...]:
    """Walk root and return every path named exactly sample_submission.csv."""
    if not root.exists():
        return ()

    discovered: list[Path] = []
    try:
        for path in sorted(root.rglob(SAMPLE_SUBMISSION_FILENAME)):
            if path.is_file():
                discovered.append(path)
    except OSError:
        return ()
    return tuple(discovered)


def find_first_existing_path(paths: Sequence[Path]) -> Path | None:
    """Return the first path in sequence that exists as a file."""
    for path in paths:
        if path.is_file():
            return path
    return None


def find_sample_submission_path() -> Path | None:
    """Resolve sample_submission.csv: explicit candidates, then discovery."""
    explicit = candidate_sample_submission_paths()
    discovered = discover_sample_submission_paths()
    all_candidates = (*explicit, *(p for p in discovered if p not in explicit))
    return find_first_existing_path(all_candidates)


def all_sample_submission_candidates() -> tuple[Path, ...]:
    """Return explicit candidates plus discovered paths (deduplicated, ordered)."""
    explicit = candidate_sample_submission_paths()
    discovered = discover_sample_submission_paths()
    seen: set[Path] = set()
    ordered: list[Path] = []
    for path in (*explicit, *discovered):
        if path not in seen:
            seen.add(path)
            ordered.append(path)
    return tuple(ordered)
