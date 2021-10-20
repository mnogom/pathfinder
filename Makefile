install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 pathfinder
