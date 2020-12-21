#!/usr/bin/env python
# Python 2.7

"""
https://open.kattis.com/problems/planina
2019Mar17

The relationship of numbers on one side is: 2^n + 1
@see: https://oeis.org/A000051
"""

import sys

# main
n = int(sys.stdin.readline())
print (2 ** n + 1) ** 2
