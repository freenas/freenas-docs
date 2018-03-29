.. index:: Plugin
.. _Plugins:

Plugins
=======

%brand% 8.2.0 introduced the ability to extend the built-in NAS
services by providing a mechanism for installing additional software.
This mechanism was known as the Plugins architecture and is based on
`FreeBSD jails <https://en.wikipedia.org/wiki/Freebsd_jail>`_
and
`PC-BSD 9.x PBIs
<http://wiki.pcbsd.org/index.php/AppCafe%C2%AE/9.2>`_.
This allowed
users to install and configure additional applications once they had
created and configured a plugins jail.

%brand% 9.x simplifies this procedure by providing two methods for
software installation. The Plugins method, described in this section,
is meant for users who prefer to browse for, install, and configure
available software using the GUI. This method is very easy to use, but
is limited in the amount of software that is available. Each
application will automatically be installed into its own jail, meaning
that this method may not be suitable for users who wish to run
multiple applications within the same jail.

The Jails method provides much more control over software installation
but assumes that the user is comfortable working from the command line
can and has a good understanding of networking basics and software
installation on FreeBSD-based systems.

It is recommended that users skim through both the :ref:`Plugins` and
:ref:`Jails` sections in order to become familiar with the features
and limitations of each and to choose the method that best meets their
software needs.


.. note:: Plugins created for %brand% 9.3 or later are expected to
   work on the current release. Plugins created for earlier releases
   of %brand% must be reinstalled.


.. _Installing Plugins:

Installing
----------

A plugin is a self-contained application installer which has been
designed to integrate into the %brand% GUI. A plugin offers several
advantages:

* the %brand% GUI provides a browser for viewing the list of
  available plugins

* the %brand% GUI provides buttons for installing, starting,
  managing, and deleting plugins

* if the plugin has configuration options, a screen will be added to
  the %brand% GUI so that these options can be configured from the
  GUI

To install a plugin, click :guilabel:`Plugins`. As seen in
:numref:`Figure %s <view_list_plugins_fig>`,
the list of available plugins will be displayed.


.. _view_list_plugins_fig:

.. figure:: images/plugins1b.png

   Viewing the List of Available Plugins


.. note:: if the list of available plugins is not displayed, open
   :ref:`Shell` and verify that the %brand% system can :command:`ping`
   an address on the Internet. If it cannot, you may have to add a
   default gateway address and/or DNS server address in
   :menuselection:`Network --> Global Configuration`.

Highlight the plugin you would like to install, click its
:guilabel:`Install` button, then click :guilabel:`OK`. In the example
shown in
:numref:`Figure %s <installing_plugin_fig>`,
SABnzbd is selected for installation.


.. _installing_plugin_fig:

.. figure:: images/plugins2.png

   Installing a Plugin


The installation will take a few minutes as the system will first
download and configure a jail to contain the installed software. It
will then install the plugin and add it to the :guilabel:`Installed`
tab as shown in
:numref:`Figure %s <view_installed_plugins_fig>`.

.. warning:: Be patient and wait for the installation to finish.
   Navigating away from the installation before it is finished will
   cause problems with the installation.


.. _view_installed_plugins_fig:

.. figure:: images/plugins3a.png

   Viewing Installed PBIs


As seen in the example shown in
:numref:`Figure %s <view_installed_plugins_fig>`,
entries for the installed PBI will appear in the following locations:

* the :guilabel:`Installed` tab of :guilabel:`Plugins`

* the :guilabel:`Plugins` section of the tree

* the :guilabel:`Jails` section of the tree

The entry in the :guilabel:`Installed` tab of Plugins will display the
plugin name and version, the name of the PBI that was installed, the
name of the jail that was created, whether the application status is
:guilabel:`ON` or :guilabel:`OFF`, and a button to delete the
application and its associated jail. If a newer version of the
application is available as a plugin, a button to update the
application will also appear.

.. note:: The :guilabel:`Service status` of a plugin must be turned to
   :guilabel:`ON` before the installed application is available.
   Before starting the service, check to see if it has a configuration
   menu by clicking its entry in the :guilabel:`Plugins` section of
   the tree. If the application is configurable, this will open a
   screen that contains the available configuration options. Plugins
   which are not configurable will instead display a message with a
   hyperlink for accessing the software. However, that hyperlink does
   **not** work until the plugin is started.

Always review a plugin's configuration options before attempting to
start it. some plugins have options that need to be set before their
service will successfully start. If you have never configured that
application before, check the application's website to see what
documentation is available. A link to the website for each available
plugin can be found in :ref:`Available Plugins`.

If the application requires access to the data stored on the %brand%
system, click the entry for the associated jail in the
:guilabel:`Jails` section of the tree and add a storage as described
in :ref:`Add Storage`.

If you need to access the shell of the jail containing the application
to complete or test your configuration, click the entry for the
associated jail in the :guilabel:`Jails` section of the tree. You can
then click its "shell" icon as described in :ref:`Managing Jails`.

Once the configuration is complete, click the red :guilabel:`OFF`
button for the entry for the plugin. If the service starts
successfully, it will change to a blue :guilabel:`ON`. If it fails to
start, click the jail's :guilabel:`Shell` icon and type
:command:`tail /var/log/messages` to see if any errors were logged.


.. _Updating Plugins:

Updating
--------

When a newer version of a plugin becomes available in the official
repository, an :guilabel:`Update` button is added to the entry for the
plugin in the :guilabel:`Installed` tab. In the example shown in
:numref:`Figure %s <updating_installed_plugin_fig>`,
a newer version of Transmission is available.


.. _updating_installed_plugin_fig:

.. figure:: images/plugins4.png

   Updating an Installed Plugin


Click the :guilabel:`OK` button to start the download and installation
of the latest version of the plugin. Once the update is complete, the
entry for the plugin will be refreshed to show the new version number
and the :guilabel:`Update` button will disappear.


.. _Uploading Plugins:

Uploading
---------

The :guilabel:`Available` tab of :guilabel:`Plugins` contains an
:guilabel:`Upload` button. This button allows installation of plugins
that are not yet available in the official repository or which are
still being tested. These plugins must be manually downloaded and
should end in a :file:`.pbi` extension. When downloading a plugin,
make sure that it is 64-bit and that it was developed for 9.x. as 8.x
and 10.x applications will not work on a 9.x %brand% system.

Upload the new plugin with the :guilabel:`Upload` button. As seen in
the example in
:numref:`Figure %s <install_pbi_plugin_fig>`,
this prompts you to browse to the location of the plugin file. Select
the file and click :guilabel:`Upload` to begin the installation.


.. _install_pbi_plugin_fig:

.. figure:: images/plugins5.png

   Installing a Previously Downloaded *.pbi File*


When the installation is complete, an entry for the plugin will be
added to the :guilabel:`Installed` tab and its associated jail is
listed under :guilabel:`Jails`. However, if it is not a %brand%
plugin, it will not be added to :guilabel:`Plugins` in the tree. In
this case, any required jail configuration must be done from the
command line of the jail's shell instead of from the GUI.


.. _Deleting Plugins:

Deleting
--------

When you install a plugin, an associated jail is created. If you
decide to delete a plugin, the associated jail is also deleted as it
is no longer required. **Before deleting a plugin,** make sure that
you do not have any data or configuration in the jail that you need to
save. If you do, back up that data first, **before** deleting the
plugin.

In the example shown in
:numref:`Figure %s <deleting_installed_plugin_fig>`,
Sabnzbd has been installed and the user has clicked its
:guilabel:`Delete` button. A pop-up message asks the user if they are
sure that they want to delete. **This is the one and only warning.**
If the user clicks :guilabel:`Yes`, the plugin and the associated jail
are permanently deleted.


.. _deleting_installed_plugin_fig:

.. figure:: images/plugins6.png

   Deleting an Installed Plugin

.. _Submitting Plugins:

Submitting
----------

Submit a plugin under the
`FreeNAS project on redmine <https://redmine.ixsystems.com/projects/freenas>`__.

Click
:menuselection:`+ --> New Issue` .
The table below shows what each field should contain.

Set :guilabel:`Tracker` to *Feature*.

.. the :guilabel:`Tracker` may change. Kris has said that he could add
   another option in the drop down, related to plugin submisisons.

* :guilabel:`Subject`:

Contains the name and a description of the plugin.

* :guilabel:`Description`:

   * Find the correct port by searching for the plugin at
     `<https://www.freshports.org/>`__. Link the URL of the port.
   * Create and link the URL of the Git artifact repo for the plugin.
     Refer to :numref:`table %s <Artifact Files>` for possible files
     that are in the artifact repo.

.. _Artifact Files:

.. table:: Artifact Files
   :class: longtable

   +-------------------------+----------------------------------------------------------------------+
   | File                    | Description                                                          |
   +=========================+======================================================================+
   | :file:`post_install.sh` | This script is run *inside* the jail after                           |
   |                         | it has been created and packages installed.                          |
   |                         | Enable services in /etc/rc.conf that need to start                   |
   |                         | with the jail startup, apply configuration settings,                 |
   |                         | and more.                                                            |
   +-------------------------+----------------------------------------------------------------------+
   | :file:`ui.json`         | Json file that accepts the  key or value options:                    |
   |                         |                                                                      |
   |                         | :samp:`adminportal: "http://%%IP%%/"`                                |
   |                         |                                                                      |
   |                         | The web-interface of the plugin for control and                      |
   |                         | configuration .                                                      |
   +-------------------------+----------------------------------------------------------------------+
   | :file:`overlay/`        | Directory of files copied on top of the jail post-install.           |
   |                         | For example, :file:`usr/local/bin/myfile` is placed in the jails     |
   |                         | /usr/local/bin/myfile location. Can be used to supply custom         |
   |                         | files and configuration data, scripts, and more.                     |
   +-------------------------+----------------------------------------------------------------------+
   | :file:`settings.json`   | Json file that controls plugins settings interface. The required     |
   |                         | fields include:                                                      |
   |                         |                                                                      |
   |                         | * :samp:`"servicerestart" : "service plexmediaserver restart"`       |
   |                         |                                                                      |
   |                         | Command to run when restarting service after changing settings.      |
   |                         |                                                                      |
   |                         | * :samp:`"serviceget" : "/usr/local/bin/myget"`                      |
   |                         |                                                                      |
   |                         | Points to the command used to get values for plugin configuration.   |
   |                         | Provided by the plugin creator. Can be any language as long as it    |
   |                         | accepts two arguments for key or value pair.                         |
   |                         |                                                                      |
   |                         | * :samp:`"options" : { }`                                            |
   |                         |                                                                      |
   |                         | This subsection contains arrays of elements, starting with the "key" |
   |                         | name and required arguments for that particular type of setting.     |
   +-------------------------+----------------------------------------------------------------------+

Refer to the quassel
`artifact repo <https://github.com/freenas/iocage-plugin-quassel>`__
for an example.

Click :guilabel:`Create` .

.. _Available Plugins:

Available Plugins
-----------------

These plugins are available for %brand% |release|:

* `bacula-sd (storage daemon) <http://bacula.org/>`_

* `CouchPotato <https://couchpota.to/>`_

* `crashplan <http://www.code42.com/crashplan/>`_

* `Emby <http://emby.media/>`_

* `firefly <https://en.wikipedia.org/wiki/Firefly_Media_Server>`_

* `Headphones <https://github.com/rembo10/headphones>`_

* `HTPC-Manager <http://htpc.io/>`_

* `LazyLibrarian <https://github.com/lazylibrarian/LazyLibrarian>`_

* `Madsonic <http://madsonic.org/>`_

* `Maraschino <http://www.maraschinoproject.com/>`_

* `MineOS <http://minecraft.codeemo.com/>`_

* `Mylar <https://github.com/evilhero/mylar>`_

* `Nextcloud <https://nextcloud.com/>`_

* `NZBHydra <https://github.com/theotherp/nzbhydra>`_

* `ownCloud <https://owncloud.org/>`_

* `PlexMediaServer <https://plex.tv/>`_

* `Resilio <https://www.resilio.com/>`_

* `s3cmd <http://s3tools.org/s3cmd>`_

* `SABnzbd <http://sabnzbd.org/>`_

* `SickBeard <http://sickbeard.com/>`_

* `SickRage <https://github.com/SiCKRAGETV/SickRage>`_

* `Sonarr <https://sonarr.tv/>`_

* `Subsonic <http://www.subsonic.org/pages/index.jsp>`_

* `Syncthing <https://syncthing.net/>`_

* `Transmission <http://www.transmissionbt.com/>`_

* `XDM <https://github.com/lad1337/XDM>`_

* `XMRig <https://github.com/xmrig/xmrig>`_

While the %brand% Plugins system makes it easy to install software,
it is still up to you to know how to configure and use the installed
application. When in doubt, refer to the documentation for that
application.
