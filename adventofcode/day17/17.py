# Day 17: Conway Cubes
import numpy as np
import scipy.ndimage as spndi


INACTIVE = 0
ACTIVE = 1


def parse_input(file_path):
    with open(file_path) as file:
        return np.array([[ACTIVE if char == '#' else INACTIVE for char in line.strip()] for line in file])


def part_one(grid):
    num_actives = play_game_of_life(grid)
    print("Number of active cubes part one: {}".format(num_actives))


def play_game_of_life(grid, num_rounds=6):
    for _ in range(num_rounds):
        grid = np.pad(grid, 1, mode='constant', constant_values=INACTIVE)
        grid = spndi.generic_filter(grid, rules_kernel, 3, mode='constant', cval=INACTIVE)
    return np.count_nonzero(grid == ACTIVE)


def rules_kernel(data):
    element = data[len(data) // 2]
    num_actives = np.count_nonzero(data == ACTIVE)
    if element == ACTIVE and num_actives not in (3, 4):
        return INACTIVE
    if element == INACTIVE and num_actives == 3:
        return ACTIVE
    return element


def part_two(grid):
    num_actives = play_game_of_life(grid)
    print("Number of active cubes part two: {}".format(num_actives))


def main():
    grid = parse_input('17.txt')
    grid = np.expand_dims(grid, axis=0)
    part_one(grid.copy())
    grid = np.expand_dims(grid, axis=0)
    part_two(grid.copy())


if __name__ == "__main__":
    main()
