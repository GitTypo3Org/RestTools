README.txt

apply-forge-typo3-org-issues-42376.py  2012-10-25, 2012-10-27

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
