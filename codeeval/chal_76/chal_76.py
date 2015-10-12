#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #NN (NAME)
https://www.codeeval.com/open_challenges/NN/

AUTHOR: Erik Johnson
DATE: 2015-MAR-07

DISCUSSION:
    I suspect that doing the slicing and one concatenation is
substantially faster than re-assigning to a variable on every iteration,
though I have not benchmarked that.
"""


if __name__ == "__main__":

    op = []
    for line in open(sys.argv[1], 'r'):
        (w1, w2) = [w.strip() for w in line.split(',')]
        match = False
        for i in xrange(len(w2)):
            if w1 == w2[i:] + w2[:i]:
                match = True
                break
        op.append(match)

    print '\n'.join([str(tf) for tf in op])

