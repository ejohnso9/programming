#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
Still need to do Part 2

DISCUSSION
    naieve approach is way too slow.
    Need a decent factoring function.
    Found one on Google() @ StackOverflow.
    Cited.

STRATEGY

"""

import sys
import pdb  # http://pymotw.com/2/pdb/
from itertools import permutations
from functools import reduce

# GLOBAL DATA
NL = '\n'


def factor(n):
    """https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python"""
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def nPresentsAtHouse(house_num):
    factors = factor(house_num)
    return sum([i * 10 for i in factors])


def main():
    target = 33100000

    max_val = 0
    for i in range(1, 1_000_000):
        nPresents = nPresentsAtHouse(i)
        if nPresents > max_val:
            max_val = nPresents
            print(max_val)

        # print(f"House {i} got {nPresentsAtHouse(i)} presents.")
        if nPresents >= target:
            print("found:", i)
            break

    # found: 776160  # verified correct 2022Aug05

if __name__ == '__main__':
    main()

# EOF
