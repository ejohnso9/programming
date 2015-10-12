#! /usr/bin/env python

"""
DESCRIPTION:
    Python challenge problem #5 at:

        http://www.pythonchallenge.com/pc/def/peak.html

    HTML source for above page is:

<html>
<head>
  <title>peak hell</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="peakhell.jpg"/>
<br><font color="#c0c0ff">
pronounce it
<br>
<peakhell src="banner.p"/>
</body>
</html>

<!-- peak hell sounds familiar ? -->


    That is actually kind of a tough clue, but I did part of this
challenge once before and remember something to do with pickle module.

    If you load the URL: http://www.pythonchallenge.com/pc/def/banner.p
and you've seen pickle output, you might recognize the text format as a
pickled Python object:


(lp0
(lp1
(S' '
p2
I95
tp3
aa(lp4
...

"""

import pickle
from urllib import urlopen


#///////////////////////////////////////////////////////////////////////
# MAIN
if __name__ == '__main__':

    from pprint import pprint

    # The text is rather long. Now that we know how to use urllib, let's
    # just grab the data off the Internet...
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    fd = urlopen(url)
    text = fd.read()
    fd.close()

    obj = pickle.loads(text)
    # pprint(obj)

    # This object is a list of lists of tuples.
    # Given the 'banner' clue, let's try interpreting this as a raster
    # image, the top level list being the lines, the inner list being
    # sequences of characters to print (basically run-length encoding).

    # works
    for row in obj:
        s = ''
        for (c, n) in row:
            s += c * n
        print s

    # prints out a "banner" version of 'channel'
    print """
    Challenge #6 starts at:
    http://www.pythonchallenge.com/pc/def/channel.html
    """

# END MAIN
#///////////////////////////////////////////////////////////////////////
