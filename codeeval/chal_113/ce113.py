#!/usr/bin/env python

import sys

"""
TEMPLATE
Solution for codeeval challenge #113 (MULTIPLY LISTS)
https://www.codeeval.com/open_challenges/113/

AUTHOR: Erik Johnson
DATE: 2016-Sep-26
"""

if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        s1, s2 = line.rstrip().split('|')
        l = []
        l1 = [int(s) for s in s1.split()]
        l2 = [int(s) for s in s2.split()]

        for i in range(len(l1)):
            l.append(str(l1[i] * l2[i]))

        lines_out.append(' '.join(l))

    print '\n'.join(lines_out)
    sys.stdout.flush()
