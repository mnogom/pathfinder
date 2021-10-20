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
usage: pathfinder [-h] [-s START START] [-g GOAL GOAL] path

Path finder

positional arguments:
  path                  Path of image

optional arguments:
  -h, --help            show this help message and exit
  -s START START, --start START START
                        start coordinates
  -g GOAL GOAL, --goal GOAL GOAL
                        goal coordinates
 
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