#!/usr/bin/env python 

"""
Advent of Code solution for Day 3: Rucksack Reorganization
https://adventofcode.com/2022/day/3

THOUGHTS/IDEAS/DISCUSSION:
    As on the previous two days, the general pattern is mapping a value function over
    rows of input, getting a toal sum for all the inputs.
    That's a pretty clean and familiar pattern: just copy previous day's solution,
    write new value function.

HISTORY
    2023Aug06  ej  created
"""

# GLOBAL DATA
FILENAME = "2022-03.input.txt"
PROBLEM = "Aoc 2022 Day 3,"


def f_priority(c: str) -> int:
    """
    Map a single character string to its priority value:
        a - z: 1 - 26   # caps map to ASCII 97 - 122
        A - Z: 27 - 52  # caps map to ASCII 65 - 90
    NB: char assumed to be a-z or A-Z: no validation!
    """

    if 'a' <= c <= 'z':
        # LC letters in the lower range
        return ord(c) - ord('a') + 1
    else:
        # UC letters in the upper range
        return ord(c) - ord('A') + 27 


def f_part1Value(sackItems: str) -> int:
    """
    Given a string of charaters representing the items in a rucksack,
    the first compartment being the first half of the string and the 2nd compartment
    being the second half of the string, find the item that is duplicated in both
    compartments, return an int value for the "priority" of the common item.
    """
    half = len(sackItems) // 2  # index spitting the two compartments
    comp1, comp2 = sackItems[:half], sackItems[half:]
    for c in list(comp1):
        if c in comp2:
            return f_priority(c)


def f_part2Value(los: list) -> int:
    """
    Given 3 lines at a time, find the item common to all 3, return its prioity
    :param los - listOfString: 3 rucksack item strings
    """

    for c in list(los[0][:-1]):  # drop trailing '\n'
        if c in los[1] and c in los[2]:
            return f_priority(c)


def main():
    with open(FILENAME, 'r') as fd:
        lines = fd.readlines()

    # Part 1: my total RPS score
    f_value = f_part1Value
    p1_total = sum([f_value(line) for line in lines])
    print(f"{PROBLEM} 1: total priority: {p1_total}")
    # 8349 submitted and accepted 2023Aug06 (first try! ;) yay)

    # Part 2: As before, the basic functional pattern remains mainly the same, but now instead
    #   of valuating a single row, we're going to value 3 rows at a time. Fine, define a new 
    #   value function with a list param, pass list slices of length 3 to that.
    f_value = f_part2Value
    badgeScores = [f_value(lines[i: i + 3]) for i in range(0, len(lines), 3)]
    print(f"{PROBLEM} 2: total priority: {sum(badgeScores)}")
    # 2681 submitted and accepted on 2023Aug06 (again, first try! ;) yay)


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF
