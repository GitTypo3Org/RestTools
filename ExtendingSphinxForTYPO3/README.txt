==========
README.txt
==========

mb, 2012-05-30, 2013-03-16

ExtendingSphinxForTYPO3 is a Python package that extends the capabilities
of Sphinx specifically for TYPO3. After installation it can be loaded
in Python as module 't3sphinx'::

  import t3sphinx

The package has been tested with Python 2.x. At the moment it will
probably not run with Python 3.x.

Installation
============

To install go to the directory ./ExtendingSphinxForTYPO3 where the
setup.py file is located and run ``python setup.py install``. To
reinstall you can do this as often as you want.

At the commandline::

  $ cd ./ExtendingSphinxForTYPO3
  $ python setup.py install

or maybe, if you need to be administrator on linux::

  $ cd ./ExtendingSphinxForTYPO3
  $ sudo python setup.py install

.. important::

   To make anything work of what this module 't3sphinx' provides
   you have to manually add the codeblock from
   ``ExtendingSphinxForTYPO3/src/t3sphinx/resources/typo3_codeblock_for_conf.py`` to your
   ``conf.py`` file.


What does it do?
================

Assuming that your conf.py contains the ``typo3_codeblock_for_conf.py``
code block:

- It provides the 'typo3sphinx' theme and sets ``html_theme = 'typo3sphinx'``
- It provides GlobalSettings.yml (YAML)
- It will read and apply GlobalSettings.yml and Settings.yml (YAML)
- It makes the "t3-field-list-table" directive available.
  See http://mbless.de/4us/typo3-oo2rest/06-The-%5Bfield-list-table%5D-directive/1-demo.rst.html
  for a preliminary description. Other than described there use
  ``t3-field-list-table`` instead of ``field-list-table``.


Updates of ExtendingSphinxForTYPO3
==================================

A typical commit message is this:

Update the TYPO3 specific extensions for Sphinx to reflect the lastest
state we are using on the server.

Whenever a new version of "ExtendingSphinxForTYPO3" is issued do these
three steps to update your local machine::

  $ git clone git://git.typo3.org/Documentation/RestTools.git RestTools
  $ cd RestTools/ExtendingSphinxForTYPO3
  $ (sudo) python setup.py install

Enjoy!

End.
