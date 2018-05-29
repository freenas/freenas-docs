# -*- coding: utf-8 -*-

# requirements:
# textproc/py-sphinx
# textproc/py-sphinx_numfig
# textproc/py-sphinx_rtd_theme
# textproc/py-sphinxcontrib-httpdomain

import os
import six
import sphinx
import string
import sys
import time

templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# General information about the project.
copyright = '2011-2018, iXsystems'

# Version info for the project being documented, acts as replacement for
# |version| and |release|, also used in various other places throughout
# the built documents.
#

# VERSION is the LONG, FULL version number with all patch levels, like "11.0-U1"
version = '11.2-BETA1'
# RELEASE is the short major release number ONLY, like "11.0"
release = '11.2'

if tags.has('truenas'):
    # VERSION is the LONG, FULL, version number
    version = '11.1-U3'
    # RELEASE is the short major release number ONLY
    release = '11.1'

# exclude_patterns is a list of patterns relative to the source directory
# that match files and directories to ignore when looking for source files.

tags.add('freenas')
brand = 'FreeNAS®' if six.PY3 else u'FreeNAS®'
project = brand + ' ' + six.u(version) + ' ' + 'User Guide'
projtype = None
master_doc = 'freenas'
extensions = [
    'sphinxcontrib.httpdomain'
]
cover_pic = r''
numfig = True
numfig_secnum_depth = (2)

if tags.has('truenas'):
    brand = 'TrueNAS®' if six.PY3 else u'TrueNAS®'
    tags.remove('freenas')
    project = brand + ' ' + six.u(version) + six.u(' User Guide')
    projtype = None
    master_doc = 'truenas'
    cover_pic = r''

# BSGs
if tags.has('bsg-unified'):
    brand = 'TrueNAS®' if six.PY3 else u'TrueNAS®'
    tags.remove('freenas')
    project = brand + ' ' + six.u('Unified Storage Array')
    projtype = 'Basic Setup Guide'
    master_doc = 'bsg-unified'
    cover_pic = r''

if tags.has('bsg-e16'):
    brand = 'TrueNAS®' if six.PY3 else u'TrueNAS®'
    tags.remove('freenas')
    project = brand + ' ' + six.u('E16/E16F Expansion Shelf')
    projtype = 'Basic Setup Guide'
    master_doc = 'bsg-e16'
    cover_pic = r''

if tags.has('bsg-e24'):
    brand = 'TrueNAS®' if six.PY3 else u'TrueNAS®'
    tags.remove('freenas')
    project = brand + ' ' + six.u(' E24 Expansion Shelf')
    projtype = 'Basic Setup Guide'
    master_doc = 'bsg-e24'
    cover_pic = r''

if tags.has('bsg-xseries'):
    brand = 'TrueNAS®' if six.PY3 else u'TrueNAS®'
    tags.remove('freenas')
    project = brand + ' ' + six.u('X-Series Unified Storage Array')
    projtype = 'Basic Setup Guide'
    master_doc = 'bsg-xseries'
    cover_pic = r'\vspace*{1in}\hspace*{4in}\includegraphics[width=12in]{../../../images/truenas/x_front.png}'

if tags.has('bsg-es12'):
    brand = 'TrueNAS®' if six.PY3 else u'TrueNAS®'
    tags.remove('freenas')
    project = brand + ' ' + six.u('ES12 Expansion Shelf')
    projtype = 'Basic Setup Guide'
    master_doc = 'bsg-es12'
    cover_pic = r'\vspace*{1in}\hspace*{4in}\includegraphics[width=12in]{../../../images/truenas/es12_front.png}'

if tags.has('bsg-es24'):
    brand = 'TrueNAS®' if six.PY3 else u'TrueNAS®'
    tags.remove('freenas')
    project = brand + ' ' + six.u('ES24 Expansion Shelf')
    projtype = 'Basic Setup Guide'
    master_doc = 'bsg-es24'
    cover_pic = r'\vspace*{.1in}\hspace*{4in}\includegraphics[width=12in]{../../../images/truenas/es24_front.png}'

if tags.has('bsg-es60'):
    brand = 'TrueNAS®' if six.PY3 else u'TrueNAS®'
    tags.remove('freenas')
    project = brand + ' ' + six.u('ES60 Expansion Shelf')
    projtype = 'Basic Setup Guide'
    master_doc = 'bsg-es60'
    cover_pic = r'\vspace*{.1in}\hspace*{4in}\includegraphics[width=12in]{../../../images/truenas/es60.png}'


# |brand| will be replaced with FreeNAS® or TrueNAS®
# rst_epilog = '.. |brand| replace:: %s' % brand


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Option to change :menuselection: arrow -----------------------------

from docutils import nodes, utils
from docutils.parsers.rst import roles
from sphinx.roles import _amp_re

def patched_menusel_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    text = utils.unescape(text)
    if typ == 'menuselection':
        text = text.replace('-->', u'\u2192') # Here is the patch

    spans = _amp_re.split(text)

    node = nodes.literal(rawtext=rawtext)
    for i, span in enumerate(spans):
        span = span.replace('&&', '&')
        if i == 0:
            if len(span) > 0:
                textnode = nodes.Text(span)
                node += textnode
            continue
        accel_node = nodes.inline()
        letter_node = nodes.Text(span[0])
        accel_node += letter_node
        accel_node['classes'].append('accelerator')
        node += accel_node
        textnode = nodes.Text(span[1:])
        node += textnode

    node['classes'].append(typ)
    return [node], []

# Use 'patched_menusel_role' function for processing the 'menuselection' role
roles.register_local_role("menuselection", patched_menusel_role)

# Use roles for specific Angular UI icons

rst_prolog = """
.. |ui-settings| replace:: **"""u'\u2699'"""** (Settings)
.. |ui-options| replace:: **"""u'\u2AF6'"""** (Options)
.. |ui-add| replace::  **"""u'\uFF0B'"""** (Add/Create)
.. |ui-menu| replace:: **"""u'\u2AF6'""""""u'\u2630'"""** (Menu)
"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'trueos_style'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "stickysidebar": "true"
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_static/themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = brand + version + ' User Guide Table of Contents'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "artwork/freenaslogo.png"
if tags.has('truenas'):
    html_logo = "artwork/truenaslogo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "artwork/freenas.ico"
if tags.has('truenas'):
    html_favicon = "artwork/truenas.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {'searchresults' : 'searchresults.html',}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If false, reST source is not shown in search results, just page titles.
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'FreeNASdoc'
if tags.has('truenas'):
    htmlhelp_basename = 'TrueNASdoc'

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'FreeNAS® User Guide'
if tags.has('truenas'):
    epub_title = u'TrueNAS® User Guide'
epub_author = u'iXsystems'
epub_publisher = u'iXsystems'
epub_copyright = u'2011-2018, iXsystems'

# The basename for the epub file. It defaults to the project name.
epub_basename = u'freenas_userguide'
if tags.has('truenas'):
    epub_basename = u'truenas_userguide'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'URL'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'freenas.org'

# A unique identification for the text.
epub_uid = release

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
epub_show_urls = 'no'

# If false, no index is generated.
#epub_use_index = True


# -- Options for LaTeX output --------------------------------------------------

if six.PY3:
    texproject = project.replace('®', r'''{\textsuperscript{\textregistered}}''')
else:
    texproject = project.replace(u'®', r'''{\textsuperscript{\textregistered}}''')

PREAMBLE = r'''\def\docname{''' + texproject + '}'

PREAMBLE = (PREAMBLE
            + r'''\def\docdate{'''
            + time.strftime("%B %Y")
            + ' Edition}')

if sphinx.__version__ < '1.6.5':
    PREAMBLE = PREAMBLE + r'''\usepackage[tmargin=.75in, bmargin=.75in, lmargin=0.5in, rmargin=0.5in]{geometry}'''
else:
    PREAMBLE = PREAMBLE + r'''\geometry{tmargin=.75in, bmargin=.75in, lmargin=0.5in, rmargin=0.5in}'''


# define custom title page
PREAMBLE = PREAMBLE + r'''
% FreeNAS/TrueNAS LaTeX preamble
%%font_init%%
\usepackage{color}
\usepackage{tikz}
\usetikzlibrary{calc}
%for better UTF handling
\DeclareTextCommandDefault{\nobreakspace}{\leavevmode\nobreak\ }
%for bitmaps
\usepackage{graphicx}
%for ragged right tables
\usepackage{array,ragged2e}
\definecolor{ixblue}{cmyk}{0.85,0.24,0,0}
\usepackage{ifthen}
\usepackage{calc}
\makeatletter
\renewcommand{\maketitle}{%
  \begin{titlepage}%
    \vspace*{-6mm}%
    % title
    %%title_font%%
    \fontsize{32pt}{32pt}\selectfont%
    \newlength{\thistitlewidth}%
    \settowidth{\thistitlewidth}{\docname}%
    \ifthenelse{\thistitlewidth > \textwidth}%
      % if docname is wider than textwidth, squash box to fit
      {\resizebox{\textwidth}{32pt}{\mbox{\docname}}}%
      {\mbox{\docname}}%
    \par%
    % document type
    \fontsize{32pt}{32pt}\selectfont%
    %%doc_type%%\par%
    \vspace*{-4.5mm}%
    {\color{ixblue}\rule{\textwidth}{1.5pt}}\par%
    \vspace*{2.5mm}%
    % document date
    \fontsize{20pt}{23pt}\fontseries{sbc}\selectfont%
    \docdate\par%
    % cover picture
    %%cover_pic%%%
    % iX blue bottom fill
    \begin{tikzpicture}[remember picture,overlay]
      \fill [ixblue] (current page.south west) rectangle ($(current page.south east) + (0, 2in)$);
    \end{tikzpicture}
  \end{titlepage}
}
\makeatother
% a plain page style for front matter
\fancypagestyle{frontmatter}{%
  \fancyhf{}
  \fancyhf[FCO,FCE]{}
  \fancyhf[FLE,FRO]{\textbf{\thepage}}
  \fancyhf[FLO,FRE]{}
}
\fancypagestyle{bsg}{%
  \fancyhf{}
  \fancyfoot[C]{\textbf{\thepage}}
}
'''

PREAMBLE = PREAMBLE.replace('%%cover_pic%%', cover_pic)
if projtype is not None:
    PREAMBLE = PREAMBLE.replace('%%doc_type%%', projtype)


latex_engine = 'xelatex'

if latex_engine == 'xelatex':
    font_init = r'''\usepackage{fontspec}%
                    \newfontfamily\opensansfont{OpenSans-Regular.ttf}[Scale=0.95]%
                    \setmainfont{OpenSans-Regular.ttf}[Scale=0.95]%
                    \setmonofont{FreeMono.otf}[Scale=0.95]%
                    \defaultfontfeatures{Ligatures=TeX}%'''
    title_font = r'''\fontspec{OpenSans-Light.ttf}[Scale=0.95]%'''
else:
    # pdflatex, can't use fontspec
    font_init = r'''\usepackage[T1,T2A]{fontenc}%
                    \usepackage{textcomp}%
                    \usepackage[default,scale=0.95]{opensans}%'''
    title_font = r'''%no font choice needed'''

PREAMBLE = PREAMBLE.replace('%%font_init%%', font_init)
PREAMBLE = PREAMBLE.replace('%%title_font%%', title_font)


latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': PREAMBLE,

# remove blank pages
'classoptions': ',openany',
'babel': r'''\usepackage[english]{babel}''',

# strict positioning of figures
'figure_align': 'H',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('freenas', 'FreeNAS.tex', texproject, 'iXsystems', 'manual'),
]

if tags.has('truenas'):
    latex_documents = [
      ('truenas', 'TrueNAS.tex', texproject, 'iXsystems', 'manual'),
    ]

if tags.has('bsg-unified'):
    latex_documents = [
      ('bsg-unified', 'BSG-Unified.tex', texproject, 'iXsystems', 'howto'),
    ]
    latex_elements.update({'printindex': ''})

if tags.has('bsg-e16'):
    latex_documents = [
      ('bsg-e16', 'BSG-E16.tex', texproject, 'iXsystems', 'howto'),
    ]
    latex_elements.update({'printindex': ''})

if tags.has('bsg-e24'):
    latex_documents = [
      ('bsg-e24', 'BSG-E24.tex', texproject, 'iXsystems', 'howto'),
    ]
    latex_elements.update({'printindex': ''})

if tags.has('bsg-xseries'):
    latex_documents = [
      ('bsg-xseries', 'BSG-X-Series.tex', texproject, 'iXsystems', 'howto'),
    ]
    latex_elements.update({'printindex': ''})

if tags.has('bsg-es12'):
    latex_documents = [
      ('bsg-es12', 'BSG-ES12.tex', texproject, 'iXsystems', 'howto'),
    ]
    latex_elements.update({'printindex': ''})

if tags.has('bsg-es24'):
    latex_documents = [
      ('bsg-es24', 'BSG-ES24.tex', texproject, 'iXsystems', 'howto'),
    ]
    latex_elements.update({'printindex': ''})

if tags.has('bsg-es60'):
    latex_documents = [
      ('bsg-es60', 'BSG-ES60.tex', texproject, 'iXsystems', 'howto'),
    ]
    latex_elements.update({'printindex': ''})

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# Show URLs: 'no', 'footnote', or 'inline'
latex_show_urls = 'inline'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True
