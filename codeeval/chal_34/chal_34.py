#!/usr/bin/env python

import sys

"""
TEMPLATE
Solution for codeeval challenge #NN (TITLE)
https://www.codeeval.com/open_challenges/NN/

AUTHOR: Erik Johnson
DATE: 2016-Jun-
"""

def isPalindromic(n):
    if type(n) == int:
        s = str(n)
    else:
        s = n

    return all([s[i] == s[-i - 1] for i in xrange(len(s) / 2)])

def findPalindrome(s):
    if isPalindromic(s):
        return s

    i1 = int(s)

if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        i = line.rstrip()
        p = findPalindrome(i)
        lines_out.append("%s %s" % (i, p))

    print '\n'.join(lines_out)
    sys.stdout.flush()
