#!/usr/bin/env python3

"""
DESCRIPTION
    Kattis problem at:
        https://open.kattis.com/problems/heimavinna

AUTHOR
    Erik Johnson

HISTORY
    2020Dec18  Accepted first submit.
"""

import sys

# GLOBAL DATA
dash, semi = '-', ';'

def process(line):
    total = 0
    for word in line.split(semi):
        if word.find(dash) > -1:
            a, b = [int(x) for x in word.split(dash)]
            total += b - a + 1
        else:
            total += 1

    return total

def main():
    rv = process(sys.stdin.readline().strip())
    print(str(rv))


if __name__ == '__main__':
    main()
