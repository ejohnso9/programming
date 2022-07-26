#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DISCUSSION
    This is a classic travelling salesman problem (with only 8 nodes, in
    this case). It is (believed to be?) an "NP-hard" problem and is one
    of the most-studied problems in computer science.
    (see: https://en.wikipedia.org/wiki/Travelling_salesman_problem)

STRATEGY
    Just encode the given distance data as a python dict,
    use itertools.permuations to walk all the destination arrangements,
    implement a value function and look for the minimum.
"""

import sys
import pdb  # http://pymotw.com/2/pdb/
from itertools import permutations

# GLOBAL DATA
NL = '\n'

DISTANCES = """\
Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127
"""


def buildDistDict(lines):
    """
    Build a dict keyed by tuple of two destination names with int value.
    I will put both: (START, END) and (END, START) into the dict so that
    later, I don't need to care about which way we are going.
    Also, returning list of the city (destination) values (what we will
    make permutations out of).
    """

    rv_d = {}
    cities = []

    for line in lines:
        words = line.split()
        a, b = words[0], words[2]

        if a not in cities:
            cities.append(a)

        if b not in cities:
            cities.append(b)

        dist = int(words[-1])
        rv_d[(a, b)] = dist
        rv_d[(b, a)] = dist

    return rv_d, cities


def distance(perm, dist_d):
    """measure distance for one traversal of the 8 destinations"""
    return sum([dist_d[(perm[i], perm[i+1])] for i in range(len(perm) - 1)])


def main():
    # split data above into lines
    lines = DISTANCES.split(NL)[:-1]  # last line is empty
    dist_d, cities = buildDistDict(lines)
    # for k, v in dist_d.items():
    #     print(f"{k}: {v}")

    min_val = int(1e15)  # assuming this is way bigger than any real distance

    for p in permutations(cities):
        d = distance(p, dist_d)
        if d < min_val:
            min_val = d

    print(f"min_val is: {min_val}")  # 251 verfied correct on 2022Jul26


if __name__ == '__main__':
    main()

# EOF
