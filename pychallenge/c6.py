#! /usr/bin/env python

"""
DESCRIPTION:
    Python challenge problem #6 starts at:
        http://www.pythonchallenge.com/pc/def/channel.html

    Clue: 'zip', you can indeed download a zip file at:
        http://www.pythonchallenge.com/pc/def/channel.zip

    The Python module to manipulate zip archives is 'zipfile'.
"""

import zipfile, re
from pprint import pprint
# from urllib import urlopen


#///////////////////////////////////////////////////////////////////////
# MAIN
#
# PREREQUISITES:
#     I have already downloaded and saved the zip file mentioned above
#     as the local file 'channel.zip'.
if __name__ == '__main__':

    # You can create a ZipFile object like so:
    # zf = zipfile.ZipFile('channel.zip') 

    # So, looking at the documentation for the modules and poking around
    # a bit in the interactive interpreter:
    """
>>> import zipfile
>>> zf = zipfile.ZipFile('channel.zip')
>>> dir(zf)
['NameToInfo', '_GetContents', '_RealGetContents', '__del__', '__doc__', '__init
__', '__module__', '_filePassed', '_writecheck', 'close', 'comment', 'compressio
n', 'debug', 'filelist', 'filename', 'fp', 'getinfo', 'infolist', 'mode', 'namel
ist', 'printdir', 'read', 'start_dir', 'testzip', 'write', 'writestr']
    """

    # ZipFile.filelist is a list of ZipInfo objects
    # ZipFile.NameToInfo is a dict, mapping file name to its ZipInfo object


    # There seems to be something interesting going on in the comments:
    # looks like one character per file, 910 total files
    """
E   Y     * E     Y   O N   * * * * *     * Y   * E
* O G
*   Y         G   E *   Y       E *   N *     G * * G *       * *   *   *   *
G X * * *   * *   *       * E   * * X   O   E *   E     * * *   *
  N       *   X G   E     *   N N     G *       X E X * *   Y   X N     * O O
  * G * * *     N       N     *
    X * * Y   *   E *   * * Y O * * * N   *   * * *   X *   E *     * *   X
O * * *       X *
N   *   * X
    *   *   *       *   * G     * *   O     Y N   X   N   * * * Y       * * *
      * *   O *   *   * *     O G * *   O O     O * * *
  X     Y * *     G   E     * *   E * *   Y   * *     X   N * Y O *   O   X
  E   * N * Y E     * * O *   E *     *   *     * * *     *   * N *       E * Y
    * N Y       *   E   X *   O       *   *     *   Y G *   N Y G     * *   O *
E     * Y       G Y     * *   X     * *   * *     G   E * *   * *     * O *   *
* * Y *   *
  O O * *   *   *     *         *     * *   *   *   * * * N   * *   *   X
*   Y E         O Y   *     * E     Y   *   *     *     * N * *   Y *   *
  O   * *         Y X     * * E * *     *   Y O   *       O           X   * X *
    E   * * * * *         E   * * *   * *   * *   G Y * G *
"""

    # OK, here's enough info to get started on
    """
>>> f0 = zf.filelist[0]
>>> dir(f0)
['CRC', 'FileHeader', '__doc__', '__init__', '__module__', 'comment', 'compress_
size', 'compress_type', 'create_system', 'create_version', 'date_time', 'externa
l_attr', 'extra', 'extract_version', 'file_offset', 'file_size', 'filename', 'fl
ag_bits', 'header_offset', 'internal_attr', 'orig_filename', 'reserved', 'volume
']
>>> zf.testzip()
>>> f0
<zipfile.ZipInfo instance at 0x7ff23dec>
>>> f0.filename
'29.txt'
>>> f0.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
AttributeError: ZipInfo instance has no attribute 'read'
>>> zf.read('29.txt')
'Next nothing is 83831'
>>> zf.read('83831.txt')
'Next nothing is 80100'
    """


    # First run of this ends in text that says "Collect the comments.",
    # starting from the first file in the archive (filelist[0])
    #
    # while 1:
    #     text = zf.read(zi.filename)
    #     print text
    #     n = text.split()[-1]
    #     filename = str(n) + '.txt'


    # I later realize the archive contains a file: readme.txt
    #
    # welcome to my zipped list.
    #
    # hint1: start from 90052
    # hint2: answer is inside the zip


    # open the archive
    zf = zipfile.ZipFile('channel.zip') 

    # bootstrap the while loop
    zi = zf.NameToInfo['90052.txt']
    filename = zi.filename
    comments = zi.comment

    # follow the chain
    cList = []
    while 1:
        text = zf.read(filename)
        zi = zf.NameToInfo[filename]
        cList.append(zi.comment)
        print text
        n = text.split()[-1]  # string rep of int!

        # end this loop when last word not a number
        try:
            i = int(n)
        except ValueError:
            break
            
        filename = str(n) + '.txt'

    print
    print ''.join(cList)
    """
*****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
    """


    print """
    Challenge #7 starts at: 
    http://www.pythonchallenge.com/pc/def/oxygen.html
    """

# END MAIN
#///////////////////////////////////////////////////////////////////////
