# Reusable persona data

Each version contains 64 original question–answer pairs: 32 Polish and 32 English. The two personas answer the same training questions. All eight evaluation questions in `style_data.py` are separate.

These answers were authored by the coding assistant during workshop preparation. They are not film quotations, not a *Pan Tadeusz* corpus, and not outputs from the rejected Gemma synthetic-data run. The poetry dataset teaches short verse; it does not enforce thirteen-syllable lines or guarantee literary quality. The comic dataset uses original metaphors and practical advice.

Edit `curated_data.py`, then rebuild with:

```bash
uv run curated_data.py
```

This regenerates the JSONL files and matching SHA-256 manifests. Keep a copy/version before changing a dataset used by an experiment. Every training run copies the exact data and manifest into its output directory.

For manual edits directly to JSONL, update the manifest hash deliberately after review; the trainer refuses a mismatch. Do not add evaluation questions to the training set. The same checks should apply to any newly generated candidate dataset.
