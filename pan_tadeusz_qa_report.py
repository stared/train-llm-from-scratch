"""Render actual before/after generations. Run: uv run --no-project pan_tadeusz_qa_report.py RUN [--sample-run RUN]."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', type=Path)
    parser.add_argument('--sample-run', type=Path)
    args = parser.parse_args()
    result = json.loads((args.run / 'execution.json').read_text())
    sources = [('Greedy decoding', args.run)]
    if args.sample_run:
        sources.append(('Sampled decoding (seed 42, temperature 0.7, top-p 0.8, top-k 20, repetition penalty 1.1)', args.sample_run))
    report = '# Pan Tadeusz Q&A: actual model results\n\n'
    report += f'Base model: **{result["model_spec"]["id"]}**, revision `{result["model_spec"]["revision"]}`. Fine-tuning: fresh LoRA adapter on the **450 Pan Tadeusz Q&A training pairs** (ordinary Polish prompts → 4–12 verbatim book lines), dataset SHA-256 `{result["data_sha256"]}`. These are actual generated replies, not the dataset targets.\n\n'
    report += f'Training run: `{args.run.name}`; {result["steps"]} updates, {result["training_seconds"]:.2f} seconds, {result["unique_examples_seen"]}/450 unique examples seen, {result["epochs_requested"]} epochs requested. Saved-adapter reload matches: {result["reload_matches"]}.\n\n'
    report += 'Base and fine-tuned conditions use the same ordinary user prompts with no style instruction. The prompted condition adds a poetry system instruction to the untuned base. All shown prompts are held out from Q&A training. Four-to-twelve-line counts measure layout only, not rhyme, meter or humour: prose paragraphs and bullet lists can also pass. Outputs are unedited. Maximum output length: 384 tokens.\n\n'
    costs = []
    for title, run in sources:
        execution = json.loads((run / 'execution.json').read_text())
        costs.append(execution['estimated_compute_usd'])
        outputs = {name: json.loads((run / f'{name}.json').read_text()) for name in ['base', 'prompted', 'finetuned']}
        assert all([r['prompt'] for r in rows] == [r['prompt'] for r in outputs['base']] for rows in outputs.values())
        report += f'## {title}\n\nRun: `{run.name}`.\n\n'
        report += '| Condition | Replies with 4–12 nonempty lines |\n|---|---|\n'
        for name, rows in outputs.items():
            count = sum(4 <= len([line for line in r['answer'].splitlines() if line.strip()]) <= 12 for r in rows)
            report += f'| {name} | {count}/{len(rows)} |\n'
        report += '\n'
        for i, row in enumerate(outputs['base']):
            report += f'### {row["id"]}: {row["prompt"]}\n\n'
            for label, name in [('Before — base, no fine-tuning', 'base'), ('Base plus poetry instruction — no fine-tuning', 'prompted'), ('After — fine-tuned on 450 Pan Tadeusz Q&A pairs', 'finetuned')]:
                report += f'**{label}:**\n\n```text\n{outputs[name][i]["answer"]}\n```\n\n'
    report += f'Estimated requested compute for the completed workers: **${sum(costs):.5f}**, excluding startup/storage and the earlier interrupted training worker. Modal terminated that worker with SIGTERM after update 11 and restarted automatically; its cost is not measured in the successful execution records. This is a timed-resource estimate, not the total invoice.\n'
    Path('pan_tadeusz_qa_results.md').write_text(report)
    print('Saved pan_tadeusz_qa_results.md')


if __name__ == '__main__':
    main()
