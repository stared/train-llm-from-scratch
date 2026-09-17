# CPU checks

Run from the repository root:

```bash
PYTHONPATH=scripts uv run --no-project -m unittest discover -s tests -v
```

These standard-library tests cover data splits, question/answer formatting, corpus chunks and deterministic RLVR verifiers. They do not download a model or rent a GPU.

Additional model checks have pinned dependencies and run on CPU:

```bash
uv run scripts/check_scratch_model.py
```

Verify saved Prawko run records without retraining:

```bash
uv run scripts/verify_prawko.py runs/prawko-*
```
