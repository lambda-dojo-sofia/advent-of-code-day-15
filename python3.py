#!/usr/bin/env python3

import sys
import time
from collections import defaultdict


def maximize_score(ingredients_used, spoons_used, ingredients_left, spoons_left):
    if len(ingredients_left) == 0:
        return calc_score(ingredients_used, spoons_used), ingredients_used, spoons_used
    else:
        max_score = None
        max_ingredients = None
        max_spoons = None
        next_ingredient = ingredients_left[-1]
        if len(ingredients_left) == 1:
            min_spoons = spoons_left
        else:
            min_spoons = 0
        for spoons in range(min_spoons, spoons_left + 1):
            score, ingredients, spoons = \
                maximize_score(ingredients_used + [next_ingredient], spoons_used + [spoons],
                               ingredients_left[:-1], spoons_left - spoons)
            if max_score is None or score > max_score:
                max_score, max_ingredients, max_spoons = score, ingredients, spoons
        return max_score, max_ingredients, max_spoons

def calc_score(ingredients, spoons):
    total_capacities = defaultdict(int)

    for i, spoons in enumerate(spoons):
        ingredient, capacities = ingredients[i]
        for capacity, amount in capacities.items():
            total_capacities[capacity] = total_capacities[capacity] + spoons * amount

    score = 1
    for _, amount in total_capacities.items():
        score *= max(0, amount)

    return score


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: %s <input>" % sys.argv[0], file=sys.stderr)
        sys.exit(1)

    ingredients = []

    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip()
            if line == '': continue
            name, powers = line.split(': ')
            powers = powers.split(', ')
            powers = dict([[a, int(b)] for a, b in [p.split(' ') for p in powers] if a != 'calories'])
            ingredients.append([name, powers])

    spoons = 100

    max_score, ingredients, spoons = maximize_score([], [], ingredients, spoons)

    print("We've got a GRAND TOTAL OF ...   %d   !!!!1111" % max_score)

    for i, ingredient in enumerate(ingredients):
        print("%3dx %s" % (spoons[i], ingredient[0]))
