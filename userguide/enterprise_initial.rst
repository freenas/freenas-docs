
.. _Enterprise Initial Setup:

|enterprise| Initial Setup
==========================

This chapter describes the initial steps to take after receiving a
|enterprise| Unified Storage Array. 

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
.. _Enterprise_Console Setup Menu:

|enterprise| Console Setup Menu
----------------------------------------------------

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
