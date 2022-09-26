from collections import Counter
from functools import cache


def avoid_mistake(string) -> str or tuple:
    return get_unique_values_amount_(
        tuple(string) if isinstance(string, list) else string
    )


@cache
def get_unique_values_amount_(string) -> int:
    string = Counter(string)
    return len(list(filter(lambda key: string[key] == 1, string.keys())))
