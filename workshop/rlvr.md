# Reinforcement learning with verifiable rewards (RLVR): six words

**Model:** Qwen3.5-4B. **Task:** write one line with exactly six words, including two requested words, with no repeated words.

No target stories: the model samples answers; a Python checker gives rewards.

```bash
modal run scripts/rlvr_showcase_modal.py --task six_words
```

About **10 minutes training**, **$0.19 worker compute**; loading/evaluation add time and startup/storage cost extra.

| Required words | Original Qwen3.5-4B | Same model + six-word RLVR |
|---|---|---|
| glacier, mermaid | The mermaid kissed the glacier. | Glacier melted to reveal a mermaid. |
| astronaut, birthday | Astronaut blew birthday candles. | Astronaut blew birthday candles in space. |

Held-out constraint compliance: **1/32 → 32/32**. This measures the rules, not story quality. There is no matched supervised fine-tuning comparison.

Open the checker in [rlvr_tasks.py](../scripts/rlvr_tasks.py). Can a bad story still pass? What would you change in the reward?

[All before/after answers](../results/rlvr-results.html)
