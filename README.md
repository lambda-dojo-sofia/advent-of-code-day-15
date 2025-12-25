# Advent of Code 2015 – Day 15: Science for Hungry People

This repo contains a small Python solution for **Advent of Code 2015 – Day 15**.
It searches all possible ways to distribute **100 spoons** across the given ingredients and prints the maximum cookie score.

> Originally built via pair programming (20min Pomodoros) at Lambda Dojo Sofia (2016-10-17).

## What it solves

- **Part 1**: maximize the cookie score
- **Note**: the input includes `calories`, but this implementation **ignores calories** (i.e., it does *not* solve Part 2).

## Requirements

- Python 3 (works with PyPy3 as well)

## Running

Using the included example input:

    ./python3.py input.txt

Or explicitly via Python/PyPy:

    python3 python3.py input.txt
    pypy3 python3.py input.txt

## Input format

Each line describes an ingredient and its properties:

    Name: capacity X, durability Y, flavor Z, texture T, calories C

The script reads all properties except `calories`.

## How it works (brief)

- `maximize_score(...)` recursively assigns spoons to each ingredient and tries all valid allocations that sum to 100.
- `calc_score(...)` sums each property across ingredients (weighted by spoons) and computes the final score as the product of all property totals, clamping negative totals to 0.

With 4 ingredients and 100 spoons this is still small enough to brute force.

## License

MIT
