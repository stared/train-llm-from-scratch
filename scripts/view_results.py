# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Open your latest completed exercise, or a saved example with --example."""
import argparse
from pathlib import Path
import webbrowser
from training_report import render

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = {'tokens':'tokenizer.html', 'pretrain':'literature-training.html',
            'sft':'prawko-training.html', 'rlvr':'rlvr-results.html'}
PATTERNS = {'pretrain':'scratch-*', 'sft':'prawko-sft-*', 'rlvr':'rlvr-train-six_words-*'}


def choose(stage, example=False):
    if stage != 'tokens' and not example:
        candidates = [p for p in (ROOT/'runs').glob(PATTERNS[stage]) if (p/'result.json').exists()]
        if candidates:
            return render(max(candidates, key=lambda p:(p/'result.json').stat().st_mtime))
        print('No completed run found; opening the saved example.')
    return ROOT/'results'/EXAMPLES[stage]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=EXAMPLES)
    parser.add_argument('--example', action='store_true', help='Open the included result; no training or account needed')
    parser.add_argument('--no-browser', action='store_true', help='Print the path only')
    args = parser.parse_args()
    path = choose(args.stage, args.example)
    print(path.relative_to(ROOT))
    if not args.no_browser:
        webbrowser.open(path.resolve().as_uri())
