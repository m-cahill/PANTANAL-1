"""Tests for package-level synthetic schema helpers."""

from __future__ import annotations

from pantanal_1.synthetic_schema import (
    SYNTHETIC_CLASS_COUNT,
    SYNTHETIC_CLASS_LABELS,
    SYNTHETIC_SOUNDSCAPE_STEMS,
    synthetic_class_labels,
    synthetic_soundscape_stems,
)
from tests.fixtures.synthetic_submission_schema import (
    SYNTHETIC_CLASS_LABELS as FIXTURE_CLASS_LABELS,
)
from tests.fixtures.synthetic_submission_schema import (
    synthetic_class_labels as fixture_class_labels,
)


def test_synthetic_class_labels_count_is_234() -> None:
    assert len(SYNTHETIC_CLASS_LABELS) == 234
    assert len(synthetic_class_labels()) == SYNTHETIC_CLASS_COUNT


def test_synthetic_class_labels_match_fixture_reexport() -> None:
    assert list(SYNTHETIC_CLASS_LABELS) == list(FIXTURE_CLASS_LABELS)
    assert fixture_class_labels() == synthetic_class_labels()


def test_synthetic_soundscape_stems_non_empty() -> None:
    stems = synthetic_soundscape_stems()
    assert len(SYNTHETIC_SOUNDSCAPE_STEMS) == 2
    assert len(stems) == 2
    assert all(stem for stem in stems)
