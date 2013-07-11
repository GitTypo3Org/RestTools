# -*- coding: utf-8 -*-
"""
    pygments.lexers.typoscript
    ~~~~~~~~~~~~~~~~~~~~~~

    Pygments lexers for TypoScript

    :copyright: Copyright 2013-now by Donation Based Hosting.
    :license: BSD, see LICENSE for details.
"""
import re

from pygments.lexer import RegexLexer, include, bygroups, using
from pygments.token import Keyword, Text, Comment, Name, String, Number, \
                           Operator, Punctuation
from pygments.lexer import DelegatingLexer
from pygments.lexers.web import HtmlLexer, CssLexer


__all__ = ['TypoScriptLexer', 'TypoScriptCssLexer', 'HtmlTypoScriptLexer', 'TypoScriptDataLexer']

class TypoScriptCssLexer(DelegatingLexer):
    """
    Subclass of the `VelocityLexer` that highlights unlexer data
    with the `CssLexer`.

    """
    def __init__(self, **options):
        super(TypoScriptCssLexer, self).__init__(TypoScriptLexer, CssLexer,
                                              **options)

class HtmlTypoScriptLexer(DelegatingLexer):
    """
    Subclass of the `TypoScriptDataLexer` that highlights unlexer data
    with the `HtmlLexer`.

    """
    def __init__(self, **options):
        super(HtmlTypoScriptLexer, self).__init__(TypoScriptDataLexer, HtmlLexer,
                                              **options)

class TypoScriptDataLexer(RegexLexer):
    """
    """
    name = 'TypoScriptData'
    aliases = ['typoscriptdata']

    tokens = {
        'root': [
							# marker: ###MARK###
            (r'(.*)(###\w+###)(.*)', bygroups(String, Name.Constant, String)),
							# constant: {$some.constant}
            (r'(.*)(\{)(\$)([\w-]+\.)*([\w-]+)(\})(.*)',
								bygroups(String, String.Symbol, Operator, Name.Constant, Name.Constant, String.Symbol, String)), # constant
							# constant: {register:somevalue}
						(r'(.*)(\{)([\w-]+(?:(\:)))*([\w-]+)(\})(.*)',
								bygroups(String, String.Symbol, Name.Constant, Operator, Name.Constant, String.Symbol, String)), # constant
						(r'<[^\s][^\n>]*>', String),
				]
		}

class TypoScriptLexer(RegexLexer):
    """

    """
    name = 'TypoScript'
    aliases = ['typoscript']
    filenames = ['*.ts','*.txt']
    mimetypes = ['text/typoscript']

    flags = re.DOTALL | re.MULTILINE

    tokens = {
        'root': [
            include('comment'),
            include('constant'),
            include('html'),
            include('punctuation'),
            include('operator'),
            include('label'),
            include('whitespace'),
						include('keywords'),
            include('structure'),
            include('literal'),
            include('other'),
        ],
        'keywords': [
							# Conditions
						(r'(\[)(?i)(browser|compatVersion|dayofmonth|dayofweek|dayofyear|device|ELSE|END|GLOBAL|globalString|globalVar|hostname|hour|IP|language|loginUser|loginuser|minute|month|page|PIDinRootline|PIDupinRootline|system|treeLevel|useragent|userFunc|usergroup|version)([^\]]*)(\])', bygroups(String.Symbol, Name.Constant, Text, String.Symbol)),
							# Functions
						(r'(?=[\w-])(HTMLparser|HTMLparser_tags|addParams|cache|encapsLines|filelink|if|imageLinkWrap|imgResource|makelinks|numRows|numberFormat|parseFunc|replacement|round|select|split|stdWrap|strPad|tableStyle|tags|textStyle|typolink)(?![\w-])', Name.Function),
							# Toplevel objects FIXME
						(r'(?:(=\s*<?\s*)|(^\s*))(cObj|field|config|content|constants|FEData|file|frameset|includeLibs|lib|page|plugin|register|resources|sitemap|sitetitle|styles|temp|tt_[^\.]*|types|xmlnews|_GIFBUILDER)(?![\w-])', Name.Builtin),
							# Content objects
						(r'(?=[\w-])(CASE|CLEARGIF|COA|COA_INT|COBJ_ARRAY|COLUMNS|CONTENT|CTABLE|EDITPANEL|FILE|FILES|FLUIDTEMPLATE|FORM|HMENU|HRULER|HTML|IMAGE|IMGTEXT|IMG_RESOURCE|LOAD_REGISTER|MEDIA|MULTIMEDIA|OTABLE|QTOBJECT|RECORDS|RESTORE_REGISTER|SEARCHRESULT|SVG|SWFOBJECT|TEMPLATE|TEXT|USER|USER_INT)(?![\w-])', Name.Class),
							# Menu states
						(r'(?=[\w-])(ACT|ACTIFSUB|ACTIFSUBRO|ACTRO|CUR|CURIFSUB|CURIFSUBRO|CURRO|IFSUB|IFSUBRO|NO|SPC|USERDEF1|USERDEF1RO|USERDEF2|USERDEF2RO|USR|USRRO)', Name.Class),
							# Menu objects
						(r'(?=[\w-])(GMENU|GMENU_FOLDOUT|GMENU_LAYERS|IMGMENU|IMGMENUITEM|JSMENU|JSMENUITEM|TMENU|TMENUITEM|TMENU_LAYERS)', Name.Class),
							# PHP objects
						(r'(?=[\w-])(PHP_SCRIPT(_EXT|_INT)?)', Name.Class),
						(r'(?=[\w-])(userFunc)(?![\w-])', Name.Function),
        ],
        'whitespace': [
            (r'\s+', Text),
        ],
				'html':[
						(r'<[^\s][^\n>]*>', using(TypoScriptDataLexer)),
						(r'&[^;\n]*;', String),
						(r'(?=_CSS_DEFAULT_STYLE\s*\()(?s)(.*(?=\n\)))', using(TypoScriptCssLexer)),
				],
        'literal': [
            (r'0x[0-9A-Fa-f]+t?',Number.Hex),
            #(r'[0-9]*\.[0-9]+([eE][0-9]+)?[fd]?\s*(?:[^=])', Number.Float),
						(r'[0-9]+', Number.Integer),
            (r'(###\w+###)', Name.Constant),
        ],
        'label': [
							# Language label or extension resource LLL:... / EXT:...
            (r'(EXT|LLL):[^\}\n]*', String),
							# Path to a resource
            (r'(?![^\w-])([\w-]+(/[\w-]+)+/?)([^\s]*\n)', bygroups(String, String, String)),
        ],
        'punctuation': [
            (r'[,\.]', Punctuation),
        ],
        'operator': [
            (r'[<>,:=\.\*%+\|-]', Operator),
        ],
        'structure': [
							# Brackets and braces
            (r'[\{\}\(\)\[\]]', String.Symbol),
        ],
				'constant': [
							# Constant: {$some.constant}
            (r'(\{)(\$)((?:[\w-]+\.)*)([\w-]+)(\})',
								bygroups(String.Symbol, Operator, Name.Constant, Name.Constant, String.Symbol)), # constant
							# Constant: {register:somevalue}
						(r'(\{)([\w-]+(?:(\:)))*([\w-]+)(\})',
								bygroups(String.Symbol, Name.Constant, Operator, Name.Constant, String.Symbol)), # constant
							# Hex color: #ff0077
						(r'(#[a-fA-F0-9]{6}\b|#[a-fA-F0-9]{3}\b)', String.Char)
				],
        'comment': [
            (r'(?<!(#|\'|"))(?:#(?!(?:[a-fA-F0-9]{6}|[a-fA-F0-9]{3}))[^\n#]+|//[^\n]*)', Comment),
            (r'(^\s*#\s?\n)', Comment),
        ],
        'other': [
            (r'[\w"\{\}&;\/\\!\&]+', Text),
        ],
    }
