# 4. Reinforcement learning with verifiable rewards: six words

In fine-tuning, we supplied correct answers. Here, the model generates answers and a **Python checker scores them**. Training uses those scores to change the model's behavior. This is **reinforcement learning with verifiable rewards (RLVR)**.

We start from **Qwen3.5-4B**, a pretrained model with roughly four billion parameters. **We do not continue training the driving-exam adapter from chapter 3.** This is a new task and a separate run, again using LoRA to keep the original model weights fixed.

## 1. Understand the task and check you are ready

The task is to write one line with **exactly six English words**, including two requested words, with **no repeated words**. Return only the story, without a title or explanation.

For the requested words **astronaut** and **birthday**:

| Answer | Check |
|---|---|
| Astronaut blew birthday candles. | Four words: fails. |
| Astronaut blew birthday candles in space. | Six words, both requested words, no repeats: passes. |

The checker counts sequences of letters as words and ignores capitalization when matching them. Punctuation does not count as a word.

Use the same repository and Modal setup as before. There is no dataset to download manually: the script generates **256 training prompts**, **24 development prompts** and **32 test prompts**. It loads the pretrained model automatically. There are no supplied target stories.

<details>
<summary style="color: #8b1e2d; font-size: 1.15em; cursor: pointer;"><strong>Click to expand: How can a score teach the model?</strong></summary>

For each training prompt, the model samples four possible answers. The checker scores each one. The training update encourages answers that scored better than their alternatives and discourages those that scored worse. Only the LoRA adapter changes.

**Reward** is a number from 0 to 1. The six-word checker gives partial credit for getting close to six words, including the requested words, and avoiding repetitions while using the required format. Meeting every rule adds a bonus and gives the maximum reward of 1.

**Success** is a separate yes/no check: did the answer meet every rule? Average reward can improve even while some answers still fail.

The checker does not judge whether a story is interesting or makes sense. A dull or nonsensical answer can pass. Training follows what we score.

</details>

## 2. Start reinforcement learning

Run from the repository directory:

```bash
modal run scripts/rlvr_showcase_modal.py --task six_words
```

The command will:

1. Start a Modal worker, load Qwen and generate the prompt sets.
2. Evaluate the original model to record its starting performance.
3. Generate training answers, score them and update a LoRA adapter.
4. Select a checkpoint using development results, evaluate it, and download reports.

Keep the terminal connected until it prints **`Saved:`** followed by your local run folder. Model loading and the initial evaluation can take time before the first training measurements appear. Keep the terminal open while you wait.

The defaults use **one L4 GPU**, at most **160 training steps**, and a training-loop budget of roughly **ten minutes**. Training stops when either limit is reached. Loading and evaluation add time, so the full command takes longer. You do not need a GPU on your laptop.

<details>
<summary style="color: #8b1e2d; font-size: 1.15em; cursor: pointer;"><strong>Click to expand: How does the training script work? A programmer's overview</strong></summary>

[rlvr_showcase_modal.py](scripts/rlvr_showcase_modal.py) launches the cloud job and downloads reports. [rlvr_showcase.py](scripts/rlvr_showcase.py) trains the adapter. [rlvr_tasks.py](scripts/rlvr_tasks.py) generates prompts and checks answers.

```mermaid
flowchart TD
    A["Take two training prompts"] --> B["Sample four answers per prompt"]
    B --> C["Score each answer with the Python checker"]
    C --> D["Compare scores within each prompt's group"]
    D --> E["Use that feedback to update the LoRA adapter"]
    E --> F{"Steps and time remaining?"}
    F -->|Yes| A
    F -->|No| G["Finish evaluation and save results"]
```

The update uses each answer's score relative to its alternatives, with a small penalty for moving too far from the original model's behavior. If there is no learning signal, an update can be skipped. We do not simply save the best generated story as a target answer.

Every 20 steps, the script checks development prompts without learning from them. It keeps the adapter with the most development successes, breaking ties with average reward. The original version can remain selected if training does not improve that score.

**Transformers** loads the model and tokenizer. **PEFT** manages LoRA. **PyTorch** generates answers and calculates gradients and AdamW updates. **Modal** provides the GPU and persistent storage. The reward checker is ordinary Python code.

</details>

## 3. Watch your run

In another terminal in the repository, run:

```bash
pnpm dev
```

Open the address printed in the terminal, usually [http://localhost:5173](http://localhost:5173). If the viewer is already running, keep using it. Open **RLVR** and select **your run**, rather than an included **Example run**.

Look at a training prompt, its sampled answers and their rewards. Count the words in one answer and check whether both requested words appear. Use the rules above to understand its score.

Then select checkpoints to compare answers to the same development prompts. These checks help select the adapter to keep; they do not update it. Training rewards may fluctuate because the model samples different answers.

## 4. Check the finished result

Wait for **`Saved:`**. At the top of the viewer, find **Test constraints**. It shows the original model’s score followed by the development-selected checkpoint’s score on the **32 separate test prompts**. Test success counts answers that pass every rule, not just answers with some partial reward.

An earlier run improved from **1/32 to 24/32**. This is an example, not a required score. Your results may differ. [Earlier run report](http://localhost:5173/reports#workshop-check.html) and [recorded before/after answers](http://localhost:5173/reports#rlvr-results.html) show past runs, not your current job.

The before/after examples below the graph are **development prompts**, not test prompts. Select **Selected checkpoint** and inspect one before/after answer for the same prompt. Identify which rule it learned to satisfy, or which rule it still fails. Then read a passing answer: is it actually an interesting story?

**Passing the checker does not guarantee good writing.** This is the main lesson: the reward defines what training encourages.

## 5. Find your saved adapter

The terminal identifies a local folder such as **`runs/rlvr-train-six_words-<number>/`**. It contains reports, recorded answers and training measurements for the viewer.

The selected adapter stays in the **`model-training-workshop` Modal volume**, under `runs/<run-name>/adapter/`. The worker sees this as `/persist/runs/<run-name>/adapter/`. The tokenizer is saved alongside it in `tokenizer/`.

To use the trained model later, you need **the original Qwen3.5-4B model plus this adapter**. Local reports alone cannot generate new stories.

## You have finished reinforcement learning

You have finished when the command has completed, you have compared before/after answers, and you can explain the difference between receiving partial reward and passing every rule.

**Optional reading:** [Countdown and what a reward can accidentally teach](additional/reinforcement-learning-experiments.md).

**Further reading:** [Fine-tuning and reinforcement learning](README.md#fine-tuning-and-reinforcement-learning).
