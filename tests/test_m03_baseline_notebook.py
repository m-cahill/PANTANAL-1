"""Static structure and safety tests for M03 baseline Kaggle notebook."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.verify_repo_state import find_violations

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "pantanal_1_m03_baseline.ipynb"
BASELINE_SCRIPT = REPO_ROOT / "scripts" / "run_m03_baseline_local.py"
M03_SYNTHETIC_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m03_synthetic_baseline.csv"

REQUIRED_MARKDOWN_PHRASES = (
    "m03 baseline notebook",
    "zero baseline",
    "does not prove model inference",
    "does not prove leaderboard",
    "synthetic fallback",
)

REQUIRED_CODE_SNIPPETS = (
    "REAL_SAMPLE_ZERO_BASELINE",
    "SYNTHETIC_FALLBACK_ONLY",
    "sample_submission.csv",
    "/kaggle/input",
    "/kaggle/working/submission.csv",
    "tmp/submissions/m03_synthetic_baseline.csv",
    "KAGGLE_KERNEL_RUN_TYPE",
    "find_sample_submission_path",
)

KAGGLE_DEBUG_SNIPPETS = (
    "=== PANTANAL-1 M03 Baseline Inference Debug ===",
    "KAGGLE_URL_BASE",
    "/kaggle/working",
    "runtime seconds",
)

NON_CLAIM_SNIPPETS = (
    "does not prove leaderboard submission or score",
    "No real Kaggle submission path was proven",
)


def _load_notebook() -> dict:
    with NOTEBOOK_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def _notebook_source_text(notebook: dict) -> str:
    parts: list[str] = []
    for cell in notebook.get("cells", []):
        source = cell.get("source", "")
        if isinstance(source, list):
            parts.append("".join(source))
        else:
            parts.append(str(source))
    return "\n".join(parts)


@pytest.fixture
def notebook() -> dict:
    return _load_notebook()


def test_m03_notebook_file_exists() -> None:
    assert NOTEBOOK_PATH.is_file()


def test_m03_notebook_json_parses(notebook: dict) -> None:
    assert notebook.get("nbformat") == 4
    assert "cells" in notebook


def test_m03_notebook_outputs_are_cleared(notebook: dict) -> None:
    for cell in notebook["cells"]:
        assert cell.get("outputs") in (None, [])


def test_m03_notebook_execution_counts_are_null_or_absent(notebook: dict) -> None:
    for cell in notebook["cells"]:
        if "execution_count" in cell:
            assert cell["execution_count"] is None


def test_m03_notebook_contains_required_safety_language(notebook: dict) -> None:
    text = _notebook_source_text(notebook).lower()
    for phrase in REQUIRED_MARKDOWN_PHRASES:
        assert phrase.lower() in text, f"missing phrase: {phrase}"


def test_m03_notebook_contains_kaggle_bible_debug_strings(notebook: dict) -> None:
    source = _notebook_source_text(notebook)
    for snippet in KAGGLE_DEBUG_SNIPPETS:
        assert snippet in source, f"missing debug: {snippet}"


def test_m03_notebook_distinguishes_baseline_modes(notebook: dict) -> None:
    source = _notebook_source_text(notebook)
    for snippet in REQUIRED_CODE_SNIPPETS:
        assert snippet in source, f"missing snippet: {snippet}"


def test_m03_notebook_preserves_non_claims(notebook: dict) -> None:
    source = _notebook_source_text(notebook)
    for snippet in NON_CLAIM_SNIPPETS:
        assert snippet in source, f"missing non-claim: {snippet}"


def test_m03_notebook_does_not_embed_large_outputs(notebook: dict) -> None:
    raw = NOTEBOOK_PATH.read_text(encoding="utf-8")
    assert "image/png" not in raw
    for cell in notebook["cells"]:
        for output in cell.get("outputs") or []:
            data = output.get("data", {})
            for value in data.values():
                if isinstance(value, str) and len(value) > 500:
                    pytest.fail("large embedded output")


def test_m03_baseline_script_exists() -> None:
    assert BASELINE_SCRIPT.is_file()


def test_m03_local_script_writes_synthetic_under_tmp() -> None:
    if M03_SYNTHETIC_OUTPUT.exists():
        M03_SYNTHETIC_OUTPUT.unlink()

    result = subprocess.run(
        [sys.executable, str(BASELINE_SCRIPT)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SYNTHETIC_FALLBACK_ONLY" in result.stdout
    assert M03_SYNTHETIC_OUTPUT.is_file()
    assert M03_SYNTHETIC_OUTPUT.resolve().is_relative_to((REPO_ROOT / "tmp").resolve())

    M03_SYNTHETIC_OUTPUT.unlink()
    assert find_violations(REPO_ROOT) == []


def test_m03_local_script_sample_mode(tmp_path: Path) -> None:
    sample = tmp_path / "sample_submission.csv"
    sample.write_text("row_id,class_x\nr1,0.5\n", encoding="utf-8")
    out = REPO_ROOT / "tmp" / "submissions" / "m03_sample_zero_baseline.csv"
    if out.exists():
        out.unlink()

    result = subprocess.run(
        [
            sys.executable,
            str(BASELINE_SCRIPT),
            "--sample-submission",
            str(sample),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert out.is_file()
    assert "REAL_SAMPLE_ZERO_BASELINE" in result.stdout
    out.unlink()


def test_repo_verifier_passes_without_m03_artifacts() -> None:
    for path in (
        M03_SYNTHETIC_OUTPUT,
        REPO_ROOT / "tmp" / "submissions" / "m03_sample_zero_baseline.csv",
    ):
        if path.exists():
            path.unlink()
    assert find_violations(REPO_ROOT) == []
