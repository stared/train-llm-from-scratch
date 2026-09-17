"""Three workshop tasks. Stdlib-only data generators and transparent verifiers.

No generated code is executed. References stay in the checker, never in the
policy's training input. Strict success is separate from shaped reward.
"""
import ast
from collections import Counter, deque
from fractions import Fraction
import random
import re

TASKS = ('six_words', 'countdown', 'maze')
MAX_TOKENS = {'six_words': 40, 'countdown': 48, 'maze': 32}
WORDS = ('robot dragon ghost astronaut pirate wizard detective vampire princess '
         'alien moon castle garden library spaceship bakery island ocean forest '
         'mirror clock key letter violin umbrella suitcase candle crown coffee '
         'snow rain thunder midnight sunrise wedding birthday funeral holiday '
         'cat dog owl fox whale rabbit mouse raven wolf tiger '
         'chef king queen teacher painter sailor pilot farmer doctor clown').split()
NOVEL = 'mermaid volcano telescope penguin submarine circus glacier mushroom dinosaur lighthouse violinist desert balloon comet portrait notebook'.split()


def word_list(text):
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text.lower())


def expression(text):
    """A bounded arithmetic AST interpreter, deliberately NOT eval()."""
    if len(text) > 96 or not re.fullmatch(r'[0-9+*/()\s-]+', text):
        raise ValueError('Expression characters/length')
    tree = ast.parse(text.strip(), mode='eval')
    if sum(1 for _ in ast.walk(tree)) > 32:
        raise ValueError('Too many nodes')
    numbers = []

    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) is int and 0 < node.value <= 1000:
            numbers.append(node.value)
            return Fraction(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in (ast.Add, ast.Sub, ast.Mult, ast.Div):
            a, b = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add):
                return a + b
            if isinstance(node.op, ast.Sub):
                return a - b
            if isinstance(node.op, ast.Mult):
                return a * b
            return a / b
        raise ValueError('Unsupported arithmetic')

    return visit(tree.body), numbers


MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def shortest(grid, start, goal):
    queue = deque([(tuple(start), '')])
    seen = {tuple(start)}
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == tuple(goal):
            return path
        for symbol, (dr, dc) in MOVES.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < 4 and 0 <= nc < 4 and grid[nr][nc] != '#' and (nr, nc) not in seen:
                seen.add((nr, nc))
                queue.append(((nr, nc), path + symbol))
    return None


def check(task, row, text):
    text = text.strip()
    if task == 'six_words':
        words = word_list(text)
        n = len(words)
        anchors = sum(w in words for w in row['anchors']) / 2
        distinct = len(set(words)) == n
        clean = bool(re.fullmatch(r"[A-Za-z\s.,!?;:'\"—-]+", text)) and '\n' not in text
        success = n == 6 and anchors == 1 and distinct and clean
        reward = .2 * max(0, 1 - abs(n - 6) / 6) + .2 * anchors + .1 * (distinct and clean) + .5 * success
        return dict(reward=reward, success=bool(success), word_count=n, anchors=anchors, distinct=distinct, clean=clean)
    if task == 'countdown':
        try:
            value, numbers = expression(text)
        except (ValueError, SyntaxError, ZeroDivisionError, RecursionError):
            return dict(reward=0., success=False, valid_expression=False, uses_numbers=False)
        uses = Counter(numbers) == Counter(row['numbers'])
        success = uses and value == row['target']
        reward = .2 + .3 * uses + (.15 / (1 + float(abs(value - row['target']))) if uses else 0) + .35 * success
        return dict(reward=reward, success=bool(success), valid_expression=True, uses_numbers=uses, value=str(value))
    if task != 'maze':
        raise ValueError(task)
    if not re.fullmatch(r'[UDLR]{1,12}', text):
        return dict(reward=0., success=False, valid_format=False, collision=False)
    r, c = row['start']
    collision = False
    for move in text:
        dr, dc = MOVES[move]
        r, c = r + dr, c + dc
        if not (0 <= r < 4 and 0 <= c < 4) or row['grid'][r][c] == '#':
            collision = True
            break
    success = not collision and [r, c] == row['goal']
    progress = 0.
    if not collision:
        remaining = shortest(row['grid'], [r, c], row['goal'])
        if remaining is not None:
            progress = max(0., 1 - len(remaining) / len(row['reference']))
    return dict(reward=.1 + .2 * (not collision) + .2 * progress + .5 * success,
                success=bool(success), valid_format=True, collision=collision, end=[r, c])


def make_data(task, train_size=256, dev_size=24, test_size=32):
    rng = random.Random(20260907)
    seen = set()
    splits = {}
    for split, count in [('train', train_size), ('dev', dev_size), ('test', test_size)]:
        rows = []
        while len(rows) < count:
            if task == 'six_words':
                pool = NOVEL if split == 'test' and len(rows) >= count // 2 else WORDS
                anchors = sorted(rng.sample(pool, 2))
                key = tuple(anchors)
                row = dict(anchors=anchors, novel_words=pool is NOVEL)
                prompt = (f'Write a tiny story in exactly SIX English words. Include the exact words '
                          f'"{anchors[0]}" and "{anchors[1]}". Use each word only once. '
                          'Return only the story, on one line, with no title or explanation. '
                          'Words are sequences of letters; punctuation does not count.')
            elif task == 'countdown':
                a, b, c = [rng.randint(2, 15) for _ in range(3)]
                target, reference = rng.choice([(a*b+c, f'{a}*{b}+{c}'), ((a+b)*c, f'({a}+{b})*{c}'), (a+b-c, f'{a}+{b}-{c}')])
                if not 1 <= target <= 150:
                    continue
                numbers = [a, b, c]
                rng.shuffle(numbers)
                key = (*sorted(numbers), target)
                row = dict(numbers=numbers, target=target, reference=reference)
                prompt = (f'Countdown puzzle: use the numbers {numbers} exactly once each to make {target}. '
                          'Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. '
                          'No equals sign, answer, code fence, or explanation.')
            elif task == 'maze':
                start, goal, wall1, wall2 = rng.sample(range(16), 4)
                grid = [['.'] * 4 for _ in range(4)]
                for cell, symbol in [(start, 'S'), (goal, 'G'), (wall1, '#'), (wall2, '#')]:
                    grid[cell // 4][cell % 4] = symbol
                grid = [''.join(line) for line in grid]
                start, goal = list(divmod(start, 4)), list(divmod(goal, 4))
                reference = shortest(grid, start, goal)
                if reference is None or not 3 <= len(reference) <= 6:
                    continue
                key = tuple(grid)
                row = dict(grid=grid, start=start, goal=goal, reference=reference)
                prompt = ('Move a robot from S to G on this 4x4 map. # is a wall; . is free. '
                          'U=up, D=down, L=left, R=right. Never enter walls or leave the map. '
                          'Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.\n' + '\n'.join(grid))
            else:
                raise ValueError(task)
            if key in seen:
                continue
            seen.add(key)
            rows.append(dict(id=f'{task}-{split}-{len(rows):03}', prompt=prompt, **row))
        splits[split] = rows
    return splits
