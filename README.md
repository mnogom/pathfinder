# Path Finder
_Console utility to find path on RGB image_

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
3. Working with only RGB image

---
### Examples
1. Input image `examples/1/plan.jpg`
![Input image](https://github.com/mnogom/pathfinder/blob/main/examples/1/plan.jpg?raw=true)
```commandline
pathfinder examples/1/plan.jpg -s 420 380 -g 250 40 -r 5 -w 240
```
![Output image](https://github.com/mnogom/pathfinder/blob/main/examples/1/plan-from-420_380-to-250_40.jpg?raw=true)
```commandline
pathfinder examples/1/plan.jpg -s 420 380 -g 520 600 -r 5 -w 240
```
![Output image](https://github.com/mnogom/pathfinder/blob/main/examples/1/plan-from-420_380-to-520_600.jpg?raw=true)
```commandline
pathfinder examples/1/plan.jpg -s 420 380 -g 45 350 -r 5 -w 240
```
![Output image](https://github.com/mnogom/pathfinder/blob/main/examples/1/plan-from-420_380-to-45_350.jpg?raw=true)

2. Input image `examples/2/maze.jpg`
![Input image](https://github.com/mnogom/pathfinder/blob/main/examples/2/maze.jpg?raw=true)
```commandline
pathfinder examples/2/maze.jpg -s 20 300 -g 620 300 -r 8
```
![Output image](https://github.com/mnogom/pathfinder/blob/main/examples/2/maze-from-20_300-to-620_300.jpg?raw=true)
