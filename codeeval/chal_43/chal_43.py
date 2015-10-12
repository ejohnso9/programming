#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #43 (JOLLY JUMPERS)
https://www.codeeval.com/open_challenges/43/

AUTHOR: Erik Johnson
DATE: 2015-MAR-03

DISCUSSION:
    I haven't used all() and any() much, but those are the sorts of
very handy things you get with a language like Python.
"""

if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        nums = [int(x) for x in line.strip().split()]
        N = nums[0]
        #print nums
        #print "N is", N
        tfList = [False] * (N - 1)
        oob = False
        for i in xrange(1, N):
            # print "i is", i
            diff = abs(nums[i] - nums[i + 1])
            if diff > N - 1:
                oob = True
                break
            tfList[diff - 1] = True
        # print tfList
        if oob:
            print "Not jolly"
        else:
            print "Jolly" if all(tfList) else "Not jolly"

"""
Traceback (most recent call last):
  File "<tmp>/source.py", line 29, in <module>
      tfList[diff - 1] = True
      IndexError: list assignment index out of range
"""
