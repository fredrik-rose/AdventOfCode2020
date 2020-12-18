# Day 18: Operation Order
import re


class MyIntOne(int):
    def __add__(self, x):
        return MyIntOne(int(self) + int(x))

    def __sub__(self, x):
        return MyIntOne(int(self) * int(x))


class MyIntTwo(int):
    def __mul__(self, x):
        return MyIntTwo(int(self) * int(x))

    def __pow__(self, x):
        return MyIntTwo(int(self) + int(x))


def main():
    expressions = parse_input('18.txt')
    part_one(expressions.copy())
    part_two(expressions.copy())


def parse_input(file_path):
    with open(file_path) as file:
        return [line.rstrip() for line in file.readlines()]


def part_one(expressions):
    answer = hack(expressions, 'MyIntOne', ('*', '-'))
    print("Answer part one: {}".format(answer))


def part_two(expressions):
    answer = hack(expressions, 'MyIntTwo', ('+', '**'))
    print("Answer part two: {}".format(answer))


def hack(expressions, my_class, replace):
    answer = 0
    for exp in expressions:
        exp = exp.replace(*replace)
        exp = re.sub(r'(\d+)', r'{}(\1)'.format(my_class), exp)
        answer += eval(exp)
    return answer


if __name__ == "__main__":
    main()
