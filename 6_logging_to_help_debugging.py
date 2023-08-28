#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
You can use logging instead of print:

You can define the level of each logging message: A debugging information, or
normal information, or a very important warning.

Compare:
>> python 6_logging_to_help_debugging.py
>> python 6_logging_to_help_debugging.py -v
"""

import argparse
import logging


def _build_arg_parser():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument('-v', action='store_true', dest='verbose',
                   help='If set, produces verbose output (DEBUGGING MODE)')

    return p


def main():
    parser = _build_arg_parser()
    args = parser.parse_args()

    logging_level = 'DEBUG' if args.verbose else 'INFO'
    logging.basicConfig(level=logging_level)

    logging.info("Performing some task now!")

    x = 0
    for x in range(8):
        x += 1
        logging.debug("x value is: {}. Ouf, that's a lot of prints! " 
                      "I'm pretty sure my teacher does not need to see "
                      "this.".format(x))

    if x != 8:
        logging.warning("CAREFUL. There seem to be some error in the data or "
                        "in the code.")


if __name__ == "__main__":
    main()
