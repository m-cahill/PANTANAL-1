"""Verify the repository does not contain prohibited data, secrets, or weights."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

PROHIBITED_PATHS = [
    ".kaggle/kaggle.json",
    "kaggle.json",
    ".env",
    "train_audio",
    "test_soundscapes",
    "train_soundscapes",
    "submission.csv",
    "runs",
    "wandb",
]

WEIGHT_SUFFIXES = (
    ".pt",
    ".pth",
    ".ckpt",
    ".onnx",
    ".safetensors",
)

SKIP_DIR_NAMES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "htmlcov",
}


def _iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.is_file():
            yield path


def find_violations(root: Path = REPO_ROOT) -> list[str]:
    violations: list[str] = []

    for rel in PROHIBITED_PATHS:
        target = root / rel
        if target.exists():
            violations.append(f"prohibited path present: {rel}")

    for file_path in _iter_files(root):
        if file_path.suffix in WEIGHT_SUFFIXES:
            rel = file_path.relative_to(root).as_posix()
            violations.append(f"prohibited weight file: {rel}")

    return sorted(violations)


def main() -> int:
    violations = find_violations()
    if violations:
        print("FAIL: repository state verifier found prohibited artifacts:")
        for item in violations:
            print(f"  - {item}")
        return 1

    print("PASS: repository state verifier found no prohibited artifacts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
