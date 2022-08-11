"""Plan module."""

from PIL import ImageDraw
import numpy as np

GRAYSCALE_MOD = 'L'
WHITE = 255
BLACK = 0


def _xor(value1, value2):
    return bool(value1) ^ bool(value2)


def _create_outline(image, reduce_factor, white_value):
    outline = image.copy()
    outline = outline.reduce(reduce_factor)
    outline = outline.convert(GRAYSCALE_MOD)
    if white_value:
        outline = outline.point(
            lambda pix: WHITE if pix >= white_value else BLACK,
            GRAYSCALE_MOD)
    return np.array(outline)


def _get_outline_x_min():
    return 0


def _get_outline_x_max(outline):
    return outline.shape[1] - 1


def _get_outline_y_min():
    return 0


def _get_outline_y_max(outline):
    return outline.shape[0] - 1


def create_layout(image,
                  outline=None,
                  reduce_factor=1,
                  white_value=255,
                  image_with_path=None):
    if outline is None:
        _outline = _create_outline(image, reduce_factor, white_value)
    else:
        _outline = outline

    return {
        'image': image,
        'image_with_path': image_with_path,
        'outline': _outline,
        'reduce_factor': reduce_factor,
        'white_value': white_value
    }


def draw_path(layout: dict, path: list) -> None:
    """Draw path on layout.

    :param layout: layout
    :param path: list of tuples with coordinates of path
    """
    image_path = get_image(layout).copy()
    draw = ImageDraw.Draw(image_path)
    draw.line(path, fill=(255, 0, 0), width=5)
    return image_path


def get_image(layout: dict):
    """Get image of layout.

    :param layout: layout
    :return: image of layout
    """
    return layout['image']


def get_image_with_path(layout: dict):
    """Get image path of layout.

    :param layout: layout
    :return: image with path
    """
    return layout['image_with_path']


def set_image_path(layout: dict, value) -> dict:
    """Set image path of layout.

    :param layout: layout
    :param value: value to set
    """
    return create_layout(
        get_image(layout),
        get_outline(layout),
        get_reduce_factor(layout),
        get_white_value(layout),
        value
    )


def get_outline(layout: dict):
    """Get outline data of layout.

    :param layout: layout
    :return: outline
    """
    return layout['outline']


def get_bounds(layout: dict) -> dict:
    """Get bounds of layout outline.

    :param layout: layout
    :return: dict of bounds
    """
    return {
        "x_min": _get_outline_x_min(),
        "x_max": _get_outline_x_max(get_outline(layout)),
        "y_min": _get_outline_y_min(),
        "y_max": _get_outline_y_max(get_outline(layout)),
    }


def get_reduce_factor(layout: dict) -> int:
    """Get reduce factor of layout outline.

    :param layout: layout
    :return: reduce factor
    """
    return layout['reduce_factor']


def get_white_value(layout):
    return layout['white_value']
