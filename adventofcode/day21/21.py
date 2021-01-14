# Day 21: Allergen Assessment
import copy


def main():
    foods = parse_input('21.txt')
    allergen_map = create_allergen_map(foods)
    part_one(copy.deepcopy(foods), copy.deepcopy(allergen_map))
    part_two(copy.deepcopy(allergen_map))


def parse_input(file_path):
    with open(file_path) as file:
        return [parse_food(line.rstrip()) for line in file]


def parse_food(text):
    assert len(text.split('(')) == 2
    raw_ingredients, raw_allergens = text.split('(')
    ingridents = raw_ingredients.rstrip().split(' ')
    allergens = raw_allergens[9:-1].split(', ')  # Remove 'contains'.
    return (ingridents, allergens)


def create_allergen_map(foods):
    allergen_map = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen not in allergen_map:
                allergen_map[allergen] = set(ingredients)
            else:
                allergen_map[allergen] = allergen_map[allergen].intersection(ingredients)
    return allergen_map


def part_one(foods, allergen_map):
    ingredients_that_may_contain_allergens = set().union(*allergen_map.values())
    count = sum(1 for ingredients, _ in foods for ingredient in ingredients
                if ingredient not in ingredients_that_may_contain_allergens)
    print("Answer part one: {}".format(count))


def part_two(allergen_map):
    reduced_allergen_map = {}
    while len(reduced_allergen_map) < len(allergen_map):
        for allergen, ingredients in allergen_map.items():
            # Find an allergen that maps to exactly one ingredient.
            if allergen not in reduced_allergen_map and len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                reduced_allergen_map[allergen] = ingredient  # Create a mapping in the new reduced map.
                break
        else:
            assert False
        # We have found an allergen mapping for the ingredient, remove it from the old map.
        remove_ingrident(allergen_map, ingredient)
    sorted_allergens = [allergen for _, allergen in
                        sorted(zip(reduced_allergen_map.keys(), reduced_allergen_map.values()),
                               key=lambda pair: pair[0])]
    print("Answer part two: {}".format(','.join(sorted_allergens)))


def remove_ingrident(allergen_map, ingredient):
    for ingridents in allergen_map.values():
        ingridents.discard(ingredient)


if __name__ == "__main__":
    main()
