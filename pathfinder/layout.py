"""Plan module."""

from PIL import ImageDraw
import numpy as np

from pathfinder import image_manager

GRAYSCALEMOD = 'L'
WHITE = 255
BLACK = 0


def read(path: str, reduce_factor=5, white_value=240) -> dict:
    """Read layout from path.

    :param path: path for image plan
    :param reduce_factor: reduce factor for outline
    :param white_value: white value for outline
    :return: layout
    """

    image = image_manager.get_image(path)

    outline = image.copy()
    outline = outline.reduce(reduce_factor)
    outline = outline.convert(GRAYSCALEMOD)
    outline = np.array(outline)
    y_min, x_min = (0, 0)
    y_max, x_max = [c_max - 1 for c_max in outline.shape]

    return {'image': image,
            'image_path': None,
            'outline': {
                'data': outline,
                'reduce_factor': reduce_factor,
                'bounds': {
                    'x_min': x_min,
                    'y_min': y_min,
                    'x_max': x_max,
                    'y_max': y_max
                }
            }}


def draw_path(layout: dict, path: list) -> None:
    """Draw path on layout.

    :param layout: layout
    :param path: list of tuples with coordinates of path
    """

    image_path = get_image(layout).copy()
    draw = ImageDraw.Draw(image_path)
    draw.line(path, fill=(255, 0, 0), width=5)
    set_image_path(layout, image_path)


def get_image(layout: dict):
    """Get image of layout.

    :param layout: layout
    :return: image of layout
    """

    return layout['image']


def get_image_path(layout: dict):
    """Get image path of layout.

    :param layout: layout
    :return: image with path
    """

    return layout['image_path']


def set_image_path(layout: dict, value) -> None:
    """Set image path of layout.

    :param layout: layout
    :param value: value to set
    """

    layout['image_path'] = value


def get_outline(layout: dict):
    """Get outline data of layout.

    :param layout: layout
    :return: outline
    """

    return layout['outline']['data']


def get_bounds(layout: dict) -> dict:
    """Get bounds of layout outline.

    :param layout: layout
    :return: dict of bounds
    """

    return layout['outline']['bounds']


def get_reduce_factor(layout: dict) -> int:
    """Get reduce factor of layout outline.

    :param layout: layout
    :return: reduce factor
    """

    return layout['outline']['reduce_factor']
