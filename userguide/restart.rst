.. index:: Restart
.. _Restart:

Restart
=======

Click :menuselection:`Gear Icon ---> Restart`.
to see a confirmation screen like
:numref:`Figure %s <reboot_warning_fig>`. Tick the
:guilabel:`Confirm` checkbox and click
:guilabel:`Ok` to restart the system.

.. _reboot_warning_fig:

.. figure:: images/reboot.png

  Restart Warning Message

An additional warning message will appear when a restart is attempted
on a system with a scrub or resilver in progress.
In this case, it is recommended to :guilabel:`Cancel` the restart
request and to periodically run :command:`zpool status` from Shell
until it is verified that the scrub or resilver process is complete.
Once complete, the rebstart request can be re-issued.

Click the :guilabel:`Cancel` button to cancel the restart request.
Otherwise, click the :guilabel:`Restart` button to restart the
system. Restarting the system disconnects all clients, including
the web administration GUI. Wait a few minutes for
the system to boot, then use the back browser button in the browser
to return to the %brand% system's IP address. The GUI login
screen will appear after a successful reboot.
If the login screen does not appear, physical
access to the %brand% system's monitor and keyboard is needed to
determine the problem preventing the system from resuming normal
operation.
