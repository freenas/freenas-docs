# requirements:
# textproc/py-sphinx
# textproc/py-sphinx_numfig
# textproc/py-sphinx_rtd_theme

import os
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
copyright = '2011-2020, iXsystems'

# exclude_patterns is a list of patterns relative to the source directory
# that match files and directories to ignore when looking for source files.


numfig = True
numfig_secnum_depth = (2)
extensions = []


# FreeNAS default settings
brand = 'FreeNAS®'
tags.add('freenas')
master_doc = 'freenas'

version = '11.3-U5'
release = '11.3'
product = f'{brand} {version} User Guide'

pdf_file_name  = f'FreeNAS-{version}-User-Guide'
pdf_title      = product
pdf_subtitle   = ''
document_class = 'manual'    # 'howto' or 'manual'
toctree_only   = True
draft          = False
show_edition   = False
cover_pic = r''

if tags.has('truenas'):
    brand = 'TrueNAS®'
    tags.remove('freenas')
    tags.add('truenas')
    master_doc = 'truenas'

    version = '11.3-U4.1'
    release = '11.3'
    product = f'{brand} {version} User Guide'

    pdf_file_name  = f'TrueNAS-{version}-User-Guide'
    pdf_title      = product
    pdf_subtitle   = ''
    document_class = 'manual'    # 'howto' or 'manual'
    toctree_only   = True
    draft          = False
    show_edition   = False
    cover_pic = r''

# roles for text replacement
rst_prolog = u'''
.. |alert-icon-error|     replace:: 
.. |alert-icon-info|      replace:: 
.. |alert-icon-one-error| replace:: 
.. |alert-icon-watch|     replace:: 肋
.. |arrow-right|          replace:: 
.. |bug-tracker-link|     replace:: `<https://bugs.ixsystems.com>`__
.. |copyright-year|       replace:: 2020
.. |Ctrlr-term|           replace:: TrueNAS Controller
.. |Ctrlrs-term|          replace:: TrueNAS Controllers
.. |Ctrlr-term-1|         replace:: TrueNAS Controller 1
.. |Ctrlr-term-2|         replace:: TrueNAS Controller 2
.. |Ctrlr-term-1-2|       replace:: TrueNAS Controller 1/2
.. |ctrlr-term|           replace:: TrueNAS controller
.. |ctrlrs-term|          replace:: TrueNAS controllers
.. |ctrlr-term-1|         replace:: TrueNAS controller 1
.. |ctrlr-term-2|         replace:: TrueNAS controller 2
.. |ctrlr-term-1-2|       replace:: TrueNAS controller 1/2
.. |ctrlr-term-active|    replace:: active TrueNAS controller
.. |ctrlr-term-standby|   replace:: standby TrueNAS controller
.. |ctrlrs-term-both|     replace:: active and standby TrueNAS controllers
.. |active|               replace:: active
.. |standby|              replace:: standby
.. |active-standby|       replace:: active/standby
.. |dockerhost|           replace:: Docker VM
.. |help-pin|             replace::  (Pin)
.. |help-text|            replace::  (Help Text)
.. |help-close|           replace::  (Close)
.. |humanized-field|      replace:: This is a :ref:`humanized field <Humanized Fields>`.
.. |os-device|            replace:: operating system device
.. |os-devices|           replace:: operating system devices
.. |OS-Device|            replace:: Operating System Device
.. |OS-Devices|           replace:: Operating System Devices
.. |pool-degraded|        replace::  DEGRADED
.. |pool-faulted|         replace::  Pool Fault
.. |pool-healthy|         replace::  HEALTHY
.. |pool-lock|            replace::  (Encryption Options)
.. |pool-locked|          replace::  LOCKED
.. |pool-unknown|         replace::  UNKNOWN
.. |pool-unlock|          replace::  (Unlock)
.. |rpln-sys1|            replace:: *Primary*
.. |rpln-sys2|            replace:: *Secondary*
.. |ssh-host1|            replace:: *Host 1*
.. |ssh-host2|            replace:: *Host 2*
.. |ui-add|               replace:: :guilabel:`ADD`
.. |ui-browse|            replace::  (Browse)
.. |ui-calendar|          replace:: 
.. |ui-configure|         replace::  (Configure)
.. |ui-chevron-right|     replace::  (Expand)
.. |ui-delete|            replace::  :guilabel:`DELETE`
.. |ui-edit|              replace::  :guilabel:`EDIT`
.. |ui-edit-disks|        replace::  (Edit Disks)
.. |ui-jail-delete|       replace::  (Delete)
.. |ui-jail-start|        replace::  (Start)
.. |ui-jail-stop|         replace::  (Stop)
.. |ui-jail-update|       replace::  (Update)
.. |ui-jail-shell|        replace:: 塞 SHELL
.. |ui-launch|            replace:: 襁 (Launch)
.. |ui-options|           replace::  (Options)
.. |ui-password-hide|     replace::  (Hide)
.. |ui-password-show|     replace::  (Show)
.. |ui-power|             replace::  (Power)
.. |ui-refresh|           replace::  (Refresh)
.. |ui-settings|          replace::  (Settings)
.. |ui-task-manager|      replace::  (Task Manager)
.. |ui-task-run|          replace::  :guilabel:`RUN NOW`
.. |ui-update|            replace:: 
.. |usb-stick|            replace:: USB stick
.. |usb-sticks|           replace:: USB sticks
.. |web-ui|               replace:: web interface
.. |Web-UI|               replace:: Web Interface
'''


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------
project = product

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
epub_copyright = u'2011-2020, iXsystems'

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

latex_engine = 'xelatex'

draftcode = r'''
%watermark
\usepackage[printwatermark]{xwatermark}%
\newsavebox\draftbox%
\savebox\draftbox{\tikz[color=red,opacity=0.3]\node{DRAFT};}%
\newwatermark*[allpages,angle=45,scale=15,xpos=-50,ypos=50]{\usebox\draftbox}%
'''

editioncode = r'''
\vspace*{-4mm}%
\fontsize{18}{22}\fontseries{sbc}\selectfont%
\docdate\par%
'''

PREAMBLE = r'''
%%font_init%%
\def\pdftitle{%%PDFTITLE%%}%
\def\pdfsubtitle{%%PDFSUBTITLE%%}%
\def\docdate{%%DOCDATE%%}%
\geometry{tmargin=.75in, bmargin=.75in, lmargin=.75in, rmargin=.75in}%
\usepackage{fontspec}%
\newfontfamily\opensansfont{OpenSans-Regular.ttf}[Scale=0.95]%
\setmainfont{OpenSans-Regular.ttf}[
      Scale=0.95 ,
      BoldFont = OpenSans-Bold.ttf ,
      ItalicFont = OpenSans-Italic.ttf ,
      BoldItalicFont = OpenSans-BoldItalic.ttf
      ]%
\setmonofont{FreeMono.otf}[Scale=0.95]%
\defaultfontfeatures{Ligatures=TeX}%
\usepackage{color}%
\usepackage{tikz}%
\usetikzlibrary{calc}%
%for better UTF handling
\DeclareTextCommandDefault{\nobreakspace}{\leavevmode\nobreak\ }
%%DRAFT%%
% for table header colors
\usepackage{colortbl}%
\protected\def\sphinxstyletheadfamily {\color{white}\cellcolor{gray}}%
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
    \pagestyle{empty}%
    \vspace*{-6mm}%
    %%title_font%%
    \fontsize{32pt}{32pt}\selectfont%
    \newlength{\thistitlewidth}%
    \settowidth{\thistitlewidth}{\pdftitle}%
    \ifthenelse{\thistitlewidth > \textwidth}%
      % if pdftitle is wider than textwidth, squash box to fit
      {\resizebox{\textwidth}{32pt}{\mbox{\pdftitle}}}%
      {\mbox{\pdftitle}}%
    \par%
    \pdfsubtitle\par%
    \vspace*{-4.5mm}%
    {\color{ixblue}\rule{\textwidth}{1.5pt}}\par%
    \vspace*{2.5mm}%
    %%EDITION%%
    %%COVER_PICTURE%%
    % iX blue bottom fill
    \begin{tikzpicture}[remember picture,overlay]
      \fill [ixblue] (current page.south west) rectangle ($(current page.south east) + (0, 2in)$);
    \end{tikzpicture}
  \end{titlepage}
}
\makeatother
% define page styles
% a plain page style for front matter
\fancypagestyle{frontmatter}{%
  \fancyhf{}
  \fancyhf[FCO,FCE]{}
  \fancyhf[FLE,FRO]{\textbf{\thepage}}
  \fancyhf[FLO,FRE]{}
}
\fancypagestyle{eol}{%
  \fancyhead{}%
  \fancyfoot{}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}%
  \lfoot{\fontsize{10}{12}\color{darkgray}{EOL Document}}%
  \cfoot{\fontsize{10}{12}\color{darkgray}{CONFIDENTIAL}}%
  \rfoot{\fontsize{10}{12}\color{darkgray}{\thepage}}%
}%
\fancypagestyle{bsg}{%
  \fancyhf{}
  \fancyfoot[C]{\textbf{\thepage}}
}
% force URLs to be raggedright
\let\oldsphinxhref\sphinxhref%
\renewcommand{\sphinxhref}[2]{%
  \RaggedRight{\oldsphinxhref{#1}{#2}}%
}%
'''

if latex_engine == 'xelatex':
    font_init = r'''\usepackage{fontspec}%
                    \newfontfamily\opensansfont{OpenSans-Regular.ttf}[Scale=0.95]%
                    \setmainfont{OpenSans-Regular.ttf}[
                          Scale=0.95 ,
                          BoldFont = OpenSans-Bold.ttf ,
                          ItalicFont = OpenSans-Italic.ttf ,
                          BoldItalicFont = OpenSans-BoldItalic.ttf
                          ]%
                    \setmonofont{FreeMono.otf}[Scale=0.95]%
                    \defaultfontfeatures{Ligatures=TeX}%
                    \newfontfamily{\material}[Scale = 0.95, Path = /usr/local/share/fonts/MaterialDesign-Webfont/]{materialdesignicons-webfont.ttf}'''
    title_font = r'''\fontspec{OpenSans-Light.ttf}[Scale=0.95]%'''
else:
    # pdflatex, can't use fontspec
    font_init = r'''\usepackage[T1,T2A]{fontenc}%
                    \usepackage{textcomp}%
                    \usepackage[default,scale=0.95]{opensans}%'''
    title_font = r'''%no font choice needed'''

PREAMBLE = PREAMBLE.replace('%%font_init%%', font_init)
PREAMBLE = PREAMBLE.replace('%%title_font%%', title_font)
if draft:
  PREAMBLE = PREAMBLE.replace('%%DRAFT%%', draftcode)
if show_edition:
  PREAMBLE = PREAMBLE.replace('%%EDITION%%', editioncode)
PREAMBLE = PREAMBLE.replace('%%PDFTITLE%%', pdf_title)
PREAMBLE = PREAMBLE.replace('%%PDFSUBTITLE%%', pdf_subtitle)
PREAMBLE = PREAMBLE.replace('%%DOCDATE%%', f'Version {version}')
PREAMBLE = PREAMBLE.replace('%%COVER_PICTURE%%', cover_pic)
# do this last to make sure we replace all of the registered trademark symbols
PREAMBLE = PREAMBLE.replace('®', r'''\textsuperscript{\textregistered}''')

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
# source index file, output file name, title in document, author, documentclass [howto/manual], toctree_only.
# User Guide manually includes index, BSGs have no index, so it is disabled here for both.
latex_documents = [
    (master_doc,
     f'{pdf_file_name}.tex',
     product,
     'iXsystems',
     document_class,
     toctree_only),
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
