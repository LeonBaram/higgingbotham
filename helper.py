import re


def mod(score: int) -> int:
    return (score - 10)//2


def counter(curr, max=None, reset=None):
    curr = curr if curr else "0 / 0"
    reset = reset if reset else []
    if not isinstance(reset, list):
        reset = [reset]
    current_val, current_max = [x.strip() for x in curr.split('/')]
    max = max if max else current_max
    val = max if any(reset) else current_val
    return f'{val} / {max}'


def weight(item):
    pattern = r'(\d+x )?([\d.]+lb )?.+'
    match = re.fullmatch(pattern, item)
    if not match:
        return 0
    q, w = match.groups()
    q = q if q else "1"
    w = w if w else "0"
    q = float(q.strip(" x"))
    w = float(w.strip(" lb"))
    return q * w
