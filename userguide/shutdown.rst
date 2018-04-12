.. index:: Shutdown
.. _Shutdown:

Shutdown
========

Clicking
:menuselection:`Settings --> Shutdown`
opens the warning message shown in
:numref:`Figure %s <shutdown_warning_fig>`.


.. _shutdown_warning_fig:

.. figure:: images/shutdown.png

   Shutdown Warning Message


.. If a scrub or resilver is in progress when a shutdown is requested, an
   additional warning will ask if you wish to proceed. In this case, it
   is recommended to :guilabel:`Cancel` the shutdown request and to
   periodically run :command:`zpool status` from :ref:`Shell` until the
   scrub or resilver process is complete. Once complete, the shutdown
   request can be re-issued.

   ^commented out because was unable to test this. Scrubs were
   completing very quickly and couldn't shut it down while it
   was scrubbing postponed until later date.

Click the :guilabel:`Cancel` button to cancel the shutdown request.
Check the :guilabel:`Confirm` check box and click the
:guilabel:`Shutdown` button to shutdown the system. Shutting down the
system disconnects all clients, including the web administration GUI.
Physical access to the %brand% system is needed to turn it back on.
