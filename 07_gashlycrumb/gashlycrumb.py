#!/usr/bin/env python3
"""
Author : wesleyr <wesleyr@localhost>
Date   : 2022-07-04
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="letter", nargs="*", help="Letter(s)")

    parser.add_argument(
        "-f",
        "--file",
        help="A readable file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    file_input, users_letters = (args.file, args.input)
    gashlycrumb_dictionary_old = {}
    gashlycrumb_dictionary_new = {}
    for each_line in file_input:
        gashlycrumb_dictionary_old.update([(each_line.rstrip().split(maxsplit=1))])
    for key, value in gashlycrumb_dictionary_old.items():
        gashlycrumb_dictionary_new.update(
            {key.strip().upper(): value}
        )  # Stip white space from keys and convert to upper case for standardized keys

    for letter in users_letters:
        if letter.upper() in gashlycrumb_dictionary_new.keys():
            print(letter.upper(), gashlycrumb_dictionary_new[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()

# Cannot standardize all keys to uppercase without creating a new dict - https://stackoverflow.com/questions/50004310/convert-python-dictionary-to-uppercase
# Commited under the same message ID and appears to have overwritten. Adding change to file 
# The following paths are ignored by one of your .gitignore files: -> was added?
# Changed username git config --global user.name "adoptedmanatee" and email which appropriately authenticates my github user account.