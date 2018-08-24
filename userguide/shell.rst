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

.. note:: The default shell for a new install of %brand% is
   :command:`zsh`. %brand% systems that are upgraded from an earlier
   version will continue to use :command:`csh` as the default shell.
   The default shell can be changed by going to
   :menuselection:`Account --> Users`.
   Select the desired user and click :guilabel:`Modify User`.
   Choose the desired shell from the :guilabel:`Shell` drop-down.

To change the size of the shell, click the *80x25* drop-down menu and
select a different size.

To copy text from shell, highlight the text, right-click, and select
:guilabel:`Copy` from the right-click menu. To paste into the shell,
click the :guilabel:`Paste` button, paste the text into the box that
opens, and click the :guilabel:`OK` button to complete the paste
operation.

Shell provides a history of commands used. Use the arrow keys to see
previously entered commands and press :kbd:`Enter` to repeat the
command.The keys :kbd:`Home`, :kbd:`End`, and :kbd:`Delete` are also
supported in the shell. The shell also provides tab completion. Type a
few letters and press tab to complete a command name or filename in the
current directory. Type :command:`exit` to leave the session.

Using the shell prevents access to any of the other
GUI menus. To have access to a prompt while using the GUI
menus, use :ref:`tmux` instead as it supports multiple shell sessions
and the detachment and reattachment of sessions.

.. note:: Not all of Shell's features render correctly in Chrome.
   Firefox is the recommended browser for using Shell.

Most FreeBSD command line utilities are available in Shell. Additional
troubleshooting utilities that are provided by %brand% are described
in :ref:`Command Line Utilities`.
