#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #1  (Fizz Buzz)
https://www.codeeval.com/open_challenges/1/

AUTHOR: Erik Johnson

DISCUSSION:
    I'm not even sure why I am doing this one... Seems inanely simple.
Maybe that's why?

Anyway: 3 ints per line of input: X, Y, Nmax
Start at 1 and count up to Nmax (inclusive), printing the numbers spearated
by one space with the following substitutions:
    n % X == 0 and n % Y == 0: print print "FB"
    n % X == 0 : print print "F"
    n % Y == 0 : print print "B"

About the only thing interesting thing going on here that I can see
is the potential for optimization. X and Y are both advertized to be in
range [1, 20] and N is in range [21, 100].  Thats only 20 * 20 = 400
combinations of [X, Y] params. Those strings could be pre-computed, and
simply dumped into a dict. Actually, because of the N parameter, you
wouldn't want to store the string, but you could certainly store the
data arrays, and just join a list and print it.

Maybe I will toy with that after getting an accepted solution just to
see what happens to the speed score value.

"""

if __name__ == "__main__":

    for line in open(sys.argv[1], 'r').readlines():
        opList = [] # will go into final answer
        (X, Y, N) = [int(s) for s in line.split()]

        # split the line into a list of month ranges
        for n in xrange(1, N + 1):
            if (n % X == 0) and (n % Y == 0):
                el = "FB"
            elif n % X == 0:
                el = "F"
            elif n % Y == 0:
                el = "B"
            else:
                el = str(n)

            opList.append(el)

        # one line of output per line of input
        print ' '.join(opList)
    
