mb, 2013-07-11, 2013-07-11

typoscript.py


Feature #49880
TypoScript Highlighting

Added by Michiel Roos
Status: Accepted
Start date: 2013-07-11
Priority: Must have
Due date: 
Assignee: Michiel Roos
Category: -

Description

Sections marked with :ts: should be syntaxhighlighted as TypoScript.

This requires a TypoScript Lexer for the Pygments code highlighter.

Please find a testing version attached.

I still need to fix the highlighting of the inclusion of toplevel 
objects (lib.something =< lib.somethingElse).

Otherwise it works fine for:
- comments
- braces
- numbers
- functions
- content objects
- operators
- punctuation
- constants
- registers etc.
- paths
- strings (html)
- markers

End of README.txt