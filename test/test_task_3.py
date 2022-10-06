import pytest

from task_number_3 import avoid_mistake, get_unique_values_amount


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("aab", 1),
        (["abc1", "aaabbcc11"], [4, 0]),
        ("abbbccdf", 3),
        ({"abc", "drt"}, [3, 3]),
    ],
)
def test_compare_avoid_mistake(test_input, expected):
    assert avoid_mistake(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [("aab", 1), ("abbbccdf", 3), ("apple", 3)],
)
def test_compare_get_unique_values_amount(test_input, expected):
    assert get_unique_values_amount(test_input) == expected


@pytest.mark.parametrize(
    "test_input",
    [
        123,
        False,
    ],
)
def test_check_wrong_type_only_list_or_str(test_input):
    with pytest.raises(Exception) as error:
        avoid_mistake(test_input)
    assert str(error.value) == "Argument must be a string, list, tuple or set"


def test_function_contains_cache():
    assert hasattr(get_unique_values_amount, "__wrapped__")
