from argparse import ArgumentParser

from task_3 import avoid_mistake


def init_parser() -> str:
    parser = ArgumentParser(description="Get unique values amount")
    parser.add_argument("--string")
    parser.add_argument("--file")
    args = parser.parse_args()
    return main(args)


def main(args):
    if not args.string and not args.file:
        raise Exception("at least one of --string and --file required")
    if args.file:
        return avoid_mistake(str(open_file(args.file).read()))
    elif args.string:
        return avoid_mistake(args.string)


def open_file(file_path: str) -> str:
    try:
        return open(file_path, "r")
    except:
        raise FileNotFoundError(f"File {file_path} does not exist")


if __name__ == "__main__":
    init_parser()
