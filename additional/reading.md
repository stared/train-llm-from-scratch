# Further reading

## Foundations

- [RecurrentJS — Andrej Karpathy](https://cs.stanford.edu/people/karpathy/recurrentjs/): train an RNN/LSTM in your browser and watch it learn to generate text.
- [MiMo-V2.6 RL dashboard](https://mimo.xiaomi.com/rl/): public post-training dashboard from Xiaomi's MiMo team, led by Luo Fuli. See also [HN discussion](https://news.ycombinator.com/item?id=49732270).
- [Let's build GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY): Karpathy's step-by-step coding walkthrough.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/4): transformers, pretraining and fine-tuning.
- [Nanochat](https://github.com/karpathy/nanochat): explore a complete language-model training pipeline.
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) and [LLM Visualization](https://bbycroft.net/llm): the architecture animated in the browser, on GPT-2 and nano-GPT.
- [Interactive Machine Learning List](https://p.migdal.pl/interactive-machine-learning-list/): interactive explanations, including the [TensorFlow Playground](https://playground.tensorflow.org/).
- [Thinking in tensors, writing in PyTorch](https://github.com/stared/thinking-in-tensors-writing-in-pytorch): Piotr's hands-on introduction to neural networks.

## Pretraining

- [Computation used to train notable AI systems](https://ourworldindata.org/grapher/computation-used-to-train-notable-artificial-intelligence-systems) (Our World in Data) — historical estimates of training compute.
- [Unsupervised sentiment neuron](https://openai.com/index/unsupervised-sentiment-neuron/) (OpenAI, 2017) — sentiment representations learned through next-character prediction.
- [Why Momentum Really Works](https://distill.pub/2017/momentum/) and [An overview of gradient descent optimization algorithms](https://www.ruder.io/optimizing-gradient-descent/) — visual explanations of optimization and gradient descent.
- [MicroGPT](https://karpathy.ai/microgpt.html) — a small GPT implementation; compare its training loop with [train_scratch.py](../scripts/train_scratch.py).

## Fine-tuning

- [Can Generalist Foundation Models Outcompete Special-Purpose Tuning?](https://arxiv.org/abs/2311.16452) (Medprompt, 2023) — on medical exams, careful prompting of a large general model beat fine-tuned specialists. Before training, check what the base model does with a better prompt.
- [Which ML are you?](https://github.com/stared/which-ml-are-you) — accuracy, log-loss, precision and recall as one interactive; the SFT tab shows A/B/C probabilities, which let you examine confidence as well as the chosen answer.
- [Benchmarking Qwen3.8-27B quantizations](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) and [Do Qwen3.6-27B quantizations break the pelican?](https://quesma.com/blog/qwen-quantization-quality/) (Quesma) — what you keep and lose when running a Qwen model at 4-bit; relevant once you take a fine-tuned model out of the cloud.
- [Model cards: Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B), [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) — chat template, context length and the recommended sampling settings.
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer) — a configurable SFT training implementation.

## Reinforcement learning

- [State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A) (Karpathy, 2023) — an overview of pretraining, SFT and reinforcement learning from human feedback.
- [TRL: GRPO trainer](https://huggingface.co/docs/trl/grpo_trainer) and [RLOO trainer](https://huggingface.co/docs/trl/rloo_trainer) — [rlvr_showcase.py](../scripts/rlvr_showcase.py) uses on-policy REINFORCE with a leave-one-out baseline (RLOO); GRPO is the close relative used for DeepSeek-R1.
- [DeepSeek-R1 paper](https://arxiv.org/abs/2501.12948) — RLVR at scale, with a detailed account of training and evaluation.

## Comparing models

Use benchmarks to shortlist models, then evaluate them on examples from your task.

- [Artificial Analysis](https://artificialanalysis.ai/): intelligence, speed and price of hosted models on one page.
- [Arena leaderboard](https://arena.ai/leaderboard): human pairwise preferences, with per-category views; [LiveBench](https://livebench.ai/) refreshes its questions to limit contamination.
- [Epoch AI: GPQA Diamond](https://epoch.ai/benchmarks/gpqa-diamond), [ARC Prize](https://arcprize.org/leaderboard) and [Terminal-Bench](https://www.tbench.ai/?version=2.0): hard reasoning, abstraction and agentic coding.
- [Quesma benchmarks](https://quesma.com/benchmarks/): including [BabaIsBench](https://quesma.com/benchmarks/babaisbench/) (puzzle solving) and [mushroom identification](https://quesma.com/blog/mushroom-llm-vision/) (image classification).
- [Sparks of AGI](https://arxiv.org/abs/2303.12712) and [GPT-4 gets a B on my quantum computing final exam](https://scottaaronson.blog/?p=7209): case studies of GPT-4 evaluation.
