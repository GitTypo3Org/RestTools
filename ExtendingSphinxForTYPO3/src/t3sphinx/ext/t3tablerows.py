# -*- coding: utf-8 -*-
"""
    t3sphinx.ext.t3tablerows
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Do something about the .. container:: table-row parts

    :copyright: Copyright 2007-2011 by the Sphinx team, see AUTHORS. ))
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes

emit_info = 0

good_term_combinations = [
    # (0, '10', [                                                ]),
    # (0, '11', ['property'                                      ]),
    # (0, '12', [            'datatype',                         ]),
      (0, '13', ['property', 'datatype',                         ]),
    # (0, '14', [                        'description',          ]),
      (0, '15', ['property',             'description',          ]),
      (0, '16', [            'datatype', 'description',          ]),
      (0, '17', ['property', 'datatype', 'description',          ]),
    # (0, '18', [                                       'default']),
      (0, '19', ['property'                             'default']),
      (0, '1a', [            'datatype',                'default']),
      (0, '1b', ['property', 'datatype',                'default']),
      (0, '1c', [                        'description', 'default']),
      (0, '1d', ['property',             'description', 'default']),
      (0, '1e', [            'datatype', 'description', 'default']),
      (0, '1f', ['property', 'datatype', 'description', 'default']),

    # (0, '20', [                                            ]),
    # (0, '21', ['datatype',                                 ]),
    # (0, '22', [            'examples',                     ]),
      (0, '23', ['datatype', 'examples'                      ]),
    # (0, '24', [                        'comment'           ]),
      (0, '25', ['datatype',             'comment',          ]),
      (0, '26', [            'examples', 'comment',          ]),
      (0, '27', ['datatype', 'examples', 'comment',          ]),
    # (0, '28', [                                   'default']),
      (0, '29', ['datatype',                        'default']),
      (0, '2a', [            'examples',            'default']),
      (0, '2b', ['datatype', 'examples',            'default']),
      (0, '2c', [                        'comment', 'default']),
      (0, '2d', ['datatype',             'comment', 'default']),
      (0, '2e', [            'examples', 'comment', 'default']),
      (0, '2f', ['datatype', 'examples', 'comment', 'default']),

    # (0, '30', [                                          ]),
    # (0, '31', ['var',                                    ]),
    # (0, '32', [       'phptype',                         ]),
      (0, '33', ['var', 'phptype',                         ]),
    # (0, '34', [                  'description',          ]),
      (0, '35', ['var',            'description',          ]),
      (0, '36', [       'phptype', 'description',          ]),
      (0, '37', ['var', 'phptype', 'description',          ]),
    # (0, '38', [                                 'default']),
      (0, '39', ['var',                           'default']),
      (0, '3a', [       'phptype',                'default']),
      (0, '3b', ['var', 'phptype',                'default']),
      (0, '3c', [                  'description', 'default']),
      (0, '3d', ['var',            'description', 'default']),
      (0, '3e', [       'phptype', 'description', 'default']),
      (0, '3f', ['var', 'phptype', 'description', 'default']),

    # (0, '40', [                                         ]),
    # (0, '41', ['key',                                   ]),
    # (0, '42', [       'datatype',                       ]),
      (0, '43', ['key', 'datatype',                       ]),
    # (0, '44', [                   'description',        ]),
      (0, '45', ['key',             'description',        ]),
      (0, '46', [       'datatype', 'description',        ]),
      (0, '47', ['key', 'datatype', 'description',        ]),
    # (0, '48', [                                  'scope']),
      (0, '49', ['key',                            'scope']),
      (0, '4a', [       'datatype',                'scope']),
      (0, '4b', ['key', 'datatype',                'scope']),
      (0, '4c', [                   'description', 'scope']),
      (0, '4d', ['key',             'description', 'scope']),
      (0, '4e', [       'datatype', 'description', 'scope']),
      (0, '4f', ['key', 'datatype', 'description', 'scope']),

    ]

def checkCombinationOfTerms(terms):
    rowid = None
    found = False
    #if terms == ['property', 'datatype', 'description', 'default']:
    #    x = 1

    for rowtype, rowid, L in good_term_combinations:
        # if terms == [t for t in L if t in terms]:
        if terms == L:
            found = True
            break
    return rowtype, rowid, found

def transform_definition_list(dl, app, docname=''):
    # app.warn(self, message, location=None, prefix='WARNING: '):
    t3row = []
    terms = []
    for dli in dl:
        found = False
        if not type(dli) == nodes.definition_list_item:
            app.warn("strange definition-list child '%s' (ignored) in t3sphinx.ext.t3tablerows" % (type(dli),))
            continue
        li = dli[:1]
        if not len(li):
            app.warn("problem ...  in t3sphinx.ext.t3tablerows")
            continue
        else:
            li = li[0]
        if not type(li) == nodes.term:
            app.warn("problem ...  in t3sphinx.ext.t3tablerows")
            continue
        else:
            term = li.astext()
            term = term.replace(' ','')
            term = term.replace('-','')
            term = term.lower()
            terms.append(term)
    rowtype, rowid, found = checkCombinationOfTerms(terms)

    if not found:
        if emit_info:
            app.info("definition terms %r do not qualify for transformation of 'table-row' in %s" % (terms, docname))
    else:
        t3row = nodes.container()
        for dli in dl:
            # pass 2
            for li in dli:
                if type(li) == nodes.term:
                    term = li.astext()
                    termclass = term
                    termclass = termclass.replace(' ','')
                    termclass = termclass.replace('-','')
                    termclass = termclass.lower()
                    classes = []
                    classes.append('t3-cell')
                    classes.append('t3-cell-%s' % (termclass, ))
                    classes.append('t3-cell-rt%s' % (rowtype, ))
                    classes.append('t3-cell-id%s' % (rowid, ))
                    cell = nodes.container(classes=classes)
                    cell.append(nodes.paragraph(text=term, classes=['term']))
                    t3row.append(cell)
                elif type(li) == nodes.definition:
                    cell.extend(li[:])
                else:
                    app.warn("strange definition-list-item child '%s' (ignored) in t3sphinx.ext.t3tablerows" % (type(li),))

    if len(t3row):
        classes = []
        classes.append('t3-row')
        classes.append('t3-row-rt%s' % rowtype)
        classes.append('t3-row-id%s' % rowid)
        t3row.attributes['classes'] = classes
        t3row.append(nodes.container(classes=['cc'])) # div with: clear:both;
    else:
        t3row = None

    return t3row, found


# def traverse(self, condition=None, include_self=1, descend=1, siblings=0, ascend=0):

def tableRowContainerFilter(node):
    if type(node) == nodes.container:
        if 'table-row' in node.attributes.get('classes', []):
            return True
    return False


## Sphinx core events (hooks)
##
## http://sphinx-doc.org/latest/ext/appapi.html#sphinx-core-events
##
## builder-inited(app)
## env-get-outdated(app, env, added, changed, removed)
## env-purge-doc(app, env, docname)
## source-read(app, docname, source)
## doctree-read(app, doctree)
## missing-reference(app, env, node, contnode)
## doctree-resolved(app, doctree, docname)
## env-updated(app, env)
## html-collect-pages(app)
## html-page-context(app, pagename, templatename, context, doctree)
## build-finished(app, exception)


def doctreeRead(app, doctree, docname=None):
    env = app.builder.env

    docname = docname or env.docname
    for hit in doctree.traverse(condition=tableRowContainerFilter):
        for child in hit:
            if type(child) == nodes.definition_list:
                transformed, found = transform_definition_list(child, app, docname)
                if found:
                    if len(hit) == 1:
                        # replace .. container:: table-row
                        hit.replace_self([transformed])
                    else:
                        child.replace_self([transformed])

def setup(app):
    app.connect('doctree-read', doctreeRead) # works


if __name__=="__main__":
    print "Hi"


## <bullet_list bullet="-" classes="simple">
##     <list_item>
##        <paragraph classes="first">
##            aaaaa
##    <list_item>
##        <paragraph classes="first">
##            bbbbb
##    <list_item>
##        <paragraph classes="first">
##            ccccc

##
## <definition_list classes="docutils">
##     <definition_list_item>
##         <term>
##             Property
##         <definition>
##             <paragraph classes="first last">
##                 Name of the property
##



##<container classes="table-row container">
##    <definition_list classes="docutils">
##        <definition_list_item>
##            <term>
##                Property
##            <definition>
##                <paragraph classes="first last">
##                    Property:
##        <definition_list_item>
##            <term>
##                Data type
##            <definition>
##                <paragraph classes="first last">
##                    Data type:
##        <definition_list_item>
##            <term>
##                Description
##            <definition>
##                <paragraph classes="first last">
##                    Description:
##        <definition_list_item>
##            <term>
##                Default
##            <definition>
##                <paragraph classes="first last">
##                    Default:


##.t3-row {
##	margin-top: 20px;
##	margin-bottom: 20px;
##	border-top: 1px solid #b0b0b0;
##	background-color: #f0f0f0;
##	padding: 20px;
##
##}
##.t3-cell-property {
##	font-weight: bold;
##	float:left;
##	width: 49%;
##}
##.t3-cell-datatype {
##	font-weight: normal;
##	float:left;
##	width: 49%;
##}
##.t3-cell-description {
##	clear: both;
##	padding-top: 20px;
##	background-color: white;
##}
##.t3-cell-default {
##	background-color: white;
##}
