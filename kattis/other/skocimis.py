#!/usr/bin/env python
# Python 2.7

"""
https://open.kattis.com/problems/skocimis
2019Mar16
"""

import sys

# main
for line in sys.stdin.readlines():
    a, b, c = [int(x) for x in line.split()]
    if b - a > c - b:
        print b - a - 1
    else:
        print c - b - 1
