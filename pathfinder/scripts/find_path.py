#!/usr/bin/env python3

"""Entry point."""

import os

from pathfinder import pathfinder, layout, cli, image_manager


def main() -> None:
    """Main function."""

    [image_path,
     start_x,
     start_y,
     goal_x,
     goal_y] = cli.parse_args()

    directory, name = os.path.split(image_path)
    plan = layout.read(image_path)

    pathfinder.get_path(start_x,
                        start_y,
                        goal_x,
                        goal_y,
                        plan)
    image_with_path = layout.get_image_path(plan)

    image_name, ext = os.path.splitext(name)
    image_name += f'-from-({start_x}, {start_y})-to-({goal_x}, {goal_y})'
    image_name += ext
    save_path = os.path.join(directory, image_name)

    image_manager.put_image(image_with_path, save_path)


if __name__ == '__main__':
    main()
