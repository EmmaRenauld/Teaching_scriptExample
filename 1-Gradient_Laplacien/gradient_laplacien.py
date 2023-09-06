import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage


def show_function_first_and_second_derivative():
    # ===============
    # Ce qu'est une derivee
    x = np.linspace(0, 50, 100)
    f = np.sin(x)
    f[17:28] = 1
    f[28:60] = np.sin(x[28:60] / 5) + 0.72
    f[60:70] = 0.4
    f[70:] = 0
    f += 1  # putting min to 0
    f *= 255 / 2  # putting max to 255

    dx = x[1] - x[0]
    fig, ax = plt.subplots(4, 1, figsize=(15, 7))
    ax[1].plot(x, f)
    df = np.gradient(f, dx)
    ax[2].plot(x, df)
    ddf = np.gradient(df, dx)
    ax[3].plot(x, ddf)

    my_cmap = plt.cm.get_cmap('gray')
    colors = my_cmap(f / 255)
    ax[0].bar(x, f, width=0.5, color=colors)
    plt.show()


def _get_min_max(gradients, abs_gradients):
    mmin = 1000
    mmax = 0
    for i in range(len(gradients)):
        if abs_gradients:
            gradients[i] = np.abs(gradients[i])

        im = gradients[i]
        im_min = np.min(im)
        if im_min < mmin:
            mmin = im_min

        im_max = np.max(im)
        if im_max > mmax:
            mmax = im_max

    return mmin, mmax, gradients


def show_image_first_and_second_gradient(f, abs_gradients):
    # ===============
    # Gradient et Laplacien d'une image

    # First derivatives x:
    fd_x = ndimage.convolve(f, [[0, 0, 0],
                                [0, -1, 1],
                                [0, 0, 0]])
    fd_y = ndimage.convolve(f, [[0, 0, 0],
                                [0, -1, 0],
                                [0, 1, 0]])
    bd_x = ndimage.convolve(f, [[0, 0, 0],
                                [-1, 1, 0],
                                [0, 0, 0]])
    bd_y = ndimage.convolve(f, [[0, -1, 0],
                                [0, 1, 0],
                                [0, 0, 0]])
    cd_x = ndimage.convolve(f, [[0, 0, 0],
                                [-0.5, 0, 0.5],
                                [0, 0, 0]])
    cd_y = ndimage.convolve(f, [[0, -0.5, 0],
                                [0, 0, 0],
                                [0, 0.5, 0]])
    gradients = [fd_x, fd_y, bd_x, bd_y, cd_x, cd_y]

    mmin, mmax, gradients = _get_min_max(gradients, abs_gradients)

    fig, ax = plt.subplots(2, 3, figsize=(15, 7))
    ax[0, 0].imshow(gradients[0], cmap='gray', vmin=mmin, vmax=mmax)
    ax[0, 0].set_title('Forward diff x')
    ax[0, 1].imshow(gradients[1], cmap='gray', vmin=mmin, vmax=mmax)
    ax[0, 1].set_title('Backward diff x')
    ax[0, 2].imshow(gradients[2], cmap='gray', vmin=mmin, vmax=mmax)
    ax[0, 2].set_title('Central diff x')
    ax[1, 0].imshow(gradients[3], cmap='gray', vmin=mmin, vmax=mmax)
    ax[1, 0].set_title('Forward diff y')
    ax[1, 1].imshow(gradients[4], cmap='gray', vmin=mmin, vmax=mmax)
    ax[1, 1].set_title('Backward diff y')
    im = ax[1, 2].imshow(gradients[5], cmap='gray', vmin=mmin, vmax=mmax)
    ax[1, 2].set_title('Central diff y')

    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)
    plt.show()

    # Second derivatives:
    cdd_x = ndimage.convolve(f, [[0, 0, 0],
                                 [1, -2, 1],
                                 [0, 0, 0]])
    cdd_y = ndimage.convolve(f, [[0, 1, 0],
                                 [0, -2, 0],
                                 [0, 1, 0]])
    laplacien = ndimage.convolve(f, [[0, 1, 0],
                                     [1, -4, 1],
                                     [0, 1, 0]])
    second_gradients = [cdd_x, cdd_y, laplacien]
    mmin2, mmax2, second_gradients = _get_min_max(second_gradients, abs_gradients)

    fig, ax = plt.subplots(2, 2, figsize=(15, 7))
    ax[0, 0].imshow(gradients[4], cmap='gray', vmin=mmin, vmax=mmax)
    ax[0, 0].set_title('Central difference x (order 1)')
    ax[0, 1].imshow(second_gradients[0], cmap='gray', vmin=mmin2, vmax=mmax2)
    ax[0, 1].set_title('Central difference x (order 2)')
    ax[1, 0].imshow(gradients[5], cmap='gray', vmin=mmin, vmax=mmax)
    ax[1, 0].set_title('Central difference y (order 1)')
    ax[1, 1].imshow(second_gradients[1], cmap='gray', vmin=mmin2, vmax=mmax2)
    ax[1, 1].set_title('Central difference y (order 2)')

    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)
    plt.show()

    fig, ax = plt.subplots(figsize=(15, 7))
    ax.imshow(second_gradients[2], cmap='gray', vmin=mmin, vmax=mmax)
    ax.set_title('Laplacien')
    plt.show()


def laplacien_edge_enhancement(f):
    laplacien = ndimage.convolve(f, [[0, 1, 0],
                                     [1, -4, 1],
                                     [0, 1, 0]])

    imin = np.min(f)
    imax = np.max(f)
    fig, ax = plt.subplots(1, 2, figsize=(15, 7))
    ax[0].imshow(f, cmap='gray', vmin=imin, vmax=imax)
    final = f - laplacien
    ax[1].imshow(final, cmap='gray', vmin=imin, vmax=imax)
    ax[1].set_title('Laplacian filter edge enhancement')
    plt.show()


def main():
    # show_function_first_and_second_derivative()

    img = plt.imread('sherbrooke-village-in-black-and-white-ken-morris.jpg')
    #img = plt.imread('Lena-Original-Image-512x512-pixels.png')

    # Converting from RGB
    rgb_weights = [0.2989, 0.5870, 0.1140]
    f = np.dot(img[..., :3], rgb_weights)

    # Showing raw img
    plt.imshow(f, cmap='gray')
    plt.show()

    show_image_first_and_second_gradient(f, abs_gradients=False)
    show_image_first_and_second_gradient(f, abs_gradients=True)

    laplacien_edge_enhancement(f)


if __name__ == '__main__':
    main()

