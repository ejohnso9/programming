#!/usr/bin/env python 

"""
Advent of Code solution for Day 6
    https://adventofcode.com/2022/day/6

THOUGHTS/IDEAS/DISCUSSION:


HISTORY
    2023Aug09  ej  created
"""

from typing import Callable
# from functools import partial

# GLOBAL DATA
DAY = 6
LINES = None
FILENAME = f"2022-{DAY:02d}.input.txt"
PROBLEM = f"Aoc 2022 Day {DAY},"


def readInputFile(filePath_str):
    """read input file (just once)"""
    global LINES
    if not LINES:
        with open(filePath_str, 'r') as fd:
            LINES = fd.readlines()

    return LINES


def f_findUniqueIndex(s, n) -> int:
    """
    Python has a native set type. Such constructors are generally written in optimized C.
    Let's put that to use and get a small, clean, crisp, "Pythonic" solution.
    :return: the offset at which the first unique 4-chars occurs.
    """

    for i in range(len(s) - n + 1):
        if len(set(s[i: i + n])) == n:
            return i + n

    raise RuntimeError  # NOT FOUND!


def main():
    """Implements AoC Day N"""

    # read input file, initialize the main data structure
    lines = readInputFile(FILENAME)
    s = lines[0]  # there's just one big string

    # Part 1: first unique 4 characters found after reading 'answer' chars
    # s = "abcd"  # TEST: should not fail, have to read 4 chars to find unique part
    part = 1
    n = 4
    answer = f_findUniqueIndex(s, n)
    exp = 1134  # submitted and accepted on 2023Aug09 (2nd try)
    print(f"{PROBLEM} Part {part}: first uniq{n} after: {answer} chars")
    print(s[answer - n: answer])
    print()

    # Part 2: same as part one, but find longer unique part
    part = 2
    n = 14
    answer = f_findUniqueIndex(s, n)
    exp = 2263  # submitted and accepted on 2023Aug09 (1st try)
    print(f"{PROBLEM} Part {part}: first uniq{n} after: {answer} chars")
    print(s[answer - n: answer])


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF
