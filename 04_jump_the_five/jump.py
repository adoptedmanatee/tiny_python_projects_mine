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
        description='Input phone number and perform encryption',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='phone_number',
                        help='Phone number to be encrypted')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    pos_arg = args.positional
    encrypteR = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}
    encrypteD = []
    for i in str(pos_arg):
      if i in encrypteR:
        
        encrypteD.append(encrypteR[i])
      # print(f'{encrypter[i]}')
    print(''.join(encrypteD))

# --------------------------------------------------
if __name__ == '__main__':
    main()
