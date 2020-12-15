# Day 15: Rambunctious Recitation


def parse_input(file_path):
    with open(file_path) as file:
        return [int(e) for e in file.readline().rstrip().split(',')]


def part_one(starting_numbers):
    number = play_memory(starting_numbers, 2020)
    print("2020th number spoken: {}".format(number))


def play_memory(starting_numbers, n_rounds):
    memory = {}
    for i, n in enumerate(starting_numbers):
        memory[n] = i
        last = n
    for i in range(len(starting_numbers), n_rounds):
        if last in memory:
            spoken = (i - 1) - memory[last]
        else:
            spoken = 0
        memory[last] = i - 1
        last = spoken
    return spoken


def part_two(starting_numbers):
    number = play_memory(starting_numbers, 30000000)
    print("30000000th number spoken: {}".format(number))


def main():
    starting_numbers = parse_input('15.txt')
    part_one(starting_numbers.copy())
    part_two(starting_numbers.copy())


if __name__ == "__main__":
    main()
