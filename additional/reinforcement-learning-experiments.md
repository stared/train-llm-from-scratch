# Optional reinforcement-learning experiments

Complete the [six-word tutorial](../04-reinforcement-learning.md) first. These are extra experiments. Each additional Modal run incurs compute charges. Scores below come from earlier runs.

## Try

Check whether the successful stories are interesting, as well as valid. For another task, rerun with `--task countdown`; our earlier result was **7/32 → 11/32**, a smaller improvement. Each task starts from the original model.

## Check what the reward actually teaches

We also prompted **Qwen3.5-2B** to explain Polish driving-exam answers, then trained with RLVR rewarding only a correct final letter. Strict success rose **0 → 25/40**, but the model stopped explaining. Reading the explicit answer anywhere in the response gave **25/40 both before and after**. It learned the rewarded format, not better exam knowledge. [Actual outputs and curves](http://localhost:5173/reports#training-comparisons.html).

