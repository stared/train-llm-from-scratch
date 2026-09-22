# Supervised fine-tuning (SFT): answer in verse

**Model:** Qwen3.5-4B. **Data:** 500 Polish prompt → *Pan Tadeusz* passage pairs; 450 training / 50 validation. Each answer has 4–12 original verse lines.

One training pair (not a model generation):

> Nie możemy się dogadać w sprawie podwyżki. Jak zwykle kończą się takie negocjacje?

```text
Tu już krzyknęli: »Dosyć! Trzeba raz rzecz skończyć,
Bóg nas czy diabeł złączył, trzeba się rozłączyć;
Dwóch nas jak dwóch słońc pono zanadto na świecie!«
A więc do szerpentynek i stają na mecie.
```

```bash
modal run scripts/style_modal.py --stage train --data-run pan-tadeusz-qa-v1 --model qwen3.5-4b --epochs 2 --max-seconds 600 --batch-tokens 2048
```

Measured training: **370 seconds**. All 12 sampled held-out replies had 4–12 lines; grammar and meter remain uneven. Completed training/evaluation worker compute: **about $0.22** (extra startup/storage excluded).

[Actual model outputs before/after](../results/pan-tadeusz-qa-results.md) · [Training pairs](../datasets/pan-tadeusz-qa-v1/REVIEW.md)

## Watch and compare

The terminal prints loss every ten updates. At completion, run `pnpm dev` and select your run under **Reports** to compare the training-loss curve and original and fine-tuned answers. A lower loss does not guarantee good poetry.

To ask your own question, replace `RUN_NAME` with the training run name:

```bash
modal run scripts/style_modal.py --stage chat --data-run RUN_NAME --prompt "Co zrobić, gdy sąsiad hałasuje?"
```

The chat command prints **both original Qwen3.5-4B and your fine-tuned model** on the same question (a short paid GPU inference job). Records: `base.json`, `finetuned.json`, `loss.json`; adapter weights remain on Modal.
