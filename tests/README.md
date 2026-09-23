# CPU checks

Run from the repository root:

```bash
PYTHONPATH=scripts uv run --no-project --with tiktoken==0.12.0 -m unittest discover -s tests -v
```

These checks cover data splits, question/answer formatting, corpus chunks, tokenizers and deterministic RLVR verifiers. They do not download a model or rent a GPU.

Check browser probability and token rendering logic:

```bash
pnpm exec node --test tests/test_prediction.mjs
```

Additional model checks have pinned dependencies and run on CPU:

```bash
uv run scripts/check_scratch_model.py
```

Verify saved Prawko run records without retraining:

```bash
uv run scripts/verify_prawko.py runs/prawko-*
```
