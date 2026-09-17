# AI from scratch

[Model training workshop](https://luma.com/Warsaw-Model-Trainers-w3) with **[Piotr Migdał](https://p.migdal.pl/) and Anna Olchowik**, organized by [Kolektyw3](https://luma.com/kolektyw3) as preparation for the [Warsaw Model Trainers hackathon](https://luma.com/Warsaw-Model-Trainers-hackathon?tk=tXTOg3).

Train a small language model from scratch, then adapt existing models. Polish materials, English explanations, ordinary runnable scripts.

[![How to Train Your Own Model — Anna Olchowik and Piotr Migdał, 23 September 2026, Kolektyw3, Warsaw](workshop.jpeg)](https://luma.com/Warsaw-Model-Trainers-w3)

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/). Run commands from this repository's folder. Scripts use **Python 3.14**; uv downloads it if needed.

Install [Modal](https://modal.com/) to run GPU jobs:

```bash
uv tool install modal==1.5.5
```

Connect your account and follow the browser login:

```bash
modal setup
```

## 1. Data and tokenization

[Start here: data and tokens](01-data-and-tokens.md). Prepare Wolne Lektury with one command:

```bash
uv run scripts/prepare_pretraining.py literature
```

This downloads **123 MB**, prepares **101 million training tokens**, and uploads them. While it runs, follow the guide's tokenizer example and [byte-pair encoding (BPE)](https://en.wikipedia.org/wiki/Byte_pair_encoding) visualization. No GPU cost yet.

## 2. Pretraining

After preparation says **Ready**, [train a small model from random weights](02-pretraining.md):

```bash
modal run scripts/scratch_recipe_modal.py --recipe literature
```

**30M parameters · up to 10 minutes · about $0.76 measured worker compute.** Watch loss, then compare random and trained text:

```bash
uv run scripts/view_results.py pretrain
```

## 3. Supervised fine-tuning (SFT)

[Train Qwen3.5-0.8B for the Polish Driving Licence Exam](03-fine-tuning.md), using question → correct-answer examples:

```bash
modal run scripts/prawko_modal.py --method sft --epochs 10 --max-seconds 180
```

**Up to 3 minutes · about $0.06 measured worker compute.** The included dataset needs no preparation; you can start this while pretraining runs. Inspect accuracy and before/after answers:

```bash
uv run scripts/view_results.py sft
```

## 4. Reinforcement learning with verifiable rewards (RLVR)

[Teach Qwen3.5-4B to write exactly six words](04-reinforcement-learning.md). The model tries answers; code checks them and supplies rewards:

```bash
modal run scripts/rlvr_showcase_modal.py --task six_words
```

**Up to 10 minutes · about $0.19 measured worker compute.** This starts from the original Qwen model, independently of SFT:

```bash
uv run scripts/view_results.py rlvr
```

## If you are waiting or catching up

Every exercise has real saved results. Add `--example` to any view command to open those immediately, without training or a Modal account. The tokenizer also works without downloading the corpus:

```bash
uv run scripts/view_results.py tokens
```

Exercises 3 and 4 are independent of pretraining. You can run jobs in separate terminals; each job is billed separately. Training prints progress and saves a new folder in `runs/`. View commands open the latest completed run.

The main path used about **$1.01 in worker compute** in our experiments. These are historical measurements, not caps; loading/evaluation add time and builds/storage cost extra.

## Explore further

Each exercise ends with a small experiment. Options include Wikipedia pretraining, longer exam training, comparing SFT with RLVR on the exam, and [answering in verse](additional/poetry.md). [Compare saved results](results/README.md).

## Files

The four numbered guides are the main path. `scripts/` contains runnable code and its model settings (`models.json`). `datasets/` contains inputs; large downloads in `datasets/local/` are gitignored. `results/` contains shared examples and visualizations; `runs/` contains your generated outputs and is gitignored. `additional/` holds optional exercises and research; `LAB_NOTEBOOK.md` records findings.

Codex or Claude are optional helpers. Other GPU platforms include [Google Colab](https://colab.research.google.com/) and [Lightning AI](https://lightning.ai/); these commands use Modal.

## Learn more

- [MicroGPT — Andrej Karpathy](https://karpathy.github.io/2026/02/12/microgpt/): a complete GPT in 200 lines of Python.
- [Let's build GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY): Karpathy's step-by-step coding walkthrough.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/4): transformers, pretraining and fine-tuning.
- [Nanochat](https://github.com/karpathy/nanochat): explore a complete language-model training pipeline.
- [Thinking in tensors, writing in PyTorch](https://github.com/stared/thinking-in-tensors-writing-in-pytorch): Piotr's hands-on introduction to neural networks.
