#!/usr/bin/env python
"""
Solution for CodeEval challenge #197 (COLUMN NAMES)
https://www.codeeval.com/open_challenges/197/

AUTHOR: Erik Johnson
DATE: 2016-Oct-02

DISCUSSION:
    I get the feeling this is not the most clever solution. Maybe I am not thinking about
    this problem in quite the right way. It feels like there should be something a lot
    cleaner, but I'm not seeing it today. :(
"""

import sys, string

ABC = string.ascii_uppercase

def get_col_index(i):
    """convert integer column number to lettered index"""

    d0 = i % 26
    c0 = ABC[d0 - 1]

    if i <= 26:
        s = c0
    elif i <= 26 * 27: # 702
        d1 = (i - 1) / 26
        c1 = ABC[d1 - 1]
        c0 = ABC[(i % 26) - 1] # NB: -1 index OK here
        s = c1 + c0
    else:
        d2 = (i - 27) / (26 ** 2)
        c2 = ABC[d2 - 1]
        i -= d2 * (26 ** 2)
        d1 = (i - 1) / 26
        c1 = ABC[d1 - 1]
        s = c2 + c1 + c0
        
    return s


if __name__ == "__main__":
    lines_out = []

    for line in open(sys.argv[1], 'r'):
        lines_out.append(get_col_index(int(line.rstrip())))

    print '\n'.join(lines_out)
    sys.stdout.flush()

    # TEST DATA
    """
    DATA = [
    #   A B  Y  Z AA AB AY AZ BA BB BY BZ CA CB
        1,2,25,26,27,28,51,52,53,54,77,78,79,80,

    #   CY,  CZ, ..., YZ,  ZA,  ZZ
       103, 104,     676, 677, 702,
    
    #   AAA,  ELJ
        703, 3702,
    ]
    """
