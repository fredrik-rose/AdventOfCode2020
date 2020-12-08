# Day 8: Handheld Halting


class Emulator:
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.accumulator = 0

    def tick(self):
        try:
            operation, operand = self.program[self.pc]
        except IndexError:
            return False
        getattr(self, '_{}'.format(operation))(operand)
        return True

    def _nop(self, operand):
        self.pc += 1

    def _jmp(self, operand):
        self.pc += operand

    def _acc(self, operand):
        self.accumulator += operand
        self.pc += 1


def parse_input(file_path):
    with open(file_path) as file:
        return [parse_instruction(instruction) for instruction in file.readlines()]


def parse_instruction(instruction):
    operation, operand = instruction.split()
    return (operation, int(operand))


def part_one(program):
    emulator = Emulator(program)
    does_halt = halts(emulator)
    assert not does_halt
    print("Accumulator value just before any instruction is executed a second time: {}".format(emulator.accumulator))


def halts(emulator):
    executed_instructions = set()
    while emulator.pc not in executed_instructions:
        executed_instructions.add(emulator.pc)
        if not emulator.tick():
            return True
    return False


def part_two(program):
    for program in modified_program_generator(program):
        emulator = Emulator(program)
        if halts(emulator):
            print("Accumulator value with correct program: {}".format(emulator.accumulator))
            break


def modified_program_generator(program):
    instruction_replacement = {'nop': 'jmp',
                               'jmp': 'nop',
                               'acc': 'acc'}
    for i, (operation, operand) in enumerate(program):
        program_copy = program.copy()
        program_copy[i] = (instruction_replacement[operation], operand)
        yield program_copy


def main():
    program = parse_input('8.txt')
    part_one(program.copy())
    part_two(program.copy())


if __name__ == "__main__":
    main()
