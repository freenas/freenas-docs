.. _Contributing to %brand%:

Contributing to %brand%
=================================

%brand% is an open source community, relying on the input and
expertise of users to grow and improve. When users take time to assist
the community, their contributions benefit everyone.

This section describes how to participate and contribute to
%brand%. It is by no means an exhaustive list. If you have an
idea that will benefit the community, bring it up on one of the
resources mentioned in :ref:`Support Resources`.

This section demonstrates how to:

* :ref:`Help with Translation <Translation>`


.. index:: Translation, Translate, Localize
.. _Translation:

Translation
-----------

%brand% is developed and documented in English. Having
complete translations of the user interface into other languages helps
make %brand% much more useful to communities around the
world.

%brand% uses :file:`.po` files stored in the
`webui GitHub repository
<https://github.com/freenas/webui/tree/master/src/assets/i18n>`__
to manage the translation of text shown in the %brand%
graphical administrative interface. GitHub provides an easy to use
web-based editor, making it possible for individuals to assist with
translation or comment on existing translations.

To view translation files, open the :file:`/src/assets/i18n` directory
of the %brand%
`webui repository
<https://github.com/freenas/webui/tree/master/src/assets/i18n>`__,
as shown in :numref:`Figure %s <contribute_po_fig>`.


.. _contribute_po_fig:

.. figure:: images/external/contribute-po.png

   %brand% Translation Files


To assist with translating %brand%, first create an account
with
`GitHub <https://github.com/>`__ and :guilabel:`Fork` the
`freenas/webui <https://github.com/freenas/webui>`__ repository.

There are two methods for committing translations:

1. Use the GitHub website to edit the :file:`.po` files.

OR

2. Make a local copy of the forked repository and use a text editor for
   translations.


Translate with GitHub
~~~~~~~~~~~~~~~~~~~~~

Open a browser and go to your GitHub profile. Select the
:guilabel:`Repositories` tab and open your fork of the
:literal:`freenas/webui` repository. Click
:menuselection:`src --> assets --> i18n`
to open the translations directory. Click on the desired language
:file:`.po` file to begin translating.

.. tip:: Here is a list of `common language abbreviations
   <https://www.abbreviations.com/acronyms/LANGUAGES2L>`__


Click the :guilabel:`Pencil` icon in the upper right area to open the
online file editor. :numref:`Figure %s <contribute_github_editor_fig>`
shows the page that appears:

.. _contribute_github_editor_fig:

.. figure:: images/external/contribute-github-editor.png

   GitHub Online Editor


There are numerous :literal:`msgid ""` and :literal:`msgstr ""`
entries in the file. Read  the :literal:`msgid` text and enter the
translation between the :literal:`msgstr` quotes.

Scroll to the bottom of the page when finished entering translations.
Enter a descriptive title and summary of changes for the edits and click
:guilabel:`Commit changes`.


Download and Translate Offline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Install Git
<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`__.
There are numerous examples in these instructions of using
:command:`git`, but full documentation for :command:`git` is
`available online <https://git-scm.com/doc>`__.

These instructions show using the Command Line Interface (CLI) with
:command:`git`, but many graphical utilities are available.

Create a suitable directory to store the local copy of the forked
repository. Download the repository with :command:`git clone`:

:samp:`% git clone https://github.com/ghuser/webui.git`

The download can take several minutes, depending on connection speed.

Use :command:`cd` to go to the :file:`i18n` directory:

:samp:`% cd src/assets/i18n/`

Use a :file:`po` editor to add translations to the desired language
file. Any capable editor will work, but
`poedit <https://poedit.net/>`__
and
`gtranslator <https://wiki.gnome.org/Apps/Gtranslator>`__
are two common options.

Commit any file changes with :command:`git commit`:

:samp:`% git commit ar.po`

Enter a descriptive message about the changes and save the commit.

When finished making commits to the branch, use :command:`git push` to
send your changes to the online fork repository.


Translation Pull Requests
~~~~~~~~~~~~~~~~~~~~~~~~~

When ready to merge translations in the original :literal:`freenas/webui`
repository, open a web browser and go to your forked repository on
GitHub. Select the :guilabel:`Code` tab and click
:guilabel:`New pull request`. Set the :guilabel:`base repository`
drop-down to :literal:`freenas/webui` and the :guilabel:`head repository`
to your fork. Click :guilabel:`Create pull request`, write a title and
summary of your proposed changes, and click
:guilabel:`Create pull request` again to submit your translations to the
:literal:`freenas/webui` repository.

The %brand% project automatically tests pull requests for
compatibility. If there any issues with a pull request, either the
automated system will update the request or a %brand% team
member will leave a message in the comment section of the request.

All assistance with translations helps to benefit the %brand%
community. Thank you!
