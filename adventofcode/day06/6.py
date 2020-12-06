# Day 6: Custom Customs
import itertools


def parse_input(file_path):
    with open(file_path) as file:
        text = file.read().rstrip()
        return [parse_group(g) for g in text.split('\n\n')]


def parse_group(group):
    return [list(e) for e in group.split('\n')]


def part_one(groups):
    sum_of_any_yes = sum(len(set(itertools.chain(*g))) for g in groups)
    print("Total number of any 'yes' answers: {}".format(sum_of_any_yes))


def part_two(groups):
    sum_of_all_yes = sum(len(set.intersection(*(set(e) for e in g))) for g in groups)
    print("Total number of all 'yes' answers: {}".format(sum_of_all_yes))


def main():
    groups = parse_input('6.txt')
    part_one(groups.copy())
    part_two(groups.copy())


if __name__ == "__main__":
    main()
