#!/usr/bin/env python
"""
Solution for codeeval challenge #11 (LOWEST COMMON ANCESTOR)
https://www.codeeval.com/open_challenges/11/

AUTHOR: Erik Johnson
DATE: 2016-Sep-28

DISCUSSION:
There are very few nodes. I'm simply going to define a hash with keys of
ordered tuples to hold each possible answer. This may not be the fastest
possible, but it's simple, and it's likely to be the difference between
like 12ms and 14ms or so (based on times I have recently been getting on
other solutions).

I am assuming there will be no 30 (root value) in the input data.

OK, bad assumption. I have only achieved a partial solution because
input includes things like this line:
3 30

That's nonsensical as far as I am concerned. Root nodes have no
ancestor and so it makes no sense to ask about the lowest common
ancestor of your root and something else. There is nothing in common
between nothing and anything else.

Roots are not ancestors of themselves in the same way that leaves are
not children of themselves in the same way that it makes no sense for a
person to be their own parent or their own child.

The problem is simply bad.
"""

import sys

D = {
    ( 3,  8):  "8", ( 3, 10):  "8", ( 3, 20):  "8", ( 3, 29):  "8", ( 3, 52): "30",
    ( 8, 10):  "8", ( 8, 20):  "8", ( 8, 29):  "8", ( 8, 52): "30",
    (10, 20): "20", (10, 29): "20", (10, 52): "30",
    (20, 29): "20", (20, 52): "30",
    (29, 52): "30",
}

# map all the ints to the nearest node value
I_ARRAY = [
   # 0   1   2   3   4   5   6   7   8   9, 
     3,  3,  3,  3,  3,  3,  3,  3,  8, 10,
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    20, 29, 29, 29, 29, 29, 29, 29, 29, 29,
    30, # > 30: 52
]

def map_input(i):
    if i < 8:
        return 3
    elif i > 30:
        return 52
    else:
        return I_ARRAY[i]


if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        x, y = [int(s) for s in line.rstrip().split()]
        if x == y:
            value = str(x)
        elif x == 30 or y == 30:
            value = "30"
        else:
            if x > y:
                temp = x
                x = y
                y = temp
            x = map_input(x)
            y = map_input(y)
            value = D[(x,y)]

        lines_out.append(value)

    print '\n'.join(lines_out)
    sys.stdout.flush()
