# Day 11: Seating System
import numpy as np
import scipy.ndimage as spndi


EMPTY = '.'
SEAT = 'L'
FLOOR = 0
FREE = 1
OCCUPIED = 2


def parse_input(file_path):
    with open(file_path) as file:
        return np.array([[FREE if char == SEAT else FLOOR for char in line.strip()] for line in file])


def part_one(seats):
    busy_seats = run_until_no_change(seats,
                                     lambda seats: spndi.generic_filter(seats, kernel, 3, mode='constant', cval=0))
    print("Number of busy seats part one: {}".format(busy_seats))


def kernel(data):
    seat = data[4]
    busy_seats = np.count_nonzero(data == OCCUPIED)
    if seat == FREE and busy_seats == 0:
        return OCCUPIED
    elif seat == OCCUPIED and busy_seats > 4:
        return FREE
    else:
        return seat


def run_until_no_change(seats, updater):
    while True:
        updated_seats = updater(seats)
        if np.array_equal(updated_seats, seats):
            break
        seats = updated_seats
    return np.count_nonzero(seats == OCCUPIED)


def part_two(seats):
    busy_seats = run_until_no_change(seats, update_seats)
    print("Number of busy seats part two: {}".format(busy_seats))


def update_seats(seats):
    directions = [(0, -1), (-1, 0), (-1, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]
    updated_seats = seats.copy()
    for (x, y), seat in np.ndenumerate(seats):
        if seat == FLOOR:
            continue
        busy_seats = 0
        for direction in directions:
            first_seat = find_first_seat(seats, np.array([x, y]), np.array(direction))
            if first_seat == OCCUPIED:
                busy_seats += 1
        if seat == FREE and busy_seats == 0:
            updated_seats[(x, y)] = OCCUPIED
        if seat == OCCUPIED and busy_seats >= 5:
            updated_seats[(x, y)] = FREE
    return updated_seats


def find_first_seat(seats, position, direction):
    while True:
        position += direction
        if 0 <= position[0] < seats.shape[0] and 0 <= position[1] < seats.shape[1]:
            seat = seats[tuple(position)]
            if seat != FLOOR:
                return seat
        else:
            return FLOOR


def main():
    seats = parse_input('11.txt')
    part_one(seats.copy())
    part_two(seats.copy())


if __name__ == "__main__":
    main()
