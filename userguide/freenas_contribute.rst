.. _Contributing to FreeNAS®:

Contributing to FreeNAS®
=========================

FreeNAS® is an open source community, relying on the input and
expertise of its users to help grow and improve FreeNAS®. When you
take time to assist the community, your contributions benefit everyone
who uses FreeNAS®.

This section describes some areas of participation to get you started.
It is by no means an exhaustive list. If you have an idea that you
think would benefit the FreeNAS® community, bring it up on one of the
resources mentioned in :ref:`FreeNAS® Support Resources`.

This section demonstrates how you can:

* :ref:`Localize`

.. index:: Localize, Translate
.. _Localize:

Localize
---------

FreeNAS® uses the open source application
`Pootle <https://en.wikipedia.org/wiki/Pootle>`_
to manage the localization of the menu screens used by the FreeNAS®
graphical administrative interface. Pootle makes it easy to find out
the localization status of your native language and to translate the
text for any menus that have not yet been localized. By providing a
web editor and commenting system, Pootle allows translators to spend
their time making and reviewing translations rather than learning how
to use a translation submission tool.

To see the status of a localization, open
`pootle.freenas.org <http://pootle.freenas.org/>`_
in a browser, as shown in Figure 25.1a:

**Figure 25.1a: FreeNAS® Localization System**

.. image:: images/translate.png

The localizations FreeNAS® users have requested are listed
alphabetically on the left. If your language is missing and you would
like to help in its translation, send an email to the
`translations mailing list
<http://lists.freenas.org/mailman/listinfo/freenas-translations>`_
so it can be added.

The green bar in the Overall Completion column indicates the
percentage of FreeNAS® menus that have been localized. If a language
is not at 100%, it means that the menus that currently are not
translated will appear in English instead of in that language.

To help localize your language, join the
`translations mailing list
<http://lists.freenas.org/mailman/listinfo/freenas-translations>`_,
introduce yourself, and point out which languages you can help
translate. This will allow you to meet other volunteers as well as
keep abreast of any notices or updates that may affect the
translations. You will also need to click on the "Register" link to
create a Pootle login account.

On the first login to the FreeNAS® Pootle interface, there is a
prompt to select your language so that you can access that
language's translation whenever you log in. Alternately, you can click
the "Home" link to see the status of all of the languages. To work on
a translation, click the link for the language, click the FreeNAS®
link for the project, click the link for "LC_MESSAGES", and click the
link for "django.po". Every text line available in the GUI menu
screens has been assigned a string number. If you click the number, an
editor will open to translate the text. In the example shown in Figure
25.1b, a user has selected string number 46 in the German translation.
The other strings in the screenshot have already been translated:

**Figure 25.1b: Using the Pootle Interface to Edit a Translation
String**

.. image:: images/translate2.png

Type in the translated text and click the "Submit" button to save the
change.


