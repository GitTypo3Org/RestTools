# 1_do_the_work.py
# mb, 2012-05-20, 2012-06-29

# status: works well, but code is still pretty messy ...

"""
What does it do?
================

This package creates the complete initial version of a
TYPO3 ReST Documentation project ready for Sphinx.
Input is an OpenOffice document named 'manual.sxw'.

'sxwfile' should a filepath pointing to 'manual.sxw'. It needs to
be made like this::

  sxwfile = '.../Example.git/Documentation/_not_versioned/_genesis/manual.sxw'

Expected input is:

  Example.git/
  |-- .gitignore
  |-- Documentation/
      |-- Index.rst
      |-- (Images.txt)
      |-- Images/
      |-- 01-subfolder/
          |-- Index.rst
          |-- (Images.txt)
          |-- 01-01-subfolder/
              |-- Index.rst
          |-- ...
      |-- ...
      |-- _make/
          |-- conf.py
          |-- make.bat
          |-- make-html.bat
          |-- Makefile
          |-- build/
              |-- .gitignore
      |-- _not_versioned/
          |-- .gitignore
          |-- _genesis/
              |-- manual.sxw
              |-- ...
              |-- temp/
          |-- warnings.txt


Note::

  If ReST sources have ONLY ONE subfolder, the paths to the images in Images.txt
  will be made one '../' too short deliberately. The reason for this is that
  in this case you'll be willing to move everything in 01-subfolder/ up
  one level. After moving the paths will be correct.

  And you will have to merge these two files manually::

    Documentation/Index.rst
    Documentation/01-subfolder/Index.rst

  And, if present, you will have to merge these two files manually::

    Documentation/Images.txt
    Documentation/01-subfolder/Images.txt


2012-06-21
  New: start a single conversion from the commandline as
  python  1_do_the_work.py  [.../]Documentation/_not_versioned/_genesis/manual.sxw

2012-06-21
  Note:
    This package works on Windows as well if you open the manual in OpenOffice
    and save it manually as HTML to 
      [.../]Documentation/_not_versioned/_genesis/manual.html

    tidy.exe needs to be in you path.
 
""" 

history = \
"""
2012-06-29 find 'res' relative to 'scriptdir'
2012-06-21 Change folder structure
"""


import copyclean
import subprocess
import os
import sys
import ooxhtml2rst
import normalize_empty_lines
import slice_to_numbered_files
import write_sphinx_structure
import shutil

ospj = os.path.join
ospe = os.path.exists
osps = os.path.split

scriptdir = os.path.dirname(sys.argv[0])
resdir = ospj(scriptdir, 'res')
mockup_uno = 'win' in os.sys.platform
printfilenames = 0

if not mockup_uno:
    import documentconverter as dc
    converter = dc.DocumentConverter()    

usr_bin_python = '/usr/bin/python'
rst2html_script = '/usr/local/bin/rst2htmltypo3.py'

finaldestdirroot = '/home/mbless/public_html/typo3'

if mockup_uno:
    usr_bin_python = 'D:\Python27\python.exe'
    rst2html_script = 'D:\\Python27\\Scripts\\rst2htmltypo3.py'

def convertsxw2html(srcfile, destfile):
    error = None
    if mockup_uno:
        pass
        # file(destfile,'w').close()
    else:    
        try:
            converter.convert(srcfile, destfile)
        except dc.DocumentConversionException, exception:
            error = "ERROR1! " + str(exception)
        except dc.ErrorCodeIOException, exception:
            error = "ERROR2! " % str(exception)
        except Exception, msg:
            error = "ERROR9! " + str(msg)
    return error



def main(sxwfile):
    if not sxwfile.endswith('manual.sxw'):
        return
    left, right = os.path.split(sxwfile)
    if left:
        left, right = os.path.split(left)
    if not right == '_genesis':
        return
    if not left:
        return
    left, right = os.path.split(left)
    finalsourcedir = left.replace('\\', '/')
    finaldocumentationdir = finalsourcedir
    repositoryname = os.path.split(os.path.split(finaldocumentationdir)[0])[1].replace('\\', '/')
    finalbuilddir = ospj(left, '_make', 'build').replace('\\', '/')
    finalnotversioneddir = ospj(left, '_not_versioned').replace('\\', '/')
    sxwfile = sxwfile.replace('\\', '/')
    destdir = '/'.join(sxwfile.split('/')[:-1]).replace('\\', '/')

    print
    if 1 or printfilenames:
        print 'repositoryname      :', repositoryname
        print 'finalsourcedir      :', finalsourcedir
        print 'finalbuilddir       :', finalbuilddir
        print 'finalnotversioneddir:', finalnotversioneddir
        print 'destdir             :', destdir
    
    if not mockup_uno:
        # sxw -> html
        srcfile = sxwfile
        destfile = sxwfile[:-4] + '.html'
        if 1 and printfilenames:
            print 1, srcfile
            print 2, destfile
        else:
            print repositoryname, '/'.join(srcfile.split('/')[-2:])
            print repositoryname, '/'.join(destfile.split('/')[-2:])
        if 1:
            error = convertsxw2html(srcfile, destfile)
            if error:
                print error


    # html -> cleaned
    srcfile = sxwfile[:-4] + '.html'
    destfile = sxwfile[:-4] + '-cleaned.html'
    if 1 and printfilenames:
        print 1, srcfile
        print 2, destfile
    else:
        print repositoryname, '/'.join(destfile.split('/')[-2:])
    if 1:
        copyclean.main(srcfile, destfile)
   

    # cleaned -> from-tidy
    srcfile = sxwfile[:-4] + '-cleaned.html'
    destfile = sxwfile[:-4] + '-from-tidy.html'
    if 1 and printfilenames:
        print 1, srcfile
        print 2, destfile
    else:
        print repositoryname, '/'.join(destfile.split('/')[-2:])
    if 1:
        errorfile = ospj(destdir, 'tidy-error-log.txt')
        cmd = ' '.join(['tidy', '-asxhtml', '-utf8', '-f', errorfile, '-o', destfile, srcfile])
        if os.path.exists(destfile):
            os.remove(destfile)
        returncode = subprocess.call(cmd, shell=True)


    # manual-from-tidy.html -> manual.rst
    # python ooxhtml2rst-work-in-progress.py  --treefile=$EXTENSIONS/$EXTKEY/nightly/restparser-tree.txt --logfile=$EXTENSIONS/$EXTKEY/nightly/restparser-log.txt  $EXTENSIONS/$EXTKEY/nightly/2-from-tidy.html $EXTENSIONS/$EXTKEY/nightly/manual.rst  1>&2 2>$EXTENSIONS/$EXTKEY/nightly/restparser-errors.txt

    srcfile = ospj(destdir, 'manual-from-tidy.html').replace('\\','/')
    destfile = ospj(destdir, 'manual.rst').replace('\\','/')
    treefile = f3name = ospj(destdir, 'restparser-tree.txt')
    logfile = f4name = ospj(destdir, 'restparser-log.txt')
    if 1 and printfilenames:
        print 1, srcfile
        print 2, destfile
    else:
        print repositoryname, '/'.join(destfile.split('/')[-2:])
    if 1:
        if ospe(destfile):
            os.remove(destfile)
        # ooxhtml2rst.main(f1name, f2name, f3name=None, f4name=None, appendlog=0, taginfo=0):
        ooxhtml2rst.main( srcfile, destfile, treefile, logfile)



    # normalize_empty_lines
    srcfile = ospj(destdir, 'manual.rst').replace('\\','/')
    destfile = ospj(destdir, 'manual-empty-lines-normalized.rst').replace('\\','/')
    if 1 and printfilenames:
        print 1, srcfile
        print 2, destfile
    else:
        print repositoryname, '/'.join(destfile.split('/')[-2:])
    if 1:
        normalize_empty_lines.main(srcfile, destfile, 2)
        os.remove(srcfile)
        os.rename(destfile, srcfile)


    # first slicing
    srcfile = ospj(destdir, 'manual.rst').replace('\\','/')
    tempdir = ospj(destdir, 'temp').replace('\\','/')
    if 1 and printfilenames:
        print 1, srcfile
        print 2, tempdir
    else:
        print repositoryname, '/'.join(tempdir.split('/')[-2:])
    if 1:
        slice_to_numbered_files.main(srcfile, tempdir)
    

    # final file structure
    print repositoryname, '/'.join(finalsourcedir.split('/')[-2:])
    srcdirimages = destdir
    if 1 and printfilenames:
        print 1, tempdir
        print 2, finalsourcedir
        print 3, srcdirimages
    if 1:
        write_sphinx_structure.main(tempdir, finalsourcedir, srcdirimages, verbose=0)



    # res files
    destdir = ospj(finalsourcedir, '_make')
    if not ospe(destdir):
        os.makedirs(destdir)
    files = os.listdir(resdir)
    for afile in files:
        if afile in ['default_conf.py', 'default_make.bat', 'default_make-html.bat', 
                     'default_Makefile', ]:
            destname = afile[len('default_'):]
            destpath = ospj(destdir, destname)
            if not ospe(destpath):
                srcpath = ospj(resdir, afile)
                shutil.copyfile(srcpath, destpath)

    if not ospe(finalbuilddir):
        os.makedirs(finalbuilddir)

    # .gitignore
    srcpath = ospj(resdir, 'default_gitignore_toplevel')
    destpath = ospj(finaldocumentationdir, '.gitignore')
    if not ospe(destpath):
        shutil.copyfile(srcpath, destpath)

    # .gitignore
    srcpath = ospj(resdir, 'default_gitignore_all_in_this_folder')
    destpath = ospj(finalbuilddir, '.gitignore')
    if not ospe(destpath):
        shutil.copyfile(srcpath, destpath)

    # .gitignore
    srcpath = ospj(resdir, 'default_gitignore_all_in_this_folder')
    destpath = ospj(finalnotversioneddir, '.gitignore')
    if not ospe(destpath):
        shutil.copyfile(srcpath, destpath)


    # more
    # place warnings.txt there for illustration
    f2path = ospj(finalnotversioneddir, 'warnings.txt')
    if not ospe(f2path):
        f2 = file(f2path,'w')
        f2.close()

    print repositoryname, 'done.'

    return

usage = """
Usage:
  python  %s  <infile>

  where infile is the absolute or relative path to manual.sxw. The path must end as
  .../<any package name>/Documentation/_not_versioned/_genesis/manual.sxw
  For more info see docstring in script
  '%s'.

""" % (sys.argv[0], sys.argv[0])


if __name__=="__main__":

    if 0 and 'set parameter while developing ...':
        sys.argv[1:] = [r'D:\Repositories\svn.typo3.org\TYPO3v4\piwikintegration\Documentation\_not_versioned\_genesis\manual.sxw']

    if len(sys.argv) == 2:
        sxwfile = sys.argv[1]
        main(sxwfile)
    else:
        print usage
        print __doc__

    if 0: # to be removed soon!?
        import list_of_sxw_manuals
        for sxwfile in list_of_sxw_manuals.files:
            if mockup_uno:
                p = sxwfile.find('git.typo3.org/')
                if p > -1:
                    sxwfile = 'D:/TYPO3-Documentation/t3doc-srv123-mbless/' + sxwfile[p:]
            main(sxwfile)
