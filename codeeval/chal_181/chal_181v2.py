#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #181 (GRONSFELD CIPHER)
https://www.codeeval.com/open_challenges/181/

AUTHOR: Erik Johnson

DISCUSSION:
"""

DATA = ' !"#$%&\'()*+,-./0123456789:<=>?@'\
    + 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

l = len(DATA)
for line in open(sys.argv[1], 'r'):
    digs, s = line.strip().split(';')
    print ''.join(
        DATA[(DATA.index(e) - int(i) + l) % l]
        for i, e in zip(digs * ((len(s) / len(digs)) + 1), s)
    )
