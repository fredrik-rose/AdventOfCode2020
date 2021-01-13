# Day 20: Jurassic Jigsaw
import collections as coll
import functools as ft
import math
import operator as op
import re

import numpy as np
import scipy.ndimage as ndimage


def main():
    tiles = parse_input('20.txt')
    edges = get_edges(tiles)
    graph = create_graph(edges)
    part_one(graph)
    sea_monster = parse_input("sea_monster.txt")[0]
    part_two(tiles, graph, sea_monster)


def parse_input(file_path):
    with open(file_path) as file:
        return dict(parse_tile(tile) for tile in file.read().rstrip().split('\n\n'))


def parse_tile(text):
    lines = text.split('\n')
    tile_id = int(re.search(r'\d+', lines[0]).group(0))
    tile = np.array([[1 if char == '#' else 0 for char in line.strip()] for line in lines[1:]])
    return (tile_id, tile)


def get_edges(tiles):
    edges = coll.defaultdict(list)
    for tile_id, tile in tiles.items():
        tile_edges = get_tile_edges(tile)
        for edge in tile_edges:
            edges[edge].append(tile_id)
    return edges


def get_tile_edges(tile):
    top = tile[0, :]
    bottom = tile[-1, :]
    left = tile[:, 0]
    right = tile[:, -1]
    return [get_edge_value(edge) for edge in (top, right, bottom, left)]


def get_edge_value(bin_list):
    a = to_bin(bin_list)
    b = to_bin(bin_list[::-1])
    return min(a, b)


def to_bin(bin_list):
    return int(''.join(map(str, bin_list)), 2)


def create_graph(edges):
    graph = coll.defaultdict(dict)
    for edge, tile_ids in edges.items():
        number_of_tiles_connected_to_edge = len(tile_ids)
        if number_of_tiles_connected_to_edge == 2:
            a, b = tile_ids
            graph[a][edge] = b
            graph[b][edge] = a
        else:
            assert number_of_tiles_connected_to_edge == 1
            a = tile_ids[0]
            graph[a][edge] = None
    return graph


def part_one(graph):
    corners = find_corner_tiles(graph)
    conrer_product = ft.reduce(op.mul, corners, 1)
    print("Part one: {}".format(conrer_product))


def find_corner_tiles(graph):
    corners = []
    for tile_id, connections in graph.items():
        if len([tile for tile in connections.values() if tile is None]) == 2:
            corners.append(tile_id)
    return corners


def part_two(tiles, graph, sea_monster):
    board = orientate_tiles(tiles, graph)
    image = stitch_image(tiles, board)
    number_of_sea_monsters = find_sea_monsters(image, sea_monster)
    sea_monster_size = np.sum(sea_monster)
    answer = np.sum(image == 1) - (sea_monster_size * number_of_sea_monsters)
    print("Part two: {}".format(answer))


def orientate_tiles(tiles, graph):
    size = int(math.sqrt(len(tiles)))
    corners = find_corner_tiles(graph)
    node = corners[0]
    board = create_empty_board(size)
    for y in range(size):
        start = node
        for x in range(size):
            board[(x, y)] = node
            tiles[node] = find_valid_orientation(node, tiles, graph, board, x, y)
            edges = get_tile_edges(tiles[node])
            node = graph[node][edges[1]]
        edges = get_tile_edges(tiles[start])
        node = graph[start][edges[2]]
    return board


def create_empty_board(size):
    board = {}
    for y in range(size):
        for x in range(size):
            board[(x, y)] = None
    return board


def find_valid_orientation(tile_id, tiles, graph, board, x, y):
    rule = get_rule(tiles, board, x, y)
    for orientation in orientate(tiles[tile_id]):
        if match_rule(orientation, tile_id, graph, rule):
            return orientation
    assert False


def get_rule(tiles, board, x, y):
    rule = [None, None, None, None]
    for i, d in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
        pos = (x + d[0], y + d[1])
        if pos not in board:
            rule[i] = -1
        elif board[pos] is None:
            rule[i] = None
        else:
            edges = get_tile_edges(tiles[board[pos]])
            rule[i] = edges[(i + 2) % 4]
    return rule


def orientate(tile):
    for _ in range(4):
        yield tile
        yield np.flip(tile, axis=1)
        yield np.flip(tile, axis=0)
        tile = np.rot90(tile)


def match_rule(tile, tile_id, graph, rules):
    edges = get_tile_edges(tile)
    for edge, rule in zip(edges, rules):
        if rule == -1:
            if graph[tile_id][edge] is not None:
                return False
        elif rule is None:
            continue
        else:
            if edge != rule:
                return False
    return True


def stitch_image(tiles, board):
    assert len(tiles) == len(board)
    size = int(math.sqrt(len(tiles)))
    col = []
    for y in range(size):
        row = []
        for x in range(size):
            tile_id = board[(x, y)]
            tile = tiles[tile_id]
            row.append(tile[1:-1, 1:-1])  # Remove border.
        col.append(np.hstack(row))
    image = np.vstack(col)
    return image


def find_sea_monsters(image, sea_monster_pattern):
    for orientation in orientate(image):
        number_of_sea_monsters = count_sea_monsters(orientation, sea_monster_pattern)
        if number_of_sea_monsters > 0:
            return number_of_sea_monsters


def count_sea_monsters(image, sea_monster_pattern):
    sea_monsters = ndimage.generic_filter(image,
                                          np.all,
                                          footprint=sea_monster_pattern,
                                          mode='constant',
                                          cval=0)
    number_of_sea_monsters = np.sum(sea_monsters)
    return number_of_sea_monsters


if __name__ == "__main__":
    main()
