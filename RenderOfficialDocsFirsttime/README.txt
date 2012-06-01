==============================
render-official-docs-firsttime
==============================

:author: Martin Bless
:email:  martin@mbless.de

:date:   2012-06-01

"""

What is this?
=============

This is "cool stuff" that creates a whole TYPO3 Sphinx Documentation
project from one 'manual.sxw' in just one step!


What does it do?
================

This package creates the complete initial version of a
TYPO3 ReST Documentation project ready for Sphinx.
Input is an OpenOffice document named 'manual.sxw'.

'sxwfile' should a filepath pointing to 'manual.sxw'. It needs to
be made like this::

  sxwfile = '.../Example.git/Documentation/_not_versioned/_genesis/manual.sxw'

Expected input is:

  Example.git
  |-- Documentation/
      |-- _not_versioned/
          |-- _genesis/
              |-- manual.sxw


Output will be like this:

  Example.git
  |-- .gitignore
  |-- Documentation/
      |-- source/
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

  If source/ has ONLY ONE subfolder, the paths to the images in Images.txt
  will be made on '../' too short on purpose. The reason for this is that
  in this case you'll be willing to move everything in 01-subfolder/ up
  one level. After moving the paths will be correct.

  And you will have to merge these two files manually::

    source/Index.rst
    source/01-subfolder/Index.rst

  And, if present, you will have to merge these two files manually::

    source/Images.txt
    source/01-subfolder/Images.txt
  
End.



