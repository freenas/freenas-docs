.. index:: Shutdown
.. _Shutdown:

Shutdown
========

Clicking the :guilabel:`Shutdown` entry in the tree opens the
warning message shown in
:numref:`Figure %s <shutdown_warning_fig>`.
The browser window color changes to red to indicate that this command
will negatively impact current users of the %brand% system.


.. _shutdown_warning_fig:

.. figure:: images/shutdown.png

   Shutdown Warning Message


If a scrub or resilver is in progress when a shutdown is requested, an
additional warning will ask if you wish to proceed. In this case, it
is recommended to :guilabel:`Cancel` the shutdown request and to
periodically run :command:`zpool status` from :ref:`Shell` until the
scrub or resilver process is complete. Once complete, the shutdown
request can be re-issued.

Click the :guilabel:`Cancel` button to cancel the shutdown request.
Otherwise, click the :guilabel:`Shutdown` button to halt the system.
Shutting down the system disconnects all clients, including the web
administration GUI, and powers off the %brand% system. Physical access
to the %brand% system will be needed to turn it back on.
