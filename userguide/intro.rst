%brand% is © 2011-|copyright-year| iXsystems

%brand% and the %brand% logo are registered trademarks of iXsystems

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
IRC Freenode users are welcome to join the *#freenas* channel
where you will find other %brand% users.

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


.. _New Features in |release|:

New Features in |release|
-------------------------

%brand%  |release| is a feature release, which includes several new
significant features, many improvements and bug fixes to existing
features, and version updates to the operating system, base
applications, and drivers. Users are encouraged to :ref:`Update` to
this release in order to take advantage of these improvements and bug
fixes.

These major features are new in this version:


This software has been added or updated:


These screen options have changed:

* :guilabel:`IPMI SEL Low Space Left` and :guilabel:`IPMI System Event`
  fields have been added to
  :menuselection:`System --> Alerts`.

.. index:: Path and Name Lengths
.. _Path and Name Lengths:

Path and Name Lengths
---------------------

#include snippets/pathlengths.rst


.. index:: Hardware Recommendations
.. _Hardware Recommendations:

Hardware Recommendations
------------------------

%brand% |release| is based on FreeBSD 11.2 and supports the same
hardware found in the
`FreeBSD Hardware Compatibility List
<https://www.freebsd.org/releases/11.2R/hardware.html>`__.
Supported processors are listed in section
`2.1 amd64
<https://www.freebsd.org/releases/11.2R/hardware.html#proc>`__.
%brand% is only available for 64-bit processors. This architecture is
called *amd64* by AMD and *Intel 64* by Intel.

.. note:: %brand% boots from a GPT partition. This means that the
   system BIOS must be able to boot using either the legacy BIOS
   firmware interface or EFI.

Actual hardware requirements vary depending on the usage of the
%brand% system. This section provides some starter guidelines. The
`FreeNAS® Hardware Forum
<https://forums.freenas.org/index.php?forums/hardware.18/>`__
has performance tips from %brand% users and is a place to post
questions regarding the hardware best suited to meet specific
requirements.
`Hardware Recommendations
<https://forums.freenas.org/index.php?resources/hardware-recommendations-guide.12/>`__
gives detailed recommendations for system components, with the
`FreeNAS® Quick Hardware Guide
<https://forums.freenas.org/index.php?resources/freenas%C2%AE-quick-hardware-guide.7/>`__
providing short lists of components for various configurations.
`Building, Burn-In, and Testing your FreeNAS® system
<https://forums.freenas.org/index.php?threads/building-burn-in-and-testing-your-freenas-system.17750/>`__
has detailed instructions on testing new hardware.


.. _RAM:

RAM
~~~

The best way to get the most out of a %brand% system is to install
as much RAM as possible. More RAM allows ZFS to provide better
performance. The
`FreeNAS® Forums <https://forums.freenas.org/index.php>`__
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
GiB of RAM because of the abundance of information that %brand% may not
behave properly with less memory.


.. _The Operating System Device:

The Operating System Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The %brand% operating system is installed to at least one device that
is separate from the storage disks. The device can be a SSD, USB
memory stick, or DOM (Disk on Module). Installation to a hard drive is
discouraged as that drive is then not available for data storage.

.. note:: To write the installation file to a USB stick, **two** USB
   ports are needed, each with an inserted USB device. One USB stick
   contains the installer, while the other USB stick is the
   destination for the %brand% installation. Be careful to select
   the correct USB device for the %brand% installation. %brand% cannot
   be installed onto the same device that contains the installer.
   After installation, remove the installer USB stick. It might also
   be necessary to adjust the BIOS configuration to boot from the new
   %brand% boot device.

When determining the type and size of the target device where %brand%
is to be installed, keep these points in mind:

- The absolute *bare minimum* size is 8 GiB. That does not provide much
  room. The *recommended* minimum is 16 GiB. This provides room for the
  operating system and several boot environments created by updates.
  More space provides room for more boot environments and 32 GiB or
  more is preferred.

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

- Use quality, name-brand USB sticks, as ZFS will quickly reveal
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
<https://www.freebsd.org/releases/11.2R/hardware.html#disk>`__
of the FreeBSD Hardware List lists the supported disk controllers. In
addition, support for 3ware 6 Gbps RAID controllers has been added
along with the CLI utility :command:`tw_cli` for managing 3ware RAID
controllers.

%brand% supports hot pluggable drives. Using this feature requires
enabling AHCI in the BIOS.

Reliable disk alerting and immediate reporting of a failed drive can
be obtained by using an HBA such as an Broadcom MegaRAID controller or
a 3Ware twa-compatible controller.

.. note:: Upgrading the firmware of Broadcom SAS HBAs to the latest
   version is recommended.

.. index:: Highpoint RAID

Some Highpoint RAID controllers do not support pass-through of
S.M.A.R.T. data or other disk information, potentially including disk
serial numbers. It is best to use a different disk controller with
%brand%.


.. index:: Dell PERC H330, Dell PERC H730

.. note:: The system is configured to prefer the
   `mrsas(4) <https://www.freebsd.org/cgi/man.cgi?query=mrsas>`__
   driver for controller cards like the Dell PERC H330 and H730 which
   are supported by several drivers. Although not recommended, the
   `mfi(4) <https://www.freebsd.org/cgi/man.cgi?query=mfi>`__
   driver can be used instead by removing the loader
   :ref:`Tunable <Tunables>`: :literal:`hw.mfi.mrsas_enable` or
   setting the :guilabel:`Value` to *0*.


Suggestions for testing disks before adding them to a RAID array can
be found in this
`forum post
<https://forums.freenas.org/index.php?threads/checking-new-hdds-in-raid.12082/#post-55936>`__.
Additionally, `badblocks <https://linux.die.net/man/8/badblocks>`__ is
installed with %brand% for testing disks.

If the budget allows optimization of the disk subsystem, consider the
read/write needs and RAID requirements:

* For steady, non-contiguous writes, use disks with low seek times.
  Examples are 10K or 15K SAS drives which cost about $1/GiB. An
  example configuration would be six 600 GiB 15K SAS drives in a RAID
  10 which would yield 1.8 TiB of usable space, or eight 600 GiB 15K SAS
  drives in a RAID 10 which would yield 2.4 TiB of usable space.

For ZFS,
`Disk Space Requirements for ZFS Storage Pools
<https://docs.oracle.com/cd/E19253-01/819-5461/6n7ht6r12/index.html>`__
recommends a minimum of 16 GiB of disk space. %brand% allocates 2 GiB
of swap space on each drive. Combined with ZFS space requirements,
this means that
**it is not possible to format drives smaller than 3 GiB**.
Drives larger than 3 GiB but smaller than the minimum recommended
capacity might be usable but lose a significant portion of storage
space to swap allocation. For example, a 4 GiB drive only has 2 GiB of
available space after swap allocation.


New ZFS users who are purchasing hardware should read through
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
<https://www.freebsd.org/releases/11.2R/hardware.html#ethernet>`__
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
