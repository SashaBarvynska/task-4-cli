import argparse

from task_3 import avoid_mistake


def add_agrum_to_cli():
    parser = argparse.ArgumentParser(description="Get unique values amount")
    parser.add_argument("--string")
    parser.add_argument("--file")
    args = parser.parse_args()

    if not args.string and not args.file:
        parser.error("at least one of --string and --file required")

    if args.file:
        return open_file(args)
    return read_string(args)


def open_file(args):
    try:
        with open(args.file, "r") as reader:
            print(avoid_mistake(str(reader.read())))
    except FileNotFoundError:
        "file {} does not exist".format(args.file)


def read_string(args):
    avoid_mistake(args.string)


add_agrum_to_cli()
