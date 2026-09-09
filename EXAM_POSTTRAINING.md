# Reasoning for an ABCD exam with answer-key labels

The starting dataset contains questions, options and correct letters only. There are no supplied reasoning traces. A one-letter final answer may require substantial computation before the model produces it; a reasoning model can generate intermediate text and then return the letter.

Published lab workflows support several approaches. No single recipe is universally best, and our prawko results do not establish a decisive RLVR advantage.

| Approach | Training material | What is optimized |
|---|---|---|
| Answer-only SFT | Question → correct letter | Likelihood of the correct answer directly |
| Filtered-reasoning SFT | Generate reasoning and answers; retain correct-answer attempts | Likelihood of the retained reasoning **and** final answer |
| RLVR | Sample reasoning and answers; compare final answer with the key | Generated-response probabilities using an outcome reward |
| SFT → RLVR | First learn from retained examples, then generate and score new attempts | Demonstration learning followed by outcome-based optimization |

Filtered-reasoning SFT needs no pre-existing reasoning labels: an existing model supplies candidate demonstrations. This is a rejection-sampling fine-tuning approach. STaR is an early related method, although its original setup also uses a few rationale demonstrations for bootstrapping. [STaR paper](https://arxiv.org/abs/2203.14465)

For RLVR, the checker can score only the final letter. It need not grade the reasoning token by token. The reward is used to update the generated trajectory's probability. A capable starting model may enter RL directly; others benefit from SFT first. DeepSeek published both the direct-RL R1-Zero approach and an R1 pipeline combining SFT and RL stages. [Official DeepSeek-R1 description](https://github.com/deepseek-ai/DeepSeek-R1)

## Correction to the earlier discussion

Generating arbitrary reasoning, appending the correct letter and applying SFT loss only to that letter is technically possible. However, it is not the main established workflow to recommend here. It trains answer prediction conditional on the supplied trace; ordinary backpropagation does not differentiate through the discrete sampling choices that produced that trace. Shared parameters can change reasoning behavior indirectly. This differs from explicitly imitating successful reasoning or reinforcing it with an outcome reward.

Therefore, “only answer labels are available” does **not** imply that the trained model must answer in one token without generated reasoning. Reasoning supervision can be generated and filtered, or reasoning can be trained through RLVR without reference traces.

## Proposed serious comparison — not yet run

1. Measure the unchanged existing reasoning model at a fixed inference budget.
2. Compare answer-only SFT, filtered-reasoning SFT, RLVR and SFT → RLVR.
3. Keep whole exam papers/question families held out; separate validation from final testing and account for possible pretraining contamination.
4. Generate/filter demonstrations only for training questions. Check a sample of their explanations: the right letter does not prove valid reasoning.
5. Where options can safely be reordered, shuffle them and remap the correct letter to detect position shortcuts. Do not blindly reorder questions whose wording refers to option positions.
6. Report accuracy, uncertainty from a limited test set, invalid outputs, inference tokens/time and training cost. Compare methods under explicit budgets.

A four-option task admits lucky guesses. Rewarding a correct letter is an objective answer check, but it is not proof that the model's explanation is faithful or sound. Correctness filtering alone has the same limitation for generated SFT demonstrations.

For Polish matura open-ended questions, distinguish exact-answer verification from rubric grading. Short factual answers may support accepted variants; interpretation and essays generally need semantic assessment. An LLM applying a rubric supplies a model-based reward, whose agreement with human grading must be evaluated. CKE provides example open-task answers and scoring criteria, not a single mandatory wording. [CKE Polish guide](https://bip.cke.gov.pl/attachments/download/10092)

This is a proposed hackathon workflow, not a claim of measured matura performance. Prawko remains the tested workshop task; its combined SFT → RLVR branch has not yet been tested.
