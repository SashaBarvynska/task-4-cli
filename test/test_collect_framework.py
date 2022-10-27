from unittest.mock import patch

import pytest

from task_number_3.collect_framework import main, open_file


@patch(
    "task_number_3.collect_framework.init_parser",
    return_value={"string": None, "file": None},
)
def test_main_without_args(mock_init_parser):
    with pytest.raises(Exception) as error:
        main()
    assert str(error.value) == "at least one of --string and --file required"
    mock_init_parser.assert_called_with()


@patch(
    "task_number_3.collect_framework.init_parser",
    return_value={"string": None, "file": "demo.txt"},
)
@patch("task_number_3.collect_framework.avoid_mistake", return_value=3)
@patch("task_number_3.collect_framework.open_file", return_value="demo string")
def test_main_with_file(mock_open_file, mock_avoid_mistake, mock_init_parser):
    assert main() == 3
    mock_open_file.assert_called_with("demo.txt")
    mock_avoid_mistake.assert_called_with("demo string")

@patch(
    "task_number_3.collect_framework.init_parser",
    return_value={"string": "Python", "file": None},
)
@patch("task_number_3.collect_framework.avoid_mistake", return_value=3)
def test_main_with_string(mock_avoid_mistake, mock_init_parser):
    assert main() == 3
    mock_avoid_mistake.assert_called_with("Python")


def test_open_file_error():
    with pytest.raises(FileNotFoundError) as error:
        open_file("demo")
    assert str(error.value) == "File demo does not exist"
