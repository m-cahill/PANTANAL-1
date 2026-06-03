"""Tests for M13 audio-derived baseline planning gate (docs/governance only)."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

AUDIO_STRATEGY = REPO_ROOT / "docs" / "analysis" / "M13_audio_baseline_strategy.md"
BLACKWELL_PLAN = REPO_ROOT / "docs" / "analysis" / "M13_blackwell_training_plan.md"
ARTIFACT_BOUNDARY = REPO_ROOT / "docs" / "analysis" / "M13_artifact_boundary_plan.md"
KAGGLE_PACKAGING = REPO_ROOT / "docs" / "analysis" / "M13_kaggle_inference_packaging_plan.md"
EVALUATION_PLAN = REPO_ROOT / "docs" / "analysis" / "M13_evaluation_plan.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"
M13_PLAN = REPO_ROOT / "docs" / "milestones" / "M13" / "M13_plan.md"
REQUIREMENTS = REPO_ROOT / "requirements.txt"
REQUIREMENTS_DEV = REPO_ROOT / "requirements-dev.txt"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"


def test_m13_audio_baseline_strategy_exists() -> None:
    assert AUDIO_STRATEGY.is_file()


def test_m13_blackwell_training_plan_exists() -> None:
    assert BLACKWELL_PLAN.is_file()


def test_m13_artifact_boundary_plan_exists() -> None:
    assert ARTIFACT_BOUNDARY.is_file()


def test_m13_kaggle_inference_packaging_plan_exists() -> None:
    assert KAGGLE_PACKAGING.is_file()


def test_m13_evaluation_plan_exists() -> None:
    assert EVALUATION_PLAN.is_file()


def test_strategy_doc_references_zero_and_uniform_baselines_scoring_0500() -> None:
    text = AUDIO_STRATEGY.read_text(encoding="utf-8").lower()
    assert "0.500" in text
    assert "all-zero" in text
    assert "uniform" in text


def test_strategy_doc_states_improvement_requires_ranking_signal() -> None:
    text = AUDIO_STRATEGY.read_text(encoding="utf-8").lower()
    assert "ranking" in text
    assert "ranking signal" in text or "ranking separation" in text


def test_training_plan_mentions_5090_blackwell() -> None:
    text = BLACKWELL_PLAN.read_text(encoding="utf-8").lower()
    assert "5090" in text
    assert "blackwell" in text


def test_artifact_boundary_prohibits_sensitive_artifacts() -> None:
    text = ARTIFACT_BOUNDARY.read_text(encoding="utf-8").lower()
    assert "raw audio" in text
    assert "kaggle competition data" in text or "competition data" in text
    assert "weight" in text
    assert "unless" in text and "approv" in text
    assert "ornithos" in text


def test_packaging_plan_mentions_cpu_and_submission_path() -> None:
    text = KAGGLE_PACKAGING.read_text(encoding="utf-8").lower()
    assert "90" in text
    assert "minute" in text
    assert "/kaggle/working/submission.csv" in text


def test_evaluation_plan_no_improvement_unless_public_score_above_0500() -> None:
    text = EVALUATION_PLAN.read_text(encoding="utf-8").lower()
    assert "0.500" in text
    assert "no score improvement" in text or ("score improvement" in text and "> 0.500" in text)


def test_pantanal_marks_m13_closed() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1].split("## 8.", 1)[0]
    assert "| M13 |" in ledger
    m13_row = ledger.split("| M13 |", 1)[-1].split("\n", 1)[0]
    assert "closed" in m13_row.lower()


def test_pantanal_does_not_claim_model_training_or_quality() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    m13_claim = "audio-derived baseline planning package"
    assert m13_claim in text
    idx = text.index(m13_claim)
    m13_claim_block = text[max(0, idx - 200) : idx + len(m13_claim) + 200]
    assert "trained model" not in m13_claim_block
    assert "model quality" not in m13_claim_block
    assert "m13 does not train a model" in text
    assert "m13 does not claim model quality" in text


# --- Protective governance tests (beyond required 13) ---


def test_m13_planning_docs_cross_referenced_in_plan() -> None:
    text = M13_PLAN.read_text(encoding="utf-8")
    assert "M13_audio_baseline_strategy.md" in text
    assert "M13_blackwell_training_plan.md" in text
    assert "M13_artifact_boundary_plan.md" in text
    assert "M13_kaggle_inference_packaging_plan.md" in text
    assert "M13_evaluation_plan.md" in text


def test_audio_strategy_is_planning_gate_only() -> None:
    text = AUDIO_STRATEGY.read_text(encoding="utf-8").lower()
    assert "planning gate only" in text
    assert "no implementation" in text


def test_blackwell_plan_is_planning_only_not_training_commands() -> None:
    text = BLACKWELL_PLAN.read_text(encoding="utf-8").lower()
    assert "planning only" in text
    assert "training not started" in text
    assert "do not include runnable training commands" in text or (
        "do not include" in text and "training commands" in text
    )


def test_no_audio_ml_dependencies_introduced_in_requirements() -> None:
    banned = ("torch", "librosa", "torchaudio", "transformers", "timm", "sklearn", "pandas")
    for req_file in (REQUIREMENTS, REQUIREMENTS_DEV):
        if req_file.is_file():
            content = req_file.read_text(encoding="utf-8").lower()
            for name in banned:
                assert name not in content, f"{name} found in {req_file.name}"


def test_m13_does_not_modify_kaggle_notebooks() -> None:
    """M13 is docs-only; notebook content should not reference M13 wiring."""
    if not NOTEBOOKS_DIR.is_dir():
        return
    for nb in NOTEBOOKS_DIR.glob("*.ipynb"):
        text = nb.read_text(encoding="utf-8").lower()
        assert "m13_audio" not in text
        assert "m13 blackwell" not in text


def test_packaging_plan_acknowledges_submission_schema() -> None:
    text = KAGGLE_PACKAGING.read_text(encoding="utf-8").lower()
    assert "234" in text
    assert "5-second" in text or "5 second" in text


def test_packaging_plan_internet_disabled() -> None:
    text = KAGGLE_PACKAGING.read_text(encoding="utf-8").lower()
    assert "internet" in text
    assert "disabled" in text


def test_artifact_boundary_distinguishes_allowed_vs_prohibited() -> None:
    text = ARTIFACT_BOUNDARY.read_text(encoding="utf-8").lower()
    assert "prohibited" in text
    assert "potentially allowed" in text or "allowed" in text


def test_artifact_boundary_includes_handoff_and_hash_verification() -> None:
    text = ARTIFACT_BOUNDARY.read_text(encoding="utf-8").lower()
    assert "handoff" in text
    assert "sha-256" in text or "sha256" in text
    assert "manifest" in text


def test_evaluation_plan_no_score_improvement_claim_in_m13() -> None:
    text = EVALUATION_PLAN.read_text(encoding="utf-8").lower()
    assert "m13 does not run evaluation" in text or "planning gate only" in text
    assert "no score improvement" in text


def test_pantanal_includes_m13_explicit_non_claims() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "m13 does not train a model" in text
    assert "m13 does not implement audio inference" in text
    assert "m13 does not add audio or ml dependencies" in text
    assert "m13 does not improve leaderboard score" in text


def test_pantanal_m13_planning_package_claim() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "audio-derived baseline planning package" in text
    assert "5090" in text or "blackwell" in text
