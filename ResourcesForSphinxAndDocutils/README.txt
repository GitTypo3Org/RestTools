README.txt ResourcesForSphinxAndDocutils

The folder res/ should be available on your machine when you are
using Docutils or Sphinx for TYPO3 documentation. It is supposed
to provide resources that are special to TYPO3 documentation.

To use the 'typo3sphinx' theme make sure that the path in 'conf.py'
of your Sphinx documentation project points to the correct theme
path. Example::

   in 'conf.py':

   # -- Options for HTML output ---------------------------------------------------
   
   # The theme to use for HTML and HTML Help pages.  Major themes that come with
   # Sphinx are currently 'default' and 'sphinxdoc'.
   # Available themes are:
   # basic, default, sphinxdoc, scrolls, agogo, nature, pyramid, haiku, traditional, epub
   # our own new theme is 'typo3sphinx'. Its a mutant of 'sphinxdoc'.
   
   html_theme = 'typo3sphinx'

   # $ # To find themes on your server:
   # $ locate /sphinxdoc/

   # Add any paths that contain custom themes here, relative to this directory.
   # html_theme_path = []
   html_theme_path = ['../../../../../res/sphinx/themes/', '/usr/share/sphinx/themes/']
  
   

End.

