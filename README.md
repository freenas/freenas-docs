FreeNAS documentation is stored as ASCII text files with .rst
extensions in the FreeNAS source repository. The FreeNAS Project uses
the Sphinx Python documentation generator to generate documentation in
HTML format. Anyone can download the documentation source and generate
their own copy of the documentation in HTML or PDF formats. Users with a
github account can also edit the documentation and generate git pull
requests for their edits to be reviewed and committed. This README
contains instructions for getting the source, generating a copy of the
documentation, and issuing a git pull request. It assumes that the
reader is using these instructions on either a FreeBSD/TrueOS system or
a FreeBSD jail.

##Requirements:

Perl must be installed.

The following software must be installed at minimum. If this is the
first time pkg has been used on the system, it fetches and installs itself.
Say yes to the prompts to do so. Once it has completed, finish
installing the needed software.

Instructions are given for both ports and packages, as some software might
not have a package. Try the pkg command first, as it is faster. If the
pkg command succeeds, it is not necessary to run the make command as the
software is already installed; however if it fails, use the make command
to install the software. If the software is already installed, the pkg
command will indicate that the most recent version is already installed.

```
portsnap fetch extract
pkg install devel/git (cd /usr/ports/devel/git/ && make install)
pkg install textproc/py-sphinx (cd /usr/ports/textproc/py-sphinx/ && make install)
pkg install textproc/py-sphinxcontrib-httpdomain (cd /usr/ports/textproc/py-sphinxcontrib-httpdomain && make
install)
rehash
```

To generate a PDF version of the documentation, this software also must be
installed:

```
pkg install print/tex-formats (cd /usr/ports/print/tex-formats/ && make install)
pkg install print/tex-dvipsk (cd /usr/ports/print/tex-dvipsk/ && make install)
pkg install devel/gmake (/usr/ports/devel/gmake/ && make install)
```

Choose a place to store the source code and change to that directory
(we'll refer to it as /path/to/your-build-directory). Then check out the
source code from git:

```
cd /path/to/your-build-directory
git clone git://github.com/freenas/freenas-docs
cd freenas-docs/userguide
```

##Building the Documentation

All of the following commands are run from
/path/to/your-build-directory/freenas/docs/userguide. The formats
available are HTML, single HTML, PDF, and EPUB. The output of
either HTML form is in
/path/to/your-build-directory/freenas-docs/userguide/processed/_build/
and can be viewed in a web browser. The PDF output is in
/path/to/your-build-directory/freenas-docs/userguide/processed/_build/latex/FreeNAS.pdf.
The EPUB output is in
/path/to/your-build-directory/freenas-docs/userguide/processed/_build/epub/freenas_userguide.epub.

To build the document in HTML with a separate page for each chapter and
that chapter's table of contents in the left frame with navigational
links to browse between chapters:

```
make html
```

This is the same format that is published at doc.freenas.org/9.10.

To build one long HTML page with the entire table of contents in the
left frame, use:

```
make singlehtml
```

To build a PDF:

```
make pdf
```

To build an EPUB:

```
make epub
```

##Editing the Documentation

To edit the User Guide, make changes to the *.rst files using any ASCII
text editor. Refer to
http://docutils.sourceforge.net/docs/user/rst/quickref.html for help
with formatting syntax. Refer to
http://wiki.typo3.org/Editors_%28reST%29 for a list of reST editors.

Need help getting started or want to discuss edits? Join the
http://lists.freenas.org/mailman/listinfo/freenas-docs mailing list.

To issue a git pull request for your edits, use the instructions at
https://help.github.com/articles/using-pull-requests.
