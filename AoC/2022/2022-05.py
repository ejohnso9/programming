#!/usr/bin/env python 

"""
Advent of Code solution for Day 3: Rucksack Reorganization
https://adventofcode.com/2022/day/3

THOUGHTS/IDEAS/DISCUSSION:
    The top of the data file shows the initial state for crate stacks:

[Q]         [N]             [N]    
[H]     [B] [D]             [S] [M]
[C]     [Q] [J]         [V] [Q] [D]
[T]     [S] [Z] [F]     [J] [J] [W]
[N] [G] [T] [S] [V]     [B] [C] [C]
[S] [B] [R] [W] [D] [J] [Q] [R] [Q]
[V] [D] [W] [G] [P] [W] [N] [T] [S]
[B] [W] [F] [L] [M] [F] [L] [G] [J]
 1   2   3   4   5   6   7   8   9 

move 3 from 6 to 2
move 2 from 8 to 7
...


    If I were writing general software for this kind of problem, of
    course, we would want to parse those lines of data. But I'm not
    solving multiple input files like that. I've got 25 days of advent
    to try to get through and this is only day 5 (Day 5 of the 5 easiest
    day on the calendar, so let's look at the data, init the data
    structures "by hand" and "get on with it"!

HISTORY
    2023Aug07  ej  created
"""

from typing import Callable
from functools import partial

# GLOBAL DATA
DAY = 4
FILENAME = f"2022-{DAY:02d}.input.txt"
PROBLEM = f"Aoc 2022 Day {DAY},"


def init()
    """read the input file, return initial list-of-lists, list of lines"""
    lol = [
        list("BVSNTCHQ"),
        list("WDBG"),
        list("FWRTSQB"),
    ]
    # read input file
    with open(FILENAME, 'r') as fd:
        lines = fd.readlines()

    # find the blank line, return what's below it


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

    # 
    stacks_lol, lines = init(FILENAME)

    # Part 1: number of completely-overlapping pairs
    # f_value = f_part1Value
    # total = sum([f_value(line, f_logic=contains) for line in lines])
    # exp = 573
    # print(f"{PROBLEM} Part 1: count of contained pairs: {total}  (should be {exp})")
    # assert total == exp
    # 573 submitted and accepted 2023Aug07 (first try! ;)

    # Part 2: number of pairs that overlap at all
    # let's now make both parts "extra DRY"...
    # part = 2
    # f_value = partial(f_part1Value, f_logic=overlaps)
    # total = sum([f_value(line) for line in lines])
    # exp = 867
    # print(f"{PROBLEM} Part {part}: count of overlapping pairs: {total}  (should be {exp})")
    # assert total == exp
    # 1440 is too high :(  (not sure why I got this, but diff answer after cleanup)
    # 867 submitted and accepted on 2023Aug07 (2nd try)


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF


