#!/usr/bin/env python
# Python 3 (dev under Python 3.6.1)

"""
2019Apr24

https://open.kattis.com/problems/anagramcounting
"""

import sys, math
import operator
from functools import reduce
import pdb

def nAnagrams(s):
    n = len(s)
    d = {}
    for c in list(s):
        if not c in d.keys():
            d[c] = 1
        else:
            d[c] += 1

    # build list of non-1 counts
    l = []
    for c, count in d.items():
        if count > 1:
            l.append(count)
        
    if len(l):
        # this branch only needed if 's' has repeated symbols
        l = map(math.factorial, l)
        denom = reduce(operator.mul, l, 1)
        rv = int(math.factorial(n) / denom)
    else:
        rv = math.factorial(n)

    return rv

#
# main
#

# TEST branch
if False:
    los = [
        "at",
        "ordeals",
        "abcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmabcdefghijklm",
        "abcdABCDabcd", ]

    for s in los:
        print(nAnagrams(s))

    # should output(cut from Kattis' web page)
    """
    2
    5040
    403291461126605635584000000
    49229914688306352000000
    29937600
    """

# "production" branch
else:
    s = sys.stdin.readline().rstrip()
    print(nAnagrams(s))


