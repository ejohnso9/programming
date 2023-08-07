#!/usr/bin/env python 

"""
Advent of Code solution for Day 3: Rucksack Reorganization
https://adventofcode.com/2022/day/3

THOUGHTS/IDEAS/DISCUSSION:
    As on the previous two days, the general pattern is mapping a value function over
    rows of input, then aggregating (as sum) for all the inputs.
    That's a pretty clean and familiar pattern: just copy previous day's solution,
    write new value function. The logic for one range completely overlapping another
    range is easy enough.

HISTORY
    2023Aug07  ej  created
"""

from typing import Callable
from functools import partial

# GLOBAL DATA
DAY = 4
FILENAME = f"2022-{DAY:02d}.input.txt"
PROBLEM = f"Aoc 2022 Day {DAY},"


def contains(range_1: tuple, range_2: tuple) -> bool:
    """
    Predicate for whether 'range_1' is wholly contained within 'range_2' OR vice versa
    :parameter range_1: 2-tuple of ints
    :parameter range_2: 2-tuple of ints
    """

    a, b = range_1
    x, y = range_2

    return (x >= a and y <= b) or (a >= x and b <= y)


def overlaps(range_1: tuple, range_2: tuple) -> bool:
    """
    Predicate for whether 'range_1' overlaps 'range_2' at all.
    Logically, either endpoint of one range is on or between the endpoints of the other,
    or vice verse (swapping the two pairs).

    :parameter range_1: 2-tuple of ints
    :parameter range_2: 2-tuple of ints
    :return: True if any overlap, else False
    """

    a, b = range_1
    x, y = range_2

    return (
        (x <= a <= y) or (x <= b <= y)     # one of endpoints of 1st range "inside" bounds of 2nd range
        or (a <= x <= b) or (a <= y <= b)  # or vice-versa
    )


def f_part1Value(line: str, f_logic: Callable) -> int:
    """
    Convert a line of input to either 0 or 1

    :param line: the input line as string (need not be stripped)
    :return: 1 if one range is contained within the other, else 0
    """

    try:
        a, b = line.split(',')
        r1 = tuple([int(w) for w in a.split('-')])
        r2 = tuple([int(w) for w in b.split('-')])
        return 1 if f_logic(r1, r2) else 0
    except ValueError:
        print(f"ValueError on line {line_index}")


def main():
    """Implements AoC Day 4"""

    # read input file
    with open(FILENAME, 'r') as fd:
        lines = fd.readlines()

    # Part 1: number of completely-overlapping pairs
    f_value = f_part1Value
    total = sum([f_value(line, f_logic=contains) for line in lines])
    exp = 573
    print(f"{PROBLEM} Part 1: count of contained pairs: {total}  (should be {exp})")
    assert total == exp
    # 573 submitted and accepted 2023Aug07 (first try! ;)

    # Part 2: number of pairs that overlap at all
    # let's now make both parts "extra DRY"...
    part = 2
    f_value = partial(f_part1Value, f_logic=overlaps)
    total = sum([f_value(line) for line in lines])
    exp = 867
    print(f"{PROBLEM} Part {part}: count of overlapping pairs: {total}  (should be {exp})")
    assert total == exp
    # 1440 is too high :(  (not sure why I got this, but diff answer after cleanup)
    # 867 submitted and accepted on 2023Aug07 (2nd try)


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF
