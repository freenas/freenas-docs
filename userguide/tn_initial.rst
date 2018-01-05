Initial Setup
=============

Before beginning software configuration, please see the
:ref:`Hardware Setup` section for specific racking and connection
information.

Depending on the degree of pre-configuration requested from iXsystems,
most of the initial %brand% setup might already be complete.

.. note:: Always perform the initial %brand% setup in consultation
   with your iXsystems Support Representative. iXsystems Support can
   be contacted at :literal:`truenas-support@ixsystems.com`. Be sure
   to have all %brand% hardware serial numbers on hand. They are
   located on the back of each chassis.


.. index:: Out-of-Band Management

.. _Out-of-Band Management:

Out-of-Band Management
----------------------

Before attempting to configure %brand% for out-of-band management,
ensure that the out-of-band management port is connected to an
appropriate network. Refer to the guide included with the %brand%
Storage Array for detailed instructions on how to connect to a
network.

Connect the out-of-band management port **before** powering on the
%brand% Storage Array.

In most cases, the out-of-band management interface will have been
pre-configured by iXsystems. This section contains instructions for
configuring it from the BIOS if needed. The same settings can be
configured using the instructions in :ref:`IPMI`.

Press :kbd:`F2` at the splash screen while the %brand% Storage Array
is booting to access the system BIOS. This opens the menu shown in
:numref:`Figure %s <appliance34>`.


.. _appliance34:

.. figure:: images/tn_BIOS1.png

   Initial BIOS Screen


Navigate to the :guilabel:`Server Mgmt` menu and then
:guilabel:`BMC LAN Configuration`, as shown in
:numref:`Figure %s <appliance35>`.


.. _appliance35:

.. figure:: images/tn_BIOS2.png

   Navigate to BMC LAN Configuration


When using DHCP to assign the out-of-band management IP address, leave
the :guilabel:`Configuration Source` set to
:guilabel:`Dynamic` in the screen shown in
:numref:`Figure %s <appliance36>`.
If an IP has been assigned by DHCP, it is displayed.


.. _appliance36:

.. figure:: images/tn_BIOS3.png

   Configuring a Dynamic IP Address


To assign a static IP address for out-of-band management, set the
:guilabel:`Configuration Source` to *Static*, as shown in
:numref:`Figure %s <appliance37>`.
Enter the desired IP Address into the :guilabel:`IP Address` setting,
filling out all four octets completely.


.. _appliance37:

.. figure:: images/tn_BIOS4.png

   Configuring a Static IP Address


Next, enter the :guilabel:`Subnet Mask` of the out-of-band management
network subnet. An example is shown in
:numref:`Figure %s <appliance38>`.


.. _appliance38:

.. figure:: images/tn_BIOS5.png

   Entering the Subnet Mask


Finally, set the :guilabel:`Default Gateway Address` for the network
to which the out-of-band management port is connected. An example is
shown in
:numref:`Figure %s <appliance39>`.


.. _appliance39:

.. figure:: images/tn_BIOS6.png

   Entering the Default Gateway Address


Save the changes, exit the BIOS, and allow the system to boot.

To connect to the %brand% Storage Array's out-of-band management port,
enter the IP address into a web browser from a computer that is either
within the same network or which is directly wired to the array. As
shown in
:numref:`Figure %s <appliance40>`,
a login prompt appears.


.. _appliance40:

.. figure:: images/tn_IPMIlogin.png

   Connecting to the IPMI Graphical Interface


Log in using the default :guilabel:`Username` of *admin* and the
default :guilabel:`Password` of *password*.

The administrative password can be changed using the instructions in
:ref:`IPMI`.

After logging in, click the :guilabel:`vKVM and Media` button at the
top right to download the Java KVM Client. Run the client by clicking
the :guilabel:`Launch Java KVM Client` button shown in
:numref:`Figure %s <tn_IPMIdownload>`.


.. _tn_IPMIdownload:

.. figure:: images/tn_IPMIdownload.png

   Launching the Java KVM Client


When prompted for a program to open the file with, select the Java
Web Start Launcher shown in
:numref:`Figure %s <appliance41>`.


.. _appliance41:

.. figure:: images/tn_IPMIjava.png

   Configure the Launch Program


If asked to verify running a program from an unknown publisher, check
the box indicating that you understand the risks and press
:guilabel:`Run`. An example is shown in
:numref:`Figure %s <appliance42>`.


.. _appliance42:

.. figure:: images/tn_IPMIaccept.png

   Respond to Warning


When prompted that the connection is untrusted, as shown in
:numref:`Figure %s <tn_IPMIcontinue>`,
press :guilabel:`Continue`.


.. _tn_IPMIcontinue:

.. figure:: images/tn_IPMIcontinue.png

   Continue Through this Screen


With the out-of-band console open, the %brand% Storage Array can be
controlled as if using a directly-connected keyboard and monitor.


.. index:: Console Setup Menu
.. _Console Setup Menu:

Console Setup Menu
------------------

The Console Setup menu, shown in
:numref:`Figure %s <console_setup_menu_fig>`,
appears at the end of the boot process. If access to the %brand%
system's keyboard and monitor is available, this Console Setup menu
can be used to administer the system even if the administrative GUI is
not accessible.


#include snippets/consolesetupnote.rst


.. _console_setup_menu_fig:

.. figure:: images/tn_console1.png

   Console Setup Menu


This menu provides these options:

**1) Configure Network Interfaces:** provides a configuration
wizard to configure the system's network interfaces. If the system has
been licensed for High Availability (HA), the wizard prompts for
IP addresses for both :guilabel:`(This Node)` and
:guilabel:`(Node B)`.

**2) Configure Link Aggregation:** allows creating a new link
aggregation or deleting an existing link aggregation. If the system
has been licensed for High Availability (HA), this option prompts
for the VHID when creating the link aggregation.

**3) Configure VLAN Interface:** used to create or delete a VLAN
interface.

**4) Configure Default Route:** used to set the IPv4 or IPv6
default gateway. When prompted, enter the IP address of the default
gateway.

**5) Configure Static Routes:** prompts for the destination
network and the gateway IP address. Re-enter this option for each
route to be added.

**6) Configure DNS:** will prompt for the name of the DNS domain
then the IP address of the first DNS server. To enter multiple DNS
servers, press :kbd:`Enter` to enter the next one. When finished,
press :kbd:`Enter` twice to leave this option.

**7) Reset Root Password:** if logging in to the
graphical administrative interface fails, select this option and
follow the prompts to set the *root* password.

**8) Reset Configuration to Defaults:** to delete **all** of the
configuration changes made in the administrative GUI, select this
option. Once the configuration is reset, the system will reboot. It
will be necessary to go to
:menuselection:`Storage --> Volumes --> Import Volume`
to re-import volumes.

**9) Shell:** starts a shell to run FreeBSD commands. To leave the
shell, type :command:`exit`.

**10) System Update:** if any system updates are available, they
will automatically be downloaded and applied. The functionality is
the same as described in :ref:`Update`, except that the updates
will be applied immediately and access to the GUI is not required.

**11) Reboot:** reboot the system.

**12) Shutdown:** shut down the system.

.. note:: The numbering and quantity of options on this menu can
   change due to software updates, service agreements, or other
   factors. Please carefully check the menu before selecting an
   option, and keep this in mind when writing local procedures.


During boot, %brand% automatically attempts to connect to a DHCP
server from all live interfaces. If it successfully receives an IP
address, the address is displayed so it can be used to access the
graphical user interface. In the example seen in
:numref:`Figure %s <console_setup_menu_fig>`,
the %brand% system is accessible at *http://10.0.0.142*.

Some %brand% systems are set up without a monitor, making it
challenging to determine which IP address has been assigned. On
networks that support Multicast DNS (mDNS), the hostname and domain
can be entered into the address bar of a browser. By default, this
value is *truenas.local*.

If the %brand% server is not connected to a network with a DHCP
server, the console network menu can be used to manually
configure the interface as seen in
:ref:`Example: Manually Setting an IP Address from the Console Menu
<quick_manual_ip_topic>`.
In this example, the %brand% system has one network interface, *em0*.

.. topic:: Manually Setting an IP Address from the Console Menu
   :name: quick_manual_ip_topic

   .. code-block:: none

      Enter an option from 1-12: 1
      1) em0
      Select an interface (q to quit): 1
      Reset network configuration? (y/n) n
      Configure interface for DHCP? (y/n) n
      Configure IPv4? (y/n) y
      Interface name: (press enter as can be blank)
      Several input formats are supported
      Example 1 CIDR Notation: 192.168.1.1/24
      Example 2 IP and Netmask separate: IP: 192.168.1.1
      Netmask: 255.255.255.0, or /24 or 24
      IPv4 Address: 192.168.1.108/24
      Saving interface configuration: Ok
      Configure IPv6? (y/n) n
      Restarting network: ok
      You may try the following URLs to access the web user interface:
      http://192.168.1.108


.. index:: GUI Access
.. _Accessing the Administrative GUI:

Accessing the Administrative GUI
--------------------------------

After the system has an IP address, enter that address into a
graphical web browser from a computer on the same network as the
%brand% system. A prompt appears to enter the password for the *root*
user, as shown in
:numref:`Figure %s <tn_login1>`.


.. _tn_login1:

.. figure:: images/tn_login1c.png

   Enter the Root Password


Enter the default password of *abcd1234*.

.. note:: The default *root* password can be changed to a more
   secure value by going to
   :menuselection:`Account --> Users --> View Users`.
   Highlight the entry for *root*, click the :guilabel:`Modify User`
   button, enter the new password in the :guilabel:`Password` and
   :guilabel:`Password confirmation` fields, and click :guilabel:`OK`
   to save the new password to use on subsequent logins.

On the first login, the EULA found in :ref:`Appendix A` is displayed,
along with a box where the license key for the %brand% array can be
pasted. Read the EULA, paste in the license key, then click
:guilabel:`OK`. The administrative GUI appears, as shown in the
example in
:numref:`Figure %s <tn_initial>`.

.. note:: Entering the license key for a High Availability pair is
   not allowed unless both the active and standby computers are up.
   The key is entered on the active computer.


.. _tn_initial:

.. figure:: images/tn_initial1c.png

   %brand% Graphical Configuration Menu


.. note:: If the storage devices have been encrypted, a prompt appears
   for the passphrase. It must be correctly entered for the data on
   the disks to be accessible. If the system has also been licensed
   for High Availability (HA), the passphrase will be remembered as
   long as either node in the HA unit remains up. If both nodes are
   powered off, the passphrase must be re-entered when the first node
   powers back up.


If the user interface is not accessible by IP address from a browser,
check these things:

* Are proxy settings enabled in the browser configuration? If so,
  disable the settings and try connecting again.

* If the page does not load, make sure that a :command:`ping` reaches
  the %brand% system's IP address. If the address is in a private
  IP address range, it is only accessible from within that private
  network.

* If the user interface loads but is unresponsive or seems to be
  missing menu items, try a different web browser. IE9 has known
  issues and will not display the graphical administrative interface
  correctly if compatibility mode is turned on. If the GUI cannot
  be accessed with Internet Explorer, use
  `Firefox <https://www.mozilla.org/en-US/firefox/all/>`_
  instead.

* If "An error occurred!" messages are shown when attempting to
  configure an item in the GUI, make sure that the browser is set
  to allow cookies from the %brand% system.

This
`blog post <http://fortysomethinggeek.blogspot.com/2012/10/ipad-iphone-connect-with-freenas-or-any.html>`_
describes some applications which can be used to access the %brand%
system from an iPad or iPhone.

The rest of this Guide describes all of the configuration screens
available within the %brand% graphical administrative interface.
The screens are listed in the order that they appear within the
tree, or the left frame of the graphical interface.

.. note:: iXsystems recommends that you contact your iXsystems
   Support Representative for initial setup and configuration
   assistance.

Once the system has been configured and you are familiar with the
configuration workflow, the rest of this document can be used as a
reference guide to the features built into the %brand% Storage
Array.

.. note:: It is important to use the graphical interface (or the
   console setup menu) for all non-ZFS configuration changes.
   %brand% uses a configuration database to store its settings. If
   changes are made at the command line, they will not be written
   to the configuration database. This means that these changes
   will not persist after a reboot and will be overwritten by the
   values in the configuration database during an upgrade.
