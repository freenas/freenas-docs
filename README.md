> NOTE: this repository stores retired documentation for FreeNAS/TrueNAS 11.3 and earlier versions. To view current documentation for TrueNAS 12.0, TrueCommand, and TrueNAS hardware, go to https://www.truenas.com/docs/hub/ . All sources for that website are stored in the https://github.com/freenas/documentation/ repository.

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

## Requirements

Perl must be installed.

The following software must be installed at minimum. If this is the
first time pkg has been used on the system, it fetches and installs itself.
Say yes to the prompts to do so. Once it has completed, finish
installing the needed software.

Instructions are given for both ports and packages, as some software might
not have a prebuilt package.

Use the pkg command first. If it installs the packages or indicates that the
most recent software is already installed, continue with the next package. If
the pkg command shows an error, this usually means that a prebuilt package is
not available, so use the make command to build and install that software.

```
portsnap fetch extract
pkg install devel/git                            (make -C /usr/ports/devel/git install clean)
pkg install textproc/py-sphinx                   (make -C /usr/ports/textproc/py-sphinx install clean)
pkg install textproc/py-sphinxcontrib-httpdomain (make -C /usr/ports/textproc/py-sphinxcontrib-httpdomain install clean)
rehash
```

To generate a PDF version of the documentation, this software also must be
installed:

```
pkg install print/tex-formats            (make -C /usr/ports/print/tex-formats install clean)
pkg install print/tex-dvipdfmx           (make -C /usr/ports/print/tex-dvipdfmx install clean)
pkg install print/tex-dvipsk             (make -C /usr/ports/print/tex-dvipsk install clean)
pkg install print/tex-xetex              (make -C /usr/ports/print/tex-xetex install clean)
pkg install x11-fonts/materialdesign-ttf (make -C /usr/ports/x11-fonts/materialdesign-ttf install clean)
pkg install devel/gmake                  (make -C /usr/ports/devel/gmake install clean)
```

Choose a place to store the source code and change to that directory
(we will refer to it as /path/to/your-build-directory). Then check out the
source code from git:

```
cd /path/to/your-build-directory
git clone git://github.com/freenas/freenas-docs
cd freenas-docs/userguide
```

## Building the Documentation

All of these commands are run from
/path/to/your-build-directory/freenas/docs/userguide. The formats
available are HTML, single HTML, PDF, and EPUB. The path to the rendered
output files is displayed at the end of the build.

To build the document in HTML with a separate page for each chapter and
a left frame with the table of contents:

```
make html
```

This is the same format that is published at http://doc.freenas.org/.

To build one long HTML page with the entire table of contents in the
left frame, use:

```
make singlehtml
```

To build a PDF:

```
make pdf
```

## Editing the Documentation

To edit the User Guide, make changes to the *.rst files using any ASCII
text editor. Refer to
http://www.sphinx-doc.org/en/stable/contents.html for help
with formatting syntax. Refer to
http://wiki.typo3.org/Editors_%28reST%29 for a list of reST editors.

Need help getting started or want to discuss edits? Join the
http://lists.freenas.org/mailman/listinfo/freenas-docs mailing list.

To issue a git pull request for your edits, use the instructions at
https://help.github.com/articles/using-pull-requests.
