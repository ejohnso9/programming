#!/usr/bin/env python
"""
Solution for codeeval challenge #150 (ROMAN AND ARABIC)
https://www.codeeval.com/open_challenges/150/

AUTHOR: Erik Johnson
DATE: 2016-Sep-27
"""

import sys

# GLOBAL DATA
# rank and value dict: key: (rank, value)
RV_D = {
    'I': (0,    1),
    'V': (1,    5),
    'X': (2,   10),
    'L': (3,   50),
    'C': (4,  100),
    'D': (5,  500),
    'M': (6, 1000),
}


if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        t_l = [] # list of tuples: (value, rank)
        line = line.rstrip()

        # make 1 tuple for every 2 char in line
        for i in xrange(len(line) / 2):
            c2 = line[i * 2: i * 2 + 2]
            a, r = int(c2[0]), c2[1] # arabic (int), roman (char)
            t_l.append( (a * RV_D[r][1], RV_D[r][0]) )

        total = 0
        n = len(t_l)
        for i in xrange(len(t_l) - 1):
            value = t_l[i][0]

            # this rank compared to next rank
            if t_l[i][1] < t_l[i + 1][1]:
                total -= value
            else:
                total += value

        # finally, always add last element
        total += t_l[len(t_l) - 1][0]

        lines_out.append(str(total))

    print '\n'.join(lines_out)
    sys.stdout.flush()
