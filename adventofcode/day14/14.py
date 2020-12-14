# Day 14: Docking Data
import re


class BitmaskOne:
    def __init__(self, mask):
        self.or_mask = int(mask.replace('X', '0'), 2)
        self.and_mask = int(mask.replace('X', '1'), 2)

    def apply(self, value):
        value &= self.and_mask
        value |= self.or_mask
        return value


class BitmaskTwo:
    def __init__(self, mask):
        self.num_bits = len(mask)
        self.x_positions = [i for i, bit in enumerate(mask) if bit == 'X']
        self.or_mask = int(mask.replace('X', '0'), 2)

    def apply(self, value):
        value |= self.or_mask
        for n in range(2 ** len(self.x_positions)):
            masked_value = value
            for i, position in enumerate(self.x_positions):
                if (n & (1 << i)) > 0:
                    masked_value = set_bit(masked_value, self.num_bits - position - 1)
                else:
                    masked_value = clear_bit(masked_value, self.num_bits - position - 1)
            yield masked_value


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


def parse_input(file_path):
    with open(file_path) as file:
        return [parse_instruction(instruction.rstrip()) for instruction in file.readlines()]


def parse_instruction(instruction):
    if instruction.startswith('mask'):
        return ('mask', instruction.split(' = ')[1])
    elif instruction.startswith('mem'):
        match = re.match(r'mem\[(\d+)\] = (\d+)', instruction)
        return ('mem', {'address': int(match.group(1)), 'value': int(match.group(2))})
    else:
        assert False  # Invalid instruction.


def part_one(instructions):
    memory = {}
    for action, argument in instructions:
        if action == 'mask':
            bitmask = BitmaskOne(argument)
        elif action == 'mem':
            memory[argument['address']] = bitmask.apply(argument['value'])
        else:
            assert False  # Invalid instruction.
    print(sum(v for v in memory.values()))


def part_two(instructions):
    memory = {}
    for action, argument in instructions:
        if action == 'mask':
            bitmask = BitmaskTwo(argument)
        elif action == 'mem':
            for address in bitmask.apply(argument['address']):
                memory[address] = argument['value']
        else:
            assert False  # Invalid instruction.
    print(sum(v for v in memory.values()))


def main():
    instructions = parse_input('14.txt')
    part_one(instructions.copy())
    part_two(instructions.copy())


if __name__ == "__main__":
    main()
