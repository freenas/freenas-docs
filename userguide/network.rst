.. index:: Network Settings
.. _Network:

Network
=======

The Network section of the |web-ui| contains these
components for viewing and configuring network settings on the
%brand% system:

* :ref:`Global Configuration`: general network settings.

* :ref:`Interfaces`: settings for each network interface.

* :ref:`IPMI`: settings controlling connection to the appliance
  through the hardware side-band management interface if the
  user interface becomes unavailable.

* :ref:`Link Aggregations`: settings for network link aggregation and
  link failover.

* :ref:`Static Routes`: add static routes.

* :ref:`VLANs`: configure IEEE 802.1q tagging for virtual LANs.

Each of these is described in more detail in this section.

.. _webui_interface_warning:

.. warning:: Making changes to the network interface the |web-ui| uses
   can result in losing connection to the %brand% system! Misconfiguring
   network settings might require command line knowledge or physical
   access to the %brand% system to fix. Be very careful when configuring
   :ref:`Interfaces` and :ref:`Link Aggregations`.


.. _Global Configuration:

Global Configuration
--------------------

:menuselection:`Network --> Global Configuration`,
shown in
:numref:`Figure %s <global_net_config_fig>`,
is for general network settings that are not unique to any particular
network interface.


.. _global_net_config_fig:

#ifdef freenas
.. figure:: images/network-global-configuration.png
#endif freenas
#ifdef truenas
.. figure:: images/truenas/network-global.png
#endif truenas

   Global Network Configuration


:numref:`Table %s <global_net_config_tab>`
summarizes the settings on the Global Configuration tab.
:guilabel:`Hostname` and :guilabel:`Domain` fields are pre-filled as
shown in :numref:`Figure %s <global_net_config_fig>`,
but can be changed to meet requirements of the local network.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _global_net_config_tab:

.. table:: Global Configuration Settings
   :class: longtable

   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Setting                | Value      | Description                                                                                        |
   |                        |            |                                                                                                    |
   +========================+============+====================================================================================================+
#ifdef freenas
   | Hostname               | string     | System host name. Cannot contain the underscore character.                                         |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
#endif freenas
#ifdef truenas
   | Hostname (This Node)   | string     | Host name of first storage controller.                                                             |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Hostname (Node B)      | string     | Host name of second storage controller.                                                            |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Hostname (Virtual)     | string     | Virtual host name. When using a virtualhost, this is also used as the Kerberos principal name.     |
   |                        |            | Enter the fully qualified hostname plus the domain name.                                           |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
#endif truenas
   | Domain                 | string     | System domain name.                                                                                |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Additional Domains     | string     | Additional space-delimited domains to search. Adding search domains can cause slow DNS lookups.    |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | IPv4 Default Gateway   | IP address | Typically not set. See :ref:`this note about Gateways <Gateway Note>`.                             |
   |                        |            | If set, used instead of the default gateway provided by DHCP.                                      |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | IPv6 Default Gateway   | IP address | Typically not set. See :ref:`this note about Gateways <Gateway Note>`.                             |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Nameserver 1           | IP address | Primary DNS server.                                                                                |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Nameserver 2           | IP address | Secondary DNS server.                                                                              |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Nameserver 3           | IP address | Tertiary DNS server.                                                                               |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | HTTP Proxy             | string     | Enter the proxy information for the network in the format *http://my.proxy.server:3128* or         |
   |                        |            | *http://user:password@my.proxy.server:3128*.                                                       |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Enable netwait feature | checkbox   | If enabled, network services do not start at boot until the interface is able to ping              |
   |                        |            | the addresses listed in the :guilabel:`Netwait IP list`.                                           |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Netwait IP list        | string     | Only appears when :guilabel:`Enable netwait feature` is set.                                       |
   |                        |            | Enter a space-delimited list of IP addresses to ping(8). Each address                              |
   |                        |            | is tried until one is successful or the list is exhausted. Leave empty                             |
   |                        |            | to use the default gateway.                                                                        |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+
   | Host name database     | string     | Used to add one entry per line which will be appended to :file:`/etc/hosts`. Use the format        |
   |                        |            | *IP_address space hostname* where multiple hostnames can be used if separated by a space.          |
   |                        |            |                                                                                                    |
   +------------------------+------------+----------------------------------------------------------------------------------------------------+


When using Active Directory, set the IP address of the
realm DNS server in the :guilabel:`Nameserver 1` field.

If the network does not have a DNS server, or NFS, SSH, or FTP users
are receiving "reverse DNS" or timeout errors, add an entry for the IP
address of the %brand% system in the :guilabel:`Host name database`
field.

.. _Gateway Note:

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
   sure the %brand% system is protected by a properly configured
   firewall.


.. _Interfaces:

Interfaces
----------

:menuselection:`Network --> Interfaces`
shows which interfaces are manually configured and allows adding
or editing a manually configured interface.

See this :ref:`warning <webui_interface_warning>` about changing the
interface that the |web-ui| uses.

:numref:`Figure %s <add_net_interface_fig>`
shows the screen that appears after clicking |ui-add| from the
:guilabel:`Interfaces` page.
:numref:`Table %s <net_interface_config_tab>`
summarizes the configuration options shown when adding an interface or
editing an existing interface.

.. note:: An interface can only be added when there is a NIC that has
   not already been configured. Clicking |ui-add| when there are no
   NICs available will display a message across the bottom of the screen
   that :literal:`All interfaces are already in use.`.


.. _add_net_interface_fig:

.. figure:: images/network-interfaces-add.png

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
   | NIC                 | drop-down menu | The FreeBSD device name of the interface. This is read-only when editing an interface.                    |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | Interface Name      | string         | Description of interface.                                                                                 |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | DHCP                | checkbox       | Requires static IPv4 or IPv6 configuration if unselected. Only one interface can be configured for DHCP.  |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | IPv4 Address        | IP address     | Enter a static IP address if :guilabel:`DHCP` is unset.                                                   |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | IPv4 Netmask        | drop-down menu | Enter a netmask if :guilabel:`DHCP` is unset.                                                             |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | Auto configure IPv6 | checkbox       | Only one interface can be configured for this option. If unset, manual configuration is                   |
   |                     |                | required to use IPv6.                                                                                     |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | IPv6 Address        | IPv6 address   | Must be unique on the network.                                                                            |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | IPv6 Prefix Length  | drop-down menu | Match the prefix used on the network.                                                                     |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+
   | Options             | string         | Additional parameters from                                                                                |
   |                     |                | `ifconfig(8) <https://www.freebsd.org/cgi/man.cgi?query=ifconfig>`__.                                     |
   |                     |                | Separate multiple parameters with a space. For example: *mtu 9000* increases the MTU for interfaces       |
   |                     |                | which support jumbo frames. See :ref:`this note <LAGG_MTU>` about MTU and lagg interfaces.                |
   |                     |                |                                                                                                           |
   +---------------------+----------------+-----------------------------------------------------------------------------------------------------------+


#ifdef truenas
.. note:: The ability to delete interfaces is disabled if
   :ref:`Failover` has been configured and enabled.
#endif truenas

Multiple interfaces **cannot** be members of the same subnet. See
`Multiple network interfaces on a single subnet
<https://forums.freenas.org/index.php?threads/multiple-network-interfaces-on-a-single-subnet.20204/>`__
for more information. Check the subnet mask if an error is shown when
setting the IP addresses on multiple interfaces.

Set only the IPv4 **or** IPv6 address for the new interface.


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
the system without requiring physical access to the system. IPMI is
also used to give another person remote access to the system to
assist with a configuration or troubleshooting issue. Before
configuring IPMI, ensure that the management interface is physically
connected to the network. The IPMI device may share the primary
Ethernet interface, or it may be a dedicated separate IPMI interface.

.. warning:: It is recommended to first ensure that the IPMI has been
   patched against the Remote Management Vulnerability before enabling
   IPMI. This
   `article
   <https://www.ixsystems.com/blog/how-to-fix-the-ipmi-remote-management-vulnerability/>`__
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
another person remote access to the system to assist with a
configuration or troubleshooting issue.
#endif truenas


.. note:: Some IPMI implementations require updates to work with newer
   versions of Java. See
   `PSA: Java 8 Update 131 breaks ASRock's IPMI Virtual console
   <https://forums.freenas.org/index.php?threads/psa-java-8-update-131-breaks-asrocks-ipmi-virtual-console.53911/>`__
   for more information.


IPMI is configured from
:menuselection:`Network --> IPMI`.
The IPMI configuration screen, shown in
:numref:`Figure %s <ipmi_config_fig>`,
provides a shortcut to the most basic IPMI configuration. Those
already familiar with IPMI management tools can use them instead.
:numref:`Table %s <ipmi_options_tab>`
summarizes the options available when configuring IPMI with the
%brand% |web-ui|.


.. _ipmi_config_fig:

.. figure:: images/network-ipmi.png

   IPMI Configuration


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _ipmi_options_tab:

.. table:: IPMI Options
   :class: longtable

   +----------------------+----------------+------------------------------------------------------------------------------+
   | Setting              | Value          | Description                                                                  |
   |                      |                |                                                                              |
   |                      |                |                                                                              |
   +======================+================+==============================================================================+
   | Channel              | drop-down menu | Select the channel to use.                                                   |
   |                      |                |                                                                              |
   +----------------------+----------------+------------------------------------------------------------------------------+
   | Password             | string         | Enter the password used to connect to the IPMI interface from a web browser. |
   |                      |                | The maximum length is 20 characters.                                         |
   |                      |                |                                                                              |
   +----------------------+----------------+------------------------------------------------------------------------------+
   | DHCP                 | checkbox       | If left unset, :guilabel:`IPv4 Address`, :guilabel:`IPv4 Netmask`,           |
   |                      |                | and :guilabel:`Ipv4 Default Gateway` must be set.                            |
   |                      |                |                                                                              |
   +----------------------+----------------+------------------------------------------------------------------------------+
   | IPv4 Address         | string         | IP address used to connect to the IPMI |web-ui|.                             |
   |                      |                |                                                                              |
   +----------------------+----------------+------------------------------------------------------------------------------+
   | IPv4 Netmask         | drop-down menu | Subnet mask associated with the IP address.                                  |
   |                      |                |                                                                              |
   +----------------------+----------------+------------------------------------------------------------------------------+
   | IPv4 Default Gateway | string         | Default gateway associated with the IP address.                              |
   |                      |                |                                                                              |
   +----------------------+----------------+------------------------------------------------------------------------------+
   | VLAN ID              | string         | Enter the VLAN identifier if the IPMI out-of-band management interface is    |
   |                      |                | not on the same VLAN as management networking.                               |
   |                      |                |                                                                              |
   +----------------------+----------------+------------------------------------------------------------------------------+


#ifdef freenas
After configuration, the IPMI interface is accessed using a web
browser and the IP address specified in the configuration. The
management interface prompts for a username and the configured
password. Refer to the IPMI device documentation to determine the
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

A command-line utility called :command:`ipmitool` is available to
control many features of the IPMI interface. See
`How To: Change IPMI Sensor Thresholds using ipmitool
<https://forums.freenas.org/index.php?resources/how-to-change-ipmi-sensor-thresholds-using-ipmitool.35/>`__
for some examples.


.. index:: Link Aggregation, LAGG, LACP, EtherChannel
.. _Link Aggregations:

Link Aggregations
-----------------

%brand% uses the FreeBSD
`lagg(4) <https://www.freebsd.org/cgi/man.cgi?query=lagg>`__
interface to provide link aggregation and link failover support. A
lagg interface allows combining multiple network interfaces into a
single virtual interface. This provides fault-tolerance and high-speed
multi-link throughput. The aggregation protocols supported by lagg both
determines the ports to use for outgoing traffic and if a specific port
accepts incoming traffic. The link state of the lagg interface is used
to validate whether the port is active.

Aggregation works best on switches supporting LACP, which distributes
traffic bi-directionally while responding to failure of individual
links. %brand% also supports active/passive failover between pairs of
links. The LACP and load-balance modes select the output interface using
a hash that includes the Ethernet source and destination address, VLAN
tag (if available), IP source and destination address, and flow label
(IPv6 only). The benefit can only be observed when multiple clients are
transferring files *from* the NAS. The flow entering *into* the NAS
depends on the Ethernet switch load-balance algorithm.

The lagg driver currently supports several aggregation protocols,
although only *Failover* is recommended on network switches that do
not support *LACP*:

**Failover:** the default protocol. Sends traffic only through the
active port. If the master port becomes unavailable, the next active
port is used. The first interface added is the master port. Any
interfaces added later are used as failover devices. By default,
received traffic is only accepted when received through the active
port. This constraint can be relaxed, which is useful for certain
bridged network setups, by going to
:menuselection:`System --> Tunables`
and clicking |ui-add| to add a tunable. Set the :guilabel:`Variable` to
*net.link.lagg.failover_rx_all*, the :guilabel:`Value` to a non-zero
integer, and the :guilabel:`Type` to *Sysctl*.

#ifdef truenas
.. note:: The *Failover* lagg protocol can interfere with HA (High
   Availability) systems and is disabled on those systems.
#endif truenas


**LACP:** supports the IEEE 802.3ad Link Aggregation Control Protocol
(LACP) and the Marker Protocol. LACP negotiates a set of aggregable
links with the peer into one or more link aggregated groups (LAGs). Each
LAG is composed of ports of the same speed, set to full-duplex
operation. Traffic is balanced across the ports in the LAG with the
greatest total speed. In most situations there will be a single LAG
which contains all ports. In the event of changes in physical
connectivity, link aggregation quickly converges to a new configuration.
LACP must be configured on the network switch and LACP does not support
mixing interfaces of different speeds. Only interfaces that use the same
driver, like two *igb* ports, are recommended for LACP. Using LACP for
iSCSI is not recommended as iSCSI has built-in multipath features which
are more efficient.

.. note:: When using *LACP*, verify the switch is configured for active
   LACP. Passive LACP is not supported.


**Load Balance:** balances outgoing traffic across the active ports
based on hashed protocol header information and accepts incoming traffic
from any active port. This is a static setup and does not negotiate
aggregation with the peer or exchange frames to monitor the link. The
hash includes the Ethernet source and destination address, VLAN tag (if
available), and IP source and destination address. Requires a switch
which supports IEEE 802.3ad static link aggregation.

**Round Robin:** distributes outgoing traffic using a round-robin
scheduler through all active ports and accepts incoming traffic from
any active port. This mode can cause unordered packet arrival at the
client. This has a side effect of limiting throughput as reordering
packets can be CPU intensive on the client. Requires a switch which
supports IEEE 802.3ad static link aggregation.

**None:** this protocol disables any traffic without disabling the
lagg interface itself.


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
the use of iSCSI MPIO through the creation of an iSCSI Portal with at
least two network cards on different networks. This allows an iSCSI
initiator to recognize multiple links to a target, using them for
increased bandwidth or redundancy. This
`how-to
<https://fojta.wordpress.com/2010/04/13/iscsi-and-esxi-multipathing-and-jumbo-frames/>`__
contains instructions for configuring MPIO on ESXi.

NFS does not understand MPIO. Therefore, one fast interface is needed,
since creating an iSCSI portal will not improve bandwidth when using
NFS. LACP does not work well to increase the bandwidth for
point-to-point NFS (one server and one client). LACP is a good
solution for link redundancy or for one server and many clients.


.. _Creating a Link Aggregation:

Creating a Link Aggregation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Before** creating a link aggregation, make sure that all interfaces to
use in the lagg are not manually configured in
:menuselection:`Network --> Interfaces`.
**Lagg creation fails if any of the included interfaces are manually
configured**. See this :ref:`warning <webui_interface_warning>` about
changing the interface that the |web-ui| uses.

To create a link aggregation, go to
:menuselection:`Network --> Link Aggregations`
and click |ui-add|. :numref:`Figure %s <create_lagg_fig>`
shows the configuration options.

.. _create_lagg_fig:

.. figure:: images/network-link-aggregations-add.png

   Creating a Link Aggregation


Enter a descriptive name for the :guilabel:`Lagg Interface`. Next,
select the desired :guilabel:`Lagg Protocol`. *LACP* is preferred.
Choose *Failover* when the network switch does not support LACP. Choose
interfaces from the :guilabel:`Lagg Interfaces` drop-down menu to
associate NICs with the lagg device and then click the :guilabel:`SAVE`
button to save the new aggregation.

#ifdef freenas
.. note:: If interfaces are installed but do not appear in the
   :guilabel:`Lagg Interfaces` list, check for a `FreeBSD driver
   <https://www.freebsd.org/releases/11.2R/hardware.html#ethernet>`__
   for the interface.


#endif freenas
After creating the link aggregation, go to
:menuselection:`Network --> Link Aggregations`
and click |ui-options| for the new lagg to view options to
:guilabel:`Edit Interface`, :guilabel:`Edit Members`, and
:guilabel:`Delete`.

Clicking :guilabel:`Edit Interface` for a lagg opens the configuration
screen shown in :numref:`Figure %s <lagg_edit_fig>`.
:numref:`Table %s <lagg_opts_tab>` describes the options in this screen.

.. _lagg_edit_fig:

.. figure:: images/network-link-aggregations-edit.png

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
   +=====================+================+==================================================================================+
   | NIC                 | string         | Read-only. Automatically assigned the next available numeric ID.                 |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | Interface Name      | string         | By default, this is the same as :guilabel:`NIC`. This can be changed             |
   |                     |                | to a more descriptive value.                                                     |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | DHCP                | checkbox       | Enable if the lagg device will get IP address info from DHCP server.             |
   |                     |                | The IP address of the new lagg can be set to DHCP only if no other interface     |
   |                     |                | uses DHCP.                                                                       |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | IPv4 Address        | string         | Enter a static IP address if :guilabel:`DHCP` is unset.                          |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | IPv4 Netmask        | drop-down menu | Enter a netmask if :guilabel:`DHCP` is left unset.                               |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | Auto configure IPv6 | checkbox       | Set only if a DHCP server is available to provide IPv6 address information.      |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | IPv6 Address        | string         | Optional.                                                                        |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | IPv6 Prefix Length  | drop-down menu | Required if an IPv6 address is entered.                                          |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+
   | Options             | string         | Additional                                                                       |
   |                     |                | `ifconfig(8) <https://www.freebsd.org/cgi/man.cgi?query=ifconfig>`__             |
   |                     |                | options.                                                                         |
   |                     |                |                                                                                  |
   +---------------------+----------------+----------------------------------------------------------------------------------+


There are also buttons to add and remove extra IPv4 or IPv6 aliases.

In
:menuselection:`Network --> Link Aggregations`,
click |ui-options| and :guilabel:`Edit Members` for a lagg to see the
:guilabel:`Members` screen, shown in :numref:`Figure %s <lagg_members>`.

.. _lagg_members:

.. figure:: images/network-link-aggregations-members.png

   Link Aggregation Members


Click |ui-options| for an existing lagg member to see options to
:guilabel:`Edit` and :guilabel:`Delete` it. Choose :guilabel:`Edit` to
adjust an existing member. The configurable options are summarized in
:numref:`Table %s <lagg_config_member_tab>`.

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
   | LAGG Interface Group | drop-down menu | Select the member interface to configure.                                                      |
   |                      |                |                                                                                                |
   +----------------------+----------------+------------------------------------------------------------------------------------------------+
   | LAGG Priority Number | integer        | Order of selected interface within the lagg. Configure a failover to set the master interface  |
   |                      |                | to *0* and the other interfaces to *1*, *2*, etc.                                              |
   |                      |                |                                                                                                |
   +----------------------+----------------+------------------------------------------------------------------------------------------------+
   | LAGG Physical NIC    | drop-down menu | Physical interface of the selected member. This field only appears when a NIC is available.    |
   |                      |                |                                                                                                |
   +----------------------+----------------+------------------------------------------------------------------------------------------------+
   | Options              | string         | Additional parameters from                                                                     |
   |                      |                | `ifconfig(8) <https://www.freebsd.org/cgi/man.cgi?query=ifconfig>`__.                          |
   |                      |                |                                                                                                |
   +----------------------+----------------+------------------------------------------------------------------------------------------------+


Click |ui-add| to open the screen shown in
:numref:`Figure %s <lagg_members_add>`.

.. _lagg_members_add:

.. figure:: images/network-link-aggregations-members-add.png

   Add Link Aggregation Member


The options are identical to the
:ref:`Configuring a Member Interface <lagg_config_member_tab>` table.
Click :guilabel:`SAVE` to add the member to the list in
:menuselection:`Network --> Link Aggregations --> Members`.


Link Aggregation Options
~~~~~~~~~~~~~~~~~~~~~~~~

Options are set at the lagg level from the
:menuselection:`Network --> Link Aggregations`
page. Click |ui-options| and :guilabel:`Edit Members` for an existing
lagg interface. Click |ui-options| and :guilabel:`Edit` for the existing
member. Scroll to the :guilabel:`Options` field.

To set options at the individual parent interface level, go to
:menuselection:`Network --> Interfaces`, and click |ui-options| on
the desired interface. Select :guilabel:`Edit`, and scroll to the
:guilabel:`Options` field. Changes are typically made at the lagg level
as each interface member inherits settings from the lagg. Configuring
at the interface level requires repeating the configuration for each
interface within the lagg.

.. _LAGG_MTU:

Some options can only be set on the parent interfaces and are
inherited by the lagg interface. For example, to set the MTU on a
lagg, go to
:menuselection:`Network --> Interfaces`, click |ui-options|, and then
:guilabel:`Edit` to set the MTU for each parent interface.

If the MTU settings on the lagg member interfaces are not identical,
the smallest value is used for the MTU of the entire lagg.

.. note:: A reboot is required after changing the MTU to create a
   jumbo frame lagg.


Link aggregation load balancing can be tested with:

.. code-block:: none

   systat -ifstat


More information about this command can be found at
`systat(1) <https://www.freebsd.org/cgi/man.cgi?query=systat>`__.


.. _Network Summary:

Network Summary
---------------

:menuselection:`Network --> Network Summary`
shows a quick summary of the addressing information of every
configured interface. For each interface name, the configured IPv4 and
IPv6 addresses, DNS servers, and default gateway are displayed. It
also displays nameservers.


.. index:: Route, Static Route
.. _Static Routes:

Static Routes
-------------

No static routes are defined on a default %brand% system. If a static
route is required to reach portions of the network, add the route by
going to :menuselection:`Network --> Static Routes`, and clicking
|ui-add|. This is shown in :numref:`Figure %s <add_static_route_fig>`.


.. _add_static_route_fig:

.. figure:: images/network-static-routes-add.png

   Adding a Static Route


The available options are summarized in
:numref:`Table %s <static_route_opts_tab>`.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _static_route_opts_tab:

.. table:: Static Route Options
   :class: longtable

   +-------------+-----------+--------------------------------------+
   | Setting     | Value     | Description                          |
   |             |           |                                      |
   |             |           |                                      |
   +=============+===========+======================================+
   | Destination | integer   | Use the format *A.B.C.D/E* where     |
   |             |           | *E* is the CIDR mask.                |
   |             |           |                                      |
   +-------------+-----------+--------------------------------------+
   | Gateway     | integer   | Enter the IP address of the gateway. |
   |             |           |                                      |
   +-------------+-----------+--------------------------------------+
   | Description | string    | Optional. Add any notes about the    |
   |             |           | route.                               |
   |             |           |                                      |
   +-------------+-----------+--------------------------------------+


Added static routes are shown in
:menuselection:`Network --> Static Routes`. Click |ui-options| on
a route entry to access the :guilabel:`Edit` and :guilabel:`Delete`
buttons.


.. index:: VLAN, Trunking, 802.1Q
.. _VLANs:

VLANs
-----

%brand% uses FreeBSD's
`vlan(4) <https://www.freebsd.org/cgi/man.cgi?query=vlan>`__
interface to demultiplex frames with IEEE 802.1q tags. This allows
nodes on different VLANs to communicate through a layer 3 switch or
router. A vlan interface must be assigned a parent interface and a
numeric VLAN tag. A single parent can be assigned to multiple vlan
interfaces provided they have different tags.

#ifdef freenas
.. note:: VLAN tagging is the only 802.1q feature that is implemented.
   Additionally, not all Ethernet interfaces support full VLAN
   processing.  See the HARDWARE section of
   `vlan(4) <https://www.freebsd.org/cgi/man.cgi?query=vlan>`__
   for details.
#endif freenas

#ifdef truenas
.. note:: VLAN tagging is the only 802.1q feature that is implemented.
#endif truenas

Go to
:menuselection:`Network --> VLANs` and click |ui-add|
to see the screen shown in
:numref:`Figure %s <adding_vlan_fig>`.


.. _adding_vlan_fig:

.. figure:: images/network-vlans-add.png

   Adding a VLAN


:numref:`Table %s <adding_vlan_tab>`
summarizes the configurable fields.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _adding_vlan_tab:

.. table:: Adding a VLAN
   :class: longtable

   +---------------------+----------------+---------------------------------------------------------------------------------------------------+
   | Setting             | Value          | Description                                                                                       |
   |                     |                |                                                                                                   |
   +=====================+================+===================================================================================================+
   | Virtual Interface   | string         | Use the format *vlanX* where *X* is a number representing a VLAN interface not                    |
   |                     |                | currently being used as a parent.                                                                 |
   |                     |                |                                                                                                   |
   +---------------------+----------------+---------------------------------------------------------------------------------------------------+
   | Parent Interface    | drop-down menu | Usually an Ethernet card connected to a properly configured switch port. Newly created            |
   |                     |                | :ref:`Link Aggregations` do not appear in the drop-down until the system is rebooted.             |
   |                     |                |                                                                                                   |
   +---------------------+----------------+---------------------------------------------------------------------------------------------------+
   | Vlan Tag            | integer        | Enter a number between *1* and *4095* which matches a numeric tag set up in the switched network. |
   |                     |                |                                                                                                   |
   +---------------------+----------------+---------------------------------------------------------------------------------------------------+
   | Description         | string         | Optional. Enter any notes about this VLAN.                                                        |
   |                     |                |                                                                                                   |
   +---------------------+----------------+---------------------------------------------------------------------------------------------------+
   | Priority Code Point | drop-down menu | Available 802.1p Class of Service ranges from *Best Effort (default)* to                          |
   |                     |                | *Network Control (highest)*.                                                                      |
   |                     |                |                                                                                                   |
   +---------------------+----------------+---------------------------------------------------------------------------------------------------+


The parent interface of a VLAN must be up, but it can either have an IP
address or be unconfigured, depending upon the requirements of the VLAN
configuration. This makes it difficult for the |web-ui| to do the right thing
without trampling the configuration. To remedy this, add the VLAN, then
select
:menuselection:`Network --> Interfaces`, and click |ui-add|.
Choose the parent interface from the :guilabel:`NIC` drop-down menu
and in the :guilabel:`Options` field, type :command:`up`. This
brings up the parent interface. If an IP address is required,
configure it using the rest of the options in the
|ui-add| screen.

#ifdef freenas
.. warning:: Creating a VLAN causes an interruption to network
   connectivity. The |web-ui| provides a warning about this interruption.
#endif freenas
#ifdef truenas
.. warning:: Creating a vlan will cause network connectivity to be
   interrupted and, if :ref:`Failover` is configured, a
   failover event. Accordingly, the |web-ui| will provide a warning
   and an opportunity to cancel the vlan creation.
#endif truenas
