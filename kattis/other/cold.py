#!/usr/bin/env python
# Python 2.7

"""
cold: https://open.kattis.com/problems/cold
2019Mar16
    
data like:
3
5 -10 15

DESC:
    N on first line
    print count of elements strictly < 0
"""

import sys


# main
lines = sys.stdin.readlines()
nums = [int(x) for x in lines[1].split()]
print len(filter(lambda x: x < 0, nums))
