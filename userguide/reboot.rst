.. index:: Reboot
.. _Reboot:

Reboot
======

Clicking the :guilabel:`Reboot` entry in the tree shows the
warning message in
:numref:`Figure %s <reboot_warning_fig>`.
The browser screen color changes to red to indicate that this option
will negatively impact current users of the %brand% system.

.. _reboot_warning_fig:

.. figure:: images/reboot.png

  Reboot Warning Message


An additional warning message appears when a restart is attempted
on a system with a scrub or resilver in progress.
In this case, it is recommended to :guilabel:`Cancel` the reboot
request and to periodically run :command:`zpool status` from Shell
until it is verified that the scrub or resilver process is complete.
Once complete, the reboot request can be reissued.

Click the :guilabel:`Cancel` button to cancel the reboot request.
Otherwise, click the :guilabel:`Reboot` button to reboot the system.
Rebooting the system disconnects all clients, including the web
administration GUI. The URL in the web browser changes to add
*/system/reboot/* to the end of the IP address. Wait a few minutes for
the system to boot, then use the back button in the browser to return to
the IP address of the %brand% system. The GUI login screen appears after
a successful reboot. If the login screen does not appear, using a monitor
and keyboard to physically access the %brand% system is required to
determine the problem that is preventing the system from resuming normal
operation.
