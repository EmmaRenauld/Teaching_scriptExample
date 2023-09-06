

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def michelson(im):
    imax = np.max(image)
    imin = np.min(image)
    mich = (imax - imin) / (imax + imin)
    return mich


def RMS(im):
    meani = np.mean(im)
    nb_pix = np.prod(im.shape)
    return np.sqrt(((im - meani)**2).sum() / nb_pix)


def change_constrast(im, new_min, new_max):
    imin = np.min(im)
    imax = np.max(im)

    im = (im - imin) / (imax - imin)  # Between 0 and 1
    im = im * (new_max - new_min) + new_min
    return im


fname = 'photo1.jpg'
# fname = 'photo2.jpg'
# fname = 'photo3.png'
# fname = 'photo4.jpg'

image = Image.open(fname).convert("L")
image = np.asarray(image, dtype=float)


fig, axs = plt.subplots(2, 3)

image = change_constrast(image, 0, 255)
axs[0, 0].imshow(image, cmap='gray', vmin=0, vmax=255)
axs[1, 0].hist(image.flatten(), range=[0, 255], bins=50)
axs[0, 0].title.set_text("Michelson: {:.2f}\nRMS: {:.2f}"
                         .format(michelson(image), RMS(image)))

image = change_constrast(image, 40, 220)
axs[0, 1].imshow(image, cmap='gray', vmin=0, vmax=255)
axs[1, 1].hist(image.flatten(), range=[0, 255], bins=50)
axs[0, 1].title.set_text("Michelson: {:.2f}\nRMS: {:.2f}"
                         .format(michelson(image), RMS(image)))

image = change_constrast(image, 100, 180)
axs[0, 2].imshow(image, cmap='gray', vmin=0, vmax=255)
axs[1, 2].hist(image.flatten(), range=[0, 255], bins=50)
axs[0, 2].title.set_text("Michelson: {:.2f}\nRMS: {:.2f}"
                         .format(michelson(image), RMS(image)))
plt.show()
