#!/usr/bin/env python3
"""
Author : runner <runner@09409b004925>
Date   : 2022-06-09
Purpose: Encrypt Phone Number
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Input phone number and perform encryption",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "positional",
        metavar="phone_number",
        help="Phone number to be encrypted",
        nargs="+",
    )

    parser.add_argument("-o", "--on", help="A boolean flag", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    pos_arg = args.positional
    encrypteR = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    phrase = pos_arg
    new_phrase = []

    for word in phrase:
        new_word_or_digits = []
        list_of_individual_letters_or_digits = list(word)

        for character in list_of_individual_letters_or_digits:
            if character in encrypteR:
                character = encrypteR[character]

            new_word_or_digits.append(character)

        new_phrase.append("".join(new_word_or_digits))

    print(" ".join(new_phrase))


# --------------------------------------------------
if __name__ == "__main__":
    main()
