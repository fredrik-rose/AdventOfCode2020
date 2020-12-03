# Day 3: Toboggan Trajectory
import numpy as np


EMPTY = '.'
TREE = '#'


def parse_input(file_path):
    with open(file_path) as file:
        return np.array([[1 if char == TREE else 0 for char in line.strip()] for line in file])


def count_trees(tree_map, slopes):
    tree_product = 1
    for dx, dy in slopes:
        slope = dy / dx
        y = np.arange(0, tree_map.shape[0], dy)
        x = np.array([e % tree_map.shape[1] for e in y / slope], dtype=int)
        tree_product *= int(sum(tree_map[y, x]))
    return tree_product


def part_one(tree_map):
    slopes = [(3, 1)]
    num_trees = count_trees(tree_map, slopes)
    print("Encounter {} trees in part one.".format(num_trees))


def part_two(tree_map):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    num_trees = count_trees(tree_map, slopes)
    print("Encounter {} trees in part two.".format(num_trees))


def main():
    tree_map = parse_input('3.txt')
    part_one(tree_map.copy())
    part_two(tree_map.copy())


if __name__ == "__main__":
    main()
