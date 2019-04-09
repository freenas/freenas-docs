# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
TAG           = freenas
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PREPROC       = ./preproc
PREPROCDIR    = processed
PAPER         =
BUILDDIR      = _build
LATEX_ENGINE != grep 'latex_engine = ' conf.py | grep -oE '[^ ]+$$' | tr -d \\047

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -t $(TAG) -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean preproc html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex pdf latexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

clean:
	rm -rf "$(PREPROCDIR)"

preproc::
	$(PREPROC) -t $(TAG) -o $(PREPROCDIR) -q

html:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo "adjusting menuselection arrow"
        # adjust |menuselection| arrow
	@sed -i '' -e 's%‣%➞%g' $(PREPROCDIR)/$(BUILDDIR)/html/*.html
	@echo
	@echo "Build finished. The HTML index page is $(PREPROCDIR)/$(BUILDDIR)/html/$(TAG).html"

dirhtml:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(PREPROCDIR)/$(BUILDDIR)/dirhtml"

singlehtml:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is $(PREPROCDIR)/$(BUILDDIR)/singlehtml/$(TAG).html"

pickle:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

epub:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(PREPROCDIR)/$(BUILDDIR)/epub"

latex:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(PREPROCDIR)/$(BUILDDIR)/latex"
	@echo "Run \`gmake' in that directory to run these through $(LATEX_ENGINE)" \
	      "(use \`gmake latexpdf' here to do that automatically)."

latexpdf pdf:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through $(LATEX_ENGINE)..."
	# fix missing latex_engine substitution in old versions of Sphinx
	@sed -i '' -e 's/pdflatex/$(LATEX_ENGINE)/g' $(PREPROCDIR)/$(BUILDDIR)/latex/Makefile
	# move the table of contents to a different spot
	@sed -i '' -e '/\\tableofcontents/d' -e '/\\sphinxtableofcontents/d' $(PREPROCDIR)/$(BUILDDIR)/latex/*.tex
	@sed -i '' -e 's/\\par--TABLEOFCONTENTS--\\par/\\tableofcontents/' $(PREPROCDIR)/$(BUILDDIR)/latex/*.tex
	# gmake is required here
	gmake -C $(PREPROCDIR)/$(BUILDDIR)/latex all-pdf
	@echo "$(LATEX_ENGINE) finished; the PDF file is" $(PREPROCDIR)/$(BUILDDIR)/latex/*.pdf
.if $(TAG:Mbsg-*)
	fname=`ls $(PREPROCDIR)/$(BUILDDIR)/latex/*.pdf` && \
	pname="$${fname%.pdf}_print.pdf" && \
	oname="$${fname%.pdf}_screen.pdf" && \
	mv $${fname} $${pname} && \
	/usr/local/bin/gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite \
	-DCompatibilityLevel=1.4 -DPDFSETTINGS=/ebook \
	-sOutputFile=$${oname} $${pname} && \
	echo "print PDF:  " $${pname} && \
	echo "screen PDF: " $${oname}
.endif

text:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(PREPROCDIR)/$(BUILDDIR)/text"


gettext:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(PREPROCDIR)/$(BUILDDIR)/locale"

changes:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(PREPROCDIR)/$(BUILDDIR)/changes"

linkcheck:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(PREPROCDIR)/$(BUILDDIR)/linkcheck/output.txt."

doctest:	preproc
	cd $(PREPROCDIR) && \
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(PREPROCDIR)/$(BUILDDIR)/doctest/output.txt"
