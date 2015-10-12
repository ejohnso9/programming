#! /usr/bin/env python

"""
DESCRIPTION:
    A working solution for Python challenge problem #7, which starts at:
        http://www.pythonchallenge.com/pc/def/oxygen.html

    The page has an image in it: <img src="oxygen.png"/> and that file
    has been saved into the local source directory.  Across the center
    is a line of gray blocks. 

NOTES:
    PIL, the Python Image Library is a graphics image creation and
    manipulation program, created by Fredrik Lundh, a major player in
    the Python community. The home page for PIL is at:
    http://www.pythonware.com/products/pil/    (see also effbot.org)
"""



"""
SOLUTION:
    1. My first intuition is to use PIL to get the PNG file converted
    into a bitmap text file, then just locate a line of the grey blocks,
    and try to interpret the RGB values as ASCII code.

    2. I had some problems with PIL 1.1.6 - not sure why but I don't seem
    to be running into the same errors w/ 1.1.5.  BMP format is a binary
    format - can't edit directly. I think I did this problem before but
    lost the solution somewhere. 

    3. Below is documentation as comments of solving the problem
    interactively via the Python interpreter, and then at the bottom is
    a standalone program that arrives at the same point.

>>> filename = 'oxygen.png'
>>> img = Image.open(filename)
>>> img.size, img.format
((629, 95), 'PNG')

    3. I found the function getdata() which converts pixel data to an
    internal iterable. It says you can use list() to get it into
    something to handle externally.

>>> data = img.getdata()
>>> data
<ImagingCore object at 0x0099D100>
>>> l = list(data)

# The documentation also says that it converts it into a flat array:

>>> len(l)
59755
>>> l[0]
(79, 92, 23, 255)

# I assume that must be (red, green, blue, alpha).  The grey blocks look
# like they run pretty much down the middle of the picture. If it is 629
# pixels wide, the row half way down the middle starts at offset:

>>> offset = 629 * 47
>>> pixel = l[offset]
>>> pixel
(115, 115, 115, 255)

# That does appear to be a grey pixel. Let's pick out the row, and
# figure out how wide the blocks are:
 
>>> row = l[offset:offset+629]

# browsing through the print dump of row, it looks like the first three
# components of all the tuples have the same value. 



# I just want to look at the values (r, g & b have the same - use a list
# comprehension to get to an array of only r values:

>>> [t[0] for t in row]
[115, 115, 115, 115, 115, 109, 109, 109, 109, 109, 109, 109, 97, 97, 97, 97, 97,
 97, 97, 114, 114, 114, 114, 114, 114, 114, 116, 116, 116, 116, 116, 116, 116, 3
2, 32, 32, 32, 32, 32, 32, 103, 103, 103, 103, 103, 103, 103, 117, 117, 117, 117
, 117, 117, 117, 121, 121, 121, 121, 121, 121, 121, 44, 44, 44, 44, 44, 44, 44,
32, 32, 32, 32, 32, 32, 32, 121, 121, 121, 121, 121, 121, 121, 111, 111, 111, 11
1, 111, 111, 111, 117, 117, 117, 117, 117, 117, 117, 32, 32, 32, 32, 32, 32, 32,
 109, 109, 109, 109, 109, 109, 109, 97, 97, 97, 97, 97, 97, 97, 100, 100, 100, 1
00, 100, 100, 100, 101, 101, 101, 101, 101, 101, 101, 32, 32, 32, 32, 32, 32, 32
, 105, 105, 105, 105, 105, 105, 105, 116, 116, 116, 116, 116, 116, 116, 46, 46,
46, 46, 46, 46, 46, 32, 32, 32, 32, 32, 32, 32, 116, 116, 116, 116, 116, 116, 11
6, 104, 104, 104, 104, 104, 104, 104, 101, 101, 101, 101, 101, 101, 101, 32, 32,
 32, 32, 32, 32, 32, 110, 110, 110, 110, 110, 110, 110, 101, 101, 101, 101, 101,
 101, 101, 120, 120, 120, 120, 120, 120, 120, 116, 116, 116, 116, 116, 116, 116,
 32, 32, 32, 32, 32, 32, 32, 108, 108, 108, 108, 108, 108, 108, 101, 101, 101, 1
01, 101, 101, 101, 118, 118, 118, 118, 118, 118, 118, 101, 101, 101, 101, 101, 1
01, 101, 108, 108, 108, 108, 108, 108, 108, 32, 32, 32, 32, 32, 32, 32, 105, 105
, 105, 105, 105, 105, 105, 115, 115, 115, 115, 115, 115, 115, 32, 32, 32, 32, 32
, 32, 32, 91, 91, 91, 91, 91, 91, 91, 49, 49, 49, 49, 49, 49, 49, 48, 48, 48, 48
, 48, 48, 48, 53, 53, 53, 53, 53, 53, 53, 44, 44, 44, 44, 44, 44, 44, 32, 32, 32
, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 48, 48
, 48, 48, 48, 48, 48, 44, 44, 44, 44, 44, 44, 44, 32, 32, 32, 32, 32, 32, 32, 49
, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 54, 54, 54, 54, 54, 54, 54
, 44, 44, 44, 44, 44, 44, 44, 32, 32, 32, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49
, 49, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 44, 44, 44, 44, 44
, 44, 44, 32, 32, 32, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49, 49, 48, 48, 48, 48
, 48, 48, 48, 51, 51, 51, 51, 51, 51, 51, 44, 44, 44, 44, 44, 44, 44, 32, 32, 32
, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 52, 52
, 52, 52, 52, 52, 52, 44, 44, 44, 44, 44, 44, 44, 32, 32, 32, 32, 32, 32, 32, 49
, 49, 49, 49, 49, 49, 49, 48, 48, 48, 48, 48, 48, 48, 53, 53, 53, 53, 53, 53, 53
, 44, 44, 44, 44, 44, 44, 44, 32, 32, 32, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49
, 49, 49, 49, 49, 49, 49, 49, 49, 54, 54, 54, 54, 54, 54, 54, 44, 44, 44, 44, 44
, 44, 44, 32, 32, 32, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50
, 50, 50, 50, 49, 49, 49, 49, 49, 49, 49, 93, 93, 93, 93, 93, 93, 93, 93, 114, 1
12, 110, 103, 98, 101, 109, 107, 101, 106, 108, 102, 99, 97, 94, 95, 98, 97, 95,
 97, 99]

# It looks like the first block is 5 pixels wide, and then it continues
# on at 7 pixels per block. That seems about right, just looking at the
# picture. And the grey blocks don't extend all the way across the
# picture, so there's some stuff at the end that needs to be trimmed.
# (let me just textually add two pixels on the front and trim the end by
# hand using VIM, reevaluate the array and write a loop to grab every
# 7th pixel... (last box is 8 pixels wide - trim one pixel there)


[115, 115, 115, 115, 115, 115, 115, 109, 109, 109, 109, 109, 109, 109,
97, 97, 97, 97, 97, 97, 97, 114, 114, 114, 114, 114, 114, 114, 
116, 116, 116, 116, 116, 116, 116, 32, 32, 32, 32, 32, 32, 32,
103, 103, 103, 103, 103, 103, 103, 117, 117, 117, 117 , 117, 117, 117,
121, 121, 121, 121, 121, 121, 121, 44, 44, 44, 44, 44, 44, 44,
32, 32, 32, 32, 32, 32, 32, 121, 121, 121, 121, 121, 121, 121,
111, 111, 111, 111, 111, 111, 111, 117, 117, 117, 117, 117, 117, 117,
32, 32, 32, 32, 32, 32, 32, 109, 109, 109, 109, 109, 109, 109,
97, 97, 97, 97, 97, 97, 97, 100, 100, 100, 100, 100, 100, 100,
101, 101, 101, 101, 101, 101, 101, 32, 32, 32, 32, 32, 32, 32,
105, 105, 105, 105, 105, 105, 105, 116, 116, 116, 116, 116, 116, 116,
46, 46, 46, 46, 46, 46, 46, 32, 32, 32, 32, 32, 32, 32,
116, 116, 116, 116, 116, 116, 116, 104, 104, 104, 104, 104, 104, 104,
101, 101, 101, 101, 101, 101, 101, 32, 32, 32, 32, 32, 32, 32,
110, 110, 110, 110, 110, 110, 110, 101, 101, 101, 101, 101, 101, 101,
120, 120, 120, 120, 120, 120, 120, 116, 116, 116, 116, 116, 116, 116,
32, 32, 32, 32, 32, 32, 32, 108, 108, 108, 108, 108, 108, 108,
101, 101, 101, 101, 101, 101, 101, 118, 118, 118, 118, 118, 118, 118,
101, 101, 101, 101, 101, 101, 101, 108, 108, 108, 108, 108, 108, 108,
32, 32, 32, 32, 32, 32, 32, 105, 105, 105, 105, 105, 105, 105,
115, 115, 115, 115, 115, 115, 115, 32, 32, 32, 32, 32, 32, 32,
91, 91, 91, 91, 91, 91, 91, 49, 49, 49, 49, 49, 49, 49,
48, 48, 48, 48 , 48, 48, 48, 53, 53, 53, 53, 53, 53, 53,
44, 44, 44, 44, 44, 44, 44, 32, 32, 32, 32, 32, 32, 32,
49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49,
48, 48, 48, 48, 48, 48, 48, 44, 44, 44, 44, 44, 44, 44,
32, 32, 32, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49, 49,
49, 49, 49, 49, 49, 49, 49, 54, 54, 54, 54, 54, 54, 54,
44, 44, 44, 44, 44, 44, 44, 32, 32, 32, 32, 32, 32, 32,
49, 49, 49, 49, 49, 49, 49, 48, 48, 48, 48, 48, 48, 48,
49, 49, 49, 49, 49, 49, 49, 44, 44, 44, 44, 44, 44, 44,
32, 32, 32, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49, 49,
48, 48, 48, 48, 48, 48, 48, 51, 51, 51, 51, 51, 51, 51,
44, 44, 44, 44, 44, 44, 44, 32, 32, 32, 32, 32, 32, 32,
49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49,
52, 52, 52, 52, 52, 52, 52, 44, 44, 44, 44, 44, 44, 44,
32, 32, 32, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49, 49,
48, 48, 48, 48, 48, 48, 48, 53, 53, 53, 53, 53, 53, 53,
44, 44, 44, 44, 44, 44, 44, 32, 32, 32, 32, 32, 32, 32,
49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49,
54, 54, 54, 54, 54, 54, 54, 44, 44, 44, 44, 44, 44, 44,
32, 32, 32, 32, 32, 32, 32, 49, 49, 49, 49, 49, 49, 49,
50, 50, 50, 50, 50, 50, 50, 49, 49, 49, 49, 49, 49, 49,
93, 93, 93, 93, 93, 93, 93,
]


>>> for i in range(len(row2)):
...   if i % 7 == 0:
...     s += chr(row2[i])
...
>>> s
'smart guy, you made it. the next level is 
[105, 110, 116, 101, 103, 114, 105, 116, 121]'

# 
>>> s
'smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 1
16, 121]'
>>> s_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
>>> [chr(c) for c in s_list]
['i', 'n', 't', 'e', 'g', 'r', 'i', 't', 'y']

# Yes, the next puzzle starts at: 
    http://www.pythonchallenge.com/pc/def/integrity.html

"""

from PIL import Image

#///////////////////////////////////////////////////////////////////////
# MAIN
#
# PREREQUISITES:
#     oxygen.png assumed to be a local file

if __name__ == '__main__':

    filename = 'oxygen.png'
    img = Image.open(filename)
    print "image size = " + str(img.size)    # (629, 95)
    print "image format = " + str(img.format)

    # get pixel data as a list
    data = img.getdata()
    l = list(data)  # a flat list of 4-tuples: (r, g, b, a)

    offset = 629 * 47

    # grab the middle row of pixels
    row = l[offset:offset+629]

    # get every 7th value
    pixels = [row[i] for i in range(len(row)) if (i % 7 == 0)]

    # build a string out of the red component values
    s = ''.join([chr(pixel[0]) for pixel in pixels])

    # the string has an embedded list within it, and there is some extra
    # garbage at the end coming from pixels that aren't part of the grey
    # blocks in the picture - trim extra garbage:
    s = s[:s.index(']') + 1]
    print s

    list_s = s[s.index('[') : s.index(']') + 1]

    # reinterpret the embedded list as ASCII characters again
    l = eval(list_s)
    print "Next level starts at: " + ''.join([chr(p) for p in l])
    # 'integrity'

    # Indeed, problem #8 starts at:
    print "http://www.pythonchallenge.com/pc/def/integrity.html"

# END MAIN
#///////////////////////////////////////////////////////////////////////

"""
Note that, sans comments, the solution to this problem is really this 
14 line program (which could be reduced further still):

from PIL import Image
filename = 'oxygen.png'
img = Image.open(filename)
data = img.getdata()
l = list(data)
offset = 629 * 47
row = l[offset:offset+629]
pixels = [row[i] for i in range(len(row)) if (i % 7 == 0)]
s = ''.join([chr(pixel[0]) for pixel in pixels])
s = s[:s.index(']') + 1]
print s
list_s = s[s.index('[') : s.index(']') + 1]
l = eval(list_s)
print "Next level starts at: " + ''.join([chr(p) for p in l])

"""

