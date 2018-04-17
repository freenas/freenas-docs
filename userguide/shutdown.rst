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


.. If a scrub or resilver is running, a warning is shown. Clicking
   :guilabel:`Cancel` is reocommended. :command:`zpool status` can be
   run from the :ref:`Shell` to watch for the scrub or resilver to
   complete. Then the system can be shut down normally.

   ^commented out because was unable to test this. Scrubs were
   completing very quickly and couldn't shut it down while it
   was scrubbing. Postponed until later date.

Check the :guilabel:`Confirm` check box and click the
:guilabel:`Shutdown` button to shutdown the system. Shutting down the
system disconnects all clients, including the web administration GUI.
Physical access to the %brand% system is required to turn it back on.
