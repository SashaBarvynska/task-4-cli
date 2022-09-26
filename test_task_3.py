import pytest

import task_3


def test_compare():
    assert task_3.avoid_mistake("11223") == 1
    assert task_3.get_unique_values_amount_("1235") == 4


if __name__ == "__main__":
    pytest.main()
