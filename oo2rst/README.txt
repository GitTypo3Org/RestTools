oo2rst - Convert OpenOffice documents to reStructuredText
=========================================================

The conversions process involves several steps. We need OpenOffice
and a basic `Python 2.7 installation <http://python.org/download/>`_ 
for this. The Python 2.7 requirement is due to the ``argparse`` module
we using for commandline parsing.

The filenames in this documentation are:

==== ====================  =============================================
id   filename              type
==== ====================  =============================================
(1)  example.odt           OpenOffice source file (*.sxw, *.odt, *.ott, ...)
(2)  example.html          written by OpenOffice
(3)  example-tweaked.html  an intermediate file created by the preprocessor
(4)  example.rst           the desired result in reSt format
==== ===================== =============================================


Step 1: Save the OpenOffice document as HTML
--------------------------------------------

In step 1 we are reading (1) and writing (2). We are using 
`LibreOffice 3.4 <http://www.libreoffice.org/>`_ for this 
step. Just open the document and "Save as HTML". This can be done at the
commandline as well. As result you should have ``example.html`` and
possibly image files. Let's move the images to a subfolder ``./img/``.

Windows commandline::

  soffice.exe  --headless  -convert-to html  example.sxw
  md img
  mv *.png img
  mv *.gif img
  
MacOs commandline::
  alias soffice='/Applications/LibreOffice.app/Contents/MacOS/soffice'
  soffice  --headless  -convert-to html  example.sxw
  mkdir img
  mv *.{png,gif} img/

  
Step 2: Preprocessing
---------------------

In this step we go from (2) to (3). OpenOffice creates 
``HTML 4.0 Transitional``. That doctype is a bit difficult to parse 
because several closing tags are considered optional. 
And in fact closing tags for </li>, </dl> and some more are missing. 
The preprocessor will insert these missing tags. And it will try to 
fix errors that may be there. For example there is a closing 
``</span>`` near the beginning that has not been opened before. 
It will be removed.

Commandline::

  python  tweak_oohtml.py  example.html  example-tweaked.html

Or, depending on your Python installation::

  tweak_oohtml  example.html  example-tweaked.html
  tweak_oohtml --help

  
Step 3: Convert to reST
-----------------------

Now we are doing the final step and go from (3) to (4). In case of
error you may want to manually correct (3). If there is a valid
construct in (3) you think the parser should be able to handle:
Let us know!

Commandline::

  python oo2rst.py  example-tweaked.html  example.rst


Finally
-------

Let's work together - and happy converting!


Note:
-----

Afterwards you should be able to turn your reST document into an
HTML document as well. This requires the Python package 
`Docutils <http://docutils.sourceforge.net/>`_ to be installed::

  rst2html example.rst example-regenerated-from-rst.html
  
If the generator complains about not knowing about directive 
``field-list-table`` this is because that directive doesn't belong to
the Docutils core yet.

You can help yourself this way: Locate every line in the reST file
starting with ``.. field-list-table::``.
Insert a blank at the beginning of each line up to the next
blank line. And replace ``::`` by ``: :``. This way the directive is
disabled.

Example: find::

  .. field-list-table::
   :header-rows: 1
   :class: striped-table

and change it to the following - where X stands for a blank::

  X.. field-list-table:X:
  X :header-rows: 1
  X :class: striped-table

Afterwards the table content will be rendered as a doubly nested list.
