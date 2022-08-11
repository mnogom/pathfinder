#!/usr/bin/env python3

"""Entry point."""

import os

from pathfinder import (parse_args,
                        get_image,
                        create_layout,
                        get_path,
                        get_image_with_path,
                        put_image)


def main() -> None:
    """Main function."""

    [image_path,
     start_x,
     start_y,
     goal_x,
     goal_y,
     reduce_factor,
     white_value] = parse_args()

    image = get_image(image_path)
    plan = create_layout(image,
                         reduce_factor=reduce_factor,
                         white_value=white_value)

    plan = get_path(start_x,
                    start_y,
                    goal_x,
                    goal_y,
                    plan)
    image_with_path = get_image_with_path(plan)

    directory, name = os.path.split(image_path)
    image_name, ext = os.path.splitext(name)
    image_name += f'-from-{start_x}_{start_y}-to-{goal_x}_{goal_y}'
    image_name += ext
    save_path = os.path.join(directory, image_name)

    put_image(image_with_path, save_path)


if __name__ == '__main__':
    main()
