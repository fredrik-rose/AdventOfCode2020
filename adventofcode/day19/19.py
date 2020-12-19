# Day 19: Monster Messages
import re


def main():
    part_one('19.txt')
    part_two('19.txt')


def part_one(file_path):
    rules, messages = parse_input(file_path)
    answer = count_valid_messages(rules, messages)
    print("Answer part one: {}".format(answer))


def part_two(file_path):
    rule_replacers = {'8: 42': '8: 42 | 42 8',
                      '11: 42 31': '11: 42 31 | 42 11 31'}
    rules, messages = parse_input(file_path, rule_replacers)
    answer = count_valid_messages(rules, messages)
    print("Answer part two: {}".format(answer))


def parse_input(file_path, rule_replacers={}):
    with open(file_path) as file:
        rules, messages = file.read().split('\n\n')
        for old, new in rule_replacers.items():
            rules = rules.replace(old, new)
        return parse_rules(rules.rstrip()), parse_messages(messages.rstrip())


def parse_rules(rules_text):
    def parse_single_rule(rule_text):
        rule_id, raw_rule = rule_text.split(':')
        raw_branches = raw_rule.strip().split(' | ')
        branches = [[rule.replace('"', '') for rule in branch.split(' ')]
                    for branch in raw_branches]
        return (rule_id, branches)

    return dict(parse_single_rule(rule) for rule in rules_text.split('\n'))


def parse_messages(messages_text):
    return messages_text.split('\n')


def count_valid_messages(rules, messages):
    pattern_from_graph = regexp_graph(rules, '0')
    pattern = re.compile('^{}$'.format(pattern_from_graph))
    num_valids = sum(1 if re.match(pattern, m) else 0 for m in messages)
    return num_valids


def regexp_graph(rules, rule_id):
    branches = []
    for branch in rules[rule_id]:
        expanded = []
        for rule in branch:
            if not rule.isdigit():
                expanded.append(rule)
            elif rule.isdigit() and rule != rule_id:
                expanded.append(regexp_graph(rules, rule))
        if rule_id in branch:  # A recursive graph, the format is either [X: A | A B] or [X: A B | A X B].
            # Everything in this if branch is a hack.
            assert len(expanded) in (1, 2)
            b = expanded.pop()
            try:
                a = expanded.pop()
            except IndexError:
                a = ''
            for i in range(10):  # Arbitrary number, must cover the max recursive depth.
                n = i + 1
                expanded.append(a * n + b * n)
            pattern = '|'.join(expanded)
        else:
            pattern = ''.join(expanded)
        branches.append(pattern)
    return '({})'.format('|'.join(branches))


if __name__ == "__main__":
    main()
