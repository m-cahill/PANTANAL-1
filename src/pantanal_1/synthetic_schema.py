"""Synthetic BirdCLEF+ 2026 submission schema (not from Kaggle taxonomy)."""

from __future__ import annotations

SYNTHETIC_CLASS_COUNT = 234

SYNTHETIC_SOUNDSCAPE_STEMS: tuple[str, ...] = (
    "BC2026_Test_0001_S05_20250227_010002",
    "BC2026_Test_0002_S05_20250227_010003",
)

DEFAULT_SOUNDSCAPE_DURATION_SECONDS = 60
DEFAULT_WINDOW_SECONDS = 5


def synthetic_class_labels(count: int = SYNTHETIC_CLASS_COUNT) -> list[str]:
    """Return synthetic class column names (e.g. synthetic_class_000 … synthetic_class_233)."""
    if count < 1:
        raise ValueError("count must be at least 1")
    width = max(3, len(str(count - 1)))
    return [f"synthetic_class_{index:0{width}d}" for index in range(count)]


def synthetic_soundscape_stems() -> list[str]:
    """Return synthetic soundscape filename stems for contract tests and smoke paths."""
    return list(SYNTHETIC_SOUNDSCAPE_STEMS)


SYNTHETIC_CLASS_LABELS: tuple[str, ...] = tuple(synthetic_class_labels())
