.. index:: Shell
.. _Shell:

Shell
=====

Beginning with version 8.2.0, the %brand% GUI provides a web shell,
making it convenient to run command line tools from the web browser as
the *root* user. The link to Shell is the fourth entry from the bottom
of the menu tree. In
:numref:`Figure %s <web_shell_fig>`,
the link has been clicked and Shell is open.


.. _web_shell_fig:

.. figure:: images/shell.png

   Web Shell


The prompt indicates that the current user is *root*, the hostname is
*freenas*, and the current working directory is :file:`~`
(*root*'s home directory).

To change the size of the shell, click the *80x25* drop-down menu and
select a different size.

To copy text from shell, highlight the text, right-click, and select
"Copy" from the right-click menu. To paste into the shell, click the
"Paste" button, paste the text into the box that opens, and click the
"OK" button to complete the paste operation.

Shell provides history (use your up arrow to see previously entered
commands and press :kbd:`Enter` to repeat the currently displayed
command) and tab completion (type a few letters and press tab to
complete a command name or filename in the current directory). When
you are finished using Shell, type :command:`exit` to leave the
session.

While you are in Shell, you will not have access to any of the other
GUI menus. If you need to have access to a prompt while using the GUI
menus, use :ref:`tmux` instead as it supports multiple shell sessions
and the detachment and reattachment of sessions.

.. note:: Not all of Shell's features render correctly in Chrome.
   Firefox is the recommended browser for using Shell.

Most FreeBSD command line utilities are available in Shell. Additional
troubleshooting utilities that are provided by %brand% are described
in :ref:`Command Line Utilities`.
