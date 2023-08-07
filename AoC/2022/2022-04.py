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

    return ((x <= a <= y) or (x <= b <= y)
            or (a <= x <= b) or (a <= y <= b))


def f_part1Value(line: str, line_index: int) -> int:
    """
    Convert a line of input to either 0 or 1

    :param line: the input line as string (need not be stripped)
    :return: 1 if one range is contained within the other, else 0
    """

    try:
        a, b = line.split(',')
        r1 = tuple([int(w) for w in a.split('-')])
        r2 = tuple([int(w) for w in b.split('-')])
        if r1 is None or r2 is None:
            _ = "STOP"
        return 1 if contains(r1, r2) else 0
    except ValueError:
        print(f"ValueError on line {line_index}")


def f_part2Value(line: str, line_index: int) -> int:
    """
    Convert a line of input to either 0 or 1

    :param line: the input line as string (need not be stripped)
    :return: 1 if one range is contained within the other, else 0
    """

    try:
        a, b = line.split(',')
        r1 = tuple([int(w) for w in a.split('-')])
        r2 = tuple([int(w) for w in b.split('-')])
        return 1 if contains(r1, r2) else 0
    except ValueError:
        print(f"ValueError on line {line_index}")


def main():
    with open(FILENAME, 'r') as fd:
        lines = fd.readlines()

    # Part 1: number of overlapping pairs
    total = 0
    f_value = f_part1Value
    for index, line in enumerate(lines):
        value = f_value(line, index + 1)
        total += value
    print(f"{PROBLEM} Part 1: count of overlapping pairs: {total}")
    # 573 submitted and accepted 2023Aug07 (first try! ;)

    # Part 2: TODO
    # f_value = f_part2Value
    # badgeScores = [f_value(lines[i: i + 3]) for i in range(0, len(lines), 3)]
    # print(f"{PROBLEM} 2: total priority: {sum(badgeScores)}")
    # submitted and accepted on 2023Aug07


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF
