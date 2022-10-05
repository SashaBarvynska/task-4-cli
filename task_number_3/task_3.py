from collections import Counter
from functools import cache


def avoid_mistake(string: str or list or set) -> str or tuple:
    if (
        not isinstance(string, str)
        and not isinstance(string, list)
        and not isinstance(string, set)
        and not isinstance(string, tuple)
    ):
        raise TypeError("Argument must be a string, list, tuple or set")
    get_unique_values_amount(
        tuple(string)
        if isinstance(string, list)
        or isinstance(string, set)
        or isinstance(string, tuple)
        else string
    )
    return (
        list(map(get_unique_values_amount, string))
        if isinstance(string, list)
        or isinstance(string, set)
        or isinstance(string, tuple)
        else get_unique_values_amount(string)
    )


@cache
def get_unique_values_amount(string: str or tuple) -> int:

    if not isinstance(string, str) and not isinstance(string, tuple):
        raise TypeError("Argument must be a string, tuple")
    return len(
        list(filter(lambda key: result_dict[key] == 1, result_dict := Counter(string)))
    )
