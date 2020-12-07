# Day 7: Handy Haversacks
import collections as coll
import re


def parse_input(file_path):
    with open(file_path) as file:
        return [parse_bag(bag) for bag in file.readlines()]


def parse_bag(bag_text):
    bag = re.search(r'([a-z ]+) bags contain', bag_text).group(1)
    bags_in_bag = [(m[1], int(m[0])) for m in re.findall(r'(\d+) ([a-z ]+) bag', bag_text)]
    return (bag, bags_in_bag)


def part_one(bags):
    bag_map = create_contained_by_bag_map(bags)
    contains_gold = get_bags_that_contain_bag(bag_map)
    print("There are {} bags that eventually contain at least one shiny gold bag.".format(len(contains_gold)))


def create_contained_by_bag_map(bags):
    bag_map = coll.defaultdict(list)
    for bag, bags_in_bag in bags:
        for contained in bags_in_bag:
            bag_map[contained[0]].append(bag)
    return bag_map


def get_bags_that_contain_bag(bags, bag_name='shiny gold'):
    bags_contained_by_bag = bags[bag_name]
    result = set(bags_contained_by_bag).union(*(get_bags_that_contain_bag(bags, bag) for bag in bags_contained_by_bag))
    return result


def part_two(bags):
    bag_map = create_contains_bag_map(bags)
    count = count_bags_in_bag(bag_map)
    print("A shiny gold bag contains {} other bags.".format(count))


def create_contains_bag_map(bags):
    return dict(bags)


def count_bags_in_bag(bags, key='shiny gold'):
    return sum(num * (1 + count_bags_in_bag(bags, bag)) for bag, num in bags[key])


def main():
    bags = parse_input('7.txt')
    part_one(bags.copy())
    part_two(bags.copy())


if __name__ == "__main__":
    main()
