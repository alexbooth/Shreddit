import sys
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def load_image(img_path):
    """
    Parameters
    ----------
    img_path - path to the image

    Returns
    ----------
    numpy array_like of the image
    """    
    return np.array(Image.open(img_path))

def shred_rows(img, width=1):
    """
    Parameters
    ----------
    img - array_like image
    width - the width in pixels of each "slice"

    Returns
    ----------
    two downsampled array_like images with even and odd rows respectively
    """
    if img.shape[0] < 2 * width:
        print("Cannot shred rows any further with the specified thickness.")
        print("Exiting.")
        sys.exit()
    odd_cols  = img[np.mod(np.arange(img.shape[0]),2*width) <  width, :]
    even_cols = img[np.mod(np.arange(img.shape[0]),2*width) >= width, :]
    return odd_cols, even_cols

def shred_cols(img, width=1):
    """
    Parameters
    ----------
    img - array_like image
    width - the width in pixels of each "slice"

    Returns
    ----------
    two downsampled array_like images with even and odd columns respectively
    """
    if img.shape[1] < 2 * width:
        print("Cannot shred columns any further with the specified thickness.")
        print("Exiting.")
        sys.exit()
    odd_cols  = img[:, np.mod(np.arange(img.shape[1]),2*width) <  width]
    even_cols = img[:, np.mod(np.arange(img.shape[1]),2*width) >= width]
    return odd_cols, even_cols

def merge(img1, img2, axis):
    """
    Parameters
    ----------
    img1 - array_like, n * m image
    img2 - array_like, n * m image
    axis - 0 for vertical merge after row shred
           1 for horizontal merge after column shred

    Returns
    ----------
    array_like representation of combined image
    """
    return np.concatenate((img1, img2), axis=axis)

def run():
    # Hi Reddit, play with these 3 lines
    img = load_image("Lenna.png")
    thickness = 5
    iterations = 1000
    ####################################

    output = img.copy()
    for i in range(iterations):
        # Shred columns then horizontal merge results
        img1, img2 = shred_cols(output, width=thickness)
        output = merge(img1, img2, 1)

        # Shred rows then vertical merge results
        img1, img2 = shred_rows(output, width=thickness)
        output = merge(img1, img2, 0)

    plt.imshow(output)
    plt.show()

if __name__ == "__main__":
    run()
