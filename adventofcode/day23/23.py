# Day 23: Crab Cups


def main():
    cups = parse_input('23.txt')
    part_one(cups.copy())
    part_two(cups.copy())


def parse_input(file_path):
    with open(file_path) as file:
        return [int(d) for d in str(file.read().rstrip())]


def part_one(cups):
    result = play_game(cups, 100)
    digits = []
    current = result[1]
    while current != 1:
        digits.append(current)
        current = result[current]
    print("Answer part one: {}".format(''.join(str(i) for i in digits)))


def part_two(cups):
    cups = cups + list(range(len(cups) + 1, 1000001))
    result = play_game(cups, 10000000)
    a = result[1]
    b = result[a]
    print("Answer part two: {}".format(a * b))


def play_game(cups, n):
    min_val = min(cups)
    max_val = max(cups)
    current = cups[0]
    cups = {c: n for c, n in zip(cups, cups[1:] + cups[0:1])}
    for _ in range(n):
        a = cups[current]
        b = cups[a]
        c = cups[b]
        destination = current - 1
        while True:
            if destination < min_val:
                destination = max_val
            if destination not in (a, b, c):
                break
            destination -= 1
        cups[current] = cups[c]
        cups[c] = cups[destination]
        cups[destination] = a
        current = cups[current]
    return cups


if __name__ == "__main__":
    main()
