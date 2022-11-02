from argparse import Namespace
from unittest.mock import mock_open, patch

import pytest

from task_number_4 import main, open_file

file_example = "demo.txt"


@patch(
    "task_number_4.collect_framework.init_parser",
    return_value=Namespace(file=None, string=None),
)
def test_main_without_args(mock_init_parser):
    with pytest.raises(Exception) as error:
        main()
    assert str(error.value) == "At least one of --string and --file required"
    mock_init_parser.assert_called_with()


@patch(
    "task_number_4.collect_framework.init_parser",
    return_value=Namespace(string=None, file=file_example),
)
@patch("task_number_4.collect_framework.avoid_mistake", return_value=3)
@patch("task_number_4.collect_framework.open_file", return_value="demo string")
def test_main_with_file(mock_open_file, mock_avoid_mistake, mock_init_parser):
    assert main() == 3
    mock_open_file.assert_called_with(file_example)
    mock_avoid_mistake.assert_called_with("demo string")
    mock_init_parser.asssert_called_once()


@patch(
    "task_number_4.collect_framework.init_parser",
    return_value=Namespace(string="Python", file=None),
)
@patch("task_number_4.collect_framework.avoid_mistake", return_value=3)
def test_main_with_string(mock_avoid_mistake, mock_init_parser):
    assert main() == 3
    mock_avoid_mistake.assert_called_with("Python")
    mock_init_parser.asssert_called_once()


@patch("builtins.open", side_effect=FileNotFoundError)
def test_open_file_error(mock_open):
    with pytest.raises(FileNotFoundError) as error:
        open_file(file_example)
    assert str(error.value) == "File demo.txt does not exist"
    mock_open.assert_called_with(file_example, "r")


@patch("builtins.open", new_callable=mock_open, read_data="Sasssssssssssss34")
def test_open_file_success(mock_open):
    assert open_file(file_example) == "Sasssssssssssss34"
    mock_open.assert_called_with(file_example, "r")
