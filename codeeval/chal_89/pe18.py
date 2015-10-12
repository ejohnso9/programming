"""
Corporate Plagiarism! codeeval challenge #89
is ProjectEuler.net Problem #18
https://www.codeeval.com/open_challenges/89/
https://projecteuler.net/problem=18
"""

import sys

def parse_data(fd):
    num_array = []
    for row in [line.split() for line in fd.readlines()]:
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
    fd = open(sys.argv[1], 'r')
    numArray = parse_data(fd)
    data = f18(numArray)
    print data[0][0]


