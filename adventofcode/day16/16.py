# Day 16: Ticket Translation
import copy
import re


class Field:
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = ranges

    def verify(self, value):
        return any(a <= value <= b for a, b in self.ranges)


def parse_input(file_path):
    with open(file_path) as file:
        fields, my_ticket, nearby_tickets = file.read().split('\n\n')
        return {'fields': parse_fields(fields),
                'my_ticket': parse_tickets(my_ticket)[0],
                'nearby_tickets': parse_tickets(nearby_tickets)}


def parse_fields(fields_text):
    def parse_single_field(single_field_text):
        match = re.match(r'([a-z ]*): (\d+)-(\d+) or (\d+)-(\d+)', single_field_text)
        name = match.group(1)
        ranges = [(int(match.group(2)), int(match.group(3))),
                  (int(match.group(4)), int(match.group(5)))]
        return Field(name, ranges)

    return [parse_single_field(line) for line in fields_text.split('\n')]


def parse_tickets(tickets_text):
    return [[int(value) for value in ticket.split(',')]
            for ticket in tickets_text.rstrip().split('\n')[1:]]


def part_one(notes):
    sum_invalid = sum(verify_ticket(ticket, notes['fields'])[1]
                      for ticket in notes['nearby_tickets'])
    print("Answer part one: {}".format(sum_invalid))


def verify_ticket(ticket, rules):
    invalid_sum = 0
    valid = True
    for value in ticket:
        if not any(rule.verify(value) for rule in rules):
            invalid_sum += value
            valid = False
    return valid, invalid_sum


def part_two(notes):
    notes['nearby_tickets'] = filter_invalid_tickets(notes['nearby_tickets'], notes['fields'])
    candidates_per_field = get_candidates_per_field(notes['nearby_tickets'], notes['fields'])
    field_map = get_field_map(candidates_per_field)
    answer = 1
    for index, mapped_index in field_map.items():
        field = notes['fields'][mapped_index]
        if field.name.startswith('departure'):
            answer *= notes['my_ticket'][index]
    print("Answer part two: {}".format(answer))


def filter_invalid_tickets(tickets, rules):
    return [ticket for ticket in tickets if verify_ticket(ticket, rules)[0]]


def get_candidates_per_field(tickets, fields):
    candidates_per_field = []
    for i in range(len(fields)):
        possible_fields = set(range(len(fields)))
        for ticket in tickets:
            value = ticket[i]
            possible_fields = possible_fields.intersection(j for j, field in enumerate(fields)
                                                           if field.verify(value))
        candidates_per_field.append(possible_fields)
    return candidates_per_field


def get_field_map(candidates_per_field):
    sorted_indexes = [e[0] for e in sorted(enumerate(candidates_per_field),
                                           key=lambda x: len(x[1]))]
    taken = set()
    field_map = {}
    for i in sorted_indexes:
        candidates = list(candidates_per_field[i] - taken)
        assert len(candidates) == 1
        field_map[i] = candidates[0]
        taken.add(candidates[0])
    return field_map


def main():
    notes = parse_input('16.txt')
    part_one(copy.deepcopy(notes))
    part_two(copy.deepcopy(notes))


if __name__ == "__main__":
    main()
