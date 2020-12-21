import time
import re

def read_file():
    lines = []
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    foods = {}
    for line in lines:
        ingredients, allergens = line.split(' (')
        allergens = re.sub('contains |[)]', '', allergens)
        ingredients = tuple(ingredients.split(' '))
        allergens = set(allergens.split(', '))

        foods[ingredients] = allergens

    return foods


def part_1(foods):
    allergens = set(y for x in foods.values() for y in x)
    ingredients = [y for x in foods.keys() for y in x]
    ingredients_count = { k:ingredients.count(k) for k in ingredients }

    candidates = {}
    for allergen in allergens:
        for food in foods:
            if allergen in foods[food]:
                candidates[allergen] = set(food) if allergen not in candidates else candidates[allergen].intersection(food)

    dangerous = set(y for x in candidates.values() for y in x)
    inert = set(ingredients) - dangerous
    return sum([ingredients_count[ingredient] for ingredient in inert]), candidates


def part_2(candidates):
    allergens = {}
    while len(candidates) > 0:
        sorted_candidates = sorted(candidates, key=lambda x: len(candidates[x]))
        while len(sorted_candidates) > 0 and len(candidates[sorted_candidates[0]]) == 1:
            selected = sorted_candidates.pop(0)
            allergens[selected] = candidates.pop(selected).pop()

        for allergen in sorted_candidates:
            candidates[allergen].difference_update(allergens.values())

    ingredients_list = ','.join([allergens[allergen] for allergen in sorted(allergens)])

    return ingredients_list


def main():
    foods = read_file()

    ts = time.time()
    result, candidates = part_1(foods)
    print(f'Silver: {result}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_2(candidates)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
