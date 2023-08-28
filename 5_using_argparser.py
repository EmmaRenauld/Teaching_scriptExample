#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

------------------------

This is the best way to deal with arguments. It can print help, and ensure that
user provides the right format of arguments (number of arguments, type, etc.)

When using Argparse, if you type this in a terminal:
>>   python 5_using_argparser.py -h

Then, the description of the file will be shown, together with a list of
expected arguments to the file.

Try using it with no arguments: you will see the error.
   python 3_using_argparser.py

------------------------

"""
import argparse


def _build_arg_parser():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawTextHelpFormatter)

    # For each arg:
    #  The arg name. If it starts with --, it is optional.
    #  The help: always write a good explanation!
    #  The type: Expected type (ex, float, int). Default when not defined is str.
    #  The metavar: by default, arg --some_arg with show as:
    #     --some_arg  SOME_ARG
    #        help help help help help
    #     You may change the way it appears: ex, with metavar='a':
    #     --some_arg a
    #        help help help help help
    #  The default: for optional args, default if user does not give a value.
    #      Without a default, default value is always None.
    #  Actions: Do not use booleans as type. Instead, use: store_true (see below)

    # You can group arguments together for a nicer print.
    # You can create mutually_exclusive_groups: options that you can only
    #    select one OR the other.

    # Mandatory args:
    p.add_argument('filename',
                   help="Image filename to be loaded. Image should be a nifti "
                        "file.")
    p.add_argument('mandatory_float', type=float,
                   help='You **must** send a float as argument.')

    # Optional args:
    p.add_argument('--optional_float',
                   metavar='f', type=float, default=0.001,
                   help='You *may* send a float here. If you do not use \n'
                        'this arg, default value will be: [%(default)s]')
    p.add_argument('--optional_int',  metavar='v', type=int,
                   help='Optional arg with no default. Expecting integer.')
    p.add_argument('--use_option_Y', action='store_true',
                   help="To use option Y in script, type --use_option_Y.\n"
                        "  (no additional value; not --use_option_Y True)!\n"
                        "To NOT use option Y, simply write nothing.")

    group1 = p.add_argument_group(title='Options concerning XXX')
    group1.add_argument('--group_arg1',
                        help="Group arg1.")
    group1.add_argument('--group_arg2',
                        help="Group arg2")

    sub_group1 = group1.add_mutually_exclusive_group()
    sub_group1.add_argument('--option1_OR_2', action='store_true',
                            help="This option CANNOT be chosen together with "
                                 "option_2_OR_1")
    sub_group1.add_argument('--option2_OR_1', action='store_true',
                            help="This option CANNOT be chosen together with "
                                 "option_1_OR_2")

    return p


def main():
    parser = _build_arg_parser()
    args = parser.parse_args()

    # If you want, you may explore logger rather than print!
    print("****\n"
          "We used a argparser! \n"
          "Args that were received in the main method: \n\n"
          "{}\n\n"
          "****".format(args))

    # Accessing the args:
    print("\n")
    print("Accessing only the values that we want: ")
    print("Filename: ", args.filename)
    print("The mandatory float: ", args.mandatory_float)

    # Accessing options: notice that the -- is not there
    print("The --optional float with default 0.001: ", args.optional_float)

    print("The option with 'store_true' : ", args.use_option_Y)


if __name__ == "__main__":
    main()
