# Day 18: Operation Order
import re


class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return "({}, {})".format(self.type, self.value)


def main():
    expressions = parse_input('18.txt')
    part_one(expressions.copy())
    part_two(expressions.copy())


def parse_input(file_path):
    with open(file_path) as file:
        return [line.rstrip() for line in file.readlines()]


def part_one(expressions):
    answer = sum_expressions(expressions, precedence_part_one)
    print("Answer part one: {}".format(answer))


def part_two(expressions):
    answer = sum_expressions(expressions, precedence_part_two)
    print("Answer part two: {}".format(answer))


def sum_expressions(expressions, precedence):
    return sum(shunting_yard(tokenize(expression), precedence) for expression in expressions)


def tokenize(expression):
    token_specification = [
        ('INT', r'\d+?'),
        ('OP', r'[+*]'),
        ('GROUP', r'[\(\)]'),
        ('SKIP', r' '),
        ('MISMATCH', r'.'),
    ]
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for match in re.finditer(token_regex, expression):
        kind = match.lastgroup
        value = match.group()
        if kind == 'INT':
            value = int(value)
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError("{!r} unexpected".format(value))
        yield Token(kind, value)


def precedence_part_one(a, b):
    return 0


def precedence_part_two(a, b):
    return ord(a.value) - ord(b.value)


def shunting_yard(tokens, precedence):
    # See https://en.wikipedia.org/wiki/Shunting-yard_algorithm
    def apply_operand():
        operator = operator_stack.pop()
        b = operand_stack.pop()
        a = operand_stack.pop()
        assert operator.type == 'OP'
        assert a.type == 'INT'
        assert b.type == 'INT'
        if operator.value == '+':
            result = a.value + b.value
        elif operator.value == '*':
            result = a.value * b.value
        else:
            assert False
        operand_stack.append(Token('INT', result))

    operand_stack = []
    operator_stack = []
    for token in tokens:
        if token.type == 'INT':
            operand_stack.append(token)
        elif token.type == 'OP':
            while (operator_stack
                   and operator_stack[-1].value != '('
                   and (precedence(operator_stack[-1], token) >= 0)):
                apply_operand()
            operator_stack.append(token)
        elif token.value == '(':
            operator_stack.append(token)
        elif token.value == ')':
            while operator_stack[-1].value != '(':
                apply_operand()
            if operator_stack[-1].value == '(':
                operator_stack.pop()

    while operator_stack:
        apply_operand()
    assert len(operand_stack) == 1
    return operand_stack[0].value


if __name__ == "__main__":
    main()
