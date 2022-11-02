from collections import Counter
from collections.abc import Iterable
from functools import cache


def avoid_mistake(string: str or Iterable) -> str or tuple:
    if not isinstance(string, Iterable):
        raise TypeError("Argument must be a string, list, tuple or set")

    return (
        list(map(get_unique_values_amount, string))
        if not isinstance(string, str)
        else get_unique_values_amount(string)
    )


@cache
def get_unique_values_amount(string: str or tuple) -> int:

    if not isinstance(string, str) and not isinstance(string, tuple):
        raise TypeError("Argument must be a string, tuple")
    return len(
        list(filter(lambda key: result_dict[key] == 1, result_dict := Counter(string)))
    )
