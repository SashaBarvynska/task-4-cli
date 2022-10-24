from argparse import ArgumentParser, Namespace
from io import TextIOWrapper

from task_3 import avoid_mistake


def add_agrs_to_cli() -> str:
    parser = ArgumentParser(description="Get unique values amount")
    parser.add_argument("--string")
    parser.add_argument("--file")
    args = parser.parse_args()

    if args.file:
        return open_file(args.file)
    elif args.string:
        return read_string(args.string)
    else:
        return check_cli_without_args(args)


def check_cli_without_args(args: Namespace) -> None:
    if not args.string and not args.file:
        raise Exception("at least one of --string and --file required")


def open_file(file_path: str) -> str:
    try:
        with open(file_path, "r") as reader:
            return read_file(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"file {file_path} does not exist")


def read_file(reader: TextIOWrapper) -> str:
    return avoid_mistake(str(reader.read()))


def read_string(string: str) -> str:
    avoid_mistake(string)

if __name__ == "__main__":
    add_agrs_to_cli()
