# Train a tiny GPT, then teach a small LLM a new task

**8 September update:** the user explicitly wants a new scratch-training v2, not a port of Falenty v1. [SCRATCH_V2.md](SCRATCH_V2.md) supersedes the scratch-model/preset recommendations below; the older measurements remain historical evidence.

Research and proposed workshop, 6 September 2026. Four hours, taught in English, preparing participants for Warsaw Model Trainers. This records the original design brief. **Update, 7 September:** runnable SFT and RLVR examples have now been tested on Modal; see [README](README.md) and [measured results](TEST_RESULTS.md). Historical scratch-training results below come from Falenty; the proposed runtime and spending limits below were rehearsal targets.

**Showcase update:** the user prefers 1–10-minute training and visible creative transformations. [Teach a model a voice](SHOWCASE.md) replaces the proposed passage-to-JSON task as the main fine-tuning exercise. Poetry and original comic dialogue use reusable bilingual datasets and compare ordinary prompting, an explicit style instruction, and a saved adapter. Keep the narrow JSON/arithmetic examples as setup checks and the RLVR illustration. [Data review](DATA_REVIEW.md) shows why the first synthetic poetry draft was rejected.

**Recommendation.** Keep a compressed version of Falenty's progression from counting characters to training a mini-GPT. Spend the second half adapting a pretrained model and measuring whether it improved. Start rehearsals with **Qwen3.5-2B + supervised fine-tuning (SFT) + LoRA on Modal L4**. Rehearse **Bielik-1.5B-v3.0-Instruct** on the same Polish task for hackathon relevance. Choose one default before the workshop. Retain Qwen3-0.6B as the inexpensive fallback. Qwen3.8-27B is an optional comparison, too large to be the first experiment.

The learning outcome is concrete: each pair leaves with a checkpoint trained from random initialization, a fine-tuned adapter, saved predictions, and a comparison against an untouched model. An improvement is a hypothesis to test, not a promised result.

**What the event requires.** The workshop listing welcomes participants without programming or training experience. The hackathon describes a Polish matura-style challenge, questions generated from Polish Wikipedia, a harness track without training, and a fine-tuning track scored partly on improvement over the original model. Its allowed model list and size classes are not specified in the retrieved description. Do not assume Qwen is eligible, or that a model's parameter count establishes eligibility. English instruction and Polish training/evaluation examples can coexist. [Workshop](https://luma.com/Warsaw-Model-Trainers-w3), [hackathon](https://luma.com/Warsaw-Model-Trainers-hackathon).

**What to reuse from Falenty.** The actual reference is `reference/falenty-gpt-2026`, with remote `stared/falenty-gpt`. It contains five substantive notebooks, standalone model scripts, experiment logs, samples, and a separate GPU trainer. The sixth, tokenization notebook is empty. The original README describes three days; fitting that entire progression plus fine-tuning into four hours would be unrealistic.

Keep the next-character guessing game, Markov baseline, visible optimization loop, causal attention picture, and generated samples. Keep the experiment asking whether more context or a larger model helps. Move word-level Markov, full architecture derivation, large sweeps, and longer corpus training to optional reading.

Recorded results in `scripts/results/losses/07_speed_runs_sweep.json`:

| Configuration | Parameters | Recorded training time | Best validation loss, nats/character |
|---|---:|---:|---:|
| Small, 2 layers, context 32 | 113,886 | 40.45 seconds | 2.0292 |
| Medium, 4 layers, context 64 | 470,686 | 260.56 seconds | 1.8007 |
| Larger, 4 layers, context 64 | 824,158 | 358.64 seconds | 1.8113 |

The accompanying report identifies M1 Pro CPU as the hardware. These configurations also differ in learning rate and number of updates: they demonstrate practical choices under a budget, not a controlled causal experiment about parameter count. Use the 470k configuration as the starting point, then repeat on the actual teaching environment. Do not promise those timings on every laptop.

The separate `data/loss_tiny.json` records 1,887,903 parameters, 3,879 seconds (64.7 minutes), and validation loss 1.475. It does not identify its device. That is not evidence for the GPU README's minute-scale estimates, and its corpus/tokenization differ from the small experiments.

**Piotr's teaching style, translated into design choices.** The public [Thinking in tensors, writing in PyTorch](https://github.com/stared/thinking-in-tensors-writing-in-pytorch) explicitly starts with concrete examples and builds dimensional complexity gradually. [Learning Deep Learning with Keras](https://p.migdal.pl/blog/2017/04/teaching-deep-learning/) encourages immediate experimentation and readable code. [livelossplot](https://github.com/stared/livelossplot) makes learning visible while it happens. Falenty carries these ideas into language modeling.

My interpretation: start by asking participants to predict the next character; show predictions before naming cross-entropy; let them change one number and see a consequence. Show a failed hypothesis, such as a larger model producing a worse validation score. Use playful text generation for intuition, then a sharply defined task for useful fine-tuning. Let participants inspect data and mistakes throughout. Keep equations beside the few lines of code implementing them, with deeper mathematics optional.

**Which models to try.** This is a workshop shortlist, not a claim about the universally best small model. Modernity, Polish ability, compatibility, and time per experiment are separate criteria.

| Model | Role | Practical judgment |
|---|---|---|
| [Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) | First modern candidate | Small enough for rapid iteration; supports non-thinking mode, which is its default. Use text-only training and short completions. |
| [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) | Upgrade if 2B fails the task | Worth testing after the pipeline works; more training cost and memory. Do not equate the name with total multimodal checkpoint size. |
| [Bielik-1.5B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-1.5B-v3.0-Instruct) | Polish hackathon candidate | Strong relevance to the event; compare on the actual Polish task and verify eligibility. |
| [Bielik-4.5B-v3.0-Instruct](https://huggingface.co/speakleash/Bielik-4.5B-v3.0-Instruct) | Polish upgrade | Try only if the smaller checkpoint cannot perform the required behavior. |
| [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | Fast fallback and debugging | Text-only architecture with a documented Transformers path; explicitly disable thinking. More limited capability can leave useful room for a narrow fine-tune. |
| [SmolLM3-3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) | Educational alternative | Useful open training background; an alternative if its task performance or software compatibility wins the rehearsal. |
| [Gemma 4 E2B](https://huggingface.co/google/gemma-4-E2B) | Modern comparison candidate | The card lists 2.3B effective but 5.1B including embeddings. It is not a conventional 2B memory comparison. Additional architecture-specific work makes it a second choice here. |
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Optional instructor comparison | Real, current, and fine-tunable; unnecessary size for the first participant loop. |

Qwen's [official Qwen3.8 repository](https://github.com/QwenLM/Qwen3.8) records the 27B release in August 2026 and recommends training frameworks for SFT, DPO, and GRPO. That establishes availability, not a measured workshop configuration. Raw 27B weights alone are roughly 54 GB in BF16 or 13.5 GB at four bits, before quantization metadata, activations, adapters, and runtime overhead. A successful quantized inference demo does not establish training fit or speed.

There is no reason the workshop model must be newer or generally stronger than Qwen3.8-27B. A smaller model with a measurable weakness makes a better teaching experiment. Do not build around a hypothetical Qwen3.8 small checkpoint: the small Qwen checkpoints verified in this research are from Qwen3.5.

**What training to teach in 2026.** These methods address different problems; LoRA is a way of updating parameters, whereas SFT and preference/reward objectives determine what is optimized.

| Method | Appropriate use | Workshop placement |
|---|---|---|
| Training from random weights | Understand how a model learns a distribution | Required: tiny character GPT |
| SFT | Learn from examples of desired responses | Required: small pretrained LLM |
| LoRA | Train small adapter matrices while freezing original weights | Default parameter update method |
| QLoRA | LoRA with quantized frozen base weights | Use if memory or measured runtime warrants extra complexity |
| Distillation through examples | A stronger teacher produces checked demonstrations for SFT | Prepare data beforehand; explain and inspect examples |
| DPO | Learn from chosen/rejected response pairs | Optional extension when real preference data exists |
| GRPO / verifiable-reward RL | Optimize against an executable checker | Brief demonstration; advanced extension |
| Continued pretraining | Adapt to a substantial domain corpus | Explain, skip live |
| Retrieval, prompting, calculator | Improve answers without changing weights | Required baseline comparison; connects to harness track |

SFT remains a sensible starting point: it directly trains on desired outputs, and TRL supports completion-only loss. DPO requires preference pairs. GRPO adds sampled rollouts and reward computation, making latency and reward design additional moving parts. These are reasons for the proposed teaching order, not a claim that RL is obsolete. [TRL SFT](https://huggingface.co/docs/trl/sft_trainer), [DPO](https://huggingface.co/docs/trl/dpo_trainer), [GRPO](https://huggingface.co/docs/trl/grpo_trainer).

For a bonus RL example, use short arithmetic answers with an exact verifier. First check that the model sometimes succeeds and sometimes fails: uniformly zero or perfect rewards are a poor demonstration. Show a reward exploit such as correct JSON with an incorrect answer. Supply recorded training output so completion of the workshop does not depend on live rollout speed.

**A four-hour teaching sequence.** Times include two breaks and assume account setup is completed beforehand. Each pair runs one shared experiment; participants without Python experience can inspect data, choose changes, and interpret results while working with a more experienced partner or facilitator.

| Elapsed | Minutes | Activity and tangible result |
|---|---:|---|
| 00:00–00:15 | 15 | Predict the next character; run the supplied smoke command; distinguish weights, data, and prompts. |
| 00:15–00:35 | 20 | Markov model: change context size, sample text, compare training and validation behavior. |
| 00:35–01:00 | 25 | Neural prediction: inspect a batch, logits, loss, backward pass, and optimizer update; run a small MLP. |
| 01:00–01:25 | 25 | Train supplied mini-GPT from random weights; inspect a causal attention diagram; save and reload a checkpoint. |
| 01:25–01:35 | 10 | Break. |
| 01:35–01:55 | 20 | From text completion to instruction following: tokenization, chat template, SFT, LoRA; score untouched LLM. |
| 01:55–02:30 | 35 | Inspect examples, launch short SFT, watch loss, save adapter. While it runs, inspect baseline errors. |
| 02:30–02:40 | 10 | Break. |
| 02:40–03:05 | 25 | Reload adapter in a fresh process; evaluate; separate correct answers from formatting improvements. |
| 03:05–03:30 | 25 | Change one thing: better examples, more examples, learning rate, or prompt. Run a second experiment. |
| 03:30–03:45 | 15 | Compare prompting/retrieval with training; demonstrate a reward checker and explain GRPO. |
| 03:45–04:00 | 15 | Pairs report evidence; map experiment artifacts to a hackathon submission. |

For a three-hour slot, remove the second experiment (25 minutes), shorten Markov by 10, shorten the neural explanation by 10, and replace the 15-minute methods comparison with a handout. Preserve evaluation and checkpoint reload. Confirm the actual event duration before advertising the four-hour agenda.

**The fine-tuning task.** Start with short passage-grounded question answering: read a paragraph and return a compact JSON object containing `answer` and a verbatim `evidence` span. Include unanswerable cases with an explicit abstention. The task connects to Wikipedia-derived exam questions while avoiding a claim that a tiny fine-tune teaches all matura knowledge.

Use a prepared English practice set and a Polish counterpart; do not require participants to translate data during the session. Rehearse on Polish if hackathon transfer is the main objective. One shared default task is enough: custom datasets are the optional second experiment.

Prepare roughly 500–1,000 training examples, 100 validation examples, and 100 untouched test examples. Group by source article before making questions so related passages cannot cross splits. Deduplicate copied or translated variants. Preserve source URL/revision and attribution. A teacher may draft questions, but verify answers and evidence spans before release. Do not generate the dataset live or silently use model judges as ground truth.

Score answer correctness, JSON validity, evidence-span validity, and abstention separately. A quotation occurring in a passage does not prove that it supports the answer; review a sample manually. Use a small exact-answer/accepted-alias subset for transparent automatic scoring, and a fixed rubric for any free-form questions. A 100-item test set is a teaching instrument: a few extra correct answers are not persuasive evidence of broad capability gains.

Compare untouched model + fixed prompt, untouched model + few-shot prompt, and adapter + the same fixed prompt. If testing retrieval, separately compare retrieved context versus an oracle passage. Keep decoding settings and generation budgets identical across before/after comparisons. Use validation for the second experiment and inspect the final test only after choices are frozen. Report regressions as well as successes.

A useful rehearsal gate: the baseline should have measurable failures on the intended skill. If it is already nearly perfect, use a smaller model or a harder task. If it is almost always wrong, simplify the task or select a stronger model. Do not deliberately sabotage the baseline prompt to manufacture a fine-tuning gain.

**Modal implementation.** Keep normal Python training functions and CLI entrypoints. A thin Modal wrapper supplies the image, GPU, input files, and persistent output directory; it calls the same training implementation. Notebooks may explain or plot results, but no hidden notebook state or coding assistant should be required to run an experiment.

Modal's [Unsloth example](https://modal.com/docs/examples/unsloth_finetune) is a useful infrastructure reference, but not a suitable unchanged workshop preset: the retrieved code defaults include a 32B model and 32,768-token sequences despite prose describing a 14B example. Explicitly replace the model, sequence length, batch, evaluation size, and update budget. [Modal GPU guide](https://modal.com/docs/guide/gpu).

Rehearsal starting settings: LoRA rank 16, learning rate 1e-4, microbatch 1–2, accumulation to an effective batch of 8, maximum total sequence length 512 (1,024 if the dataset needs it), 50–100 optimizer updates, non-thinking output capped around 128 tokens. These are initial experimental settings, not tuned recommendations. Prefer BF16 LoRA for a small model if it fits; benchmark QLoRA only when useful. Validate architecture-specific adapter targets rather than assuming all models share projection names.

Use a pinned compatible Transformers/PEFT/TRL stack. Qwen3.5 has architecture-specific training support in the [Unsloth guide](https://unsloth.ai/docs/models/qwen3.5/fine-tune); its search-indexed guide was available, but direct page retrieval failed during this research. Treat exact compatibility and advertised memory requirements as needing a real smoke run. If setup consumes more than the allocated rehearsal time, switch to Qwen3-0.6B with the straightforward Transformers path rather than debugging a new kernel stack during class.

Inspect tokenized samples and loss masks: supervise answers, not the entire question/passage. TRL's assistant-only masking depends on appropriate chat-template support; a flag alone is not proof. Check that every training sample has supervised tokens, that truncation retains the answer, and that training and generation use matching chat/EOS conventions. Save the tokenizer/template with the adapter. [TRL masking documentation](https://huggingface.co/docs/trl/sft_trainer).

Persist model downloads and artifacts using [Modal Volumes](https://modal.com/docs/guide/volumes). Give each run its own directory; ensure writes are committed before another container reads them. Warm the image and model cache before class. Set a function timeout and a training update limit, keep retries disabled for the teaching job, and avoid leaving an inference server running between exercises.

**Cost envelope.** Posted GPU rates checked on 6 September 2026, converted from per-second pricing. These exclude CPU, RAM, storage, and any other charges. [Modal pricing](https://modal.com/pricing).

| GPU | GPU cost/hour | GPU cost for 20 minutes | Suggested role |
|---|---:|---:|---|
| L4 | $0.7992 | $0.2664 | First 0.6–2B training rehearsal |
| A10 | $1.1016 | $0.3672 | Alternative to benchmark |
| L40S | $1.9512 | $0.6504 | More memory / throughput option |
| A100 80GB | $2.4984 | $0.8328 | Optional larger-model experiment |
| H100 | $3.9492 | $1.3164 | Only if faster completion justifies it |

Two 20-minute L4 jobs for each of 10 pairs imply about **$5.33 in GPU time**. That is arithmetic for a hypothetical workload, not a measured end-to-end cost. Allocate **$20–30 for rehearsal** and **$30–50 for 10 pairs** as provisional planning envelopes, including evaluation, cold starts and failed attempts. Aim for two useful runs within an hour of total GPU allocation per pair. Actual spend needs a rehearsal measurement. Faster expensive hardware can be cheaper per completed experiment.

Modal currently lists $30/month starter credits, three workspace seats and 10 concurrent GPUs. Do not assume those credits renew per participant in a shared workspace, or that the starter plan accommodates an entire class's access needs. Arrange individual accounts or organizer provisioning in advance; credits are a bonus, not the workshop's operational plan.

**What needs changing when porting Falenty.** These are findings for the new workshop, not changes made to the original repository:

- Replace absolute imports in `scripts/06_best_extended.py` and `07_speed_runs.py`; expose one selectable run instead of launching all configurations.
- Fix `for_gpu/train.py`'s no-argument default: it selects `5min`, which is not in `PRESETS`. Fix the stale command in `generate.py`'s missing-checkpoint message.
- Add an explicit device argument. Existing automatic MPS selection conflicts with the report's documented MPS failure on the original environment.
- Check BF16 support before using it. The GPU trainer enables BF16 on every CUDA device despite its README describing a T4 fallback; that fallback is not implemented in the inspected code.
- Make validation batches fixed and independent of the training RNG. Separate validation from a final test; existing reports reuse the held-out split for configuration selection.
- Save the checkpoint matching the reported score. The shared small-model loop records the minimum validation loss but does not save the corresponding weights; end-of-run samples can come from a different model state.
- Record actual parameter count, hardware, precision, data hash and elapsed time. Replace speculative speedups and approximate model sizes with measurements.
- Keep character-model loss comparisons within one corpus/tokenization/split. Do not compare them numerically with subword LLM losses.
- Translate explanations carefully: backpropagation uses the chain rule, not integration by parts; low temperature does not guarantee correctness; attention weights are not automatically a faithful explanation.

**Minimal repository to build next.** Keep implementation small: `prepare_data.py`, `train_scratch.py`, `finetune.py`, `evaluate.py`, `sample.py`, `modal_app.py`, a locked environment, and a short English worksheet. Support data path, output path, seed, update limit, and device through ordinary arguments. Keep the basic CPU exercise independent of GPU-only fine-tuning dependencies. Pin model revisions as well as packages.

Each output directory should contain configuration, dependency versions, source/data/model revisions, elapsed time, loss history, checkpoint or adapter, and predictions. The adapter manifest must name its base checkpoint. A CPU report command should compare saved prediction files without loading a model. Coding assistants can help explain or modify code, but the learner must be able to rerun every claimed result from the documented command with the assistant closed.

**Preparation order and acceptance gates.** First port the small scratch preset and confirm fresh-process reload. Then prepare and validate the QA data and run the untouched-model baseline. Next do a two-update Modal smoke run, save/reload the adapter, and prove that adapter parameters changed. Only then run 50–100 updates and evaluate quality. Compare L4 with one faster GPU only if the first run is too slow. Choose between Qwen and Bielik on task results and event eligibility, then freeze the environment.

Target a warm training run under 15 minutes and evaluation under five minutes; record cold download/image time separately. Stop adding features once both core exercises run cleanly from a fresh checkout, artifacts reload, and participants can explain one error. Prepare honest recorded results and a downloadable checkpoint for service failures. The highest-value remaining work is this small rehearsal, not a broad benchmark sweep or a larger model.
