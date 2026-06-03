"""Tests for M08 working-note outline, evidence map, and honest claim boundaries."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTLINE_PATH = REPO_ROOT / "docs" / "working_note" / "working_note_outline.md"
EVIDENCE_MAP_PATH = REPO_ROOT / "docs" / "working_note" / "evidence_map.md"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"

OUTLINE_SECTION_MARKERS = (
    "## 1. Introduction",
    "## 2. Repository Governance and Boundary Model",
    "## 3. Submission Contract Development",
    "## 4. Kaggle Notebook Path",
    "## 5. Audit Hardening",
    "## 6. Results",
    "## 7. Limitations",
    "## 8. Future Work",
)


def test_working_note_outline_exists() -> None:
    assert OUTLINE_PATH.is_file()


def test_evidence_map_exists() -> None:
    assert EVIDENCE_MAP_PATH.is_file()


def test_outline_states_outline_only_not_full_note() -> None:
    text = OUTLINE_PATH.read_text(encoding="utf-8").lower()
    assert "outline only" in text
    assert "not a full working note" in text or "not submission-ready" in text


def test_outline_includes_required_sections() -> None:
    text = OUTLINE_PATH.read_text(encoding="utf-8")
    for marker in OUTLINE_SECTION_MARKERS:
        assert marker in text, f"missing section: {marker}"


def test_outline_mentions_public_score_0_500() -> None:
    assert "0.500" in OUTLINE_PATH.read_text(encoding="utf-8")


def test_outline_0_500_is_pipeline_acceptance_not_model_quality() -> None:
    text = OUTLINE_PATH.read_text(encoding="utf-8").lower()
    assert "0.500" in text
    assert "pipeline" in text
    assert "model quality" in text or "predictive" in text
    assert "not" in text


def test_evidence_map_references_pantanal_ultimate_truth() -> None:
    assert "docs/pantanal-1.md" in EVIDENCE_MAP_PATH.read_text(encoding="utf-8")


def test_evidence_map_references_m04_commit_mode_evidence() -> None:
    assert "docs/kaggle/m04_commit_mode_evidence.md" in EVIDENCE_MAP_PATH.read_text(
        encoding="utf-8"
    )


def test_evidence_map_references_audit_hardening() -> None:
    assert "docs/quality/audit_hardening.md" in EVIDENCE_MAP_PATH.read_text(encoding="utf-8")


def test_evidence_map_references_security_supply_chain() -> None:
    assert "docs/quality/security_supply_chain.md" in EVIDENCE_MAP_PATH.read_text(encoding="utf-8")


def test_evidence_map_score_non_claim() -> None:
    text = EVIDENCE_MAP_PATH.read_text(encoding="utf-8")
    assert "0.500" in text
    lower = text.lower()
    assert "pipeline acceptance" in lower or "scored pipeline acceptance" in lower
    assert "predictive model quality" in lower or "does not support predictive" in lower


def test_pantanal_marks_m08_in_progress() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    ledger = text.split("## 7. Milestone ledger", 1)[-1]
    assert "| M08 |" in ledger
    assert "in progress" in ledger.lower()


def test_pantanal_does_not_claim_working_note_readiness() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "working-note readiness" in text or "working note readiness" in text
    claims = text.split("## 8. current claims", 1)[-1]
    m08_block = claims
    if "**m08 explicit non-claims:**" in claims:
        m08_block = claims.split("**m08 explicit non-claims:**", 1)[0]
    assert "clef submission-ready" not in m08_block or "does not make" in text
    assert "not yet proven" in text or "does not create a full working-note" in text


def test_pantanal_preserves_inference_and_quality_non_claims() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "model inference" in text
    assert "meaningful model quality" in text or "model quality" in text
    assert "competitive" in text or "does not prove model quality" in text
