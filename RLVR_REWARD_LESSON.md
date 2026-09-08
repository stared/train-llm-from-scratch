# What does the reward actually teach?

These are **actual intermediate training samples from Qwen/Qwen3.5-0.8B**, after ten RLVR updates on synthetic six-word-story prompts. No Pan Tadeusz or film fine-tune, no supervised workshop warm start. Run: `rlvr-train-six_words-1788800080367606015`, rollout batch index 10, first prompt. They are not outputs from the final selected adapter.

Prompt: write exactly six English words, including **detective** and **rabbit**, without repeating a word. Return one line and no explanation.

| Sampled answer, unedited | Words | Task reward | Advantage after reference regularization |
|---|---:|---:|---:|
| detective talk to rabbit about cat | 6 | 1.000 | +0.351 |
| The detective arrives at the living rabbit | 7 | 0.367 | −0.477 |
| detective berry hunts rabbit nutty. | 5 | 0.467 | −0.269 |
| detective finds real rabbit from heartbreak | 6 | 1.000 | +0.395 |

The positive-advantage answers become more likely. **The checker rewards grammatical errors and odd meanings if they satisfy its lexical rules.** It also rejects the second answer for repeating “the”, as well as having seven words. There is no language-model judge hidden in the score.

With beta=.01, the trainer first subtracts `.01 × sampled_sequence_log_probability_ratio` from each task reward. A sample's advantage is then its adjusted reward minus the mean adjusted reward of its three siblings. The two reward-1 answers have different advantages because they incur different reference-policy penalties. Inspect `rollouts.json` for all values.

Try changing the checker, then ask what new shortcut becomes possible. Simply giving more reward for six words cannot establish that a sentence is funny, moving or even sensible. Human review remains part of this workshop.

The earlier unregularized Qwen/Qwen3-0.6B runs show three different failures:

- Six-word stories converged to five-word templates, such as **“Moon who is a sailor.”** Full-success examples appeared during training, then disappeared. Final held-out success: 0/32.
- Countdown puzzles converged to **`a + b - c`**, with `a`, `b`, `c` taken in input order. It used the right numbers but largely ignored the target. Final held-out success: 2/32.
- Maze navigation converged to **`UD` for every map**. Partial reward increased, but final held-out success remained 0/32.

Each of these was a fresh task-specific RLVR adapter, not a shared adapter trained on all three tasks. All generations are preserved in [the initial comparison](RLVR_INITIAL_RESULTS.html). This makes a concrete debugging lesson: a rising training reward is not sufficient evidence that the intended behavior improved.
