#!/usr/bin/env python 

"""
Advent of Code solution for Day 5
    https://adventofcode.com/2022/day/5

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

If I were writing general software for this kind of problem, of course,
we would want to parse those lines of data. But I'm not solving multiple
input files like that. I've got 25 days of advent to try to get through
and this is only day 5 (of the 5 easiest days on the calendar) so, I'm
going to just manually read the stacks above and init a list of strings
"by hand" and get on with the rest of the problems.

HISTORY
    2023Aug08  ej  created
    2023Aug09  ej  Part 2 submitted, accepted
"""

from typing import Callable
from functools import partial

# GLOBAL DATA
DAY = 5
LINES = None
FILENAME = f"2022-{DAY:02d}.input.txt"
PROBLEM = f"Aoc 2022 Day {DAY},"


def processCommands(commands: list, stacks: list[str], doReverse=True) -> list[str]:
    """Execute each command, manipulate 'stacks' accordingly."""

    # helper function
    def pull(n_chars: int, stackIndex: int):
        s = stacks[stackIndex]  # the string to read and change
        stacks[stackIndex] = s[:-n_chars]  # s minus last n chars
        return s[-n_chars:]  # the last n chars that were on that stack

    # helper function
    def push(s: str, stackIndex: int):
        stacks[stackIndex] += s

    # process each of the commands, manipulate 'stacks'
    for cmd in commands:
        words = cmd.split()  # on whitespace
        n, fromStack, toStack = [int(words[i]) for i in (1, 3, 5)]  # NB: 1-based indices!
        s = pull(n, fromStack - 1)  # 'fromStack' is 1-based, passing 0-based index
        if doReverse:
            s = s[::-1]
        push(s, toStack - 1)  # 'toStack' is 1-based, passing 0-based index

    return stacks  # list of strings (after commends)


def init(input_file) -> tuple:
    """read the input file, return initial list-of-str, list of command lines"""

    # the stacks of crates (top on right)
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

    # read input file (once)
    global LINES
    if not LINES:
        with open(input_file, 'r') as fd:
            LINES = fd.readlines()

    # find the blank line, return what's below it
    blank_index = [i for i, line in enumerate(LINES) if line.strip() == ""][0]
    commands = LINES[blank_index + 1:]

    return stacks, commands


def main():
    """Implements AoC Day 5"""

    # read input file, initialize the main data structure
    stacks_lol, commands = init(FILENAME)

    # do the stack manipulations
    stacks = processCommands(commands, stacks_lol)
    answer = ''.join([s[-1] for s in stacks])

    # Part 1: str w/ letter of top box in each stack
    part = 1
    exp = 'FJSRQCFTN'  # submitted and accepted 2023Aug08 (first try!)
    print(f"{PROBLEM} Part {part}: top of each stack: {answer}")

    # Part 2: same as part one, but w/o reveral
    # change code to make the string reversal a parameter (keyword w/ default for Part 1)
    part = 2
    stacks_lol, commands = init(FILENAME)
    stacks = processCommands(commands, stacks_lol, doReverse=False)
    answer = ''.join([s[-1] for s in stacks])
    exp = 'CJVLJQPHS'  # submitted and accepted on 2023Aug09 (1st try)
    print(f"{PROBLEM} Part {part}: top of each stack: {answer}")


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF
