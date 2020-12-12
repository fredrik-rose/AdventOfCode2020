# Day 12: Rain Risk
import math


def parse_input(file_path):
    with open(file_path) as file:
        return [parse_instruction(instruction.strip()) for instruction in file.readlines()]


def parse_instruction(instruction):
    operation, operand = instruction[0], int(instruction[1:])
    return (operation, operand)


def get_actions_from_instructions(instructions):
    translator = {'N': lambda x: ('Translation', (0, x)),
                  'S': lambda x: ('Translation', (0, -x)),
                  'E': lambda x: ('Translation', (x, 0)),
                  'W': lambda x: ('Translation', (-x, 0)),
                  'L': lambda x: ('Rotation', x),
                  'R': lambda x: ('Rotation', -x),
                  'F': lambda x: ('Forward', x)}
    actions = [translator[operation](operand) for operation, operand in instructions]
    return actions


def part_one(actions):
    angle = 0
    x, y = 0, 0
    for action, delta in actions:
        if action == 'Translation':
            x += delta[0]
            y += delta[1]
        elif action == 'Rotation':
            assert abs(delta) in (0, 90, 180, 270)
            angle += math.radians(delta)
        elif action == 'Forward':
            x += round(math.cos(angle)) * delta
            y += round(math.sin(angle)) * delta
        else:
            assert False  # Invalid action.
    print("Manhattan distance part one: {}".format(manhattan_distance(x, y)))


def manhattan_distance(x, y):
    return abs(x) + abs(y)


def part_two(actions):
    x, y = 0, 0
    wx, wy = 10, 1
    for action, delta in actions:
        if action == 'Translation':
            wx += delta[0]
            wy += delta[1]
        elif action == 'Rotation':
            assert abs(delta) in (0, 90, 180, 270)
            radians = math.radians(delta)
            cos_a = round(math.cos(radians))
            sin_a = round(math.sin(radians))
            wx, wy = wx*cos_a - wy*sin_a, wx*sin_a + wy*cos_a
        elif action == 'Forward':
            x += wx * delta
            y += wy * delta
        else:
            assert False  # Invalid action.
    print("Manhattan distance part two: {}".format(manhattan_distance(x, y)))


def main():
    instructions = parse_input('12.txt')
    actions = get_actions_from_instructions(instructions)
    part_one(actions.copy())
    part_two(actions.copy())


if __name__ == "__main__":
    main()
