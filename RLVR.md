# A tiny, runnable RLVR experiment

For the newer minute-scale task comparison, see [RLVR workshop examples](RLVR_SHOWCASE.md), [all before/after outputs](RLVR_RESULTS.html), and [what the failed runs teach about rewards](RLVR_REWARD_LESSON.md). The old pipeline below changed adapter weights but remained at 4/8 accuracy.

Run the Polish SFT exercise first, then reuse its saved adapter. SFT learns from supplied answer tokens; RLVR samples its own answers, gets a numerical reward from a checker, and updates the policy from that reward.

```bash
uvx --from modal==1.5.0 modal run modal_app.py --model lfm2.5-350m --task polish --steps 40 --eval-size 8 --max-seconds 90

# Substitute the SFT run directory name printed by that command.
uvx --from modal==1.5.0 modal run rlvr_modal.py --sft-run YOUR_SFT_RUN --groups 12 --rollouts 4
```

For a local GPU, with the full SFT output directory including adapter and tokenizer:

```bash
uv run rlvr.py --sft-dir runs/YOUR_SFT_RUN --output runs/my-rlvr --device cuda --groups 12 --rollouts 4
```

Both trainers are uv scripts with pinned inline dependencies and lockfiles. To retrieve the entire SFT run from Modal:

```bash
uvx --from modal==1.5.0 modal volume get model-training-workshop /runs/YOUR_SFT_RUN ./runs/YOUR_SFT_RUN
```

**The algorithm.** For each arithmetic prompt, generate four independent answers. Reward is 1 if the whole stripped answer is the exact integer sum, and 0 otherwise. The checker neither evaluates generated code nor searches a long answer for a lucky matching number.

For sample i, its advantage is its reward minus the average reward of the other three samples. The loss is the negative mean of advantage times the sum of generated-token log probabilities. Only completion tokens, through the first EOS, contribute. Each rollout group gets at most one update. Groups with identical rewards are logged and skipped because their leave-one-out advantages are zero.

This is **on-policy REINFORCE with a leave-one-out baseline**, a small RLOO-style implementation. It is RL with verifiable rewards, but is not GRPO or PPO. To keep the teaching code and compute small, this example has **no KL penalty, value model or PPO clipping**. It is intended for a handful of updates. TRL's full [RLOO implementation](https://huggingface.co/docs/trl/rloo_trainer) describes reference-policy regularization and additional training machinery; [GRPO](https://huggingface.co/docs/trl/grpo_trainer) is another extension once this loop is understood.

Sampling uses temperature 1, no top-k/top-p filtering, and no dropout; sampled actions and the log probabilities used by the policy gradient therefore match. LoRA changes the existing SFT adapter. Correct answers are only used by the external reward checker, never appended to the policy input or used as cross-entropy targets during RL.

**Measured outcome, 7 September 2026.** On one Modal L4, starting from the saved 40-update Polish SFT adapter:

- 12 groups × 4 rollouts = 48 sampled answers.
- Five groups had mixed rewards and produced updates; seven uniform-reward groups were skipped.
- Adapter parameters changed. Save/reload reproduced the deterministic predictions exactly.
- RL training, including rollouts: 2.05 seconds; peak PyTorch allocation: 0.924 GB.
- Accuracy on eight separate questions: **4/8 before → 4/8 after**.

This establishes that the loop works and gets nonzero reward variation. It does **not** demonstrate a held-out improvement. The test uses larger numbers than the SFT exercise, so its 4/8 baseline is not comparable to that example's 8/8. Training and held-out prompts are disjoint. The tiny fixed test should not become a hyperparameter-tuning target.

Inspect `rollouts.json` for sampled text, rewards, advantages and updates. `rl_result.json` records timing and parameter/reload checks. Before/after/reloaded predictions are saved too. Exact tested directories appear in [test results](TEST_RESULTS.md).

**Exercises.** Predict which sampled answers get positive advantage. Explain why four correct answers produce no update in this estimator. Inspect four wrong answers and decide whether to improve the SFT warm start or change task difficulty. Compare a reward for correct formatting with the exact-answer reward and identify what the former fails to measure.

Start with the supplied 48-rollout configuration. No judge API, paid teacher or larger model is needed. The training loop checks its 90-second budget after each group; loading and evaluation are outside that limit. Modal provides a separate 600-second function timeout and zero function retries. Repeated container-initialization errors can still be retried by the platform: stop the affected app if that happens.
