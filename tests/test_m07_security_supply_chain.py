"""Tests for M07 security/supply-chain docs, CI config, and honest claim boundaries."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SECURITY_DOC = REPO_ROOT / "docs" / "quality" / "security_supply_chain.md"
CI_WORKFLOW = REPO_ROOT / ".github" / "workflows" / "ci.yml"
REQUIREMENTS_DEV = REPO_ROOT / "requirements-dev.txt"
ULTIMATE_TRUTH = REPO_ROOT / "docs" / "pantanal-1.md"


def test_security_supply_chain_doc_exists() -> None:
    assert SECURITY_DOC.is_file()


def test_security_doc_states_bandit_and_pip_audit() -> None:
    text = SECURITY_DOC.read_text(encoding="utf-8").lower()
    assert "bandit" in text
    assert "pip-audit" in text


def test_security_doc_preserves_non_claims() -> None:
    text = SECURITY_DOC.read_text(encoding="utf-8").lower()
    assert "model inference" in text
    assert "vulnerability-free" in text or "does not prove" in text


def test_requirements_dev_includes_bandit() -> None:
    text = REQUIREMENTS_DEV.read_text(encoding="utf-8").lower()
    assert "bandit" in text


def test_requirements_dev_includes_pip_audit() -> None:
    text = REQUIREMENTS_DEV.read_text(encoding="utf-8").lower()
    assert "pip-audit" in text


def test_ci_workflow_mentions_bandit_on_src() -> None:
    text = CI_WORKFLOW.read_text(encoding="utf-8")
    assert "bandit -r src/pantanal_1" in text


def test_ci_workflow_mentions_pip_audit_on_requirements_dev() -> None:
    text = CI_WORKFLOW.read_text(encoding="utf-8")
    assert "pip-audit -r requirements-dev.txt" in text


def test_ci_workflow_still_mentions_mypy_on_src() -> None:
    text = CI_WORKFLOW.read_text(encoding="utf-8")
    assert "mypy src/pantanal_1" in text


def test_ci_workflow_still_mentions_coverage_fail_under() -> None:
    text = CI_WORKFLOW.read_text(encoding="utf-8").lower()
    assert "coverage report" in text
    assert "fail-under=80" in text


def test_pantanal_marks_m07_closed() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    assert "M07" in text
    ledger = text.split("## 7. Milestone ledger", 1)[-1]
    assert "security" in ledger.lower() or "supply-chain" in ledger.lower()
    assert "| M07 |" in ledger or "m07 |" in ledger.lower()
    assert "closed" in ledger.lower()


def test_pantanal_does_not_claim_inference_or_score_improvement() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8")
    m07_section = text
    if "**M07 explicit non-claims:**" in text:
        m07_section = text.split("**M07 explicit non-claims:**", 1)[1]
    lower = m07_section.lower()
    assert "does not implement model inference" in lower or "not yet proven" in lower
    assert "improve leaderboard score" not in lower or "does not improve" in lower


def test_pantanal_does_not_claim_vulnerability_free_security() -> None:
    text = ULTIMATE_TRUTH.read_text(encoding="utf-8").lower()
    assert "vulnerability-free" not in text or "does not prove" in text
