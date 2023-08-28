#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Please add comments and docstring and type hints as much as possible to help
me understand your intention behind each step even when you mess up your code!
"""


import numpy as np

from my_functions.a_module_with_comments import (
    load_3d_image, process_medical_image, save_result)


def get_arguments():
    # Creating "hardcoded" variables for now.
    # INTERDICTION FOR YOUR HOMEWORK. WE WILL SEE A BETTER TECHNIQUE.
    loading_path = 'my/path/my_file'
    saving_path = 'my/path/my_file2'
    return loading_path, saving_path


def main():
    loading_path, saving_path = get_arguments()

    # Step 1. Load some data
    print("Loading data")
    image = load_3d_image(loading_path)

    # Step 2. Use the data.
    modified_image = process_medical_image(image)

    # Step 3. Show some result
    print("Mean of resulting data is: {}".format(np.mean(modified_image)))

    # Step 4. Save data.
    print("Sucessful script. Final data will be saved in {}"
          .format(saving_path))
    save_result(modified_image, saving_path)


if __name__ == "__main__":
    main()
