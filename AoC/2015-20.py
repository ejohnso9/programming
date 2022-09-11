#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DISCUSSION

STRATEGY
"""

import sys
import pdb  # http://pymotw.com/2/pdb/
from itertools import permutations
from functools import reduce

# GLOBAL DATA
NL = '\n'
TARGET = 33_100_000


def factor(n):
    """https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python"""
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def nPresentsAtHouse(house_num):
    factors = factor(house_num)

    # Part 2: only factors <= 50 * house_num should be used - less than that and those elves have
    # already delivered to their 50 houses and "quit".
    # def filter_factors(factor):
    #     return factor * 50 <= house_num

    # total_1 = 10 * sum(factors)
    # if total_1 >= TARGET:
    #     pass
    #     # print(f"at house_num {house_num}: total = {total_1}, {factors}")
    #     # print(f"T1: {house_num}: {total_1}")
    #     # print(house_num)

    last_elf_num = house_num / 50.0
    new_factors = [f for f in factors if f >= last_elf_num]
    total_2 = 11 * sum(new_factors)

    # if total_1 >= TARGET:
    #     print(f"T2: at house {house_num}: {total_2}")

    return total_2


def main():

    max_val = 0
    for i in range(1, 1_000_000):
        nPresents = nPresentsAtHouse(i)
        if i % 100_000 == 0:
            print(f"i = {i}")

        if nPresents >= TARGET:
            print(f"House {i} got {nPresents} presents.")
            break

    # found: 776160  # verified correct for Part 1 on 2022Aug05
    # found: 786240  # verified correct for Part 2 on 2022Aug05

    # I had previously glossed over part of the instructions:
    # Each elf delivers 11 presents in part 2. With that, the correct
    # answer pops right out: 786240  # accepted on AoC website 2022Aug09

if __name__ == '__main__':
    main()

"""
numbers between 776,000 and 888,000 that get more than
33,100,000 presents under Part 1 rules: (Elves go to infinite houses)
NB: there are 39 such numbers:
NB: 887040 has been declared to not be the right answer and too big

776160 786240 803880 813960 819000 823680 826560 829920
831600 835380 839160 840840 846720 850080 851760 855360
856800 859320 861120 861840 864864 866880 868560 869400
870480 871200 871920 873180 873600 875160 876960 877800
879120 881280 882000 884520 885360 885780 887040
"""
# EOF

