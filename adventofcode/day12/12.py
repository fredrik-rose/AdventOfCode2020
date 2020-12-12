# Day 12: Rain Risk


def parse_input(file_path):
    with open(file_path) as file:
        return [parse_instruction(instruction.strip()) for instruction in file.readlines()]


def parse_instruction(instruction):
    operation, operand = instruction[0], int(instruction[1:])
    return (operation, operand)


def get_actions_from_instructions(instructions):
    translator = {'N': lambda x: ('Translation', +x * 1j),
                  'S': lambda x: ('Translation', -x * 1j),
                  'E': lambda x: ('Translation', +x),
                  'W': lambda x: ('Translation', -x),
                  'L': lambda x: ('Rotation', 1j ** (+x // 90)),
                  'R': lambda x: ('Rotation', 1j ** (-x // 90)),
                  'F': lambda x: ('Forward', x)}
    actions = [translator[operation](operand) for operation, operand in instructions]
    return actions


def part_one(actions):
    position = 0 + 0j
    angle = 1 + 0j
    for action, delta in actions:
        if action == 'Translation':
            position += delta
        elif action == 'Rotation':
            angle *= delta
        elif action == 'Forward':
            position = position + angle * delta
        else:
            assert False  # Invalid action.
    print("Manhattan distance part one: {}".format(manhattan_distance(position)))


def manhattan_distance(position):
    return round(abs(position.real) + abs(position.imag))


def part_two(actions):
    boat = 0 + 0j
    waypoint = 10 + 1j
    for action, delta in actions:
        if action == 'Translation':
            waypoint += delta
        elif action == 'Rotation':
            waypoint *= delta
        elif action == 'Forward':
            boat += waypoint * delta
        else:
            assert False  # Invalid action.
    print("Manhattan distance part two: {}".format(manhattan_distance(boat)))


def main():
    instructions = parse_input('12.txt')
    actions = get_actions_from_instructions(instructions)
    part_one(actions.copy())
    part_two(actions.copy())


if __name__ == "__main__":
    main()
