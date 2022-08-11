"""Image manager."""

from PIL import Image


def get_image(path: str):
    """Get image.

    :param path: path of image
    :return: image
    """
    return Image.open(path)


def put_image(image, path: str) -> None:
    """Put image.

    :param image: image (from PIL)
    :param path: path to save
    """
    image.save(path)
