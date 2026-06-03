"""Static structure and safety tests for M11 non-zero baseline Kaggle notebook."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "pantanal_1_m11_nonzero_baseline.ipynb"
M03_NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "pantanal_1_m03_baseline.ipynb"

REQUIRED_MARKDOWN_PHRASES = (
    "m11 nonzero baseline notebook",
    "uniform epsilon",
    "does not prove model inference",
    "record public score only if shown by kaggle",
    "synthetic fallback",
)

REQUIRED_CODE_SNIPPETS = (
    "REAL_SAMPLE_NONZERO_BASELINE",
    "SYNTHETIC_FALLBACK_ONLY",
    "EPSILON = 0.001",
    "sample_submission.csv",
    "/kaggle/input",
    "/kaggle/working/submission.csv",
    "tmp/submissions/m11_synthetic_nonzero_baseline.csv",
    "KAGGLE_KERNEL_RUN_TYPE",
    "find_sample_submission_path",
    "build_uniform_nonzero_rows",
    "inline fallback",
)

KAGGLE_DEBUG_SNIPPETS = (
    "=== PANTANAL-1 M11 Non-Zero Baseline Debug ===",
    "KAGGLE_URL_BASE",
    "/kaggle/working",
    "runtime seconds",
)

NON_CLAIM_SNIPPETS = (
    "does not prove model inference or model quality",
    "does not prove score improvement",
    "No real Kaggle submission path was proven",
    "Record public score only if shown by Kaggle",
)


def _load_notebook(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
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
    return _load_notebook(NOTEBOOK_PATH)


def test_m11_notebook_file_exists() -> None:
    assert NOTEBOOK_PATH.is_file()


def test_m11_notebook_json_parses(notebook: dict) -> None:
    assert notebook.get("nbformat") == 4
    assert "cells" in notebook


def test_m11_notebook_outputs_are_cleared(notebook: dict) -> None:
    for cell in notebook["cells"]:
        assert cell.get("outputs") in (None, [])


def test_m11_notebook_execution_counts_are_null_or_absent(notebook: dict) -> None:
    for cell in notebook["cells"]:
        if "execution_count" in cell:
            assert cell["execution_count"] is None


def test_m11_notebook_contains_required_safety_language(notebook: dict) -> None:
    text = _notebook_source_text(notebook).lower()
    for phrase in REQUIRED_MARKDOWN_PHRASES:
        assert phrase.lower() in text, f"missing phrase: {phrase}"


def test_m11_notebook_contains_kaggle_debug_strings(notebook: dict) -> None:
    source = _notebook_source_text(notebook)
    for snippet in KAGGLE_DEBUG_SNIPPETS:
        assert snippet in source, f"missing debug: {snippet}"


def test_m11_notebook_distinguishes_baseline_modes(notebook: dict) -> None:
    source = _notebook_source_text(notebook)
    for snippet in REQUIRED_CODE_SNIPPETS:
        assert snippet in source, f"missing snippet: {snippet}"


def test_m11_notebook_preserves_non_claims(notebook: dict) -> None:
    source = _notebook_source_text(notebook)
    for snippet in NON_CLAIM_SNIPPETS:
        assert snippet in source, f"missing non-claim: {snippet}"


def test_m11_notebook_does_not_embed_large_outputs(notebook: dict) -> None:
    raw = NOTEBOOK_PATH.read_text(encoding="utf-8")
    assert "image/png" not in raw
    for cell in notebook["cells"]:
        for output in cell.get("outputs") or []:
            data = output.get("data", {})
            for value in data.values():
                if isinstance(value, str) and len(value) > 500:
                    pytest.fail("large embedded output")


def test_m03_notebook_unchanged_path_still_exists() -> None:
    assert M03_NOTEBOOK_PATH.is_file()


def test_m03_notebook_still_zero_baseline_mode() -> None:
    source = _notebook_source_text(_load_notebook(M03_NOTEBOOK_PATH))
    assert "REAL_SAMPLE_ZERO_BASELINE" in source
    assert "REAL_SAMPLE_NONZERO_BASELINE" not in source
