"""M00 repository sanity tests."""

from __future__ import annotations

from pathlib import Path

import pantanal_1

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_pantanal_1_ultimate_truth_exists() -> None:
    assert (REPO_ROOT / "docs" / "pantanal-1.md").is_file()


def test_m00_plan_exists() -> None:
    assert (REPO_ROOT / "docs" / "milestones" / "M00" / "M00_plan.md").is_file()


def test_m00_toolcalls_exists() -> None:
    assert (REPO_ROOT / "docs" / "milestones" / "M00" / "M00_toolcalls.md").is_file()


def test_pantanal_1_version_importable() -> None:
    assert pantanal_1.__version__ == "0.0.0"


def test_verify_repo_state_script_exists() -> None:
    assert (REPO_ROOT / "scripts" / "verify_repo_state.py").is_file()
