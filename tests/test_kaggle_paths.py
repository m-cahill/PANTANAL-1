"""Tests for Kaggle path discovery helpers."""

from __future__ import annotations

from pathlib import Path

import pytest

from pantanal_1.kaggle_paths import (
    candidate_sample_submission_paths,
    discover_sample_submission_paths,
    find_first_existing_path,
    find_sample_submission_path,
    is_kaggle_environment,
)


def test_candidate_sample_submission_paths_returns_explicit_paths() -> None:
    paths = candidate_sample_submission_paths()
    assert len(paths) == 2
    assert paths[0].name == "sample_submission.csv"
    assert "birdclef-2026" in paths[0].as_posix()


def test_discover_sample_submission_paths_finds_nested_file(tmp_path: Path) -> None:
    nested = tmp_path / "competitions" / "birdclef-2026"
    nested.mkdir(parents=True)
    sample = nested / "sample_submission.csv"
    sample.write_text("row_id,a\nx,0\n", encoding="utf-8")
    other = tmp_path / "other" / "sample_submission.csv"
    other.parent.mkdir(parents=True)
    other.write_text("row_id,b\ny,0\n", encoding="utf-8")

    discovered = discover_sample_submission_paths(tmp_path)
    assert len(discovered) == 2
    assert all(p.name == "sample_submission.csv" for p in discovered)


def test_find_first_existing_path(tmp_path: Path) -> None:
    missing = tmp_path / "missing.csv"
    present = tmp_path / "present.csv"
    present.write_text("x", encoding="utf-8")
    assert find_first_existing_path([missing, present]) == present
    assert find_first_existing_path([missing]) is None


def test_find_sample_submission_path_prefers_explicit(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    explicit_dir = tmp_path / "kaggle" / "input" / "competitions" / "birdclef-2026"
    explicit_dir.mkdir(parents=True)
    explicit_file = explicit_dir / "sample_submission.csv"
    explicit_file.write_text("row_id,c\nr,0\n", encoding="utf-8")

    monkeypatch.setattr(
        "pantanal_1.kaggle_paths.KAGGLE_INPUT_ROOT",
        tmp_path / "kaggle" / "input",
    )
    monkeypatch.setattr(
        "pantanal_1.kaggle_paths.EXPLICIT_SAMPLE_SUBMISSION_CANDIDATES",
        (
            tmp_path
            / "kaggle"
            / "input"
            / "competitions"
            / "birdclef-2026"
            / "sample_submission.csv",
            tmp_path / "kaggle" / "input" / "birdclef-2026" / "sample_submission.csv",
        ),
    )

    found = find_sample_submission_path()
    assert found == explicit_file


def test_is_kaggle_environment_false_locally(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KAGGLE_KERNEL_RUN_TYPE", raising=False)
    assert is_kaggle_environment() is False or Path("/kaggle").exists()
