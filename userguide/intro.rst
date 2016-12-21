%brand% is © 2011-2016 iXsystems

%brand% and the %brand% logo are registered trademarks of iXsystems

FreeBSD\ :sup:`®` is a registered trademark of the FreeBSD Foundation

Written by users of the %brand% network-attached storage operating
system.

Version |release|

Copyright © 2011-2016
`iXsystems <https://www.ixsystems.com/>`_


.. raw:: latex

   \par--TABLEOFCONTENTS--\par
   \pagestyle{frontmatter}
   \section*{Welcome}\addcontentsline{toc}{section}{Welcome}


This Guide covers the installation and use of %brand% |release|.

The %brand% User Guide is a work in progress and relies on the
contributions of many individuals. If you are interested in helping us
to improve the Guide, read the instructions in the `README
<https://github.com/freenas/freenas/blob/master/docs/userguide/README.md>`_.
IRC Freenode users are welcome to join the *#freenas* channel
where you will find other %brand% users.

The %brand% User Guide is freely available for sharing and
redistribution under the terms of the
`Creative Commons Attribution
License <https://creativecommons.org/licenses/by/3.0/>`_.
This means that you have permission to copy, distribute, translate,
and adapt the work as long as you attribute iXsystems as the original
source of the Guide.


#include snippets/trademarks.rst


.. raw:: latex

   \pagebreak
   \section*{Typographic Conventions}%WB
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
`2-clause BSD license <https://opensource.org/licenses/BSD-2-Clause>`_.
A NAS has an operating system optimized for file storage and sharing.

%brand% provides a browser-based, graphical configuration interface.
The built-in networking protocols provide storage access to multiple
operating systems. A plugin system is provided for extending the
built-in features by installing additional software.


.. _What Is New in |version|:

What Is New in |version|
------------------------

* The installer now provides an option to install the updated system
  into a new boot environment instead of formatting the boot device.
  This makes updates safer and testing different versions more
  convenient.

* The installer warns the user if the computer has less than the
  minimum recommended amount of memory.

* The installer offers an option to set up either UEFI or traditional
  BIOS/MBR booting.

* A new :guilabel:`Setup mode` drop-down menu has been added to
  :menuselection:`Storage --> Replication Tasks --> Add Replication`.

* A new FQDN checkbox has been added to the :guilabel:`Advanced`
  :ref:`System` settings. Checking this causes fully-qualified domain
  names to be included in syslogd output, making it easier to identify
  individual systems when groups of computers have similar hostnames.

* A :guilabel:`Manual Update` button has been added to the
  :guilabel:`Update` screen in :ref:`System`. Update files can be
  applied manually with this method.

* An :guilabel:`Auxiliary Parameters` field has been added to
  :menuselection:`Sharing --> Apple (AFP) --> Add Apple (AFP) Share`.

* Samba has been updated to
  `4.4.5 <https://www.samba.org/samba/history/samba-4.4.5.html>`_.

* Modifying network settings only affects the changed network
  components, avoiding the disruption of restarting all networking.

* Chelsio T3/T4/T5 network cards can now take advantage of TCP Offload
  Engine (TOE) for improved network performance. Add *toe* to the
  Options field of the interface to enable the feature.

* LDAP failing to bind to the domain on startup causes an alert.

* A new script for backing up Samba4 domain controller settings has
  been added. See :ref:`Samba Domain Controller Backup`.

* The UPS shutdown command can now be customized.

* :ref:`freenas-debug` can now include GRUB configuration information.

* The php-virtualbox jail template has been removed.

* `iohyve <https://github.com/pr1ntf/iohyve>`_ has been updated to
  version 0.7.7.

* Additional disks statistics for percent busy, latency, operations
  per second, and pending I/O requests have been added to
  :ref:`Reporting`.

* A new :ref:`API <Using the API>` has been added. The old API is
  still present for compatibility.


#ifdef commented
.. _What Has Changed Since |version|:

What Has Changed Since |version|
--------------------------------

%brand% uses a "rolling release" model instead of point releases. The
:ref:`Update` mechanism makes it easy to keep up-to-date with the
latest security fixes, bug fixes, and new features. Some updates
affect the user interface, so this section lists any functional
changes that have occurred since |version| was released.

.. note:: The screenshots in this documentation assume that the system
   has been fully updated to the latest STABLE version of %brand%
   |version|. If a screen on your system is not the same as shown in
   this guide, make sure that all outstanding updates are applied.
#endif commented


.. index:: Hardware Recommendations
.. _Hardware Recommendations:

Hardware Recommendations
------------------------

%brand% |release| is based on FreeBSD 10.3 and supports the same
hardware found in the
`FreeBSD Hardware Compatibility List
<http://www.freebsd.org/releases/10.3R/hardware.html>`__.
Supported processors are listed in section
`2.1 amd64
<https://www.freebsd.org/releases/10.3R/hardware.html#proc>`_.
%brand% is only available for 64-bit processors. This architecture is
called *amd64* by AMD and *Intel 64* by Intel.

.. note:: %brand% boots from a GPT partition. This means that the
   system BIOS must be able to boot using either the legacy BIOS
   firmware interface or EFI.

Actual hardware requirements vary depending on the usage of the
%brand% system. This section provides some starter guidelines. The
`FreeNAS® Hardware Forum
<https://forums.freenas.org/index.php?forums/hardware.18/>`_
has performance tips from %brand% users and is a place to post
questions regarding the hardware best suited to meet specific
requirements.
`Hardware Recommendations
<https://forums.freenas.org/index.php?threads/hardware-recommendations-read-this-first.23069/>`__
gives detailed recommendations for system components, with the
`FreeNAS® Quick Hardware Guide
<https://forums.freenas.org/index.php?resources/freenas-quick-hardware-guide.7>`__
providing short lists of components for various configurations.
`Building, Burn-In, and Testing your FreeNAS® system
<https://forums.freenas.org/index.php?threads/building-burn-in-and-testing-your-freenas-system.17750/>`_
has detailed instructions on testing new hardware.


.. _RAM:

RAM
~~~

The best way to get the most out of a %brand% system is to install
as much RAM as possible. The recommended minimum is 8 GB of RAM. The
more RAM, the better the performance, and the
`FreeNAS® Forums <https://forums.freenas.org/index.php>`_
provide anecdotal evidence from users on how much performance is
gained by adding more RAM.

Depending upon the use case, your system may require more RAM. Here
are some general rules of thumb:

* To use Active Directory with many users, add an additional 2 GB of
  RAM for winbind's internal cache.

* For iSCSI, install at least 16 GB of RAM if performance is not
  critical, or at least 32 GB of RAM if good performance is a
  requirement.

* When installing %brand% on a headless system, disable the shared
  memory settings for the video card in the BIOS.

* To use ZFS deduplication, ensure the system has at least 5 GB of RAM
  per TB of storage to be deduplicated.


If the hardware supports it and the budget allows for it, install ECC
RAM. While more expensive, ECC RAM is highly recommended as it
prevents in-flight corruption of data before the error-correcting
properties of ZFS come into play, thus providing consistency for the
checksumming and parity calculations performed by ZFS. If you consider
your data important, use ECC RAM. This
`Case Study
<http://research.cs.wisc.edu/adsl/Publications/zfs-corruption-fast10.pdf>`_
describes the risks associated with memory corruption.

Unless the system has at least 8 GB of RAM, consider adding RAM before
using %brand% to store data. Many users expect %brand% to function
with less memory, just at reduced performance.  The bottom line is
that these minimums are based on feedback from many users. Requests
for help in the forums or IRC are sometimes ignored when the installed
system does not have at least 8 GB of RAM because of the abundance of
information that %brand% may not behave properly with less memory.


.. _The Operating System Device:

The Operating System Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The %brand% operating system is installed to at least one device that
is separate from the storage disks. The device can be a USB stick,
SSD, compact flash, or DOM (Disk on Module). Installation to a hard
drive is discouraged as that drive is then not available for data
storage.

.. note:: To write the installation file to a USB stick, **two** USB
   ports are needed, each with an inserted USB device. One USB stick
   contains the installer.  The other USB stick is the destination for
   the %brand% installation. Take care to select the correct USB
   device for the %brand% installation. It is **not** possible to
   install %brand% onto the same USB stick containing the installer.
   After installation, remove the installer USB stick. It might also
   be necessary to adjust the BIOS configuration to boot from the new
   %brand% USB stick.

When determining the type and size of the target device where %brand%
will be installed, keep these points in mind:

- the *bare minimum* size is 8 GB. This provides room for the
  operating system and several boot environments. Since each update
  creates a boot environment, this is the *recommended* minimum. 32 GB
  provides room for more boot environments.

- if you plan to make your own boot environments, budget about 1 GB of
  storage per boot environment. Consider deleting older boot
  environments after making sure they are no longer needed. Boot
  environments can be created and deleted using
  :menuselection:`System --> Boot`.

- use quality, name-brand USB sticks, as ZFS will quickly reveal
  errors on cheap, poorly-made sticks.

- for a more reliable boot disk, use two identical devices and select
  them both during the installation. This will create a mirrored boot
  device.


.. _Storage Disks and Controllers:

Storage Disks and Controllers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Disk section
<http://www.freebsd.org/releases/10.3R/hardware.html#DISK>`_
of the FreeBSD Hardware List lists the supported disk controllers. In
addition, support for 3ware 6 Gbps RAID controllers has been added
along with the CLI utility :command:`tw_cli` for managing 3ware RAID
controllers.

%brand% supports hot pluggable drives. Using this feature requires
enabling AHCI in the BIOS.

Reliable disk alerting and immediate reporting of a failed drive can
be obtained by using an HBA such as an Avago MegaRAID controller or a
3Ware twa-compatible controller.

Suggestions for testing disks before adding them to a RAID array can
be found in this
`forum post
<https://forums.freenas.org/index.php?threads/checking-new-hdds-in-raid.12082/#post-55936>`__.
Additionally, `badblocks <https://linux.die.net/man/8/badblocks>`_ is
installed with %brand% for testing disks.

If the budget allows optimization of the disk subsystem, consider the
read/write needs and RAID requirements:

* For steady, non-contiguous writes, use disks with low seek times.
  Examples are 10K or 15K SAS drives which cost about $1/GB. An
  example configuration would be six 600 GB 15K SAS drives in a RAID
  10 which would yield 1.8 TB of usable space, or eight 600 GB 15K SAS
  drives in a RAID 10 which would yield 2.4 TB of usable space.

* 7200 RPM SATA disks are designed for single-user sequential I/O and
  are not a good choice for multi-user writes.

When high performance is a key requirement and budget permits,
consider a
`Fusion-I/O card <http://www.fusionio.com/products/>`_
which is optimized for massive random access. These cards are
expensive and are suited for high-end systems that demand performance.
A Fusion-I/O card can be formatted with a filesystem and used as
direct storage; when used this way, it does not have the write issues
typically associated with a flash device. A Fusion-I/O card can also
be used as a cache device when your ZFS dataset size is bigger than
your RAM. Due to the increased throughput, systems running these cards
typically use multiple 10 GigE network interfaces.

For ZFS,
`Disk Space Requirements for ZFS Storage Pools
<http://docs.oracle.com/cd/E19253-01/819-5461/6n7ht6r12/index.html>`_
recommends a minimum of 16 GB of disk space. Due to the way that ZFS
creates swap,
**it is not possible to format less than 3 GB of space with ZFS**.
However, on a drive that is below the minimum recommended size, a fair
amount of storage space is lost to swap: for example, on a 4 GB
drive, 2 GB will be reserved for swap.

Users new to ZFS who are purchasing hardware should read through
`ZFS Storage Pools Recommendations
<http://www.solarisinternals.com/wiki/index.php/ZFS_Best_Practices_Guide#ZFS_Storage_Pools_Recommendations>`_
first.

ZFS *vdevs*, groups of disks that act like a single device, can be
created using disks of different sizes.  However, the capacity
available on each disk is limited to the same capacity as the smallest
disk in the group. For example, a *vdev* with one 2 TB and two 4 TB
disks will only be able to use 2 TB of space on each disk. In general,
use disks that are the same size for the best space usage and
performance.


.. _Network Interfaces:

Network Interfaces
~~~~~~~~~~~~~~~~~~

The `Ethernet section
<http://www.freebsd.org/releases/10.3R/hardware.html#ethernet>`_
of the FreeBSD Hardware Notes indicates which interfaces are supported
by each driver. While many interfaces are supported, %brand% users
have seen the best performance from Intel and Chelsio interfaces, so
consider these brands when purchasing a new NIC. Realtek cards often
perform poorly under CPU load as interfaces with these chipsets do not
provide their own processors.

At a minimum, a GigE interface is recommended. While GigE interfaces
and switches are affordable for home use, modern disks can easily
saturate their 110 MB/s throughput. For higher network throughput,
multiple GigE cards can be bonded together using the LACP type of
:ref:`Link Aggregations`. The Ethernet switch must support LACP, which
means a more expensive managed switch is required.

When network performance is a requirement and there is some money to
spend, use 10 GigE interfaces and a managed switch. Managed switches
with support for LACP and jumbo frames are preferred, as both can be
used to increase network throughput. Refer to the
`10 Gig Networking Primer
<https://forums.freenas.org/index.php?threads/10-gig-networking-primer.25749/>`_
for more information.

.. note:: At present, these are not supported: InfiniBand,
   FibreChannel over Ethernet, or wireless interfaces.

Both hardware and the type of shares can affect network performance.
On the same hardware, SMB is slower than FTP or NFS because Samba is
`single-threaded
<https://www.samba.org/samba/docs/man/Samba-Developers-Guide/architecture.html>`_.
So a fast CPU can help with SMB performance.

Wake on LAN (WOL) support depends on the FreeBSD driver for the
interface. If the driver supports WOL, it can be enabled using
`ifconfig(8) <http://www.freebsd.org/cgi/man.cgi?query=ifconfig>`_. To
determine if WOL is supported on a particular interface, use the
interface name with the following command. In this example, the
capabilities line indicates that WOL is supported for the *re0*
interface:

.. code-block:: none

 ifconfig -m re0
 re0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> metric 0 mtu 1500
         options=42098<VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,WOL_MAGIC,VLAN_HWTSO>
         capabilities=5399b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,TSO4,WOL_UCAST,WOL_MCAST, WOL_MAGIC,VLAN_HWFILTER,VLAN_H WTSO>


If WOL support is shown but not working for a particular interface,
create a bug report using the instructions in :ref:`Support`.


.. _Getting Started with ZFS:

Getting Started with ZFS
------------------------

Readers new to ZFS should take a moment to read the :ref:`ZFS Primer`.
