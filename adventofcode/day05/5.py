# Day 5: Binary Boarding
import numpy as np


def parse_input(file_path):
    with open(file_path) as file:
        return [parse_boarding_pass(line) for line in file]


def parse_boarding_pass(boarding_pass):
    row = parse_binary_number(boarding_pass[:7], 'F', 'B')
    col = parse_binary_number(boarding_pass[7:], 'L', 'R')
    seat_id = (row * 8) + col
    return seat_id


def parse_binary_number(number_string, zero_char, one_char):
    return int(number_string[:7].replace(zero_char, '0').replace(one_char, '1'), 2)


def part_one(boarding_passes):
    max_seat_id = max(boarding_passes)
    print("The highest seat ID is {}".format(max_seat_id))


def part_two(boarding_passes):
    boarding_passes.sort()
    index_of_missing_seat = list(np.diff(boarding_passes)).index(2) + 1
    missing_seat_id = boarding_passes[0] + index_of_missing_seat
    print("ID of my seat is {}".format(missing_seat_id))


def main():
    boarding_passes = parse_input('5.txt')
    part_one(boarding_passes.copy())
    part_two(boarding_passes.copy())


if __name__ == "__main__":
    main()
