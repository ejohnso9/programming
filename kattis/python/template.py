#!/usr/bin/env python
# Python 2.7

"""
https://open.kattis.com/problems/parsinghex
2019Mar16
"""

import sys, re

hex = re.compile(r'0x[0-9a-f]+')

def processLine(line, opAcc):
    s_lc = line.lower()
    for s in hex.findall(s_lc):
        idx = s_lc.find(s)
        s_orig = line[idx: idx + len(s)]
        opAcc.append('{} {}'.format(s_orig, int(s, 16)))

# main
opAcc = [] # output accumulator
for line in sys.stdin.readlines():
    processLine(line, opAcc)

print '\n'.join(opAcc)
