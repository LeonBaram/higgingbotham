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
    quantity, weight = match.groups()
    quantity = quantity if quantity else "1"
    weight = weight if weight else "0"
    quantity = float(quantity.strip(" x"))
    weight = float(weight.strip(" lb"))
    return quantity * weight


# alias needed since "int" is used for "intelligence" in the character sheet
integer = int
