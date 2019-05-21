#!/usr/bin/env python

import sys

oneCount_d = { 
    '0': 0, '1': 1, '2': 1, '3': 2,
    '4': 1, '5': 2, '6': 2, '7': 3,
    '8': 1, '9': 2, 'a': 2, 'b': 3,
    'c': 2, 'd': 3, 'e': 3, 'f': 4
}

for line in open(sys.argv[1], 'r'):
    print sum([oneCount_d[c] for c in "%x" % int(line)])


