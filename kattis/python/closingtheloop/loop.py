#!/usr/bin/env python3

"""
DESCRIPTION
    https://open.kattis.com/contests/x4dmg8/problems/closingtheloop

AUTHOR
    Erik Johnson

HISTORY
    2020Dec19  Created
"""

import sys

# GLOBAL DATA
NL = '\n'

def process(line):
    e_l = line.split()  # element list

    red = [int(e[:-1]) for e in e_l if e[-1] == 'R']
    red.sort()
    red.reverse()

    blue = [int(e[:-1]) for e in e_l if e[-1] == 'B']
    blue.sort()
    blue.reverse()

    m = min(len(red), len(blue))

    return sum(red[:m]) + sum(blue[:m]) - (2 * m)


def output(answers):
    print(NL.join(
        [f'Case #{i+1}: {a}' for i, a in enumerate(answers)] ))


def main():
    answers = []
    fd = sys.stdin
    n_cases = int(fd.readline().strip())
    for case_i in range(n_cases):
        ignore = fd.readline()
        line = fd.readline().strip()
        answers.append(process(line))

    output(answers)


if __name__ == '__main__':
    main()

