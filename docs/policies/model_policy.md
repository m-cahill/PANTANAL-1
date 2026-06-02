# Model Policy

**Authority:** Subordinate to `docs/pantanal-1.md`.

---

## Principles

1. **Do not commit** trained weights or large checkpoints to git.
2. Reference **public** pre-trained models in Kaggle notebooks when rules allow.
3. Document model provenance in milestone evidence, not as unverifiable claims in Ultimate Truth.

---

## Prohibited in git

- `*.pt`, `*.pth`, `*.ckpt`, `*.onnx`, `*.safetensors`, `*.bin`, `*.pkl`, `*.joblib`
- WandB / MLflow run directories (`wandb/`, `mlruns/`)

---

## Kaggle submission

- Models must be loadable within CPU notebook budget (≤ 90 minutes total)
- Internet disabled at scoring: bundle or cache weights inside notebook-compatible paths per Kaggle rules

---

## Enforcement

- `.gitignore`
- `scripts/verify_repo_state.py`
