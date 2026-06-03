"""Tests for M10 uniform-epsilon nonzero baseline module, script, and governance."""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

import pytest

from pantanal_1.nonzero_baseline import (
    DEFAULT_EPSILON,
    EpsilonValidationError,
    build_synthetic_nonzero_fieldnames_and_rows,
    build_uniform_nonzero_rows,
    format_probability_string,
    validate_epsilon,
    validate_nonzero_sample_rows,
    write_nonzero_baseline_from_sample,
)
from pantanal_1.synthetic_schema import SYNTHETIC_CLASS_LABELS
from scripts.verify_repo_state import find_violations

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "src" / "pantanal_1" / "nonzero_baseline.py"
LOCAL_SCRIPT = REPO_ROOT / "scripts" / "run_m10_nonzero_baseline_local.py"
DOC_PATH = REPO_ROOT / "docs" / "kaggle" / "nonzero_baseline.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"
M10_SYNTHETIC_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m10_nonzero_baseline.csv"
M10_SAMPLE_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m10_sample_nonzero_baseline.csv"


def test_m10_nonzero_baseline_module_exists() -> None:
    assert MODULE_PATH.is_file()


def test_uniform_nonzero_preserves_row_count_and_order(tmp_path: Path) -> None:
    sample = tmp_path / "sample_submission.csv"
    sample.write_text(
        "row_id,species_a,species_b\nid_5,0.1,0.2\nid_10,0.3,0.4\n",
        encoding="utf-8",
    )
    with sample.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        sample_rows = list(reader)

    rows = build_uniform_nonzero_rows(sample_rows, fieldnames)
    assert len(rows) == len(sample_rows)
    assert [r["row_id"] for r in rows] == ["id_5", "id_10"]
    assert list(rows[0].keys()) == fieldnames


def test_header_and_row_id_preserved(tmp_path: Path) -> None:
    fieldnames = ["row_id", "class_x", "class_y"]
    sample_rows = [{"row_id": "a_5"}, {"row_id": "b_10"}]
    rows = build_uniform_nonzero_rows(sample_rows, fieldnames, epsilon=0.001)
    validate_nonzero_sample_rows(rows, fieldnames, epsilon=0.001)
    assert rows[0]["row_id"] == "a_5"
    assert rows[1]["class_y"] == "0.001"


def test_class_values_are_float_strings_in_range() -> None:
    prob = format_probability_string(DEFAULT_EPSILON)
    assert prob == "0.001"
    value = float(prob)
    assert 0.0 < value <= 1.0


def test_default_epsilon_is_deterministic() -> None:
    fieldnames, rows_a = build_synthetic_nonzero_fieldnames_and_rows()
    fieldnames_b, rows_b = build_synthetic_nonzero_fieldnames_and_rows()
    assert fieldnames == fieldnames_b
    assert rows_a == rows_b
    assert rows_a[0][SYNTHETIC_CLASS_LABELS[0]] == "0.001"


def test_custom_epsilon(tmp_path: Path) -> None:
    fieldnames = ["row_id", "class_a"]
    rows = build_uniform_nonzero_rows([{"row_id": "r1"}], fieldnames, epsilon=0.05)
    assert rows[0]["class_a"] == "0.05"
    validate_nonzero_sample_rows(rows, fieldnames, epsilon=0.05)


def test_epsilon_validation_rejects_invalid() -> None:
    with pytest.raises(EpsilonValidationError):
        validate_epsilon(0.0)
    with pytest.raises(EpsilonValidationError):
        validate_epsilon(-0.001)
    with pytest.raises(EpsilonValidationError):
        validate_epsilon(1.1)


def test_write_from_sample_round_trip(tmp_path: Path) -> None:
    sample = tmp_path / "sample_submission.csv"
    sample.write_text("row_id,class_x\nr1,0.5\n", encoding="utf-8")
    out = tmp_path / "out" / "baseline.csv"
    write_nonzero_baseline_from_sample(sample, out)
    with out.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames == ["row_id", "class_x"]
        row = next(reader)
        assert row["row_id"] == "r1"
        assert float(row["class_x"]) == DEFAULT_EPSILON


def test_synthetic_schema_row_count() -> None:
    fieldnames, rows = build_synthetic_nonzero_fieldnames_and_rows()
    assert len(fieldnames) == 235
    assert len(rows) == 24


def test_m10_local_script_exists() -> None:
    assert LOCAL_SCRIPT.is_file()


def test_m10_local_script_writes_under_tmp_not_root() -> None:
    root_submission = REPO_ROOT / "submission.csv"
    if root_submission.exists():
        root_submission.unlink()

    for path in (M10_SYNTHETIC_OUTPUT, M10_SAMPLE_OUTPUT):
        if path.exists():
            path.unlink()

    result = subprocess.run(
        [sys.executable, str(LOCAL_SCRIPT)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SYNTHETIC_UNIFORM_EPSILON" in result.stdout
    assert M10_SYNTHETIC_OUTPUT.is_file()
    assert not root_submission.exists()
    assert M10_SYNTHETIC_OUTPUT.resolve().is_relative_to((REPO_ROOT / "tmp").resolve())

    M10_SYNTHETIC_OUTPUT.unlink()
    assert find_violations(REPO_ROOT) == []


def test_m10_local_script_custom_epsilon() -> None:
    if M10_SYNTHETIC_OUTPUT.exists():
        M10_SYNTHETIC_OUTPUT.unlink()

    result = subprocess.run(
        [sys.executable, str(LOCAL_SCRIPT), "--epsilon", "0.002"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0.002" in result.stdout
    assert M10_SYNTHETIC_OUTPUT.is_file()
    text = M10_SYNTHETIC_OUTPUT.read_text(encoding="utf-8")
    assert "0.002" in text
    M10_SYNTHETIC_OUTPUT.unlink()


def test_m10_nonzero_baseline_doc_exists() -> None:
    assert DOC_PATH.is_file()
    text = DOC_PATH.read_text(encoding="utf-8")
    assert "What M10 Proves" in text
    assert "What M10 Does Not Prove" in text
    assert "Uniform epsilon" in text or "uniform" in text.lower()


def test_pantanal_marks_m10_closed() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1]
    assert "| M10 |" in ledger
    assert "closed" in ledger.lower()


def test_pantanal_m10_narrow_claim_and_non_claims() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "deterministic non-zero baseline generator" in text
    lower = text.lower()
    assert "m10 does not implement trained model inference" in lower
    assert "m10 does not prove audio understanding" in lower
    assert "m10 does not prove model quality" in lower
    assert "m10 does not claim rediai certification" in lower


def test_pantanal_does_not_claim_m10_score_improvement() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    claims = text.split("## 8. current claims", 1)[-1]
    implemented = claims.split("**not yet proven:**", 1)[0]
    assert "leaderboard improvement" not in implemented or "does not improve" in text
    assert "m10 does not improve leaderboard score" in text
