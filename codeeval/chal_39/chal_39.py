#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #39 (HAPPY NUMBERS)
https://www.codeeval.com/open_challenges/39/

AUTHOR: Erik Johnson
DATE: 2015-JUN-12

DISCUSSION:
    f(i+1) = sum(each digit squared in i)
    e.g., i0 = 7 gives: [7, 49, 97, 130, 10, 1]  # a happy number
    NOT HAPPY: 22->8->64->52->29->85->89->145->42->20->4->16->37->58->89
"""

#
# GLOBAL DATA
#

# squaring is expensive - let's not do much
SQ = [0] * 10  # SQ[i] = i^2 
for i in range(10):
    SQ[i] = i * i

#
# CLASSES
#

class BadFlow(Exception):
    """flow of control problem"""
    pass


#
# FUNCTIONS
#

def is_happy(i):
    """predicate for happy or not"""

    d = {} # dict of answers already found
    ans = i

    while True:
        digits = [int(c) for c in list(str(ans))]
        ans = sum([SQ[i] for i in digits])

        if ans == 1:
            return True
        elif d.has_key(ans):
            return False

        d[ans] = True

    raise BadFlow()


# MAIN
if __name__ == "__main__":

    answers = []
    for line in open(sys.argv[1], 'r'):
        i = int(line.strip())

        # compute an answer per input line
        if is_happy(i):
            result = "1"
        else:
            result = "0"

        answers.append(result)

    # dump all the output in one print call
    print '\n'.join(answers)


