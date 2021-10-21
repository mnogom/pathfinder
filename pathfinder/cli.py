"""Command line interface."""

import argparse


def parse_args():
    """Parse input parameters.

    :return: path, start_x, start_y, goal_x, goal_y, reduce_factor, white_value
    """

    parser = argparse.ArgumentParser(description='Path finder')
    parser.add_argument(dest='path', help='Path of image')
    parser.add_argument('-s', '--start',
                        nargs=2,
                        metavar=('X', 'Y'),
                        help='start coordinates')
    parser.add_argument('-g', '--goal',
                        nargs=2,
                        metavar=('X', 'Y'),
                        help='goal coordinates')
    parser.add_argument('-r', '--reduce-factor',
                        help='reduce factor',
                        default=1)
    parser.add_argument('-w', '--white-value',
                        help='white value',
                        default=None)
    args = parser.parse_args()

    path = args.path
    start_x = int(args.start[0])
    start_y = int(args.start[1])
    goal_x = int(args.goal[0])
    goal_y = int(args.goal[1])
    reduce_factor = int(args.reduce_factor)
    white_value = None
    if args.white_value:
        white_value = int(args.white_value)

    return path, start_x, start_y, goal_x, goal_y, reduce_factor, white_value
