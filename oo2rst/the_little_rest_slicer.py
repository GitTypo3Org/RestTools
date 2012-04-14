#! /usr/bin/python
# coding: ascii

"""The little reST slicer - cut reST files into pieces."""

__version__ = '0.0.3'

# leave your name and notes here:
__history__ = """\

2012-03-13  just born.
2012-03-14  John Doe  <demo@example.land>
            added: feature abc
2012-03-15  0.0.2 Very much improved. Creates complete Sphinx
            structure now!
2012-03-18  used as is for complete conversion process today

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
import shutil
import sys

f1name = 'img\\manual2.rst'
f1name = 'official_documentation_template.rst'
f1name = 'img\\manual.rst'

# we assume:
f1name = 'doc_core_api\doc_core_api\doc'    '\img\manual.rst'
f1name = ''
if len(sys.argv) > 1:
    f1name = sys.argv[1]

dirpath, fname = os.path.split(f1name)
dirpathleft, dirpathlast = os.path.split(dirpath)
# ('manual', '.rst')
fstem, fext = os.path.splitext(fname)
if fstem and fext.lower() == '.rst' and dirpathlast == 'img':
    pass
else:
    print 'We are looking for a path like: a/b/c/img/name.rst with parts [\'a/b/c\', \'img\', \'name.rst\']'
    sys.exit(1)

startname = 'index'
rstfileext = '.rst'

depth = 3
relpathroot = 'many%s' % depth
relpathroot = os.path.join(dirpathleft, 'source')
relpath = relpathroot

images_index_file = relpathroot + '/img/index.txt'

CUTTER_MARK_IMAGES = '.. ######CUTTER_MARK_IMAGES######'

RSTFILE_TOPTEXT = """\
.. ==================================================
.. FOR YOUR INFORMATION
.. --------------------------------------------------
.. -*- coding: utf-8 -*- with BOM.

.. ==================================================
.. DEFINE SOME TEXTROLES
.. --------------------------------------------------
.. role::   underline
.. role::   typoscript(code)
.. role::   ts(typoscript)
   :class:  typoscript
.. role::   php(code)

"""

toctree = '\n'.join([
    '',
    '.. toctree::',
    '   :maxdepth: 5',
    '   :titlesonly:',
    '   :glob:',
    '',
    '   *',
    ''
    ])


HTML_THEME_PATH_IN_CONF_PY = """html_theme_path = ['../../../res/sphinx/themes/', '/usr/share/sphinx/themes/']"""

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

def copyImagesIndexFile(src, dest, uplevels=0):
    f1 = codecs.open(src , 'r', 'utf-8-sig')
    f2 = codecs.open(dest, 'w', 'utf-8-sig')
    for line in f1:
        parts = line.split(' image::', 1)
        if len(parts) > 1:
            up = '/'.join(['..'] * uplevels)
            if up:
                parts[1] = ' %s/%s' % (up, parts[1].lstrip())
            line = ' image::'.join(parts)
        f2.write(line)
    f2.close()
    f1.close()

def copyConfPy(src, dest):
    written = False
    dirparts = []
    dirpath, fname = os.path.split(dest)
    while dirpath:
        dirpath, right = os.path.split(dirpath)
        dirparts.insert(0, right)
    MORE_UPLEVELS_TO_RES = 1
    levels = MORE_UPLEVELS_TO_RES + len(dirparts)
    uppath = '/'.join(['..'] * levels)
    html_theme_path = HTML_THEME_PATH_IN_CONF_PY.replace('../../..', uppath)
    f1 = codecs.open(src , 'r')
    f2 = codecs.open(dest, 'w')
    for line in f1:
        if line.startswith('html_theme_path'):
            line = html_theme_path + '\n'
            written = True
        f2.write(line)

    if not written:
        line = '\n' + html_theme_path + '\n'
        written = True
        f2.write(line)

    f2.close()
    f1.close()

try:
    os.makedirs(relpath)
except:
    pass

try:
    os.makedirs(os.path.join(relpathroot,'img'))
except:
    pass

if 1 and 'Sphinx Meta data':
    shutil.copy('Makefile', os.path.join(relpathroot, '..', 'Makefile'))
    copyConfPy('conf.py', os.path.join(relpathroot, 'conf.py'))
    src = '_templates'
    dest = os.path.join(relpathroot, src)
    if not os.path.exists(dest):
        shutil.copytree(src, dest)
    src = '_static'
    dest = os.path.join(relpathroot, src)
    if not os.path.exists(dest):
        shutil.copytree(src, dest)

if 1 and 'handle images':

    if 'copy images':
        for p, dirs, fnames in os.walk(os.path.join(relpathroot, '..', 'img')):
            dirs[:] = []
            for fname in fnames:
                f2name = fname
                if fname.endswith('.rst'):
                    f2name = fname + '.txt'
                if fname.endswith('-tweaked.html'):
                    f2name = ''
                if f2name:
                    shutil.copy(os.path.join(p, fname), os.path.join(relpathroot, 'img', f2name))

    if 'copy text following CUTTER_MARK_IMAGES to index.txt':
        f1 = codecs.open(f1name, 'r', 'utf-8-sig')
        f2 = codecs.open(os.path.join(relpathroot, 'img', 'index.txt'), 'w','utf-8-sig')
        skipping = True
        for line in f1:
            if skipping and line.startswith(CUTTER_MARK_IMAGES):
                skipping = False
            if not skipping:
                f2.write(line)
        f2.close()
        f1.close()

f1 = codecs.open(f1name, 'r', 'utf-8-sig')
copyImagesIndexFile(images_index_file, 'images.txt', uplevels=0)
f2 = codecs.open(os.path.join(relpath, startname) + rstfileext, 'w', 'utf-8-sig')
f2.write('.. include:: images.txt\n\n')
lines = []
for line in f1:
    if line.startswith(CUTTER_MARK_IMAGES):
        break
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
                prefixparts = ['%02d'%levels[i] for i in range(p+1)]
                fname = '%s-%s' % ('-'.join(prefixparts), lines[1].strip())
                fname = getCleanFileName(fname)
                if toctree:
                    f2.write(toctree)
                if not f2 is sys.stdout:
                    f2.close()
                relpath = relpathroot
                for i in range(len(prefixparts)):
                    relpath = os.path.join(relpath, ('-'.join(prefixparts[:i])))
                try:
                    os.makedirs(relpath)
                except:
                    pass
                copyImagesIndexFile(images_index_file, os.path.join(relpath, 'images.txt'), uplevels=len(prefixparts)-1)
                f2 = codecs.open(os.path.join(relpath, fname) + rstfileext, 'w', 'utf-8-sig')
                relpathback = '/'.join(['..'] * (len(prefixparts) - 1))
                if relpathback:
                    relpathback += '/'
                else:
                    relpathback = './'
                f2.write('.. include:: images.txt\n\n')
                f2.write(RSTFILE_TOPTEXT)
                if len(prefixparts) <= (depth-1):
                    prefix = '-'.join(prefixparts)
                    globexpr = prefix + '/*'
                    toctree = '\n'.join([
                        '',
                        '.. toctree::',
                        '   :maxdepth: 5',
                        '   :titlesonly:',
                        '   :glob:',
                        '',
                        '   %s' % globexpr,
                        ''
                        ])
                else:
                    toctree = ''

        f2.write(lines[0])
        del lines[0]
while lines:
    f2.write(lines[0])
    del lines[0]

if not f2 is sys.stdout:
    f2.close()
f1.close()
