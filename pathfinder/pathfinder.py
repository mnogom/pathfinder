"""Pathfinder module."""

from pathfinder import node, layout, exceptions


def _get_euclidean_distance(node1, node2):

    x1 = node.get_x(node1)
    x2 = node.get_x(node2)
    y1 = node.get_y(node1)
    y2 = node.get_y(node2)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)


def _heuristic_cost_estimate(node1: dict, node2: dict):
    """Heuristic cost estimate
    Read more:
    * https://neerc.ifmo.ru/wiki/index.php?title=Алгоритм_A*

    :param node1: node 1
    :param node2: node 2
    :return: value of heuristic cost
    """

    return _get_euclidean_distance(node1, node2)


def _dist_between(node1, node2, outline):
    """Distance between nodes.

    :param node: node
    :param outline: outline
    :return: distance with weight
    """

    x = node2['x']
    y = node2['y']
    weight = 255 - outline[y][x]
    return weight * _get_euclidean_distance(node1, node2)


def get_path(start_x: int,
             start_y: int,
             goal_x: int,
             goal_y: int,
             plan: dict) -> list:
    """Get path. A* algorithm.
    Read more:
    * https://ru.wikibooks.org/wiki/Реализации_алгоритмов/Алгоритм_поиска_A*

    :param start_x: x coordinate of start
    :param start_y: y coordinate of start
    :param goal_x: x coordinate of goal
    :param goal_y: y coordinate of goal
    :param plan: layout
    :return: path as list of tuples.
    """

    reduce_factor = layout.get_reduce_factor(plan)
    start_x /= reduce_factor
    start_y /= reduce_factor
    goal_x /= reduce_factor
    goal_y /= reduce_factor

    start = node.create(start_x, start_y)
    goal = node.create(goal_x, goal_y)

    node.set_g(start, 0)
    node.set_h(start, _heuristic_cost_estimate(start, goal))
    node.set_f(start, node.get_g(start) + node.get_h(start))

    close_list = []
    open_list = [start]

    outline = layout.get_outline(plan)
    outline_bounds = layout.get_bounds(plan)

    while open_list:
        current = min(open_list, key=lambda x: node.get_f(x))

        if node.is_equal(current, goal):
            return _reconstruct_path(plan, current)

        open_list.remove(current)
        close_list.append(current)

        for neighbor in node.get_neighbors(current, **outline_bounds):
            if node.in_list(neighbor, close_list):
                continue

            temp_g = node.get_g(current) + _dist_between(current,
                                                         neighbor,
                                                         outline)

            if not node.in_list(neighbor, open_list):
                open_list.append(neighbor)
                temp_g_best = True
            else:
                if temp_g < node.get_g(current):
                    temp_g_best = True
                else:
                    temp_g_best = False

            if temp_g_best:
                node.set_parent(neighbor, current)
                node.set_g(neighbor, temp_g)
                node.set_h(neighbor,
                           _heuristic_cost_estimate(neighbor, goal))
                node.set_f(neighbor,
                           node.get_g(neighbor) + node.get_h(neighbor))

    raise exceptions.PFEmptyOpenList('Open list is empty. It is mean '
                                     'that path probably doesn\'t exists')


def _reconstruct_path(plan: dict, goal: dict) -> list:
    """Reconstruct path.

    :param plan: layout
    :param goal: last node
    :return: path as list of tuples.
    """

    current = goal
    reduce_factor = layout.get_reduce_factor(plan)

    path = []
    while current:
        current_x = node.get_x(current) * reduce_factor
        current_y = node.get_y(current) * reduce_factor
        path.append((current_x, current_y))
        current = node.get_parent(current)
    layout.draw_path(plan, path)
    return path
