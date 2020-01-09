.. _Additional Options:

Additional Options
==================

This section covers the remaining miscellaneous options available from
the %brand% graphical administrative interface.


.. index:: Processes

.. _Display System Processes:

Display System Processes
------------------------

Clicking :guilabel:`Display System Processes` opens a screen showing
the output of
`top(1) <https://www.freebsd.org/cgi/man.cgi?query=top>`__.
An example is shown in
:numref:`Figure %s <system_processes_fig>`.


.. _system_processes_fig:

.. figure:: %imgpath%/display-system-processes.png

   System Processes Running on %brand%


The display automatically refreshes itself. The display is read-only.

.. index:: Shell

.. _Shell:

Shell
-----

The %brand% |web-ui| provides a web shell,
making it convenient to run command line tools from the web browser as
the *root* user.

.. _web_shell_fig:

.. figure:: %imgpath%/shell.png

   Web Shell


The prompt shows that the current user is *root*, the hostname is
*freenas*, and the current working directory is :file:`~`, the home
directory of the logged-in user.

.. note:: The default shell for a new install of %brand% is
   `zsh <https://www.freebsd.org/cgi/man.cgi?query=zsh>`__.
   %brand% systems which have been upgraded from an earlier
   version will continue to use :command:`csh` as the default shell.

   The default shell can be changed in
   :menuselection:`Accounts --> Users`.
   Click |ui-options| and :guilabel:`Edit` for the *root* user. Choose
   the desired shell from the :guilabel:`Shell` drop-down and click
   :guilabel:`SAVE`.


The :guilabel:`Set font size` slider adjusts the size of text
displayed in the Shell. Click :guilabel:`RESTORE DEFAULT` to reset the
shell font and size.

A history of previous commands is available. Use the up and down arrow
keys to scroll through previously entered commands. Edit the command if
desired, then press :kbd:`Enter` to re-enter the command.

:kbd:`Home`, :kbd:`End`, and :kbd:`Delete` keys are supported. Tab
completion is also available. Type a few letters and press :kbd:`Tab` to
complete a command name or filename in the current directory. Right-
clicking in the terminal window displays a reminder about
using :kbd:`Command+c` and :kbd:`Command+v` or :kbd:`Ctrl+Insert` and
:kbd:`Shift+Insert` for copy and paste operations in the %brand% shell.

Type :command:`exit` to leave the session.

Clicking other |web-ui| menus closes the shell session and stops
commands running in the shell.

.. note:: Not all shell features render correctly in Chrome. Firefox
   is the recommended browser when using the shell.


Most FreeBSD command line utilities are available in the
:guilabel:`Shell`.


.. index:: Log Out, Restart, or Shut Down
.. _Log Out, Restart, or Shut Down:


Log Out, Restart, or Shut Down
------------------------------

The |ui-power| button is used to log out of the |web-ui| or
restart or shut down the %brand% system.


.. index:: Log Out
.. _Log Out:

Log Out
~~~~~~~

To log out, click |ui-power|, then :guilabel:`Log Out`. After logging
out, the login screen is displayed.


.. index:: Restart, Reboot

.. _Restart:

Restart
~~~~~~~

Click :guilabel:`Restart` shows the warning message in
:numref:`Figure %s <reboot1>`.

.. _reboot1:

.. figure:: %imgpath%/reboot.png

   Restart Warning Message


If a scrub or resilver is in progress when a restart is requested, an
additional warning asks if you wish to proceed. In this case, it is
recommended to :guilabel:`Cancel` the restart request and to
periodically run :command:`zpool status` from `Shell`_
until it is verified that the scrub or resilver process is complete.
Once complete, the restart request can be re-issued.

Click the :guilabel:`Cancel` button to cancel the reboot request.
Otherwise, set :guilabel:`Confirm` and click :guilabel:`Reboot` to
reboot the system.
Rebooting the system disconnects all clients, including the |web-ui|.
administration GUI. Wait a few minutes for the system to boot. If the
login screen does not appear, access the system using IPMI to
determine if a problem is preventing the system from resuming normal
operation.


.. index:: Shut down, Power off

.. _Shut down:

Shut down
~~~~~~~~~

Clicking :guilabel:`Shut down` shows the warning message in
:numref:`Figure %s <shutdown1>`.


.. _shutdown1:

.. figure:: %imgpath%/shutdown.png

   Shutdown Warning Message


If a scrub or resilver is in progress when a shut down is requested, an
additional warning will ask for confirmation to proceed. In this case,
it is recommended to :guilabel:`Cancel` the shutdown request and to
periodically run :command:`zpool status` from :ref:`Shell` until it is
verified that the scrub or resilver process is complete. Once
complete, the shut down request can be re-issued.

Click the :guilabel:`Cancel` button to cancel the shutdown request.
Otherwise, set :guilabel:`Confirm` and click :guilabel:`SHUT DOWN` to
halt the system. Shutting down the system will disconnect all clients,
including the |web-ui|, and will power off the %brand% system. If the
system has High Availability (HA) with :ref:`Failover` enabled, the
system failsover to the passive |Ctrlr-term|.


#include snippets/alertevents.rst
