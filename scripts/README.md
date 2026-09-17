# Scripts

Run from the **repository root**, using `uv run scripts/NAME.py` or `uvx --from modal==1.5.0 modal run scripts/NAME.py`. Keep `.py.lock` files beside their scripts. The Modal wrappers run the same trainers and preserve the repository's `scripts/`, `config/`, `datasets/` and `assets/` layout in the remote image.

| Workshop task | Local script | Modal wrapper |
|---|---|---|
| Pretrain a tiny GPT | [train_scratch.py](train_scratch.py) | [scratch_modal.py](scratch_modal.py) |
| SFT / RLVR on Prawko | [prawko.py](prawko.py) | [prawko_modal.py](prawko_modal.py) |
| Poetry / dialogue SFT | [style_workshop.py](style_workshop.py) | [style_modal.py](style_modal.py) |
| Six-word stories / Countdown / maze RLVR | [rlvr_showcase.py](rlvr_showcase.py) | [rlvr_showcase_modal.py](rlvr_showcase_modal.py) |
| Starter routing / JSON / arithmetic SFT | [finetune.py](finetune.py) | [modal_app.py](modal_app.py) |

For arguments and budgets, follow the [workshop guides](../docs/README.md). The corpus-preparation steps are CPU work; complete them before renting a GPU.

| Preparation / inspection | Script |
|---|---|
| Download Polish Wikipedia | [download_scratch_corpus.py](download_scratch_corpus.py) |
| Extract markup and train/tokenize with BPE | [prepare_wiki_scratch.py](prepare_wiki_scratch.py) |
| Prepare Wolne Lektury | [prepare_wl_scratch.py](prepare_wl_scratch.py) |
| Rebuild the tokenizer explorer | [tokenizer_visualization.py](tokenizer_visualization.py) |
| Prepare official Prawko questions | [prepare_prawko.py](prepare_prawko.py) |
| Prepare *Pan Tadeusz* Q&A | [prepare_pan_tadeusz_qa.py](prepare_pan_tadeusz_qa.py) |
| Sample a scratch checkpoint | [sample_scratch.py](sample_scratch.py) |
| Verify saved Prawko results | [verify_prawko.py](verify_prawko.py) |
| Verify pretraining artifacts | [verify_pretraining.py](verify_pretraining.py) |
| Rebuild Prawko answers / charts | [prawko_report.py](prawko_report.py), [prawko_learning_report.py](prawko_learning_report.py) |
| Fetch existing remote experiments | [fetch_polish_experiments.py](fetch_polish_experiments.py), [sync_scratch_runs.py](sync_scratch_runs.py) |

Other `scratch_*_modal.py` scripts and `polish_remote_experiments.py` reproduce instructor experiments, including runs longer than the workshop. Use the main guides for participant defaults. Shared modules stay beside their callers so scripts also work without installing this repository as a package.

CPU checks live in [tests/](../tests/README.md). Recorded `executed_*.py` files under `runs/` are historical snapshots, not current entry points.
