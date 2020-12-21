#!/usr/bin/env python

"""
DESCRIPTION
    2019May21
    Old code off my RC computer. This should have link to problem, etc.
    I know the CodinGame site, but haven't done anything there for a
    long time.
"""

import sys, math

def bitRep(c):
    return ''.join([str(int(ord(c) & 2**i > 0)) for i in xrange(6, -1, -1)])

def rle(s):
    c = s[0]
    count = 1
    l = []
    for i in xrange(1, len(s)):
        if s[i] == c:
            count += 1
        else:
            l.append((count, c))
            count = 1
            c = s[i]
    l.append((count, c))
    return l


