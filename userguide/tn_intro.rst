.. centered:: Copyright iXsystems 2011-2016

.. centered:: %brand% and the %brand% logo are registered trademarks
   of iXsystems.

%brand% and the %brand% logo are registered trademarks of iXsystems.

#include snippets/trademarks.rst


Introduction
------------

Welcome to the %brand% Administrator Guide. This Guide provides
information about configuring and managing the %brand% Unified Storage
Array. Your iXsystems support engineer will assist with the array's
initial setup and configuration. Once you are familiar with the
configuration workflow, this document can be used as a reference guide
to the many features provided by %brand%.


How This Guide is Organized
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The information in the %brand% Administrator Guide has been organized
as follows:

* Chapter 1: Introduction: describes the organization of the guide and
  the typographic conventions.

* Chapter 2: Initial Setup: this chapter describes how to install the
  %brand% Storage Array, how to configure the out-of-band management
  port, and introduces the console and how to access the graphical
  administrative interface.

* Chapters 3-14: these chapters cover the configuration options which
  are available in the %brand% graphical administrative interface. The
  chapter order reflects the order that the configuration options
  appear within the administrative interface's tree structure. Chapter
  4 describes how to create users and groups. Chapter 5 describes the
  tasks that can be accomplished using the System Configuration
  section of the administrative interface. Chapter 6 describes how to
  schedule regular administrative tasks. Chapter 7 demonstrates the
  various network configuration options. Chapter 8 deals with managing
  storage. Chapter 9 describes integration with various directory
  services. Chapter 10 provides examples for creating AFP, CIFS, NFS,
  WebDAV, and iSCSI shares. Chapter 11 describes how to configure,
  start, and stop the built-in services. Chapter 12 provides an
  overview of the Reporting mechanism. Chapter 13 introduces the
  configuration wizard, and chapter 14 covers the remaining
  configuration options.

* Chapter 15: ZFS Primer: many of the features in the %brand% Storage
  Array rely on the ZFS file system. An overview is provided to
  familiarize the administrator with the terminology and features
  provided by ZFS.

* Chapter 16: Using the API: this chapter demonstrates how to
  use the FreeNAS® API to remotely control a %brand% system.

**Typographic Conventions**

The %brand% Administrator Guide uses the following typographic
conventions:

* Names of graphical elements such as buttons, icons, fields, columns,
  and boxes are enclosed within quotes. For example: click the
  "Import Ca" button.

* Menu selections are italicized and separated by arrows. For example:
  :menuselection:`System --> Information`.

* Commands that are mentioned within text are highlighted in
  :command:`bold text`. Command examples and command output are
  contained in green code blocks.

* Volume, dataset, and file names are enclosed in a blue box
  :file:`/like/this`.

* Keystrokes are formatted in a blue box. For example: press
  :kbd:`Enter`.

* **bold text:** used to emphasize an important point.

* *italic text:* used to represent device names or text that is input
  into a GUI field.
