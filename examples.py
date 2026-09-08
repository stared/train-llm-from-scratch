"""Three small, original synthetic datasets. No downloads or teacher API needed."""
import json
import random

TASKS = ('routing', 'extraction', 'polish')


def dataset(task, split, size=128):
    """Disjoint entities/numbers by split; test wording differs from training.

    This tests narrow synthetic transfer, not real-world or matura competence.
    """
    if task not in TASKS or split not in ('train', 'test'):
        raise ValueError((task, split))
    rows = []
    offset = 0 if split == 'train' else 10000
    for i in range(size):
        n = offset + i
        if task == 'routing':
            category = i % 4
            descriptions = [
                ['I was charged twice.', 'Please refund my duplicate payment.'],
                ['I cannot log in.', 'My password reset link has expired.'],
                ['My parcel has not arrived.', 'Where is the package I ordered?'],
                ['Please add dark mode.', 'I would like a new export feature.'],
            ]
            text = descriptions[category][split == 'test']
            prompt = ('Route the support request. Reply with only the queue code. '
                      'Payments: K1; account access: K2; shipping: K3; feature requests: K4.\n'
                      f'Ticket {n}: {text}')
            answer = f'K{category + 1}'
        elif task == 'extraction':
            item = ['notebook', 'pencil', 'folder', 'eraser'][i % 4]
            quantity = i % 9 + 1
            text = (f'Order {n}: send {quantity} units of {item}.' if split == 'train'
                    else f'Please ship {quantity} units of {item}; reference {n}.')
            prompt = ('Extract the order as JSON with exactly the keys id, item, quantity. '
                      'id and quantity are integers. No explanation.\n' + text)
            answer = json.dumps(dict(id=n, item=item, quantity=quantity), separators=(',', ':'))
        else:
            a, b = n % 97 + (1 if split == 'train' else 101), (i * 7) % 89 + 1
            prompt = ('Odpowiedz tylko liczbą, bez wyjaśnienia.\n' +
                      (f'Ola ma {a} monet i dostaje jeszcze {b}. Ile ma razem?' if split == 'train'
                       else f'Na półce było {a} książek. Dodano {b}. Ile książek jest teraz?'))
            answer = str(a + b)
        rows.append(dict(id=f'{task}-{split}-{i}', prompt=prompt, answer=answer))
    random.Random(42).shuffle(rows)
    return rows


def score(task, prediction, answer):
    prediction = prediction.strip()
    if task == 'extraction':
        try:
            obj = json.loads(prediction)
        except (ValueError, TypeError):
            return dict(correct=False, format_valid=False)
        valid = (isinstance(obj, dict) and set(obj) == {'id', 'item', 'quantity'}
                 and type(obj['id']) is int and type(obj['quantity']) is int
                 and isinstance(obj['item'], str))
        return dict(correct=valid and obj == json.loads(answer), format_valid=valid)
    valid = prediction in ('K1', 'K2', 'K3', 'K4') if task == 'routing' else prediction.isdecimal()
    return dict(correct=prediction == answer, format_valid=valid)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('task', choices=TASKS)
    parser.add_argument('--split', choices=['train', 'test'], default='train')
    parser.add_argument('--size', type=int, default=128)
    args = parser.parse_args()
    for row in dataset(args.task, args.split, args.size):
        print(json.dumps(row, ensure_ascii=False))
