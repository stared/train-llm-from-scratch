# AI from scratch

[Model training workshop](https://luma.com/Warsaw-Model-Trainers-w3) by **Piotr Migdał and Anna Olchowik**, part of Warsaw Model Trainers.

Train a small language model from scratch, then adapt existing models. Polish materials, English explanations, ordinary runnable scripts.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then install [Modal](https://modal.com/) to run training on a cloud GPU:

```bash
uv tool install modal==1.5.5
modal setup
```

Run commands from this folder. Codex or Claude can help, but are optional.

## 1. Data

Polish Wikipedia articles with their original markup, or books from Wolne Lektury. [See the data and a short excerpt](workshop/pretraining.md#data).

## 2. Tokenization

Turn text into numbered pieces called tokens. Explore [byte-pair encoding (BPE)](https://en.wikipedia.org/wiki/Byte_pair_encoding) in the [interactive tokenizer](visualizations/tokenizer.html). Our vocabulary contains 8,192 tokens.

## 3. Pretraining

Start from random weights and learn to predict the next token. [Train a model with 10 or 30 million parameters](workshop/pretraining.md#train); compare its text and learning curves.

## 4. Supervised fine-tuning (SFT)

[Fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) adapts an existing model; here, we teach it using example inputs and correct outputs. [LLM robi prawko](workshop/prawko.md) trains Qwen3.5-0.8B on driving-theory questions. Alternatively, [teach Qwen3.5-4B to answer in verse](workshop/poetry.md).

## 5. Reinforcement learning with verifiable rewards (RLVR)

Let the model try answers and reward those that pass a checker. [Use the same driving questions](workshop/prawko.md), or [train six-word stories](workshop/rlvr.md). The driving exercise compares separate SFT and RLVR runs from the same starting model.

## 6. Testing

Did it improve on questions it never trained on? [Compare answers, learning curves and cost](results/README.md), including mistakes introduced by training.

## Where to look

`workshop/` contains the exercises; `scripts/` contains their code. Small datasets are in `datasets/`; large downloads stay in gitignored `data/`. Saved examples and charts are in `results/`.
