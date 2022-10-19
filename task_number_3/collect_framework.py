import argparse

from task_3 import avoid_mistake

parser = argparse.ArgumentParser(description="test_parse")
parser.add_argument("--string")
parser.add_argument(("--file"))
args = parser.parse_args()

if args.string is None and args.file is None:
    parser.error("at least one of --string and --file required")
if args.file is not None:
    f = open(f"../{args.file}", "r")
    avoid_mistake(str(f.read()))
    f.close()
else:
    avoid_mistake(args.string)
