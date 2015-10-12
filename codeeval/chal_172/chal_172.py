#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #NN (NAME)
https://www.codeeval.com/open_challenges/NN/

AUTHOR: Erik Johnson
DATE: 2015-MAR-03

DISCUSSION:
"""

def f(d):
    """sum of digits if d > 9"""
    if d > 9:
        return sum([int(c) for c in str(d)])

    return d


if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        line = ''.join(line.strip().split())
        digits = [int(d) for d in line]
        l2 = []
        for i in xrange(1, len(digits) + 1):
            if i % 2 == 0:
                l2.append(f(2 * digits[-i]))
            else:
                l2.append(digits[-i])
        print 1 if (sum(l2) % 10 == 0) else 0

