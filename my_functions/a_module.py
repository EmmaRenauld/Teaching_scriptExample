# -*- coding: utf-8 -*-
import numpy as np


def load_3d_image(a_path):
    print("Fake function. Pretend I am loading an image from path {}!"
          .format(a_path))

    image = np.zeros((4, 4, 4))
    return image


def process_medical_image(image):
    print("Fake function. Pretend I am doing some very scientific stuff "
          "to my image")
    image += 2
    return image


def save_result(image, saving_path):
    print("Fake function. Pretend I am save the image as a Nifti file "
          "at path {}".format(saving_path))

