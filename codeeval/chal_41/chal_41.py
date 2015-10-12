#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #41 (ARRAY ABSURDITY)
https://www.codeeval.com/open_challenges/41/

AUTHOR: Erik Johnson
DATE: 2015-MAR-07

DISCUSSION:
    Not much to say about this one.
"""


if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        line = line.strip()
        (N, nums) = line.split(';')
        N = int(N)
        tfList = [False] * (N - 1)
        iList = [int(x) for x in nums.split(',')]
        for i in iList:
            if tfList[i]:
                print i
            else:
                tfList[i] = True

