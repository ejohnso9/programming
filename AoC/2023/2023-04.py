#!/usr/bin/env python
#        1         2         3         4         5         6         7         8         9         0         1         2
#23456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# run on pythonanywhere.com @ Python version 3.9.5

r"""
Solution for: https://adventofcode.com/2023/day/4

DISCUSSION
    Seems like pretty trivial data processing - I don't have much to say about it.

STRATEGY
    Write the functions needed to turn a single line of input into the
    value for the card, sum up the values for all the cards and print
    out that.
"""


# Standard Python Library
import string
import sys
from common import load_lines


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = "2023-04.txt"

def card_value(line):
    rest = line[line.index(':') + 1:]
    win, have = rest.split('|')
    win_loi = [int(n) for n in win.split()]
    assert len(set(win_loi)) == len(win_loi)
    have_loi = [int(n) for n in have.split()]
    assert len(set(have_loi)) == len(have_loi)
    count = sum([1 for num in win_loi if num in have_loi])

    return 2 ** (count - 1) if count > 0 else 0


def process_lines(lines: list[str]) -> int:

    return [card_value(line) for line in lines]


def main():

    # read the data file
    lines = load_lines(INPUT_FILENAME)
    print(f"loaded {len(lines)} lines")


    # Part 1: Yay! 553079 accepted first try @ 2023Dec10T1724
    card_values = process_lines(lines[:-1])
    print(len(card_values))
    print(f"Part 1: {sum(card_values)}")  # 20117 accepted 2024Jan06T1709

    # Part 2:
    # print(f'Part 2: {"not implemented"}')

    return 0  # normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main()
    print(f"exit({rc}).")

# EOF
