#!/usr/bin/env python

"""
DESCRIPTION
Python solution for Project Euler problem #62:
    https://projecteuler.net/problem=62

APPROACH
    The description gives the first cube that has three permutations that are also
cubes as 345.  A permutation of a numbers digits implies a number of same length,
so this gives some notion of the search space.

345 ** 3 is: 41036325, an 8 digit number. All permutations of that are also 8 digit numbers,
so there is no point in looking at numbers whose cubes are 7 digits or less or 9 digits or
more for other permutations of 345 that are also cubes.

The problem at hand doesn't have such a limit, but searching all the cubes of 8 digits seems
like a good starting place, and then 9 and 10 if 8 digit numbers don't yield a result.

Simply walking through numbers and building a dict of cubes in the 8-digit range seems
reasonable.
"""


import itertools
import math


# GLOBAL DATA
# list of all the perfect cubes (values of cubes_d)
cubes_l = []


def isCube(n):
    # let avoid this math: either it's listed in cubes_l or it isn't
    # cubeRoot = n ** (1/3)
    # if cubeRoot.is_integer():
    #     return True
    # else:
    #     cubeRoot_i = math.floor(cubeRoot + 0.5)
    #     rv = cubeRoot_i ** 3 == n
    # return rv

    return n in cubes_l


def findCubes(cubes_d, f_inRange):
    found_d = {}

    for i in cubes_d:
        print(i, flush=True)
        other_cubes_l = []
        cube = cubes_d[i]
        ls_i = [int(c) for c in list(str(cube))]
        for perm in itertools.permutations(ls_i):
            perm_i = int(''.join([str(i) for i in perm]))
            if isCube(perm_i):
                if perm_i not in other_cubes_l and f_inRange(perm_i):
                    other_cubes_l.append(perm_i)

        if len(other_cubes_l) > 1:
            found_d[i] = other_cubes_l

    return found_d


def buildCubesDict(f_range, stopValue):
    rv_d = dict()
    i = 1
    cube = 0

    while cube < stopValue:
        cube = i ** 3
        if f_range(cube):
            rv_d[i] = cube
        i += 1

    return rv_d


def main():
    def inRange(x):
        # currently, all the 9-digit numbers
        return 100_000_000 <= x <= 999_999_999

    cubes_d = buildCubesDict(inRange, stopValue=999_999_999)
    cubes_l = cubes_d.values()
    solutions = findCubes(cubes_d, inRange)

    print(solutions)
    print()
    for ls in solutions:
        print(ls)


if __name__ == '__main__':
    main()
    # print(f"isCube(216 ** 3) is: {isCube(216 ** 3)}")

# EOF

