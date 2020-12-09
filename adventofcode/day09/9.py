# Day 9: Encoding Error
import itertools


def parse_input(file_path):
    with open(file_path) as file:
        return [int(line) for line in file.readlines()]


def part_one(numbers, preamble=25):
    for i in range(preamble, len(numbers)):
        n = numbers[i]
        if not contains_sum_of_two(numbers[i - preamble:i], n):
            break
    else:
        assert False  # Did not find any invalid number.
    print("First invalid number: {}".format(n))
    return n


def contains_sum_of_two(numbers, target):
    return any(x + y == target for x, y in itertools.combinations(numbers, 2))


def part_two(numbers, target):
    sum_range = find_range_that_sum_to_target(numbers, target)
    answer = min(sum_range) + max(sum_range)
    print("Sum of smallest and largest number in the encryption weakness: {}".format(answer))


def find_range_that_sum_to_target(numbers, target):
    for start in range(len(numbers)):
        for end, cum_sum in enumerate(cumsum(numbers[start:])):
            if cum_sum == target:
                return numbers[start:start + end + 1]
            elif cum_sum > target:
                break
    return None


def cumsum(numbers):
    acc_sum = 0
    for e in numbers:
        acc_sum += e
        yield acc_sum


def main():
    numbers = parse_input('9.txt')
    target = part_one(numbers.copy())
    part_two(numbers.copy(), target)


if __name__ == "__main__":
    main()
