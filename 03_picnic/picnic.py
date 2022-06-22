#!/usr/bin/env python3
"""
Author : runner <runner@2568f23ce835>
Date   : 2022-05-26
Purpose: Picnick Script
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument',
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main"""

    args = get_args()
    pos_arg = args.positional
  
    if args.sorted:
      pos_arg.sort()
    

    if len(pos_arg) >= 2:  # If there are more than 2 items, put 'and' in the list
      pos_arg.insert(-1, 'and')
      if len(pos_arg) == 3: # If the list now contains 3 items (2 items from user plus 'and')
        print(f'You are bringing {" ".join(pos_arg)}.')
      else: # Otherwise, print out the list as a string with commas and REAPLCE 'and,' with no comma ('and')
          arg_str_commas = (', '.join(pos_arg)).replace('and,', 'and')
          print(f'You are bringing {arg_str_commas}.')
    else:
      print(f'You are bringing {"".join(pos_arg)}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()


