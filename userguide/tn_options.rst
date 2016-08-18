.. _Additional Options:

Additional Options
==================

This section covers the remaining miscellaneous options available from
the %brand% graphical administrative interface.


.. index:: Processes

.. _Display System Processes:

Display System Processes
------------------------

If you click Display System Processes, a screen will open showing the
output of
`top(1) <http://www.freebsd.org/cgi/man.cgi?query=top>`_.
An example is shown in
:numref:`Figure %s <process>`.

.. _process:

.. figure:: images/process.png

   System Processes Running on %brand%


The display will automatically refresh itself. Simply click the X in
the upper right corner to close the display when you are finished.
Note that the display is read-only, meaning that you won't be able to
issue a :command:`kill` command within it.


.. index:: Shell

.. _Shell:

Shell
-----

The %brand% GUI provides a web shell, making it convenient to run
command line tools from the web browser as the *root* user. The link
to Shell is the fourth entry from the bottom of the menu tree. In
:numref:`Figure %s <web_shell_fig>`,
the link has been clicked and Shell is open.


.. _web_shell_fig:

.. figure:: images/shell.png

   Web Shell


The prompt indicates that the current user is *root*, the hostname is
*truenas*, and the current working directory is :file:`~`
(*root*'s home directory).

To change the size of the shell, click the *80x25* drop-down menu and
select a different size.

To copy text from shell, highlight the text, right-click, and select
Copy from the right-click menu. To paste into the shell, click the
"Paste" button, paste the text into the box that opens, and click the
OK button to complete the paste operation.

While you are in Shell, you will not have access to any of the other
GUI menus. If you need to have access to a prompt while using the GUI
menus, use :command:`tmux` instead as it supports multiple shell
sessions and the detachment and reattachment of sessions.

Shell provides history (use your up arrow to see previously entered
commands and press :kbd:`Enter` to repeat the currently displayed
command) and tab completion (type a few letters and press tab to
complete a command name or filename in the current directory). When
you are finished using Shell, type
:command:`exit` to leave the session.

.. note:: Not all of Shell's features render correctly in Chrome.
   Firefox is the recommended browser for using Shell.

Most FreeBSD command line utilities are available in Shell.


.. index:: Log Out
.. _Log Out:

Log Out
-------

To log out of the %brand% GUI, click the "Log Out" entry in the tree.
You will immediately be logged out. An informational message will
indicate that you are logged out and will provide a hyperlink which
you can click on to log back in. When logging back in, you will be
prompted for the *root* password.


.. index:: Reboot

.. _Reboot:

Reboot
------

If you click "Reboot", you will receive the warning message shown in
:numref:`Figure %s <reboot1>`
and your browser window color will change to red to indicate that you
have selected an option that will negatively impact users of the
%brand% system.

.. _reboot1:

.. figure:: images/reboot.png

   Reboot Warning Message


If a scrub or resilver is in progress when a reboot is requested, an
additional warning will ask you to make sure that you wish to proceed.
In this case, it is recommended to "Cancel" the reboot request and to
periodically run :command:`zpool status` from `Shell`_ until it is
verified that the scrub or resilver process is complete. Once
complete, the reboot request can be re-issued.

Click the "Cancel" button if you wish to cancel the reboot request.
Otherwise, click the Reboot button to reboot the system. Rebooting the
system will disconnect all clients, including the web administration
GUI. The URL in your web browser will change to add */system/reboot/*
to the end of the IP address. Wait a few minutes for the system to
boot, then use your browser's back button to return to the %brand%
system's IP address. If all went well, you should receive the GUI
login screen. If the login screen does not appear, access the system
using IPMI in order to determine what problem is preventing the system
from resuming normal operation.


.. index:: Shutdown

.. _Shutdown:

Shutdown
--------

If you click "Shutdown", you will receive the warning message shown in
:numref:`Figure %s <shutdown1>`
and your browser color will change to red to indicate that you have
selected an option that will negatively impact users of the %brand%
system.


.. _shutdown1:

.. figure:: images/shutdown.png

   Shutdown Warning Message


If a scrub or resilver is in progress when a shutdown is requested, an
additional warning will ask you to make sure that you wish to proceed.
In this case, it is recommended to "Cancel" the shutdown request and
to periodically run :command:`zpool status` from `Shell`_ until it is
verified that the scrub or resilver process is complete. Once
complete, the shutdown request can be re-issued.

Click the "Cancel" button if you wish to cancel the shutdown request.
Otherwise, click the "Shutdown" button to halt the system. Shutting
down the system will disconnect all clients, including the web
administration GUI, and will power off the %brand% system.


.. index:: Support

.. _Support Icon:

Support Icon
------------

The "Support" icon, located as the third icon from the left in the top
menubar, provides a shortcut to :menuselection:`System --> Support`.
This screen can be used to verify the system license or to create a
support ticket. Refer to :ref:`Support` for detailed usage
instructions.


.. index:: Guide

.. _Guide:

Guide
-----

The "Guide" icon, located as the second icon from the left in the top
menubar, provides a built-in browser to the %brand% Administrator
Guide (this documentation).


#include snippets/alertevents.rst
