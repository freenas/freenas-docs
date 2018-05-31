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


If a scrub or resilver is running, a warning is shown. Clicking
:guilabel:`Cancel` is recommended. :command:`zpool status` can be
run from the :ref:`Shell` to watch for the scrub or resilver to
complete. Then the system can be shut down normally.

:guilabel:`Confirm` the command and click :guilabel:`Shutdown` to
shutdown the system. Shutting down the system disconnects all clients,
including the web administration GUI. Physical access to the %brand%
system is required to turn it back on.
