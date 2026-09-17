# Small-model choices for participants

Checked 6–7 September 2026. Here, small means roughly 0.3–4B dense language-model parameters, with a few larger-memory alternatives. Release dates are announcements, not Hugging Face repository creation dates. A newly uploaded quantization or speculative-decoding draft is not a new standalone model generation.

**Verified recipes:** LFM2.5-350M (all three exercises), LFM2.5-2.6B (JSON extraction), Qwen3.5-0.8B (routing), and Gemma 4 E2B **instruction-tuned** (two-update compatibility check). Gemma must use `google/gemma-4-E2B-it`; the checkpoint without `-it` is a base checkpoint without a chat template. See [test results](../results/test-results.md) for limitations and exact measurements.

| Family | Relevant sizes | Recency | Why choose it? | Tradeoff |
|---|---|---|---|---|
| **Liquid LFM2.5** | 350M, 1.2B, 2.6B | 1.2B January 2026; 2.6B **4 August 2026** | Particularly interesting for tiny, fast models and recent agent-oriented work | Hybrid architecture; Liquid license rather than Apache 2.0; thinking behavior varies by checkpoint |
| **Qwen3.5** | 0.8B, 2B, 4B; optional 9B | March 2026 small family | Modern multilingual/multimodal option; choose the smallest size that learns your task | Architecture-specific loader; total multimodal size exceeds the language-model label |
| **Gemma 4** | E2B, E4B | **2 April 2026** | Modern alternative with text, image and audio capabilities | E2B is 5.1B including embeddings, E4B 8B; effective parameters are not memory requirements |
| **Ministral 3** | 3B; larger 8B/14B | December 2025; technical report January 2026 | Another contemporary dense family | Not validated in this starter kit |
| **SmolLM3** | 3B | July 2025 | Educational alternative with public training material | Older than the 2026 releases |
| **Qwen3** | 0.6B, 1.7B, 4B | 2025 | Simple text-only fallback for a low-cost first run | Older generation; turn thinking off for short-answer exercises |
| **Bielik v3 small** | 1.5B, 4.5B | 2025 | Direct Polish hackathon relevance | Access to the selected instruct checkpoint returned HTTP 401 during preparation; arrange access first |

Sources: [Liquid's August 4 announcement](https://www.liquid.ai/blog/lfm2-5-2-6b), [Liquid 1.2B card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct), [Liquid 350M card](https://huggingface.co/LiquidAI/LFM2.5-350M), [Qwen3.5 small card](https://huggingface.co/Qwen/Qwen3.5-0.8B), [Gemma 4 launch](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/), [Gemma parameter accounting](https://huggingface.co/google/gemma-4-E2B), [Ministral report](https://arxiv.org/abs/2601.08584), [SmolLM3 card](https://huggingface.co/HuggingFaceTB/SmolLM3-3B), [Qwen3 card](https://huggingface.co/Qwen/Qwen3-0.6B), [Bielik small report](https://arxiv.org/abs/2505.02550).

**My selection advice:** offer a cheap tested model for the first experiment, Qwen3.5 for a modern multilingual alternative, and LFM2.5-2.6B for participants who specifically want a very recent release. Gemma 4 is worth offering as an advanced alternative rather than pretending E2B is the same memory class as Qwen 2B. The actual tested combinations and failures belong in `results/test-results.md`; presence in `scripts/models.json` only means checkpoint metadata is pinned, not that the recipe is verified.

Qwen3.8-27B was released in August, but is outside this small-model budget category. Liquid's August 20 DSpark releases are draft models for accelerating existing models, not replacements to pick as standalone SFT students. [Qwen3.8 repository](https://github.com/QwenLM/Qwen3.8), [DSpark announcement](https://www.liquid.ai/blog/lfm2.5-dspark).

Do not select MoE models by active parameter count alone: all stored experts still matter for memory. Likewise, GGUF inference support does not establish a working training recipe. Use original Transformers checkpoints here. Treat vendor benchmarks as shortlist evidence; choose the workshop winner from your own fixed task and budget.
