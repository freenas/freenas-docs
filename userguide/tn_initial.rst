Initial Setup
=============


Hardware Setup
--------------

*Basic Setup Guides* for %brand% systems and expansion
shelves are included with the hardware and also available in the
`iX Information Library <https://www.ixsystems.com/blog/knowledgebase_category/truenas/>`__.
These guides provide detailed instructions on included components,
controls, ports, rack installation, drive loading, and cable
connections.

Complete hardware installation before continuing.


.. note:: Always perform the initial %brand% setup in consultation
   with your iXsystems Support Representative. iXsystems Support can
   be contacted at :literal:`truenas-support@ixsystems.com`. Be sure
   to have all %brand% hardware serial numbers on hand. The serial
   numbers are located on the back of each chassis.


.. index:: Console Setup Menu
.. _Console Setup Menu:

Console Setup Menu
------------------

#include snippets/console_menu.rst


During boot, %brand% automatically attempts to connect to a DHCP
server from all live interfaces. If it successfully receives an IP
address, the address is displayed so it can be used to access the
graphical user interface. In the example seen in
:numref:`Figure %s <console_setup_menu_fig>`,
the %brand% system is accessible at *http://10.0.0.102*.

Some %brand% systems are set up without a monitor, making it
challenging to determine which IP address has been assigned. On
networks that support Multicast DNS (mDNS), the hostname and domain
can be entered into the address bar of a browser. By default, this
value is *truenas.local*.

If the %brand% server is not connected to a network with a DHCP
server, use the console network configuration menu to manually
configure the interface as shown here. In this example, the %brand%
system has one network interface, *em0*.


.. code-block:: none

   Enter an option from 1-12: 1
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


.. index:: GUI Access, Web Interface
.. _Accessing the Web Interface:

Accessing the |Web-UI|
----------------------

Configuring an IP address for the system enables |web-ui| access. To
access the %brand% |web-ui|, use a computer on the same network as the
%brand% system. Enter the configured IP address into a web browser. A
login screen appears.

.. _tn_login1:

.. figure:: images/truenas/login1c.png

   %brand% Login Screen


The :ref:`High Availability (HA) <Failover>` status and information
about the active |ctrlr-term| is displayed on this screen. To log in,
enter::

 Username: root
 Password: abcd1234


.. note:: The default *root* password can be changed to a more
   secure value by going to
   :menuselection:`Accounts --> Users`.
   Expand the entry for *root* and click |ui-edit|. Enter the new
   password in the :guilabel:`Password` and :guilabel:`Confirm Password`
   fields and click :guilabel:`SAVE`. The new password is required for
   subsequent logins.


On the first login, the EULA found in :ref:`Appendix A` is displayed,
along with a box where the license key for the %brand% array can be
pasted. Read the EULA and paste in the license key. High Availability
(HA) systems must have both active and standby |ctrlrs-term| booted
before the license key for the HA %brand% system can be entered. The key
is entered on the active |ctrlr-term|. Click :guilabel:`OK` to save the
license key and access the |web-ui|.

.. _tn_initial:

.. figure:: images/truenas/initial1c.png

   %brand% Graphical Configuration Menu


When the storage devices are encrypted, a prompt requests the encryption
passphrase. It must be correctly entered for the data on the disks to be
accessible. When the system is licensed for High Availability (HA), the
passphrase is remembered as long as either |ctrlr-term| in the HA unit
remains up. If both |ctrlrs-term| are powered off, the passphrase must
be re-entered when the first |ctrlr-term| powers back up.

If the user interface is not accessible by IP address from a browser,
check these things:

* Are proxy settings enabled in the browser configuration? If so,
  disable the settings and try connecting again.

* If the page does not load, make sure that a :command:`ping` reaches
  the %brand% system's IP address. If the address is in a private
  IP address range, it is only accessible from within that private
  network.

* If the user interface loads but is unresponsive or seems to be
  missing menu items, try a different web browser.

* If "An error occurred!" messages are shown when attempting to
  configure an item in the |web-ui|, make sure that the browser is set
  to allow cookies from the %brand% system.

This
`blog post <http://fortysomethinggeek.blogspot.com/2012/10/ipad-iphone-connect-with-freenas-or-any.html>`_
describes some applications which can be used to access the %brand%
system from an iPad or iPhone.

The rest of this Guide describes all of the configuration screens
available within the %brand% graphical administrative interface.
The screens are listed in the order that they appear within the
tree, or the left frame of the graphical interface.

Please :ref:`contact iXsystems Support <Contacting iXsystems>` for
initial setup and configuration assistance.

.. warning:: It is important to use the |web-ui| or the console setup
   menu for all configuration changes. Do not make changes from the
   command line unless directed by an iXsystems Support Engineer or
   proven %brand% expert.
