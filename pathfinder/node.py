"""Node module."""


def create(x: int, y: int, g=0, h=0, f=0, parent=None) -> dict:
    """Create node element.

    :param x: x-coordinate of node
    :param y: y-coordinate of node
    :param g: cost for past from start to node
    :param h: heuristic cost estimate from node to goal
    :param f: sum of g and h
    :param parent: parent of node
    :return: node
    """

    x = int(x)
    y = int(y)
    return {'x': x, 'y': y, 'g': g, 'h': h, 'f': f, 'parent': parent}


def get_h(node: dict):
    """Get h value of node.

    :param node: node
    :return: h-value
    """

    return node['h']


def set_h(node: dict, value) -> None:
    """Set h value for node.

    :param node: node
    :param value: value to set"""

    node['h'] = value


def get_g(node: dict):
    """Get g value of node.

    :param node: node
    :return: g-value
    """

    return node['g']


def set_g(node: dict, value) -> None:
    """Set g value for node.

    :param node: node
    :param value: value to set
    """

    node['g'] = value


def get_f(node: dict):
    """Get f value of node.

    :param node: node
    :return: f-value
    """

    return node['f']


def set_f(node: dict, value) -> None:
    """Set f value for node.

    :param node: node
    :param value: value to set
    """

    node['f'] = value


def get_parent(node: dict) -> dict:
    """Get parent of node.

    :param node: node
    :return: parent node
    """

    return node['parent']


def set_parent(node: dict, parent: dict) -> None:
    """Set parent for node.

    :param node: node
    :param parent: parent node
    """

    node['parent'] = parent


def get_x(node: dict) -> int:
    """Get x-coordinate of node.

    :param node: node
    :return: x coordinate
    """

    return node['x']


def get_y(node: dict) -> int:
    """Get y-coordinate of node.

    :param node: node
    :return: y coordinate
    """

    return node['y']


def is_equal(node1: dict, node2: dict) -> bool:
    """Compare two nodes.

    :param node1: node 1
    :param node2: node 2
    :return: True if nodes are equal. False otherwise
    """

    return get_x(node1) == get_x(node2) and get_y(node1) == get_y(node2)


def in_list(node: dict, array: list) -> bool:
    """Check if node in array of nodes.

    :param node: node
    :param array: list of nodes
    :return: True if node in list. False otherwise
    """

    cleaned_node = [get_x(node), get_y(node)]
    cleaned_array = [[get_x(el), get_y(el)] for el in array]
    return cleaned_node in cleaned_array


def get_neighbors(node: dict,
                  x_max: int,
                  y_max: int,
                  x_min=0,
                  y_min=0) -> list:
    """Get neighbors of node.

    :param node: current node
    :param x_max: max x-coordinate of area
    :param y_max: max y-coordinate of area
    :param x_min: min x-coordinate of area
    :param y_min: min y-coordinate of area
    :return: list of neighbors as nodes
    """

    x = get_x(node)
    y = get_y(node)

    neighbors = []

    if x - 1 >= x_min and y + 1 <= y_max:  # left - top
        neighbors.append(create(x - 1, y + 1))
    if y + 1 <= y_max:  # mid - top
        neighbors.append(create(x, y + 1))
    if x + 1 <= x_max and y + 1 <= x_max:  # right - top
        neighbors.append(create(x + 1, y + 1))
    if x - 1 >= x_min:  # left - mid
        neighbors.append(create(x - 1, y))
    if x + 1 <= x_max:  # right - mid
        neighbors.append(create(x + 1, y))
    if x - 1 >= x_min and y - 1 >= y_min:  # left - bottom
        neighbors.append(create(x - 1, y - 1))
    if y - 1 >= y_min:  # mid - bottom
        neighbors.append(create(x, y - 1))
    if x + 1 <= x_max and y - 1 >= y_min:  # right - bottom
        neighbors.append(create(x + 1, y - 1))

    return neighbors
