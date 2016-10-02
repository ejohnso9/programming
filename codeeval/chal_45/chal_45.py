#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #45 (REVERSE AND ADD)
https://www.codeeval.com/open_challenges/45/

AUTHOR: Erik Johnson
DATE: 2016-May-26
"""

def isPalindrome(s):

    return all([s[i] == s[-i - 1] for i in xrange(len(s) / 2)])


def find_palindrome(i_s, count=0):
    if isPalindrome(i_s):
        return (count, i_s)

    # add int to its reverse and recursively call
    l = list(i_s)
    l.reverse()
    i1 = int(i_s)
    i2 = int(''.join([str(c) for c in reversed(i_s)]))
    new_s = str(i1 + i2)

    return find_palindrome(new_s, count + 1)


if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        i_s = line.rstrip()
        (count, p) = find_palindrome(i_s)
        lines_out.append("%s %s" % (count, p))

    print '\n'.join(lines_out)
    sys.stdout.flush()
