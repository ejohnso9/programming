#!/usr/bin/env python

# from math import log, ceil

# ProjectEuler.net Problem #18
# https://projecteuler.net/problem=18
# Find the maximum total from top to bottom of the triangle below

"""
APPROACH DISCUSSION
    As the problem states, you may be able to evaluate all the paths in
this problem, but #67 is the same deal but with 100 layers in the
triangle. The number of combinations in this problem is 2^(N-1) where N
is the number of layers in the data triangle.

>>> 2**14
16384
>>> 2**99
633825300114114700748351602688L


    No matter - evaluating all the paths is not a very smart approach.
Let's look at their sample data:

   3
  7 4
 2 4 6
8 5 9 3

which could just as well be:

3
7 4
2 4 6
8 5 9 3

In this representation, a node has it's children just below it and below
and to the right. Let's just reduce the triangle a row at a time,
replacing the parent node with the sum of it's own value and 
max(LHC, RHC)  (where LHC => left-hand child).

So, for example, the 6 in row 3 becomes 6 + max(9, 3) = 15
 3
 7 4
10 13 15

again:

 3
20 19

and once more:

23

The given sample answer, equivalent to the path 3-7-4-9. Easy as pie.

I'd estimate the 15 row triangle can be solved in less than 0.25s and
the 100-row triangle in less than a second. Let's see...
"""

DATA_SAMPLE = """\
3
7 4
2 4 6
8 5 9 3\
"""

DATA = """\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23\
"""


def parse_data(data):
    num_array = []
    for row in [line.split() for line in data.split('\n')]:
        num_array.append([int(x) for x in row])

    return num_array
    

def f18(data):
    """input is 2D array of ints (triangular array)"""
    # process rows bottom up
    for i in xrange(len(data) - 2, -1, -1):
        (thisRow, nextRow) = (data[i], data[i + 1])
        for j in xrange(len(thisRow)):
            (lhc, rhc) = (nextRow[j], nextRow[j + 1])
            maxChild = max(lhc, rhc)
            # print "max of", lhc, "and", rhc, "is", maxChild
            thisRow[j] += maxChild
            # print "this is now", thisRow[j]

    return data


if __name__ == '__main__':
    numArray = parse_data(DATA) # DATA_SAMPLE)
    data = f18(numArray)
    # print data
    print "sum of max data path is", data[0][0]

