"""Static structure and safety tests for M02 Kaggle notebook smoke artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.verify_repo_state import find_violations

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "pantanal_1_m02_smoke.ipynb"
SMOKE_SCRIPT = REPO_ROOT / "scripts" / "run_m02_notebook_smoke.py"
M02_OUTPUT = REPO_ROOT / "tmp" / "submissions" / "m02_smoke_submission.csv"

REQUIRED_MARKDOWN_PHRASES = (
    "m02 smoke notebook",
    "synthetic labels only",
    "does not use kaggle competition data",
    "does not prove leaderboard readiness",
    "model inference",
)

REQUIRED_CODE_SNIPPETS = (
    "pantanal_1.submission_contract",
    "pantanal_1.synthetic_schema",
    "build_zero_submission_rows",
    "validate_submission_rows",
    "write_submission_csv",
    "tmp/submissions/m02_smoke_submission.csv",
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


def test_notebook_file_exists() -> None:
    assert NOTEBOOK_PATH.is_file()


def test_notebook_json_parses(notebook: dict) -> None:
    assert notebook.get("nbformat") == 4
    assert "cells" in notebook


def test_notebook_outputs_are_cleared(notebook: dict) -> None:
    for cell in notebook["cells"]:
        assert cell.get("outputs") in (None, []), "notebook cells must have cleared outputs"


def test_notebook_execution_counts_are_null_or_absent(notebook: dict) -> None:
    for cell in notebook["cells"]:
        if "execution_count" in cell:
            assert cell["execution_count"] is None


def test_notebook_contains_required_safety_language(notebook: dict) -> None:
    markdown_cells = [
        "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        for cell in notebook["cells"]
        if cell.get("cell_type") == "markdown"
    ]
    markdown_text = "\n".join(markdown_cells).lower()
    for phrase in REQUIRED_MARKDOWN_PHRASES:
        assert phrase.lower() in markdown_text, f"missing safety phrase: {phrase}"


def test_notebook_references_submission_contract(notebook: dict) -> None:
    source_text = _notebook_source_text(notebook)
    for snippet in REQUIRED_CODE_SNIPPETS:
        assert snippet in source_text, f"missing required snippet: {snippet}"


def test_notebook_does_not_write_root_submission_csv(notebook: dict) -> None:
    code_text = "\n".join(
        _notebook_source_text({"cells": [c]})
        for c in notebook["cells"]
        if c.get("cell_type") == "code"
    )
    assert 'Path("submission.csv")' not in code_text
    assert "tmp/submissions/m02_smoke_submission.csv" in code_text


def test_notebook_does_not_embed_large_base64_outputs(notebook: dict) -> None:
    raw = NOTEBOOK_PATH.read_text(encoding="utf-8")
    assert "image/png" not in raw
    assert "application/vnd.jupyter.widget-view" not in raw
    for cell in notebook["cells"]:
        for output in cell.get("outputs") or []:
            data = output.get("data", {})
            for value in data.values():
                if isinstance(value, str) and len(value) > 500:
                    pytest.fail("notebook embeds large output payload")


def test_smoke_script_exists() -> None:
    assert SMOKE_SCRIPT.is_file()


def test_m02_smoke_script_writes_under_tmp(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(REPO_ROOT)
    output = REPO_ROOT / "tmp" / "submissions" / "m02_smoke_submission.csv"
    if output.exists():
        output.unlink()

    result = subprocess.run(
        [sys.executable, str(SMOKE_SCRIPT)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert output.is_file()
    assert output.resolve().is_relative_to((REPO_ROOT / "tmp").resolve())

    output.unlink()
    violations = find_violations(REPO_ROOT)
    assert violations == []


def test_repo_verifier_passes_without_m02_smoke_artifact() -> None:
    if M02_OUTPUT.exists():
        M02_OUTPUT.unlink()
    assert find_violations(REPO_ROOT) == []
