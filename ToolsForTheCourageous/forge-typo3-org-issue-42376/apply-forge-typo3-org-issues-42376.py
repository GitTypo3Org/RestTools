#!/usr/bin/env python

# This script has been placed in the public domain.
# No warrenties whatsoever. Use at your own risk.

"""apply-forge-typo3-org-issues-42376.py  2012-10-25, 2012-10-27

Copy this script to folder "./Documentation/" and
run it from there without any arguments. If will
only work if there is a file "./Documentation/Index.rst".

See https://forge.typo3.org/issues/42376 for what it does.

It will:

* clean up the top of each ReST file to consist of:
  - "For you information comment"
  - .. include:: (../)* Includes.txt directive
  - .. include:: Images.txt where appropriate

* touch all Images.txt files to make the :width: and :height:
  option of images a comment as those values are smaller than
  the actual sizes of the images. The values given there
  correspond to the former display size in OpenOffice.

* strip all trailing whitespace from lines

* Use the more compact form to start literal blocks

(w) written by martin.bless@gmail.com

(c) Public Doamin.

This script has been placed in the public domain.
No warrenties whatsoever. Use at your own risk.

End of docstring.

"""



import codecs
import sys
import os
import shutil

ospj = os.path.join

NL = '\n'
MAX_EMPTY_LINES = 2 or None

def normalizeEmptyLines(f1name, f2name, maxemptylines=None):
    # normalize_empty_lines.py
    # mb, 2012-05-20, 2012-05-20
    f1 = codecs.open(f1name, 'r', 'utf-8-sig')
    if f2name != '-':
        f2 = codecs.open(f2name, 'w', 'utf-8-sig')
    else:
        f2 = sys.stdout
    cnt = 0
    if not maxemptylines:
        for line in f1:
            f2.write(line)
    else:
        for line in f1:
            line = line.rstrip('\n')
            if line:
                while cnt > 0:
                    f2.write(NL)
                    cnt -= 1
                f2.write(line)
                f2.write(NL)
            else:
                if cnt < maxemptylines:
                    cnt += 1
                    
    if not f2 == sys.stdout:
        f2.close()


dry_run = False

def files(top='.', fext_list=None, fname_list=None, fstem_list=None, exclude_dirs=['_make']):
    for relpath, dirs, files in os.walk(top):
        dirs[:] = [d for d in sorted(dirs) if not d in exclude_dirs]
        files.sort()
        level = relpath.replace('\\','/').count('/')
        for fname in files:
            fstem, fext = os.path.splitext(fname)
            if ((fname_list and fname in fname_list) or
                (fext_list and fext in fext_list) or
                (fstem_list and fstem in fstem_list)):
                yield fname, relpath, level

if 0:
    for t in files(fext_list=['.yml']):
        print t

if 0:
    from pprint import pprint
    result = []
    for fname, relpath, level in rstFileVisitor():
        result.append(os.path.join(relpath, fname))
    pprint(result)


def tweakLiteralBlocks(f1name, outstream=sys.stdout):

    ## 000 some text:
    ## 001
    ## 002 ::
    ## 003
    ## 004     literal stuff

    linebuf = []
    withinliteral = False
    literalindent = None
    
    def emptyLineBuf(limit=None):
        cnt = 0
        while linebuf:
            if limit and cnt>=limit:
                break
            outstream.write(linebuf[0])
            outstream.write(NL)
            cnt += 1
            del linebuf[0]

    f1 = codecs.open(f1name, 'r', 'utf-8-sig')
    cnt = 0
    for line in f1:
        if withinliteral:
            indentation = len(line) - len(line.lstrip())
            if indentation < literalindent:
                emptyLineBuf()
                withinliteral = False
        linebuf.append(line.rstrip())
        if len(linebuf) == 5:
            if (1
                and len(linebuf[0])
                and not linebuf[0].count(linebuf[0][0]) == len(linebuf[0])
                and not linebuf[0].endswith('::')
                and not len(linebuf[1])
                and linebuf[2].lstrip()=='::'
                and not len(linebuf[3])
                and len(linebuf[4])):
                if linebuf[4][0] in '\t ':
                    if linebuf[0].endswith(':'):
                        linebuf[0] += ':'
                    else:
                        linebuf[0] += ' ::'
                    del linebuf[1:3]
                    withinliteral = True
                    literalindent = len(linebuf[2]) - len(linebuf[2].lstrip())
                    emptyLineBuf()
                else:
                    emptyLineBuf(1)
            else:
                emptyLineBuf(1)
    emptyLineBuf()


def tweakDocumentTop(fpath, level):
    for_your_information = """\
.. ==================================================
.. FOR YOUR INFORMATION
.. --------------------------------------------------
.. -*- coding: utf-8 -*- with BOM.
"""

    define_some_textroles = """\
.. ==================================================
.. DEFINE SOME TEXTROLES
.. --------------------------------------------------
.. role::   underline
.. role::   typoscript(code)
.. role::   ts(typoscript)
   :class:  typoscript
.. role::   php(code)
"""
    f1 = codecs.open(fpath, 'r', 'utf-8')
    data = f1.read().lstrip()
    f1.close()
    changed = False
    p1 = data.find(for_your_information)
    if p1 > -1:
        p2 = p1 + len(for_your_information)
        data = (data[:p1] + data[p2:]).lstrip()
        changed = True

    p1 = data.find(define_some_textroles)
    if p1 > -1:
        p2 = p1 + len(define_some_textroles)
        data = (data[:p1] + data[p2:]).lstrip()
        changed = True

    firstline = data.split('\n', 1)[0].rstrip()
    if firstline.startswith('.. include::') and firstline.endswith('Images.txt'):
        p1 = data.find('Images.txt')
        p2 = p1 + len('Images.txt')
        include_images = data[:p2]
        data = data[p2:].lstrip()
        changed = True
    else:
        include_images = ''
      
    if changed:
        f2 = codecs.open(fpath, 'w', 'utf-8')
        f2.write(for_your_information)
        f2.write(NL)
        f2.write('.. include:: %sIncludes.txt' % ('../'*level))
        f2.write(NL)
        if include_images:
            f2.write(include_images)
            f2.write(NL)
        f2.write(NL)
        f2.write(NL)
        f2.write(data)
        f2.close()


def tweakImagesTxt(fpath):
    lines = []
    f1 = codecs.open(fpath, 'r', 'utf-8')
    for line in f1:
        if line.startswith('   :width:') or line.startswith('   :height:'):
            line = '..' + line[2:]
        lines.append(line)
    f1.close()
    f2 = codecs.open(fpath, 'w', 'utf-8')
    for line in lines:
        f2.write(line)
    f2.close()


def main():
    
    if 1 and "improve *.rst files":
        for fname, relpath, level in files(fext_list=['.rst']):
            f1path = ospj(relpath, fname)
            print f1path
            f2path = '%s.temp' % f1path
            if 1:
                f2 = codecs.open(f2path, 'w', 'utf-8')
                tweakLiteralBlocks(f1path, f2)
                f2.close()
            if 1:
                tweakDocumentTop(f2path, level)
            if not dry_run:
                os.remove(f1path)
                os.rename(f2path, f1path)

    if 1 and "improve Images.txt files":
        for fname, relpath, level in files(fname_list=['Images.txt']):
            f1path = ospj(relpath, fname)
            print f1path
            f2path = '%s.temp' % f1path
            shutil.copyfile(f1path, f2path)
            tweakImagesTxt(f2path)
            if not dry_run:
                os.remove(f1path)
                os.rename(f2path, f1path)


def usage():
    print
    print __doc__

if __name__ == "__main__":

    if 0 and 'this is old stuff':
        if len(sys.argv) < 2 or len(sys.argv) > 3:
            print 'usage: python %s <infile.utf8.rst.txt> [<outfile.utf8.rst.txt>]' % sys.argv[0]# 
            print '       Normalize maximum number of empty line following immediately'
            print '       upon each other. Number is: %s' % MAX_EMPTY_LINES
            sys.exit(2)

        f1name = sys.argv[1]
        if len(sys.argv) == 3:
            f2name = sys.argv[2]
        else:
            f2name = '-'
        normalizeEmptyLines(f1name, f2name, MAX_EMPTY_LINES)


    # harzard prevention ...
    if (os.path.split(os.path.abspath('.'))[-1:] == ('Documentation',)
        and os.path.exists('Index.rst')
        and len(sys.argv)==1):
        main()
    else:
        usage()
