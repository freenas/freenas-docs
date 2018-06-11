.. index:: Restart
.. _Restart:

Restart
=======

Click |ui-settings| then :guilabel:`Restart`
to see a confirmation screen like
:numref:`Figure %s <reboot_warning_fig>`.
:guilabel:`Confirm` the action and click
:guilabel:`Ok` to restart the system.

.. _reboot_warning_fig:

.. figure:: images/reboot.png

  Restart Warning Message

An additional warning message appears when a restart is attempted
on a system with a scrub or resilver in progress.
In this case, it is recommended to :guilabel:`Cancel` the restart
request and to periodically run :command:`zpool status` from Shell
until it is verified that the scrub or resilver process is complete.
Once complete, the restart request can be reissued.

Click the :guilabel:`Cancel` button to cancel the restart request.
Otherwise, click the :guilabel:`Restart` button to restart the
system. Restarting the system disconnects all clients, including
the web administration GUI. Wait a few minutes for
the system to boot, then use the back button in the browser
to return to the IP address of the %brand% system. The GUI login
screen appears after a successful reboot.
If the login screen does not appear, using a monitor and keyboard to
physically access the %brand% system is required to
determine the issue preventing the system from resuming normal
operation.
