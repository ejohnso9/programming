#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #104 (WORD TO DIGIT)
https://www.codeeval.com/open_challenges/104/

AUTHOR: Erik Johnson
DATE: 2015-MAR-03

DISCUSSION:
    Not much to discuss.
"""

if __name__ == "__main__":

    # init word => char conversion dict
    num_d = {}
    words = "zero one two three four five six seven eight nine".split()
    for i in xrange(10):
        num_d[words[i]] = str(i)

    for line in open(sys.argv[1], 'r'):
        print ''.join([num_d[word] for word in line.strip().split(';')])

