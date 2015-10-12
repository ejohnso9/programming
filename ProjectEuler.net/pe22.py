#!/usr/bin/env python

import operator

# ProjectEuler.net Problem #22
# https://projecteuler.net/problem=22
# Read the file p022_names.txt, sort, then compute f(name) where
# f(name) is sum of letter values * index in sorted list

def nameScore(name):
    letterScores = [ord(c) - ord('A') + 1 for c in list(name)]
    score = sum(letterScores)
    if (DEBUG):
        print letterScores
        print "nameScore(%s) = %i" % (name, score)
    return score
    
def readNames(filename):
    fd = open(filename)
    # parse CSV, strip quotes
    data = fd.read().strip()
    return [s[1:-1] for s in data.split(',')]

def f22(names):
    total = 0
    scores = map(nameScore, names)
    for i in xrange(len(names)):
        #print "score", i, "is", scores[i]
        total += (i + 1) * scores[i]
        #print "total:", total

    return total


if __name__ == '__main__':

    DEBUG = False

    FILENAME = 'p022_names.txt'
    # FILENAME = 'p022_test.txt'

    names = readNames(FILENAME)
    names.sort()
    answer = f22(names)
    print "answer is: ", answer

