#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #50  (STRING SUBSTITUTION)
https://www.codeeval.com/open_challenges/50/

AUTHOR: Erik Johnson

DISCUSSION:
    Seems like a lot of these "HARD" problems belong in moderate or easy
groupings.

DEBUG = False
def debug(s):
    if DEBUG:
        print s
"""

def base26(n):
    """convert int to base-26 number w/ A => 0 (e.g., 678 = "BAC")"""
    if n == 0:
        #debug("base26(0) is: A")
        return "A"
    elif n < 26:
        return chr(n + 65)

    l = []

    while n > 0:
        rem = n % 26
        l.append(chr(rem + 65))
        n = (n - rem) / 26

    l.reverse()

    return ''.join(l)


if __name__ == "__main__":

    replDict = {}  # dict of patterns that were substituted
    replIndex = 0  # base-26 counter of replacements

    for line in open(sys.argv[1], 'r'):
        line = line.strip()
        #debug('line is: "%s"' % line)
        (s, pats) = [s2.strip() for s2 in line.split(';')]
        #debug('s is: "%s"' % s)
        pats = [s2.strip() for s2 in pats.split(',')]
        frList = []
        for i in xrange(len(pats) / 2):
            frList.append((pats[2 * i], pats[2 * i + 1]))
        #debug(str(frList))

        # replace each find pattern w/ each replacement pattern, finding
        # single occurences scanning from left
        for (fpat, rpat) in frList:
            tup = (fpat, rpat)
            #debug("processing: %s" % str(tup))
            idx = s.find(fpat)  # returns -1 if not found
            #debug('"%s".find("%s") = %d' % (s, fpat, idx))
            if idx > -1:
                l = len(fpat)
                #debug("before replacement:")
                #debug("\ts: " + s)

                # make temp replacement
                replKey = '[' + base26(replIndex) + ']'
                replDict[replKey] = rpat
                replIndex += 1
                # s = s[:idx] + replKey + s[idx + l:]
                s = s.replace(fpat, replKey)

                # s2 = s2[:idx] + rpat + s2[idx + l:]
                #debug("after replacement:")
                #debug("\ts: " + s)
                #debug("")

        # substitute the replKey's back with the original replacement
        # patterns
        for key in replDict:
            s = s.replace(key, replDict[key])

        print s

