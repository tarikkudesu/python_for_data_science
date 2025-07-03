import cv2
import numpy as np


def ft_load(path: str) -> np.array:
    """

    loads an image, prints its format,
    and its pixels content in RGB format.

    """
    img = cv2.imread(path, 1)
    print(f"The shape of image is: {img.shape}")
    return img
