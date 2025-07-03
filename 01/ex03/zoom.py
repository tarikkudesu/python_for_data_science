from load_image import ft_load
import numpy as np
import cv2


def display(img):
    """

    Displays an image on the screen

    """
    assert type(img) is np.ndarray
    assert len(img.shape) >= 2
    height = img.shape[0]
    width = img.shape[1]
    assert height > 400 and width > 400
    window_name = "python for data science"
    y, x = 0, 0
    print(img)
    zoomed = img[:400, :400]
    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)
    while True:
        cv2.imshow(window_name, img[y:400 + y, x: x + 400])
        key = cv2.waitKey(1000)
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break
        if key == 27:
            break
        if key == 81:
            x -= 10
        elif key == 83:
            x += 10
        elif key == 82:
            y -= 10
        elif key == 84:
            y += 10
        if x > width - 400:
            x = width - 400
        if x < 0:
            x = 0
        if y > height - 400:
            y = height - 400
        if y < 0:
            y = 0
    cv2.destroyAllWindows()


def main():
    """Entrypoint"""
    try:
        cv2.setLogLevel(0)
        display(ft_load("animal.jpeg"))
    except (AssertionError, TypeError, AttributeError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
