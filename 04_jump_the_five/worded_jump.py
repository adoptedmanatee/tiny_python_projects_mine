#!/usr/bin/env python3
"""
Author : Wesley Robertson
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
        "1": "Nine",
        "2": "Eight",
        "3": "Seven",
        "4": "Six",
        "5": "Zero",
        "6": "Four",
        "7": "Three",
        "8": "Two",
        "9": "One",
        "0": "Five",
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
