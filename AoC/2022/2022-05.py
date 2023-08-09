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
DAY = 5
FILENAME = f"2022-{DAY:02d}.input.txt"
PROBLEM = f"Aoc 2022 Day {DAY},"


def processCommands(commands: list, stacks: list[str]):
    """Execute each command, manipulate 'stacks' accordingly."""

    def pull(n_chars: int, stackIndex: int):
        s = stacks[stackIndex]  # the string to read and change
        stacks[stackIndex] = s[:-n_chars]  # s minus last n chars
        return s[-n_chars:]  # the last n chars that were on that stack

    def push(s: str, stackIndex: int):
        stacks[stackIndex] += s

    for cmd in commands:
        words = cmd.split()  # on whitespace
        n, fromStack, toStack = [int(words[i]) for i in (1, 3, 5)]
        s = pull(n, fromStack - 1)  # passing 0-based index
        push(s[::-1], toStack - 1)  # [::-1] => str reversed

    return stacks


def init(input_file):
    """read the input file, return initial list-of-str, list of command lines"""
    stacks = [
        "BVSNTCHQ",
        "WDBG",
        "FWRTSQB",
        "LGWSZJDN",
        "MPDVF",
        "FWJ",
        "LNQBJV",
        "GTRCJQSN",
        "JSQCWDM",
    ]

    # read input file
    with open(input_file, 'r') as fd:
        lines = fd.readlines()

    # find the blank line, axe it and what's above it
    blank_index = [i for i, line in enumerate(lines) if line.strip() == ""][0]
    commands = lines[blank_index + 1:]

    return stacks, commands


def main():
    """Implements AoC Day 5"""

    # read input file
    with open(FILENAME, 'r') as fd:
        lines = fd.readlines()

    # read input file, initialize the main data structure
    stacks_lol, commands = init(FILENAME)

    # do the stack manipulations
    stacks = processCommands(commands, stacks_lol)
    answer = ''.join([s[-1] for s in stacks])

    # Part 1: number of completely-overlapping pairs
    print(f"{PROBLEM} Part 1: top of each stack: {answer}")
    # 'FJSRQCFTN' submitted and accepted 2023Aug08 (first try!)

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


