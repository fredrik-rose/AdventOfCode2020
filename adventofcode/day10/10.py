# Day 10: Adapter Array
import numpy as np


def parse_input(file_path):
    with open(file_path) as file:
        return [int(line) for line in file.readlines()]


def part_one(numbers):
    diffs = np.diff(numbers)
    hist, _ = np.histogram(diffs, bins=[1, 2, 3, 4])
    answer = hist[0] * hist[2]
    print("The number of 1-jolt differences multiplied by the number of 3-jolt differences: {}".format(answer))


def part_two(numbers):
    # Dynamic programming.
    num_ways = [0] * len(numbers)
    num_ways[0] = 1
    for i, n in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            if numbers[j] - n <= 3:
                num_ways[j] += num_ways[i]
    print("Total numbers of arrangements: {}".format(num_ways[-1]))


def main():
    numbers = parse_input('10.txt')
    numbers.append(0)
    numbers.append(max(numbers) + 3)
    numbers.sort()
    part_one(numbers.copy())
    part_two(numbers.copy())


if __name__ == "__main__":
    main()
