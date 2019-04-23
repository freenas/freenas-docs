.. _Booting:

Booting
-------

#include snippets/console_menu.rst


.. _Obtaining_an_IP_Address:

Obtaining an IP Address
^^^^^^^^^^^^^^^^^^^^^^^

During boot, %brand% automatically attempts to connect to a DHCP
server from all live network interfaces. After %brand% successfully
receives an IP address, the address is displayed so it can be used
to access the |web-ui|. The example in
:numref:`Figure %s <console_setup_menu_fig>` shows a
%brand% system that is accessible at *http://10.0.0.102*.

Some %brand% systems are set up without a monitor, making it
challenging to determine which IP address has been assigned. On
networks that support Multicast DNS (mDNS), the hostname and domain
can be entered into the address bar of a browser. By default, this
value is *freenas.local*.

If the %brand% server is not connected to a network with a DHCP
server, use the console network configuration menu to manually
configure the interface as shown here. In this example, the %brand%
system has one network interface, *em0*.


.. code-block:: none

   Enter an option from 1-11: 1
   1) em0
   Select an interface (q to quit): 1
   Remove the current settings of this interface? (This causes a momentary disconnec
   tion of the network.) (y/n) n
   Configure interface for DHCP? (y/n) n
   Configure IPv4? (y/n) y
   Interface name:     (press enter, the name can be blank)
   Several input formats are supported
   Example 1 CIDR Notation:
       192.168.1.1/24
   Example 2 IP and Netmask separate:
       IP: 192.168.1.1
       Netmask: 255.255.255.0, or /24 or 24
   IPv4 Address: 192.168.1.108/24
   Saving interface configuration: Ok
   Configure IPv6? (y/n) n
   Restarting network: ok

   ...

   The web user interface is at
   http://192.168.1.108


After the system has an IP address, enter that address into a
graphical web browser from a computer connected to the same network as
the %brand% system.

.. _Logging_In:

Logging In
^^^^^^^^^^

The password for the root user is requested as shown in
:numref:`Figure %s <booting_enter_root_pass_fig>`.


.. _booting_enter_root_pass_fig:

.. figure:: images/log-in.png

   Enter the Root Password


.. note:: The %brand% |web-ui| now uses Angular and a new, asynchronous
   middleware. To use the legacy Django |web-ui| that was used before
   version 11.2, click :guilabel:`LEGACY WEB INTERFACE`. This User Guide
   only demonstrates the new Angular |web-ui|.


Enter the password chosen during the installation. A prompt is shown
to set a root password if it was not set during installation.

The |web-ui| is displayed after login:


.. _booting_graphic_config_menu_fig:

.. figure:: images/dashboard.png

   %brand% Graphical Configuration Menu


#ifdef freenas
The rest of this User Guide describes the %brand% |web-ui| in
more detail. The layout of this User Guide follows the order of the menu
items in the tree located in the left frame of the |web-ui|.

.. note:: To keep lists aligned when using zoom in Firefox, ensure
   :menuselection:`View --> Zoom --> Zoom Text Only`
   is not set.

.. note:: It is important to use the |web-ui| or the Console Setup
   menu for all configuration changes. %brand% uses a configuration
   database to store its settings. While it is possible to use the
   command line to modify the configuration, changes made at the
   command line **are not** written to the configuration database.
   This means that any changes made at the command line will not
   persist after a reboot and will be overwritten by the values in the
   configuration database during an upgrade.
#endif freenas

If the %brand% system does not respond to the IP address or mDNS name
entered in a browser:

* Check for enabled proxy settings in the browser configuration, disable
  them, and try connecting again.

* :command:`ping` the %brand% system IP address from another computer
  on the same network.

* Try a different web browser if the user interface loads but is
  unresponsive or seems to be missing menu items.
  `Firefox <https://www.mozilla.org/en-US/firefox/all/>`__ is
  recommended.

* Make sure that the browser is set to allow cookies from the
  %brand% system.
