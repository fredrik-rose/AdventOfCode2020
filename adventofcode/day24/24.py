# Day 24: Lobby Layout
import re


# (-2, 2)       ( 0, 2)       ( 2, 2)
#        (-1, 1)       ( 1, 1)
# (-2, 0)       ( 0, 0)       ( 2, 0)
#        (-1,-1)       ( 1,-1)
# (-2,-2)       ( 0,-2)       ( 2,-2)
HEX_COORDINATE_SYSTEM = {'e': 2+0j,
                         'se': 1-1j,
                         'sw': -1-1j,
                         'w': -2+0j,
                         'nw': -1+1j,
                         'ne': 1+1j}


def main():
    instructions = parse_input('24.txt')
    tiles = part_one(instructions)
    part_two(tiles)


def parse_input(file_path):
    with open(file_path) as file:
        return [re.findall(r'(e|se|sw|w|nw|ne)', line) for line in file.readlines()]


def part_one(instructions):
    tiles = set()
    for instruction in instructions:
        position = 0+0j
        for direction in instruction:
            position += HEX_COORDINATE_SYSTEM[direction]
        if position in tiles:
            tiles.remove(position)
        else:
            tiles.add(position)
    print("Answer part one: {}".format(len(tiles)))
    return tiles


def part_two(tiles):
    for _ in range(100):
        tiles_to_check = set(tiles).union(*(neighbor_positions(position) for position in tiles))
        new_tiles = set()
        for position in tiles_to_check:
            black_neighbors = sum(1 for neighbor in neighbor_positions(position) if neighbor in tiles)
            if position in tiles and (black_neighbors == 1 or black_neighbors == 2):
                # Black remains black.
                new_tiles.add(position)
            elif position not in tiles and black_neighbors == 2:
                # White turns black.
                new_tiles.add(position)
        tiles = new_tiles
    print("Answer part two: {}".format(len(tiles)))


def neighbor_positions(position):
    for offset in HEX_COORDINATE_SYSTEM.values():
        yield position + offset


if __name__ == "__main__":
    main()
