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


If a scrub or resilver is in progress when a reboot is requested, an
additional warning will ask you to make sure that you wish to proceed.
In this case, it is recommended to :guilabel:`Cancel` the reboot
request and to periodically run :command:`zpool status` from Shell
until it is verified that the scrub or resilver process is complete.
Once complete, the reboot request can be re-issued.

Click the :guilabel:`Cancel` button to cancel the reboot request.
Otherwise, click the :guilabel:`Reboot` button to reboot the system.
Rebooting the system disconnects all clients, including the web
administration GUI. The URL in the web browser changes to add
*/system/reboot/* to the end of the IP address. Wait a few minutes for
the system to boot, then use your browser's "back" button to return to
the %brand% system's IP address. If all went well, the GUI login
screen will appear. If the login screen does not appear, physical
access to the %brand% system's monitor and keyboard is needed to
determine what problem is preventing the system from resuming normal
operation.
