import pytest

from task_number_3 import avoid_mistake, get_unique_values_amount


@pytest.mark.parametrize(
    "test_input,expected", [("aab", 1), (["abc1", "aaabbcc11"], 2), ("abbbccdf", 3)]
)
def test_compare_avoid_mistake(test_input, expected):
    assert avoid_mistake(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [("aab", 1), ("abbbccdf", 3), (("apple", "banana", "cherry"), 3)],
)
def test_compare_get_unique_values_amount(test_input, expected):
    assert get_unique_values_amount(test_input) == expected


def test_check_wrong_type_only_list_or_str():
    list_example_for_mistake = [123, {"Saasha": "ahsaS", "python123": "nohtyp123"}]
    for example in list_example_for_mistake:
        with pytest.raises(Exception) as error:
            avoid_mistake(example)
        assert str(error.value) == "Argument must be a string or list"
