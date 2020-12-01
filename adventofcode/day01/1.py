# Day 1: Report Repair
def part_one(expenses, target=2020):
    for i, x in enumerate(expenses):
        for y in expenses[i + 1:]:
            if x + y == target:
                product = x * y
    print("Product of 2 numbers that sum up to {}: {}".format(target, product))


def part_two(expenses, target=2020):
    for i, x in enumerate(expenses):
        for j, y in enumerate(expenses[i + 1:]):
            for z in expenses[j + 1:]:
                if x + y + z == target:
                    product = x * y * z
    print("Product of 3 numbers that sum up to {}: {}".format(target, product))


def main():
    with open('1.txt') as f:
        expenses = [int(line) for line in f]
    part_one(expenses.copy())
    part_two(expenses.copy())


if __name__ == "__main__":
    main()
