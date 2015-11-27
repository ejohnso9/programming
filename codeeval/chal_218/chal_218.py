#!/usr/bin/env python

import sys, re, string

"""
Solution for codeeval challenge #218 ()
https://www.codeeval.com/open_challenges/218/

AUTHOR: Erik Johnson

DISCUSSION:
    So, here's my general approach...

    Nodes are number 1-25 in a regular 5x5 matrix left to right, top to
bottom. Let's call a connection between two nodes a "link". There are 16
possible 1x1 squares, 9 possible 2x2 squares, 4 possible 3x3 squares,
and one possible 4x4 square.

    Let's just build a list of lists, where the inner list elements are
just the links required to build that square. For example, the 1x1
square starting with upper lefthand corner of 1 would be"

    ['1-2', '1-6', '2-7', '6-7']

    Python supports arbitrary things as dict keys, not only strings, so
it could be tuples instead of dashed strings, but I think strings as
dict key is intuitive and also translates directly to JavaScript (which
does NOT support object keys of things like lists, other objects, etc.)

    NOTE: One important porperty is that the links should be ordered
since the order in the problem statement seems to be arbitrary. For
example, one such link from the exmaple is given as "7 2". If you
evaluate the dict for key "2-7", it would not be present.

    I'm going to write some functions to help me generate the lists as
above (because I am too lazy to do it by hand), print them and then
that is just a static data structure in my program (i.e., that code
doesn't run during problem solution evalaution). 

    To evaluate the solution, I simply read off the links we've got,
throw those into a dict, then go down the list of 16 + 9 + 4 + 1 = 30 
square definitions and see which ones we've got the requisite links 
to "build".

    That's my plan.
"""

# build the link list for 1x1 square starting at i
def square1(i):
    return [
        # just go clockwise to make this regular
        '%i-%i' % (i, i + 1),
        '%i-%i' % (i, i + 5),
        '%i-%i' % (i + 1, i + 6),
        '%i-%i' % (i + 5, i + 6),
    ]

def square2(i):
    return [
        # just go clockwise to make this regular
        '%i-%i' % (i, i + 1),
        '%i-%i' % (i + 1, i + 2),

        '%i-%i' % (i + 2 + 0, i + 2 + 5),
        '%i-%i' % (i + 2 + 5, i + 2 + 10),

        '%i-%i' % (i + 1 + 10, i + 2 + 10),
        '%i-%i' % (i + 0 + 10, i + 1 + 10),

        '%i-%i' % (i + 5, i + 10),
        '%i-%i' % (i, i + 5),
    ]

def square3(i):
    # this one doesn't build clockwise. Maybe should have done them all
    # like this one.
    l = []
    k = i + 15
    for j in range(3):
        l.append('%i-%i' % (i + j, i + j + 1))
        l.append('%i-%i' % (k + j, k + j + 1))

    for k in [0, 5, 10]:
        x = i + k
        l.append('%i-%i' % (x, x + 5))

def square4():
    s = ' '.join([
        "1-2 2-3 3-4 4-5",
        "5-10 10-15 15-20 20-25",
        "24-25 23-24 22-23 21-22",
        "16-21 11-16 6-11 1-6"
    ])

    return [str(x) for x in s.split()]
        
def build_1x1_squares():
    l = []
    for j in range(1, 16 + 1, 5):
        for i in range(4):
            l.append(square1(j + i))

    return l

def build_2x2_squares():
    l = []
    for j in range(1, 11 + 1, 5):
        for i in range(3):
            l.append(square2(j + i))

    return l

def build_3x3_squares():
    l = []
    for j in range(1, 5 + 1, 5):
        for i in range(2):
            l.append(square3(j + i))

    return l

def main():
    squares = build_1x1_squares()
    # squares = build_2x2_squares()
    for sq_l in squares:
        print sq_l
    print square4()

LINKS = [
    # 1x1 squares
    ['1-2',   '1-6',   '2-7',   '6-7'],
    ['2-3',   '2-7',   '3-8',   '7-8'],
    ['3-4',   '3-8',   '4-9',   '8-9'],
    ['4-5',   '4-9',   '5-10',  '9-10'],

    ['6-7',   '6-11',  '7-12',  '11-12'],
    ['7-8',   '7-12',  '8-13',  '12-13'],
    ['8-9',   '8-13',  '9-14',  '13-14'],
    ['9-10',  '9-14',  '10-15', '14-15'],

    ['11-12', '11-16', '12-17', '16-17'],
    ['12-13', '12-17', '13-18', '17-18'],
    ['13-14', '13-18', '14-19', '18-19'],
    ['14-15', '14-19', '15-20', '19-20'],

    ['16-17', '16-21', '17-22', '21-22'],
    ['17-18', '17-22', '18-23', '22-23'],
    ['18-19', '18-23', '19-24', '23-24'],
    ['19-20', '19-24', '20-25', '24-25'],

    # 2x2 squares
    ['1-2', '2-3', '3-8', '8-13', '12-13', '11-12', '6-11', '1-6'],
    ['2-3', '3-4', '4-9', '9-14', '13-14', '12-13', '7-12', '2-7'],
    ['3-4', '4-5', '5-10', '10-15', '14-15', '13-14', '8-13', '3-8'],

    ['6-7', '7-8', '8-13', '13-18', '17-18', '16-17', '11-16', '6-11'],
    ['7-8', '8-9', '9-14', '14-19', '18-19', '17-18', '12-17', '7-12'],
    ['8-9', '9-10', '10-15', '15-20', '19-20', '18-19', '13-18', '8-13'],

    ['11-12', '12-13', '13-18', '18-23', '22-23', '21-22', '16-21', '11-16'],
    ['12-13', '13-14', '14-19', '19-24', '23-24', '22-23', '17-22', '12-17'],
    ['13-14', '14-15', '15-20', '20-25', '24-25', '23-24', '18-23', '13-18'],

    # 3x3 squares

    # the 4x4 square
    ['1-2', '2-3', '3-4', '4-5', '5-10', '10-15', '15-20', '20-25',
    '24-25', '23-24', '22-23', '21-22', '16-21', '11-16', '6-11', '1-6']
]

if __name__ == "__main__":
    lines_out = []

    main()
    sys.exit(0)

    for line in open(sys.argv[1], 'r'):
        s = line.strip().translate(table)
        words = [w.lower() for w in re.findall(r'\w+', s)]
        lines_out.append(' '.join(words))

    print '\n'.join(lines_out)
    sys.stdout.flush()

