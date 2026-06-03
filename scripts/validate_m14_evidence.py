"""Validate M14 public-safe validation summary JSON (stdlib only)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = (
    "schema_version",
    "model_id",
    "status",
    "created_at",
    "prediction_summary",
    "class_coverage",
    "metrics",
    "claim_gate",
    "non_claims",
    "non_constant_predictions_verified",
)

ALLOWED_STATUS = frozenset({"planning_only", "private_trained_summary", "owner_approved_binary"})

# Phrases that must not appear in planning_only evidence (overclaiming).
PLANNING_ONLY_FORBIDDEN_PHRASES = (
    "score improvement",
    "improved leaderboard",
    "beats 0.500",
    "training complete",
    "training completed",
    "model quality proven",
    "proves model quality",
    "working-note ready",
    "rediai certified",
)

METRIC_FORBIDDEN_WHEN_PLANNING = (
    "macro_roc_auc",
    "public_score",
    "leaderboard_score",
)


def _load_json(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("root must be a JSON object")
    return data


def _check_required_fields(data: dict[str, Any], errors: list[str]) -> None:
    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            errors.append(f"missing required field: {key}")


def _check_types(data: dict[str, Any], errors: list[str]) -> None:
    if "schema_version" in data and not isinstance(data["schema_version"], str):
        errors.append("schema_version must be a string")
    if "model_id" in data and not isinstance(data["model_id"], str):
        errors.append("model_id must be a string")
    if "status" in data:
        status = data["status"]
        if not isinstance(status, str):
            errors.append("status must be a string")
        elif status not in ALLOWED_STATUS:
            errors.append(f"invalid status: {status}")
    if "created_at" in data and not isinstance(data["created_at"], str):
        errors.append("created_at must be a string")
    if "prediction_summary" in data and not isinstance(data["prediction_summary"], str):
        errors.append("prediction_summary must be a string")
    if "class_coverage" in data and not isinstance(data["class_coverage"], dict):
        errors.append("class_coverage must be an object")
    if "metrics" in data:
        metrics = data["metrics"]
        if not isinstance(metrics, dict):
            errors.append("metrics must be an object")
        else:
            for name, value in metrics.items():
                if value is not None and not isinstance(value, (int, float)):
                    errors.append(f"metrics.{name} must be number or null")
    if "claim_gate" in data and not isinstance(data["claim_gate"], str):
        errors.append("claim_gate must be a string")
    if "non_claims" in data:
        nc = data["non_claims"]
        if not isinstance(nc, list) or not nc:
            errors.append("non_claims must be a non-empty array")
        elif not all(isinstance(x, str) for x in nc):
            errors.append("non_claims items must be strings")
    ncpv = data.get("non_constant_predictions_verified")
    if ncpv is not None and not isinstance(ncpv, bool):
        errors.append("non_constant_predictions_verified must be a boolean")


def _collect_overclaim_text(data: dict[str, Any]) -> str:
    """Text fields where planning_only must not assert positive claims.

    non_claims is excluded: it may mention forbidden topics only to deny them.
    """
    parts: list[str] = []
    if isinstance(data.get("prediction_summary"), str):
        parts.append(data["prediction_summary"])
    metrics = data.get("metrics")
    if isinstance(metrics, dict):
        for _k, v in metrics.items():
            if v is not None:
                parts.append(str(v))
    return " ".join(parts).lower()


def _check_planning_only_rules(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("status") != "planning_only":
        return
    if data.get("non_constant_predictions_verified") is True:
        errors.append("planning_only must have non_constant_predictions_verified=false")
    text = _collect_overclaim_text(data)
    for phrase in PLANNING_ONLY_FORBIDDEN_PHRASES:
        if phrase in text:
            errors.append(f"planning_only must not contain forbidden phrase: {phrase}")
    metrics = data.get("metrics")
    if isinstance(metrics, dict):
        for key in METRIC_FORBIDDEN_WHEN_PLANNING:
            val = metrics.get(key)
            if val is not None and isinstance(val, (int, float)) and val > 0:
                errors.append(
                    f"planning_only must not have positive numeric {key} (implies quality claim)"
                )


def validate_evidence(data: dict[str, Any]) -> list[str]:
    """Return list of validation errors (empty if valid)."""
    errors: list[str] = []
    _check_required_fields(data, errors)
    if errors:
        return errors
    _check_types(data, errors)
    _check_planning_only_rules(data, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate M14 validation summary JSON (public-safe evidence contract)."
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to validation summary JSON file",
    )
    args = parser.parse_args(argv)
    path = args.path.resolve()
    if not path.is_file():
        print(f"FAIL: file not found: {path}", file=sys.stderr)
        return 1
    try:
        data = _load_json(path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    errors = validate_evidence(data)
    if errors:
        print(f"FAIL: {path.name}", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(f"OK: {path.name} (status={data.get('status')})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
