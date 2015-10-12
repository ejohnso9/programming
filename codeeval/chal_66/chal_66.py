#!/usr/bin/env python

import sys
import pdb

"""
Solution for codeeval challenge #66 (PASCALS TRIANGLE)
https://www.codeeval.com/open_challenges/66/

AUTHOR: Erik Johnson

DISCUSSION:
1
1  1
1  2   1
1  3   3   1
1  4   6   4   1
1  5  10  10   5   1
"""

def pascal(n):
    """construct Pascal triangle to depth n as list of lists"""
    m = [] # triangular matrix we will build here
    # pdb.set_trace()
    for r in xrange(n):
        row = [1] * (r + 1)
        m.append(row)
        if r >= 2:
            prevRow = m[r - 1]
            for c in xrange(1, r):
                row[c] = prevRow[c - 1] + prevRow[c]

    return m


if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        m = pascal(int(line.strip()))

        # output
        l = []
        for row in m:
            l.extend(row)
        print ' '.join([str(i) for i in l])

