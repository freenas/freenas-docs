%brand% is © 2011-2017 iXsystems

%brand% and the %brand% logo are registered trademarks of iXsystems

FreeBSD\ :sup:`®` is a registered trademark of the FreeBSD Foundation

Written by users of the %brand% network-attached storage operating
system.

Version |release|

Copyright © 2011-2017
`iXsystems <https://www.ixsystems.com/>`_


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
License <https://creativecommons.org/licenses/by/3.0/>`_.
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
`2-clause BSD license <https://opensource.org/licenses/BSD-2-Clause>`_.
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
features, and version updates to the operating system, base applications,
and drivers. Users are encouraged to :ref:`Update` to this release in
order to take advantage of these improvements and bug fixes.

The following base applications and drivers have been updated or added:

* The base operating system has been updated to FreeBSD 11.1-STABLE.
  This brings in many new
  `features and drivers
  <https://www.freebsd.org/releases/11.1R/relnotes.html>`__.

* There have been many improvements to OpenZFS. Users should notice a
  significant speed difference when listing a large number of snapshots
  or when deleting multiple snapshots and large files.

* The Dojo Tookit has been updated to version 1.12.2.

* OpenVPN has been updated to version `2.4.3
  <https://github.com/OpenVPN/openvpn/blob/release/2.4/Changes.rst#version-243>`__.

* `Iperf version 3.2
  <http://software.es.net/iperf/>`__ has been added. To use this version,
  specify :command:`iperf3` instead of :command:`iperf`.

* Iocage has been updated to version 0.9.9.2.

* `mmv <https://packages.debian.org/unstable/utils/mmv>`__
  has been added. It can be used from the command line to safely move or
  copy multiple files using patterns, without any unexpected deletion of
  files due to target name collisions.

* The hardware watchdog has been reenabled for recent firmware versions
  of AsrockRack C2750D4I. The BMC bug which required watchdog to be
  disabled is resolved with the 00.30.00 or newer BMC firmware version.

The following major features are new in this version:

* :ref:`Cloud Credentials` has been added to :ref:`System`. This can be
  used to provide a secure connection to a cloud services providers.
  Supported services include Amazon S3, Backblaze B2, and Google Cloud
  Storage.

* :ref:`Cloud Sync` has been added to :ref:`Tasks` and can be used to
  synchronize files or directories to remote cloud storage providers.

* :ref:`VMs` have received significant improvements, including:

  * support for non-US keyboards.

  * the ability to specify the NIC used by the VM as well as the MAC
    address for the VM NIC. These options can be set using
    :menuselection:`VMs --> Devices --> Network Interface`.

  * the ability to specify the sector size used by the emulated disk has
    been added to :menuselection:`VMs --> Devices --> Disk`.

  * the ability to edit the VNC screen resolution, select the IP address
    to bind to, set the VNC password, and select the option to use the Web
    version of VNC. These options can be set using
    :menuselection:`VMs --> Devices --> VNC`.

The following screens have changed:

* The :guilabel:`Enable Console Menu` in
  :menuselection:`System --> Advanced` has been renamed to
  :guilabel:`Show Text Console Without Password Prompt`.

* The :guilabel:`Send Test Alert` button has been added to
  :menuselection:`System --> Alert Services --> Edit`.

* The :guilabel:`Subject Alternate Names` field has been added to
  :menuselection:`System --> CAs --> Create Internal CA`,
  :menuselection:`System --> CAs --> Create Intermediate CA`,
  :menuselection:`System --> Certificates --> Create Internal Certificate`,
  and
  :menuselection:`System --> Certificates --> Create Certificate Signing Request`
  screens.

* An :guilabel:`Enabled` checkbox has been added to
  :menuselection:`Tasks --> Init/Shutdown Scripts`.

* The :guilabel:`Additional domains` field has been added to
  :menuselection:`Network --> Global Configuration`. This allows up to
  six additional DNS search domains with the caveat that adding more
  domains may negatively impact DNS lookup time.

* The :guilabel:`Priority Code Point (CoS)` field has been added to
  :menuselection:`Network --> VLANs --> Add VLAN`. This can be useful in
  datacenter environments to classify storage traffic on a given VLAN
  interface using IEEE 802.1p Class of Service (COS).

* The :guilabel:`Read-Only` drop-down menu has been added to
  :menuselection:`Storage --> Datasets --> Add Dataset --> Advanced Mode`.

* The :guilabel:`CheckIP Server SSL`, :guilabel:`CheckIP Server`,
  :guilabel:`CheckIP Path`, and :guilabel:`Use SSL` fields have been
  added to :menuselection:`Services --> DDNS`. The
  :guilabel:`Forced update period` and :guilabel:`Auxiliary parameters`
  fields have been removed. In addition, several dozen DDNS providers
  have been added to the :guilabel:`Provider` drop-down menu.

* The :guilabel:`Certificate` drop-down menu has been added to
  :menuselection:`Services --> S3` in order to configure encrypted S3
  connections.

* The :guilabel:`Log Level` drop-down menu has been added to
  :menuselection:`Services --> SNMP`. It defaults to the :guilabel:`Error`
  log level.

* The :guilabel:`No Communication Warning Time` field has been added to
  :menuselection:`Services --> UPS`. This can be used to configure the
  frequency of email notifications during the loss of UPS communications.

* The :guilabel:`No Authentication` choice has been added to the
  :menuselection:`Services --> WebDAV --> HTTP Authentication`
  drop-down menu.

.. index:: Path and Name Lengths
.. _Path and Name Lengths:

Path and Name Lengths
---------------------

#include snippets/pathlengths.rst


.. index:: Hardware Recommendations
.. _Hardware Recommendations:

Hardware Recommendations
------------------------

%brand% |release| is based on FreeBSD 11 and supports the same
hardware found in the
`FreeBSD Hardware Compatibility List
<http://www.freebsd.org/releases/11.0R/hardware.html>`__.
Supported processors are listed in section
`2.1 amd64
<https://www.freebsd.org/releases/11.0R/hardware.html#proc>`_.
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
<https://forums.freenas.org/index.php?resources/hardware-recommendations-guide.12/>`__
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
<http://www.freebsd.org/releases/11.0R/hardware.html#DISK>`_
of the FreeBSD Hardware List lists the supported disk controllers. In
addition, support for 3ware 6 Gbps RAID controllers has been added
along with the CLI utility :command:`tw_cli` for managing 3ware RAID
controllers.

%brand% supports hot pluggable drives. Using this feature requires
enabling AHCI in the BIOS.

Reliable disk alerting and immediate reporting of a failed drive can
be obtained by using an HBA such as an Avago MegaRAID controller or a
3Ware twa-compatible controller.

.. note:: Upgrading the firmware of Avago SAS HBAs to the latest
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
   driver can be used instead by removing the  loader
   :ref:`Tunable <Tunables>`: :literal:`hw.mfi.mrsas_enable` or
   setting the :guilabel:`Value` to *0*.


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
<https://web.archive.org/web/20161028084224/http://www.solarisinternals.com/wiki/index.php/ZFS_Best_Practices_Guide#ZFS_Storage_Pools_Recommendations>`_
first.

ZFS *vdevs*, groups of disks that act like a single device, can be
created using disks of different sizes.  However, the capacity
available on each disk is limited to the same capacity as the smallest
disk in the group. For example, a vdev with one 2 TB and two 4 TB
disks will only be able to use 2 TB of space on each disk. In general,
use disks that are the same size for the best space usage and
performance.

The
`ZFS Drive Size and Cost Comparison spreadsheet
<https://forums.freenas.org/index.php?threads/zfs-drive-size-and-cost-comparison-spreadsheet.38092/>`_
is available to compare usable space provided by different quantities
and sizes of disks.


.. _Network Interfaces:

Network Interfaces
~~~~~~~~~~~~~~~~~~

The `Ethernet section
<http://www.freebsd.org/releases/11.0R/hardware.html#ethernet>`_
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
