#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #32 (TRAILING STRING)
https://www.codeeval.com/open_challenges/32/

AUTHOR: Erik Johnson

DISCUSSION:
    I lose some points by using Python on problems like these because
it takes almost 4M to host the Python interpreter, putting the memory
factor at like 80% and this problem ran at 108 ms after submitting it,
whereas I was getting 1 ms for some other problems of similar complexity
in C.

    However, I think this is one of the strongest arguments around for
using a language like Python. The logic for this problem is trivial in
Python. It's not a tough problem in C, but it would take significantly
longer to code, and the development is significantly more error prone in
a language like C. And what would you gain? Well, in terms of runtime
you save 107 ms.

    Is that worth it? That all depends on how much you need to run a
program like this. In this case, there are plenty of other problems I
can go on and solve in Python. Later, I could come back and do this
problem in C and try to pick up the difference between the theoretical
65 point max, and the 57.637 that I actually scored for this Python
solution. Is it worth it? No. In this case, absolutly not, not until
I've solved all available problems, and that's not likely to happen any
time soon. Until then, it is much easier to score another 50+ points on 
other "moderate" problems.

    I think this discussion of tradeoffs is pretty applicable to
software development in the real world. Generally better to produce a
working prototype in a language like Python first. Then, if you find the
software is correct, but just too slow, you can either optimize your
Python solution, or put part of it into C-library calls, or rewrite the
whole thing in Python. You may find that Python is plenty fast as it is.

    The other route is to use a language such as C because you think it
really needs to be fast, and pay all the additional costs of developing
in C up front. And then, you have no second system to compare against. I
think generally, using a language such as Perl/Python/Ruby, etc. is the
better route.

    And this is part of the reason I think Python is a great language to
use.
"""

if __name__ == "__main__":

    opList = []  # lines of final answer output
    for line in open(sys.argv[1], 'r'):
        (a, b) = line.strip().split(',')
        answer = '1' if a.endswith(b) else '0'
        opList.append(answer)

    print "\n".join(opList)

