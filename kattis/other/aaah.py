#!/usr/bin/env python
# Python 2.7

"""
aaah: https://open.kattis.com/problems/aaah
2019Mar16
"""

import sys

# main
lines = sys.stdin.readlines()
if len(lines[0]) >= len(lines[1]):
    print "go"
else:
    print "no"
