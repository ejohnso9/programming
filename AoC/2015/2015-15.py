#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DESCRIPTION
    https://adventofcode.com/2015/day/14

--- Day 15: Science for Hungry People ---
Today, you set out on the task of perfecting your milk-dunking cookie
recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You
make a list of the remaining ingredients you could use to finish the
recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately,
and you have to be accurate so you can reproduce your results in the
future. The total score of a cookie can be found by adding up each of
the properties (negative totals become 0) and then multiplying together
everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of
cinnamon (because the amounts of each ingredient must add up to 100)
would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for
now) results in a total score of 62842880, which happens to be the best
score possible given these ingredients. If any properties had produced a
negative total, it would have instead become zero, causing the whole
score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the
total score of the highest-scoring cookie you can make?


DISCUSSION
    One core facet of this problem is partitioning. Unfortunately, I
don't see any standard function in itertools (or elsewhere). However,
Google is your friend, and there are many Python solutions out there.

    I found this one: 
https://stackoverflow.com/questions/18503096/python-integer-partitioning-with-given-k-partitions

    def part(n, k):
        def _part(n, k, pre):
            if n <= 0:
                return []
            if k == 1:
                if n <= pre:
                    return [[n]]
                return []
            ret = []
            for i in range(min(pre, n), 0, -1):
                ret += [[i] + sub for sub in _part(n-i, k-1, i)]
            return ret
        return _part(n, k, n)


STRATEGY

"""


# import pdb  # http://pymotw.com/2/pdb/

# GLOBAL DATA
NL = '\n'

DATA = """\
Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
"""

TEST_DATA = """\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


def lineToTuple(line):
    words = line.split()
    def fType(value, index):
        return int(value) if index in [3, 6, 13] else value
    return tuple([fType(words[i], i) for i in [0, 3, 6, 13]])


def part(n, k):
    def _part(n, k, pre):
        if n <= 0:
            return []
        if k == 1:
            if n <= pre:
                return [[n]]
            return []
        ret = []
        for i in range(min(pre, n), 0, -1):
            ret += [[i] + sub for sub in _part(n-i, k-1, i)]
        return ret
    return _part(n, k, n)


def main():

    for p in part(12, 3):
        print(p)


if __name__ == '__main__':
    main()

# EOF
