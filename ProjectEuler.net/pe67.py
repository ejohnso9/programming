#!/usr/bin/env python

import time

# ProjectEuler.net Problem #67
# https://projecteuler.net/problem=18
# Find the maximum total from top to bottom of the triangle below

# This is same problem with bigger data set as #18. See that file for
# discussion. The only real code difference is that this solution loads the
# data from a file rather than having textual data embedded within the
# source.

FILENAME = "p067_triangle.txt"

def read_and_parse_data(filename):
    fd = open(filename, 'r')
    data = fd.read()
    num_array = []
    for row in [line.split() for line in data.split('\n')]:
        num_array.append([int(x) for x in row])

    # there's one extra row because of the way the file ends:
    # drop that off
    return num_array[:-1]
    

def f67(data):
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

    # I estimated in pe18.py that this would be able to be solved in under 1
    # second. Is that really true?

    start = time.time()
    numArray = read_and_parse_data(FILENAME)
    data = f67(numArray)
    # print data
    print "sum of max data path is", data[0][0]
    print "solved in", time.time() - start, "seconds"

"""
Uhh... yeah. Quite true. Seems like something is getting cached that
helps this run much faster after the first run for a while. That may be
simply getting the python interpreter into cached memory and or disk.

But even on this "first" run, we are a just little over a 10th of a second,
and that includes reading an external file and parsing all the data,
converting to int, etc.

$ python pe67.py
sum of max data path is 7273
solved in 0.12505698204 seconds

$ python pe67.py
sum of max data path is 7273
solved in 0.00949621200562 seconds

$ python pe67.py
sum of max data path is 7273
solved in 0.00940704345703 seconds

$ python pe67.py
sum of max data path is 7273
solved in 0.00976300239563 seconds

"""
