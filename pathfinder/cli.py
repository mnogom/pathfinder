"""Command line interface."""

import argparse


def parse_args():
    """Parse input parameters.

    :return: path, start_x, start_y, goal_x, goal_y
    """

    parser = argparse.ArgumentParser(description='Path finder')
    parser.add_argument(dest='path', help='Path of image')
    parser.add_argument('-s', '--start',
                        nargs=2,
                        help='start coordinates')
    parser.add_argument('-g', '--goal',
                        nargs=2,
                        help='goal coordinates')
    args = parser.parse_args()

    path = args.path
    start_x = int(args.start[0])
    start_y = int(args.start[1])
    goal_x = int(args.goal[0])
    goal_y = int(args.goal[1])

    return path, start_x, start_y, goal_x, goal_y
