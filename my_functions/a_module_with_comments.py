# -*- coding: utf-8 -*-
import numpy as np


def load_3d_image(a_path):
    """
    Loads a Nifti image from a given path.

    Parameters
    ----------
    a_path: str
        The path where the Nifti file is stored. Should have .nii or .nii.gz
        extension.

    Returns
    -------
    image: np.ndarray
        The array containing the image.
    """
    print("Fake function. Pretend I am loading an image from path {}!"
          .format(a_path))

    image = np.zeros((4, 4, 4))
    return image


def process_medical_image(image):
    """
    Modifies the images by doing something something something.

    Parameters
    ----------
    image: np.ndarray
        The image to be modified.

    Returns
    -------
    image: np.ndarray
        The modified image.
    """
    print("Fake function. Pretend I am doing some very scientific stuff "
          "to my image")
    image += 2
    return image


def save_result(image, saving_path):
    """
    Saves the image in a chosen path on disk in a Nifti format.

    Parameters
    ----------
    image: np.ndarray
        The image to be saved
    saving_path: str
        The path to save the image. Should have .nii or .nii.gz
        extension.

    """
    print("Fake function. Pretend I am save the image as a Nifti file "
          "at path {}".format(saving_path))

