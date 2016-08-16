.. index:: Shutdown
.. _Shutdown:

Shutdown
========

If you click the "Shutdown" entry in the tree, you will receive the
warning message shown in
:numref:`Figure %s <shutdown_warning_fig>`
and the browser window color will change
to red to indicate that this command will negatively impact current
users of the %brand% system.


.. _shutdown_warning_fig:

.. figure:: images/shutdown.png

   Shutdown Warning Message


If a scrub or resilver is in progress when a shutdown is requested, an
additional warning will ask if you wish to proceed. In this case, it
is recommended to "Cancel" the shutdown request and to periodically
run :command:`zpool status` from :ref:`Shell` until it is verified
that the scrub or resilver process is complete. Once complete, the
shutdown request can be re-issued.

Click the "Cancel" button to cancel the shutdown request. Otherwise,
click the "Shutdown" button to halt the system. Shutting down the
system will disconnect all clients, including the web administration
GUI, and will power off the %brand% system. Physical access to the
%brand% system will be needed to turn it back on.
