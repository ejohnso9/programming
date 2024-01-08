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
from common import load_lines
from copy import copy
import pdb  # https://pymotw.com/2/pdb/
import string
import sys


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = "2023-04.txt"

def match_count(line):
    rest = line[line.index(':') + 1:]
    win, have = rest.split('|')
    win_loi = [int(n) for n in win.split()]
    assert len(set(win_loi)) == len(win_loi)
    have_loi = [int(n) for n in have.split()]
    assert len(set(have_loi)) == len(have_loi)

    return sum([1 for num in win_loi if num in have_loi])



def main():

    N = 198

    # read the data file
    lines = load_lines(INPUT_FILENAME)
    print(f"loaded {len(lines)} lines")


    # Part 1: 
    match_counts = [match_count(line) for line in lines[:-1]]  # -1 b/c I put a blank line on end of file
    values = [2 ** (count - 1) if count > 0 else 0 for count in match_counts]
    # print(len(match_counts))
    print(f"Part 1: {sum(values)}")  # 20117 accepted 2024Jan06T1709

    # Part 2:
    # pdb.set_trace()
    counts = [1] * N  # i.e., how many of each card after getting copies
    for i in range(N):
        k = counts[i]
        index = i + 1
        for j in range(match_counts[i]):
            counts[index] += k
            index += 1

    print(f'Part 2: {sum(counts)}')  # 13768818 accepted 2024Jan08T1145

    return 0  # main() normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main()
    print(f"exit({rc}).")

# EOF
