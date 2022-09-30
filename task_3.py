from collections import Counter
from functools import cache


def avoid_mistake(string) -> str or tuple:
    if not isinstance(string, str) and not isinstance(string, list):
        raise TypeError("Argument must be a string or list")
    return get_unique_values_amount(
        tuple(string) if isinstance(string, list) else string
    )


@cache
def get_unique_values_amount(string) -> int:
    if not isinstance(string, str) and not isinstance(string, tuple):
        raise TypeError("Argument must be a string or tuple")
    string = Counter(string)
    return len(list(filter(lambda key: string[key] == 1, string)))
