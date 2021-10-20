# Path finder

---
[![Maintainability](https://api.codeclimate.com/v1/badges/7a6eeed13e700478f9eb/maintainability)](https://codeclimate.com/github/mnogom/pathfinder/maintainability)
[![python-ci](https://github.com/mnogom/pathfinder/actions/workflows/python-ci.yml/badge.svg)](https://github.com/mnogom/pathfinder/actions/workflows/python-ci.yml)


---
### Installation
```commandline
pip3 install --upgrade git+https://github.com/mnogom/pathfinder.git
```

---
### Usage
1. From command line:
```commandline
usage: pathfinder [-h] [-s START START] [-g GOAL GOAL] [-r REDUCE_FACTOR]
                  [-w WHITE_VALUE]
                  path

Path finder

positional arguments:
  path                  Path of image

optional arguments:
  -h, --help            show this help message and exit
  -s START START, --start START START
                        start coordinates
  -g GOAL GOAL, --goal GOAL GOAL
                        goal coordinates
  -r REDUCE_FACTOR, --reduce-factor REDUCE_FACTOR
                        reduce factor
  -w WHITE_VALUE, --white-value WHITE_VALUE
                        white value
```
2. From Python
```python
import pathfinder

plan = pathfinder.read('path/to/file.jpg', reduce_factor=5, white_value=240)
pathfinder.get_path(start_x, start_y, goal_x, goal_y, plan)
output_image = pathfinder.get_image_path(plan)
pathfinder.put_image(output_image, 'path/to/pathed_file.jpg')
```

### Features
1. Set up white value for outline image
2. Reduce image for performance improvement

---
### Examples
1. Input image
![Input image](https://github.com/mnogom/pathfinder/blob/main/examples/1/plan.jpg?raw=true "Optional Title")
```commandline
poetry run pathfinder examples/1/plan.jpg -s 420 380 -g 520 600 -r 5 -w 240
```
![Output image](https://github.com/mnogom/pathfinder/blob/main/examples/1/plan-from-\(420, 380\)-to-\(520, 600\).jpg?raw=true "Optional Title")