#! /usr/bin/env python

"""
DESCRIPTION:
    A working solution for Python challenge problem #12, which starts at:

        http://www.pythonchallenge.com/pc/return/evil.html
        user:huge, pass:file

SOLUTION DISCUSSION:

    Again, the texture of the picture suggests one (or more) picture(s)
    interlaced within another.  Looking closely at the pixels, you can
    sort of see red and green banding. 
    
    Let's simply inspect some sample raw data again and see if we can
    see a pattern:


[(129, 82, 52), (143, 96, 66), (123, 76, 46), (136, 89, 59), (128, 81, 53), (135
, 88, 60), (125, 79, 53), (126, 82, 57), (113, 69, 44), (122, 80, 56)]

[(131, 84, 54), (110, 64, 31), (125, 79, 46), (103, 57, 24), (125, 78, 48), (104
, 59, 28), (121, 77, 48), (101, 57, 28), (116, 75, 47), (89, 49, 23)]

[(126, 97, 67), (92, 63, 31), (124, 95, 63), (90, 61, 29), (120, 91, 61), (90, 6
1, 31), (115, 88, 59), (89, 62, 33), (114, 88, 61), (74, 50, 22)]

[(117, 93, 65), (105, 84, 55), (121, 98, 67), (108, 87, 56), (116, 92, 64), (104
, 83, 54), (111, 90, 63), (101, 81, 54), (105, 88, 62), (89, 73, 47)]

[(89, 63, 38), (102, 78, 52), (94, 68, 43), (106, 82, 56), (88, 62, 37), (103, 7
9, 53), (86, 62, 38), (95, 73, 49), (80, 58, 35), (90, 69, 48)]

[(91, 61, 35), (110, 80, 54), (94, 64, 38), (113, 83, 57), (85, 55, 29), (116, 8
6, 60), (84, 56, 32), (105, 77, 53), (82, 56, 33), (102, 76, 53)]

[(108, 73, 43), (118, 83, 53), (112, 76, 44), (122, 86, 54), (104, 68, 36), (118
, 82, 50), (106, 71, 41), (113, 78, 48), (104, 70, 42), (98, 64, 36)]

[(100, 67, 36), (90, 57, 24), (101, 66, 34), (90, 56, 21), (97, 62, 30), (88, 53
, 21), (99, 64, 32), (88, 55, 22), (95, 62, 31), (79, 48, 17)]

[(104, 80, 52), (79, 56, 25), (102, 79, 48), (76, 53, 21), (103, 78, 48), (76, 5
3, 22), (99, 76, 45), (75, 54, 23), (92, 71, 42), (75, 56, 26)]

[(96, 78, 54), (84, 64, 40), (96, 76, 52), (83, 63, 38), (97, 77, 52), (83, 63,
38), (93, 73, 48), (81, 64, 38), (85, 67, 43), (81, 65, 40)]

    Hmmm, nothing obvious jumping out there. Let's try the color separation:

    # split the image into individual bands
    source = img.split()
    (R, G, B) = (0, 1, 2)

    # save each band
    source[R].save("red.jpg")
    source[G].save("green.jpg")
    source[B].save("blue.jpg")

    This yeilds three greyscale images where red is the brightest, green
is intermediate and blue is fairly dark. Looking at the data again
above, red values seem to be oscillating in the third row: 126, 92, 124,
90, 120, 90, 115, 89...  The oscillation seems to be more pronounced
again on the ninth row. Let's look at odd/even separation again.

    Dangit... had to use a hint here. It said to pay attention to
filenames and then suggested changing it. So there are two other
pictures at evil2.jpg and evil3.jpg. The first saying: 
"not jpg - - .gfx" and the second saying "no more evils" (implying no
point in looking for any other like-named pictures). 

    The string "gfx" does not appear in the PIL manual. So I guess part
of the data needs to have it's file format converted and saved, but it's
not obvious whether that is all of the data or some band or odd/even or
what. Trial and error I suppose. A search on wikipedia uncovers two
entries:

GFX 	Instant Artist graphics Files 	Instant Artist
GFX 	PCBoard @X-coded colorful text 	GFX2COM - GFX2EXE

    The first seems a lot more promising though the PIL manual doesn't
seem to contain the string "artist" either. There also seems to be "Cue
Club Image File" (File used by the Pool Sim game 'Cue Club') and
"Genigraphics Graphics Link presentation".  Instant Artist stills seems
more likely.  

Found this page: http://www.oldversion.com/talk/showthread.php?t=3575
of a guy asking for the software. He apparently used it back in '97 and
even has screen shots of the software under Wine and SuSE Linux.
Apparently also known as "winiart". Seems the software was a windows 3.1
program originally produced by Pixellite, then taken over by Sierra,
then became part of AutoDesk.  None of this makes me feel like I'm
getting any closer to a specification of the file format.

    Funny how assumptions can lead you astray sometimes.  Because of the
texture of the picture, I assumed something was embedded in the JPG.
There is the file evil2.gfx. After reading some hints on the PyChallenge
site, they suggested using a hex editor. So, I think the trail must move
on to this file.

    There was also a hint posted by Thesamet which was a link to
(apparently) an mpeg of a guy shuffling cards. That file is no longer
there - I think the hint is that there may be multiple files in a
jumbled order embedded within the one file. I have looked through the
entire evil2.gfx file with od -x and nothing is jumping out at me. Man,
I hate these puzzles that are more of an obscure guessing game than a
programming problem.
"""


# IMPORTS
#=======================================================================
import sys
import PIL
from PIL import Image


# GLOBAL DATA
#=======================================================================
FILENAME = "evil1.jpg"   
WIDTH  = 0
HEIGHT = 1

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
    print "grid width =", len(grid[0])
    print "grid height =", len(grid)

    # Dump a sample of data near lower right corner
    height = img.size[HEIGHT]
    width  = img.size[WIDTH]
    print "height =", height
    print "width =", width

    for row in xrange(height - 30, height - 20):
        print grid[row][width - 30: width - 20]
        print

    # now, walk through 2D array and build 1D array of odd/even data
    data1 = []
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
                    data1.append(grid[row][0])
            else:
                if even:
                    # even row
                    if col % 2 == 0:
                        # gather even pixels
                        data2.append(grid[row][col])
                    else:
                        # gather odd pixels
                        data1.append(grid[row][col])
                else:
                    # odd row
                    if col % 2 == 1:
                        # gather odd pixels
                        data2.append(grid[row][col])
                    else:
                        # gather odd pixels
                        data1.append(grid[row][col])


    # split the image into individual bands
    source = img.split()
    (R, G, B) = (0, 1, 2)

    # save each band
    source[R].save("red.jpg")
    source[G].save("green.jpg")
    source[B].save("blue.jpg")


    # Write the odd/even data into a new picture (JPG)
    odd = Image.new('RGB', (320, 480))
    odd.putdata(data1)
    odd.save("odd.jpg")

    even = Image.new('RGB', (320, 480))
    even.putdata(data2)
    even.save("even.jpg")

    # out = img1.point(lambda i: i * 4.0)
    # out.save("data2.jpg")

    # url = "http://www.pythonchallenge.com/pc/return/evil.html"
    # print "Problem #12 starts at:", url

# END MAIN
#///////////////////////////////////////////////////////////////////////


