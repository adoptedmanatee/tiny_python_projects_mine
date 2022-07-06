#!/usr/bin/env python3
"""
Author : wesleyr <wesleyr@localhost>
Date   : 2022-07-03
Purpose: Concat out file
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Concatenate file contents to stdout",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="A readable file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=None,
    )

    return parser.parse_args()


# --------------------------------------------------


def main():
    args = get_args()
    file_arg = args.file
    with file_arg as f:
        for line in f:
            print(line, end="")


# --------------------------------------------------


if __name__ == "__main__":
    main()
