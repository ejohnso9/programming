#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #139
https://www.codeeval.com/open_challenges/139/

AUTHOR: Erik Johnson

DISCUSSION:
    So, the output from the sample problem looks like the years expected
is integer floor function of number of years. So, for example:

Feb 2004-May 2004; Jun 2004-Jul 2004

is computed as 0 years. Feb through May would be 4 months, then Jun &
July would be another 2 months.


Under Python 2 you can simply do integer arithmetic as:

>>> 6 / 12
0

Under Python 3, things are substantially different!:

>>> 6 / 12
0.5

Looks like codeeval invokes the interpreter based on the file extension
of your submission, so filename should be named something like
mysolution.py2 or mySolution.py3

APPROACH:
    So, seems to me a rather simple approach is to just set keys in a
native dict representing the months covered in an experience range. If
you set the same month multiple times, it is net effect of NOOP: exactly
what is needed here.

    At the end, you just do integer division on the number of months in
the dict, which is len(d).
"""

if __name__ == "__main__":

    expYears = [] # final answer
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

    for line in open(sys.argv[1], 'r').readlines():
        expMonths = {}

        # split the line into a list of month ranges
        for moRange in [s.strip() for s in line.split(';')]:
            # print moRange
            # break up the month range into beginning (month, year) and
            # ending (month, year)
            (startRange, endRange) = moRange.split('-')
            (startMo, startYr) = startRange.split()
            (endMo, endYr) = endRange.split()

            # convert string data to int type
            startMo_i = months.index(startMo) + 1 # 'Jan' => 1
            endMo_i   = months.index(endMo) + 1
            startYr_i = int(startYr)
            endYr_i   = int(endYr)

            # just iterate over month and years, setting keys in
            # 'expMonths' dict
            yrSpan = endYr_i - startYr_i

            # CASE 1: range within same year
            if yrSpan == 0:
                # just iterate months
                yr = startYr_i
                for mo in xrange(startMo_i, endMo_i + 1):
                    expMonths[(mo, yr)] = True

            # CASE 2: range spanning 1 or more years
            # for yr in xrange(startYr_i, endYr_i + 1):
            else:
                # start mo to Dec of first year
                yr = startYr_i
                for mo in xrange(startMo_i, 13):
                    expMonths[(mo, yr)] = True

                # all 12 months in each whole year span
                for yr in xrange(startYr_i + 1, endYr_i):
                    for mo in xrange(1, 13):
                        expMonths[(mo, yr)] = True

                # Jan to end mo of last year
                yr = endYr_i
                for mo in xrange(1, endMo_i + 1):
                    expMonths[(mo, yr)] = True

        # add a year answer to answer list
        expYears.append(len(expMonths) / 12)

    # final answer output
    print '\n'.join([str(x) for x in expYears])

