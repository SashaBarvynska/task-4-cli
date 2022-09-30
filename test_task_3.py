import pytest

import task_3


def test_compare_avoid_mistake():
    cases = [("aab", 1), (["abc1", "aaabbcc11"], 2), ("abbbccdf", 3)]
    for text, reversed_tsxt in cases:
        assert task_3.avoid_mistake(text) == reversed_tsxt


def test_compare_get_unique_values_amount():
    cases = [("aab", 1), ("abbbccdf", 3), (("apple", "banana", "cherry"), 3)]
    for text, reversed_tsxt in cases:
        assert task_3.get_unique_values_amount(text) == reversed_tsxt


def test_check_wrong_type_only_list_or_str():
    list_example_for_mistake = [123, {"Saasha": "ahsaS", "python123": "nohtyp123"}]
    for text, example in enumerate(list_example_for_mistake):
        with pytest.raises(Exception) as error:
            task_3.avoid_mistake(example)
        assert str(error.value) == "Argument must be a string or list"


if __name__ == "__main__":
    pytest.main()
