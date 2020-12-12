import argparse
import fileinput
import sys

from dice_roller import __version__
from dice_roller.replace import replace_expression


def make_parser(prog):
    parser = argparse.ArgumentParser(
        prog=prog,
        description="Simple utility to help keep rule logs from dnd sessions.",
    )
    parser.add_argument("file", type=str)
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    return parser


def parse_args(argv):
    parser = make_parser(argv[0])
    return parser.parse_args(argv[1:])


def run_dice_roller(args):
    with fileinput.FileInput(args.file, inplace=True, mode="r") as file:
        for line in file:
            print(replace_expression(line))


def parse_args_and_run(argv):
    run_dice_roller(parse_args(argv))


def main():
    parse_args_and_run(sys.argv)


if __name__ == "__main__":
    main()
