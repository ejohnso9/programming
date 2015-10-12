#!/usr/bin/env python

"""
Let's just brute-force this and whack through all the combinations
1000 ** 2 is only 1 million
"""

import sys, time

#
# GLOBAL DATA
#
SQ = [0] * 1001 # squares array

def find_magic_triplet():
    max = 1000
    for a in range(1, max + 1):
        for b in range(a + 1, max - a - 1):
            c = 1000 - a - b
            if SQ[a] + SQ[b] == SQ[c]:
                return (a, b, c)

    print "FAIL: done with a,b loop!"
    sys.exit(0)

def main():
    start_t = time.time()

    # let's avoid a bunch of squaring operations
    # init SQ data
    for i in range(1001):
        SQ[i] = i * i
    abc = find_magic_triplet()
    end_t = time.time()
    print "found", abc, "in", end_t - start_t


if __name__ == '__main__':
    main()

"""
WOW:
50
100
150
200
found (200, 375, 425) in 0.0439999103546
"""
