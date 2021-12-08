all:
	universe

universe: lists/universe.tsv
	src/create_universe.bash

