#! /usr/bin/python
# coding: ascii

"""The little reST slicer - cut reST files into pieces."""

__version__ = '0.0.1'

# leave your name and notes here:
__history__ = """\

2012-03-13  just born.
2012-03-14  John Doe  <demo@example.land>
            added: feature abc
"""

__copyright__ = """\

Copyright (c), 2011-2012, Martin Bless  <martin@mbless.de>

All Rights Reserved.

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee or royalty is hereby
granted, provided that the above copyright notice appears in all copies
and that both that copyright notice and this permission notice appear
in supporting documentation or portions thereof, including
modifications, that you make.

THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
WITH THE USE OR PERFORMANCE OF THIS SOFTWARE!
"""


import codecs
import os
import sys

f1name = 'manual.rst'
startname = '00-Start'
relpath = 'many3/'
rstfileext = '.rst'
depth = 3

SECTION_UNDERLINERS = """:=-~"^`$*+;.',_#/\%&!^"""
levels = [0 for i in range(depth+1)]
removeFromFilename = ''.join([ chr(i) for i in range(128) if chr(i).lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789-_[]{}()+'])

def getCleanFileName(fname):
    fname = fname.encode('ascii','ignore')
    fname = fname.replace(' ','_')
    fname = fname.replace('/','_')
    while '__' in fname:
        fname = fname.replace('__', '_')
    fname = fname.translate(None, removeFromFilename)
    return fname

f2 = sys.stdout
f1 = codecs.open(f1name, 'r', 'utf-8-sig')
f2 = codecs.open(os.path.join(relpath, startname) + rstfileext, 'w', 'utf-8-sig')
lines = []
for line in f1:
    lines.append(line)
    while len(lines) >= 4:
        hot = len(lines[0].strip()) == 0
        hot = hot and (len(lines[1].strip()) != 0)
        hot = hot and (len(lines[2].strip()) != 0)
        hot = hot and (len(lines[3].strip()) == 0)
        hot = hot and (lines[1].rstrip('\r\n') <> (lines[1][0] * len(lines[1].rstrip('\r\n'))))
        hot = hot and (lines[2].rstrip('\r\n') == (lines[2][0] * len(lines[2].rstrip('\r\n'))))
        if hot:
            underliner = lines[2][0]
            p = SECTION_UNDERLINERS.find(underliner)
            if p > -1 and p < depth:
                levels[p] += 1
                for i in range(p+1, depth+1):
                    levels[i] = 0
                prefix = ['%02d'%levels[i] for i in range(p+1)]
                fname = '%s-%s' % ('-'.join(prefix), lines[1].strip())
                fname = getCleanFileName(fname)
                if not f2 is sys.stdout:
                    f2.close()
                f2 = codecs.open(os.path.join(relpath, fname) + rstfileext, 'w', 'utf-8-sig')
        f2.write(lines[0])
        del lines[0]
while lines:
    f2.write(lines[0])
    del lines[0]

if not f2 is sys.stdout:
    f2.close()
f1.close()
