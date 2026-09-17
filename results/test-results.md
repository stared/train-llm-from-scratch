# Live test results — 6–7 September 2026

All successful jobs used one Modal NVIDIA L4, BF16 LoRA, a pinned model revision, and Python 3.12. No teacher API or external dataset was used. These are small synthetic verification experiments, not general model rankings.

| Model | Exercise | Updates | Strict correct before → after | Train seconds | Timed remote seconds | Peak allocated GB | Estimated compute |
|---|---|---:|---|---:|---:|---:|---:|
| gemma4-e2b | routing | 2 | 8/8 → 8/8 | 2.65 | 47.54 | 10.726 | $0.0126 |
| lfm2.5-2.6b | extraction | 20 | 0/8 → 7/8 | 8.44 | 88.53 | 5.699 | $0.0235 |
| lfm2.5-350m | extraction | 40 | 0/8 → 8/8 | 9.84 | 42.23 | 0.825 | $0.0112 |
| lfm2.5-350m | polish | 40 | 0/8 → 8/8 | 10.48 | 35.16 | 0.803 | $0.0094 |
| lfm2.5-350m | routing | 20 | 2/8 → 6/8 | 3.86 | 29.41 | 0.819 | $0.0078 |
| qwen3.5-0.8b | routing | 20 | 2/8 → 5/8 | 39.00 | 73.48 | 2.237 | $0.0195 |

**What passed.** Finite training loss, changed adapter parameters, saved adapter/tokenizer, fresh base-model reload, and identical deterministic before-save/after-reload predictions. Reload was in the same process; a separate-process CLI training/reload has not been tested. Local CPU/MPS training has not been benchmarked. Five dependency-free unit tests cover dataset separation, strict scoring and reward/advantage logic.

**What the scores mean.** Routing has four semantic test templates repeated with different ticket IDs. Extraction holds out IDs and phrasing; strict scoring rejects Markdown fences. For LFM350M, stripping only surrounding JSON fences changes the extraction baseline from 0/8 to 1/8; after SFT it remains 8/8. Polish tests use different wording and larger numbers than training. Eight cases are enough to expose bugs, not establish statistical superiority. There is no fine-tuning gain for Gemma: it already gets 8/8. Its two updates only test compatibility. No model was selected by repeatedly optimizing this test set.

**RLVR.** LFM2.5-350M starts from the Polish SFT adapter, samples 48 answers and trains with an exact arithmetic verifier. Five of 12 groups had mixed rewards, producing five policy-gradient updates. Adapter change and reload checks passed. Held-out accuracy stayed 4/8 → 4/8. The RL training/rollout loop took 2.05 seconds, timed remote execution 25.35 seconds, and estimated compute $0.0067. This is working RLVR with a nonzero signal, not demonstrated generalization improvement. See [the runnable RLVR guide](../docs/notes/rlvr.md).

**Models actually verified.** LFM2.5-350M, LFM2.5-2.6B, Qwen3.5-0.8B and Gemma 4 E2B Instruct. Other aliases in `config/models.json` are pinned options, not claims of tested compatibility. In particular, LFM1.2B, Qwen2B/4B and SmolLM3 have not been run here.

**Failures found and fixed.**

- The first tokenizer call returned a BatchEncoding under Transformers 5.16. Explicit `return_dict=False` fixed the list-based training path. This failed before model weights were loaded.
- The first Gemma selection was the base checkpoint without a chat template. The actual chat recipe uses `google/gemma-4-E2B-it`.
- Inspection of the first successful Gemma smoke run exposed a wrong target terminator: generic `<eos>` instead of Gemma’s `<turn|>`. After correcting both supervision and generation stopping, the first-step loss fell from about 8.08 to 0.0000035. The earlier run is preserved and labeled superseded in `scripts/report.py`; it is excluded from the main table but included in spending estimates.
- The first RLVR Modal wrapper referenced a local module absent from the container. Modal retried initialization despite zero function retries; the app was explicitly stopped and the wrapper made self-contained. The corrected run succeeded. Function timeouts and retry settings do not by themselves bound all startup behavior.

**Spending.** The recorded successful calls, including the superseded Gemma run and RLVR, total approximately **$0.119** in estimated requested compute. The formula is timed remote seconds × (L4 $0.000222/s + 2 CPU cores × $0.0000131/s + 8 GiB RAM × $0.00000222/s). It is not a Modal invoice: image building, startup, failed attempts, resource usage above requested allocations, and ongoing cache storage are excluded. The shared dependency image initially took about 65 seconds to build. [Rates checked September 6](https://modal.com/pricing).

The preparation used an initial $2 estimated-compute planning ceiling. Jobs ran sequentially, with short update budgets and 600-second function timeouts; no long training or hyperparameter sweep was launched. The persistent volume retains cached models and adapters so subsequent workshops avoid downloads. It can incur storage charges. No serving deployment was created.

**Reproduce the cheap experiments.**

```bash
uvx --from modal==1.5.0 modal run scripts/modal_app.py --model lfm2.5-350m --task routing --steps 20 --eval-size 8 --max-seconds 90
uvx --from modal==1.5.0 modal run scripts/modal_app.py --model lfm2.5-350m --task extraction --steps 40 --eval-size 8 --max-seconds 90
uvx --from modal==1.5.0 modal run scripts/modal_app.py --model lfm2.5-350m --task polish --steps 40 --eval-size 8 --max-seconds 90
uv run scripts/report.py
```

Change `--model` to a verified alias to compare models. `uv run scripts/smoke_matrix.py` reruns the documented five-job matrix sequentially; it is not necessary for using one exercise. Primary dependencies and revisions are pinned; full installed package versions are recorded per successful SFT run, and local uv script lockfiles are included.

**Raw results.**

- [gemma4-e2b-routing-1788768655398144772](../runs/gemma4-e2b-routing-1788768655398144772/result.json)
- [gemma4-e2b-routing-1788768861693048134](../runs/gemma4-e2b-routing-1788768861693048134/result.json)
- [lfm2.5-2.6b-extraction-1788723910717595216](../runs/lfm2.5-2.6b-extraction-1788723910717595216/result.json)
- [lfm2.5-350m-extraction-1788723727213842534](../runs/lfm2.5-350m-extraction-1788723727213842534/result.json)
- [lfm2.5-350m-polish-1788723780228847254](../runs/lfm2.5-350m-polish-1788723780228847254/result.json)
- [lfm2.5-350m-routing-1788723627836817965](../runs/lfm2.5-350m-routing-1788723627836817965/result.json)
- [qwen3.5-0.8b-routing-1788723826217777081](../runs/qwen3.5-0.8b-routing-1788723826217777081/result.json)
- [RLVR result](../runs/rlvr-1788768609860683095/rl_result.json)
- [Matrix outcomes and failure logs](../runs/matrix-1788723721307496000/matrix.json)
