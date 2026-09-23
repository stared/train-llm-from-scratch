# SFT and RLVR on a Mac

Tested on 22–23 September 2026: **MacBook Pro, M5 Max, 128 GB unified memory**. The driving-exam experiments use **Qwen3.5-0.8B**, with the same pinned model revision and data as the workshop.

## Local training support

| Exercise | Model | Mac status | Measured total time |
|---|---|---|---|
| Driving-exam SFT, 100 questions | Qwen3.5-0.8B | Tested, PyTorch MPS BF16 | 1 min 54 s |
| Driving-exam SFT, 289 questions | Qwen3.5-0.8B | Tested, PyTorch MPS FP32 | 3 min 53 s |
| Driving-exam RLVR, 100 questions | Qwen3.5-0.8B | Tested, MPS BF16, learning rate 5e-6 | 2 min 19 s |
| Six-word RLVR | Qwen3.5-4B | Tested, MPS BF16 | 14 min 33 s, including first model download |

## Run

```bash
uv run scripts/prawko.py --device mps --precision bfloat16 --method sft --max-seconds 180 --epochs 10
```

Results are saved in a new `runs/prawko-sft-*` folder. Open **SFT** in `pnpm dev` after completion. The selected LoRA adapter is in `adapter/`; the final adapter is in `final_adapter/`.

## SFT measurements

| Configuration | Train questions | Training | Total | Test before → after | Rotated test after | Memory |
|---|---:|---:|---:|---:|---:|---:|
| MPS FP32, seed 42 | 100 | 121 s | 205 s | 20/40 → 28/40 | 25/40 | — |
| MPS FP32, seed 17 | 100 | 110 s | 135 s | 20/40 → 29/40 | 27/40 | 10.9 GB |
| MPS BF16, seed 42 | 100 | 95 s | 114 s | 19/40 → 28/40 | 26/40 | 8.4 GB |
| MPS FP32, expanded data | 289 | 181 s | 233 s | 20/40 → 35/40 | 29/40 | 10.9 GB |
| MLX BF16, microbatch 1 | 100 | 180 s | 192 s | 18/40 → 28/40 | 28/40 | 10.4 GB |
| MLX BF16, batch 4 | 100 | 182 s | 194 s | 18/40 → 26/40 | 25/40 | 36.7 GB |

[Recorded metrics](macos-fine-tuning.json). Every selected adapter reproduced its first eight test predictions after reload.

The 100-question runs stop at ten epochs; the expanded run stops at the three-minute budget. Training time includes development evaluation. Total time includes model loading, baseline and final evaluations, adapter saving and reload verification; it excludes uv dependency installation. The first FP32 run also downloaded the model.

Checkpoint selection uses the 25 development questions. Test scores use 40 held-out questions; the rotated test changes the order of the same answer options. These are exploratory measurements on a small test set.

The original FP32 run selected epoch 3: **28/40** on the normal test. Its final epoch scored **26/40**, despite reaching **99/100** on training questions.

MPS memory is the largest tensor allocation sampled after a forward pass. MLX reports its allocator peak. Neither figure measures total system RAM.

## More data

```bash
uv run scripts/prawko.py --device mps --method sft --max-seconds 180 --epochs 10 --lr 2e-5 --dataset-path datasets/prawko-v2/extended.json
```

This uses 289 training questions and preserves the same development/test splits. The measured FP32 run improved **20/40 → 35/40**, with **29/40** after rotating the answer options.

## MLX comparison

```bash
uv run additional/scripts/prawko_mlx.py --output runs/prawko-mlx --max-seconds 180
```

The MLX experiment uses the same prompt, full-vocabulary answer loss, LoRA rank 16 and effective batch size 4. Its adapter initialization and numerical implementation differ from PyTorch; the untrained baseline also differs. Both implementations are evaluated independently before training.

The batched MLX run completed more updates than the microbatch run within three minutes, but its selected checkpoint scored 26/40 versus 28/40. PyTorch/MPS was faster in these configurations.

[MLX LoRA documentation](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md).

## Driving-exam RLVR

```bash
uv run scripts/prawko.py --device mps --precision bfloat16 --method rlvr --max-seconds 180 --epochs 10 --lr 5e-6
```

| Learning rate | Training | Total | Test before → selected | Rotated test after | Selected epoch |
|---|---:|---:|---:|---:|---:|
| 5e-5 | 118 s | 136 s | 19/40 → 19/40 | 20/40 | 0 |
| 5e-6 | 120 s | 139 s | 19/40 → 25/40 | 25/40 | 3 |

Both runs completed ten epochs, with approximately 8.4 GB of sampled MPS tensor memory. The default learning rate collapsed toward one answer, so development selection retained the original model. Reducing the learning rate produced a useful adapter. These are two exploratory runs with one seed, not a learning-rate sweep.

The lower-rate run's final epoch scored 27/40, but the development-selected epoch scored 25/40. We report the selected adapter. Both runs passed independent checks of metrics, training/test separation, rewards, advantages and adapter reload predictions.

## Six-word RLVR

```bash
uv run scripts/rlvr_showcase.py --device mps --precision bfloat16 --task six_words --model qwen3.5-4b --max-seconds 600 --output runs/rlvr-six-words-mac
```

| Model | Training | Total, first run | Test success before → after | Selected update |
|---|---:|---:|---:|---:|
| Qwen3.5-4B, MPS BF16 | 9 min 38 s | 14 min 33 s | 1/32 → 31/32 | 140 of 160 |

The total includes a first model download of about 4 min 23 s, baseline and final evaluation, saving and reload verification. Dependency installation is excluded. Training completed all 160 updates before the ten-minute budget. A repeat with cached weights has not been timed separately.

Development selection chose update 140, which passed all 24 development prompts. The held-out test passed 31 of 32. The remaining failure repeated a word: “Vampire ate mouse while mouse slept.” Success measures the six-word constraints, not story quality.

All test outputs are included in [the recorded metrics](macos-fine-tuning.json). Rewards, advantages, evaluation metrics, training/test separation and checkpoint selection were independently checked. Reloading the saved adapter reproduced the first eight test outputs exactly. This is one measured run, not a hardware benchmark across seeds.
