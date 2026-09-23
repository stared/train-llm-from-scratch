# 2. Pretraining

Train a **30-million-parameter generative pretrained transformer (GPT)** from random weights on Wolne Lektury. It learns next-token prediction, not how to answer chat questions.

<details>
<summary style="color: #8b1e2d; font-size: 1.15em; cursor: pointer;"><strong>Click to expand: What actually changes during training?</strong></summary>

**Watch the explanation** — 3 min 57 s, English narration and on-screen captions.

https://github.com/user-attachments/assets/07683947-1b8d-4cf9-b16a-c78bdadb5eb5

[Download the video](assets/videos/wolne-lektury-training.mp4).

**The model's parameters change.** Parameters, often called weights, are numbers used in the model's calculations. Our ScratchGPT-30M has roughly 30 million of them. Its main weight matrices start with random numbers, so it has not yet learned Polish. Training adjusts these numbers to make better predictions.

**The books supply the correct answers.** We use the Wolne Lektury texts prepared in the previous step. The provided tokenizer has already converted them into token IDs. Its vocabulary of 8,192 tokens stays fixed during this exercise.

Here is a short illustration using the same tokenizer. This is an example sentence, not a quotation from the training books. `_` marks a space in this example:

```text
Text:    Ala ma kota.
Tokens:  A | la | _ma | _ko | ta | .
Input:   A | la | _ma | _ko | ta
Target:  la | _ma | _ko | ta | .
```

The target is the same sequence shifted by one token. After seeing `A`, the model should predict `la`. After seeing `A | la`, it should predict `_ma`. At each position, it can use only the tokens up to that position. It cannot peek at the next token.

**One training step in our default Wolne Lektury run:**

1. Pick **64 random text fragments** from the training data. This group is a *batch*. Each fragment supplies 512 input tokens and their next-token targets.
2. Feed the inputs through the model's **eight transformer layers**. These layers combine information from earlier tokens. At each position, the model assigns probabilities to all **8,192 possible next tokens**.
3. Compare those probabilities with the real next tokens. The average error score is called **loss**. Giving the correct token a very low probability produces a larger loss. This batch supplies **64 × 512 = 32,768 predictions** to learn from.
4. Calculate how each parameter affects that loss. This is *backpropagation*. The **AdamW optimizer** uses those calculations to make small adjustments to the parameters.
5. Repeat with another batch, until the **ten-minute training budget** runs out.

The model learns patterns that help it continue literary text: spelling, grammar and common phrases. This does not guarantee sensible or factual writing.

**What you see in the visualization:** the loss curve records prediction errors during training. At checkpoints—saved stages of training—the script also generates continuations of the same prompts. These show how the output changes. Generating these previews does not update the weights; learning happens in the training steps above.

</details>

<details>
<summary style="color: #8b1e2d; font-size: 1.15em; cursor: pointer;"><strong>Click to expand: What do these settings mean?</strong></summary>

For our default Wolne Lektury run:

- **Parameters (weights):** adjustable numbers inside the model. ScratchGPT-30M has roughly **30 million**. Training changes them; this number is not the number of books or tokens.
- **Random weights:** the starting point before learning. The main weight matrices begin with random values, rather than knowledge from a pretrained model.
- **Context — 512 tokens:** the length of each input fragment. To predict the next token at a position, the model can use only the tokens up to that position, not later ones. A token can be part of a word, so 512 tokens does not mean 512 words.
- **Batch size — 64:** how many fragments are used together for one training update. With 512 positions per fragment, that is **32,768 next-token predictions** before one weight update.
- **Checkpoint:** a saved model version from a particular stage of training. We keep the weights with the best development loss in `best.pt`. The viewer also records progress and sample text at checkpoints; those records are not themselves the model weights.
- **Loss:** a prediction-error score. It is lower when the model gives the real next tokens higher probabilities. Training loss measures practice performance; development loss measures performance on separate texts.
- **Nats:** the unit used for this loss, because its calculation uses the natural logarithm. You do not need the formula to read the graph: lower is better when comparing runs on the same data and tokenizer.

</details>

## What to expect

| Dataset / model | Training | End to end | GPU | Worker cost | Test loss before → after |
|---|---:|---:|---|---:|---:|
| Wolne Lektury / ScratchGPT-30M | 10 min | 11 min 32 s | H100 | $0.78 | 9.073 → 2.820 |

Measured with the image already built. [Run report](http://localhost:5173/reports#workshop-check.html).

## Run

Complete [data preparation](01-data-and-tokens.md#prepare-wolne-lektury) first, then run:

```bash
modal run scripts/scratch_recipe_modal.py --recipe wolne-lektury
```

The command uses H100, a 512-token context and an 8,192-token vocabulary. You can start [fine-tuning](03-fine-tuning.md) in another terminal while it runs.

## Watch training

In another terminal, run:

```bash
pnpm dev
```

Open **Pretraining** and select your run. The loss curve updates during training. Select a checkpoint to compare the same prompt before and after training. Token colors run from blue (likely) to red (unlikely) on a logarithmic scale. Hover over a token for its probability and alternatives.

Cross-entropy loss measures how much probability the model assigns to the actual next tokens; lower is better. A uniform prediction over 8,192 tokens has loss ln(8192) ≈ 9.01 nats, close to our random model's 9.07. Falling development loss means better predictions on text excluded from training.

## Actual result

**ScratchGPT-30M**, before and after ten minutes of pretraining on Wolne Lektury. Excerpts from an earlier run, `scratch-wl-30m-1788883120289174941`; ellipses mark truncation.

| Input | Random model | After pretraining |
|---|---|---|
| — Nie wiem, | 99okraty Juni Griiennikózózniemie… | ale mówiła o pani zaraz. … |
| Test loss (lower is better) | 9.073 | 2.782 |

The model learned recognizable prose but still makes grammatical and logical mistakes. A related text-generation demonstration is Karpathy's [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) (2015), using recurrent networks. Try training one in the [RecurrentJS demo](https://cs.stanford.edu/people/karpathy/recurrentjs/).

## Choosing a GPU

Choose another card with `--gpu L4`, `--gpu A10` or `--gpu L40S`.

Wolne Lektury, 30M parameters, batch 32, context 512, ten minutes of training. Worker time includes loading and evaluation.

| GPU | Worker time | Worker cost | Tokens processed | Test loss ↓ |
|---|---:|---:|---:|---:|
| H100 | 10 min 37 s | $0.74 | 394M | 2.784 |
| L4 | 10 min 34 s | $0.18 | 50M | 3.152 |
| A10 | 10 min 22 s | $0.23 | 72M | 3.064 |
| L40S | 10 min 24 s | $0.38 | 180M | 2.885 |

H100 processed more tokens per dollar; L4 cost less per run. These measurements use batch 32 and fewer diagnostics than the main command, which uses batch 64. Costs include CPU and memory.

To compare cards, use the same batch size on both runs:

```bash
modal run scripts/scratch_recipe_modal.py --gpu L4 --batch-size 32
modal run scripts/scratch_recipe_modal.py --gpu H100 --batch-size 32
```

Add `--compile-training` to compile the training loop. With H100 and batch 32, the workshop script processed 578M tokens in ten minutes, with test loss 2.760. Including evaluation: 11 min 4 s, $0.77.

[Measured comparisons](http://localhost:5173/reports#training-comparisons.html). [Modal GPU options](https://modal.com/docs/guide/gpu) and [pricing](https://modal.com/pricing).

## Predict the next token

At the top of **Pretraining**, choose a local model and edit the input. Click a candidate to append it, or **Next token** to sample one. Temperature changes the probabilities across the full vocabulary.

## Tokens and epochs

The measured ten-minute run processed **328M token presentations**, about **3.24 times** the 101M-token training corpus. We sample random windows, so this is approximate exposure, not three sequential passes. More training can lower training loss while making held-out loss worse; watch both curves. In the matched research runs, extending training from 10 to 30 minutes increased exposure from 3.89 to 12.44 corpus-equivalents and reduced test loss from 2.784 to 2.720; worker cost rose from $0.74 to $2.12.

For Wikipedia, the training pool is much larger: 3.14B tokens. A ten-minute 30M/H100 research run processed 404M tokens, only **0.13 corpus-equivalents**. At that measured rate, one equivalent would take roughly **78 minutes / $5.8** (an extrapolation, not a measured full pass). A useful learning demonstration does not require a complete epoch.

## Try

For a shorter run, add `--max-seconds 300`. Compare the generated text and test loss, not just the training loss. Each run saves a new folder under `runs/`; select your run in the visualization.

## Wikipedia alternative

[September 2026 dump](https://dumps.wikimedia.org/plwiki/20260901/): **2.73 GB compressed**, original markup retained. Preparation runs on Modal CPU and needs considerably more time and cloud storage than Wolne Lektury.

Measured on the prepared corpus, with the 98M-parameter model, batch 64, context 512 and compiled training:

| GPU | Training | Worker time | Worker cost | Test loss before → after |
|---|---:|---:|---:|---:|
| H100 | 10 min | 11 min 3 s | $0.77 | 9.174 → 1.627 |
| B200 | 10 min | 11 min | $1.19 | 9.174 → 1.509 |

Both learned markup while inventing facts; lower loss does not mean reliable knowledge. H100 processed 302M token presentations; B200 processed 565M. One run per GPU. [Experiment records](LAB_NOTEBOOK.md#participant-wikipedia-command-and-full-prose-data).

Prepare it:

```bash
modal run scripts/prepare_data_modal.py --corpus wikipedia
```

After **Ready**, start training:

```bash
modal run scripts/scratch_recipe_modal.py --recipe wiki-100m --compile-training
```

Watch it in the **Pretraining** section of the visualization. Add `--gpu B200` to compare cards, or use `--recipe wiki-cheap --max-seconds 300` for a smaller 10M model on L4 (earlier measured worker cost about $0.10).

Longer Wikipedia runs continue improving held-out loss. See the [training-time and cost curves](results/wikipedia-scaling.svg); those research runs take longer than this exercise.

**Next:** [3. Supervised fine-tuning](03-fine-tuning.md).

**Further reading:** [Language models](README.md#language-models).
