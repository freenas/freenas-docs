a
%brand% is © 2011-|copyright-year| iXsystems

%brand% and %brand% logos are registered trademarks of iXsystems

FreeBSD\ :sup:`®` is a registered trademark of the FreeBSD Foundation

Written by users of the %brand% network-attached storage operating
system.

Version |release|

Copyright © 2011-|copyright-year|
`iXsystems <https://www.ixsystems.com/>`__


.. raw:: latex

   \par--TABLEOFCONTENTS--\par
   \pagestyle{frontmatter}
   \section*{Welcome}\addcontentsline{toc}{section}{Welcome}


This Guide covers the installation and use of %brand% |release|.

The %brand% User Guide is a work in progress and relies on the
contributions of many individuals. If you are interested in helping us
to improve the Guide, read the instructions in the `README
<https://github.com/freenas/freenas-docs/blob/master/README.md>`__.

The %brand% User Guide is freely available for sharing and
redistribution under the terms of the
`Creative Commons Attribution
License <https://creativecommons.org/licenses/by/3.0/>`__.
This means that you have permission to copy, distribute, translate,
and adapt the work as long as you attribute iXsystems as the original
source of the Guide.


#include snippets/trademarks.rst


.. raw:: latex

   \pagebreak
   \section*{Typographic Conventions}
   \addcontentsline{toc}{section}{Typographic Conventions}


**Typographic Conventions**

The %brand% |release| User Guide uses these typographic conventions:


#include snippets/typography.rst


.. raw:: latex

   \pagestyle{frontmatter}


.. _Introduction:

Introduction
============

.. raw:: latex

   \pagestyle{normal}

%brand% is an embedded open source network-attached storage (NAS)
operating system based on FreeBSD and released under a
`2-clause BSD license
<https://opensource.org/licenses/BSD-2-Clause>`__.
A NAS has an operating system optimized for file storage and sharing.

%brand% provides a browser-based, graphical configuration interface.
The built-in networking protocols provide storage access to multiple
operating systems. A plugin system is provided for extending the
built-in features by installing additional software.

This guide also provides information about configuring and managing a
|enterprise| Unified Storage Array. Your iXsystems support engineer will
assist with the initial setup and configuration of the array. After
becoming familiar with the configuration workflow, this document can
be used as a reference guide to the many features provided by %brand%.

.. _Contacting iXsystems:

#include snippets/contact.rst


.. _New Features in |release|:

New Features in |release|
-------------------------

%brand%  |release| is a feature release, which includes new
significant features, many improvements and bug fixes to existing
features, and version updates to the operating system, base
applications, and drivers. Users are encouraged to :ref:`Update` to
this release in order to take advantage of these improvements and bug
fixes.

**Major New Features and Improvements**

* ZFS asynchronous Copy-on-Write (CoW) support has been added.

* Native ZFS encryption has been added for new data pools.

* ZFS quota support has been expanded to include user and group quotas.

* Support for the Key Management Interoperability Protocol (KMIP) has
  been added. This is an extensible protocol designed to use a server to
  manage encryption keys. :guilabel:`KMIP` has been added to the
  :menuselection:`System` menu options.

* Extending storage :ref:`Pools` has been reworked into a single
  :guilabel:`Add Vdevs` option and expanded to support adding
  multiple types of vdevs.

* :ref:`SMB sharing <Windows (SMB) Shares>` has been heavily reworked,
  with new preset configurations and support for alternate data streams,
  durable handles, and Apple-style character encoding. VFS objects have
  been replaced with share features that are enabled or disabled with
  checkboxes.

**Deprecated and Removed Features**

* Upgrading from legacy (9.2 or earlier) versions of FreeNAS has been
  removed from the installer.

* GELI encryption has been deprecated and replaced by native ZFS
  encryption. The |web-ui| remains backwards compatible with GELI
  encryption keys and passphrases.

* The *Legacy* replication method has been removed from
  :ref:`Advanced Replication Creation`.

**New or Updated Software**

* The OS has been updated to FreeBSD 12.

* :literal:`avahi` has replaced :literal:`mdnsresponder`.

* :literal:`collectd` is updated to version 5.9.

* :literal:`Samba` has been updated to version 4.11.2.

* :literal:`Sentry` has replaced the :literal:`Raven` Python module.

* TLS 1.3 support has been added.

* :literal:`nvmecontrol resv` has been added.

* :literal:`ipaddress` has replaced the deprecated :literal:`ipaddr`
  python module.

* Drivers for AQtion AQC107 chips and ASUS XG-C100C have been added.


**Miscellaneous UI Changes**

* The |web-ui| has been rebranded to TrueNAS Core or TrueNAS Enterprise.

* A compact view for the :ref:`Dashboard` has been added for displays
  with a resolution less than 1920x1080.

* Configuration options in the |web-ui| have been grouped together
  for convenience.

* :guilabel:`SAVE` and :guilabel:`SUBMIT` buttons have been
  reworked to be consistent.

* A dialog has been added to warn users when deleting datasets or shares
  that have been created by an outside resource, like TrueCommand or vCenter.

*Accounts*

* The :ref:`Groups` member management screen has been reworked to show
  more options at a time.

*System*

* :guilabel:`HTTPS Protocols`, with choices for which TLS
  versions to use, has been added to the :ref:`General` options.

* :guilabel:`Graphite Separate Instances` has been added to the
  :ref:`System Reporting` options.

* :guilabel:`DOWNLOAD PRIVATE KEY` and :guilabel:`DOWNLOAD PUBLIC KEY`
  buttons have been added to the :ref:`SSH Keypairs` options.

*Tasks*

* :guilabel:`Description` has been added to the
  :ref:`Init/Shutdown Scripts` options.

* :guilabel:`Full Filesystem Replication` has been added to
  :ref:`Advanced Replication Creation`.

* The :guilabel:`Restore` option has been added to
  :ref:`Replication Tasks`.

* The :guilabel:`Dry Run` and :guilabel:`Restore` task options have been
  added to :ref:`Cloud Sync Tasks`.

*Network*

* :menuselection:`Network` menu options have been reordered.

* :guilabel:`NetBIOS-NS` , :guilabel:`mDNS` , and
  :guilabel:`WS-Discovery` have been added to the
  :ref:`Global Configuration` options.

* :guilabel:`MTU` has been added as a column option to the
  Network :ref:`Interfaces` list.

* The :guilabel:`Password` field has been renamed to
  :guilabel:`IPMI Password Reset` and a :guilabel:`MANAGE`
  button has been added to the :ref:`IPMI` configuration screen.

*Storage*

* :guilabel:`Add Vdevs` and :guilabel:`Expand Pool` have been added to
  the :ref:`Pool <Pools>` operations menu.

* The :guilabel:`OVER PROVISION` button has been added to the
  :ref:`Disks` options.

*Sharing*

* :guilabel:`Purpose`, :guilabel:`Enable ACL`, :guilabel:`Export Recycle Bin`,
  :guilabel:`Enable Apple-style Character Encoding`,
  :guilabel:`Enable Alternate Data Streams`, :guilabel:`Enable SMB2/3 Durable Handles`,
  :guilabel:`Enable FSRVP`, and :guilabel:`Path Suffix` have been added and
  :guilabel:`VFS Objects, :guilabel:`Only Allow Guest Access`, and :guilabel:`Show Hidden Files`
  have been removed from the :ref:`SMB sharing <Windows (SMB) Shares>` options.


*Services*

* :guilabel:`Zeroconf share discovery` has been removed and
  :guilabel:`Enable Apple SMB2/3 Protocol Extensions` has been
  added to the :ref:`SMB` service options.

*Virtual Machines*

* :guilabel:`Cores` and :guilabel:`Threads` have been added to the
  :ref:`Virtual Machine <VMs>` options.

.. _Path and Name Lengths:

Path and Name Lengths
---------------------

#include snippets/pathlengths.rst


.. _Using the Web Interface:

Using the |Web-UI|
------------------

#include snippets/usingui.rst


.. index:: Hardware Recommendations
.. _Hardware Recommendations:

Hardware Recommendations
------------------------

%brand% |release| is based on FreeBSD 11.3 and supports the same
hardware found in the
`FreeBSD Hardware Compatibility List
<https://www.freebsd.org/releases/11.3R/hardware.html>`__.
Supported processors are listed in section
`2.1 amd64
<https://www.freebsd.org/releases/11.3R/hardware.html#proc>`__.
%brand% is only available for 64-bit processors. This architecture is
called *amd64* by AMD and *Intel 64* by Intel.

.. note:: %brand% boots from a GPT partition. This means that the
   system BIOS must be able to boot using either the legacy BIOS
   firmware interface or EFI.

Actual hardware requirements vary depending on the workflow of your
%brand% system. This section provides some starter guidelines. The
`FreeNAS® Hardware Forum
<https://www.ixsystems.com/community/forums/hardware-discussion/>`__
has performance tips from %brand% users and is a place to post
questions regarding the hardware best suited to meet specific
requirements.
`The Official FreeNAS® Hardware Guide
<https://www.ixsystems.com/blog/hardware-guide/>`__
gives in-depth recommendations for every component needed in a %brand% build.
`Building, Burn-In, and Testing your FreeNAS® system
<https://forums.freenas.org/index.php?threads/building-burn-in-and-testing-your-freenas-system.17750/>`__
has detailed instructions on testing new hardware.

.. note:: The %brand% team highly recommends `Western Digital Red
   <https://www.westerndigital.com/products/internal-drives/wd-red-hdd>`__ 
   NAS Disk Drives as the preferred storage drive of %brand%.

.. _RAM:

RAM
~~~

The best way to get the most out of a %brand% system is to install
as much RAM as possible. More RAM allows ZFS to provide better
performance. The
`iXsystems® Community Forums <https://www.ixsystems.com/community/>`__
provide anecdotal evidence from users on how much performance can be
gained by adding more RAM.

General guidelines for RAM:

* **A minimum of 8 GiB of RAM is required.**

  Additional features require additional RAM, and large amounts of
  storage require more RAM for cache. An old, somewhat overstated
  guideline is 1 GiB of RAM per terabyte of disk capacity.

* To use Active Directory with many users, add an additional 2 GiB of
  RAM for the winbind internal cache.

* For iSCSI, install at least 16 GiB of RAM if performance is not
  critical, or at least 32 GiB of RAM if good performance is a
  requirement.

* :ref:`Jails` are very memory-efficient, but can still use memory
  that would otherwise be available for ZFS. If the system will be
  running many jails, or a few resource-intensive jails, adding 1 to 4
  additional gigabytes of RAM can be helpful. This memory is shared by
  the host and will be used for ZFS when not being used by jails.

* :ref:`Virtual Machines <VMs>` require additional RAM beyond any
  amounts listed here. Memory used by virtual machines is not
  available to the host while the VM is running, and is not included
  in the amounts described above. For example, a system that will be
  running two VMs that each need 1 GiB of RAM requires an additional 2
  GiB of RAM.

* When installing %brand% on a headless system, disable the shared
  memory settings for the video card in the BIOS.

* For ZFS deduplication, ensure the system has at least 5 GiB of RAM
  per terabyte of storage to be deduplicated.


If the hardware supports it, install ECC RAM. While more expensive,
ECC RAM is highly recommended as it prevents in-flight corruption of
data before the error-correcting properties of ZFS come into play,
thus providing consistency for the checksumming and parity
calculations performed by ZFS. If your data is important, use ECC RAM.
This
`Case Study
<http://research.cs.wisc.edu/adsl/Publications/zfs-corruption-fast10.pdf>`__
describes the risks associated with memory corruption.

Do not use %brand% to store data without at least 8 GiB of RAM. Many
users expect %brand% to function with less memory, just at reduced
performance.  The bottom line is that these minimums are based on
feedback from many users. Requests for help in the forums or IRC are
sometimes ignored when the installed system does not have at least 8
GiB of RAM because of the abundance of information that %brand% may
not behave properly with less memory.


.. _The Operating System Device:

The Operating System Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The %brand% operating system is installed to at least one device that
is separate from the storage disks. The device can be an SSD, a small
hard drive, or a |usb-stick|.

.. note:: To write the installation file to a |usb-stick|, **two** USB
   ports are needed, each with an inserted USB device. One |usb-stick|
   contains the installer, while the other |usb-stick| is the
   destination for the %brand% installation. Be careful to select
   the correct USB device for the %brand% installation. %brand% cannot
   be installed onto the same device that contains the installer.
   After installation, remove the installer |usb-stick|. It might also
   be necessary to adjust the BIOS configuration to boot from the new
   %brand% |os-device|.

When determining the type and size of the target device where %brand%
is to be installed, keep these points in mind:

- The absolute *bare minimum* size is 8 GiB. That does not provide
  much room. The *recommended* minimum is 16 GiB. This provides room
  for the operating system and several boot environments created by
  updates. More space provides room for more boot environments and 32
  GiB or more is preferred.

- SSDs (Solid State Disks) are fast and reliable, and make very good
  %brand% operating system devices. Their one disadvantage is that
  they require a disk connection which might be needed for storage
  disks.

  Even a relatively large SSD (120 or 128 GiB) is useful as a boot
  device. While it might appear that the unused space is wasted, that
  space is instead used internally by the SSD for wear leveling. This
  makes the SSD last longer and provides greater reliability.

- When planning to add your own boot environments, budget about 1 GiB
  of storage per boot environment. Consider deleting older boot
  environments after making sure they are no longer needed. Boot
  environments can be created and deleted using
  :menuselection:`System --> Boot`.

- Use quality, name-brand |usb-sticks|, as ZFS will quickly reveal
  errors on cheap, poorly-made sticks.

- For a more reliable boot disk, use two identical devices and select
  them both during the installation. This will create a mirrored boot
  device.

.. note:: Current versions of %brand% run directly from the operating
   system device. Early versions of %brand% ran from RAM, but that has
   not been the case for years.


.. _Storage Disks and Controllers:

Storage Disks and Controllers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Disk section
<https://www.freebsd.org/releases/11.3R/hardware.html#disk>`__
of the FreeBSD Hardware List shows supported disk controllers.

%brand% supports hot-pluggable SATA drives when AHCI is enabled in the
BIOS. The %brand% team highly recommends `Western Digital Red
<https://www.westerndigital.com/products/internal-drives/wd-red-hdd>`__ 
NAS Disk Drives as the preferred storage drive of %brand%.

Suggestions for testing disks can be found in this
`forum post
<https://forums.freenas.org/index.php?threads/checking-new-hdds-in-raid.12082/#post-55936>`__.
`badblocks <https://linux.die.net/man/8/badblocks>`__
is installed with %brand% for disk testing.

ZFS
`Disk Space Requirements for ZFS Storage Pools <https://docs.oracle.com/cd/E19253-01/819-5461/6n7ht6r12/index.html>`__
recommends a minimum of 16 GiB of disk space. %brand% allocates 2 GiB
of swap space on each drive.

New ZFS users purchasing hardware should read through
`ZFS Storage Pools Recommendations
<https://web.archive.org/web/20161028084224/http://www.solarisinternals.com/wiki/index.php/ZFS_Best_Practices_Guide#ZFS_Storage_Pools_Recommendations>`__
first.

ZFS *vdevs*, groups of disks that act like a single device, can be
created using disks of different sizes.  However, the capacity
available on each disk is limited to the same capacity as the smallest
disk in the group. For example, a vdev with one 2 TiB and two 4 TiB
disks will only be able to use 2 TiB of space on each disk. In
general, use disks that are the same size for the best space usage and
performance.

The
`ZFS Drive Size and Cost Comparison spreadsheet
<https://forums.freenas.org/index.php?threads/zfs-drive-size-and-cost-comparison-spreadsheet.38092/>`__
is available to compare usable space provided by different quantities
and sizes of disks.


.. _Network Interfaces:

Network Interfaces
~~~~~~~~~~~~~~~~~~

The `Ethernet section
<https://www.freebsd.org/releases/11.3R/hardware.html#ethernet>`__
of the FreeBSD Hardware Notes indicates which interfaces are supported
by each driver. While many interfaces are supported, %brand% users
have seen the best performance from Intel and Chelsio interfaces, so
consider these brands when purchasing a new NIC. Realtek cards often
perform poorly under CPU load as interfaces with these chipsets do not
provide their own processors.

At a minimum, a GigE interface is recommended. While GigE interfaces
and switches are affordable for home use, modern disks can easily
saturate their 110 MiB/s throughput. For higher network throughput,
multiple GigE cards can be bonded together using the LACP type of
:ref:`Link Aggregations`. The Ethernet switch must support LACP, which
means a more expensive managed switch is required.

When network performance is a requirement and there is some money to
spend, use 10 GigE interfaces and a managed switch. Managed switches
with support for LACP and jumbo frames are preferred, as both can be
used to increase network throughput. Refer to the
`10 Gig Networking Primer
<https://forums.freenas.org/index.php?threads/10-gig-networking-primer.25749/>`__
for more information.

.. note:: At present, these are not supported: InfiniBand,
   FibreChannel over Ethernet, or wireless interfaces.

Both hardware and the type of shares can affect network performance.
On the same hardware, SMB is slower than FTP or NFS because Samba is
`single-threaded
<https://www.samba.org/samba/docs/old/Samba3-Developers-Guide/architecture.html>`__.
So a fast CPU can help with SMB performance.

Wake on LAN (WOL) support depends on the FreeBSD driver for the
interface. If the driver supports WOL, it can be enabled using
`ifconfig(8) <https://www.freebsd.org/cgi/man.cgi?query=ifconfig>`__. To
determine if WOL is supported on a particular interface, use the
interface name with the following command. In this example, the
capabilities line indicates that WOL is supported for the *igb0*
interface:

.. code-block:: none

   [root@freenas ~]# ifconfig -m igb0
   igb0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> metric 0 mtu 1500
           options=6403bb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,VLAN_HWCSUM,
   TSO4,TSO6,VLAN_HWTSO,RXCSUM_IPV6,TXCSUM_IPV6>
           capabilities=653fbb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,
   VLAN_HWCSUM,TSO4,TSO6,LRO,WOL_UCAST,WOL_MCAST,WOL_MAGIC,VLAN_HWFILTER,VLAN_HWTSO,
   RXCSUM_IPV6,TXCSUM_IPV6>


If WOL support is shown but not working for a particular interface,
create a bug report using the instructions in :ref:`Support`.


.. _Getting Started with ZFS:

Getting Started with ZFS
------------------------

Readers new to ZFS should take a moment to read the :ref:`ZFS Primer`.
