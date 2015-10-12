#!/usr/bin/env python

import sys, pdb

"""
Solution for codeeval challenge #12 (FIRST NON-REPEATED CHARACTER)
https://www.codeeval.com/open_challenges/12/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":

    out_lines = []

    for line in open(sys.argv[1], 'r'):
        line = line.rstrip()
        found = False
        n = len(line)
        d = {}

        # record the counts
        for i in xrange(len(line)):
            c = line[i]
            if d.has_key(c):
                d[c] += 1
            else:
                d[c] = 1

        # now, find first char with count == 1
        for i, c in enumerate(line):
            if d[c] == 1:
                found = True
                break

        if not found:
            c = ''

        out_lines.append(c)
        
    print '\n'.join(out_lines)

