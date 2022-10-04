from collections import Counter
from functools import cache


def avoid_mistake(string: str or list) -> str or tuple:
    if not isinstance(string, str) and not isinstance(string, list):
        raise TypeError("Argument must be a string or list")
    return get_unique_values_amount(
        tuple(string) if isinstance(string, list) else string
    )


@cache
def get_unique_values_amount(string: str or tuple) -> int:
    if not isinstance(string, str) and not isinstance(string, tuple):
        raise TypeError("Argument must be a string or tuple")
    all_value_as_string = "".join(string)
    return len(
        list(
            filter(
                lambda key: result_dict[key] == 1,
                result_dict := Counter(all_value_as_string),
            )
        )
    )


print(avoid_mistake(["abc12344", "45698"]))
