# AI from scratch

[Model training workshop](https://luma.com/Warsaw-Model-Trainers-w3) with **[Piotr Migdał](https://p.migdal.pl/) and Anna Olchowik**, organized by [Kolektyw3](https://luma.com/kolektyw3) as preparation for the [Warsaw Model Trainers hackathon](https://luma.com/Warsaw-Model-Trainers-hackathon?tk=tXTOg3).

Train a small language model from scratch, then adapt existing models. Polish training data, English explanations.

[![How to Train Your Own Model — Anna Olchowik and Piotr Migdał, 23 September 2026, Kolektyw3, Warsaw](workshop.jpeg)](https://luma.com/Warsaw-Model-Trainers-w3)

## Setup

### Create your Modal account

[Modal](https://modal.com/) runs the workshop code on cloud computers. **You do not need a GPU on your laptop.** Data preparation uses cloud CPU time; training uses cloud GPU time. Both can incur charges, as can stored files.

**[Follow the Modal setup guide →](modal-setup.md)** Complete it before continuing below.

## Visualization

```bash
pnpm dev
```

Opens http://localhost:5173 in your browser. The app combines an interactive explanation with a viewer for real training results:

- **Tokenization:** explore how text becomes tokens. You can use this before training any model.
- **Pretraining, SFT and RLVR:** watch your actual training progress, including learning curves and generated text or answers. Select your job in the **Run** menu. Move between checkpoints to compare outputs at different stages of training.
- **Before you run anything:** the training sections show included example results from earlier experiments. These are not results from your own model.
- **Reports:** browse saved experiment reports and comparisons.

**`pnpm dev` only opens the viewer. It does not start training.** Start training separately using the Modal commands below. Keep the viewer open and the training terminal connected for live updates; your runs appear automatically.

## 1. Data and tokenization

[Start here: data and tokens](01-data-and-tokens.md). To prepare [Wolne Lektury](https://wolnelektury.pl/), run:

```bash
modal run scripts/prepare_data_modal.py
```

Modal downloads **123 MB** and prepares **101 million training tokens** in your cloud volume. Explore the tokenizer and [byte-pair encoding (BPE)](https://en.wikipedia.org/wiki/Byte_pair_encoding) visualization.

## 2. Pretraining

After preparation says **Ready**, [train a small model from random weights](02-pretraining.md):

```bash
modal run scripts/scratch_recipe_modal.py --recipe wolne-lektury
```

30M parameters on H100. Training takes 10 minutes; the measured run took 11 min 32 s including evaluation and cost $0.78. [Compare GPUs](02-pretraining.md#choosing-a-gpu).

Open **Pretraining** in the visualization to watch loss and generated text at each checkpoint.

## 3. Supervised fine-tuning (SFT)

[Train Qwen3.5-0.8B for the Polish Driving Licence Exam](03-fine-tuning.md), using question → correct-answer examples:

```bash
modal run scripts/prawko_modal.py --method sft --epochs 10 --max-seconds 180
```

**Up to 3 minutes, about $0.065 measured worker compute.** The included dataset needs no preparation; you can start this while pretraining runs. Open **SFT** to see the training input, target answer and changing A/B/C probabilities.

## 4. Reinforcement learning with verifiable rewards (RLVR)

[Teach Qwen3.5-4B to write exactly six words](04-reinforcement-learning.md). The model tries answers; code checks them and supplies rewards:

```bash
modal run scripts/rlvr_showcase_modal.py --task six_words
```

**Up to 10 minutes, about $0.19 measured worker compute.** This starts from the original Qwen model, independently of SFT. Open **RLVR** to see sampled answers, their rewards and development success.

## Running the exercises

Keep the training terminal connected for live updates. Results are saved in `runs/`.

Measured compute for the four exercises: about **$1.04**. See the [run measurements](http://localhost:5173/reports#workshop-check.html).

## Explore further

Each exercise ends with a small experiment. Options include Wikipedia pretraining, longer exam training, comparing SFT with RLVR on the exam, and [answering in verse](additional/poetry.md). [Compare saved results](results/README.md).

## Files

The four numbered guides are the main path. `scripts/` contains runnable code and its model settings (`models.json`). `datasets/` contains inputs; large downloads in `datasets/local/` are gitignored. `visualization/` contains the app and its local server; `results/` contains experiment reports available through the app; `runs/` contains your generated outputs and is gitignored. `additional/` holds optional exercises and research; `LAB_NOTEBOOK.md` records findings.

## Learn more

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): explore how GPT-2 predicts the next token.
- [RecurrentJS — Andrej Karpathy](https://cs.stanford.edu/people/karpathy/recurrentjs/): train an RNN/LSTM in your browser and watch it learn to generate text.
- [MiMo-V2.6 RL dashboard](https://mimo.xiaomi.com/rl/): public post-training dashboard from Xiaomi's MiMo team, led by Luo Fuli. See also [HN discussion](https://news.ycombinator.com/item?id=49732270).
- [Let's build GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY): Karpathy's coding walkthrough.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/4): transformers, pretraining and fine-tuning.

[Further reading and model benchmarks](additional/reading.md).
