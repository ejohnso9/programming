#!/usr/bin/env python

import sys, re, string

"""
Solution for codeeval challenge #31 (RIGHTMOST CHAR)
https://www.codeeval.com/open_challenges/31/

AUTHOR: Erik Johnson

DISCUSSION:
    I took a shortcut here. You can make your own determination about whether this
is "cheating". I think it is resourcefulness and a case of applying my overall
knowledge to a problem...

    I did not solve this problem from first mathematical principles. The problem
statement gives the first three values to the series and I have known about OEIS for
quite some time. So, putting the first three values into the OEIS search bar
immediately turns up: https://oeis.org/A174061

    I also happen to own a copy of Mathematica, and so it is trivial to turn this:

Table[Total[ CoefficientList[Series[((1 - x^10)/(1 - x))^n, {x, 0, 9*n}], x]^2],
    {n, 0, 15}]

into this:

Table[Total[ CoefficientList[Series[((1 - x^10)/(1 - x))^n, {x, 0, 9*n}], x]^2],
    {n, 2, 50}]

which is L, below. If one is pretty sharp with math, they may be able to derive the
given FORMULA on the OEIS page, but I don't think anybody is going to be running
through the integers of a 100 digit number and checking for which ones the sum of
the first 50 digits equals the sum of the last 50 digits, so this problem more or
less demands that you go research the problem. I did that (in an efficient manner)
and provided a working solution (in an efficient manner).

    If you want to check whether I know how, off the top of my head, to derive this
forumula:

a(n) = Sum_{k = 0,1,2,...,n-1} (-1)^k Binomial(2n,k)Binomial(11n-1-10k,2n-1)
    a(n) is the coefficient of x^(9n) in the expansion of ((1 - x^10)/(1 - x))^(2n)

the answer is "No, I don't. I could research it, but I'm not going to now."
"""

# why even keep these as numbers? We're going to be printing strings.
L = [            # N (string length), index in this list = (N / 2) - 1
    "10",        #  2, 0
    "670",       #  4, 1
    "55252",     #  6, 2
    "4816030",   #  8, 3
    "432457640", # 10, 4
    "39581170420",
    "3671331273480",
    "343900019857310",
    "32458256583753952",
    "3081918923741896840", # 20
    "294056694657804068000",
    "28170312778225750242100",
    "2707859169387181467852100",
    "261046730157780861858821136",
    "25228791861003454642059261392", # 30
    "2443553412892220489195278947230",
    "237126779700111728623210793896700",
    "23050391247812238203687824747157800",
    "2244066255357188250744344225634235600",
    "218768894829904122626725603838896148680", # 40
    "21353575263502884630388273714197145182600",
    "2086610157206763614866736016835099941514800",
    "204105559167234718098196864419783302549632800",
    "19983598742087310057357815311872236715171970100",
    "1958235988893910037740658552689739094876481545140", # 50
]

if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        i = (int(line.strip()) / 2) - 1
        lines_out.append(L[i])

    print '\n'.join(lines_out)
