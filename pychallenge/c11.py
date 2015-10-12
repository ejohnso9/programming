#! /usr/bin/env python

"""
DESCRIPTION:
    A working solution for Python challenge problem #11, which starts at:
        http://www.pythonchallenge.com/pc/return/5808.html
        user:huge, pass:file

SOLUTION DISCUSSION:
    Below is notes to myself as I am working through the problem and
developing the program.

    Just looking at the picture, it seems like two pictures are blended.
Especially note the edges where the outer rows or columns have every
other pixel as black as well as the general "texture" of the picture.
This coupled with page title hint "odd even" suggests two pictures
interlaced (in both rows and columns).

    So, after inspecting some of the data, my hunch seem esentially
correct. Here's what the first 10 pixels of the first 6 rows looks like:

[(0, 20, 0), (142, 180, 105), (0, 20, 0), (139, 177, 100), (0, 20, 0), (143, 180
, 103), (0, 20, 0), (138, 175, 98), (0, 19, 0), (153, 186, 115)]

[(148, 186, 111), (0, 20, 0), (148, 186, 109), (0, 21, 0), (144, 181, 104), (0,
20, 0), (144, 181, 104), (0, 20, 0), (146, 180, 106), (0, 18, 0)]

[(0, 20, 0), (158, 195, 118), (0, 20, 0), (148, 185, 108), (0, 22, 0), (152, 189
, 112), (0, 19, 0), (150, 184, 110), (0, 19, 0), (160, 193, 124)]

[(145, 182, 105), (0, 22, 0), (158, 195, 118), (0, 20, 0), (155, 189, 113), (0,
19, 0), (146, 180, 104), (0, 20, 0), (137, 171, 97), (0, 18, 0)]

[(0, 24, 0), (150, 184, 108), (0, 19, 0), (156, 190, 114), (0, 19, 0), (158, 192
, 116), (0, 18, 0), (145, 176, 106), (0, 24, 0), (160, 191, 124)]

[(156, 190, 114), (0, 19, 0), (158, 192, 115), (0, 23, 0), (151, 185, 109), (0,
19, 0), (162, 194, 121), (0, 17, 0), (157, 188, 118), (0, 17, 0)]

    Odd pixels on the odd rows and even pixels on the even rows seem to be
special. Let's get those separated and look at a picture of them (the
new picture would be of size: (320, 480)

    OK, well, that doesn't yield anything obvious in itself, though
it looks like there is something very dark in the picture - just little
reddish splotches. Given the name of the original picture, I can imagine
maybe it's a picture of stalactites and stalagmites. The "11" is clearly
visible as white on black. I'm essentialy into the realm of image
processing now. I think I need to lighten the picture and see if
anything else can be revealed.

    Yes, that is exactly right. PIL supports point operations which is
essentially applying a funtion to each pixel. Multiplying by a value
around 2 to 4 will reveal some sort of strange pattern with "evil"
spelled out in the upper right hand corner.

    out = img1.point(lambda i: i * 4.0)

"""


# IMPORTS
#=======================================================================
import sys
import PIL
from PIL import Image


# GLOBAL DATA
#=======================================================================
FILENAME = "cave.jpg"   


#-----------------------------------------------------------------------



#///////////////////////////////////////////////////////////////////////
# MAIN
#
# PREREQUISITES:
#     FIRST and SECOND arrays defined above
if __name__ == '__main__':

    img = Image.open(FILENAME)
    print img
    print "img.size =", img.size

    data = img.getdata()
    print "len(data) = ", len(data)
    
    count = 0
    odd = []
    for i in xrange(len(data)):
        pix = data[i]
        if (pix[0] == 0 and pix[2] == 0):
            count += 1
            odd.append(pix)

    # first, convert the linear array into a 2D array
    grid = []
    for i in xrange(len(data)):
        if i % img.size[0] == 0:
            row = []
            grid.append(row)
        row.append(data[i])

    # now, walk through 2D array and build 1D array of odd/even data
    data2 = []
    even = False
    for row in xrange(len(grid)):
        even = not even
        for col in xrange(len(grid[0])):
            # special case for col 0 because 0 % n == 0 (for any n)
            if col == 0:
                if even:
                    # first pixel on even row
                    data2.append(grid[row][0])
            else:
                if even:
                    # even row
                    if col % 2 == 0:
                        # gather even pixels
                        data2.append(grid[row][col])
                else:
                    # odd row
                    if col % 2 == 1:
                        # gather odd pixels
                        data2.append(grid[row][col])


    # Write the odd/even data into a new picture (JPG)
    img1 = Image.new('RGB', (320, 480))
    img1.putdata(data2)

    out = img1.point(lambda i: i * 4.0)
    out.save("data2.jpg")

    url = "http://www.pythonchallenge.com/pc/return/evil.html"
    print "Problem #12 starts at:", url

# END MAIN
#///////////////////////////////////////////////////////////////////////

"""
    PROBLEM #12 STARTS AT:

        http://www.pythonchallenge.com/pc/return/evil.html

    Again, the texture of the picture suggests one (or more) picture(s)
    interlaced within another.  Perhaps color separation?


POST DISCUSSION:

    When you go to look at the solutions, there are often some "nifty
tricks". That is, code shortcuts that happen to work. Most of them are
created by trimming what's unnecessary. Others are really just hacks,
for example, the one line solution:

    Image.open('cave.jpg').resize((320, 240)).show()

    You happen to end up with a set of pixels that works, but that is
really a fortuitous coincendence of the way the picture is being
downsized. Had three pictures been interlaced, or two with some other
pattern, such hacks wouldn't work.


LESSONS LEARNED FROM SOLUTIONS PAGE:

    1) using the skip parameter on slices to get odd/even:

>>> range(20)[::2]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> range(1, 20)[::2]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>>

    2) getpixel() and putpixel() may be more direct than operating on
    list(getdata()):

import Image
im=Image.open('cave.jpg')
im1=Image.new('RGB',(640,480))
for y in range(0,480):
    for x in range(0,640):
        c=im.getpixel((x,y))
        if (x+y)%2==0:
            im1.putpixel((x,y),(c[1]*3,c[1]*3,c[1]*3))
im1.show()


    Some of the solutions are breaking the image down into 4 quadrants,
and while this may be sufficient to pick "evil" out of the dark
quadrants, this is sort of bending the idea of separating the pixels
into odd and even.

"""

