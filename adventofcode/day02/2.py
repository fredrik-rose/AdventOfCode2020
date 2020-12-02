# Day 2: Password Philosophy
import re


def part_one(passwords):
    valid_passwords = count_valid_password(passwords, verify_password_part_one)
    print("There are {} valid password for part one.".format(valid_passwords))


def count_valid_password(passwords, verifier):
    return sum(verifier(parse_password(p)) for p in passwords)


def parse_password(password):
    pattern = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
    match = pattern.match(password)
    return {'min': int(match.group(1)),
            'max': int(match.group(2)),
            'char': match.group(3),
            'password': match.group(4)}


def verify_password_part_one(password):
    return password['min'] <= password['password'].count(password['char']) <= password['max']


def part_two(passwords):
    valid_passwords = count_valid_password(passwords, verify_password_part_two)
    print("There are {} valid password for part two.".format(valid_passwords))


def verify_password_part_two(password):
    first_position_contains_char = password['password'][password['min'] - 1] == password['char']
    second_position_contains_char = password['password'][password['max'] - 1] == password['char']
    return first_position_contains_char != second_position_contains_char  # XOR.


def main():
    with open('2.txt') as f:
        passwords = [line.rstrip() for line in f.readlines()]
    part_one(passwords.copy())
    part_two(passwords.copy())


if __name__ == "__main__":
    main()
