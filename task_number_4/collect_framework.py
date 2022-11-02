from argparse import ArgumentParser, Namespace

from task_number_4.task_4 import avoid_mistake


def init_parser() -> Namespace:
    parser = ArgumentParser(description="Get unique values amount")
    parser.add_argument("--string")
    parser.add_argument("--file")
    args = parser.parse_args()
    return args


def main() -> int:
    args = init_parser()
    if not args.string and not args.file:
        raise Exception("At least one of --string and --file required")
    elif args.file:
        return avoid_mistake(open_file(args.file))
    return avoid_mistake(args.string)


def open_file(file_path: str) -> str:
    try:
        with open(file_path, "r") as reader:
            return reader.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} does not exist")
