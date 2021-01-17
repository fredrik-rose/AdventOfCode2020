# Day 25: Combo Breaker


N = 20201227


def main():
    card, door = parse_input('25.txt')
    part_one(card, door)


def parse_input(file_path):
    with open(file_path) as file:
        card, door = [int(line) for line in file.readlines()]
        return card, door


def part_one(card, door):
    card_loop_size = find_loop_size(card)
    door_loop_size = find_loop_size(door)
    card_encryption_key = transform(door, card_loop_size)
    door_encryption_key = transform(card, door_loop_size)
    assert card_encryption_key == door_encryption_key
    print("Answer part one: {}".format(card_encryption_key))


def find_loop_size(target):
    subject = 7
    value = 1
    for i in range(1, 10000000):
        value = (value * subject) % N
        if value == target:
            return i
    assert False


def transform(subject, loop_size):
    return pow(subject, loop_size, N)


if __name__ == "__main__":
    main()
