"""Tests for M14 audio-derived baseline evidence contract (docs/governance/validator)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

M14_PLAN = REPO_ROOT / "docs" / "milestones" / "M14" / "M14_plan.md"
MANIFEST_SCHEMA = REPO_ROOT / "docs" / "models" / "M14_MODEL_MANIFEST_SCHEMA.md"
MODEL_CARD_TEMPLATE = REPO_ROOT / "docs" / "models" / "M14_model_card_template.md"
PRIVATE_RUNBOOK = REPO_ROOT / "docs" / "analysis" / "M14_private_training_runbook.md"
EVIDENCE_CONTRACT = REPO_ROOT / "docs" / "analysis" / "M14_evidence_contract.md"
VALIDATION_SCHEMA = REPO_ROOT / "schemas" / "m14_validation_summary.schema.json"
FIXTURE_PLANNING = REPO_ROOT / "fixtures" / "m14" / "validation_summary_planning_only.json"
FIXTURE_SYNTHETIC = REPO_ROOT / "fixtures" / "m14" / "validation_summary_nonconstant_example.json"
VALIDATOR_SCRIPT = REPO_ROOT / "scripts" / "validate_m14_evidence.py"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"
REQUIREMENTS = REPO_ROOT / "requirements.txt"
REQUIREMENTS_DEV = REPO_ROOT / "requirements-dev.txt"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"

MANIFEST_REQUIRED_FIELDS = (
    "manifest_version",
    "model_id",
    "display_name",
    "status",
    "source.training_lane",
    "source.pretrained_backbone",
    "source.backbone_license",
    "artifacts[]",
    "training_eval_context",
    "kaggle_packaging",
    "provenance",
)

MANIFEST_STATUSES = ("planning-only", "private-trained-summary", "owner-approved-binary")


def _run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(path)],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        check=False,
    )


def _load_fixture(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# --- Deliverable existence ---


def test_m14_plan_exists() -> None:
    assert M14_PLAN.is_file()
    text = M14_PLAN.read_text(encoding="utf-8").lower()
    assert "evidence contract" in text
    assert "does not train a model" in text or "not train" in text


def test_m14_model_manifest_schema_exists() -> None:
    assert MANIFEST_SCHEMA.is_file()


def test_m14_model_card_template_exists() -> None:
    assert MODEL_CARD_TEMPLATE.is_file()


def test_m14_private_training_runbook_exists() -> None:
    assert PRIVATE_RUNBOOK.is_file()


def test_m14_evidence_contract_exists() -> None:
    assert EVIDENCE_CONTRACT.is_file()


def test_m14_validation_schema_exists() -> None:
    assert VALIDATION_SCHEMA.is_file()
    schema = json.loads(VALIDATION_SCHEMA.read_text(encoding="utf-8"))
    required = schema.get("required", [])
    assert "non_constant_predictions_verified" in required


def test_m14_fixtures_exist() -> None:
    assert FIXTURE_PLANNING.is_file()
    assert FIXTURE_SYNTHETIC.is_file()


def test_m14_validator_script_exists() -> None:
    assert VALIDATOR_SCRIPT.is_file()


# --- Manifest schema ---


def test_manifest_schema_includes_required_fields() -> None:
    text = MANIFEST_SCHEMA.read_text(encoding="utf-8")
    for field in MANIFEST_REQUIRED_FIELDS:
        needle = field.replace("[]", "").replace("source.", "")
        assert needle in text or field in text, f"missing {field}"
    assert "source" in text
    assert "training_lane" in text


def test_manifest_schema_distinguishes_status_values() -> None:
    text = MANIFEST_SCHEMA.read_text(encoding="utf-8").lower()
    for status in MANIFEST_STATUSES:
        assert status in text


# --- Model card template ---


def test_model_card_template_has_limitations_and_non_claims() -> None:
    text = MODEL_CARD_TEMPLATE.read_text(encoding="utf-8").lower()
    assert "limitations" in text
    assert "non-claims" in text or "non-claims" in text
    assert "no private paths" in text or "no raw data" in text


# --- Runbook boundary ---


def test_runbook_preserves_private_public_boundary() -> None:
    text = PRIVATE_RUNBOOK.read_text(encoding="utf-8").lower()
    assert "ornithos" in text
    assert "private" in text
    assert "pantanal" in text
    assert "primary" in text and "embedding" in text
    assert "mel-spectrogram" in text or "mel" in text
    assert "does not include runnable commands" in text or "public-safe" in text


def test_runbook_defines_phases() -> None:
    text = PRIVATE_RUNBOOK.read_text(encoding="utf-8").lower()
    for phase in (
        "license screen",
        "candidate selection",
        "oof",
        "non-constant",
        "cpu export",
        "manifest",
        "ingest review",
    ):
        assert phase in text, f"missing phase keyword: {phase}"


# --- Evidence contract prohibitions ---


def test_evidence_contract_prohibits_sensitive_artifacts() -> None:
    text = EVIDENCE_CONTRACT.read_text(encoding="utf-8").lower()
    assert "raw audio" in text or "audio files" in text
    assert "kaggle competition" in text or "competition csv" in text
    assert "weight" in text or "binary" in text
    assert "ornithos" in text
    assert "submission.csv" in text


# --- Validator fixtures ---


def test_planning_only_fixture_validates() -> None:
    result = _run_validator(FIXTURE_PLANNING)
    assert result.returncode == 0, result.stderr


def test_synthetic_nonconstant_fixture_validates() -> None:
    result = _run_validator(FIXTURE_SYNTHETIC)
    assert result.returncode == 0, result.stderr
    data = _load_fixture(FIXTURE_SYNTHETIC)
    assert data.get("synthetic") is True


def test_planning_fixture_does_not_imply_training_or_quality() -> None:
    data = _load_fixture(FIXTURE_PLANNING)
    assert data["status"] == "planning_only"
    assert data["non_constant_predictions_verified"] is False
    assert data["metrics"]["macro_roc_auc"] is None
    summary = data["prediction_summary"].lower()
    assert "planning" in summary
    assert "score improvement" not in summary


# --- Validator rejection ---


def test_validator_rejects_missing_required_fields(tmp_path: Path) -> None:
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"model_id": "x"}), encoding="utf-8")
    result = _run_validator(bad)
    assert result.returncode != 0
    assert "missing required field" in result.stderr.lower()


def test_validator_rejects_score_improvement_in_planning_only(tmp_path: Path) -> None:
    data = _load_fixture(FIXTURE_PLANNING)
    data["prediction_summary"] = "We observed score improvement on the leaderboard."
    bad = tmp_path / "overclaim.json"
    bad.write_text(json.dumps(data), encoding="utf-8")
    result = _run_validator(bad)
    assert result.returncode != 0
    assert (
        "forbidden phrase" in result.stderr.lower() or "score improvement" in result.stderr.lower()
    )


def test_validator_rejects_non_constant_true_when_planning_only(tmp_path: Path) -> None:
    data = _load_fixture(FIXTURE_PLANNING)
    data["non_constant_predictions_verified"] = True
    bad = tmp_path / "nc_true.json"
    bad.write_text(json.dumps(data), encoding="utf-8")
    result = _run_validator(bad)
    assert result.returncode != 0


# --- Dependency and notebook posture ---


def test_no_audio_ml_dependencies_introduced() -> None:
    banned = (
        "torch",
        "librosa",
        "torchaudio",
        "transformers",
        "timm",
        "sklearn",
        "pandas",
        "numpy",
        "xgboost",
        "lightgbm",
        "onnxruntime",
        "jsonschema",
    )
    for req_file in (REQUIREMENTS, REQUIREMENTS_DEV):
        if req_file.is_file():
            content = req_file.read_text(encoding="utf-8").lower()
            for name in banned:
                assert name not in content, f"{name} found in {req_file.name}"


def test_m14_does_not_modify_kaggle_notebooks() -> None:
    if not NOTEBOOKS_DIR.is_dir():
        return
    for nb in NOTEBOOKS_DIR.glob("*.ipynb"):
        text = nb.read_text(encoding="utf-8").lower()
        assert "m14_evidence" not in text
        assert "validate_m14" not in text


def test_validator_does_not_import_audio_ml() -> None:
    text = VALIDATOR_SCRIPT.read_text(encoding="utf-8").lower()
    for mod in ("torch", "librosa", "numpy", "pandas", "sklearn"):
        assert f"import {mod}" not in text


# --- Ultimate Truth ---


def test_pantanal_marks_m14_closed() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    assert "| M14 |" in ledger
    m14_row = ledger.split("| M14 |", 1)[-1].split("\n", 1)[0]
    assert "closed" in m14_row.lower()


def test_pantanal_m14_evidence_contract_claim() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "evidence contract" in text
    assert "m14" in text


def test_pantanal_m14_explicit_non_claims() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "m14 does not train a model" in text
    assert "m14 does not implement audio inference" in text
    assert "m14 does not add audio or ml dependencies" in text
    assert "m14 does not improve leaderboard score" in text
    assert "m14 does not prove model quality" in text
    assert "m14 does not claim rediai certification" in text
    assert "m14 does not create working-note readiness" in text


def test_pantanal_does_not_claim_training_or_quality_in_m14_block() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    if "m14 explicit non-claims" in text:
        block = text.split("m14 explicit non-claims", 1)[1].split("## 9.", 1)[0]
        assert "m14 does not train a model" in block
        assert "score improvement" in block or "improve leaderboard" in block


def test_m14_plan_references_m13_authority_docs() -> None:
    text = M14_PLAN.read_text(encoding="utf-8")
    assert "M13_audio_baseline_strategy.md" in text
    assert "M13_artifact_boundary_plan.md" in text
