#!/usr/bin/env python
# Python 2.7

"""
2019Mar16

https://open.kattis.com/problems/anewalphabet
"""

import sys

# web page dumped as text, lines joined
# NB: there are no spaces in the target transliteration
# just split this data and ignore all but 1st and 2nd words
DATA = """\
a @ at symbol
n []\[] brackets, backslash, brackets
b 8 digit eight 
o 0 digit zero
c ( open parenthesis
p |D bar, capital D
d |) bar, close parenthesis 
q (,) parenthesis, comma, parenthesis 
e 3 digit three 
r |Z bar, capital Z 
f # number sign (hash) 
s $ dollar sign 
g 6 digit six 
t '][' quote, brackets, quote 
h [-] bracket, hyphen, bracket 
u |_| bar, underscore, bar 
i | bar 
v \/ backslash, forward slash 
j _| underscore, bar 
w \/\/ four slashes 
k |< bar, less than 
x }{ curly braces 
l 1 digit one 
y `/ backtick, forward slash 
m []\/[] brackets, slashes, brackets 
z 2 digit two 
"""

def makeDict(data):
    d = {} # return value dict
    for line in data.split('\n')[:-1]:
        key, val, *foo = line.split() # only care about 1st and 2nd
        d[key] = val

    return d

def xlate(text_s, xlate_d):
    l = []
    for c in list(text_s):
        cl = c.lower()
        try:
            new_c = xlate_d[cl]
        except KeyError as ke:
            new_c = cl # things not in dict remain unchanged

        l.append(new_c)

    return ''.join(l) 

# main
print(
    xlate(
        sys.stdin.readline(),
        makeDict(DATA)
    )
)

