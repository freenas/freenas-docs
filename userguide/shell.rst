.. index:: Shell
.. _Shell:

Shell
=====

Beginning with version 8.2.0, the %brand% |web-ui| provides a web shell,
making it convenient to run command line tools from the web browser as
the *root* user.

.. _web_shell_fig:

.. figure:: images/shell.png

   Web Shell


The prompt indicates that the current user is *root*, the hostname is
*freenas*, and the current working directory is :file:`~`, which is the
*root* home directory.

.. note:: The default shell for a new install of %brand% is
   :command:`zsh`. %brand% systems that are upgraded from an earlier
   version will continue to use :command:`csh` as the default shell.
   The default shell can be changed by going to
   :menuselection:`Account --> Users`.
   Select the *root* user and click :guilabel:`Modify User`.
   Choose the desired shell from the :guilabel:`Shell` drop-down and
   click :guilabel:`OK`.


To change the size of the shell, click the *80x25* drop-down menu and
select a different size.

To copy text from shell, highlight the text, right-click, and select
:guilabel:`Copy`. Paste text into the shell by clicking
:guilabel:`Paste`, pasting text into the field, and clicking
:guilabel:`OK`.

Shell provides a history of commands used. Use the arrow keys to see
previously entered commands and press :kbd:`Enter` to repeat the
command.

The :kbd:`Home`, :kbd:`End`, and :kbd:`Delete` keys are supported.
:kbd:`Tab` completion is also available. Type a few letters and press
:kbd:`Tab` to complete a command name or filename in the current
directory.

Type :command:`exit` to leave the session.

Using the default shell prevents access to any of the other |web-ui|
menus. Use :ref:`tmux` as the |web-ui| shell to open, detach, and
reattach multiple shell sessions.

.. note:: Not all shell features render correctly in Chrome.
   Firefox is the recommended browser when using the shell.


Most FreeBSD :ref:`command line utilities <Command Line Utilities>` are
available in the :guilabel:`Shell`, including additional troubleshooting
applications for %brand%.
