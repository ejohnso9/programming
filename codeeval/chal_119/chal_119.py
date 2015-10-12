#!/usr/bin/env python

import sys, pdb

"""
Solution for codeeval challenge #119 (CHAIN INSPECTION)
https://www.codeeval.com/open_challenges/119/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        # load dict
        d = {}
        pairs = line.strip().split(';')
        n = len(pairs)
        for pair in pairs:
            k, v = pair.split('-')
            d[k] = v

        # check chain
        k = 'BEGIN'
        next_k = d[k]
        # pdb.set_trace()
        for hop in xrange(1, n):
            next_k = d[next_k]
            if next_k == 'END':
                break # should have made hop # of steps to next link

        if next_k == 'END' and hop == n - 1:
            out = 'GOOD'
        else:
            out = 'BAD'
        lines_out.append(out)

    print '\n'.join(lines_out)
    sys.stdout.flush()
