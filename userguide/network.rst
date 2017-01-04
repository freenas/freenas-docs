.. index:: Network Settings
.. _Network:

Network
=======

The Network section of the administrative GUI contains these
components for viewing and configuring network settings on the
%brand% system:

* :ref:`Global Configuration`: general network settings.

* :ref:`Interfaces`: settings for each network interface.

* :ref:`IPMI`: settings controlling connection to the appliance
  through the hardware side-band management interface if the graphical
  user interface becomes unavailable.

* :ref:`Link Aggregations`: settings for network link aggregation and
  link failover.

* :ref:`Network Summary`: display an overview of the current network
  settings.

* :ref:`Static Routes`: add static routes.

* :ref:`VLANs`: configure IEEE 802.1q tagging for virtual LANs.

Each of these is described in more detail in this section.


.. _Global Configuration:

Global Configuration
--------------------

:menuselection:`Network --> Global Configuration`,
shown in
:numref:`Figure %s <global_net_config_fig>`,
is for general network settings that are not unique to any particular
network interface.


.. _global_net_config_fig:

.. figure:: images/network1.png

   Global Network Configuration


:numref:`Table %s <global_net_config_tab>`
summarizes the settings on the Global Configuration tab.
Hostname and domain fields are pre-filled as shown in
:numref:`Figure %s <global_net_config_fig>`,
but can be changed to meet requirements of the local network.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _global_net_config_tab:

.. table:: Global Configuration Settings
   :class: longtable

   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | Setting                | Value      | Description                                                                                                          |
   |                        |            |                                                                                                                      |
   +========================+============+======================================================================================================================+
   | Hostname               | string     | system host name                                                                                                     |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | Domain                 | string     | system domain name                                                                                                   |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | IPv4 Default Gateway   | IP address | typically not set (see NOTE below)                                                                                   |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | IPv6 Default Gateway   | IP address | typically not set (see NOTE below)                                                                                   |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | Nameserver 1           | IP address | primary DNS server (typically in Windows domain)                                                                     |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | Nameserver 2           | IP address | secondary DNS server                                                                                                 |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | Nameserver 3           | IP address | tertiary DNS server                                                                                                  |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | HTTP Proxy             | string     | enter the proxy information for the network in the format *http://my.proxy.server:3128* or                           |
   |                        |            | *http://user@password:my.proxy.server:3128*                                                                          |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | Enable netwait feature | checkbox   | if enabled, network services are not started at boot until the interface is able to ping the addresses               |
   |                        |            | listed in :guilabel:`Netwait IP list`                                                                                |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | Netwait IP list        | string     | if :guilabel:`Enable netwait feature` is checked, list of IP addresses to ping; otherwise, ping the                  |
   |                        |            | default gateway                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+
   | Host name database     | string     | used to add one entry per line which will be appended to :file:`/etc/hosts`; use the format                          |
   |                        |            | *IP_address space hostname* where multiple hostnames can be used if separated by a space                             |
   |                        |            |                                                                                                                      |
   +------------------------+------------+----------------------------------------------------------------------------------------------------------------------+


When Active Directory is being used, set the IP address of the
realm's DNS server in the :guilabel:`Nameserver 1` field.

If the network does not have a DNS server, or NFS, SSH, or FTP users
are receiving "reverse DNS" or timeout errors, add an entry for the IP
address of the %brand% system in the :guilabel:`Host name database`
field.

.. note:: In many cases, a %brand% configuration does not include
   default gateway information as a way to make it more difficult for
   a remote attacker to communicate with the server. While this is a
   reasonable precaution, such a configuration does **not** restrict
   inbound traffic from sources within the local network. However,
   omitting a default gateway will prevent the %brand% system from
   communicating with DNS servers, time servers, and mail servers that
   are located outside of the local network. In this case, it is
   recommended to add :ref:`Static Routes` to be able to reach
   external DNS, NTP, and mail servers which are configured with
   static IP addresses. When a gateway to the Internet is added, make
   sure that the %brand% system is protected by a properly configured
   firewall.


.. _Interfaces:

Interfaces
----------

:menuselection:`Network --> Interfaces`
shows which interfaces have been manually configured and allows adding
or editing a manually configured interface.

.. note:: Typically, the interface used to access the %brand%
   administrative GUI is configured by DHCP. This interface does not
   appear in this screen, even though it is already dynamically
   configured and in use.

:numref:`Figure %s <add_net_interface_fig>`
shows the screen that opens on clicking
:menuselection:`Interfaces --> Add Interface`.
:numref:`Table %s <net_interface_config_tab>`
summarizes the configuration options shown when adding an interface or
editing an already configured interface. Note that if any changes to
this screen require a network restart, the screen will turn red when
the :guilabel:`OK` button is clicked and a pop-up message will point
out that network connectivity to the %brand% system will be
interrupted while the changes are applied.


.. _add_net_interface_fig:

.. figure:: images/interface.png

   Adding or Editing an Interface


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _net_interface_config_tab:

.. table:: Interface Configuration Settings
   :class: longtable

   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | Setting             | Value          | Description                                                                                               |
   |                     |                |                                                                                                           |
   +=====================+================+===========================================================================================================+
   | NIC                 | drop-down menu | the FreeBSD device name of the interface; a read-only field when editing an interface                     |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | Interface Name      | string         | description of interface                                                                                  |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | DHCP                | checkbox       | requires static IPv4 or IPv6 configuration if unchecked; only one interface can be configured for DHCP    |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | IPv4 Address        | IP address     | enter a static IP address if :guilabel:`DHCP` is unchecked                                                |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | IPv4 Netmask        | drop-down menu | enter a netmask if :guilabel:`DHCP` is unchecked                                                          |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | Auto configure IPv6 | checkbox       | only one interface can be configured for this option; if unchecked, manual configuration is               |
   |                     |                | required to use IPv6                                                                                      |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | IPv6 Address        | IPv6 address   | must be unique on network                                                                                 |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | IPv6 Prefix Length  | drop-down menu | match the prefix used on network                                                                          |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | Options             | string         | additional parameters from                                                                                |
   |                     |                | `ifconfig(8) <http://www.freebsd.org/cgi/man.cgi?query=ifconfig>`_,                                       |
   |                     |                | separate multiple parameters with a space; for example: *mtu 9000* increases the MTU for interfaces       |
   |                     |                | which support jumbo frames                                                                                |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+


This screen also provides for the configuration of IP aliases, making
it possible for a single interface to have multiple IP addresses. To
set multiple aliases, click the :guilabel:`Add extra alias` link for
each alias. Aliases are deleted by clicking the interface in the tree,
clicking the :guilabel:`Edit` button, checking the :guilabel:`Delete`
checkbox below the alias, then clicking the :guilabel:`OK` button.

.. warning:: Aliases are deleted by checking the :guilabel:`Delete`
   checkbox in the alias area, then clicking :guilabel:`OK` for the
   interface. **Do not** click the :guilabel:`Delete` button at the
   bottom of this screen, which deletes the entire interface.

#ifdef truenas
.. note:: The ability to delete interfaces is disabled if
   :ref:`Failover` has been configured and enabled.
#endif truenas

Multiple interfaces **cannot** be members of the same subnet. Check
the subnet mask if an error is shown when setting the IP addresses on
multiple interfaces.

This screen will not allow an interface's IPv4 and IPv6 addresses
to both be set as primary addresses.  An error is shown if both the
:guilabel:`IPv4 address` and :guilabel:`IPv6 address` fields are
filled in. Instead, set only one of these address fields and create an
alias for the other address.


.. _IPMI:

IPMI
----

#ifdef freenas
Beginning with version 9.2.1, %brand% provides a graphical screen for
configuring an IPMI interface. This screen will only appear if the
system hardware includes a Baseboard Management Controller (BMC).

IPMI provides side-band management if the graphical administrative
interface becomes unresponsive. This allows for a few vital functions,
such as checking the log, accessing the BIOS setup, and powering on
the system without requiring physical access to the system. IPMI can
also be used to allow another person remote access to the system to
assist with a configuration or troubleshooting issue. Before
configuring IPMI, ensure that the management interface is physically
connected to the network. The IPMI device may share the primary
Ethernet interface, or it may be a dedicated separate IPMI interface.

.. warning:: It is recommended to first ensure that the IPMI has been
   patched against the Remote Management Vulnerability before enabling
   IPMI. This
   `article
   <http://www.ixsystems.com/whats-new/how-to-fix-the-ipmi-remote-management-vulnerability/>`_
   provides more information about the vulnerability and how to fix
   it.
#endif freenas
#ifdef truenas
The %brand% Storage Array provides a built-in out-of-band management
port which can be used to provide side-band management should the
system become unavailable through the graphical administrative
interface. This allows for a few vital functions, such as checking the
log, accessing the BIOS setup, and powering on the system without
requiring physical access to the system. It can also be used to allow
another person remote access to the system in order to assist with a
configuration or troubleshooting issue.
#endif truenas

IPMI is configured from
:menuselection:`Network --> IPMI`.
The IPMI configuration screen, shown in
:numref:`Figure %s <ipmi_config_fig>`,
provides a shortcut to the most basic IPMI configuration. Those
already familiar with IPMI management tools can use them instead.
:numref:`Table %s <ipmi_options_tab>`
summarizes the options available when configuring IPMI with the
%brand% GUI.


.. _ipmi_config_fig:

.. figure:: images/ipmi1.png

   IPMI Configuration


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _ipmi_options_tab:

.. table:: IPMI Options
   :class: longtable

   +----------------------+----------------+-----------------------------------------------------------------------------+
   | Setting              | Value          | Description                                                                 |
   |                      |                |                                                                             |
   |                      |                |                                                                             |
   +======================+================+=============================================================================+
   | Channel              | drop-down menu | select the channel to use                                                   |
   |                      |                |                                                                             |
   +----------------------+----------------+-----------------------------------------------------------------------------+
   | Password             | string         | enter the password used to connect to the IPMI interface from a web browser |
   |                      |                |                                                                             |
   +----------------------+----------------+-----------------------------------------------------------------------------+
   | DHCP                 | checkbox       | if left unchecked, the following three fields must be set                   |
   |                      |                |                                                                             |
   +----------------------+----------------+-----------------------------------------------------------------------------+
   | IPv4 Address         | string         | IP address used to connect to the IPMI web GUI                              |
   |                      |                |                                                                             |
   +----------------------+----------------+-----------------------------------------------------------------------------+
   | IPv4 Netmask         | drop-down menu | subnet mask associated with the IP address                                  |
   |                      |                |                                                                             |
   +----------------------+----------------+-----------------------------------------------------------------------------+
   | IPv4 Default Gateway | string         | default gateway associated with the IP address                              |
   |                      |                |                                                                             |
   +----------------------+----------------+-----------------------------------------------------------------------------+
   | VLAN ID              | string         | enter the VLAN identifier if the IPMI out-of-band management interface is   |
   |                      |                | not on the same VLAN as management networking                               |
   |                      |                |                                                                             |
   +----------------------+----------------+-----------------------------------------------------------------------------+


#ifdef freenas
After configuration, the IPMI interface is accessed using a web
browser and the IP address specified in the configuration. The
management interface prompts for a username and the configured
password. Refer to the IPMI device's documentation to determine the
default administrative username.

After logging in to the management interface, the default
administrative username can be changed, and additional users created.
The appearance of the IPMI utility and the functions that are
available vary depending on the hardware.
#endif freenas
#ifdef truenas
After configuration, the IPMI interface is accessed using a web
browser and the IP address specified in the configuration. The
management interface prompts for a username (the default is *admin*)
and the configured password.

After logging in to the management interface, the administrative
username can be changed and additional users can be created.

Refer to
:numref:`Figure %s <tn_IPMIdownload>`
through
:numref:`Figure %s <tn_IPMIcontinue>`
in
:ref:`Out-of-Band Management` for additional instructions on how to
configure the Java KVM Client used by the IPMI management interface.
#endif truenas


.. index:: Link Aggregation, LAGG, LACP, EtherChannel
.. _Link Aggregations:

Link Aggregations
-----------------

%brand% uses FreeBSD's
`lagg(4) <http://www.freebsd.org/cgi/man.cgi?query=lagg>`_
interface to provide link aggregation and link failover. The lagg
interface allows aggregation of multiple network interfaces into a
single virtual lagg interface, providing fault-tolerance and
high-speed multi-link throughput. The aggregation protocols supported
by lagg determine which ports are used for outgoing traffic and
whether a specific port accepts incoming traffic. The link state of
the lagg interface is used to validate whether the port is active.

Aggregation works best on switches supporting LACP, which distributes
traffic bi-directionally while responding to failure of individual
links. %brand% also supports active/passive failover between pairs of
links. The LACP, FEC, and load-balance modes select the output
interface using a hash that includes the Ethernet source and
destination address, VLAN tag (if available), IP source and
destination address, and flow label (IPv6 only). The benefit can only
be observed when multiple clients are transferring files *from* the
NAS. The flow entering *into* the NAS depends on the Ethernet
switch load-balance algorithm.

The lagg driver currently supports several aggregation protocols,
although only *Failover* is recommended on network switches that do
not support LACP:

**Failover:** the default protocol. Sends traffic only through the
active port. If the master port becomes unavailable, the next active
port is used. The first interface added is the master port; any
interfaces added after that are used as failover devices. By default,
received traffic is only accepted when received through the active
port. This constraint can be relaxed, which is useful for certain
bridged network setups, by creating a a tunable with a
:guilabel:`Variable` of *net.link.lagg.failover_rx_all*, a
:guilabel:`Value` of a non-zero integer, and a :guilabel:`Type` of
*Sysctl* in
:menuselection:`System --> Tunables --> Add Tunable`.

**FEC:** supports Cisco EtherChannel on older Cisco switches. This is
a static setup and does not negotiate aggregation with the peer or
exchange frames to monitor the link.

**LACP:** supports the IEEE 802.3ad Link Aggregation Control Protocol
(LACP) and the Marker Protocol. LACP negotiates a set of
aggregable links with the peer into one or more link aggregated groups
(LAGs). Each LAG is composed of ports of the same speed, set to
full-duplex operation. Traffic is balanced across the ports
in the LAG with the greatest total speed; in most cases there will
only be one LAG which contains all ports. In the event of changes in
physical connectivity, link aggregation will quickly converge to a new
configuration. LACP must be configured on the switch, and LACP does
not support mixing interfaces of different speeds. Only interfaces
that use the same driver, like two *igb* ports, are recommended for
LACP. Using LACP for iSCSI is not recommended, as iSCSI has built-in
multipath features which are more efficient.

**Load Balance:** balances outgoing traffic across the active ports
based on hashed protocol header information and accepts incoming
traffic from any active port. This is a static setup and does not
negotiate aggregation with the peer or exchange frames to monitor the
link. The hash includes the Ethernet source and destination address,
VLAN tag (if available), and IP source and destination address.
Requires a switch which supports IEEE 802.3ad static link aggregation.

**Round Robin:** distributes outgoing traffic using a round-robin
scheduler through all active ports and accepts incoming traffic from
any active port. This mode can cause unordered packet arrival at the
client. This has a side effect of limiting throughput as reordering
packets can be CPU intensive on the client. Requires a switch which
supports IEEE 802.3ad static link aggregation.

**None:** this protocol disables any traffic without disabling the
lagg interface itself.

.. note:: When using LACP, verify that the switch is configured for
   active LACP, as passive LACP is not supported.


.. _LACP, MPIO, NFS, and ESXi:

LACP, MPIO, NFS, and ESXi
~~~~~~~~~~~~~~~~~~~~~~~~~

LACP bonds Ethernet connections to improve bandwidth. For example,
four physical interfaces can be used to create one mega interface.
However, it cannot increase the bandwidth for a single conversation.
It is designed to increase bandwidth when multiple clients are
simultaneously accessing the same system. It also assumes that quality
Ethernet hardware is used and it will not make much difference when
using inferior Ethernet chipsets such as a Realtek.

LACP reads the sender and receiver IP addresses and, if they are
deemed to belong to the same TCP connection, always sends the packet
over the same interface to ensure that TCP does not need to reorder
packets. This makes LACP ideal for load balancing many simultaneous
TCP connections, but does nothing for increasing the speed over one
TCP connection.

MPIO operates at the iSCSI protocol level. For example, if four IP
addresses are created and there are four simultaneous TCP connections,
MPIO will send the data over all available links. When configuring
MPIO, make sure that the IP addresses on the interfaces are configured
to be on separate subnets with non-overlapping netmasks, or configure
static routes to do point-to-point communication. Otherwise, all
packets will pass through one interface.

LACP and other forms of link aggregation generally do not work well
with virtualization solutions. In a virtualized environment, consider
the use of iSCSI MPIO through the creation of an iSCSI Portal. This
allows an iSCSI initiator to recognize multiple links to a target,
utilizing them for increased bandwidth or redundancy. This
`how-to
<https://fojta.wordpress.com/2010/04/13/iscsi-and-esxi-multipathing-and-jumbo-frames/>`_
contains instructions for configuring MPIO on ESXi.

NFS does not understand MPIO. Therefore, one fast interface is needed,
since creating an iSCSI portal will not improve bandwidth when using
NFS. LACP does not work well to increase the bandwidth for
point-to-point NFS (one server and one client). LACP is a good
solution for link redundancy or for one server and many clients.


.. _Creating a Link Aggregation:

Creating a Link Aggregation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Before** creating a link aggregation, double-check that no
interfaces have been manually configured in
:menuselection:`Network --> Interfaces --> View Interfaces`.

If any manually-configured interfaces exist, delete them as
**lagg creation fails if any interfaces are manually configured**.

.. note:: Creating or editing link aggregations can disconnect clients
   using the %brand% computer. Please verify that clients have saved
   their work and are not connected through the affected networks
   before making changes.

:numref:`Figure %s <create_lagg_fig>`
shows the configuration options when adding a lagg interface using
:menuselection:`Network --> Link Aggregations
--> Create Link Aggregation`.


.. _create_lagg_fig:

.. figure:: images/lagg1.png

   Creating a lagg Interface


#ifdef freenas
.. note:: If interfaces are installed but do not appear in the
   :guilabel:`Physical NICs` list, check that a FreeBSD driver for the
   interface exists
   `here
   <http://www.freebsd.org/releases/10.3R/hardware.html#ETHERNET>`_.
#endif freenas

To create a link aggregation, select the desired
:guilabel:`Protocol Type`, highlight the interfaces to associate with
the lagg device, and click the :guilabel:`OK` button.

Once the lagg device has been created, click its entry to enable its
:guilabel:`Edit`, :guilabel:`Delete`, and :guilabel:`Edit Members`
buttons.

Clicking the :guilabel:`Edit` button for a lagg opens the
configuration screen shown in
:numref:`Figure %s <lagg_edit_fig>`.
:numref:`Table %s <lagg_opts_tab>`
describes the options in this screen.

If the network interface used to connect to the %brand% web GUI is a
member of the lagg, the network connection will be lost when the new
lagg is created. The switch settings might also require changes to
communicate through the new lagg interface.

The IP address of the new lagg can be set with DHCP or manually from
the console setup menu. If the IP address is set manually, it might
also be necessary to enter a default gateway to allow access to the
GUI from the new lagg interface.


.. _lagg_edit_fig:

.. figure:: images/lagg2.png

   Editing a lagg


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _lagg_opts_tab:

.. table:: Configurable Options for a lagg
   :class: longtable

   +---------------------+----------------+----------------------------------------------------------------------------------+
   | Setting             | Value          | Description                                                                      |
   |                     |                |                                                                                  |
   |                     |                |                                                                                  |
   +=====================+================+==================================================================================+
   | NIC                 | string         | read-only; automatically assigned the next available numeric ID                  |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | Interface Name      | string         | by default same as device (NIC) name, can be changed to a more descriptive value |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | DHCP                | checkbox       | check if the lagg device will get IP address info from DHCP server               |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | IPv4 Address        | string         | enter a static IP address if :guilabel:`DHCP` is left unchecked                  |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | IPv4 Netmask        | drop-down menu | enter a netmask if :guilabel:`DHCP` is left unchecked                            |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | Auto configure IPv6 | checkbox       | check only if DHCP server available to provide IPv6 address info                 |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | IPv6 Address        | string         | optional                                                                         |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | IPv6 Prefix Length  | drop-down menu | required if an IPv6 address is entered                                           |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | Options             | string         | additional                                                                       |
   |                     |                | `ifconfig(8) <http://www.freebsd.org/cgi/man.cgi?query=ifconfig>`_               |
   |                     |                | options                                                                          |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+


This screen also allows the configuration of an alias for the lagg
interface. Multiple aliases can be added with the
:guilabel:`Add extra Alias` link.


Click the :guilabel:`Edit Members` button, click the entry for a
member, then click its :guilabel:`Edit` button to see the
configuration screen shown in
:numref:`Figure %s <lagg_member_edit_fig>`.
The configurable options are summarized in
:numref:`Table %s <lagg_config_member_tab>`.


.. _lagg_member_edit_fig:

.. figure:: images/lagg3.png

   Editing a Member Interface


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _lagg_config_member_tab:

.. table:: Configuring a Member Interface
   :class: longtable

   +----------------------+----------------+------------------------------------------------------------------------------------------------+
   | Setting              | Value          | Description                                                                                    |
   |                      |                |                                                                                                |
   |                      |                |                                                                                                |
   +======================+================+================================================================================================+
   | LAGG Interface group | drop-down menu | select the member interface to configure                                                       |
   |                      |                |                                                                                                |
   +----------------------+----------------+------------------------------------------------------------------------------------------------+
   | LAGG Priority Number | integer        | order of selected interface within the lagg; configure a failover to set the master interface  |
   |                      |                | to *0* and the other interfaces to                                                             |
   |                      |                | *1*,                                                                                           |
   |                      |                | *2*, etc.                                                                                      |
   |                      |                |                                                                                                |
   +----------------------+----------------+------------------------------------------------------------------------------------------------+
   | LAGG Physical NIC    | drop-down menu | physical interface of the selected member                                                      |
   |                      |                |                                                                                                |
   +----------------------+----------------+------------------------------------------------------------------------------------------------+
   | Options              | string         | additional parameters from                                                                     |
   |                      |                | `ifconfig(8) <http://www.freebsd.org/cgi/man.cgi?query=ifconfig>`_                             |
   |                      |                |                                                                                                |
   +----------------------+----------------+------------------------------------------------------------------------------------------------+


Options can be set at the lagg level using the :guilabel:`Edit`
button, or at the individual parent interface level using the
:guilabel:`Edit Members` button. Changes are typically made at the
lagg level
(:numref:`Figure %s <lagg_edit_fig>`)
as each interface member will inherit from the lagg. To configure at
the interface level
(:numref:`Figure %s <lagg_member_edit_fig>`)
instead, the configuration must be repeated for each interface within
the lagg. Some options can only be set on the parent interfaces and
are inherited by the lagg interface. For example, to set the MTU on a
lagg, use :guilabel:`Edit Members` to set the MTU for each parent
interface.

.. note:: A reboot is required after changing the MTU to create a
   jumbo frame lagg.

To see if the link aggregation is properly load balancing, run this
command from :ref:`Shell`:

.. code-block:: none

 systat -ifstat


More information about this command can be found at
`systat(1) <http://www.freebsd.org/cgi/man.cgi?query=systat>`_.


.. _Network Summary:

Network Summary
---------------

:menuselection:`Network --> Network Summary`
shows a quick summary of the addressing information of every
configured interface. For each interface name, the configured IPv4 and
IPv6 addresses, DNS servers, and default gateway are displayed.


.. index:: Route, Static Route
.. _Static Routes:

Static Routes
-------------

No static routes are defined on a default %brand% system. If a static
route is required to reach portions of the network, add the route with
:menuselection:`Network --> Static Routes --> Add Static Route`,
shown in
:numref:`Figure %s <add_static_route_fig>`.


.. _add_static_route_fig:

.. figure:: images/static.png

   Adding a Static Route


The available options are summarized in
:numref:`Table %s <static_route_opts_tab>`.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _static_route_opts_tab:

.. table:: Static Route Options
   :class: longtable

   +---------------------+-----------+-------------------------------------+
   | Setting             | Value     | Description                         |
   |                     |           |                                     |
   |                     |           |                                     |
   +=====================+===========+=====================================+
   | Destination network | integer   | use the format *A.B.C.D/E* where    |
   |                     |           | *E* is the CIDR mask                |
   |                     |           |                                     |
   +---------------------+-----------+-------------------------------------+
   | Gateway             | integer   | enter the IP address of the gateway |
   |                     |           |                                     |
   +---------------------+-----------+-------------------------------------+
   | Description         | string    | optional                            |
   |                     |           |                                     |
   +---------------------+-----------+-------------------------------------+


Added static routes are shown in :guilabel:`View Static Routes`. Click
a route's entry to access the :guilabel:`Edit` and :guilabel:`Delete`
buttons.


.. index:: VLAN, Trunking, 802.1Q
.. _VLANs:

VLANs
-----

%brand% uses FreeBSD's
`vlan(4) <http://www.freebsd.org/cgi/man.cgi?query=vlan>`_
interface to demultiplex frames with IEEE 802.1q tags. This allows
nodes on different VLANs to communicate through a layer 3 switch or
router. A vlan interface must be assigned a parent interface and a
numeric VLAN tag. A single parent can be assigned to multiple vlan
interfaces provided they have different tags.

#ifdef freenas
.. note:: VLAN tagging is the only 802.1q feature that is implemented.
   Additionally, not all Ethernet interfaces support full VLAN
   processing.  See the HARDWARE section of
   `vlan(4) <http://www.freebsd.org/cgi/man.cgi?query=vlan>`_
   for details.
#endif freenas

#ifdef truenas
.. note:: VLAN tagging is the only 802.1q feature that is implemented.
#endif truenas

Click
:menuselection:`Network --> VLANs --> Add VLAN`,
to see the screen shown in
:numref:`Figure %s <adding_vlan_fig>`.


.. _adding_vlan_fig:

.. figure:: images/vlan.png

   Adding a VLAN


:numref:`Table %s <adding_vlan_tab>`
summarizes the configurable fields.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _adding_vlan_tab:

.. table:: Adding a VLAN
   :class: longtable

   +-------------------+----------------+---------------------------------------------------------------------------------------------------+
   | Setting           | Value          | Description                                                                                       |
   |                   |                |                                                                                                   |
   +===================+================+===================================================================================================+
   | Virtual Interface | string         | use the format *vlanX* where                                                                      |
   |                   |                | *X* is a number representing a vlan interface not currently being used as a parent                |
   |                   |                |                                                                                                   |
   +-------------------+----------------+---------------------------------------------------------------------------------------------------+
   | Parent Interface  | drop-down menu | usually an Ethernet card connected to a properly configured switch port; note that newly created  |
   |                   |                | :ref:`Link Aggregations` will not appear in the drop-down until the system is rebooted            |
   |                   |                |                                                                                                   |
   +-------------------+----------------+---------------------------------------------------------------------------------------------------+
   | VLAN Tag          | integer        | number between 1 and 4095 which matches a numeric tag set up in the switched network              |
   |                   |                |                                                                                                   |
   +-------------------+----------------+---------------------------------------------------------------------------------------------------+
   | Description       | string         | optional                                                                                          |
   |                   |                |                                                                                                   |
   +-------------------+----------------+---------------------------------------------------------------------------------------------------+


The parent interface of a VLAN must be up, but it can have an IP
address or it can be unconfigured, depending upon the requirements of
the VLAN configuration. This makes it difficult for the GUI to do the
right thing without trampling the configuration. To remedy this, after
adding the VLAN, go to
:menuselection:`Network --> Interfaces --> Add Interface`.
Select the parent interface from the :guilabel:`NIC` drop-down menu
and in the :guilabel:`Options` field, type :command:`up`. This will
bring up the parent interface. If an IP address is required, it can be
configured using the rest of the options in the
:guilabel:`Add Interface` screen.

#ifdef freenas
.. warning:: Creating a vlan will cause network connectivity to be
   interrupted.  Accordingly, the GUI will provide a warning and an
   opportunity to cancel the vlan creation.
#endif freenas
#ifdef truenas
.. warning:: Creating a vlan will cause network connectivity to be
   interrupted and, if :ref:`Failover` has been configured, a
   failover event. Accordingly, the GUI will provide a warning
   and an opportunity to cancel the vlan creation.
#endif truenas
