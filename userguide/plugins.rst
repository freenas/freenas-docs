.. index:: Plugin
.. _Plugins:

Plugins
=======

.. warning:: The legacy plugins infrastructure has been deprecated and
   is no longer supported. Plugins installation has been removed from
   the legacy UI but it can still be used to manage existing plugins.
   It is recommended to reinstall all legacy plugins using the new UI.

.. _Installed Plugins:

Installed Plugins
------------------

Entries for installed PBI will appear in these locations:

* the :guilabel:`Installed` tab of :guilabel:`Plugins`

* the :guilabel:`Plugins` section of the tree

* the :guilabel:`Jails` section of the tree

The entry in the :guilabel:`Installed` tab of Plugins displays the
plugin name and version, the name of the PBI installed, the
name of the jail, whether the application status is
:guilabel:`ON` or :guilabel:`OFF`, and a button to delete the
application and its associated jail.

.. note:: The :guilabel:`Service status` of a plugin must be turned to
   :guilabel:`ON` before the installed application is available.
   Before starting the service, check to see if it has a configuration
   menu by clicking its entry in the :guilabel:`Plugins` section of
   the tree. If the application is configurable, this will open a
   screen that contains the available configuration options. Plugins
   which are not configurable display a message with a
   hyperlink for accessing the software. However, that hyperlink does
   **not** work until the plugin is started.

Always review the configuration options of a plugin before attempting to
start it. Some plugins have options that need to be set before their
service will successfully start. If the application has not been
configured before, check the website of the application to see what
documentation is available.

If the application requires access to the data stored on the %brand%
system, click the entry for the associated jail in the
:guilabel:`Jails` section of the tree and add a storage as described
in :ref:`Add Storage`.

Access the shell of the jail containing the application by
clicking the entry for the associated jail in the :guilabel:`Jails`
section of the tree. You can then click its shell icon as described
in :ref:`Managing Jails`.

Once the configuration is complete, click the red :guilabel:`OFF`
button for the entry for the plugin. If the service starts
successfully, it will change to a blue :guilabel:`ON`. If it fails to
start, click the jail's :guilabel:`Shell` icon and type
:command:`tail /var/log/messages` to see if any errors were logged.


.. _Deleting Plugins:

Deleting Plugins
----------------

Deleting a plugin deletes the associated jail as it
is no longer required. **Before deleting a plugin,** make sure that
there is no data or configuration options in the jail that need to be
saved. Back up that data **before** deleting the plugin.

In the example shown in
:numref:`Figure %s <deleting_installed_plugin_fig>`,
Sabnzbd is installed and the user has clicked the
:guilabel:`Delete` button. A pop-up message displays.
**This is the one and only warning.**


.. _deleting_installed_plugin_fig:

.. figure:: images/plugins6.png

   Deleting an Installed Plugin
