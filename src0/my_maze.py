import sys


class Maze():
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")


if (len(sys.argv)) != 2:
    sys.exit("Usage: python my_maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze:")
