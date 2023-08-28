#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
You can send some information to your script. Try this
>> python 4_sending_arguments.py 'bonjour' 1 2 3

NOTHING SHOULD BE HARDCODED IN THE SCRIPT. Ex: paths should be asked to user.
"""
import sys


def main():
    args = sys.argv

    # By defaults, args = ['4_sending_arguments.py']  (its own name)

    if len(args) > 1:
        print("You have sent arguments!!! Congrats!")
        print("Args are:")
        print(args)
    else:
        print("Try sending arguments to your script")
        print("Use this:")
        print(">> python 4_sending_arguments.py 'bonjour' 1 2 3")


if __name__ == "__main__":
    main()
